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


class Planet(BaseModel):
    asteroid_belts: Optional[List[int]] = Field(
        None,
        description='asteroid_belts array',
        max_items=100,
        title='get_universe_systems_system_id_asteroid_belts',
    )
    moons: Optional[List[int]] = Field(
        None,
        description='moons array',
        max_items=1000,
        title='get_universe_systems_system_id_moons',
    )
    planet_id: int = Field(
        ...,
        description='planet_id integer',
        title='get_universe_systems_system_id_planet_id',
    )


class Position(BaseModel):
    x: float = Field(
        ..., description='x number', title='get_universe_systems_system_id_x'
    )
    y: float = Field(
        ..., description='y number', title='get_universe_systems_system_id_y'
    )
    z: float = Field(
        ..., description='z number', title='get_universe_systems_system_id_z'
    )


class GetUniverseSystemsSystemIdOk(BaseModel):
    constellation_id: int = Field(
        ...,
        description='The constellation this solar system is in',
        title='get_universe_systems_system_id_constellation_id',
    )
    name: str = Field(
        ..., description='name string', title='get_universe_systems_system_id_name'
    )
    planets: Optional[List[Planet]] = Field(
        None,
        description='planets array',
        max_items=1000,
        title='get_universe_systems_system_id_planets',
    )
    position: Position = Field(
        ...,
        description='position object',
        title='get_universe_systems_system_id_position',
    )
    security_class: Optional[str] = Field(
        None,
        description='security_class string',
        title='get_universe_systems_system_id_security_class',
    )
    security_status: float = Field(
        ...,
        description='security_status number',
        title='get_universe_systems_system_id_security_status',
    )
    star_id: Optional[int] = Field(
        None,
        description='star_id integer',
        title='get_universe_systems_system_id_star_id',
    )
    stargates: Optional[List[int]] = Field(
        None,
        description='stargates array',
        max_items=25,
        title='get_universe_systems_system_id_stargates',
    )
    stations: Optional[List[int]] = Field(
        None,
        description='stations array',
        max_items=25,
        title='get_universe_systems_system_id_stations',
    )
    system_id: int = Field(
        ...,
        description='system_id integer',
        title='get_universe_systems_system_id_system_id',
    )


class Headers200_get_universe_systems_system_id(ModelBaseEVECelery):
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


class Response200_get_universe_systems_system_id(ModelCachedResponse):
    """
    Information about a solar system

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        {
          "constellation_id": 20000001,
          "name": "Akpivem",
          "planets": [
            {
              "moons": [
                40000042
              ],
              "planet_id": 40000041
            },
            {
              "planet_id": 40000043
            }
          ],
          "position": {
            "x": -91174141133075340,
            "y": 43938227486247170,
            "z": -56482824383339900
          },
          "security_class": "B",
          "security_status": 0.8462923765182495,
          "star_id": 40000040,
          "stargates": [
            50000342
          ],
          "system_id": 30000003
        }

    """

    headers: Headers200_get_universe_systems_system_id = Field(
        ..., description='The response headers for this request.'
    )
    body: GetUniverseSystemsSystemIdOk = Field(
        ..., description='The response body for this request.'
    )
