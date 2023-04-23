"""
A task definition module with associated response models returned by the task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Task.py'.
"""

from typing import Union, Optional
from pydantic import validate_arguments
from EVECelery.tasks.BaseTasks.TaskESI import TaskESI

from .Models.get_markets_region_id_orders_200 import (
    Response200_get_markets_region_id_orders,
)


class get_markets_region_id_orders(TaskESI):
    """
    List orders in a region
    """

    def request_method(self) -> str:
        """
        Returns the type of request made to ESI

        This method will return the request method (get, post, etc.) made to ESI.

        :return: Request method passed to requests.request()
        """
        return "get"

    def route(self, region_id: int, **kwargs) -> str:
        """
        ESI route with input request parameters

        :param region_id: Return orders in this region

        :return: ESI route with request path parameters if any
        """
        return f"/markets/{region_id}/orders/"

    def cache_ttl_default(self) -> int:
        """
        TTL for when cache is unspecified.

        :return: The number of seconds to cache a response
        """
        return 300  # current esi x-cached-seconds header

    @validate_arguments
    def get_sync(
        self,
        region_id: int,
        datasource: str = "tranquility",
        order_type: str = "all",
        page: int = 1,
        type_id: int | None = None,
        kwargs_apply_async: Optional[dict] = None,
        kwargs_get: Optional[dict] = None,
    ) -> Union[Response200_get_markets_region_id_orders]:
        """
        List orders in a region

        Return a list of orders in a region

        ---
        Alternate route: `/dev/markets/{region_id}/orders/`

        Alternate route: `/legacy/markets/{region_id}/orders/`

        Alternate route: `/v1/markets/{region_id}/orders/`

        ---
        This route is cached for up to 300 seconds


        NOTE: This function calls the task and blocks until the result is available. This function is a wrapper around Celery's `task.apply_async() <https://docs.celeryq.dev/en/stable/reference/celery.app.task.html?highlight=apply_async#celery.app.task.Task.apply_async>`_
        and `AsyncResult.get() <https://docs.celeryq.dev/en/stable/reference/celery.result.html#celery.result.AsyncResult.get>`_ methods.
        Instead of a dictionary, this function returns a pydantic model to more easily see what returned data responses look like, what is optionally returned, etc.

        If you would instead like to return an async result, use Celery's `apply_async() <https://docs.celeryq.dev/en/stable/reference/celery.app.task.html?highlight=apply_async#celery.app.task.Task.apply_async>`_ method on this task.

        :param region_id: Return orders in this region
        :param datasource: The server name you would like data from -- ['tranquility']
        :param order_type: Filter buy/sell orders, return all orders by default. If you query without type_id, we always return both buy and sell orders -- ['buy', 'sell', 'all']
        :param page: Which page of results to return
        :param type_id: Return orders only for this type
        :param Optional[dict] kwargs_apply_async: Dictionary of keyword arguments passed to `task.apply_async() <https://docs.celeryq.dev/en/stable/reference/celery.app.task.html?highlight=apply_async#celery.app.task.Task.apply_async>`_
        :param Optional[dict] kwargs_get: Dictionary of keyword arguments passed to `AsyncResult.get() <https://docs.celeryq.dev/en/stable/reference/celery.result.html#celery.result.AsyncResult.get>`_
        :return: The response from ESI as a pydantic object. The response model will follow the structure of :class:`Response200_get_markets_region_id_orders`.
        """
        return super().get_sync(
            region_id=region_id,
            datasource=datasource,
            order_type=order_type,
            page=page,
            type_id=type_id,
            kwargs_apply_async=kwargs_apply_async,
            kwargs_get=kwargs_get,
        )

    @validate_arguments
    def run(
        self,
        region_id: int,
        datasource: str = "tranquility",
        order_type: str = "all",
        page: int = 1,
        type_id: int | None = None,
        **kwargs,
    ) -> dict:
        """
        The task body that runs on the EVECelery worker

        This is the task body that runs on the EVECelery worker.

        IMPORTANT NOTE: You should not directly call this function from your client code as it will run within the context of your client and won't be sent to the message broker to run on a worker node.
        To correctly call this task body, see `Celery's documentation <https://docs.celeryq.dev/en/stable/userguide/calling.html>`_ on methods for calling tasks.

        See also this task's :func:`get_sync` which is a wrapper function around Celery's apply_async().get() call.

        List orders in a region

        Return a list of orders in a region

        ---
        Alternate route: `/dev/markets/{region_id}/orders/`

        Alternate route: `/legacy/markets/{region_id}/orders/`

        Alternate route: `/v1/markets/{region_id}/orders/`

        ---
        This route is cached for up to 300 seconds

        :param region_id: Return orders in this region
        :param datasource: The server name you would like data from -- ['tranquility']
        :param order_type: Filter buy/sell orders, return all orders by default. If you query without type_id, we always return both buy and sell orders -- ['buy', 'sell', 'all']
        :param page: Which page of results to return
        :param type_id: Return orders only for this type

        :return: The response from ESI as a JSON dictionary. The response dictionary will follow the structure of :class:`Response200_get_markets_region_id_orders`.
        """
        return super().run(
            region_id=region_id,
            datasource=datasource,
            order_type=order_type,
            page=page,
            type_id=type_id,
            **kwargs,
        )
