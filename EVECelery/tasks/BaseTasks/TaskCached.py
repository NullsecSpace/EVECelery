from typing import Union, Tuple, Optional
import hashlib
from .TaskBase import TaskBase, ModelTaskBaseResponse
from EVECelery.clients.ClientRedis import ClientRedisLocks, ClientRedisCache
from EVECelery.exceptions.tasks import CachedException
import redis
from pydantic import Field


class ModelCachedResponse(ModelTaskBaseResponse):
    """
    A cache response pydantic model for validation.


    """
    cache_hit: bool = Field(default=False, description='True if the request was returned from cache.')
    cache_key: str = Field(default=None, description='The cache key as it exists in Redis.')
    cache_ttl: int = Field(default=None,
                           description='The current cache TTL for a previously cached response or the TTL to set on a result to cache.')


class ModelCachedSuccess(ModelCachedResponse):
    """

    """
    pass


class ModelCachedException(ModelCachedResponse):
    """
    An exception occurred that should be cached to avoid exhausting error limits.


    """
    exception_message: str = Field(default='No exception info provided',
                                   description='The message for a cached exception.')


class TaskCached(TaskBase):
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

    def default_ttl(self) -> int:
        """
        Default TTL to set in Redis for results that don't have expiry information.

        :return: The number of seconds to cache a response
        """
        return 86400

    def get_hash(self, **kwargs) -> str:
        """
        Returns the SHA256 hash of kwargs

        """
        h = hashlib.sha256()
        for k, v in sorted(kwargs.items()):
            h.update(f'{k}:{v}'.encode('utf-8'))
        return h.hexdigest()

    def get_redis_cache_key(self, **kwargs) -> str:
        """Returns the Redis key for storing a cached response with the provided input parameters.

        :param kwargs: Parameters passed to the task
        :return: Redis key for storing the value of the ESI response
        :rtype: str
        """
        return f'Cache.{self.name}.{self.get_hash(**kwargs)}'

    def get_redis_lock_key(self, **kwargs) -> str:
        """Returns the Redis key for lock response with the provided input parameters.

        :param kwargs: ESI request parameters
        :return: Redis key for storing ESI locks
        :rtype: str
        """
        return f'Lock.{self.name}.{self.get_hash(**kwargs)}'

    def cache_key_exists(self, **kwargs) -> bool:
        """
        Check if cache key exists for given input
        """
        return self.redis_cache.exists(self.get_redis_cache_key(**kwargs)) >= 1

    def get_sync(self, kwargs_apply_async: Optional[dict] = None, kwargs_get: Optional[dict] = None,
                 **kwargs) -> ModelCachedResponse:
        if kwargs is None:
            kwargs = {}
        r = super().get_sync(kwargs_apply_async=kwargs_apply_async, kwargs_get=kwargs_get, **kwargs)
        m = self.to_pydantic(r)
        if not isinstance(m, ModelCachedResponse):
            raise TypeError('Returned result should inherit from model ModelCachedResponse')
        return m

    def run(self, **kwargs) -> dict:
        """
        Returns the result from the Redis cache if it exists, otherwise runs and returns :func:`_run_get_result` as a dictionary.

        This function checks the cache based on the provided input and will return the result from the cache first, skipping a rerun of :func:`_run_get_result`.
        If the result does not exist in the cache it will run :func:`_run_get_result` and cache the result for future task runs.

        If an exception is raised by :func:`_run_get_result` the exception will be raised to the calling client and will not be cached.
        If :func:`_run_get_result` returns a :func:`ModelCachedException` then the exception will first be cached and then thrown to the calling client as a :func:`CachedException`.

        :return: The response data as a dictionary.
            This dictionary can be converted to a pydantic model by passing it to this task's :func:`to_pydantic` method
            for easier inspection and schema documentation (required fields, field meanings, etc.).
        """
        with self.redis_locks.lock(name=self.get_redis_lock_key(**kwargs), blocking_timeout=15, timeout=300):
            key_cache = self.get_redis_cache_key(**kwargs)
            cached_data: str = self.redis_cache.get(key_cache)
            if cached_data:
                response_pydantic = self.to_pydantic(cached_data)
                response_pydantic.cache_ttl = self.redis_cache.ttl(key_cache)  # need to return current ttl, not initial
                response_pydantic.cache_hit = True
            else:
                response_pydantic = self._run_get_result(**kwargs)
                response_pydantic.cache_hit = False
                response_pydantic.cache_key = key_cache
                if response_pydantic.cache_ttl is None:
                    response_pydantic.cache_ttl = self.default_ttl()

                self.redis_cache.set(name=response_pydantic.cache_key, value=response_pydantic.json(),
                                     ex=response_pydantic.cache_ttl)

        if isinstance(response_pydantic, ModelCachedException):
            raise CachedException(
                f'{response_pydantic.exception_message} - Cached exception expires in {response_pydantic.cache_ttl} seconds')
        else:
            return response_pydantic.dict()

    def _run_get_result(self, **kwargs) -> Union[ModelCachedResponse, ModelCachedException]:
        """
        The task body to execute if the result is not currently cached.

        This function is the body of a task that gets executed when a previously returned result is not cached or has expired.
        This function must return a pydantic model that inherits from :func:`ModelCachedResponse` or :func:`ModelCachedException`.

        If :func:`ModelCachedException` is returned, then the exception will be cached for the defined TTL and have an exception thrown to the calling client.

        :return: The response success or cached exception pydantic model.
        """
        raise NotImplementedError
