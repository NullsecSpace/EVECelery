from typing import Union
from celery import Task
from celery.result import AsyncResult


class BaseTask(Task):
    """The base task class"""
    autoretry_for = (Exception,)
    max_retries = 1
    retry_backoff = 1
    retry_backoff_max = 1
    retry_jitter = False

    def __init__(self):
        self.name = self.__class__.__name__

    def get_async(self, ignore_result: bool = False, **kwargs) -> AsyncResult:
        """Returns an async result / promise representing the future evaluation of a task.
        This function does not block the calling process and returns immediately.

        :param ignore_result: Set false to store result in celery result backend, else ignore the result.
        :type ignore_result: bool
        :param kwargs: ESI request parameters
        :return: Promise for a future evaluation of a celery task
        :rtype: celery.result.AsyncResult
        """
        return self.apply_async(ignore_result=ignore_result, kwargs=kwargs)

    def get_sync(self, timeout: float = 10, **kwargs) -> Union[list, str, dict]:
        """Call a task and block until the result is set.

        :param timeout: The time in seconds to block waiting for the task to complete.
        Setting this to None blocks forever.
        :type timeout: float
        :param kwargs: Task parameters
        :return: The task result
        """
        return self.get_async(ignore_result=False, **kwargs).get(timeout=timeout, propagate=True)
