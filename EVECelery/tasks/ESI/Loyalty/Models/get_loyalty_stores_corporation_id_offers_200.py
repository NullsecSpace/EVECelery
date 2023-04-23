"""
A model definition module returned by an ESI task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Models.py'.
"""
from __future__ import annotations
from EVECelery.tasks.BaseTasks.Models.ModelsBase import ModelBaseEVECelery
from EVECelery.tasks.BaseTasks.Models.ModelsCached import ModelCachedResponse
from typing import List, Optional

from pydantic import BaseModel, Field


class RequiredItem(BaseModel):
    quantity: int = Field(
        ...,
        description='quantity integer',
        title='get_loyalty_stores_corporation_id_offers_required_item_quantity',
    )
    type_id: int = Field(
        ...,
        description='type_id integer',
        title='get_loyalty_stores_corporation_id_offers_required_item_type_id',
    )


class GetLoyaltyStoresCorporationIdOffersOkItem(BaseModel):
    ak_cost: Optional[int] = Field(
        None,
        description='Analysis kredit cost',
        title='get_loyalty_stores_corporation_id_offers_ak_cost',
    )
    isk_cost: int = Field(
        ...,
        description='isk_cost integer',
        title='get_loyalty_stores_corporation_id_offers_isk_cost',
    )
    lp_cost: int = Field(
        ...,
        description='lp_cost integer',
        title='get_loyalty_stores_corporation_id_offers_lp_cost',
    )
    offer_id: int = Field(
        ...,
        description='offer_id integer',
        title='get_loyalty_stores_corporation_id_offers_offer_id',
    )
    quantity: int = Field(
        ...,
        description='quantity integer',
        title='get_loyalty_stores_corporation_id_offers_quantity',
    )
    required_items: List[RequiredItem] = Field(
        ...,
        description='required_items array',
        max_items=100,
        title='get_loyalty_stores_corporation_id_offers_required_items',
    )
    type_id: int = Field(
        ...,
        description='type_id integer',
        title='get_loyalty_stores_corporation_id_offers_type_id',
    )


class GetLoyaltyStoresCorporationIdOffersOk(BaseModel):
    __root__: List[GetLoyaltyStoresCorporationIdOffersOkItem] = Field(
        ...,
        description='200 ok array',
        max_items=10000,
        title='get_loyalty_stores_corporation_id_offers_ok',
    )


class Headers200_get_loyalty_stores_corporation_id_offers(ModelBaseEVECelery):
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


class Response200_get_loyalty_stores_corporation_id_offers(ModelCachedResponse):
    """
    A list of offers

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "ak_cost": 35000,
            "isk_cost": 0,
            "lp_cost": 100,
            "offer_id": 1,
            "quantity": 1,
            "required_items": [],
            "type_id": 123
          },
          {
            "isk_cost": 1000,
            "lp_cost": 100,
            "offer_id": 2,
            "quantity": 10,
            "required_items": [
              {
                "quantity": 10,
                "type_id": 1234
              }
            ],
            "type_id": 1235
          }
        ]

    """

    headers: Headers200_get_loyalty_stores_corporation_id_offers = Field(
        ..., description='The response headers for this request.'
    )
    body: GetLoyaltyStoresCorporationIdOffersOk = Field(
        ..., description='The response body for this request.'
    )
