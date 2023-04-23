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


class GetAlliancesOkItem(BaseModel):
    __root__: conint(ge=0) = Field(
        ..., description='200 ok integer', title='get_alliances_200_ok'
    )


class GetAlliancesOk(BaseModel):
    __root__: List[GetAlliancesOkItem] = Field(
        ..., description='200 ok array', max_items=5000, title='get_alliances_ok'
    )


class Headers200_get_alliances(ModelBaseEVECelery):
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


class Response200_get_alliances(ModelCachedResponse):
    """
    List of Alliance IDs

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          99000001,
          99000002
        ]

    """

    headers: Headers200_get_alliances = Field(
        ..., description='The response headers for this request.'
    )
    body: GetAlliancesOk = Field(..., description='The response body for this request.')
