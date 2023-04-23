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

from pydantic import BaseModel, Field, conint


class GetCharactersCharacterIdPlanetsOkItem(BaseModel):
    last_update: datetime = Field(
        ...,
        description='last_update string',
        title='get_characters_character_id_planets_last_update',
    )
    num_pins: conint(ge=1) = Field(
        ...,
        description='num_pins integer',
        title='get_characters_character_id_planets_num_pins',
    )
    owner_id: int = Field(
        ...,
        description='owner_id integer',
        title='get_characters_character_id_planets_owner_id',
    )
    planet_id: int = Field(
        ...,
        description='planet_id integer',
        title='get_characters_character_id_planets_planet_id',
    )
    planet_type: Literal[
        'temperate', 'barren', 'oceanic', 'ice', 'gas', 'lava', 'storm', 'plasma'
    ] = Field(
        ...,
        description='planet_type string',
        title='get_characters_character_id_planets_planet_type',
    )
    solar_system_id: int = Field(
        ...,
        description='solar_system_id integer',
        title='get_characters_character_id_planets_solar_system_id',
    )
    upgrade_level: conint(ge=0, le=5) = Field(
        ...,
        description='upgrade_level integer',
        title='get_characters_character_id_planets_upgrade_level',
    )


class GetCharactersCharacterIdPlanetsOk(BaseModel):
    __root__: List[GetCharactersCharacterIdPlanetsOkItem] = Field(
        ...,
        description='200 ok array',
        max_items=10,
        title='get_characters_character_id_planets_ok',
    )


class Headers200_get_characters_character_id_planets(ModelBaseEVECelery):
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


class Response200_get_characters_character_id_planets(ModelCachedResponse):
    """
    List of colonies

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "last_update": "2016-11-28T16:42:51Z",
            "num_pins": 1,
            "owner_id": 90000001,
            "planet_id": 40023691,
            "planet_type": "plasma",
            "solar_system_id": 30000379,
            "upgrade_level": 0
          },
          {
            "last_update": "2016-11-28T16:41:54Z",
            "num_pins": 1,
            "owner_id": 90000001,
            "planet_id": 40023697,
            "planet_type": "barren",
            "solar_system_id": 30000379,
            "upgrade_level": 0
          }
        ]

    """

    headers: Headers200_get_characters_character_id_planets = Field(
        ..., description='The response headers for this request.'
    )
    body: GetCharactersCharacterIdPlanetsOk = Field(
        ..., description='The response body for this request.'
    )
