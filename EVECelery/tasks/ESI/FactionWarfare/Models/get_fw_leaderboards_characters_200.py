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


class ActiveTotalItem(BaseModel):
    amount: Optional[int] = Field(
        None,
        description='Amount of kills',
        title='get_fw_leaderboards_characters_amount',
    )
    character_id: Optional[int] = Field(
        None,
        description='character_id integer',
        title='get_fw_leaderboards_characters_character_id',
    )


class LastWeekItem(BaseModel):
    amount: Optional[int] = Field(
        None,
        description='Amount of kills',
        title='get_fw_leaderboards_characters_last_week_amount',
    )
    character_id: Optional[int] = Field(
        None,
        description='character_id integer',
        title='get_fw_leaderboards_characters_last_week_character_id',
    )


class YesterdayItem(BaseModel):
    amount: Optional[int] = Field(
        None,
        description='Amount of kills',
        title='get_fw_leaderboards_characters_yesterday_amount',
    )
    character_id: Optional[int] = Field(
        None,
        description='character_id integer',
        title='get_fw_leaderboards_characters_yesterday_character_id',
    )


class Kills(BaseModel):
    active_total: List[ActiveTotalItem] = Field(
        ...,
        description='Top 100 ranking of pilots active in faction warfare by total kills. A pilot is considered "active" if they have participated in faction warfare in the past 14 days',
        max_items=100,
        title='get_fw_leaderboards_characters_active_total',
    )
    last_week: List[LastWeekItem] = Field(
        ...,
        description='Top 100 ranking of pilots by kills in the past week',
        max_items=100,
        title='get_fw_leaderboards_characters_last_week',
    )
    yesterday: List[YesterdayItem] = Field(
        ...,
        description='Top 100 ranking of pilots by kills in the past day',
        max_items=100,
        title='get_fw_leaderboards_characters_yesterday',
    )


class ActiveTotalItem1(BaseModel):
    amount: Optional[int] = Field(
        None,
        description='Amount of victory points',
        title='get_fw_leaderboards_characters_active_total_amount',
    )
    character_id: Optional[int] = Field(
        None,
        description='character_id integer',
        title='get_fw_leaderboards_characters_active_total_character_id',
    )


class LastWeekItem1(BaseModel):
    amount: Optional[int] = Field(
        None,
        description='Amount of victory points',
        title='get_fw_leaderboards_characters_last_week_amount_1',
    )
    character_id: Optional[int] = Field(
        None,
        description='character_id integer',
        title='get_fw_leaderboards_characters_last_week_character_id_1',
    )


class YesterdayItem1(BaseModel):
    amount: Optional[int] = Field(
        None,
        description='Amount of victory points',
        title='get_fw_leaderboards_characters_yesterday_amount_1',
    )
    character_id: Optional[int] = Field(
        None,
        description='character_id integer',
        title='get_fw_leaderboards_characters_yesterday_character_id_1',
    )


class VictoryPoints(BaseModel):
    active_total: List[ActiveTotalItem1] = Field(
        ...,
        description='Top 100 ranking of pilots active in faction warfare by total victory points. A pilot is considered "active" if they have participated in faction warfare in the past 14 days',
        max_items=100,
        title='get_fw_leaderboards_characters_victory_points_active_total',
    )
    last_week: List[LastWeekItem1] = Field(
        ...,
        description='Top 100 ranking of pilots by victory points in the past week',
        max_items=100,
        title='get_fw_leaderboards_characters_victory_points_last_week',
    )
    yesterday: List[YesterdayItem1] = Field(
        ...,
        description='Top 100 ranking of pilots by victory points in the past day',
        max_items=100,
        title='get_fw_leaderboards_characters_victory_points_yesterday',
    )


class GetFwLeaderboardsCharactersOk(BaseModel):
    kills: Kills = Field(
        ...,
        description='Top 100 rankings of pilots by number of kills from yesterday, last week and in total',
        title='get_fw_leaderboards_characters_kills',
    )
    victory_points: VictoryPoints = Field(
        ...,
        description='Top 100 rankings of pilots by victory points from yesterday, last week and in total',
        title='get_fw_leaderboards_characters_victory_points',
    )


class Headers200_get_fw_leaderboards_characters(ModelBaseEVECelery):
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


class Response200_get_fw_leaderboards_characters(ModelCachedResponse):
    """
    Character leaderboard of kills and victory points within faction warfare

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        {
          "kills": {
            "active_total": [
              {
                "amount": 10000,
                "character_id": 2112625428
              },
              {
                "amount": 8500,
                "character_id": 95465499
              }
            ],
            "last_week": [
              {
                "amount": 100,
                "character_id": 2112625428
              },
              {
                "amount": 70,
                "character_id": 95465499
              }
            ],
            "yesterday": [
              {
                "amount": 34,
                "character_id": 2112625428
              },
              {
                "amount": 20,
                "character_id": 95465499
              }
            ]
          },
          "victory_points": {
            "active_total": [
              {
                "amount": 1239158,
                "character_id": 2112625428
              },
              {
                "amount": 1139029,
                "character_id": 95465499
              }
            ],
            "last_week": [
              {
                "amount": 2660,
                "character_id": 2112625428
              },
              {
                "amount": 2000,
                "character_id": 95465499
              }
            ],
            "yesterday": [
              {
                "amount": 620,
                "character_id": 2112625428
              },
              {
                "amount": 550,
                "character_id": 95465499
              }
            ]
          }
        }

    """

    headers: Headers200_get_fw_leaderboards_characters = Field(
        ..., description='The response headers for this request.'
    )
    body: GetFwLeaderboardsCharactersOk = Field(
        ..., description='The response body for this request.'
    )
