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


class Modifier(BaseModel):
    domain: Optional[str] = Field(
        None, description='domain string', title='get_dogma_effects_effect_id_domain'
    )
    effect_id: Optional[int] = Field(
        None,
        description='effect_id integer',
        title='get_dogma_effects_effect_id_modifier_effect_id',
    )
    func: str = Field(
        ..., description='func string', title='get_dogma_effects_effect_id_func'
    )
    modified_attribute_id: Optional[int] = Field(
        None,
        description='modified_attribute_id integer',
        title='get_dogma_effects_effect_id_modified_attribute_id',
    )
    modifying_attribute_id: Optional[int] = Field(
        None,
        description='modifying_attribute_id integer',
        title='get_dogma_effects_effect_id_modifying_attribute_id',
    )
    operator: Optional[int] = Field(
        None,
        description='operator integer',
        title='get_dogma_effects_effect_id_operator',
    )


class GetDogmaEffectsEffectIdOk(BaseModel):
    description: Optional[str] = Field(
        None,
        description='description string',
        title='get_dogma_effects_effect_id_description',
    )
    disallow_auto_repeat: Optional[bool] = Field(
        None,
        description='disallow_auto_repeat boolean',
        title='get_dogma_effects_effect_id_disallow_auto_repeat',
    )
    discharge_attribute_id: Optional[int] = Field(
        None,
        description='discharge_attribute_id integer',
        title='get_dogma_effects_effect_id_discharge_attribute_id',
    )
    display_name: Optional[str] = Field(
        None,
        description='display_name string',
        title='get_dogma_effects_effect_id_display_name',
    )
    duration_attribute_id: Optional[int] = Field(
        None,
        description='duration_attribute_id integer',
        title='get_dogma_effects_effect_id_duration_attribute_id',
    )
    effect_category: Optional[int] = Field(
        None,
        description='effect_category integer',
        title='get_dogma_effects_effect_id_effect_category',
    )
    effect_id: int = Field(
        ...,
        description='effect_id integer',
        title='get_dogma_effects_effect_id_effect_id',
    )
    electronic_chance: Optional[bool] = Field(
        None,
        description='electronic_chance boolean',
        title='get_dogma_effects_effect_id_electronic_chance',
    )
    falloff_attribute_id: Optional[int] = Field(
        None,
        description='falloff_attribute_id integer',
        title='get_dogma_effects_effect_id_falloff_attribute_id',
    )
    icon_id: Optional[int] = Field(
        None, description='icon_id integer', title='get_dogma_effects_effect_id_icon_id'
    )
    is_assistance: Optional[bool] = Field(
        None,
        description='is_assistance boolean',
        title='get_dogma_effects_effect_id_is_assistance',
    )
    is_offensive: Optional[bool] = Field(
        None,
        description='is_offensive boolean',
        title='get_dogma_effects_effect_id_is_offensive',
    )
    is_warp_safe: Optional[bool] = Field(
        None,
        description='is_warp_safe boolean',
        title='get_dogma_effects_effect_id_is_warp_safe',
    )
    modifiers: Optional[List[Modifier]] = Field(
        None,
        description='modifiers array',
        max_items=100,
        title='get_dogma_effects_effect_id_modifiers',
    )
    name: Optional[str] = Field(
        None, description='name string', title='get_dogma_effects_effect_id_name'
    )
    post_expression: Optional[int] = Field(
        None,
        description='post_expression integer',
        title='get_dogma_effects_effect_id_post_expression',
    )
    pre_expression: Optional[int] = Field(
        None,
        description='pre_expression integer',
        title='get_dogma_effects_effect_id_pre_expression',
    )
    published: Optional[bool] = Field(
        None,
        description='published boolean',
        title='get_dogma_effects_effect_id_published',
    )
    range_attribute_id: Optional[int] = Field(
        None,
        description='range_attribute_id integer',
        title='get_dogma_effects_effect_id_range_attribute_id',
    )
    range_chance: Optional[bool] = Field(
        None,
        description='range_chance boolean',
        title='get_dogma_effects_effect_id_range_chance',
    )
    tracking_speed_attribute_id: Optional[int] = Field(
        None,
        description='tracking_speed_attribute_id integer',
        title='get_dogma_effects_effect_id_tracking_speed_attribute_id',
    )


class Headers200_get_dogma_effects_effect_id(ModelBaseEVECelery):
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


class Response200_get_dogma_effects_effect_id(ModelCachedResponse):
    """
    Information about a dogma effect

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        {
          "description": "Requires a high power slot.",
          "display_name": "High power",
          "effect_category": 0,
          "effect_id": 12,
          "icon_id": 293,
          "name": "hiPower",
          "post_expression": 131,
          "pre_expression": 131,
          "published": true
        }

    """

    headers: Headers200_get_dogma_effects_effect_id = Field(
        ..., description='The response headers for this request.'
    )
    body: GetDogmaEffectsEffectIdOk = Field(
        ..., description='The response body for this request.'
    )
