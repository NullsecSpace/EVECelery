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

from pydantic import BaseModel, Field, conint


class Kills(BaseModel):
    last_week: int = Field(
        ...,
        description="Last week's total number of kills by a given character against enemy factions",
        title='get_characters_character_id_fw_stats_last_week',
    )
    total: int = Field(
        ...,
        description='Total number of kills by a given character against enemy factions since the character enlisted',
        title='get_characters_character_id_fw_stats_total',
    )
    yesterday: int = Field(
        ...,
        description="Yesterday's total number of kills by a given character against enemy factions",
        title='get_characters_character_id_fw_stats_yesterday',
    )


class VictoryPoints(BaseModel):
    last_week: int = Field(
        ...,
        description="Last week's victory points gained by the given character",
        title='get_characters_character_id_fw_stats_victory_points_last_week',
    )
    total: int = Field(
        ...,
        description='Total victory points gained since the given character enlisted',
        title='get_characters_character_id_fw_stats_victory_points_total',
    )
    yesterday: int = Field(
        ...,
        description="Yesterday's victory points gained by the given character",
        title='get_characters_character_id_fw_stats_victory_points_yesterday',
    )


class GetCharactersCharacterIdFwStatsOk(BaseModel):
    current_rank: Optional[conint(ge=0, le=9)] = Field(
        None,
        description="The given character's current faction rank",
        title='get_characters_character_id_fw_stats_current_rank',
    )
    enlisted_on: Optional[datetime] = Field(
        None,
        description='The enlistment date of the given character into faction warfare. Will not be included if character is not enlisted in faction warfare',
        title='get_characters_character_id_fw_stats_enlisted_on',
    )
    faction_id: Optional[int] = Field(
        None,
        description='The faction the given character is enlisted to fight for. Will not be included if character is not enlisted in faction warfare',
        title='get_characters_character_id_fw_stats_faction_id',
    )
    highest_rank: Optional[conint(ge=0, le=9)] = Field(
        None,
        description="The given character's highest faction rank achieved",
        title='get_characters_character_id_fw_stats_highest_rank',
    )
    kills: Kills = Field(
        ...,
        description='Summary of kills done by the given character against enemy factions',
        title='get_characters_character_id_fw_stats_kills',
    )
    victory_points: VictoryPoints = Field(
        ...,
        description='Summary of victory points gained by the given character for the enlisted faction',
        title='get_characters_character_id_fw_stats_victory_points',
    )


class Headers200_get_characters_character_id_fw_stats(ModelBaseEVECelery):
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


class Response200_get_characters_character_id_fw_stats(ModelCachedResponse):
    """
    Faction warfare statistics for a given character

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
          "victory_points": {
            "last_week": 102640,
            "total": 52658260,
            "yesterday": 15980
          }
        }

    """

    headers: Headers200_get_characters_character_id_fw_stats = Field(
        ..., description='The response headers for this request.'
    )
    body: GetCharactersCharacterIdFwStatsOk = Field(
        ..., description='The response body for this request.'
    )
