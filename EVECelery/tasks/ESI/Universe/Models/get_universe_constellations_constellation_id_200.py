"""
A model definition module returned by an ESI task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Models.py'.
"""
from __future__ import annotations
from EVECelery.tasks.BaseTasks.Models.ModelsBase import ModelBaseEVECelery
from EVECelery.tasks.BaseTasks.Models.ModelsCached import ModelCachedResponse
from typing import List

from pydantic import BaseModel, Field


class Position(BaseModel):
    x: float = Field(
        ...,
        description='x number',
        title='get_universe_constellations_constellation_id_x',
    )
    y: float = Field(
        ...,
        description='y number',
        title='get_universe_constellations_constellation_id_y',
    )
    z: float = Field(
        ...,
        description='z number',
        title='get_universe_constellations_constellation_id_z',
    )


class GetUniverseConstellationsConstellationIdOk(BaseModel):
    constellation_id: int = Field(
        ...,
        description='constellation_id integer',
        title='get_universe_constellations_constellation_id_constellation_id',
    )
    name: str = Field(
        ...,
        description='name string',
        title='get_universe_constellations_constellation_id_name',
    )
    position: Position = Field(
        ...,
        description='position object',
        title='get_universe_constellations_constellation_id_position',
    )
    region_id: int = Field(
        ...,
        description='The region this constellation is in',
        title='get_universe_constellations_constellation_id_region_id',
    )
    systems: List[int] = Field(
        ...,
        description='systems array',
        max_items=10000,
        title='get_universe_constellations_constellation_id_systems',
    )


class Headers200_get_universe_constellations_constellation_id(ModelBaseEVECelery):
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


class Response200_get_universe_constellations_constellation_id(ModelCachedResponse):
    """
    Information about a constellation

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        {
          "constellation_id": 20000009,
          "name": "Mekashtad",
          "position": {
            "x": 67796138757472320,
            "y": -70591121348560960,
            "z": -59587016159270070
          },
          "region_id": 10000001,
          "systems": [
            20000302,
            20000303
          ]
        }

    """

    headers: Headers200_get_universe_constellations_constellation_id = Field(
        ..., description='The response headers for this request.'
    )
    body: GetUniverseConstellationsConstellationIdOk = Field(
        ..., description='The response body for this request.'
    )
