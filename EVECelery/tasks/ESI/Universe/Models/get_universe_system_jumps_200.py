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


class GetUniverseSystemJumpsOkItem(BaseModel):
    ship_jumps: int = Field(
        ...,
        description='ship_jumps integer',
        title='get_universe_system_jumps_ship_jumps',
    )
    system_id: int = Field(
        ...,
        description='system_id integer',
        title='get_universe_system_jumps_system_id',
    )


class GetUniverseSystemJumpsOk(BaseModel):
    __root__: List[GetUniverseSystemJumpsOkItem] = Field(
        ...,
        description='200 ok array',
        max_items=10000,
        title='get_universe_system_jumps_ok',
    )


class Headers200_get_universe_system_jumps(ModelBaseEVECelery):
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


class Response200_get_universe_system_jumps(ModelCachedResponse):
    """
    A list of systems and number of jumps

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "ship_jumps": 42,
            "system_id": 30002410
          }
        ]

    """

    headers: Headers200_get_universe_system_jumps = Field(
        ..., description='The response headers for this request.'
    )
    body: GetUniverseSystemJumpsOk = Field(
        ..., description='The response body for this request.'
    )
