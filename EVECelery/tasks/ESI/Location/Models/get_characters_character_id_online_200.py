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


class GetCharactersCharacterIdOnlineOk(BaseModel):
    last_login: Optional[datetime] = Field(
        None,
        description='Timestamp of the last login',
        title='get_characters_character_id_online_last_login',
    )
    last_logout: Optional[datetime] = Field(
        None,
        description='Timestamp of the last logout',
        title='get_characters_character_id_online_last_logout',
    )
    logins: Optional[int] = Field(
        None,
        description='Total number of times the character has logged in',
        title='get_characters_character_id_online_logins',
    )
    online: bool = Field(
        ...,
        description='If the character is online',
        title='get_characters_character_id_online_online',
    )


class Headers200_get_characters_character_id_online(ModelBaseEVECelery):
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


class Response200_get_characters_character_id_online(ModelCachedResponse):
    """
    Object describing the character's online status

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        {
          "last_login": "2017-01-02T03:04:05Z",
          "last_logout": "2017-01-02T04:05:06Z",
          "logins": 9001,
          "online": true
        }

    """

    headers: Headers200_get_characters_character_id_online = Field(
        ..., description='The response headers for this request.'
    )
    body: GetCharactersCharacterIdOnlineOk = Field(
        ..., description='The response body for this request.'
    )
