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


class GetDogmaEffectsOk(BaseModel):
    __root__: List[int] = Field(
        ..., description='200 ok array', max_items=10000, title='get_dogma_effects_ok'
    )


class Headers200_get_dogma_effects(ModelBaseEVECelery):
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


class Response200_get_dogma_effects(ModelCachedResponse):
    """
    A list of dogma effect ids

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          1,
          2,
          3
        ]

    """

    headers: Headers200_get_dogma_effects = Field(
        ..., description='The response headers for this request.'
    )
    body: GetDogmaEffectsOk = Field(
        ..., description='The response body for this request.'
    )
