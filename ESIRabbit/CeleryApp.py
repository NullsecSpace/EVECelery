from celery import Celery, Task
import os
from ESIRabbit.tasks.BaseTasks.BaseTask import BaseTask
from ESIRabbit.tasks.Alliance import *
from ESIRabbit.tasks.Character import *
from ESIRabbit.tasks.Corporation import *
from ESIRabbit.tasks.Market import *
from ESIRabbit.tasks.Universe import *

app = Celery("ESIRabbit")


class CeleryApp:
    def __init__(self, broker_user: str, broker_password: str, broker_host: str, broker_port: str, broker_vhost: str,
                 result_user: str, result_password: str, result_host: str, result_port: str, result_db: str,
                 config_object: str = "ESIRabbit.celeryconfig"):
        app.config_from_object(config_object)
        broker_url = f"amqp://{broker_user}:{broker_password}@{broker_host}:{broker_port}/{broker_vhost}"
        result_backend = f"redis://{result_user}:{result_password}@{result_host}:{result_port}/{result_db}"
        app.conf.update(broker_url=broker_url)
        app.conf.update(result_backend=result_backend)
        BaseTask.set_redis_details(host=result_host, port=result_port, db=result_db,
                                   user=result_user, password=result_password)
        self.queues = ["ESIRabbitDefault"]
        self.task_routes = {}
        self._register_defaults()

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

    def _register_defaults(self):
        for t in self.default_tasks():
            queue_name = f"Get{t.name}"
            self.register_task(t)
            self.register_additional_queue(queue_name)
            self.register_task_route(t.name, queue_name)

    def register_additional_queue(self, queue: str):
        self.queues.append(queue)

    def register_task_route(self, task_name: str, queue_name: str):
        self.task_routes[task_name] = {"queue": queue_name}
        app.conf.update(task_routes=self.task_routes)

    @staticmethod
    def register_task(task: Task):
        app.register_task(task)

    def start(self, max_concurrency: int = 10):
        app.start(argv=["worker", "-l", "WARNING", f"--autoscale={max_concurrency},1",
                        "-Q", ",".join(self.queues)])

    @classmethod
    def main(cls):
        c = cls(os.environ["BrokerUser"], os.environ["BrokerPassword"], os.environ["BrokerHost"],
                os.environ["BrokerPort"], os.environ["BrokerVhost"],
                os.environ["ResultBackendUser"], os.environ["ResultBackendPassword"],
                os.environ["ResultBackendHost"],
                os.environ["ResultBackendPort"], os.environ["ResultBackendDb"])
        c.start()


if __name__ == '__main__':
    CeleryApp.main()
