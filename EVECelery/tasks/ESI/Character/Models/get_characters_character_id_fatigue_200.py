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


class GetCharactersCharacterIdFatigueOk(BaseModel):
    jump_fatigue_expire_date: Optional[datetime] = Field(
        None,
        description="Character's jump fatigue expiry",
        title='get_characters_character_id_fatigue_jump_fatigue_expire_date',
    )
    last_jump_date: Optional[datetime] = Field(
        None,
        description="Character's last jump activation",
        title='get_characters_character_id_fatigue_last_jump_date',
    )
    last_update_date: Optional[datetime] = Field(
        None,
        description="Character's last jump update",
        title='get_characters_character_id_fatigue_last_update_date',
    )


class Headers200_get_characters_character_id_fatigue(ModelBaseEVECelery):
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


class Response200_get_characters_character_id_fatigue(ModelCachedResponse):
    """
    Jump activation and fatigue information

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        {
          "jump_fatigue_expire_date": "2017-07-06T15:47:00Z",
          "last_jump_date": "2017-07-05T15:47:00Z",
          "last_update_date": "2017-07-05T15:42:00Z"
        }

    """

    headers: Headers200_get_characters_character_id_fatigue = Field(
        ..., description='The response headers for this request.'
    )
    body: GetCharactersCharacterIdFatigueOk = Field(
        ..., description='The response body for this request.'
    )
