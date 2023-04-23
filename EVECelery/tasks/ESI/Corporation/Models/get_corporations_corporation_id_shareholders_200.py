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


class GetCorporationsCorporationIdShareholdersOkItem(BaseModel):
    share_count: int = Field(
        ...,
        description='share_count integer',
        title='get_corporations_corporation_id_shareholders_share_count',
    )
    shareholder_id: int = Field(
        ...,
        description='shareholder_id integer',
        title='get_corporations_corporation_id_shareholders_shareholder_id',
    )
    shareholder_type: Literal['character', 'corporation'] = Field(
        ...,
        description='shareholder_type string',
        title='get_corporations_corporation_id_shareholders_shareholder_type',
    )


class GetCorporationsCorporationIdShareholdersOk(BaseModel):
    __root__: List[GetCorporationsCorporationIdShareholdersOkItem] = Field(
        ...,
        description='List of shareholders',
        max_items=1000,
        title='get_corporations_corporation_id_shareholders_ok',
    )


class Headers200_get_corporations_corporation_id_shareholders(ModelBaseEVECelery):
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


class Response200_get_corporations_corporation_id_shareholders(ModelCachedResponse):
    """
    List of shareholders

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "share_count": 580,
            "shareholder_id": 98000001,
            "shareholder_type": "corporation"
          },
          {
            "share_count": 20,
            "shareholder_id": 2112000003,
            "shareholder_type": "character"
          },
          {
            "share_count": 300,
            "shareholder_id": 2112000004,
            "shareholder_type": "character"
          },
          {
            "share_count": 100,
            "shareholder_id": 2112000001,
            "shareholder_type": "character"
          }
        ]

    """

    headers: Headers200_get_corporations_corporation_id_shareholders = Field(
        ..., description='The response headers for this request.'
    )
    body: GetCorporationsCorporationIdShareholdersOk = Field(
        ..., description='The response body for this request.'
    )
