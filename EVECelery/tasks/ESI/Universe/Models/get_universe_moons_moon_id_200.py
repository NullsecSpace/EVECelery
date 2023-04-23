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
    x: float = Field(..., description='x number', title='get_universe_moons_moon_id_x')
    y: float = Field(..., description='y number', title='get_universe_moons_moon_id_y')
    z: float = Field(..., description='z number', title='get_universe_moons_moon_id_z')


class GetUniverseMoonsMoonIdOk(BaseModel):
    moon_id: int = Field(
        ..., description='moon_id integer', title='get_universe_moons_moon_id_moon_id'
    )
    name: str = Field(
        ..., description='name string', title='get_universe_moons_moon_id_name'
    )
    position: Position = Field(
        ..., description='position object', title='get_universe_moons_moon_id_position'
    )
    system_id: int = Field(
        ...,
        description='The solar system this moon is in',
        title='get_universe_moons_moon_id_system_id',
    )


class Headers200_get_universe_moons_moon_id(ModelBaseEVECelery):
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


class Response200_get_universe_moons_moon_id(ModelCachedResponse):
    """
    Information about a moon

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        {
          "moon_id": 40000042,
          "name": "Akpivem I - Moon 1",
          "position": {
            "x": 58605102008,
            "y": -3066616285,
            "z": -55193617920
          },
          "system_id": 30000003
        }

    """

    headers: Headers200_get_universe_moons_moon_id = Field(
        ..., description='The response headers for this request.'
    )
    body: GetUniverseMoonsMoonIdOk = Field(
        ..., description='The response body for this request.'
    )
