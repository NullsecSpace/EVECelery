from EVECelery.utils.ErrorLimiter import ESIErrorLimiter
from EVECelery.utils.RequestHeaders import RequestHeaders
import requests
from datetime import datetime
from dateutil.parser import parse as dtparse
from typing import Union
from .TaskCached import TaskCached, ModelCachedSuccess, ModelCachedException
from requests.exceptions import RequestException
from redis.exceptions import RedisError


class TaskESI(TaskCached):
    autoretry_for = (RequestException, RedisError)
    max_retries = 3
    retry_backoff = 5
    retry_backoff_max = 60
    retry_jitter = True
    soft_time_limit = 30

    def __init__(self):
        super().__init__()
        self.name = '.'.join(self.__module__.split('.')[-3:])

    @property
    def queue_assignment(self) -> str | None:
        """
        The queue to register this task with.

        Returns the name of the queue to optionally register this task with.
        If None is provided then this task is registered with the default queue defined by the celery app.

        """
        return self.name

    def request_method(self) -> str:
        """
        Returns the type of request made to ESI

        This method will return the request method (get, post, etc.) made to ESI.
        :return: Request method passed to requests.request()
        """
        return 'get'

    def default_ttl(self) -> int:
        """
        Default TTL to set in Redis for results that don't have expiry information.

        :return: The number of seconds to cache a response
        """
        return 86400

    def base_url(self) -> str:
        """Base URL for ESI requests

        :return: ESI base request URL
        :rtype: str
        """
        return "https://esi.evetech.net/latest"

    def route(self, **kwargs) -> str:
        """ESI route with input request parameters

        :param kwargs: ESI request parameters to fill in the ESI request string
        :return: ESI route with request parameters
        :rtype: str
        """
        raise NotImplementedError

    def request_url(self, **kwargs) -> str:
        """ESI request URL with request parameters

        :param kwargs: ESI request parameters to fill in the ESI request string
        :return: ESI request URL with request parameters
        :rtype: str
        """
        return f"{self.base_url()}{self.route(**kwargs)}"

    def _run_get_result(self, **kwargs) -> Union[ModelCachedSuccess, ModelCachedException]:
        """Gets the ESI cached response.
        If the response is not yet cached or hasn't been resolved then perform an ESI call caching the new response.

        This function should not be called outside of celery tasks and should only be invoked
        by the task function handling a lookup queue.

        :param redis: The redis client
        :param kwargs: ESI request parameters
        :return: Dictionary containing response from ESI.
            If ESI returned a 404 error the response will be in the form
            {"error": error_message, "error_code": 404}
            If the response doesn't require request inputs then list is usually returned (list factions, prices, etc).
            If the response requires inputs a dictionary is usually returned.
            Only /universe/factions/ and /markets/prices/ returns a list, all else return dictionaries.
        :rtype: dict or list
        :raises EVECelery.exceptions.utils.ErrorLimitExceeded: If the remaining error limit is below the allowed threshold.
        """
        ESIErrorLimiter.check_limit(self.redis_cache)
        rheaders = {}
        try:
            resp = requests.request(self.request_method(), self.request_url(**kwargs),
                                    headers=RequestHeaders.get_headers(), timeout=15, verify=True)
            rheaders = resp.headers
            if 200 <= resp.status_code < 300:
                ttl_expire = int(max(
                    (dtparse(rheaders["expires"], ignoretz=True) - datetime.utcnow()).total_seconds(),
                    1)
                )
                ESIErrorLimiter.update_limit(self.redis_cache,
                                             error_limit_remain=int(rheaders["x-esi-error-limit-remain"]),
                                             error_limit_reset=int(rheaders["x-esi-error-limit-reset"]),
                                             time=dtparse(rheaders["date"], ignoretz=True)
                                             )
                response_model = self.reflection_get_model(f'ResponseSuccess{resp.status_code}_{self.__name__}')
                response_data = resp.json()
                if isinstance(response_data, dict):
                    return response_model(cache_ttl=ttl_expire, headers=resp.headers, **response_data)
                else:  # list response
                    return response_model(cache_ttl=ttl_expire, headers=resp.headers, items=response_data)
            elif 400 <= resp.status_code < 500:
                ESIErrorLimiter.update_limit(self.redis_cache,
                                             error_limit_remain=int(rheaders["x-esi-error-limit-remain"]),
                                             error_limit_reset=int(rheaders["x-esi-error-limit-reset"]),
                                             time=dtparse(rheaders["date"], ignoretz=True)
                                             )
                msg = f'{resp.status_code} - {resp.json()}'
                return ModelCachedException(exception_message=msg)
            else:
                resp.raise_for_status()
                raise ValueError(f'Unhandled response code {resp.status_code}')
        except Exception as ex:
            try:
                ESIErrorLimiter.update_limit(self.redis_cache,
                                             error_limit_remain=int(rheaders["x-esi-error-limit-remain"]),
                                             error_limit_reset=int(rheaders["x-esi-error-limit-reset"]),
                                             time=dtparse(rheaders["date"], ignoretz=True)
                                             )
            except KeyError:
                ESIErrorLimiter.decrement_limit(self.redis_cache, datetime.utcnow())
            raise ex
