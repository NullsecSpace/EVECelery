"""
A task definition module with associated response models returned by the task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Task.py'.
"""

from typing import Union, Optional
from pydantic import validate_arguments
from EVECelery.tasks.BaseTasks.TaskESI import TaskESI

from .Models.get_characters_character_id_mail_200 import (
    Response200_get_characters_character_id_mail,
)


class get_characters_character_id_mail(TaskESI):
    """
    Return mail headers
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
        return f"/characters/{character_id}/mail/"

    def cache_ttl_default(self) -> int:
        """
        TTL for when cache is unspecified.

        :return: The number of seconds to cache a response
        """
        return 30  # current esi x-cached-seconds header

    @validate_arguments
    def get_sync(
        self,
        character_id: int,
        datasource: str = "tranquility",
        labels: list[int] | None = None,
        last_mail_id: int | None = None,
        token: str | None = None,
        kwargs_apply_async: Optional[dict] = None,
        kwargs_get: Optional[dict] = None,
    ) -> Union[Response200_get_characters_character_id_mail]:
        """
        Return mail headers

        Return the 50 most recent mail headers belonging to the character that match the query criteria. Queries can be filtered by label, and last_mail_id can be used to paginate backwards

        ---
        Alternate route: `/dev/characters/{character_id}/mail/`

        Alternate route: `/legacy/characters/{character_id}/mail/`

        Alternate route: `/v1/characters/{character_id}/mail/`

        ---
        This route is cached for up to 30 seconds


        NOTE: This function calls the task and blocks until the result is available. This function is a wrapper around Celery's `task.apply_async() <https://docs.celeryq.dev/en/stable/reference/celery.app.task.html?highlight=apply_async#celery.app.task.Task.apply_async>`_
        and `AsyncResult.get() <https://docs.celeryq.dev/en/stable/reference/celery.result.html#celery.result.AsyncResult.get>`_ methods.
        Instead of a dictionary, this function returns a pydantic model to more easily see what returned data responses look like, what is optionally returned, etc.

        If you would instead like to return an async result, use Celery's `apply_async() <https://docs.celeryq.dev/en/stable/reference/celery.app.task.html?highlight=apply_async#celery.app.task.Task.apply_async>`_ method on this task.

        :param character_id: An EVE character ID
        :param datasource: The server name you would like data from -- ['tranquility']
        :param labels: Fetch only mails that match one or more of the given labels
        :param last_mail_id: List only mail with an ID lower than the given ID, if present
        :param token: Access token to use if unable to set a header
        :param Optional[dict] kwargs_apply_async: Dictionary of keyword arguments passed to `task.apply_async() <https://docs.celeryq.dev/en/stable/reference/celery.app.task.html?highlight=apply_async#celery.app.task.Task.apply_async>`_
        :param Optional[dict] kwargs_get: Dictionary of keyword arguments passed to `AsyncResult.get() <https://docs.celeryq.dev/en/stable/reference/celery.result.html#celery.result.AsyncResult.get>`_
        :return: The response from ESI as a pydantic object. The response model will follow the structure of :class:`Response200_get_characters_character_id_mail`.
        """
        return super().get_sync(
            character_id=character_id,
            datasource=datasource,
            labels=labels,
            last_mail_id=last_mail_id,
            token=token,
            kwargs_apply_async=kwargs_apply_async,
            kwargs_get=kwargs_get,
        )

    @validate_arguments
    def run(
        self,
        character_id: int,
        datasource: str = "tranquility",
        labels: list[int] | None = None,
        last_mail_id: int | None = None,
        token: str | None = None,
        **kwargs,
    ) -> dict:
        """
        The task body that runs on the EVECelery worker

        This is the task body that runs on the EVECelery worker.

        IMPORTANT NOTE: You should not directly call this function from your client code as it will run within the context of your client and won't be sent to the message broker to run on a worker node.
        To correctly call this task body, see `Celery's documentation <https://docs.celeryq.dev/en/stable/userguide/calling.html>`_ on methods for calling tasks.

        See also this task's :func:`get_sync` which is a wrapper function around Celery's apply_async().get() call.

        Return mail headers

        Return the 50 most recent mail headers belonging to the character that match the query criteria. Queries can be filtered by label, and last_mail_id can be used to paginate backwards

        ---
        Alternate route: `/dev/characters/{character_id}/mail/`

        Alternate route: `/legacy/characters/{character_id}/mail/`

        Alternate route: `/v1/characters/{character_id}/mail/`

        ---
        This route is cached for up to 30 seconds

        :param character_id: An EVE character ID
        :param datasource: The server name you would like data from -- ['tranquility']
        :param labels: Fetch only mails that match one or more of the given labels
        :param last_mail_id: List only mail with an ID lower than the given ID, if present
        :param token: Access token to use if unable to set a header

        :return: The response from ESI as a JSON dictionary. The response dictionary will follow the structure of :class:`Response200_get_characters_character_id_mail`.
        """
        return super().run(
            character_id=character_id,
            datasource=datasource,
            labels=labels,
            last_mail_id=last_mail_id,
            token=token,
            **kwargs,
        )
