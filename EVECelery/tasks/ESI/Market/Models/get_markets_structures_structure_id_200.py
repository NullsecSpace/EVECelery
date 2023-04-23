"""
A model definition module returned by an ESI task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Models.py'.
"""
from __future__ import annotations
from EVECelery.tasks.BaseTasks.Models.ModelsBase import ModelBaseEVECelery
from EVECelery.tasks.BaseTasks.Models.ModelsCached import ModelCachedResponse
from datetime import datetime
from typing import List, Literal

from pydantic import BaseModel, Field


class GetMarketsStructuresStructureIdOkItem(BaseModel):
    duration: int = Field(
        ...,
        description='duration integer',
        title='get_markets_structures_structure_id_duration',
    )
    is_buy_order: bool = Field(
        ...,
        description='is_buy_order boolean',
        title='get_markets_structures_structure_id_is_buy_order',
    )
    issued: datetime = Field(
        ...,
        description='issued string',
        title='get_markets_structures_structure_id_issued',
    )
    location_id: int = Field(
        ...,
        description='location_id integer',
        title='get_markets_structures_structure_id_location_id',
    )
    min_volume: int = Field(
        ...,
        description='min_volume integer',
        title='get_markets_structures_structure_id_min_volume',
    )
    order_id: int = Field(
        ...,
        description='order_id integer',
        title='get_markets_structures_structure_id_order_id',
    )
    price: float = Field(
        ...,
        description='price number',
        title='get_markets_structures_structure_id_price',
    )
    range: Literal[
        'station',
        'region',
        'solarsystem',
        '1',
        '2',
        '3',
        '4',
        '5',
        '10',
        '20',
        '30',
        '40',
    ] = Field(
        ...,
        description='range string',
        title='get_markets_structures_structure_id_range',
    )
    type_id: int = Field(
        ...,
        description='type_id integer',
        title='get_markets_structures_structure_id_type_id',
    )
    volume_remain: int = Field(
        ...,
        description='volume_remain integer',
        title='get_markets_structures_structure_id_volume_remain',
    )
    volume_total: int = Field(
        ...,
        description='volume_total integer',
        title='get_markets_structures_structure_id_volume_total',
    )


class GetMarketsStructuresStructureIdOk(BaseModel):
    __root__: List[GetMarketsStructuresStructureIdOkItem] = Field(
        ...,
        description='200 ok array',
        max_items=1000,
        title='get_markets_structures_structure_id_ok',
    )


class Headers200_get_markets_structures_structure_id(ModelBaseEVECelery):
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
    X_Pages: int | None = Field(description="Maximum page number", alias="X-Pages")


class Response200_get_markets_structures_structure_id(ModelCachedResponse):
    """
    A list of orders

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "duration": 90,
            "is_buy_order": false,
            "issued": "2016-09-03T05:12:25Z",
            "location_id": 1020988381992,
            "min_volume": 1,
            "order_id": 4623824223,
            "price": 9.9,
            "range": "region",
            "type_id": 34,
            "volume_remain": 1296000,
            "volume_total": 2000000
          }
        ]

    """

    headers: Headers200_get_markets_structures_structure_id = Field(
        ..., description='The response headers for this request.'
    )
    body: GetMarketsStructuresStructureIdOk = Field(
        ..., description='The response body for this request.'
    )
