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


class Position(BaseModel):
    x: float = Field(
        ...,
        description='x number',
        title='post_characters_character_id_assets_locations_x',
    )
    y: float = Field(
        ...,
        description='y number',
        title='post_characters_character_id_assets_locations_y',
    )
    z: float = Field(
        ...,
        description='z number',
        title='post_characters_character_id_assets_locations_z',
    )


class PostCharactersCharacterIdAssetsLocationsOkItem(BaseModel):
    item_id: int = Field(
        ...,
        description='item_id integer',
        title='post_characters_character_id_assets_locations_item_id',
    )
    position: Position = Field(
        ...,
        description='position object',
        title='post_characters_character_id_assets_locations_position',
    )


class PostCharactersCharacterIdAssetsLocationsOk(BaseModel):
    __root__: List[PostCharactersCharacterIdAssetsLocationsOkItem] = Field(
        ...,
        description='200 ok array',
        max_items=1000,
        title='post_characters_character_id_assets_locations_ok',
    )


class Headers200_post_characters_character_id_assets_locations(ModelBaseEVECelery):
    """
    Headers for response code 200
    """

    pass


class Response200_post_characters_character_id_assets_locations(ModelCachedResponse):
    """
    List of asset locations

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "item_id": 12345,
            "position": {
              "x": 1.2,
              "y": 2.3,
              "z": -3.4
            }
          }
        ]

    """

    headers: Headers200_post_characters_character_id_assets_locations = Field(
        ..., description='The response headers for this request.'
    )
    body: PostCharactersCharacterIdAssetsLocationsOk = Field(
        ..., description='The response body for this request.'
    )
