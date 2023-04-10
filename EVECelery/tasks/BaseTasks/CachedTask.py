import json
from typing import Union, Tuple, Optional
import hashlib
from .BaseTask import BaseTask
from EVECelery.clients.ClientRedis import ClientRedisLocks, ClientRedisCache
from EVECelery.exceptions.tasks import CachedException
import redis
from pydantic import BaseModel, Field, validator, validate_arguments
import sys
import inspect


class ModelCachedResponse(BaseModel):
    """
    A cache response pydantic model for validation.


    """
    cache_hit: bool = Field(default=False, description='True if the request was returned from cache.')
    cache_key: str = Field(default=None, description='The cache key as it exists in Redis.')
    cache_ttl: int = Field(default=None,
                           description='The current cache TTL for a previously cached response or the TTL to set on a result to cache.')
    pydantic_model: str = Field(default=None,
                                description='The name of the pydantic model class that this model was initialized with.')

    class Config:
        validate_assignment = True

    @validator('pydantic_model', pre=True, always=True)
    def dynamic_set_pydantic_model(cls, v):
        return v or cls.class_name()

    @classmethod
    def class_name(cls) -> str:
        return cls.__name__


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

    @validate_arguments
    def deserialize_to_pydantic(self, json_str: Union[str, dict]) -> Union[ModelCachedResponse, ModelCachedException]:
        """
        #todo docs
        """
        if isinstance(json_str, str):
            deserialized_data = json.loads(json_str)
        else:
            deserialized_data: dict = json_str

        model_name = deserialized_data.get('pydantic_model')
        if model_name is None:
            raise KeyError('The data from Redis did not include the "pydantic_model" attribute. '
                           'This is required for deserializing previously serialized pydantic model. '
                           'Insure your model inherits from ModelCachedResponse.')
        model = getattr(sys.modules[self.__module__], model_name)
        if not issubclass(model, ModelCachedResponse):
            raise TypeError('Model must inherit from ModelCachedResponse.')
        return model.parse_obj(deserialized_data)

    def get_sync(self, kwargs_apply_async: Optional[dict] = None, kwargs_get: Optional[dict] = None,
                 **kwargs) -> ModelCachedResponse:
        return super().get_sync(kwargs_apply_async=kwargs_apply_async, kwargs_get=kwargs_get, **kwargs)

    def run(self, **kwargs) -> dict:
        """
        Check that cache first for a result. #todo more docs
        """
        with self.redis_locks.lock(name=self.get_redis_lock_key(**kwargs), blocking_timeout=15, timeout=300):
            key_cache = self.get_redis_cache_key(**kwargs)
            cached_data: str = self.redis_cache.get(key_cache)
            if cached_data:
                response_pydantic = self.deserialize_to_pydantic(cached_data)
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

    def _run_get_result(self, **kwargs) -> Union[ModelCachedResponse]:
        """
        Run method called by task if the result is not cached.
        :return: A tuple with of (response, cache_ttl)
        """
        raise NotImplementedError
