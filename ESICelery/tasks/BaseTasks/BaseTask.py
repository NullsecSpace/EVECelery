from celery import Task
import redis
from ESICelery.clients.ClientRedis import ClientRedisLocks, ClientRedisCache


class BaseTask(Task):
    _client_redis_locks: ClientRedisLocks = None
    _client_redis_cache: ClientRedisCache = None

    def __init__(self):
        self.name = self.__class__.__name__

    @property
    def redis_locks(self) -> redis.Redis:
        if self._client_redis_locks is None:
            c = ClientRedisLocks()
            c.check_connection()
            self._client_redis_locks = c
        return self._client_redis_locks.redis

    @property
    def redis_cache(self) -> redis.Redis:
        if self._client_redis_cache is None:
            c = ClientRedisCache()
            c.check_connection()
            self._client_redis_cache = c
        return self._client_redis_cache.redis
