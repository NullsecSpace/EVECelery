"""
A model definition module returned by an ESI task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Models.py'.
"""
from __future__ import annotations
from EVECelery.tasks.BaseTasks.Models.ModelsBase import ModelBaseEVECelery
from EVECelery.tasks.BaseTasks.Models.ModelsCached import ModelCachedResponse
from datetime import datetime
from typing import List, Literal, Optional

from pydantic import BaseModel, Field


class GetFleetsFleetIdMembersOkItem(BaseModel):
    character_id: int = Field(
        ...,
        description='character_id integer',
        title='get_fleets_fleet_id_members_character_id',
    )
    join_time: datetime = Field(
        ...,
        description='join_time string',
        title='get_fleets_fleet_id_members_join_time',
    )
    role: Literal[
        'fleet_commander', 'wing_commander', 'squad_commander', 'squad_member'
    ] = Field(
        ...,
        description='Member’s role in fleet',
        title='get_fleets_fleet_id_members_role',
    )
    role_name: str = Field(
        ...,
        description='Localized role names',
        title='get_fleets_fleet_id_members_role_name',
    )
    ship_type_id: int = Field(
        ...,
        description='ship_type_id integer',
        title='get_fleets_fleet_id_members_ship_type_id',
    )
    solar_system_id: int = Field(
        ...,
        description='Solar system the member is located in',
        title='get_fleets_fleet_id_members_solar_system_id',
    )
    squad_id: int = Field(
        ...,
        description='ID of the squad the member is in. If not applicable, will be set to -1',
        title='get_fleets_fleet_id_members_squad_id',
    )
    station_id: Optional[int] = Field(
        None,
        description='Station in which the member is docked in, if applicable',
        title='get_fleets_fleet_id_members_station_id',
    )
    takes_fleet_warp: bool = Field(
        ...,
        description='Whether the member take fleet warps',
        title='get_fleets_fleet_id_members_takes_fleet_warp',
    )
    wing_id: int = Field(
        ...,
        description='ID of the wing the member is in. If not applicable, will be set to -1',
        title='get_fleets_fleet_id_members_wing_id',
    )


class GetFleetsFleetIdMembersOk(BaseModel):
    __root__: List[GetFleetsFleetIdMembersOkItem] = Field(
        ...,
        description='200 ok array',
        max_items=256,
        title='get_fleets_fleet_id_members_ok',
    )


class Headers200_get_fleets_fleet_id_members(ModelBaseEVECelery):
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


class Response200_get_fleets_fleet_id_members(ModelCachedResponse):
    """
    A list of fleet members

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "character_id": 93265215,
            "join_time": "2016-04-29T12:34:56Z",
            "role": "squad_commander",
            "role_name": "Squad Commander (Boss)",
            "ship_type_id": 33328,
            "solar_system_id": 30003729,
            "squad_id": 3129411261968,
            "station_id": 61000180,
            "takes_fleet_warp": true,
            "wing_id": 2073711261968
          }
        ]

    """

    headers: Headers200_get_fleets_fleet_id_members = Field(
        ..., description='The response headers for this request.'
    )
    body: GetFleetsFleetIdMembersOk = Field(
        ..., description='The response body for this request.'
    )
