"""
A task definition module with associated response models returned by the task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Task.py'.
"""

from typing import Union, Optional
from pydantic import validate_arguments
from EVECelery.tasks.BaseTasks.TaskESI import TaskESI

from .Models.get_corporations_corporation_id_contracts_contract_id_items_200 import (
    Response200_get_corporations_corporation_id_contracts_contract_id_items,
)


class get_corporations_corporation_id_contracts_contract_id_items(TaskESI):
    """
    Get corporation contract items
    """

    def request_method(self) -> str:
        """
        Returns the type of request made to ESI

        This method will return the request method (get, post, etc.) made to ESI.

        :return: Request method passed to requests.request()
        """
        return "get"

    def route(self, contract_id: int, corporation_id: int, **kwargs) -> str:
        """
        ESI route with input request parameters

        :param contract_id: ID of a contract
        :param corporation_id: An EVE corporation ID

        :return: ESI route with request path parameters if any
        """
        return f"/corporations/{corporation_id}/contracts/{contract_id}/items/"

    def cache_ttl_default(self) -> int:
        """
        TTL for when cache is unspecified.

        :return: The number of seconds to cache a response
        """
        return 3600  # current esi x-cached-seconds header

    @validate_arguments
    def get_sync(
        self,
        contract_id: int,
        corporation_id: int,
        datasource: str = "tranquility",
        token: str | None = None,
        kwargs_apply_async: Optional[dict] = None,
        kwargs_get: Optional[dict] = None,
    ) -> Union[Response200_get_corporations_corporation_id_contracts_contract_id_items]:
        """
        Get corporation contract items

        Lists items of a particular contract

        ---
        Alternate route: `/dev/corporations/{corporation_id}/contracts/{contract_id}/items/`

        Alternate route: `/legacy/corporations/{corporation_id}/contracts/{contract_id}/items/`

        Alternate route: `/v1/corporations/{corporation_id}/contracts/{contract_id}/items/`

        ---
        This route is cached for up to 3600 seconds


        NOTE: This function calls the task and blocks until the result is available. This function is a wrapper around Celery's `task.apply_async() <https://docs.celeryq.dev/en/stable/reference/celery.app.task.html?highlight=apply_async#celery.app.task.Task.apply_async>`_
        and `AsyncResult.get() <https://docs.celeryq.dev/en/stable/reference/celery.result.html#celery.result.AsyncResult.get>`_ methods.
        Instead of a dictionary, this function returns a pydantic model to more easily see what returned data responses look like, what is optionally returned, etc.

        If you would instead like to return an async result, use Celery's `apply_async() <https://docs.celeryq.dev/en/stable/reference/celery.app.task.html?highlight=apply_async#celery.app.task.Task.apply_async>`_ method on this task.

        :param contract_id: ID of a contract
        :param corporation_id: An EVE corporation ID
        :param datasource: The server name you would like data from -- ['tranquility']
        :param token: Access token to use if unable to set a header
        :param Optional[dict] kwargs_apply_async: Dictionary of keyword arguments passed to `task.apply_async() <https://docs.celeryq.dev/en/stable/reference/celery.app.task.html?highlight=apply_async#celery.app.task.Task.apply_async>`_
        :param Optional[dict] kwargs_get: Dictionary of keyword arguments passed to `AsyncResult.get() <https://docs.celeryq.dev/en/stable/reference/celery.result.html#celery.result.AsyncResult.get>`_
        :return: The response from ESI as a pydantic object. The response model will follow the structure of :class:`Response200_get_corporations_corporation_id_contracts_contract_id_items`.
        """
        return super().get_sync(
            contract_id=contract_id,
            corporation_id=corporation_id,
            datasource=datasource,
            token=token,
            kwargs_apply_async=kwargs_apply_async,
            kwargs_get=kwargs_get,
        )

    @validate_arguments
    def run(
        self,
        contract_id: int,
        corporation_id: int,
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

        Get corporation contract items

        Lists items of a particular contract

        ---
        Alternate route: `/dev/corporations/{corporation_id}/contracts/{contract_id}/items/`

        Alternate route: `/legacy/corporations/{corporation_id}/contracts/{contract_id}/items/`

        Alternate route: `/v1/corporations/{corporation_id}/contracts/{contract_id}/items/`

        ---
        This route is cached for up to 3600 seconds

        :param contract_id: ID of a contract
        :param corporation_id: An EVE corporation ID
        :param datasource: The server name you would like data from -- ['tranquility']
        :param token: Access token to use if unable to set a header

        :return: The response from ESI as a JSON dictionary. The response dictionary will follow the structure of :class:`Response200_get_corporations_corporation_id_contracts_contract_id_items`.
        """
        return super().run(
            contract_id=contract_id,
            corporation_id=corporation_id,
            datasource=datasource,
            token=token,
            **kwargs,
        )
