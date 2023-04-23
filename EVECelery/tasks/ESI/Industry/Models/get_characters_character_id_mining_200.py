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


class GetCharactersCharacterIdMiningOkItem(BaseModel):
    date: date = Field(
        ..., description='date string', title='get_characters_character_id_mining_date'
    )
    quantity: int = Field(
        ...,
        description='quantity integer',
        title='get_characters_character_id_mining_quantity',
    )
    solar_system_id: int = Field(
        ...,
        description='solar_system_id integer',
        title='get_characters_character_id_mining_solar_system_id',
    )
    type_id: int = Field(
        ...,
        description='type_id integer',
        title='get_characters_character_id_mining_type_id',
    )


class GetCharactersCharacterIdMiningOk(BaseModel):
    __root__: List[GetCharactersCharacterIdMiningOkItem] = Field(
        ...,
        description='200 ok array',
        max_items=1000,
        title='get_characters_character_id_mining_ok',
    )


class Headers200_get_characters_character_id_mining(ModelBaseEVECelery):
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


class Response200_get_characters_character_id_mining(ModelCachedResponse):
    """
    Mining ledger of a character

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "date": "2017-09-19",
            "quantity": 7004,
            "solar_system_id": 30003707,
            "type_id": 17471
          },
          {
            "date": "2017-09-18",
            "quantity": 5199,
            "solar_system_id": 30003707,
            "type_id": 17471
          }
        ]

    """

    headers: Headers200_get_characters_character_id_mining = Field(
        ..., description='The response headers for this request.'
    )
    body: GetCharactersCharacterIdMiningOk = Field(
        ..., description='The response body for this request.'
    )
