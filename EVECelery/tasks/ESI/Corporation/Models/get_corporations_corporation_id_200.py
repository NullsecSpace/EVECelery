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

from pydantic import BaseModel, Field, confloat


class GetCorporationsCorporationIdOk(BaseModel):
    alliance_id: Optional[int] = Field(
        None,
        description='ID of the alliance that corporation is a member of, if any',
        title='get_corporations_corporation_id_alliance_id',
    )
    ceo_id: int = Field(
        ...,
        description='ceo_id integer',
        title='get_corporations_corporation_id_ceo_id',
    )
    creator_id: int = Field(
        ...,
        description='creator_id integer',
        title='get_corporations_corporation_id_creator_id',
    )
    date_founded: Optional[datetime] = Field(
        None,
        description='date_founded string',
        title='get_corporations_corporation_id_date_founded',
    )
    description: Optional[str] = Field(
        None,
        description='description string',
        title='get_corporations_corporation_id_description',
    )
    faction_id: Optional[int] = Field(
        None,
        description='faction_id integer',
        title='get_corporations_corporation_id_faction_id',
    )
    home_station_id: Optional[int] = Field(
        None,
        description='home_station_id integer',
        title='get_corporations_corporation_id_home_station_id',
    )
    member_count: int = Field(
        ...,
        description='member_count integer',
        title='get_corporations_corporation_id_member_count',
    )
    name: str = Field(
        ...,
        description='the full name of the corporation',
        title='get_corporations_corporation_id_name',
    )
    shares: Optional[int] = Field(
        None,
        description='shares integer',
        title='get_corporations_corporation_id_shares',
    )
    tax_rate: confloat(ge=0.0, le=1.0) = Field(
        ...,
        description='tax_rate number',
        title='get_corporations_corporation_id_tax_rate',
    )
    ticker: str = Field(
        ...,
        description='the short name of the corporation',
        title='get_corporations_corporation_id_ticker',
    )
    url: Optional[str] = Field(
        None, description='url string', title='get_corporations_corporation_id_url'
    )
    war_eligible: Optional[bool] = Field(
        None,
        description='war_eligible boolean',
        title='get_corporations_corporation_id_war_eligible',
    )


class Headers200_get_corporations_corporation_id(ModelBaseEVECelery):
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


class Response200_get_corporations_corporation_id(ModelCachedResponse):
    """
    Public information about a corporation

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        {
          "alliance_id": 434243723,
          "ceo_id": 180548812,
          "creator_id": 180548812,
          "date_founded": "2004-11-28T16:42:51Z",
          "description": "This is a corporation description, it's basically just a string",
          "member_count": 656,
          "name": "C C P",
          "tax_rate": 0.256,
          "ticker": "-CCP-",
          "url": "http://www.eveonline.com"
        }

    """

    headers: Headers200_get_corporations_corporation_id = Field(
        ..., description='The response headers for this request.'
    )
    body: GetCorporationsCorporationIdOk = Field(
        ..., description='The response body for this request.'
    )
