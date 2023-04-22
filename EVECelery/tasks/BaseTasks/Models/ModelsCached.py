from pydantic import Field
from .ModelsBase import ModelBaseEVECelery, ModelBaseWithModelInfo


class ModelCacheInfo(ModelBaseEVECelery):
    """
    A model for cache information.

    """
    class Config:
        validate_assignment = True  # this should be the only pydantic response that has direct manipulation of the variables

    hit: bool = Field(default=False, description='True if the request was returned from cache.')
    key: str = Field(default=None, description='The cache key as it exists in Redis.')
    ttl: int = Field(default=None, description='The current cache TTL for a previously cached response or the TTL to set on a result to cache.')


class ModelCachedResponse(ModelBaseWithModelInfo):
    """
    A cache response pydantic model for validation.

    """
    cache: ModelCacheInfo = Field(default=None, description='Information about the cache for this request.')


class ModelCachedSuccess(ModelCachedResponse):
    """
    A successful response that was cached.

    """
    pass


class ModelCachedException(ModelCachedResponse):
    """
    An exception occurred that should be cached to avoid exhausting error limits.


    """
    message: str = Field(default='No exception info provided', description='The message for a cached exception.')
