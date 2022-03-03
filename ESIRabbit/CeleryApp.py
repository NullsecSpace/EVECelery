from celery import Celery
import os
from ESIRabbit.celeryconfig import task_routes
from ESIRabbit.tasks.BaseTasks.BaseTask import BaseTask


app = Celery("ESIRabbit")


class CeleryApp:
    def __init__(self, broker_user: str, broker_password: str, broker_host: str, broker_port: str, broker_vhost: str,
                 result_user: str, result_password: str, result_host: str, result_port: str, result_db: str,
                 config_object: str = "ESIRabbit.celeryconfig", additional_queues: list[str] = None,
                 max_concurrency: int = 10):
        if additional_queues is None:
            self.additional_queues = []
        else:
            self.additional_queues = additional_queues
        app.config_from_object(config_object)
        broker_url = f"amqp://{broker_user}:{broker_password}@{broker_host}:{broker_port}/{broker_vhost}"
        result_backend = f"redis://{result_user}:{result_password}@{result_host}:{result_port}/{result_db}"
        app.conf.update(broker_url=broker_url)
        app.conf.update(result_backend=result_backend)
        self.max_concurrency = max_concurrency
        BaseTask.set_redis_details(host=result_host, port=result_port, db=result_db,
                                   user=result_user, password=result_password)

    def get_queues(self):
        queues = ["ESIRabbitDefault"]
        for k, v in task_routes.items():
            queues.append(v.get("queue"))
        queues += self.additional_queues
        return queues

    def start(self):
        app.start(argv=["worker", "-l", "WARNING", f"--autoscale={self.max_concurrency},2",
                        "-Q", ",".join(self.get_queues())])


def main():
    c = CeleryApp(os.environ["BrokerUser"], os.environ["BrokerPassword"], os.environ["BrokerHost"],
                  os.environ["BrokerPort"], os.environ["BrokerVhost"],
                  os.environ["ResultBackendUser"], os.environ["ResultBackendPassword"], os.environ["ResultBackendHost"],
                  os.environ["ResultBackendPort"], os.environ["ResultBackendDb"])
    c.start()


if __name__ == '__main__':
    main()
