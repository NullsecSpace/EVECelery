"""
A model definition module returned by an ESI task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Models.py'.
"""
from __future__ import annotations
from EVECelery.tasks.BaseTasks.Models.ModelsBase import ModelBaseEVECelery
from EVECelery.tasks.BaseTasks.Models.ModelsCached import ModelCachedResponse
from typing import List, Literal

from pydantic import BaseModel, Field


class GetFwSystemsOkItem(BaseModel):
    contested: Literal['captured', 'contested', 'uncontested', 'vulnerable'] = Field(
        ..., description='contested string', title='get_fw_systems_contested'
    )
    occupier_faction_id: int = Field(
        ...,
        description='occupier_faction_id integer',
        title='get_fw_systems_occupier_faction_id',
    )
    owner_faction_id: int = Field(
        ...,
        description='owner_faction_id integer',
        title='get_fw_systems_owner_faction_id',
    )
    solar_system_id: int = Field(
        ...,
        description='solar_system_id integer',
        title='get_fw_systems_solar_system_id',
    )
    victory_points: int = Field(
        ..., description='victory_points integer', title='get_fw_systems_victory_points'
    )
    victory_points_threshold: int = Field(
        ...,
        description='victory_points_threshold integer',
        title='get_fw_systems_victory_points_threshold',
    )


class GetFwSystemsOk(BaseModel):
    __root__: List[GetFwSystemsOkItem] = Field(
        ..., description='200 ok array', max_items=171, title='get_fw_systems_ok'
    )


class Headers200_get_fw_systems(ModelBaseEVECelery):
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


class Response200_get_fw_systems(ModelCachedResponse):
    """
    All faction warfare solar systems

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "contested": "uncontested",
            "occupier_faction_id": 500001,
            "owner_faction_id": 500001,
            "solar_system_id": 30002096,
            "victory_points": 60,
            "victory_points_threshold": 3000
          }
        ]

    """

    headers: Headers200_get_fw_systems = Field(
        ..., description='The response headers for this request.'
    )
    body: GetFwSystemsOk = Field(..., description='The response body for this request.')
