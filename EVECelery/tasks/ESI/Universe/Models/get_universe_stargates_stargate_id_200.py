"""
A model definition module returned by an ESI task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Models.py'.
"""
from __future__ import annotations
from EVECelery.tasks.BaseTasks.Models.ModelsBase import ModelBaseEVECelery
from EVECelery.tasks.BaseTasks.Models.ModelsCached import ModelCachedResponse
from pydantic import BaseModel, Field


class Destination(BaseModel):
    stargate_id: int = Field(
        ...,
        description='The stargate this stargate connects to',
        title='get_universe_stargates_stargate_id_destination_stargate_id',
    )
    system_id: int = Field(
        ...,
        description='The solar system this stargate connects to',
        title='get_universe_stargates_stargate_id_destination_system_id',
    )


class Position(BaseModel):
    x: float = Field(
        ..., description='x number', title='get_universe_stargates_stargate_id_x'
    )
    y: float = Field(
        ..., description='y number', title='get_universe_stargates_stargate_id_y'
    )
    z: float = Field(
        ..., description='z number', title='get_universe_stargates_stargate_id_z'
    )


class GetUniverseStargatesStargateIdOk(BaseModel):
    destination: Destination = Field(
        ...,
        description='destination object',
        title='get_universe_stargates_stargate_id_destination',
    )
    name: str = Field(
        ..., description='name string', title='get_universe_stargates_stargate_id_name'
    )
    position: Position = Field(
        ...,
        description='position object',
        title='get_universe_stargates_stargate_id_position',
    )
    stargate_id: int = Field(
        ...,
        description='stargate_id integer',
        title='get_universe_stargates_stargate_id_stargate_id',
    )
    system_id: int = Field(
        ...,
        description='The solar system this stargate is in',
        title='get_universe_stargates_stargate_id_system_id',
    )
    type_id: int = Field(
        ...,
        description='type_id integer',
        title='get_universe_stargates_stargate_id_type_id',
    )


class Headers200_get_universe_stargates_stargate_id(ModelBaseEVECelery):
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


class Response200_get_universe_stargates_stargate_id(ModelCachedResponse):
    """
    Information about a stargate

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        {
          "destination": {
            "stargate_id": 50000056,
            "system_id": 30000001
          },
          "name": "Stargate (Tanoo)",
          "position": {
            "x": -101092761600,
            "y": 5279539200,
            "z": 1550503403520
          },
          "stargate_id": 50000342,
          "system_id": 30000003,
          "type_id": 29624
        }

    """

    headers: Headers200_get_universe_stargates_stargate_id = Field(
        ..., description='The response headers for this request.'
    )
    body: GetUniverseStargatesStargateIdOk = Field(
        ..., description='The response body for this request.'
    )
