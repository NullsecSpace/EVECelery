"""
A model definition module returned by an ESI task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Models.py'.
"""
from __future__ import annotations
from EVECelery.tasks.BaseTasks.Models.ModelsBase import ModelBaseEVECelery
from EVECelery.tasks.BaseTasks.Models.ModelsCached import ModelCachedResponse
from typing import List, Literal

from pydantic import BaseModel, Field


class PostUniverseNamesOkItem(BaseModel):
    category: Literal[
        'alliance',
        'character',
        'constellation',
        'corporation',
        'inventory_type',
        'region',
        'solar_system',
        'station',
        'faction',
    ] = Field(..., description='category string', title='post_universe_names_category')
    id: int = Field(..., description='id integer', title='post_universe_names_id')
    name: str = Field(..., description='name string', title='post_universe_names_name')


class PostUniverseNamesOk(BaseModel):
    __root__: List[PostUniverseNamesOkItem] = Field(
        ..., description='200 ok array', max_items=1000, title='post_universe_names_ok'
    )


class Headers200_post_universe_names(ModelBaseEVECelery):
    """
    Headers for response code 200
    """

    pass


class Response200_post_universe_names(ModelCachedResponse):
    """
    List of id/name associations for a set of IDs. All IDs must resolve to a name, or nothing will be returned

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "category": "character",
            "id": 95465499,
            "name": "CCP Bartender"
          },
          {
            "category": "solar_system",
            "id": 30000142,
            "name": "Jita"
          }
        ]

    """

    headers: Headers200_post_universe_names = Field(
        ..., description='The response headers for this request.'
    )
    body: PostUniverseNamesOk = Field(
        ..., description='The response body for this request.'
    )
