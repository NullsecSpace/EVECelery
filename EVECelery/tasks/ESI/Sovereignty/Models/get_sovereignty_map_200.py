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


class GetSovereigntyMapOkItem(BaseModel):
    alliance_id: Optional[int] = Field(
        None, description='alliance_id integer', title='get_sovereignty_map_alliance_id'
    )
    corporation_id: Optional[int] = Field(
        None,
        description='corporation_id integer',
        title='get_sovereignty_map_corporation_id',
    )
    faction_id: Optional[int] = Field(
        None, description='faction_id integer', title='get_sovereignty_map_faction_id'
    )
    system_id: int = Field(
        ..., description='system_id integer', title='get_sovereignty_map_system_id'
    )


class GetSovereigntyMapOk(BaseModel):
    __root__: List[GetSovereigntyMapOkItem] = Field(
        ..., description='200 ok array', max_items=10000, title='get_sovereignty_map_ok'
    )


class Headers200_get_sovereignty_map(ModelBaseEVECelery):
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


class Response200_get_sovereignty_map(ModelCachedResponse):
    """
    A list of sovereignty information for solar systems in New Eden

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "faction_id": 500001,
            "system_id": 30045334
          }
        ]

    """

    headers: Headers200_get_sovereignty_map = Field(
        ..., description='The response headers for this request.'
    )
    body: GetSovereigntyMapOk = Field(
        ..., description='The response body for this request.'
    )
