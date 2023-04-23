"""
A model definition module returned by an ESI task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Models.py'.
"""
from __future__ import annotations
from EVECelery.tasks.BaseTasks.Models.ModelsBase import ModelBaseEVECelery
from EVECelery.tasks.BaseTasks.Models.ModelsCached import ModelCachedResponse
from datetime import date
from typing import List

from pydantic import BaseModel, Field


class GetMarketsRegionIdHistoryOkItem(BaseModel):
    average: float = Field(
        ..., description='average number', title='get_markets_region_id_history_average'
    )
    date: date = Field(
        ...,
        description='The date of this historical statistic entry',
        title='get_markets_region_id_history_date',
    )
    highest: float = Field(
        ..., description='highest number', title='get_markets_region_id_history_highest'
    )
    lowest: float = Field(
        ..., description='lowest number', title='get_markets_region_id_history_lowest'
    )
    order_count: int = Field(
        ...,
        description='Total number of orders happened that day',
        title='get_markets_region_id_history_order_count',
    )
    volume: int = Field(
        ..., description='Total', title='get_markets_region_id_history_volume'
    )


class GetMarketsRegionIdHistoryOk(BaseModel):
    __root__: List[GetMarketsRegionIdHistoryOkItem] = Field(
        ...,
        description='200 ok array',
        max_items=500,
        title='get_markets_region_id_history_ok',
    )


class Headers200_get_markets_region_id_history(ModelBaseEVECelery):
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


class Response200_get_markets_region_id_history(ModelCachedResponse):
    """
    A list of historical market statistics

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "average": 5.25,
            "date": "2015-05-01",
            "highest": 5.27,
            "lowest": 5.11,
            "order_count": 2267,
            "volume": 16276782035
          }
        ]

    """

    headers: Headers200_get_markets_region_id_history = Field(
        ..., description='The response headers for this request.'
    )
    body: GetMarketsRegionIdHistoryOk = Field(
        ..., description='The response body for this request.'
    )
