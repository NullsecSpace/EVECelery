"""
A model definition module returned by an ESI task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Models.py'.
"""
from __future__ import annotations
from EVECelery.tasks.BaseTasks.Models.ModelsBase import ModelBaseEVECelery
from EVECelery.tasks.BaseTasks.Models.ModelsCached import ModelCachedResponse
from typing import Optional

from pydantic import BaseModel, Field


class GetCharactersCharacterIdLocationOk(BaseModel):
    solar_system_id: int = Field(
        ...,
        description='solar_system_id integer',
        title='get_characters_character_id_location_solar_system_id',
    )
    station_id: Optional[int] = Field(
        None,
        description='station_id integer',
        title='get_characters_character_id_location_station_id',
    )
    structure_id: Optional[int] = Field(
        None,
        description='structure_id integer',
        title='get_characters_character_id_location_structure_id',
    )


class Headers200_get_characters_character_id_location(ModelBaseEVECelery):
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


class Response200_get_characters_character_id_location(ModelCachedResponse):
    """
    Information about the characters current location. Returns the current solar system id, and also the current station or structure ID if applicable

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        {
          "solar_system_id": 30002505,
          "structure_id": 1000000016989
        }

    """

    headers: Headers200_get_characters_character_id_location = Field(
        ..., description='The response headers for this request.'
    )
    body: GetCharactersCharacterIdLocationOk = Field(
        ..., description='The response body for this request.'
    )
