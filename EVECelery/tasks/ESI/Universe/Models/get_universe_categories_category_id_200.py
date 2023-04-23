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


class GetUniverseCategoriesCategoryIdOk(BaseModel):
    category_id: int = Field(
        ...,
        description='category_id integer',
        title='get_universe_categories_category_id_category_id',
    )
    groups: List[int] = Field(
        ...,
        description='groups array',
        max_items=10000,
        title='get_universe_categories_category_id_groups',
    )
    name: str = Field(
        ..., description='name string', title='get_universe_categories_category_id_name'
    )
    published: bool = Field(
        ...,
        description='published boolean',
        title='get_universe_categories_category_id_published',
    )


class Headers200_get_universe_categories_category_id(ModelBaseEVECelery):
    """
    Headers for response code 200
    """

    Cache_Control: str | None = Field(
        description="The caching mechanism used", alias="Cache-Control"
    )
    Content_Language: str | None = Field(
        description="The language used in the response", alias="Content-Language"
    )
    ETag: str | None = Field(description="RFC7232 compliant entity tag")
    Expires: str | None = Field(description="RFC7231 formatted datetime string")
    Last_Modified: str | None = Field(
        description="RFC7231 formatted datetime string", alias="Last-Modified"
    )


class Response200_get_universe_categories_category_id(ModelCachedResponse):
    """
    Information about an item category

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        {
          "category_id": 6,
          "groups": [
            25,
            26,
            27
          ],
          "name": "Ship",
          "published": true
        }

    """

    headers: Headers200_get_universe_categories_category_id = Field(
        ..., description='The response headers for this request.'
    )
    body: GetUniverseCategoriesCategoryIdOk = Field(
        ..., description='The response body for this request.'
    )
