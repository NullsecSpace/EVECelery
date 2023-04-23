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


class GetCharactersCharacterIdTitlesOkItem(BaseModel):
    name: Optional[str] = Field(
        None, description='name string', title='get_characters_character_id_titles_name'
    )
    title_id: Optional[int] = Field(
        None,
        description='title_id integer',
        title='get_characters_character_id_titles_title_id',
    )


class GetCharactersCharacterIdTitlesOk(BaseModel):
    __root__: List[GetCharactersCharacterIdTitlesOkItem] = Field(
        ...,
        description='200 ok array',
        max_items=16,
        title='get_characters_character_id_titles_ok',
    )


class Headers200_get_characters_character_id_titles(ModelBaseEVECelery):
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


class Response200_get_characters_character_id_titles(ModelCachedResponse):
    """
    A list of titles

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "name": "Awesome Title",
            "title_id": 1
          }
        ]

    """

    headers: Headers200_get_characters_character_id_titles = Field(
        ..., description='The response headers for this request.'
    )
    body: GetCharactersCharacterIdTitlesOk = Field(
        ..., description='The response body for this request.'
    )
