from EVECelery.exceptions.tasks import NotCached
from EVECelery.utils.ErrorLimiter import ESIErrorLimiter
from EVECelery.utils.RequestHeaders import RequestHeaders
import json
import requests
from datetime import datetime
from dateutil.parser import parse as dtparse
from .CachedTask import CachedTask


class ESIRequest(CachedTask):
    def ttl_404(self) -> int:
        """Returns the redis TTL for caching ESI responses that errored with a 404 - not found

        :return: Seconds to cache a 404 not found ESI response in Redis
        :rtype: int
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
        return f"{self.base_url()}{self.route(**kwargs)}/?datasource=tranquility"

    def run(self, *args, **kwargs):
        """
        The task body
        """
        try:
            return super().run(*args, **kwargs)
        except NotCached:
            return self._request_esi(**kwargs)

    def _request_esi(self, **kwargs):
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
        lookup_key = self.get_redis_response_key(**kwargs)
        lock_key = self.get_redis_lock_key(**kwargs)
        with self.redis_locks.lock(lock_key, blocking_timeout=15, timeout=300):
            ESIErrorLimiter.check_limit(self.redis_cache)
            rheaders = {}
            try:
                resp = requests.get(self.request_url(**kwargs), headers=RequestHeaders.get_headers(),
                                    timeout=5, verify=True)
                rheaders = resp.headers
                if resp.status_code == 200:
                    d = resp.json()
                    ttl_expire = int(max(
                        (dtparse(rheaders["expires"], ignoretz=True) - datetime.utcnow()).total_seconds(),
                        1)
                    )
                    self.redis_cache.set(name=lookup_key, value=json.dumps(d), ex=ttl_expire)
                    ESIErrorLimiter.update_limit(self.redis_cache,
                                                 error_limit_remain=int(rheaders["x-esi-error-limit-remain"]),
                                                 error_limit_reset=int(rheaders["x-esi-error-limit-reset"]),
                                                 time=dtparse(rheaders["date"], ignoretz=True)
                                                 )
                    return json.loads(self.redis_cache.get(lookup_key))
                elif resp.status_code == 400 or resp.status_code == 404:
                    d = {"error": str(resp.json().get("error")), "error_code": resp.status_code}
                    self.redis_cache.set(name=lookup_key, value=json.dumps(d), ex=self.ttl_404())
                    ESIErrorLimiter.update_limit(self.redis_cache,
                                                 error_limit_remain=int(rheaders["x-esi-error-limit-remain"]),
                                                 error_limit_reset=int(rheaders["x-esi-error-limit-reset"]),
                                                 time=dtparse(rheaders["date"], ignoretz=True)
                                                 )
                    return json.loads(self.redis_cache.get(lookup_key))
                else:
                    resp.raise_for_status()
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

