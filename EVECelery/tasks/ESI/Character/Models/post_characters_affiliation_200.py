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


class PostCharactersAffiliationOkItem(BaseModel):
    alliance_id: Optional[int] = Field(
        None,
        description="The character's alliance ID, if their corporation is in an alliance",
        title='post_characters_affiliation_alliance_id',
    )
    character_id: int = Field(
        ...,
        description="The character's ID",
        title='post_characters_affiliation_character_id',
    )
    corporation_id: int = Field(
        ...,
        description="The character's corporation ID",
        title='post_characters_affiliation_corporation_id',
    )
    faction_id: Optional[int] = Field(
        None,
        description="The character's faction ID, if their corporation is in a faction",
        title='post_characters_affiliation_faction_id',
    )


class PostCharactersAffiliationOk(BaseModel):
    __root__: List[PostCharactersAffiliationOkItem] = Field(
        ...,
        description='200 ok array',
        max_items=1000,
        title='post_characters_affiliation_ok',
    )


class Headers200_post_characters_affiliation(ModelBaseEVECelery):
    """
    Headers for response code 200
    """

    pass


class Response200_post_characters_affiliation(ModelCachedResponse):
    """
    Character corporation, alliance and faction IDs

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "alliance_id": 434243723,
            "character_id": 95538921,
            "corporation_id": 109299958
          }
        ]

    """

    headers: Headers200_post_characters_affiliation = Field(
        ..., description='The response headers for this request.'
    )
    body: PostCharactersAffiliationOk = Field(
        ..., description='The response body for this request.'
    )
