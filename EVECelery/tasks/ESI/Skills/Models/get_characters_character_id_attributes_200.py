"""
A model definition module returned by an ESI task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Models.py'.
"""
from __future__ import annotations
from EVECelery.tasks.BaseTasks.Models.ModelsBase import ModelBaseEVECelery
from EVECelery.tasks.BaseTasks.Models.ModelsCached import ModelCachedResponse
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class GetCharactersCharacterIdAttributesOk(BaseModel):
    accrued_remap_cooldown_date: Optional[datetime] = Field(
        None,
        description='Neural remapping cooldown after a character uses remap accrued over time',
        title='get_characters_character_id_attributes_accrued_remap_cooldown_date',
    )
    bonus_remaps: Optional[int] = Field(
        None,
        description='Number of available bonus character neural remaps',
        title='get_characters_character_id_attributes_bonus_remaps',
    )
    charisma: int = Field(
        ...,
        description='charisma integer',
        title='get_characters_character_id_attributes_charisma',
    )
    intelligence: int = Field(
        ...,
        description='intelligence integer',
        title='get_characters_character_id_attributes_intelligence',
    )
    last_remap_date: Optional[datetime] = Field(
        None,
        description='Datetime of last neural remap, including usage of bonus remaps',
        title='get_characters_character_id_attributes_last_remap_date',
    )
    memory: int = Field(
        ...,
        description='memory integer',
        title='get_characters_character_id_attributes_memory',
    )
    perception: int = Field(
        ...,
        description='perception integer',
        title='get_characters_character_id_attributes_perception',
    )
    willpower: int = Field(
        ...,
        description='willpower integer',
        title='get_characters_character_id_attributes_willpower',
    )


class Headers200_get_characters_character_id_attributes(ModelBaseEVECelery):
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


class Response200_get_characters_character_id_attributes(ModelCachedResponse):
    """
    Attributes of a character

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        {
          "charisma": 20,
          "intelligence": 20,
          "memory": 20,
          "perception": 20,
          "willpower": 20
        }

    """

    headers: Headers200_get_characters_character_id_attributes = Field(
        ..., description='The response headers for this request.'
    )
    body: GetCharactersCharacterIdAttributesOk = Field(
        ..., description='The response body for this request.'
    )
