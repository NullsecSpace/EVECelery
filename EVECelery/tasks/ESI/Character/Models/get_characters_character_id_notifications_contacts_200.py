"""
A model definition module returned by an ESI task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Models.py'.
"""
from __future__ import annotations
from EVECelery.tasks.BaseTasks.Models.ModelsBase import ModelBaseEVECelery
from EVECelery.tasks.BaseTasks.Models.ModelsCached import ModelCachedResponse
from datetime import datetime
from typing import List

from pydantic import BaseModel, Field


class GetCharactersCharacterIdNotificationsContactsOkItem(BaseModel):
    message: str = Field(
        ...,
        description='message string',
        title='get_characters_character_id_notifications_contacts_message',
    )
    notification_id: int = Field(
        ...,
        description='notification_id integer',
        title='get_characters_character_id_notifications_contacts_notification_id',
    )
    send_date: datetime = Field(
        ...,
        description='send_date string',
        title='get_characters_character_id_notifications_contacts_send_date',
    )
    sender_character_id: int = Field(
        ...,
        description='sender_character_id integer',
        title='get_characters_character_id_notifications_contacts_sender_character_id',
    )
    standing_level: float = Field(
        ...,
        description='A number representing the standing level the receiver has been added at by the sender. The standing levels are as follows: -10 -> Terrible | -5 -> Bad |  0 -> Neutral |  5 -> Good |  10 -> Excellent',
        title='get_characters_character_id_notifications_contacts_standing_level',
    )


class GetCharactersCharacterIdNotificationsContactsOk(BaseModel):
    __root__: List[GetCharactersCharacterIdNotificationsContactsOkItem] = Field(
        ...,
        description='200 ok array',
        max_items=50,
        title='get_characters_character_id_notifications_contacts_ok',
    )


class Headers200_get_characters_character_id_notifications_contacts(ModelBaseEVECelery):
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


class Response200_get_characters_character_id_notifications_contacts(
    ModelCachedResponse
):
    """
    A list of contact notifications

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "message": "hello friend :3",
            "notification_id": 1,
            "send_date": "2017-08-16T10:08:00Z",
            "sender_character_id": 95465499,
            "standing_level": 1.5
          }
        ]

    """

    headers: Headers200_get_characters_character_id_notifications_contacts = Field(
        ..., description='The response headers for this request.'
    )
    body: GetCharactersCharacterIdNotificationsContactsOk = Field(
        ..., description='The response body for this request.'
    )
