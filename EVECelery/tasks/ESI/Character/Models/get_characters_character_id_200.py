"""
A model definition module returned by an ESI task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Models.py'.
"""
from __future__ import annotations
from EVECelery.tasks.BaseTasks.Models.ModelsBase import ModelBaseEVECelery
from EVECelery.tasks.BaseTasks.Models.ModelsCached import ModelCachedResponse
from datetime import datetime
from typing import Literal, Optional

from pydantic import BaseModel, Field, confloat


class GetCharactersCharacterIdOk(BaseModel):
    alliance_id: Optional[int] = Field(
        None,
        description="The character's alliance ID",
        title='get_characters_character_id_alliance_id',
    )
    birthday: datetime = Field(
        ...,
        description='Creation date of the character',
        title='get_characters_character_id_birthday',
    )
    bloodline_id: int = Field(
        ...,
        description='bloodline_id integer',
        title='get_characters_character_id_bloodline_id',
    )
    corporation_id: int = Field(
        ...,
        description="The character's corporation ID",
        title='get_characters_character_id_corporation_id',
    )
    description: Optional[str] = Field(
        None,
        description='description string',
        title='get_characters_character_id_description',
    )
    faction_id: Optional[int] = Field(
        None,
        description='ID of the faction the character is fighting for, if the character is enlisted in Factional Warfare',
        title='get_characters_character_id_faction_id',
    )
    gender: Literal['female', 'male'] = Field(
        ..., description='gender string', title='get_characters_character_id_gender'
    )
    name: str = Field(
        ..., description='name string', title='get_characters_character_id_name'
    )
    race_id: int = Field(
        ..., description='race_id integer', title='get_characters_character_id_race_id'
    )
    security_status: Optional[confloat(ge=-10.0, le=10.0)] = Field(
        None,
        description='security_status number',
        title='get_characters_character_id_security_status',
    )
    title: Optional[str] = Field(
        None,
        description='The individual title of the character',
        title='get_characters_character_id_title',
    )


class Headers200_get_characters_character_id(ModelBaseEVECelery):
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


class Response200_get_characters_character_id(ModelCachedResponse):
    """
    Public data for the given character

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        {
          "birthday": "2015-03-24T11:37:00Z",
          "bloodline_id": 3,
          "corporation_id": 109299958,
          "description": "",
          "gender": "male",
          "name": "CCP Bartender",
          "race_id": 2,
          "title": "All round pretty awesome guy"
        }

    """

    headers: Headers200_get_characters_character_id = Field(
        ..., description='The response headers for this request.'
    )
    body: GetCharactersCharacterIdOk = Field(
        ..., description='The response body for this request.'
    )
