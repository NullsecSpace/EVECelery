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


class Participant(BaseModel):
    alliance_id: int = Field(
        ...,
        description='alliance_id integer',
        title='get_sovereignty_campaigns_alliance_id',
    )
    score: float = Field(
        ..., description='score number', title='get_sovereignty_campaigns_score'
    )


class GetSovereigntyCampaignsOkItem(BaseModel):
    attackers_score: Optional[float] = Field(
        None,
        description='Score for all attacking parties, only present in Defense Events.\n',
        title='get_sovereignty_campaigns_attackers_score',
    )
    campaign_id: int = Field(
        ...,
        description='Unique ID for this campaign.',
        title='get_sovereignty_campaigns_campaign_id',
    )
    constellation_id: int = Field(
        ...,
        description='The constellation in which the campaign will take place.\n',
        title='get_sovereignty_campaigns_constellation_id',
    )
    defender_id: Optional[int] = Field(
        None,
        description='Defending alliance, only present in Defense Events\n',
        title='get_sovereignty_campaigns_defender_id',
    )
    defender_score: Optional[float] = Field(
        None,
        description='Score for the defending alliance, only present in Defense Events.\n',
        title='get_sovereignty_campaigns_defender_score',
    )
    event_type: Literal[
        'tcu_defense', 'ihub_defense', 'station_defense', 'station_freeport'
    ] = Field(
        ...,
        description='Type of event this campaign is for. tcu_defense, ihub_defense and station_defense are referred to as "Defense Events", station_freeport as "Freeport Events".\n',
        title='get_sovereignty_campaigns_event_type',
    )
    participants: Optional[List[Participant]] = Field(
        None,
        description='Alliance participating and their respective scores, only present in Freeport Events.\n',
        max_items=5000,
        title='get_sovereignty_campaigns_participants',
    )
    solar_system_id: int = Field(
        ...,
        description='The solar system the structure is located in.\n',
        title='get_sovereignty_campaigns_solar_system_id',
    )
    start_time: datetime = Field(
        ...,
        description='Time the event is scheduled to start.\n',
        title='get_sovereignty_campaigns_start_time',
    )
    structure_id: int = Field(
        ...,
        description='The structure item ID that is related to this campaign.\n',
        title='get_sovereignty_campaigns_structure_id',
    )


class GetSovereigntyCampaignsOk(BaseModel):
    __root__: List[GetSovereigntyCampaignsOkItem] = Field(
        ...,
        description='200 ok array',
        max_items=10000,
        title='get_sovereignty_campaigns_ok',
    )


class Headers200_get_sovereignty_campaigns(ModelBaseEVECelery):
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


class Response200_get_sovereignty_campaigns(ModelCachedResponse):
    """
    A list of sovereignty campaigns

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "attackers_score": 0.4,
            "campaign_id": 32833,
            "constellation_id": 20000125,
            "defender_id": 1695357456,
            "defender_score": 0.6,
            "event_type": "station_defense",
            "solar_system_id": 30000856,
            "start_time": "2016-10-29T14:34:40Z",
            "structure_id": 61001096
          }
        ]

    """

    headers: Headers200_get_sovereignty_campaigns = Field(
        ..., description='The response headers for this request.'
    )
    body: GetSovereigntyCampaignsOk = Field(
        ..., description='The response body for this request.'
    )
