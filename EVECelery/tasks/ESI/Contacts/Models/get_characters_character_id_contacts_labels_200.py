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


class GetCharactersCharacterIdContactsLabelsOkItem(BaseModel):
    label_id: int = Field(
        ...,
        description='label_id integer',
        title='get_characters_character_id_contacts_labels_label_id',
    )
    label_name: str = Field(
        ...,
        description='label_name string',
        title='get_characters_character_id_contacts_labels_label_name',
    )


class GetCharactersCharacterIdContactsLabelsOk(BaseModel):
    __root__: List[GetCharactersCharacterIdContactsLabelsOkItem] = Field(
        ...,
        description='200 ok array',
        max_items=64,
        title='get_characters_character_id_contacts_labels_ok',
    )


class Headers200_get_characters_character_id_contacts_labels(ModelBaseEVECelery):
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


class Response200_get_characters_character_id_contacts_labels(ModelCachedResponse):
    """
    A list of contact labels

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "label_id": 123,
            "label_name": "Friends"
          }
        ]

    """

    headers: Headers200_get_characters_character_id_contacts_labels = Field(
        ..., description='The response headers for this request.'
    )
    body: GetCharactersCharacterIdContactsLabelsOk = Field(
        ..., description='The response body for this request.'
    )