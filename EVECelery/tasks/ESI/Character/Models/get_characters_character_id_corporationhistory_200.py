"""
A model definition module returned by an ESI task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Models.py'.
"""
from __future__ import annotations
from EVECelery.tasks.BaseTasks.Models.ModelsBase import ModelBaseEVECelery
from EVECelery.tasks.BaseTasks.Models.ModelsCached import ModelCachedResponse
from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field


class GetCharactersCharacterIdCorporationhistoryOkItem(BaseModel):
    corporation_id: int = Field(
        ...,
        description='corporation_id integer',
        title='get_characters_character_id_corporationhistory_corporation_id',
    )
    is_deleted: Optional[bool] = Field(
        None,
        description='True if the corporation has been deleted',
        title='get_characters_character_id_corporationhistory_is_deleted',
    )
    record_id: int = Field(
        ...,
        description='An incrementing ID that can be used to canonically establish order of records in cases where dates may be ambiguous',
        title='get_characters_character_id_corporationhistory_record_id',
    )
    start_date: datetime = Field(
        ...,
        description='start_date string',
        title='get_characters_character_id_corporationhistory_start_date',
    )


class GetCharactersCharacterIdCorporationhistoryOk(BaseModel):
    __root__: List[GetCharactersCharacterIdCorporationhistoryOkItem] = Field(
        ...,
        description='200 ok array',
        max_items=10000,
        title='get_characters_character_id_corporationhistory_ok',
    )


class Headers200_get_characters_character_id_corporationhistory(ModelBaseEVECelery):
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


class Response200_get_characters_character_id_corporationhistory(ModelCachedResponse):
    """
    Corporation history for the given character

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "corporation_id": 90000001,
            "is_deleted": true,
            "record_id": 500,
            "start_date": "2016-06-26T20:00:00Z"
          },
          {
            "corporation_id": 90000002,
            "record_id": 501,
            "start_date": "2016-07-26T20:00:00Z"
          }
        ]

    """

    headers: Headers200_get_characters_character_id_corporationhistory = Field(
        ..., description='The response headers for this request.'
    )
    body: GetCharactersCharacterIdCorporationhistoryOk = Field(
        ..., description='The response body for this request.'
    )
