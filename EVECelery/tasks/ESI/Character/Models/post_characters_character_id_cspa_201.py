"""
A model definition module returned by an ESI task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Models.py'.
"""
from __future__ import annotations
from EVECelery.tasks.BaseTasks.Models.ModelsBase import ModelBaseEVECelery
from EVECelery.tasks.BaseTasks.Models.ModelsCached import ModelCachedResponse
from pydantic import BaseModel, Field


class PostCharactersCharacterIdCspaCreated(BaseModel):
    __root__: float = Field(
        ...,
        description='201 created number',
        title='post_characters_character_id_cspa_created',
    )


class Headers201_post_characters_character_id_cspa(ModelBaseEVECelery):
    """
    Headers for response code 201
    """

    pass


class Response201_post_characters_character_id_cspa(ModelCachedResponse):
    """
    Aggregate cost of sending a mail from the source character to the target characters, in ISK

    Response for code 201. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        2950.0

    """

    headers: Headers201_post_characters_character_id_cspa = Field(
        ..., description='The response headers for this request.'
    )
    body: PostCharactersCharacterIdCspaCreated = Field(
        ..., description='The response body for this request.'
    )
