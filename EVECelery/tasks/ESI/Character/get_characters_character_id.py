"""
A task definition module with associated response models returned by the task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Task.py'.
"""

from EVECelery.tasks.BaseTasks.TaskESI import TaskESI
from EVECelery.tasks.BaseTasks.TaskBase import ModelTaskBaseResponse
from EVECelery.tasks.BaseTasks.TaskCached import (
    ModelCachedSuccess,
    ModelCachedException,
)
from pydantic import BaseModel, Field, validate_arguments
from typing import Union, Optional


class SuccessHeaders200_get_characters_character_id(ModelTaskBaseResponse):
    """
    Headers for response code 200
    """

    Cache_Control: str | None = Field(
        description="The caching mechanism used", alias="Cache-Control"
    )
    ETag: str | None = Field(description="RFC7232 compliant entity tag")
    Expires: str | None = Field(description="RFC7231 formatted datetime string")
    Last_Modified: str | None = Field(
        description="RFC7231 formatted datetime string", alias="Last-Modified"
    )


class Success200_get_characters_character_id(ModelCachedSuccess):
    """
    Public data for the given character

    Response for response code 200. This is the response body model that also contains the headers.

    Example responses from ESI:

    .. code-block:: json

        {
          "birthday": "2015-03-24T11:37:00Z",
          "bloodline_id": 3,
          "corporation_id": 109299958,
          "description": "",
          "gender": "male",
          "name": "CCP Bartender",
          "race_id": 2,
          "title": "All round pretty awesome guy"
        }

    """

    headers: SuccessHeaders200_get_characters_character_id = Field(
        ..., description='The response headers for this request.'
    )
    alliance_id: int | None = Field(description="The character's alliance ID")
    birthday: str = Field(default=..., description="Creation date of the character")
    bloodline_id: int = Field(default=..., description="bloodline_id integer")
    corporation_id: int = Field(
        default=..., description="The character's corporation ID"
    )
    description: str | None = Field(description="description string")
    faction_id: int | None = Field(
        description="ID of the faction the character is fighting for, if the character is enlisted in Factional Warfare"
    )
    gender: str = Field(default=..., description="gender string")
    name: str = Field(default=..., description="name string")
    race_id: int = Field(default=..., description="race_id integer")
    security_status: float | None = Field(description="security_status number")
    title: str | None = Field(description="The individual title of the character")


class get_characters_character_id(TaskESI):
    """
    Get character's public information
    """

    def request_method(self) -> str:
        """
        Returns the type of request made to ESI

        This method will return the request method (get, post, etc.) made to ESI.

        :return: Request method passed to requests.request()
        """
        return "get"

    def route(self, character_id: int, **kwargs) -> str:
        """
        ESI route with input request parameters

        :param character_id: An EVE character ID

        :return: ESI route with request path parameters if any
        """
        return f"/characters/{character_id}/"

    def cache_ttl_default(self) -> int:
        """
        TTL for when cache is unspecified.

        :return: The number of seconds to cache a response
        """
        return 86400  # current esi x-cached-seconds header

    @validate_arguments
    def get_sync(
        self,
        character_id: int,
        datasource: str = "tranquility",
        kwargs_apply_async: Optional[dict] = None,
        kwargs_get: Optional[dict] = None,
    ) -> Union[Success200_get_characters_character_id]:
        """
        Get character's public information

        Public information about a character

        ---
        Alternate route: `/dev/characters/{character_id}/`

        Alternate route: `/legacy/characters/{character_id}/`

        Alternate route: `/v5/characters/{character_id}/`

        ---
        This route is cached for up to 86400 seconds


        NOTE: This function calls the task and blocks until the result is available. This function is a wrapper around Celery's `task.apply_async() <https://docs.celeryq.dev/en/stable/reference/celery.app.task.html?highlight=apply_async#celery.app.task.Task.apply_async>`_
        and `AsyncResult.get() <https://docs.celeryq.dev/en/stable/reference/celery.result.html#celery.result.AsyncResult.get>`_ methods.
        Instead of a dictionary, this function returns a pydantic model to more easily see what returned data responses look like, what is optionally returned, etc.

        If you would instead like to return an async result, use Celery's `apply_async() <https://docs.celeryq.dev/en/stable/reference/celery.app.task.html?highlight=apply_async#celery.app.task.Task.apply_async>`_ method on this task.

        :param character_id: An EVE character ID
        :param datasource: The server name you would like data from -- ['tranquility']
        :param Optional[dict] kwargs_apply_async: Dictionary of keyword arguments passed to `task.apply_async() <https://docs.celeryq.dev/en/stable/reference/celery.app.task.html?highlight=apply_async#celery.app.task.Task.apply_async>`_
        :param Optional[dict] kwargs_get: Dictionary of keyword arguments passed to `AsyncResult.get() <https://docs.celeryq.dev/en/stable/reference/celery.result.html#celery.result.AsyncResult.get>`_
        :return: The response from ESI as a pydantic object. The response model will follow the structure of :class:`Success200_get_characters_character_id`.
        """
        return super().get_sync(
            character_id=character_id,
            datasource=datasource,
            kwargs_apply_async=kwargs_apply_async,
            kwargs_get=kwargs_get,
        )

    @validate_arguments
    def run(self, character_id: int, datasource: str = "tranquility", **kwargs) -> dict:
        """
        The task body that runs on the EVECelery worker

        This is the task body that runs on the EVECelery worker.

        IMPORTANT NOTE: You should not directly call this function from your client code as it will run within the context of your client and won't be sent to the message broker to run on a worker node.
        To correctly call this task body, see `Celery's documentation <https://docs.celeryq.dev/en/stable/userguide/calling.html>`_ on methods for calling tasks.

        See also this task's :func:`get_sync` which is a wrapper function around Celery's apply_async().get() call.

        Get character's public information

        Public information about a character

        ---
        Alternate route: `/dev/characters/{character_id}/`

        Alternate route: `/legacy/characters/{character_id}/`

        Alternate route: `/v5/characters/{character_id}/`

        ---
        This route is cached for up to 86400 seconds

        :param character_id: An EVE character ID
        :param datasource: The server name you would like data from -- ['tranquility']

        :return: The response from ESI as a JSON dictionary. The response dictionary will follow the structure of :class:`Success200_get_characters_character_id`.
        """
        return super().run(character_id=character_id, datasource=datasource, **kwargs)
