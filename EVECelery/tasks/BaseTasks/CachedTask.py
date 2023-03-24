import json
from typing import Union
import hashlib
from .BaseTask import BaseTask
from EVECelery.clients.ClientRedis import ClientRedisLocks, ClientRedisCache
from EVECelery.exceptions.tasks import NotCached
import redis


class CachedTask(BaseTask):
    """
    A task utilizing Redis for some form of caching and locks where the results are cached.
    """

    @property
    def redis_locks(self) -> redis.Redis:
        """Get the Redis client for managing the locks"""
        return ClientRedisLocks().redis

    @property
    def redis_cache(self) -> redis.Redis:
        """Get the Redis client for managing the cache"""
        return ClientRedisCache().redis

    def get_redis_response_key(self, **kwargs) -> str:
        """Returns the Redis key for storing a cache response with the provided input parameters.

        :param kwargs: Parameters passed to the task
        :return: Redis key for storing the value of the ESI response
        :rtype: str
        """
        h = hashlib.sha256()
        for k, v in sorted(kwargs.items()):
            h.update(f'{k}:{v}'.encode('utf-8'))
        return f'{self.name}-{h.hexdigest()}'

    def get_redis_lock_key(self, **kwargs) -> str:
        """Returns the Redis key for lock response with the provided input parameters.

        :param kwargs: ESI request parameters
        :return: Redis key for storing ESI locks
        :rtype: str
        """
        k = self.get_redis_response_key(**kwargs)
        return f"Lock-{k}"

    def validate_inputs(self, **kwargs) -> None:
        """Run validation checks before continuing a task run or checking the cache.

        :param kwargs: Task request parameters
        :return: None
        :raises EVECelery.exceptions.tasks.InputValidationError: If an input task parameter contains
            invalid syntax
        """
        raise NotImplementedError

    def get_cached(self, **kwargs) -> Union[list, str, dict]:
        """Get the cached response with the task request parameters from Redis if it exists.

        :param kwargs: Task request parameters
        :return: Dictionary, list, or string containing cached response from the previously ran task.
        :raises EVECelery.exceptions.tasks.NotCached: If the request has not yet been resolved by a previous task invocation or the TTL expired.
        :raises EVECelery.exceptions.tasks.InputValidationError: If a task input parameter contains invalid data or syntax
        """
        self.validate_inputs(**kwargs)
        cached_data = self.redis_cache.get(self.get_redis_response_key(**kwargs))
        if cached_data:
            return json.loads(cached_data)
        else:
            raise NotCached

    def run(self, *args, **kwargs) -> Union[list, str, dict]:
        """
        Check that cache first for a result. #todo more docs
        """
        with self.redis_locks.lock(self.get_redis_lock_key(**kwargs), blocking_timeout=15, timeout=300):
            return self.get_cached(**kwargs)
