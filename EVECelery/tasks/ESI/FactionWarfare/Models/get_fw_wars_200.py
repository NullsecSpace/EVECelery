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


class GetFwWarsOkItem(BaseModel):
    against_id: int = Field(
        ...,
        description='The faction ID of the enemy faction.',
        title='get_fw_wars_against_id',
    )
    faction_id: int = Field(
        ..., description='faction_id integer', title='get_fw_wars_faction_id'
    )


class GetFwWarsOk(BaseModel):
    __root__: List[GetFwWarsOkItem] = Field(
        ..., description='List of factions at war', max_items=8, title='get_fw_wars_ok'
    )


class Headers200_get_fw_wars(ModelBaseEVECelery):
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


class Response200_get_fw_wars(ModelCachedResponse):
    """
    A list of NPC factions at war

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "against_id": 500002,
            "faction_id": 500001
          }
        ]

    """

    headers: Headers200_get_fw_wars = Field(
        ..., description='The response headers for this request.'
    )
    body: GetFwWarsOk = Field(..., description='The response body for this request.')
