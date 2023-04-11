from celery import Celery, Task
from .__version__ import __version__, __url__, __license__
from EVECelery.tasks.BaseTasks.TaskBase import TaskBase
from EVECelery.tasks.Alliance import *
from EVECelery.clients.ClientRabbitMQ import ClientRabbitMQ
from EVECelery.clients.ClientRedis import ClientRedisResultBackend
import os
from typing import Optional
from EVECelery.utils.Singleton import Singleton
import random


class EVECeleryWorker(metaclass=Singleton):
    """Celery worker server wrapper.
    Creating an instance of this class creates a celery app and registers the default tasks.

    :param broker_user: RabbitMQ user
    :param broker_password: RabbitMQ password
    :param broker_host: RabbitMQ hostname
    :param broker_port: RabbitMQ port - normally 5672
    :param broker_vhost: RabbitMQ vhost - namespace for all EVECelery queues
    :param result_user: Redis user - normally "default" if not explicitly configured
    :param result_password: Redis password
    :param result_host: Redis hostname
    :param result_port: Redis port - normally 6379
    :param result_db: Redis db - normally 0 for the default db
    :param queue_prefix: Prefix to add to all generated ESI queue names
    """

    def __init__(self, broker_user: Optional[str] = None, broker_password: Optional[str] = None,
                 broker_host: Optional[str] = None, broker_port: Optional[int] = None,
                 broker_vhost: Optional[str] = None,
                 result_user: Optional[str] = None, result_password: Optional[str] = None,
                 result_host: Optional[str] = None, result_port: Optional[int] = None, result_db: Optional[int] = None,
                 queue_prefix: str = "EVECelery.",
                 connection_check: bool = False):
        self.broker = ClientRabbitMQ(user=broker_user, password=broker_password, host=broker_host, port=broker_port,
                                     vhost=broker_vhost)
        self.result_backend = ClientRedisResultBackend(user=result_user, password=result_password, host=result_host,
                                                       port=result_port, db=result_db)

        if connection_check:
            self.result_backend.check_connection()
            self.broker.check_connection()

        self.max_concurrency = int(os.environ.get('EVECelery_MaxConcurrency', 10))

        self.queue_prefix = queue_prefix
        self.default_queue = f"{self.queue_prefix}Default"

        self.worker_name = f"EVECeleryWorker{random.randint(1000000, 9999999)}"
        self.app = Celery("EVECelery")
        self.app.conf.update(**self.celery_config())

        self.queues = set()
        self.queues.add(self.default_queue)

        self.task_routes = {}
        self.beat_schedule = {}
        self._register_all_tasks()

    def celery_config(self) -> dict:
        return {
            'task_serializer': 'json',
            'result_serializer': 'json',
            'accept_content': ['json'],
            'enable_utc': True,
            'broker_url': self.broker.connection_str,
            'result_backend': self.result_backend.connection_str,
            'task_default_queue': self.default_queue,
            'result_expires': 5400  # default
        }

    def _register_all_tasks(self):
        """
        Register all subtasks that inherit from BaseTask

        This method will register and initialize all subtasks that inherit from BaseTask.
        """
        for t in TaskBase.get_all_subtasks():
            task = t()
            self.app.register_task(task)
            if hasattr(task, 'queue_assignment') and task.queue_assignment is not None:
                q = f'{self.queue_prefix}{task.queue_assignment}'
                self.register_additional_queue(q)
                self.register_task_route(task.name, q)
            else:
                self.register_task_route(task.name, self.default_queue)

    def register_additional_queue(self, queue: str):
        """Register an additional queue that this Celery app should process.

        :param queue: Name of the queue
        :return: None
        """
        self.queues.add(queue)

    def register_task_route(self, task_name: str, queue_name: str):
        """Register a task to a specific queue using a Celery task route.

        :param task_name: The name of the task
        :param queue_name: Name of the queue to route tasks to.
        :return: None
        """
        self.task_routes[task_name] = {"queue": queue_name}
        self.app.conf.update(task_routes=self.task_routes)

    def register_task(self, task: Task):
        """Register a task instance with the Celery app. A task must inherit from the Celery Task base class.

        :param task: A task instance
        :return: None
        """
        self.app.register_task(task)

    @classmethod
    def print_header(cls):
        print(f"EVECelery {__version__} ({__url__})\n{__license__}")

    def start(self):
        """Starts the Celery app and beings processing messages in the queues.

        :return: None
        """
        self.print_header()
        self.app.start(argv=["worker", "-l", "WARNING", f"-n{self.worker_name}@%h", f"--autoscale={self.max_concurrency},1",
                             "-Q", ",".join(self.queues)])
