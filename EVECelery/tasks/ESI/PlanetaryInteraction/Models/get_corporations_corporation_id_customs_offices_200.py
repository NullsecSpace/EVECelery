"""
A model definition module returned by an ESI task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Models.py'.
"""
from __future__ import annotations
from EVECelery.tasks.BaseTasks.Models.ModelsBase import ModelBaseEVECelery
from EVECelery.tasks.BaseTasks.Models.ModelsCached import ModelCachedResponse
from typing import List, Literal, Optional

from pydantic import BaseModel, Field, conint


class GetCorporationsCorporationIdCustomsOfficesOkItem(BaseModel):
    alliance_tax_rate: Optional[float] = Field(
        None,
        description='Only present if alliance access is allowed',
        title='get_corporations_corporation_id_customs_offices_alliance_tax_rate',
    )
    allow_access_with_standings: bool = Field(
        ...,
        description='standing_level and any standing related tax rate only present when this is true',
        title='get_corporations_corporation_id_customs_offices_allow_access_with_standings',
    )
    allow_alliance_access: bool = Field(
        ...,
        description='allow_alliance_access boolean',
        title='get_corporations_corporation_id_customs_offices_allow_alliance_access',
    )
    bad_standing_tax_rate: Optional[float] = Field(
        None,
        description='bad_standing_tax_rate number',
        title='get_corporations_corporation_id_customs_offices_bad_standing_tax_rate',
    )
    corporation_tax_rate: Optional[float] = Field(
        None,
        description='corporation_tax_rate number',
        title='get_corporations_corporation_id_customs_offices_corporation_tax_rate',
    )
    excellent_standing_tax_rate: Optional[float] = Field(
        None,
        description='Tax rate for entities with excellent level of standing, only present if this level is allowed, same for all other standing related tax rates',
        title='get_corporations_corporation_id_customs_offices_excellent_standing_tax_rate',
    )
    good_standing_tax_rate: Optional[float] = Field(
        None,
        description='good_standing_tax_rate number',
        title='get_corporations_corporation_id_customs_offices_good_standing_tax_rate',
    )
    neutral_standing_tax_rate: Optional[float] = Field(
        None,
        description='neutral_standing_tax_rate number',
        title='get_corporations_corporation_id_customs_offices_neutral_standing_tax_rate',
    )
    office_id: int = Field(
        ...,
        description='unique ID of this customs office',
        title='get_corporations_corporation_id_customs_offices_office_id',
    )
    reinforce_exit_end: conint(ge=0, le=23) = Field(
        ...,
        description='reinforce_exit_end integer',
        title='get_corporations_corporation_id_customs_offices_reinforce_exit_end',
    )
    reinforce_exit_start: conint(ge=0, le=23) = Field(
        ...,
        description='Together with reinforce_exit_end, marks a 2-hour period where this customs office could exit reinforcement mode during the day after initial attack',
        title='get_corporations_corporation_id_customs_offices_reinforce_exit_start',
    )
    standing_level: Optional[
        Literal['bad', 'excellent', 'good', 'neutral', 'terrible']
    ] = Field(
        None,
        description='Access is allowed only for entities with this level of standing or better',
        title='get_corporations_corporation_id_customs_offices_standing_level',
    )
    system_id: int = Field(
        ...,
        description='ID of the solar system this customs office is located in',
        title='get_corporations_corporation_id_customs_offices_system_id',
    )
    terrible_standing_tax_rate: Optional[float] = Field(
        None,
        description='terrible_standing_tax_rate number',
        title='get_corporations_corporation_id_customs_offices_terrible_standing_tax_rate',
    )


class GetCorporationsCorporationIdCustomsOfficesOk(BaseModel):
    __root__: List[GetCorporationsCorporationIdCustomsOfficesOkItem] = Field(
        ...,
        description='200 ok array',
        max_items=1000,
        title='get_corporations_corporation_id_customs_offices_ok',
    )


class Headers200_get_corporations_corporation_id_customs_offices(ModelBaseEVECelery):
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
    X_Pages: int | None = Field(description="Maximum page number", alias="X-Pages")


class Response200_get_corporations_corporation_id_customs_offices(ModelCachedResponse):
    """
    A list of customs offices and their settings

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "alliance_tax_rate": 0.1,
            "allow_access_with_standings": true,
            "allow_alliance_access": false,
            "corporation_tax_rate": 0.02,
            "excellent_standing_tax_rate": 0.05,
            "good_standing_tax_rate": 0.2,
            "neutral_standing_tax_rate": 0.5,
            "office_id": 1000000014530,
            "reinforce_exit_end": 1,
            "reinforce_exit_start": 23,
            "standing_level": "neutral",
            "system_id": 30003657
          }
        ]

    """

    headers: Headers200_get_corporations_corporation_id_customs_offices = Field(
        ..., description='The response headers for this request.'
    )
    body: GetCorporationsCorporationIdCustomsOfficesOk = Field(
        ..., description='The response body for this request.'
    )
