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


class DogmaAttribute(BaseModel):
    attribute_id: int = Field(
        ...,
        description='attribute_id integer',
        title='get_universe_types_type_id_attribute_id',
    )
    value: float = Field(
        ..., description='value number', title='get_universe_types_type_id_value'
    )


class DogmaEffect(BaseModel):
    effect_id: int = Field(
        ...,
        description='effect_id integer',
        title='get_universe_types_type_id_effect_id',
    )
    is_default: bool = Field(
        ...,
        description='is_default boolean',
        title='get_universe_types_type_id_is_default',
    )


class GetUniverseTypesTypeIdOk(BaseModel):
    capacity: Optional[float] = Field(
        None, description='capacity number', title='get_universe_types_type_id_capacity'
    )
    description: str = Field(
        ...,
        description='description string',
        title='get_universe_types_type_id_description',
    )
    dogma_attributes: Optional[List[DogmaAttribute]] = Field(
        None,
        description='dogma_attributes array',
        max_items=1000,
        title='get_universe_types_type_id_dogma_attributes',
    )
    dogma_effects: Optional[List[DogmaEffect]] = Field(
        None,
        description='dogma_effects array',
        max_items=1000,
        title='get_universe_types_type_id_dogma_effects',
    )
    graphic_id: Optional[int] = Field(
        None,
        description='graphic_id integer',
        title='get_universe_types_type_id_graphic_id',
    )
    group_id: int = Field(
        ..., description='group_id integer', title='get_universe_types_type_id_group_id'
    )
    icon_id: Optional[int] = Field(
        None, description='icon_id integer', title='get_universe_types_type_id_icon_id'
    )
    market_group_id: Optional[int] = Field(
        None,
        description='This only exists for types that can be put on the market',
        title='get_universe_types_type_id_market_group_id',
    )
    mass: Optional[float] = Field(
        None, description='mass number', title='get_universe_types_type_id_mass'
    )
    name: str = Field(
        ..., description='name string', title='get_universe_types_type_id_name'
    )
    packaged_volume: Optional[float] = Field(
        None,
        description='packaged_volume number',
        title='get_universe_types_type_id_packaged_volume',
    )
    portion_size: Optional[int] = Field(
        None,
        description='portion_size integer',
        title='get_universe_types_type_id_portion_size',
    )
    published: bool = Field(
        ...,
        description='published boolean',
        title='get_universe_types_type_id_published',
    )
    radius: Optional[float] = Field(
        None, description='radius number', title='get_universe_types_type_id_radius'
    )
    type_id: int = Field(
        ..., description='type_id integer', title='get_universe_types_type_id_type_id'
    )
    volume: Optional[float] = Field(
        None, description='volume number', title='get_universe_types_type_id_volume'
    )


class Headers200_get_universe_types_type_id(ModelBaseEVECelery):
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


class Response200_get_universe_types_type_id(ModelCachedResponse):
    """
    Information about a type

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        {
          "description": "The Rifter is a...",
          "group_id": 25,
          "name": "Rifter",
          "published": true,
          "type_id": 587
        }

    """

    headers: Headers200_get_universe_types_type_id = Field(
        ..., description='The response headers for this request.'
    )
    body: GetUniverseTypesTypeIdOk = Field(
        ..., description='The response body for this request.'
    )
