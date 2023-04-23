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


class Level(BaseModel):
    cost: float = Field(
        ..., description='cost number', title='get_insurance_prices_cost'
    )
    name: str = Field(
        ..., description='Localized insurance level', title='get_insurance_prices_name'
    )
    payout: float = Field(
        ..., description='payout number', title='get_insurance_prices_payout'
    )


class GetInsurancePricesOkItem(BaseModel):
    levels: List[Level] = Field(
        ...,
        description='A list of a available insurance levels for this ship type',
        max_items=6,
        title='get_insurance_prices_levels',
    )
    type_id: int = Field(
        ..., description='type_id integer', title='get_insurance_prices_type_id'
    )


class GetInsurancePricesOk(BaseModel):
    __root__: List[GetInsurancePricesOkItem] = Field(
        ..., description='200 ok array', max_items=1000, title='get_insurance_prices_ok'
    )


class Headers200_get_insurance_prices(ModelBaseEVECelery):
    """
    Headers for response code 200
    """

    Cache_Control: str | None = Field(
        description="The caching mechanism used", alias="Cache-Control"
    )
    Content_Language: str | None = Field(
        description="The language used in the response", alias="Content-Language"
    )
    ETag: str | None = Field(description="RFC7232 compliant entity tag")
    Expires: str | None = Field(description="RFC7231 formatted datetime string")
    Last_Modified: str | None = Field(
        description="RFC7231 formatted datetime string", alias="Last-Modified"
    )


class Response200_get_insurance_prices(ModelCachedResponse):
    """
    A list of insurance levels for all ship types

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "levels": [
              {
                "cost": 10.01,
                "name": "Basic",
                "payout": 20.01
              }
            ],
            "type_id": 1
          }
        ]

    """

    headers: Headers200_get_insurance_prices = Field(
        ..., description='The response headers for this request.'
    )
    body: GetInsurancePricesOk = Field(
        ..., description='The response body for this request.'
    )
