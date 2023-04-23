"""
A model definition module returned by an ESI task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Models.py'.
"""
from __future__ import annotations
from EVECelery.tasks.BaseTasks.Models.ModelsBase import ModelBaseEVECelery
from EVECelery.tasks.BaseTasks.Models.ModelsCached import ModelCachedResponse
from datetime import datetime
from typing import List, Literal, Optional

from pydantic import BaseModel, Field


class GetCharactersCharacterIdOrdersOkItem(BaseModel):
    duration: int = Field(
        ...,
        description='Number of days for which order is valid (starting from the issued date). An order expires at time issued + duration',
        title='get_characters_character_id_orders_duration',
    )
    escrow: Optional[float] = Field(
        None,
        description='For buy orders, the amount of ISK in escrow',
        title='get_characters_character_id_orders_escrow',
    )
    is_buy_order: Optional[bool] = Field(
        None,
        description='True if the order is a bid (buy) order',
        title='get_characters_character_id_orders_is_buy_order',
    )
    is_corporation: bool = Field(
        ...,
        description='Signifies whether the buy/sell order was placed on behalf of a corporation.',
        title='get_characters_character_id_orders_is_corporation',
    )
    issued: datetime = Field(
        ...,
        description='Date and time when this order was issued',
        title='get_characters_character_id_orders_issued',
    )
    location_id: int = Field(
        ...,
        description='ID of the location where order was placed',
        title='get_characters_character_id_orders_location_id',
    )
    min_volume: Optional[int] = Field(
        None,
        description='For buy orders, the minimum quantity that will be accepted in a matching sell order',
        title='get_characters_character_id_orders_min_volume',
    )
    order_id: int = Field(
        ...,
        description='Unique order ID',
        title='get_characters_character_id_orders_order_id',
    )
    price: float = Field(
        ...,
        description='Cost per unit for this order',
        title='get_characters_character_id_orders_price',
    )
    range: Literal[
        '1',
        '10',
        '2',
        '20',
        '3',
        '30',
        '4',
        '40',
        '5',
        'region',
        'solarsystem',
        'station',
    ] = Field(
        ...,
        description='Valid order range, numbers are ranges in jumps',
        title='get_characters_character_id_orders_range',
    )
    region_id: int = Field(
        ...,
        description='ID of the region where order was placed',
        title='get_characters_character_id_orders_region_id',
    )
    type_id: int = Field(
        ...,
        description='The type ID of the item transacted in this order',
        title='get_characters_character_id_orders_type_id',
    )
    volume_remain: int = Field(
        ...,
        description='Quantity of items still required or offered',
        title='get_characters_character_id_orders_volume_remain',
    )
    volume_total: int = Field(
        ...,
        description='Quantity of items required or offered at time order was placed',
        title='get_characters_character_id_orders_volume_total',
    )


class GetCharactersCharacterIdOrdersOk(BaseModel):
    __root__: List[GetCharactersCharacterIdOrdersOkItem] = Field(
        ...,
        description='200 ok array',
        max_items=305,
        title='get_characters_character_id_orders_ok',
    )


class Headers200_get_characters_character_id_orders(ModelBaseEVECelery):
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


class Response200_get_characters_character_id_orders(ModelCachedResponse):
    """
    Open market orders placed by a character

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "duration": 30,
            "escrow": 45.6,
            "is_buy_order": true,
            "is_corporation": false,
            "issued": "2016-09-03T05:12:25Z",
            "location_id": 456,
            "min_volume": 1,
            "order_id": 123,
            "price": 33.3,
            "range": "station",
            "region_id": 123,
            "type_id": 456,
            "volume_remain": 4422,
            "volume_total": 123456
          }
        ]

    """

    headers: Headers200_get_characters_character_id_orders = Field(
        ..., description='The response headers for this request.'
    )
    body: GetCharactersCharacterIdOrdersOk = Field(
        ..., description='The response body for this request.'
    )
