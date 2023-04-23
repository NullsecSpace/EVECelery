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
        None, description='Amount of kills', title='get_fw_leaderboards_amount'
    )
    faction_id: Optional[int] = Field(
        None, description='faction_id integer', title='get_fw_leaderboards_faction_id'
    )


class LastWeekItem(BaseModel):
    amount: Optional[int] = Field(
        None,
        description='Amount of kills',
        title='get_fw_leaderboards_last_week_amount',
    )
    faction_id: Optional[int] = Field(
        None,
        description='faction_id integer',
        title='get_fw_leaderboards_last_week_faction_id',
    )


class YesterdayItem(BaseModel):
    amount: Optional[int] = Field(
        None,
        description='Amount of kills',
        title='get_fw_leaderboards_yesterday_amount',
    )
    faction_id: Optional[int] = Field(
        None,
        description='faction_id integer',
        title='get_fw_leaderboards_yesterday_faction_id',
    )


class Kills(BaseModel):
    active_total: List[ActiveTotalItem] = Field(
        ...,
        description='Top 4 ranking of factions active in faction warfare by total kills. A faction is considered "active" if they have participated in faction warfare in the past 14 days',
        max_items=4,
        title='get_fw_leaderboards_active_total',
    )
    last_week: List[LastWeekItem] = Field(
        ...,
        description='Top 4 ranking of factions by kills in the past week',
        max_items=4,
        title='get_fw_leaderboards_last_week',
    )
    yesterday: List[YesterdayItem] = Field(
        ...,
        description='Top 4 ranking of factions by kills in the past day',
        max_items=4,
        title='get_fw_leaderboards_yesterday',
    )


class ActiveTotalItem1(BaseModel):
    amount: Optional[int] = Field(
        None,
        description='Amount of victory points',
        title='get_fw_leaderboards_active_total_amount',
    )
    faction_id: Optional[int] = Field(
        None,
        description='faction_id integer',
        title='get_fw_leaderboards_active_total_faction_id',
    )


class LastWeekItem1(BaseModel):
    amount: Optional[int] = Field(
        None,
        description='Amount of victory points',
        title='get_fw_leaderboards_last_week_amount_1',
    )
    faction_id: Optional[int] = Field(
        None,
        description='faction_id integer',
        title='get_fw_leaderboards_last_week_faction_id_1',
    )


class YesterdayItem1(BaseModel):
    amount: Optional[int] = Field(
        None,
        description='Amount of victory points',
        title='get_fw_leaderboards_yesterday_amount_1',
    )
    faction_id: Optional[int] = Field(
        None,
        description='faction_id integer',
        title='get_fw_leaderboards_yesterday_faction_id_1',
    )


class VictoryPoints(BaseModel):
    active_total: List[ActiveTotalItem1] = Field(
        ...,
        description='Top 4 ranking of factions active in faction warfare by total victory points. A faction is considered "active" if they have participated in faction warfare in the past 14 days',
        max_items=4,
        title='get_fw_leaderboards_victory_points_active_total',
    )
    last_week: List[LastWeekItem1] = Field(
        ...,
        description='Top 4 ranking of factions by victory points in the past week',
        max_items=4,
        title='get_fw_leaderboards_victory_points_last_week',
    )
    yesterday: List[YesterdayItem1] = Field(
        ...,
        description='Top 4 ranking of factions by victory points in the past day',
        max_items=4,
        title='get_fw_leaderboards_victory_points_yesterday',
    )


class GetFwLeaderboardsOk(BaseModel):
    kills: Kills = Field(
        ...,
        description='Top 4 rankings of factions by number of kills from yesterday, last week and in total',
        title='get_fw_leaderboards_kills',
    )
    victory_points: VictoryPoints = Field(
        ...,
        description='Top 4 rankings of factions by victory points from yesterday, last week and in total',
        title='get_fw_leaderboards_victory_points',
    )


class Headers200_get_fw_leaderboards(ModelBaseEVECelery):
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


class Response200_get_fw_leaderboards(ModelCachedResponse):
    """
    Corporation leaderboard of kills and victory points within faction warfare

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        {
          "kills": {
            "active_total": [
              {
                "amount": 832273,
                "faction_id": 500004
              },
              {
                "amount": 687915,
                "faction_id": 500001
              }
            ],
            "last_week": [
              {
                "amount": 730,
                "faction_id": 500001
              },
              {
                "amount": 671,
                "faction_id": 500004
              }
            ],
            "yesterday": [
              {
                "amount": 100,
                "faction_id": 500001
              },
              {
                "amount": 50,
                "faction_id": 500004
              }
            ]
          },
          "victory_points": {
            "active_total": [
              {
                "amount": 53130500,
                "faction_id": 500001
              },
              {
                "amount": 50964263,
                "faction_id": 500004
              }
            ],
            "last_week": [
              {
                "amount": 97360,
                "faction_id": 500001
              },
              {
                "amount": 84980,
                "faction_id": 500004
              }
            ],
            "yesterday": [
              {
                "amount": 5000,
                "faction_id": 500002
              },
              {
                "amount": 3500,
                "faction_id": 500003
              }
            ]
          }
        }

    """

    headers: Headers200_get_fw_leaderboards = Field(
        ..., description='The response headers for this request.'
    )
    body: GetFwLeaderboardsOk = Field(
        ..., description='The response body for this request.'
    )
