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


class HomeLocation(BaseModel):
    location_id: Optional[int] = Field(
        None,
        description='location_id integer',
        title='get_characters_character_id_clones_location_id',
    )
    location_type: Optional[Literal['station', 'structure']] = Field(
        None,
        description='location_type string',
        title='get_characters_character_id_clones_location_type',
    )


class JumpClone(BaseModel):
    implants: List[int] = Field(
        ...,
        description='implants array',
        max_items=64,
        title='get_characters_character_id_clones_implants',
    )
    jump_clone_id: int = Field(
        ...,
        description='jump_clone_id integer',
        title='get_characters_character_id_clones_jump_clone_id',
    )
    location_id: int = Field(
        ...,
        description='location_id integer',
        title='get_characters_character_id_clones_jump_clone_location_id',
    )
    location_type: Literal['station', 'structure'] = Field(
        ...,
        description='location_type string',
        title='get_characters_character_id_clones_jump_clone_location_type',
    )
    name: Optional[str] = Field(
        None, description='name string', title='get_characters_character_id_clones_name'
    )


class GetCharactersCharacterIdClonesOk(BaseModel):
    home_location: Optional[HomeLocation] = Field(
        None,
        description='home_location object',
        title='get_characters_character_id_clones_home_location',
    )
    jump_clones: List[JumpClone] = Field(
        ...,
        description='jump_clones array',
        max_items=64,
        title='get_characters_character_id_clones_jump_clones',
    )
    last_clone_jump_date: Optional[datetime] = Field(
        None,
        description='last_clone_jump_date string',
        title='get_characters_character_id_clones_last_clone_jump_date',
    )
    last_station_change_date: Optional[datetime] = Field(
        None,
        description='last_station_change_date string',
        title='get_characters_character_id_clones_last_station_change_date',
    )


class Headers200_get_characters_character_id_clones(ModelBaseEVECelery):
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


class Response200_get_characters_character_id_clones(ModelCachedResponse):
    """
    Clone information for the given character

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        {
          "home_location": {
            "location_id": 1021348135816,
            "location_type": "structure"
          },
          "jump_clones": [
            {
              "implants": [
                22118
              ],
              "jump_clone_id": 12345,
              "location_id": 60003463,
              "location_type": "station"
            }
          ]
        }

    """

    headers: Headers200_get_characters_character_id_clones = Field(
        ..., description='The response headers for this request.'
    )
    body: GetCharactersCharacterIdClonesOk = Field(
        ..., description='The response body for this request.'
    )
