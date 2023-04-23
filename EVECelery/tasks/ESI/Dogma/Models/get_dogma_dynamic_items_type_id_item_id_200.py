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


class DogmaAttribute(BaseModel):
    attribute_id: int = Field(
        ...,
        description='attribute_id integer',
        title='get_dogma_dynamic_items_type_id_item_id_attribute_id',
    )
    value: float = Field(
        ...,
        description='value number',
        title='get_dogma_dynamic_items_type_id_item_id_value',
    )


class DogmaEffect(BaseModel):
    effect_id: int = Field(
        ...,
        description='effect_id integer',
        title='get_dogma_dynamic_items_type_id_item_id_effect_id',
    )
    is_default: bool = Field(
        ...,
        description='is_default boolean',
        title='get_dogma_dynamic_items_type_id_item_id_is_default',
    )


class GetDogmaDynamicItemsTypeIdItemIdOk(BaseModel):
    created_by: int = Field(
        ...,
        description='The ID of the character who created the item',
        title='get_dogma_dynamic_items_type_id_item_id_created_by',
    )
    dogma_attributes: List[DogmaAttribute] = Field(
        ...,
        description='dogma_attributes array',
        max_items=1000,
        title='get_dogma_dynamic_items_type_id_item_id_dogma_attributes',
    )
    dogma_effects: List[DogmaEffect] = Field(
        ...,
        description='dogma_effects array',
        max_items=1000,
        title='get_dogma_dynamic_items_type_id_item_id_dogma_effects',
    )
    mutator_type_id: int = Field(
        ...,
        description='The type ID of the mutator used to generate the dynamic item.',
        title='get_dogma_dynamic_items_type_id_item_id_mutator_type_id',
    )
    source_type_id: int = Field(
        ...,
        description='The type ID of the source item the mutator was applied to create the dynamic item.',
        title='get_dogma_dynamic_items_type_id_item_id_source_type_id',
    )


class Headers200_get_dogma_dynamic_items_type_id_item_id(ModelBaseEVECelery):
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


class Response200_get_dogma_dynamic_items_type_id_item_id(ModelCachedResponse):
    """
    Details about a dynamic item

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        {
          "created_by": 2112625428,
          "dogma_attributes": [
            {
              "attribute_id": 9,
              "value": 350
            }
          ],
          "dogma_effects": [
            {
              "effect_id": 508,
              "is_default": false
            }
          ],
          "mutator_type_id": 47845,
          "source_type_id": 33103
        }

    """

    headers: Headers200_get_dogma_dynamic_items_type_id_item_id = Field(
        ..., description='The response headers for this request.'
    )
    body: GetDogmaDynamicItemsTypeIdItemIdOk = Field(
        ..., description='The response body for this request.'
    )
