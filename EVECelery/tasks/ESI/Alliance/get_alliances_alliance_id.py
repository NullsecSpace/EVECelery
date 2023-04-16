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


class ResponseSuccessHeaders200_get_alliances_alliance_id(ModelTaskBaseResponse):
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


class ResponseSuccess200_get_alliances_alliance_id(ModelCachedSuccess):
    """
    Public data about an alliance

    Response for response code 200. This is the response body model that also contains the headers.

    --Example responses from ESI:
    {
      "creator_corporation_id": 45678,
      "creator_id": 12345,
      "date_founded": "2016-06-26T21:00:00Z",
      "executor_corporation_id": 98356193,
      "name": "C C P Alliance",
      "ticker": "<C C P>"
    }

    """

    headers: ResponseSuccessHeaders200_get_alliances_alliance_id = Field(
        ..., description='The response headers for this request.'
    )
    creator_corporation_id: int = Field(
        default=..., description="ID of the corporation that created the alliance"
    )
    creator_id: int = Field(
        default=..., description="ID of the character that created the alliance"
    )
    date_founded: str = Field(default=..., description="date_founded string")
    executor_corporation_id: int | None = Field(
        description="the executor corporation ID, if this alliance is not closed"
    )
    faction_id: int | None = Field(
        description="Faction ID this alliance is fighting for, if this alliance is enlisted in factional warfare"
    )
    name: str = Field(default=..., description="the full name of the alliance")
    ticker: str = Field(default=..., description="the short name of the alliance")


class get_alliances_alliance_id(TaskESI):
    """
    Get alliance information
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
        return f"/alliances/{alliance_id}/"

    def cache_ttl_default(self) -> int:
        """
        TTL for when cache is unspecified.

        :return: The number of seconds to cache a response
        """
        return 3600  # current esi x-cached-seconds header

    @validate_arguments
    def get_sync(
        self,
        alliance_id: int,
        datasource: str = "tranquility",
        kwargs_apply_async: Optional[dict] = None,
        kwargs_get: Optional[dict] = None,
    ):
        """
        Get alliance information

        Public information about an alliance

        ---
        Alternate route: `/dev/alliances/{alliance_id}/`

        Alternate route: `/legacy/alliances/{alliance_id}/`

        Alternate route: `/v3/alliances/{alliance_id}/`

        Alternate route: `/v4/alliances/{alliance_id}/`

        ---
        This route is cached for up to 3600 seconds


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

        Get alliance information

        Public information about an alliance

        ---
        Alternate route: `/dev/alliances/{alliance_id}/`

        Alternate route: `/legacy/alliances/{alliance_id}/`

        Alternate route: `/v3/alliances/{alliance_id}/`

        Alternate route: `/v4/alliances/{alliance_id}/`

        ---
        This route is cached for up to 3600 seconds

        :param alliance_id: An EVE alliance ID
        :param datasource: The server name you would like data from -- ['tranquility']

        :return: The response from ESI as a JSON dictionary.
        """
        return super().run(alliance_id=alliance_id, datasource=datasource, **kwargs)