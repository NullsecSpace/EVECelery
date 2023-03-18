import os
import sys
from typing import Optional
from pydantic import BaseModel, validator
from EVECelery.utils.Singleton import Singleton
import traceback
import redis


class ConfigRedis(BaseModel):
    user: str
    password: str
    host: str
    port: int
    db: int

    @validator('db')
    def valid_db_number(cls, v):
        if not 0 <= v <= 15:
            raise ValueError('Redis DB must be between 0 and 15.')
        return v


class ClientRedis(metaclass=Singleton):
    """

    :param user: Redis user
    :param password: Redis password
    :param host: Redis hostname
    :param port: Redis port - normally 6379
    :param db: Redis DB - namespace for all queues
    """

    def __init__(self, user: str, password: str, host: str, port: int, db: int):
        self.config = ConfigRedis(user=user, password=password, host=host, port=port, db=db)
        self._redis = None

    def check_connection(self) -> bool:
        return self.redis.ping()

    @property
    def redis(self) -> redis.Redis:
        if self._redis is None:
            self._redis = redis.Redis(username=self.config.user, host=self.config.host, port=self.config.port,
                                      db=self.config.db, password=self.config.password, socket_timeout=10)
        return self._redis

    @property
    def connection_str(self):
        return f"redis://{self.config.user}:{self.config.password}@{self.config.host}:{self.config.port}/{self.config.db}"


class ClientRedisResultBackend(ClientRedis):
    def __init__(self, user: Optional[str] = None, password: Optional[str] = None, host: Optional[str] = None,
                 port: Optional[int] = None, db: Optional[int] = None):
        try:
            if user is None:
                user = os.environ['EVECelery_Redis_ResultBackend_User']
            if password is None:
                password = os.environ['EVECelery_Redis_ResultBackend_Password']
            if host is None:
                host = os.environ['EVECelery_Redis_ResultBackend_Host']
            if port is None:
                port = os.environ.get('EVECelery_Redis_ResultBackend_Port', 6379)
            if db is None:
                db = os.environ.get('EVECelery_Redis_ResultBackend_DB', 0)
        except KeyError as ex:
            traceback.print_exc()
            print(f'The environmental variable is not set for {ex}. '
                  f'Please set this env var or pass it as an argument to initialize ClientRedisResultBackend.')
            sys.exit(1)
        super().__init__(user=user, password=password, host=host, port=port, db=db)


class ClientRedisLocks(ClientRedis):
    def __init__(self, user: Optional[str] = None, password: Optional[str] = None, host: Optional[str] = None,
                 port: Optional[int] = None, db: Optional[int] = None):
        try:
            if user is None:
                user = os.environ.get('EVECelery_Redis_Locks_User',
                                      os.environ.get('EVECelery_Redis_ResultBackend_User'))
                if user is None:
                    raise KeyError('EVECelery_Redis_Locks_User')
            if password is None:
                password = os.environ.get('EVECelery_Redis_Locks_Password',
                                          os.environ.get('EVECelery_Redis_ResultBackend_Password'))
                if password is None:
                    raise KeyError('EVECelery_Redis_Locks_Password')
            if host is None:
                host = os.environ.get('EVECelery_Redis_Locks_Host',
                                      os.environ.get('EVECelery_Redis_ResultBackend_Host'))
                if host is None:
                    raise KeyError('EVECelery_Redis_Locks_Host')
            if port is None:
                port = os.environ.get('EVECelery_Redis_Locks_Port',
                                      os.environ.get('EVECelery_Redis_ResultBackend_Port', 6379))
            if db is None:
                db = os.environ.get('EVECelery_Redis_Locks_DB',
                                    int(os.environ.get('EVECelery_Redis_ResultBackend_DB', 0)) + 1)
        except KeyError as ex:
            traceback.print_exc()
            print(f'The environmental variable is not set for {ex}. '
                  f'Please set this env var or pass it as an argument to initialize ClientRedisLocks.')
            sys.exit(1)
        super().__init__(user=user, password=password, host=host, port=port, db=db)


class ClientRedisCache(ClientRedis):
    def __init__(self, user: Optional[str] = None, password: Optional[str] = None, host: Optional[str] = None,
                 port: Optional[int] = None, db: Optional[int] = None):
        try:
            if user is None:
                user = os.environ.get('EVECelery_Redis_Cache_User',
                                      os.environ.get('EVECelery_Redis_ResultBackend_User'))
                if user is None:
                    raise KeyError('EVECelery_Redis_Cache_User')
            if password is None:
                password = os.environ.get('EVECelery_Redis_Cache_Password',
                                          os.environ.get('EVECelery_Redis_ResultBackend_Password'))
                if password is None:
                    raise KeyError('EVECelery_Redis_Cache_Password')
            if host is None:
                host = os.environ.get('EVECelery_Redis_Cache_Host',
                                      os.environ.get('EVECelery_Redis_ResultBackend_Host'))
                if host is None:
                    raise KeyError('EVECelery_Redis_Cache_Host')
            if port is None:
                port = os.environ.get('EVECelery_Redis_Cache_Port',
                                      os.environ.get('EVECelery_Redis_ResultBackend_Port', 6379))
            if db is None:
                db = os.environ.get('EVECelery_Redis_Cache_DB',
                                    int(os.environ.get('EVECelery_Redis_ResultBackend_DB', 0)) + 2)
        except KeyError as ex:
            traceback.print_exc()
            print(f'The environmental variable is not set for {ex}. '
                  f'Please set this env var or pass it as an argument to initialize ClientRedisCache.')
            sys.exit(1)
        super().__init__(user=user, password=password, host=host, port=port, db=db)
