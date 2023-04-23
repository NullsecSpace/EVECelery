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


class Kills(BaseModel):
    last_week: int = Field(
        ...,
        description="Last week's total number of kills against enemy factions",
        title='get_fw_stats_last_week',
    )
    total: int = Field(
        ...,
        description='Total number of kills against enemy factions since faction warfare began',
        title='get_fw_stats_total',
    )
    yesterday: int = Field(
        ...,
        description="Yesterday's total number of kills against enemy factions",
        title='get_fw_stats_yesterday',
    )


class VictoryPoints(BaseModel):
    last_week: int = Field(
        ...,
        description="Last week's victory points gained",
        title='get_fw_stats_victory_points_last_week',
    )
    total: int = Field(
        ...,
        description='Total victory points gained since faction warfare began',
        title='get_fw_stats_victory_points_total',
    )
    yesterday: int = Field(
        ...,
        description="Yesterday's victory points gained",
        title='get_fw_stats_victory_points_yesterday',
    )


class GetFwStatsOkItem(BaseModel):
    faction_id: int = Field(
        ..., description='faction_id integer', title='get_fw_stats_faction_id'
    )
    kills: Kills = Field(
        ...,
        description='Summary of kills against an enemy faction for the given faction',
        title='get_fw_stats_kills',
    )
    pilots: int = Field(
        ...,
        description='How many pilots fight for the given faction',
        title='get_fw_stats_pilots',
    )
    systems_controlled: int = Field(
        ...,
        description='The number of solar systems controlled by the given faction',
        title='get_fw_stats_systems_controlled',
    )
    victory_points: VictoryPoints = Field(
        ...,
        description='Summary of victory points gained for the given faction',
        title='get_fw_stats_victory_points',
    )


class GetFwStatsOk(BaseModel):
    __root__: List[GetFwStatsOkItem] = Field(
        ..., description='200 ok array', max_items=4, title='get_fw_stats_ok'
    )


class Headers200_get_fw_stats(ModelBaseEVECelery):
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


class Response200_get_fw_stats(ModelCachedResponse):
    """
    Per faction breakdown of faction warfare statistics

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "faction_id": 500001,
            "kills": {
              "last_week": 893,
              "total": 684350,
              "yesterday": 136
            },
            "pilots": 28863,
            "systems_controlled": 20,
            "victory_points": {
              "last_week": 102640,
              "total": 52658260,
              "yesterday": 15980
            }
          }
        ]

    """

    headers: Headers200_get_fw_stats = Field(
        ..., description='The response headers for this request.'
    )
    body: GetFwStatsOk = Field(..., description='The response body for this request.')
