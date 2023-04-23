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


class GetCorporationsCorporationIdMembersTitlesOkItem(BaseModel):
    character_id: int = Field(
        ...,
        description='character_id integer',
        title='get_corporations_corporation_id_members_titles_character_id',
    )
    titles: List[int] = Field(
        ...,
        description='A list of title_id',
        max_items=16,
        title='get_corporations_corporation_id_members_titles_titles',
    )


class GetCorporationsCorporationIdMembersTitlesOk(BaseModel):
    __root__: List[GetCorporationsCorporationIdMembersTitlesOkItem] = Field(
        ...,
        description='200 ok array',
        max_items=12601,
        title='get_corporations_corporation_id_members_titles_ok',
    )


class Headers200_get_corporations_corporation_id_members_titles(ModelBaseEVECelery):
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


class Response200_get_corporations_corporation_id_members_titles(ModelCachedResponse):
    """
    A list of members and theirs titles

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "character_id": 12345,
            "titles": []
          }
        ]

    """

    headers: Headers200_get_corporations_corporation_id_members_titles = Field(
        ..., description='The response headers for this request.'
    )
    body: GetCorporationsCorporationIdMembersTitlesOk = Field(
        ..., description='The response body for this request.'
    )
