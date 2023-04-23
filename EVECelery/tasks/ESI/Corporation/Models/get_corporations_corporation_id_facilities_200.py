"""
A model definition module returned by an ESI task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Models.py'.
"""
from __future__ import annotations
from EVECelery.tasks.BaseTasks.Models.ModelsBase import ModelBaseEVECelery
from EVECelery.tasks.BaseTasks.Models.ModelsCached import ModelCachedResponse
from typing import List

from pydantic import BaseModel, Field


class GetCorporationsCorporationIdFacilitiesOkItem(BaseModel):
    facility_id: int = Field(
        ...,
        description='facility_id integer',
        title='get_corporations_corporation_id_facilities_facility_id',
    )
    system_id: int = Field(
        ...,
        description='system_id integer',
        title='get_corporations_corporation_id_facilities_system_id',
    )
    type_id: int = Field(
        ...,
        description='type_id integer',
        title='get_corporations_corporation_id_facilities_type_id',
    )


class GetCorporationsCorporationIdFacilitiesOk(BaseModel):
    __root__: List[GetCorporationsCorporationIdFacilitiesOkItem] = Field(
        ...,
        description='200 ok array',
        max_items=1000,
        title='get_corporations_corporation_id_facilities_ok',
    )


class Headers200_get_corporations_corporation_id_facilities(ModelBaseEVECelery):
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


class Response200_get_corporations_corporation_id_facilities(ModelCachedResponse):
    """
    List of corporation facilities

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "facility_id": 123,
            "system_id": 45678,
            "type_id": 2502
          }
        ]

    """

    headers: Headers200_get_corporations_corporation_id_facilities = Field(
        ..., description='The response headers for this request.'
    )
    body: GetCorporationsCorporationIdFacilitiesOk = Field(
        ..., description='The response body for this request.'
    )
