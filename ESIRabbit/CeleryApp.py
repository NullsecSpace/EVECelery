from celery import Celery, Task
import os
from ESIRabbit.tasks.Alliance import *
from ESIRabbit.tasks.Character import *
from ESIRabbit.tasks.Corporation import *
from ESIRabbit.tasks.Market import *
from ESIRabbit.tasks.Universe import *
import ESIRabbit.config

app = Celery("ESIRabbit")


class CeleryApp:
    def __init__(self, broker_user: str, broker_password: str, broker_host: str, broker_port: int, broker_vhost: str,
                 result_user: str, result_password: str, result_host: str, result_port: int, result_db: int,
                 header_email: str, config_object: str = "ESIRabbit.celeryconfig", queue_prefix: str = "ESI"):
        """

        :param broker_user: RabbitMQ user
        :param broker_password: RabbitMQ password
        :param broker_host: RabbitMQ hostname
        :param broker_port: RabbitMQ port - normally 5672
        :param broker_vhost: RabbitMQ vhost - namespace for all ESIRabbit queues
        :param result_user: Redis user - normally "default" if not explicitly configured
        :param result_password: Redis password
        :param result_host: Redis hostname
        :param result_port: Redis port - normally 6379
        :param result_db: Redis db - normally 0 for the default db
        :param header_email: Your contact email to include in http requests to ESI and ZK
        :param config_object: Custom config object to overwrite the default ESIRabbit.celeryconfig - optional
        :param queue_prefix: Prefix to add to all generated queue names
        """
        app.config_from_object(config_object)
        broker_url = f"amqp://{broker_user}:{broker_password}@{broker_host}:{broker_port}/{broker_vhost}"
        result_backend = f"redis://{result_user}:{result_password}@{result_host}:{result_port}/{result_db}"
        app.conf.update(broker_url=broker_url)
        app.conf.update(result_backend=result_backend)
        app.conf.update(task_default_queue=f"{queue_prefix}Default")

        ESIRabbit.config.header_email = header_email
        ESIRabbit.config.redis_host = result_host
        ESIRabbit.config.redis_port = result_port
        ESIRabbit.config.redis_db = result_db
        ESIRabbit.config.redis_user = result_user
        ESIRabbit.config.redis_password = result_password

        self.queues = [f"{queue_prefix}Default"]
        self.task_routes = {}
        self._register_defaults(queue_prefix)

    @staticmethod
    def default_tasks():
        yield AllianceInfo()
        yield CharacterPublicInfo()
        yield CorporationInfo()
        yield PricesList()
        yield CategoryInfo()
        yield ConstellationInfo()
        yield FactionsList()
        yield GroupInfo()
        yield RegionInfo()
        yield SystemInfo()
        yield TypeInfo()

    def _register_defaults(self, queue_prefix: str):
        for t in self.default_tasks():
            queue_name = f"{queue_prefix}{t.name}"
            self.register_task(t)
            self.register_additional_queue(queue_name)
            self.register_task_route(t.name, queue_name)

    def register_additional_queue(self, queue: str):
        """Register an additional queue that this Celery app should process.

        :param queue: Name of the queue
        :return: None
        """
        self.queues.append(queue)

    def register_task_route(self, task_name: str, queue_name: str):
        """Register a task to a specific queue using a Celery task route.

        :param task_name: The name of the task
        :param queue_name: Name of the queue to route tasks to.
        :return: None
        """
        self.task_routes[task_name] = {"queue": queue_name}
        app.conf.update(task_routes=self.task_routes)

    @staticmethod
    def register_task(task: Task):
        """Register a task instance with the Celery app. A task must inherit from the Celery Task base class.

        :param task: A task instance
        :return: None
        """
        app.register_task(task)

    def start(self, max_concurrency: int = 10):
        """Starts the Celery app and beings processing messages in the queues.

        :param max_concurrency: The maximum number of processes that celery can autoscale to.
        :return: None
        """
        ESIRabbit.config.max_concurrency = max_concurrency
        app.start(argv=["worker", "-l", "WARNING", f"--autoscale={max_concurrency},1",
                        "-Q", ",".join(self.queues)])

    @classmethod
    def main(cls):
        try:
            c = cls(os.environ["BrokerUser"], os.environ["BrokerPassword"], os.environ["BrokerHost"],
                    int(os.environ["BrokerPort"]), os.environ["BrokerVhost"],
                    os.environ["ResultBackendUser"], os.environ["ResultBackendPassword"],
                    os.environ["ResultBackendHost"],
                    int(os.environ["ResultBackendPort"]), int(os.environ["ResultBackendDb"]),
                    os.environ["HeaderEmail"])
        except KeyError as ex:
            print("Environmental variable is not set.")
            raise ex
        c.start()


if __name__ == '__main__':
    CeleryApp.main()
