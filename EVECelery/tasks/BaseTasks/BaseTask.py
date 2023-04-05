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

    @property
    def queue_assignment(self) -> str | None:
        """
        The queue to register this task with.

        Returns the name of the queue to optionally register this task with.
        If None is provided then this task is registered with the default queue defined by the celery app.

        """
        return None

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

    @classmethod
    def get_all_subtasks(cls):
        """
        Yield task subclasses that inherit from this task class.

        Yields all subclasses from this base class. The base class itself is not yielded.

        """
        for c in cls.__subclasses__():
            if issubclass(c, Task):
                yield c
            yield from c.get_all_subtasks()
