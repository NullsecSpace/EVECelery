"""
A model definition module returned by an ESI task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Models.py'.
"""
from __future__ import annotations
from EVECelery.tasks.BaseTasks.Models.ModelsBase import ModelBaseEVECelery
from EVECelery.tasks.BaseTasks.Models.ModelsCached import ModelCachedResponse
from datetime import datetime
from typing import List

from pydantic import BaseModel, Field


class GetCharactersCharacterIdOpportunitiesOkItem(BaseModel):
    completed_at: datetime = Field(
        ...,
        description='completed_at string',
        title='get_characters_character_id_opportunities_completed_at',
    )
    task_id: int = Field(
        ...,
        description='task_id integer',
        title='get_characters_character_id_opportunities_task_id',
    )


class GetCharactersCharacterIdOpportunitiesOk(BaseModel):
    __root__: List[GetCharactersCharacterIdOpportunitiesOkItem] = Field(
        ...,
        description='200 ok array',
        max_items=100,
        title='get_characters_character_id_opportunities_ok',
    )


class Headers200_get_characters_character_id_opportunities(ModelBaseEVECelery):
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


class Response200_get_characters_character_id_opportunities(ModelCachedResponse):
    """
    A list of opportunities task ids

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "completed_at": "2016-04-29T12:34:56Z",
            "task_id": 1
          }
        ]

    """

    headers: Headers200_get_characters_character_id_opportunities = Field(
        ..., description='The response headers for this request.'
    )
    body: GetCharactersCharacterIdOpportunitiesOk = Field(
        ..., description='The response body for this request.'
    )
