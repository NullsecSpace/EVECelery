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


class SuccessHeaders200_get_characters_character_id_search(ModelTaskBaseResponse):
    """
    Headers for response code 200
    """

    Cache_Control: str | None = Field(
        description="The caching mechanism used", alias="Cache-Control"
    )
    Content_Language: str | None = Field(
        description="The language used in the response", alias="Content-Language"
    )
    ETag: str | None = Field(description="RFC7232 compliant entity tag")
    Expires: str | None = Field(description="RFC7231 formatted datetime string")
    Last_Modified: str | None = Field(
        description="RFC7231 formatted datetime string", alias="Last-Modified"
    )


class Success200_get_characters_character_id_search(ModelCachedSuccess):
    """
    A list of search results

    Response for response code 200. This is the response body model that also contains the headers.

    Example responses from ESI:

    .. code-block:: json

        {
          "solar_system": [
            30002510
          ],
          "station": [
            60004588,
            60004594,
            60005725,
            60009106,
            60012721,
            60012724,
            60012727
          ]
        }

    """

    headers: SuccessHeaders200_get_characters_character_id_search = Field(
        ..., description='The response headers for this request.'
    )
    agent: list[int] | None = Field(description="agent array")
    alliance: list[int] | None = Field(description="alliance array")
    character: list[int] | None = Field(description="character array")
    constellation: list[int] | None = Field(description="constellation array")
    corporation: list[int] | None = Field(description="corporation array")
    faction: list[int] | None = Field(description="faction array")
    inventory_type: list[int] | None = Field(description="inventory_type array")
    region: list[int] | None = Field(description="region array")
    solar_system: list[int] | None = Field(description="solar_system array")
    station: list[int] | None = Field(description="station array")
    structure: list[int] | None = Field(description="structure array")


class get_characters_character_id_search(TaskESI):
    """
    Search on a string
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
        return f"/characters/{character_id}/search/"

    def cache_ttl_default(self) -> int:
        """
        TTL for when cache is unspecified.

        :return: The number of seconds to cache a response
        """
        return 3600  # current esi x-cached-seconds header

    @validate_arguments
    def get_sync(
        self,
        categories: list[str],
        character_id: int,
        search: str,
        datasource: str = "tranquility",
        language: str = "en",
        strict: bool = False,
        token: str | None = None,
        kwargs_apply_async: Optional[dict] = None,
        kwargs_get: Optional[dict] = None,
    ) -> Union[Success200_get_characters_character_id_search]:
        """
        Search on a string

        Search for entities that match a given sub-string.

        ---
        Alternate route: `/dev/characters/{character_id}/search/`

        Alternate route: `/legacy/characters/{character_id}/search/`

        Alternate route: `/v3/characters/{character_id}/search/`

        ---
        This route is cached for up to 3600 seconds


        NOTE: This function calls the task and blocks until the result is available. This function is a wrapper around Celery's `task.apply_async() <https://docs.celeryq.dev/en/stable/reference/celery.app.task.html?highlight=apply_async#celery.app.task.Task.apply_async>`_
        and `AsyncResult.get() <https://docs.celeryq.dev/en/stable/reference/celery.result.html#celery.result.AsyncResult.get>`_ methods.
        Instead of a dictionary, this function returns a pydantic model to more easily see what returned data responses look like, what is optionally returned, etc.

        If you would instead like to return an async result, use Celery's `apply_async() <https://docs.celeryq.dev/en/stable/reference/celery.app.task.html?highlight=apply_async#celery.app.task.Task.apply_async>`_ method on this task.

        :param categories: Type of entities to search for
        :param character_id: An EVE character ID
        :param search: The string to search on
        :param datasource: The server name you would like data from -- ['tranquility']
        :param language: Language to use in the response, takes precedence over Accept-Language -- ['en', 'en-us', 'de', 'fr', 'ja', 'ru', 'zh', 'ko', 'es']
        :param strict: Whether the search should be a strict match
        :param token: Access token to use if unable to set a header
        :param Optional[dict] kwargs_apply_async: Dictionary of keyword arguments passed to `task.apply_async() <https://docs.celeryq.dev/en/stable/reference/celery.app.task.html?highlight=apply_async#celery.app.task.Task.apply_async>`_
        :param Optional[dict] kwargs_get: Dictionary of keyword arguments passed to `AsyncResult.get() <https://docs.celeryq.dev/en/stable/reference/celery.result.html#celery.result.AsyncResult.get>`_
        :return: The response from ESI as a pydantic object. The response model will follow the structure of :class:`Success200_get_characters_character_id_search`.
        """
        return super().get_sync(
            categories=categories,
            character_id=character_id,
            search=search,
            datasource=datasource,
            language=language,
            strict=strict,
            token=token,
            kwargs_apply_async=kwargs_apply_async,
            kwargs_get=kwargs_get,
        )

    @validate_arguments
    def run(
        self,
        categories: list[str],
        character_id: int,
        search: str,
        datasource: str = "tranquility",
        language: str = "en",
        strict: bool = False,
        token: str | None = None,
        **kwargs,
    ) -> dict:
        """
        The task body that runs on the EVECelery worker

        This is the task body that runs on the EVECelery worker.

        IMPORTANT NOTE: You should not directly call this function from your client code as it will run within the context of your client and won't be sent to the message broker to run on a worker node.
        To correctly call this task body, see `Celery's documentation <https://docs.celeryq.dev/en/stable/userguide/calling.html>`_ on methods for calling tasks.

        See also this task's :func:`get_sync` which is a wrapper function around Celery's apply_async().get() call.

        Search on a string

        Search for entities that match a given sub-string.

        ---
        Alternate route: `/dev/characters/{character_id}/search/`

        Alternate route: `/legacy/characters/{character_id}/search/`

        Alternate route: `/v3/characters/{character_id}/search/`

        ---
        This route is cached for up to 3600 seconds

        :param categories: Type of entities to search for
        :param character_id: An EVE character ID
        :param search: The string to search on
        :param datasource: The server name you would like data from -- ['tranquility']
        :param language: Language to use in the response, takes precedence over Accept-Language -- ['en', 'en-us', 'de', 'fr', 'ja', 'ru', 'zh', 'ko', 'es']
        :param strict: Whether the search should be a strict match
        :param token: Access token to use if unable to set a header

        :return: The response from ESI as a JSON dictionary. The response dictionary will follow the structure of :class:`Success200_get_characters_character_id_search`.
        """
        return super().run(
            categories=categories,
            character_id=character_id,
            search=search,
            datasource=datasource,
            language=language,
            strict=strict,
            token=token,
            **kwargs,
        )
