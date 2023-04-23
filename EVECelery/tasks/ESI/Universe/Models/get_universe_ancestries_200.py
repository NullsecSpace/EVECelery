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


class GetUniverseAncestriesOkItem(BaseModel):
    bloodline_id: int = Field(
        ...,
        description='The bloodline associated with this ancestry',
        title='get_universe_ancestries_bloodline_id',
    )
    description: str = Field(
        ...,
        description='description string',
        title='get_universe_ancestries_description',
    )
    icon_id: Optional[int] = Field(
        None, description='icon_id integer', title='get_universe_ancestries_icon_id'
    )
    id: int = Field(..., description='id integer', title='get_universe_ancestries_id')
    name: str = Field(
        ..., description='name string', title='get_universe_ancestries_name'
    )
    short_description: Optional[str] = Field(
        None,
        description='short_description string',
        title='get_universe_ancestries_short_description',
    )


class GetUniverseAncestriesOk(BaseModel):
    __root__: List[GetUniverseAncestriesOkItem] = Field(
        ...,
        description='200 ok array',
        max_items=100,
        title='get_universe_ancestries_ok',
    )


class Headers200_get_universe_ancestries(ModelBaseEVECelery):
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


class Response200_get_universe_ancestries(ModelCachedResponse):
    """
    A list of ancestries

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "bloodline_id": 1,
            "description": "Acutely aware of the small population...",
            "id": 12,
            "name": "Tube Child",
            "short_description": "Manufactured citizens of the State."
          }
        ]

    """

    headers: Headers200_get_universe_ancestries = Field(
        ..., description='The response headers for this request.'
    )
    body: GetUniverseAncestriesOk = Field(
        ..., description='The response body for this request.'
    )
