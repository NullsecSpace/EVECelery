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


class GetCorporationsCorporationIdAlliancehistoryOkItem(BaseModel):
    alliance_id: Optional[int] = Field(
        None,
        description='alliance_id integer',
        title='get_corporations_corporation_id_alliancehistory_alliance_id',
    )
    is_deleted: Optional[bool] = Field(
        None,
        description='True if the alliance has been closed',
        title='get_corporations_corporation_id_alliancehistory_is_deleted',
    )
    record_id: int = Field(
        ...,
        description='An incrementing ID that can be used to canonically establish order of records in cases where dates may be ambiguous',
        title='get_corporations_corporation_id_alliancehistory_record_id',
    )
    start_date: datetime = Field(
        ...,
        description='start_date string',
        title='get_corporations_corporation_id_alliancehistory_start_date',
    )


class GetCorporationsCorporationIdAlliancehistoryOk(BaseModel):
    __root__: List[GetCorporationsCorporationIdAlliancehistoryOkItem] = Field(
        ...,
        description='200 ok array',
        max_items=10000,
        title='get_corporations_corporation_id_alliancehistory_ok',
    )


class Headers200_get_corporations_corporation_id_alliancehistory(ModelBaseEVECelery):
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


class Response200_get_corporations_corporation_id_alliancehistory(ModelCachedResponse):
    """
    Alliance history for the given corporation

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "alliance_id": 99000006,
            "is_deleted": true,
            "record_id": 23,
            "start_date": "2016-10-25T14:46:00Z"
          },
          {
            "record_id": 1,
            "start_date": "2015-07-06T20:56:00Z"
          }
        ]

    """

    headers: Headers200_get_corporations_corporation_id_alliancehistory = Field(
        ..., description='The response headers for this request.'
    )
    body: GetCorporationsCorporationIdAlliancehistoryOk = Field(
        ..., description='The response body for this request.'
    )
