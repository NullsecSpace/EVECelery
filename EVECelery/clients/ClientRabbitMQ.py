import os
import sys
from typing import Optional
from pydantic import BaseModel
import traceback
from .BaseClient import BaseClient
from EVECelery.utils.Singleton import Singleton
import pika


class ConfigRabbitMQ(BaseModel):
    user: str
    password: str
    host: str
    port: int
    vhost: str


class ClientRabbitMQ(BaseClient, metaclass=Singleton):
    """
    The RabbitMQ client wrapper used as the Celery broker service.

    :param user: RabbitMQ user
    :param password: RabbitMQ password
    :param host: RabbitMQ hostname
    :param port: RabbitMQ port - normally 5672
    :param vhost: RabbitMQ vhost - namespace for all queues
    """

    def __init__(self, user: Optional[str] = None, password: Optional[str] = None, host: Optional[str] = None,
                 port: Optional[int] = None, vhost: Optional[str] = None):
        try:
            if user is None:
                user = os.environ['EVECelery_RabbitMQ_User']
            if password is None:
                password = os.environ['EVECelery_RabbitMQ_Password']
            if host is None:
                host = os.environ['EVECelery_RabbitMQ_Host']
            if port is None:
                port = os.environ.get('EVECelery_RabbitMQ_Port', 5672)
            if vhost is None:
                vhost = os.environ['EVECelery_RabbitMQ_Vhost']
        except KeyError as ex:
            traceback.print_exc()
            print(f'The environmental variable is not set for {ex}. '
                  f'Please set this env var or pass it as an argument to initialize ClientRabbitMQ.')
            sys.exit(1)
        self.config = ConfigRabbitMQ(user=user, password=password, host=host, port=port, vhost=vhost)

    def check_connection(self) -> bool:
        credentials = pika.PlainCredentials(username=self.config.user, password=self.config.password,
                                            erase_on_connect=True)
        c = pika.BlockingConnection(pika.ConnectionParameters(host=self.config.host, port=self.config.port,
                                                              virtual_host=self.config.vhost, credentials=credentials,
                                                              blocked_connection_timeout=10, socket_timeout=10))
        c.close()
        return True


    @property
    def connection_str(self):
        return f"amqp://{self.config.user}:{self.config.password}@{self.config.host}:{self.config.port}/{self.config.vhost}"
