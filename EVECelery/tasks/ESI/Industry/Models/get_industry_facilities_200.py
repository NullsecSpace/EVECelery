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


class GetIndustryFacilitiesOkItem(BaseModel):
    facility_id: int = Field(
        ...,
        description='ID of the facility',
        title='get_industry_facilities_facility_id',
    )
    owner_id: int = Field(
        ...,
        description='Owner of the facility',
        title='get_industry_facilities_owner_id',
    )
    region_id: int = Field(
        ...,
        description='Region ID where the facility is',
        title='get_industry_facilities_region_id',
    )
    solar_system_id: int = Field(
        ...,
        description='Solar system ID where the facility is',
        title='get_industry_facilities_solar_system_id',
    )
    tax: Optional[float] = Field(
        None,
        description='Tax imposed by the facility',
        title='get_industry_facilities_tax',
    )
    type_id: int = Field(
        ...,
        description='Type ID of the facility',
        title='get_industry_facilities_type_id',
    )


class GetIndustryFacilitiesOk(BaseModel):
    __root__: List[GetIndustryFacilitiesOkItem] = Field(
        ...,
        description='200 ok array',
        max_items=10000,
        title='get_industry_facilities_ok',
    )


class Headers200_get_industry_facilities(ModelBaseEVECelery):
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


class Response200_get_industry_facilities(ModelCachedResponse):
    """
    A list of facilities

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "facility_id": 60012544,
            "owner_id": 1000126,
            "region_id": 10000001,
            "solar_system_id": 30000032,
            "tax": 0.1,
            "type_id": 2502
          }
        ]

    """

    headers: Headers200_get_industry_facilities = Field(
        ..., description='The response headers for this request.'
    )
    body: GetIndustryFacilitiesOk = Field(
        ..., description='The response body for this request.'
    )
