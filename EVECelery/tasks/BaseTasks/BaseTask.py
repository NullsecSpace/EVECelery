from celery import Task
import redis
from EVECelery.clients.ClientRedis import ClientRedisLocks, ClientRedisCache


class BaseTask(Task):
    def __init__(self):
        self.name = self.__class__.__name__

    @property
    def redis_locks(self) -> redis.Redis:
        return ClientRedisLocks().redis

    @property
    def redis_cache(self) -> redis.Redis:
        return ClientRedisCache().redis
