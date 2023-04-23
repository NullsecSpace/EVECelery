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


class Position(BaseModel):
    x: float = Field(
        ..., description='x number', title='get_universe_structures_structure_id_x'
    )
    y: float = Field(
        ..., description='y number', title='get_universe_structures_structure_id_y'
    )
    z: float = Field(
        ..., description='z number', title='get_universe_structures_structure_id_z'
    )


class GetUniverseStructuresStructureIdOk(BaseModel):
    name: str = Field(
        ...,
        description='The full name of the structure',
        title='get_universe_structures_structure_id_name',
    )
    owner_id: int = Field(
        ...,
        description='The ID of the corporation who owns this particular structure',
        title='get_universe_structures_structure_id_owner_id',
    )
    position: Optional[Position] = Field(
        None,
        description='Coordinates of the structure in Cartesian space relative to the Sun, in metres.\n',
        title='get_universe_structures_structure_id_position',
    )
    solar_system_id: int = Field(
        ...,
        description='solar_system_id integer',
        title='get_universe_structures_structure_id_solar_system_id',
    )
    type_id: Optional[int] = Field(
        None,
        description='type_id integer',
        title='get_universe_structures_structure_id_type_id',
    )


class Headers200_get_universe_structures_structure_id(ModelBaseEVECelery):
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


class Response200_get_universe_structures_structure_id(ModelCachedResponse):
    """
    Data about a structure

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        {
          "name": "V-3YG7 VI - The Capital",
          "owner_id": 109299958,
          "solar_system_id": 30000142
        }

    """

    headers: Headers200_get_universe_structures_structure_id = Field(
        ..., description='The response headers for this request.'
    )
    body: GetUniverseStructuresStructureIdOk = Field(
        ..., description='The response body for this request.'
    )
