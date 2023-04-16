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


class ResponseSuccessHeaders200_get_alliances_alliance_id_icons(ModelTaskBaseResponse):
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


class ResponseSuccess200_get_alliances_alliance_id_icons(ModelCachedSuccess):
    """
    Icon URLs for the given alliance id and server

    Response for response code 200. This is the response body model that also contains the headers.

    --Example responses from ESI:
    {
      "px128x128": "https://images.evetech.net/Alliance/503818424_128.png",
      "px64x64": "https://images.evetech.net/Alliance/503818424_64.png"
    }

    """

    headers: ResponseSuccessHeaders200_get_alliances_alliance_id_icons = Field(
        ..., description='The response headers for this request.'
    )
    px128x128: str | None = Field(description="px128x128 string")
    px64x64: str | None = Field(description="px64x64 string")


class get_alliances_alliance_id_icons(TaskESI):
    """
    Get alliance icon
    """

    def request_method(self) -> str:
        """
        Returns the type of request made to ESI

        This method will return the request method (get, post, etc.) made to ESI.

        :return: Request method passed to requests.request()
        """
        return "get"

    def route(self, alliance_id: int, **kwargs) -> str:
        """
        ESI route with input request parameters

        :param alliance_id: An EVE alliance ID

        :return: ESI route with request path parameters if any
        """
        return f"/alliances/{alliance_id}/icons/"

    def cache_ttl_default(self) -> int:
        """
        TTL for when cache is unspecified.

        :return: The number of seconds to cache a response
        """
        return 60  # current esi x-cached-seconds header

    @validate_arguments
    def get_sync(
        self,
        alliance_id: int,
        datasource: str = "tranquility",
        kwargs_apply_async: Optional[dict] = None,
        kwargs_get: Optional[dict] = None,
    ):
        """
        Get alliance icon

        Get the icon urls for a alliance

        ---
        Alternate route: `/legacy/alliances/{alliance_id}/icons/`

        Alternate route: `/v1/alliances/{alliance_id}/icons/`

        ---
        This route expires daily at 11:05

        ---
        [Diff of the upcoming changes](https://esi.evetech.net/diff/latest/dev/#GET-/alliances/{alliance_id}/icons/)


        NOTE: This function calls the task and blocks until the result is available. This function is a wrapper around Celery's `task.apply_async() <https://docs.celeryq.dev/en/stable/reference/celery.app.task.html?highlight=apply_async#celery.app.task.Task.apply_async>`_
        and `AsyncResult.get() <https://docs.celeryq.dev/en/stable/reference/celery.result.html#celery.result.AsyncResult.get>`_ methods.
        Instead of a dictionary, this function returns a pydantic model to more easily see what returned data responses look like, what is optionally returned, etc.

        If you would instead like to return an async result, use Celery's `apply_async() <https://docs.celeryq.dev/en/stable/reference/celery.app.task.html?highlight=apply_async#celery.app.task.Task.apply_async>`_ method on this task.

        :param alliance_id: An EVE alliance ID
        :param datasource: The server name you would like data from -- ['tranquility']
        :param Optional[dict] kwargs_apply_async: Dictionary of keyword arguments passed to `task.apply_async() <https://docs.celeryq.dev/en/stable/reference/celery.app.task.html?highlight=apply_async#celery.app.task.Task.apply_async>`_
        :param Optional[dict] kwargs_get: Dictionary of keyword arguments passed to `AsyncResult.get() <https://docs.celeryq.dev/en/stable/reference/celery.result.html#celery.result.AsyncResult.get>`_
        :return: The response from ESI as a pydantic object.
        """
        return super().get_sync(
            alliance_id=alliance_id,
            datasource=datasource,
            kwargs_apply_async=kwargs_apply_async,
            kwargs_get=kwargs_get,
        )

    @validate_arguments
    def run(self, alliance_id: int, datasource: str = "tranquility", **kwargs) -> dict:
        """
        The task body that runs on the EVECelery worker

        This is the task body that runs on the EVECelery worker.

        IMPORTANT NOTE: You should not directly call this function from your client code as it will run within the context of your client and won't be sent to the message broker to run on a worker node.
        To correctly call this task body, see `Celery's documentation <https://docs.celeryq.dev/en/stable/userguide/calling.html>`_ on methods for calling tasks.

        See also this task's :func:`get_sync` which is a wrapper function around Celery's apply_async().get() call.

        Get alliance icon

        Get the icon urls for a alliance

        ---
        Alternate route: `/legacy/alliances/{alliance_id}/icons/`

        Alternate route: `/v1/alliances/{alliance_id}/icons/`

        ---
        This route expires daily at 11:05

        ---
        [Diff of the upcoming changes](https://esi.evetech.net/diff/latest/dev/#GET-/alliances/{alliance_id}/icons/)

        :param alliance_id: An EVE alliance ID
        :param datasource: The server name you would like data from -- ['tranquility']

        :return: The response from ESI as a JSON dictionary.
        """
        return super().run(alliance_id=alliance_id, datasource=datasource, **kwargs)
