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


class GetCorporationCorporationIdMiningObserversObserverIdOkItem(BaseModel):
    character_id: int = Field(
        ...,
        description='The character that did the mining\n',
        title='get_corporation_corporation_id_mining_observers_observer_id_character_id',
    )
    last_updated: date = Field(
        ...,
        description='last_updated string',
        title='get_corporation_corporation_id_mining_observers_observer_id_last_updated',
    )
    quantity: int = Field(
        ...,
        description='quantity integer',
        title='get_corporation_corporation_id_mining_observers_observer_id_quantity',
    )
    recorded_corporation_id: int = Field(
        ...,
        description='The corporation id of the character at the time data was recorded.\n',
        title='get_corporation_corporation_id_mining_observers_observer_id_recorded_corporation_id',
    )
    type_id: int = Field(
        ...,
        description='type_id integer',
        title='get_corporation_corporation_id_mining_observers_observer_id_type_id',
    )


class GetCorporationCorporationIdMiningObserversObserverIdOk(BaseModel):
    __root__: List[GetCorporationCorporationIdMiningObserversObserverIdOkItem] = Field(
        ...,
        description='200 ok array',
        max_items=1000,
        title='get_corporation_corporation_id_mining_observers_observer_id_ok',
    )


class Headers200_get_corporation_corporation_id_mining_observers_observer_id(
    ModelBaseEVECelery
):
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


class Response200_get_corporation_corporation_id_mining_observers_observer_id(
    ModelCachedResponse
):
    """
    Mining ledger of an observer

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "character_id": 95465499,
            "last_updated": "2017-09-19",
            "quantity": 500,
            "recorded_corporation_id": 109299958,
            "type_id": 1230
          }
        ]

    """

    headers: Headers200_get_corporation_corporation_id_mining_observers_observer_id = (
        Field(..., description='The response headers for this request.')
    )
    body: GetCorporationCorporationIdMiningObserversObserverIdOk = Field(
        ..., description='The response body for this request.'
    )
