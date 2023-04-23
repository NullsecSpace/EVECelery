"""
A task definition module with associated response models returned by the task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Task.py'.
"""

from typing import Union, Optional
from pydantic import validate_arguments
from EVECelery.tasks.BaseTasks.TaskESI import TaskESI

from .Models.post_ui_autopilot_waypoint_204 import (
    Response204_post_ui_autopilot_waypoint,
)


class post_ui_autopilot_waypoint(TaskESI):
    """
    Set Autopilot Waypoint
    """

    def request_method(self) -> str:
        """
        Returns the type of request made to ESI

        This method will return the request method (get, post, etc.) made to ESI.

        :return: Request method passed to requests.request()
        """
        return "post"

    def route(self, **kwargs) -> str:
        """
        ESI route with input request parameters


        :return: ESI route with request path parameters if any
        """
        return f"/ui/autopilot/waypoint/"

    def cache_ttl_default(self) -> int:
        """
        TTL for when cache is unspecified.

        :return: The number of seconds to cache a response
        """
        return 60  # current esi x-cached-seconds header

    @validate_arguments
    def get_sync(
        self,
        destination_id: int,
        add_to_beginning: bool = False,
        clear_other_waypoints: bool = False,
        datasource: str = "tranquility",
        token: str | None = None,
        kwargs_apply_async: Optional[dict] = None,
        kwargs_get: Optional[dict] = None,
    ) -> Union[Response204_post_ui_autopilot_waypoint]:
        """
        Set Autopilot Waypoint

        Set a solar system as autopilot waypoint

        ---
        Alternate route: `/dev/ui/autopilot/waypoint/`

        Alternate route: `/legacy/ui/autopilot/waypoint/`

        Alternate route: `/v2/ui/autopilot/waypoint/`



        NOTE: This function calls the task and blocks until the result is available. This function is a wrapper around Celery's `task.apply_async() <https://docs.celeryq.dev/en/stable/reference/celery.app.task.html?highlight=apply_async#celery.app.task.Task.apply_async>`_
        and `AsyncResult.get() <https://docs.celeryq.dev/en/stable/reference/celery.result.html#celery.result.AsyncResult.get>`_ methods.
        Instead of a dictionary, this function returns a pydantic model to more easily see what returned data responses look like, what is optionally returned, etc.

        If you would instead like to return an async result, use Celery's `apply_async() <https://docs.celeryq.dev/en/stable/reference/celery.app.task.html?highlight=apply_async#celery.app.task.Task.apply_async>`_ method on this task.

        :param destination_id: The destination to travel to, can be solar system, station or structure's id
        :param add_to_beginning: Whether this solar system should be added to the beginning of all waypoints
        :param clear_other_waypoints: Whether clean other waypoints beforing adding this one
        :param datasource: The server name you would like data from -- ['tranquility']
        :param token: Access token to use if unable to set a header
        :param Optional[dict] kwargs_apply_async: Dictionary of keyword arguments passed to `task.apply_async() <https://docs.celeryq.dev/en/stable/reference/celery.app.task.html?highlight=apply_async#celery.app.task.Task.apply_async>`_
        :param Optional[dict] kwargs_get: Dictionary of keyword arguments passed to `AsyncResult.get() <https://docs.celeryq.dev/en/stable/reference/celery.result.html#celery.result.AsyncResult.get>`_
        :return: The response from ESI as a pydantic object. The response model will follow the structure of :class:`Response204_post_ui_autopilot_waypoint`.
        """
        return super().get_sync(
            destination_id=destination_id,
            add_to_beginning=add_to_beginning,
            clear_other_waypoints=clear_other_waypoints,
            datasource=datasource,
            token=token,
            kwargs_apply_async=kwargs_apply_async,
            kwargs_get=kwargs_get,
        )

    @validate_arguments
    def run(
        self,
        destination_id: int,
        add_to_beginning: bool = False,
        clear_other_waypoints: bool = False,
        datasource: str = "tranquility",
        token: str | None = None,
        **kwargs,
    ) -> dict:
        """
        The task body that runs on the EVECelery worker

        This is the task body that runs on the EVECelery worker.

        IMPORTANT NOTE: You should not directly call this function from your client code as it will run within the context of your client and won't be sent to the message broker to run on a worker node.
        To correctly call this task body, see `Celery's documentation <https://docs.celeryq.dev/en/stable/userguide/calling.html>`_ on methods for calling tasks.

        See also this task's :func:`get_sync` which is a wrapper function around Celery's apply_async().get() call.

        Set Autopilot Waypoint

        Set a solar system as autopilot waypoint

        ---
        Alternate route: `/dev/ui/autopilot/waypoint/`

        Alternate route: `/legacy/ui/autopilot/waypoint/`

        Alternate route: `/v2/ui/autopilot/waypoint/`


        :param destination_id: The destination to travel to, can be solar system, station or structure's id
        :param add_to_beginning: Whether this solar system should be added to the beginning of all waypoints
        :param clear_other_waypoints: Whether clean other waypoints beforing adding this one
        :param datasource: The server name you would like data from -- ['tranquility']
        :param token: Access token to use if unable to set a header

        :return: The response from ESI as a JSON dictionary. The response dictionary will follow the structure of :class:`Response204_post_ui_autopilot_waypoint`.
        """
        return super().run(
            destination_id=destination_id,
            add_to_beginning=add_to_beginning,
            clear_other_waypoints=clear_other_waypoints,
            datasource=datasource,
            token=token,
            **kwargs,
        )
