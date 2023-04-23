"""
A model definition module returned by an ESI task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Models.py'.
"""
from __future__ import annotations
from EVECelery.tasks.BaseTasks.Models.ModelsBase import ModelBaseEVECelery
from EVECelery.tasks.BaseTasks.Models.ModelsCached import ModelCachedResponse
from datetime import datetime
from typing import List, Literal, Optional

from pydantic import BaseModel, Field


class Recipient(BaseModel):
    recipient_id: int = Field(
        ...,
        description='recipient_id integer',
        title='get_characters_character_id_mail_recipient_id',
    )
    recipient_type: Literal[
        'alliance', 'character', 'corporation', 'mailing_list'
    ] = Field(
        ...,
        description='recipient_type string',
        title='get_characters_character_id_mail_recipient_type',
    )


class GetCharactersCharacterIdMailOkItem(BaseModel):
    from_: Optional[int] = Field(
        None,
        alias='from',
        description='From whom the mail was sent',
        title='get_characters_character_id_mail_from',
    )
    is_read: Optional[bool] = Field(
        None,
        description='is_read boolean',
        title='get_characters_character_id_mail_is_read',
    )
    labels: Optional[List[int]] = Field(
        None,
        description='labels array',
        ge=0,
        max_items=25,
        title='get_characters_character_id_mail_labels',
        unique_items=True,
    )
    mail_id: Optional[int] = Field(
        None,
        description='mail_id integer',
        title='get_characters_character_id_mail_mail_id',
    )
    recipients: Optional[List[Recipient]] = Field(
        None,
        description='Recipients of the mail',
        max_items=52,
        min_items=0,
        title='get_characters_character_id_mail_recipients',
        unique_items=True,
    )
    subject: Optional[str] = Field(
        None,
        description='Mail subject',
        title='get_characters_character_id_mail_subject',
    )
    timestamp: Optional[datetime] = Field(
        None,
        description='When the mail was sent',
        title='get_characters_character_id_mail_timestamp',
    )


class GetCharactersCharacterIdMailOk(BaseModel):
    __root__: List[GetCharactersCharacterIdMailOkItem] = Field(
        ...,
        description='200 ok array',
        max_items=50,
        title='get_characters_character_id_mail_ok',
    )


class Headers200_get_characters_character_id_mail(ModelBaseEVECelery):
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


class Response200_get_characters_character_id_mail(ModelCachedResponse):
    """
    The requested mail

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "from": 90000001,
            "is_read": true,
            "labels": [
              3
            ],
            "mail_id": 7,
            "recipients": [
              {
                "recipient_id": 90000002,
                "recipient_type": "character"
              }
            ],
            "subject": "Title for EVE Mail",
            "timestamp": "2015-09-30T16:07:00Z"
          }
        ]

    """

    headers: Headers200_get_characters_character_id_mail = Field(
        ..., description='The response headers for this request.'
    )
    body: GetCharactersCharacterIdMailOk = Field(
        ..., description='The response body for this request.'
    )
