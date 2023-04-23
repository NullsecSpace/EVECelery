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


class GetAlliancesAllianceIdOk(BaseModel):
    creator_corporation_id: int = Field(
        ...,
        description='ID of the corporation that created the alliance',
        title='get_alliances_alliance_id_creator_corporation_id',
    )
    creator_id: int = Field(
        ...,
        description='ID of the character that created the alliance',
        title='get_alliances_alliance_id_creator_id',
    )
    date_founded: datetime = Field(
        ...,
        description='date_founded string',
        title='get_alliances_alliance_id_date_founded',
    )
    executor_corporation_id: Optional[int] = Field(
        None,
        description='the executor corporation ID, if this alliance is not closed',
        title='get_alliances_alliance_id_executor_corporation_id',
    )
    faction_id: Optional[int] = Field(
        None,
        description='Faction ID this alliance is fighting for, if this alliance is enlisted in factional warfare',
        title='get_alliances_alliance_id_faction_id',
    )
    name: str = Field(
        ...,
        description='the full name of the alliance',
        title='get_alliances_alliance_id_name',
    )
    ticker: str = Field(
        ...,
        description='the short name of the alliance',
        title='get_alliances_alliance_id_ticker',
    )


class Headers200_get_alliances_alliance_id(ModelBaseEVECelery):
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


class Response200_get_alliances_alliance_id(ModelCachedResponse):
    """
    Public data about an alliance

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        {
          "creator_corporation_id": 45678,
          "creator_id": 12345,
          "date_founded": "2016-06-26T21:00:00Z",
          "executor_corporation_id": 98356193,
          "name": "C C P Alliance",
          "ticker": "<C C P>"
        }

    """

    headers: Headers200_get_alliances_alliance_id = Field(
        ..., description='The response headers for this request.'
    )
    body: GetAlliancesAllianceIdOk = Field(
        ..., description='The response body for this request.'
    )
