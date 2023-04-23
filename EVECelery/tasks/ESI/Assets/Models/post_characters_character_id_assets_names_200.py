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


class PostCharactersCharacterIdAssetsNamesOkItem(BaseModel):
    item_id: int = Field(
        ...,
        description='item_id integer',
        title='post_characters_character_id_assets_names_item_id',
    )
    name: str = Field(
        ...,
        description='name string',
        title='post_characters_character_id_assets_names_name',
    )


class PostCharactersCharacterIdAssetsNamesOk(BaseModel):
    __root__: List[PostCharactersCharacterIdAssetsNamesOkItem] = Field(
        ...,
        description='200 ok array',
        max_items=1000,
        title='post_characters_character_id_assets_names_ok',
    )


class Headers200_post_characters_character_id_assets_names(ModelBaseEVECelery):
    """
    Headers for response code 200
    """

    pass


class Response200_post_characters_character_id_assets_names(ModelCachedResponse):
    """
    List of asset names

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "item_id": 12345,
            "name": "Awesome Name"
          }
        ]

    """

    headers: Headers200_post_characters_character_id_assets_names = Field(
        ..., description='The response headers for this request.'
    )
    body: PostCharactersCharacterIdAssetsNamesOk = Field(
        ..., description='The response body for this request.'
    )
