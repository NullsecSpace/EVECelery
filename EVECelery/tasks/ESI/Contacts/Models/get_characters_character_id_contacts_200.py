"""
A model definition module returned by an ESI task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Models.py'.
"""
from __future__ import annotations
from EVECelery.tasks.BaseTasks.Models.ModelsBase import ModelBaseEVECelery
from EVECelery.tasks.BaseTasks.Models.ModelsCached import ModelCachedResponse
from typing import List, Literal, Optional

from pydantic import BaseModel, Field


class GetCharactersCharacterIdContactsOkItem(BaseModel):
    contact_id: int = Field(
        ...,
        description='contact_id integer',
        title='get_characters_character_id_contacts_contact_id',
    )
    contact_type: Literal['character', 'corporation', 'alliance', 'faction'] = Field(
        ...,
        description='contact_type string',
        title='get_characters_character_id_contacts_contact_type',
    )
    is_blocked: Optional[bool] = Field(
        None,
        description='Whether this contact is in the blocked list. Note a missing value denotes unknown, not true or false',
        title='get_characters_character_id_contacts_is_blocked',
    )
    is_watched: Optional[bool] = Field(
        None,
        description='Whether this contact is being watched',
        title='get_characters_character_id_contacts_is_watched',
    )
    label_ids: Optional[List[int]] = Field(
        None,
        description='label_ids array',
        max_items=63,
        title='get_characters_character_id_contacts_label_ids',
    )
    standing: float = Field(
        ...,
        description='Standing of the contact',
        title='get_characters_character_id_contacts_standing',
    )


class GetCharactersCharacterIdContactsOk(BaseModel):
    __root__: List[GetCharactersCharacterIdContactsOkItem] = Field(
        ...,
        description='200 ok array',
        max_items=1024,
        title='get_characters_character_id_contacts_ok',
    )


class Headers200_get_characters_character_id_contacts(ModelBaseEVECelery):
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
    X_Pages: int | None = Field(description="Maximum page number", alias="X-Pages")


class Response200_get_characters_character_id_contacts(ModelCachedResponse):
    """
    A list of contacts

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "contact_id": 123,
            "contact_type": "character",
            "is_blocked": true,
            "is_watched": true,
            "standing": 9.9
          }
        ]

    """

    headers: Headers200_get_characters_character_id_contacts = Field(
        ..., description='The response headers for this request.'
    )
    body: GetCharactersCharacterIdContactsOk = Field(
        ..., description='The response body for this request.'
    )
