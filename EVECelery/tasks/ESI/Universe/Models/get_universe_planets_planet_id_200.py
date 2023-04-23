"""
A model definition module returned by an ESI task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Models.py'.
"""
from __future__ import annotations
from EVECelery.tasks.BaseTasks.Models.ModelsBase import ModelBaseEVECelery
from EVECelery.tasks.BaseTasks.Models.ModelsCached import ModelCachedResponse
from pydantic import BaseModel, Field


class Position(BaseModel):
    x: float = Field(
        ..., description='x number', title='get_universe_planets_planet_id_x'
    )
    y: float = Field(
        ..., description='y number', title='get_universe_planets_planet_id_y'
    )
    z: float = Field(
        ..., description='z number', title='get_universe_planets_planet_id_z'
    )


class GetUniversePlanetsPlanetIdOk(BaseModel):
    name: str = Field(
        ..., description='name string', title='get_universe_planets_planet_id_name'
    )
    planet_id: int = Field(
        ...,
        description='planet_id integer',
        title='get_universe_planets_planet_id_planet_id',
    )
    position: Position = Field(
        ...,
        description='position object',
        title='get_universe_planets_planet_id_position',
    )
    system_id: int = Field(
        ...,
        description='The solar system this planet is in',
        title='get_universe_planets_planet_id_system_id',
    )
    type_id: int = Field(
        ...,
        description='type_id integer',
        title='get_universe_planets_planet_id_type_id',
    )


class Headers200_get_universe_planets_planet_id(ModelBaseEVECelery):
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


class Response200_get_universe_planets_planet_id(ModelCachedResponse):
    """
    Information about a planet

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        {
          "name": "Akpivem III",
          "planet_id": 40000046,
          "position": {
            "x": -189226344497,
            "y": 9901605317,
            "z": -254852632979
          },
          "system_id": 30000003,
          "type_id": 13
        }

    """

    headers: Headers200_get_universe_planets_planet_id = Field(
        ..., description='The response headers for this request.'
    )
    body: GetUniversePlanetsPlanetIdOk = Field(
        ..., description='The response body for this request.'
    )
