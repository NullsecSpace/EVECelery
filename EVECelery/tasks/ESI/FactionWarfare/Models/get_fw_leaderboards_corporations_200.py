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
        title='get_fw_leaderboards_corporations_amount',
    )
    corporation_id: Optional[int] = Field(
        None,
        description='corporation_id integer',
        title='get_fw_leaderboards_corporations_corporation_id',
    )


class LastWeekItem(BaseModel):
    amount: Optional[int] = Field(
        None,
        description='Amount of kills',
        title='get_fw_leaderboards_corporations_last_week_amount',
    )
    corporation_id: Optional[int] = Field(
        None,
        description='corporation_id integer',
        title='get_fw_leaderboards_corporations_last_week_corporation_id',
    )


class YesterdayItem(BaseModel):
    amount: Optional[int] = Field(
        None,
        description='Amount of kills',
        title='get_fw_leaderboards_corporations_yesterday_amount',
    )
    corporation_id: Optional[int] = Field(
        None,
        description='corporation_id integer',
        title='get_fw_leaderboards_corporations_yesterday_corporation_id',
    )


class Kills(BaseModel):
    active_total: List[ActiveTotalItem] = Field(
        ...,
        description='Top 10 ranking of corporations active in faction warfare by total kills. A corporation is considered "active" if they have participated in faction warfare in the past 14 days',
        max_items=10,
        title='get_fw_leaderboards_corporations_active_total',
    )
    last_week: List[LastWeekItem] = Field(
        ...,
        description='Top 10 ranking of corporations by kills in the past week',
        max_items=10,
        title='get_fw_leaderboards_corporations_last_week',
    )
    yesterday: List[YesterdayItem] = Field(
        ...,
        description='Top 10 ranking of corporations by kills in the past day',
        max_items=10,
        title='get_fw_leaderboards_corporations_yesterday',
    )


class ActiveTotalItem1(BaseModel):
    amount: Optional[int] = Field(
        None,
        description='Amount of victory points',
        title='get_fw_leaderboards_corporations_active_total_amount',
    )
    corporation_id: Optional[int] = Field(
        None,
        description='corporation_id integer',
        title='get_fw_leaderboards_corporations_active_total_corporation_id',
    )


class LastWeekItem1(BaseModel):
    amount: Optional[int] = Field(
        None,
        description='Amount of victory points',
        title='get_fw_leaderboards_corporations_last_week_amount_1',
    )
    corporation_id: Optional[int] = Field(
        None,
        description='corporation_id integer',
        title='get_fw_leaderboards_corporations_last_week_corporation_id_1',
    )


class YesterdayItem1(BaseModel):
    amount: Optional[int] = Field(
        None,
        description='Amount of victory points',
        title='get_fw_leaderboards_corporations_yesterday_amount_1',
    )
    corporation_id: Optional[int] = Field(
        None,
        description='corporation_id integer',
        title='get_fw_leaderboards_corporations_yesterday_corporation_id_1',
    )


class VictoryPoints(BaseModel):
    active_total: List[ActiveTotalItem1] = Field(
        ...,
        description='Top 10 ranking of corporations active in faction warfare by total victory points. A corporation is considered "active" if they have participated in faction warfare in the past 14 days',
        max_items=10,
        title='get_fw_leaderboards_corporations_victory_points_active_total',
    )
    last_week: List[LastWeekItem1] = Field(
        ...,
        description='Top 10 ranking of corporations by victory points in the past week',
        max_items=10,
        title='get_fw_leaderboards_corporations_victory_points_last_week',
    )
    yesterday: List[YesterdayItem1] = Field(
        ...,
        description='Top 10 ranking of corporations by victory points in the past day',
        max_items=10,
        title='get_fw_leaderboards_corporations_victory_points_yesterday',
    )


class GetFwLeaderboardsCorporationsOk(BaseModel):
    kills: Kills = Field(
        ...,
        description='Top 10 rankings of corporations by number of kills from yesterday, last week and in total',
        title='get_fw_leaderboards_corporations_kills',
    )
    victory_points: VictoryPoints = Field(
        ...,
        description='Top 10 rankings of corporations by victory points from yesterday, last week and in total',
        title='get_fw_leaderboards_corporations_victory_points',
    )


class Headers200_get_fw_leaderboards_corporations(ModelBaseEVECelery):
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


class Response200_get_fw_leaderboards_corporations(ModelCachedResponse):
    """
    Corporation leaderboard of kills and victory points within faction warfare

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        {
          "kills": {
            "active_total": [
              {
                "amount": 81692,
                "corporation_id": 1000180
              },
              {
                "amount": 76793,
                "corporation_id": 1000182
              }
            ],
            "last_week": [
              {
                "amount": 290,
                "corporation_id": 1000180
              },
              {
                "amount": 169,
                "corporation_id": 1000182
              }
            ],
            "yesterday": [
              {
                "amount": 51,
                "corporation_id": 1000180
              },
              {
                "amount": 39,
                "corporation_id": 1000182
              }
            ]
          },
          "victory_points": {
            "active_total": [
              {
                "amount": 18640927,
                "corporation_id": 1000180
              },
              {
                "amount": 18078265,
                "corporation_id": 1000181
              }
            ],
            "last_week": [
              {
                "amount": 91980,
                "corporation_id": 1000180
              },
              {
                "amount": 58920,
                "corporation_id": 1000181
              }
            ],
            "yesterday": [
              {
                "amount": 12600,
                "corporation_id": 1000180
              },
              {
                "amount": 8240,
                "corporation_id": 1000181
              }
            ]
          }
        }

    """

    headers: Headers200_get_fw_leaderboards_corporations = Field(
        ..., description='The response headers for this request.'
    )
    body: GetFwLeaderboardsCorporationsOk = Field(
        ..., description='The response body for this request.'
    )
