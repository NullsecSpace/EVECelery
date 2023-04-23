"""
A model definition module returned by an ESI task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Models.py'.
"""
from __future__ import annotations
from EVECelery.tasks.BaseTasks.Models.ModelsBase import ModelBaseEVECelery
from EVECelery.tasks.BaseTasks.Models.ModelsCached import ModelCachedResponse
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class Kills(BaseModel):
    last_week: int = Field(
        ...,
        description="Last week's total number of kills by members of the given corporation against enemy factions",
        title='get_corporations_corporation_id_fw_stats_last_week',
    )
    total: int = Field(
        ...,
        description='Total number of kills by members of the given corporation against enemy factions since the corporation enlisted',
        title='get_corporations_corporation_id_fw_stats_total',
    )
    yesterday: int = Field(
        ...,
        description="Yesterday's total number of kills by members of the given corporation against enemy factions",
        title='get_corporations_corporation_id_fw_stats_yesterday',
    )


class VictoryPoints(BaseModel):
    last_week: int = Field(
        ...,
        description="Last week's victory points gained by members of the given corporation",
        title='get_corporations_corporation_id_fw_stats_victory_points_last_week',
    )
    total: int = Field(
        ...,
        description='Total victory points gained since the given corporation enlisted',
        title='get_corporations_corporation_id_fw_stats_victory_points_total',
    )
    yesterday: int = Field(
        ...,
        description="Yesterday's victory points gained by members of the given corporation",
        title='get_corporations_corporation_id_fw_stats_victory_points_yesterday',
    )


class GetCorporationsCorporationIdFwStatsOk(BaseModel):
    enlisted_on: Optional[datetime] = Field(
        None,
        description='The enlistment date of the given corporation into faction warfare. Will not be included if corporation is not enlisted in faction warfare',
        title='get_corporations_corporation_id_fw_stats_enlisted_on',
    )
    faction_id: Optional[int] = Field(
        None,
        description='The faction the given corporation is enlisted to fight for. Will not be included if corporation is not enlisted in faction warfare',
        title='get_corporations_corporation_id_fw_stats_faction_id',
    )
    kills: Kills = Field(
        ...,
        description='Summary of kills done by the given corporation against enemy factions',
        title='get_corporations_corporation_id_fw_stats_kills',
    )
    pilots: Optional[int] = Field(
        None,
        description='How many pilots the enlisted corporation has. Will not be included if corporation is not enlisted in faction warfare',
        title='get_corporations_corporation_id_fw_stats_pilots',
    )
    victory_points: VictoryPoints = Field(
        ...,
        description='Summary of victory points gained by the given corporation for the enlisted faction',
        title='get_corporations_corporation_id_fw_stats_victory_points',
    )


class Headers200_get_corporations_corporation_id_fw_stats(ModelBaseEVECelery):
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


class Response200_get_corporations_corporation_id_fw_stats(ModelCachedResponse):
    """
    Faction warfare statistics for a given corporation

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        {
          "enlisted_on": "2017-10-17T00:00:00Z",
          "faction_id": 500001,
          "kills": {
            "last_week": 893,
            "total": 684350,
            "yesterday": 136
          },
          "pilots": 28863,
          "victory_points": {
            "last_week": 102640,
            "total": 52658260,
            "yesterday": 15980
          }
        }

    """

    headers: Headers200_get_corporations_corporation_id_fw_stats = Field(
        ..., description='The response headers for this request.'
    )
    body: GetCorporationsCorporationIdFwStatsOk = Field(
        ..., description='The response body for this request.'
    )
