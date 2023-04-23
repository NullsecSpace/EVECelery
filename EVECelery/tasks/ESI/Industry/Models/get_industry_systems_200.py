"""
A model definition module returned by an ESI task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Models.py'.
"""
from __future__ import annotations
from EVECelery.tasks.BaseTasks.Models.ModelsBase import ModelBaseEVECelery
from EVECelery.tasks.BaseTasks.Models.ModelsCached import ModelCachedResponse
from typing import List, Literal

from pydantic import BaseModel, Field


class CostIndice(BaseModel):
    activity: Literal[
        'copying',
        'duplicating',
        'invention',
        'manufacturing',
        'none',
        'reaction',
        'researching_material_efficiency',
        'researching_technology',
        'researching_time_efficiency',
        'reverse_engineering',
    ] = Field(..., description='activity string', title='get_industry_systems_activity')
    cost_index: float = Field(
        ..., description='cost_index number', title='get_industry_systems_cost_index'
    )


class GetIndustrySystemsOkItem(BaseModel):
    cost_indices: List[CostIndice] = Field(
        ...,
        description='cost_indices array',
        max_items=10,
        title='get_industry_systems_cost_indices',
    )
    solar_system_id: int = Field(
        ...,
        description='solar_system_id integer',
        title='get_industry_systems_solar_system_id',
    )


class GetIndustrySystemsOk(BaseModel):
    __root__: List[GetIndustrySystemsOkItem] = Field(
        ...,
        description='200 ok array',
        max_items=10000,
        title='get_industry_systems_ok',
    )


class Headers200_get_industry_systems(ModelBaseEVECelery):
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


class Response200_get_industry_systems(ModelCachedResponse):
    """
    A list of cost indicies

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "cost_indices": [
              {
                "activity": "invention",
                "cost_index": 0.0048
              }
            ],
            "solar_system_id": 30011392
          }
        ]

    """

    headers: Headers200_get_industry_systems = Field(
        ..., description='The response headers for this request.'
    )
    body: GetIndustrySystemsOk = Field(
        ..., description='The response body for this request.'
    )
