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


class GetCharactersCharacterIdMailListsOkItem(BaseModel):
    mailing_list_id: int = Field(
        ...,
        description='Mailing list ID',
        title='get_characters_character_id_mail_lists_mailing_list_id',
    )
    name: str = Field(
        ...,
        description='name string',
        title='get_characters_character_id_mail_lists_name',
    )


class GetCharactersCharacterIdMailListsOk(BaseModel):
    __root__: List[GetCharactersCharacterIdMailListsOkItem] = Field(
        ...,
        description='200 ok array',
        max_items=1000,
        title='get_characters_character_id_mail_lists_ok',
    )


class Headers200_get_characters_character_id_mail_lists(ModelBaseEVECelery):
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


class Response200_get_characters_character_id_mail_lists(ModelCachedResponse):
    """
    Mailing lists

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "mailing_list_id": 1,
            "name": "test_mailing_list"
          }
        ]

    """

    headers: Headers200_get_characters_character_id_mail_lists = Field(
        ..., description='The response headers for this request.'
    )
    body: GetCharactersCharacterIdMailListsOk = Field(
        ..., description='The response body for this request.'
    )
