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


class GetUniverseFactionsOkItem(BaseModel):
    corporation_id: Optional[int] = Field(
        None,
        description='corporation_id integer',
        title='get_universe_factions_corporation_id',
    )
    description: str = Field(
        ..., description='description string', title='get_universe_factions_description'
    )
    faction_id: int = Field(
        ..., description='faction_id integer', title='get_universe_factions_faction_id'
    )
    is_unique: bool = Field(
        ..., description='is_unique boolean', title='get_universe_factions_is_unique'
    )
    militia_corporation_id: Optional[int] = Field(
        None,
        description='militia_corporation_id integer',
        title='get_universe_factions_militia_corporation_id',
    )
    name: str = Field(
        ..., description='name string', title='get_universe_factions_name'
    )
    size_factor: float = Field(
        ..., description='size_factor number', title='get_universe_factions_size_factor'
    )
    solar_system_id: Optional[int] = Field(
        None,
        description='solar_system_id integer',
        title='get_universe_factions_solar_system_id',
    )
    station_count: int = Field(
        ...,
        description='station_count integer',
        title='get_universe_factions_station_count',
    )
    station_system_count: int = Field(
        ...,
        description='station_system_count integer',
        title='get_universe_factions_station_system_count',
    )


class GetUniverseFactionsOk(BaseModel):
    __root__: List[GetUniverseFactionsOkItem] = Field(
        ...,
        description='200 ok array',
        max_items=10000,
        title='get_universe_factions_ok',
    )


class Headers200_get_universe_factions(ModelBaseEVECelery):
    """
    Headers for response code 200
    """

    Cache_Control: str | None = Field(
        description="The caching mechanism used", alias="Cache-Control"
    )
    Content_Language: str | None = Field(
        description="The language used in the response", alias="Content-Language"
    )
    ETag: str | None = Field(description="RFC7232 compliant entity tag")
    Expires: str | None = Field(description="RFC7231 formatted datetime string")
    Last_Modified: str | None = Field(
        description="RFC7231 formatted datetime string", alias="Last-Modified"
    )


class Response200_get_universe_factions(ModelCachedResponse):
    """
    A list of factions

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "corporation_id": 456,
            "description": "blah blah",
            "faction_id": 1,
            "is_unique": true,
            "name": "Faction",
            "size_factor": 1.0,
            "solar_system_id": 123,
            "station_count": 1000,
            "station_system_count": 100
          }
        ]

    """

    headers: Headers200_get_universe_factions = Field(
        ..., description='The response headers for this request.'
    )
    body: GetUniverseFactionsOk = Field(
        ..., description='The response body for this request.'
    )
