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


class PostCharactersCharacterIdContactsCreated(BaseModel):
    __root__: List[int] = Field(
        ...,
        description='201 created array',
        max_items=100,
        title='post_characters_character_id_contacts_created',
    )


class Headers201_post_characters_character_id_contacts(ModelBaseEVECelery):
    """
    Headers for response code 201
    """

    pass


class Response201_post_characters_character_id_contacts(ModelCachedResponse):
    """
    A list of contact ids that successfully created

    Response for code 201. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          123,
          456
        ]

    """

    headers: Headers201_post_characters_character_id_contacts = Field(
        ..., description='The response headers for this request.'
    )
    body: PostCharactersCharacterIdContactsCreated = Field(
        ..., description='The response body for this request.'
    )
