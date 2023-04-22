from celery import Task
from typing import Optional, Union, Type
from pydantic import BaseModel, validate_arguments
import json
import sys
import inspect
from .Models.ModelsBase import ModelBaseWithModelInfo


class TaskBase(Task):
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

    @classmethod
    @validate_arguments
    def reflection_get_model(cls, model_name: str):
        """
        Lookup a pydantic model in the current module by its string name.

        Resolves a pydantic model existing or imported by the current module by its name.
        :param model_name: The class name to lookup

        """
        if model_name is None:
            raise KeyError('The data from Redis did not include the "pydantic_model" attribute. '
                           'This is required for deserializing previously serialized pydantic model. '
                           'Insure your model inherits from ModelCachedResponse.')
        model = getattr(sys.modules[cls.__module__], model_name)
        if not inspect.isclass(model):
            raise TypeError('Expected lookup value to be a class')
        if not issubclass(model, BaseModel):
            raise TypeError('The specified class does not inherit from pydantic BaseModel')
        return model

    @classmethod
    @validate_arguments
    def to_pydantic(cls, json_data: Union[str, dict]) -> Type[ModelBaseWithModelInfo]:
        """
        Deserialize a JSON serialized string to a pydantic model.

        This function will deserialize a json string to a pydantic model.
        It will also create a pydantic model from a dictionary if the data has been deserialized elsewhere.

        For this function to correctly identify the pydantic model to generate the input must contain the 'pydantic_model' key.
        This key refers to the name of the pydantic class model within the calling module.
        The pydantic model to generate must exist within the current module's namespace and its name must exactly match the 'pydantic_model' value.

        :param json_data: The JSON data to deserialize. If this is a string it is first deserialized using json.loads().
            If this is a dictionary it is directly parsed by the pydantic model.

        :raises KeyError: If the input data does not contain the 'pydantic_model' key.
        :raises AttributeError: If the lookup key from 'pydantic_model' is unable to find the specified model
        :raises TypeError: If the lookup key refers to an unexpected type
        :returns: The deserialized JSON data as a pydantic object.
        """
        if isinstance(json_data, str):
            deserialized_data = json.loads(json_data)
        else:
            deserialized_data: dict = json_data
        model = cls.reflection_get_model(deserialized_data.get('pydantic_model'))
        if not issubclass(model, ModelBaseWithModelInfo):
            raise TypeError('Lookup model must inherit from ModelBaseWithModelInfo.')
        return model(**deserialized_data)

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

        :examples:
        >>> TaskBase.get_sync(kwargs_get={'timeout': 5}) # equivalent to BaseTask.apply_async().get(timeout=5)

        >>> r = TaskBase.get_sync() # equivalent to BaseTask.apply_async().get()

        >>> r = TaskBase.get_sync(lookup_id=5) # equivalent to BaseTask.apply_async(kwargs={'lookup_id': 5}).get()
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
