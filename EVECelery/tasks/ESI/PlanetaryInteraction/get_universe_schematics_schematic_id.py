"""
A task definition module with associated response models returned by the task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Task.py'.
"""

from typing import Union, Optional
from pydantic import validate_arguments
from EVECelery.tasks.BaseTasks.TaskESI import TaskESI

from .Models.get_universe_schematics_schematic_id_200 import (
    Response200_get_universe_schematics_schematic_id,
)


class get_universe_schematics_schematic_id(TaskESI):
    """
    Get schematic information
    """

    def request_method(self) -> str:
        """
        Returns the type of request made to ESI

        This method will return the request method (get, post, etc.) made to ESI.

        :return: Request method passed to requests.request()
        """
        return "get"

    def route(self, schematic_id: int, **kwargs) -> str:
        """
        ESI route with input request parameters

        :param schematic_id: A PI schematic ID

        :return: ESI route with request path parameters if any
        """
        return f"/universe/schematics/{schematic_id}/"

    def cache_ttl_default(self) -> int:
        """
        TTL for when cache is unspecified.

        :return: The number of seconds to cache a response
        """
        return 3600  # current esi x-cached-seconds header

    @validate_arguments
    def get_sync(
        self,
        schematic_id: int,
        datasource: str = "tranquility",
        kwargs_apply_async: Optional[dict] = None,
        kwargs_get: Optional[dict] = None,
    ) -> Union[Response200_get_universe_schematics_schematic_id]:
        """
        Get schematic information

        Get information on a planetary factory schematic

        ---
        Alternate route: `/dev/universe/schematics/{schematic_id}/`

        Alternate route: `/legacy/universe/schematics/{schematic_id}/`

        Alternate route: `/v1/universe/schematics/{schematic_id}/`

        ---
        This route is cached for up to 3600 seconds


        NOTE: This function calls the task and blocks until the result is available. This function is a wrapper around Celery's `task.apply_async() <https://docs.celeryq.dev/en/stable/reference/celery.app.task.html?highlight=apply_async#celery.app.task.Task.apply_async>`_
        and `AsyncResult.get() <https://docs.celeryq.dev/en/stable/reference/celery.result.html#celery.result.AsyncResult.get>`_ methods.
        Instead of a dictionary, this function returns a pydantic model to more easily see what returned data responses look like, what is optionally returned, etc.

        If you would instead like to return an async result, use Celery's `apply_async() <https://docs.celeryq.dev/en/stable/reference/celery.app.task.html?highlight=apply_async#celery.app.task.Task.apply_async>`_ method on this task.

        :param schematic_id: A PI schematic ID
        :param datasource: The server name you would like data from -- ['tranquility']
        :param Optional[dict] kwargs_apply_async: Dictionary of keyword arguments passed to `task.apply_async() <https://docs.celeryq.dev/en/stable/reference/celery.app.task.html?highlight=apply_async#celery.app.task.Task.apply_async>`_
        :param Optional[dict] kwargs_get: Dictionary of keyword arguments passed to `AsyncResult.get() <https://docs.celeryq.dev/en/stable/reference/celery.result.html#celery.result.AsyncResult.get>`_
        :return: The response from ESI as a pydantic object. The response model will follow the structure of :class:`Response200_get_universe_schematics_schematic_id`.
        """
        return super().get_sync(
            schematic_id=schematic_id,
            datasource=datasource,
            kwargs_apply_async=kwargs_apply_async,
            kwargs_get=kwargs_get,
        )

    @validate_arguments
    def run(self, schematic_id: int, datasource: str = "tranquility", **kwargs) -> dict:
        """
        The task body that runs on the EVECelery worker

        This is the task body that runs on the EVECelery worker.

        IMPORTANT NOTE: You should not directly call this function from your client code as it will run within the context of your client and won't be sent to the message broker to run on a worker node.
        To correctly call this task body, see `Celery's documentation <https://docs.celeryq.dev/en/stable/userguide/calling.html>`_ on methods for calling tasks.

        See also this task's :func:`get_sync` which is a wrapper function around Celery's apply_async().get() call.

        Get schematic information

        Get information on a planetary factory schematic

        ---
        Alternate route: `/dev/universe/schematics/{schematic_id}/`

        Alternate route: `/legacy/universe/schematics/{schematic_id}/`

        Alternate route: `/v1/universe/schematics/{schematic_id}/`

        ---
        This route is cached for up to 3600 seconds

        :param schematic_id: A PI schematic ID
        :param datasource: The server name you would like data from -- ['tranquility']

        :return: The response from ESI as a JSON dictionary. The response dictionary will follow the structure of :class:`Response200_get_universe_schematics_schematic_id`.
        """
        return super().run(schematic_id=schematic_id, datasource=datasource, **kwargs)
