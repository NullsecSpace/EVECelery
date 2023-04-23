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


class Graphic(BaseModel):
    color: Optional[int] = Field(
        None,
        description='color integer',
        title='get_characters_character_id_medals_color',
    )
    graphic: str = Field(
        ...,
        description='graphic string',
        title='get_characters_character_id_medals_graphic_graphic',
    )
    layer: int = Field(
        ...,
        description='layer integer',
        title='get_characters_character_id_medals_layer',
    )
    part: int = Field(
        ..., description='part integer', title='get_characters_character_id_medals_part'
    )


class GetCharactersCharacterIdMedalsOkItem(BaseModel):
    corporation_id: int = Field(
        ...,
        description='corporation_id integer',
        title='get_characters_character_id_medals_corporation_id',
    )
    date: datetime = Field(
        ..., description='date string', title='get_characters_character_id_medals_date'
    )
    description: str = Field(
        ...,
        description='description string',
        title='get_characters_character_id_medals_description',
    )
    graphics: List[Graphic] = Field(
        ...,
        description='graphics array',
        max_items=9,
        min_items=3,
        title='get_characters_character_id_medals_graphics',
    )
    issuer_id: int = Field(
        ...,
        description='issuer_id integer',
        title='get_characters_character_id_medals_issuer_id',
    )
    medal_id: int = Field(
        ...,
        description='medal_id integer',
        title='get_characters_character_id_medals_medal_id',
    )
    reason: str = Field(
        ...,
        description='reason string',
        title='get_characters_character_id_medals_reason',
    )
    status: Literal['public', 'private'] = Field(
        ...,
        description='status string',
        title='get_characters_character_id_medals_status',
    )
    title: str = Field(
        ...,
        description='title string',
        title='get_characters_character_id_medals_title',
    )


class GetCharactersCharacterIdMedalsOk(BaseModel):
    __root__: List[GetCharactersCharacterIdMedalsOkItem] = Field(
        ...,
        description='200 ok array',
        max_items=1000,
        title='get_characters_character_id_medals_ok',
    )


class Headers200_get_characters_character_id_medals(ModelBaseEVECelery):
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


class Response200_get_characters_character_id_medals(ModelCachedResponse):
    """
    A list of medals

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "corporation_id": 98000001,
            "date": "2017-03-16T15:01:45Z",
            "description": "For 33 corp!",
            "graphics": [
              {
                "color": -1,
                "graphic": "caldari.1_1",
                "layer": 0,
                "part": 1
              },
              {
                "color": -330271,
                "graphic": "caldari.1_2",
                "layer": 1,
                "part": 1
              },
              {
                "color": -1,
                "graphic": "compass.1_2",
                "layer": 0,
                "part": 2
              }
            ],
            "issuer_id": 2112000002,
            "medal_id": 3,
            "reason": "Thanks!",
            "status": "private",
            "title": "33 tester medal"
          }
        ]

    """

    headers: Headers200_get_characters_character_id_medals = Field(
        ..., description='The response headers for this request.'
    )
    body: GetCharactersCharacterIdMedalsOk = Field(
        ..., description='The response body for this request.'
    )
