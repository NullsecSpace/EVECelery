"""
A model definition module returned by an ESI task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Models.py'.
"""
from __future__ import annotations
from EVECelery.tasks.BaseTasks.Models.ModelsBase import ModelBaseEVECelery
from EVECelery.tasks.BaseTasks.Models.ModelsCached import ModelCachedResponse
from typing import List

from pydantic import BaseModel, Field, conint


class GetCorporationsCorporationIdWalletsOkItem(BaseModel):
    balance: float = Field(
        ...,
        description='balance number',
        title='get_corporations_corporation_id_wallets_balance',
    )
    division: conint(ge=1, le=7) = Field(
        ...,
        description='division integer',
        title='get_corporations_corporation_id_wallets_division',
    )


class GetCorporationsCorporationIdWalletsOk(BaseModel):
    __root__: List[GetCorporationsCorporationIdWalletsOkItem] = Field(
        ...,
        description='200 ok array',
        max_items=7,
        title='get_corporations_corporation_id_wallets_ok',
    )


class Headers200_get_corporations_corporation_id_wallets(ModelBaseEVECelery):
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


class Response200_get_corporations_corporation_id_wallets(ModelCachedResponse):
    """
    List of corporation wallets

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "balance": 123.45,
            "division": 1
          },
          {
            "balance": 123.45,
            "division": 2
          },
          {
            "balance": 123.45,
            "division": 3
          },
          {
            "balance": 123.45,
            "division": 4
          },
          {
            "balance": 123.45,
            "division": 5
          },
          {
            "balance": 123.45,
            "division": 6
          },
          {
            "balance": 123.45,
            "division": 7
          }
        ]

    """

    headers: Headers200_get_corporations_corporation_id_wallets = Field(
        ..., description='The response headers for this request.'
    )
    body: GetCorporationsCorporationIdWalletsOk = Field(
        ..., description='The response body for this request.'
    )
