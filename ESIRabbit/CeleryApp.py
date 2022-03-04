from celery import Celery, Task
import os
from ESIRabbit.celeryconfig import task_routes
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
        for k, v in task_routes.items():
            self.queues.append(v["queue"])

        default_tasks = [AllianceInfo(),
                         CharacterPublicInfo(),
                         CorporationInfo(),
                         PricesList(),
                         CategoryInfo(),
                         ConstellationInfo(),
                         FactionsList(),
                         GroupInfo(),
                         RegionInfo(),
                         SystemInfo(),
                         TypeInfo()
                         ]
        self.register_tasks(default_tasks)

    def register_additional_queues(self, queues: list[str]):
        for q in queues:
            self.queues.append(q)

    def register_tasks(self, tasks: list[Task]):
        for t in tasks:
            app.register_task(t)

    def start(self, max_concurrency: int = 10):
        app.start(argv=["worker", "-l", "WARNING", f"--autoscale={max_concurrency},1",
                        "-Q", ",".join(self.queues)])

def main():
    c = CeleryApp(os.environ["BrokerUser"], os.environ["BrokerPassword"], os.environ["BrokerHost"],
                  os.environ["BrokerPort"], os.environ["BrokerVhost"],
                  os.environ["ResultBackendUser"], os.environ["ResultBackendPassword"], os.environ["ResultBackendHost"],
                  os.environ["ResultBackendPort"], os.environ["ResultBackendDb"])
    c.start()


if __name__ == '__main__':
    main()
