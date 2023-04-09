from celery import Task
from typing import Optional
from pydantic import validate_arguments


class BaseTask(Task):
    """
    The base Celery task class used by EVECelery.

    All tasks to be processed and automatically registered by the EVECelery workers should inherit from this base task.

    This BaseTask supports all methods and properties available by Celery's class-based `tasks <https://docs.celeryq.dev/en/stable/reference/celery.app.task.html>`_.
    """

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

    @validate_arguments
    def get_sync(self, kwargs_apply_async: Optional[dict] = None, kwargs_get: Optional[dict] = None, **kwargs):
        """
        Call this task and block until the result is available.

        Calls this celery task with additional helper functionality specific for
        EVECelery (deserialization to pydantic models support and result backend resource cleanup).
        This function is a wrapper around Celery's `task.apply_async() <https://docs.celeryq.dev/en/stable/reference/celery.app.task.html?highlight=apply_async#celery.app.task.Task.apply_async>`_
        and `AsyncResult.get() <https://docs.celeryq.dev/en/stable/reference/celery.result.html#celery.result.AsyncResult.get>`_ methods.

        :param Optional[dict] kwargs_apply_async: Dictionary of keyword arguments passed to `task.apply_async() <https://docs.celeryq.dev/en/stable/reference/celery.app.task.html?highlight=apply_async#celery.app.task.Task.apply_async>`_
        :param Optional[dict] kwargs_get: Dictionary of keyword arguments passed to `AsyncResult.get() <https://docs.celeryq.dev/en/stable/reference/celery.result.html#celery.result.AsyncResult.get>`_
        :param **kwargs: Keyword arguments passed to this task's :func:`~run` method.
        :return: Result of a task
        """
        if kwargs_apply_async is None:
            kwargs_apply_async = {}
        if kwargs_get is None:
            kwargs_get = {}
        f = self.apply_async(kwargs=kwargs, **kwargs_apply_async)
        result = f.get(**kwargs_get)
        f.forget()
        return result

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
