"""
A model definition module returned by an ESI task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Models.py'.
"""
from __future__ import annotations
from EVECelery.tasks.BaseTasks.Models.ModelsBase import ModelBaseEVECelery
from EVECelery.tasks.BaseTasks.Models.ModelsCached import ModelCachedResponse
from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field


class GetCorporationsCorporationIdMembertrackingOkItem(BaseModel):
    base_id: Optional[int] = Field(
        None,
        description='base_id integer',
        title='get_corporations_corporation_id_membertracking_base_id',
    )
    character_id: int = Field(
        ...,
        description='character_id integer',
        title='get_corporations_corporation_id_membertracking_character_id',
    )
    location_id: Optional[int] = Field(
        None,
        description='location_id integer',
        title='get_corporations_corporation_id_membertracking_location_id',
    )
    logoff_date: Optional[datetime] = Field(
        None,
        description='logoff_date string',
        title='get_corporations_corporation_id_membertracking_logoff_date',
    )
    logon_date: Optional[datetime] = Field(
        None,
        description='logon_date string',
        title='get_corporations_corporation_id_membertracking_logon_date',
    )
    ship_type_id: Optional[int] = Field(
        None,
        description='ship_type_id integer',
        title='get_corporations_corporation_id_membertracking_ship_type_id',
    )
    start_date: Optional[datetime] = Field(
        None,
        description='start_date string',
        title='get_corporations_corporation_id_membertracking_start_date',
    )


class GetCorporationsCorporationIdMembertrackingOk(BaseModel):
    __root__: List[GetCorporationsCorporationIdMembertrackingOkItem] = Field(
        ...,
        description='200 ok array',
        max_items=12601,
        title='get_corporations_corporation_id_membertracking_ok',
    )


class Headers200_get_corporations_corporation_id_membertracking(ModelBaseEVECelery):
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


class Response200_get_corporations_corporation_id_membertracking(ModelCachedResponse):
    """
    List of member character IDs

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "character_id": 2112000001,
            "location_id": 30003657,
            "logoff_date": "2017-08-03T14:31:16Z",
            "logon_date": "2017-08-03T14:22:03Z",
            "ship_type_id": 22464,
            "start_date": "2017-07-10T14:46:00Z"
          },
          {
            "character_id": 2112000002,
            "location_id": 30003657,
            "logoff_date": "2017-07-25T11:07:40Z",
            "logon_date": "2017-07-25T10:54:00Z",
            "ship_type_id": 670,
            "start_date": "2017-07-10T14:50:00Z"
          }
        ]

    """

    headers: Headers200_get_corporations_corporation_id_membertracking = Field(
        ..., description='The response headers for this request.'
    )
    body: GetCorporationsCorporationIdMembertrackingOk = Field(
        ..., description='The response body for this request.'
    )
