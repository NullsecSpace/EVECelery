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

from pydantic import BaseModel, Field, conint


class Label(BaseModel):
    __root__: conint(ge=0) = Field(
        ...,
        description='label integer',
        title='get_characters_character_id_mail_mail_id_label',
    )


class Recipient(BaseModel):
    recipient_id: int = Field(
        ...,
        description='recipient_id integer',
        title='get_characters_character_id_mail_mail_id_recipient_id',
    )
    recipient_type: Literal[
        'alliance', 'character', 'corporation', 'mailing_list'
    ] = Field(
        ...,
        description='recipient_type string',
        title='get_characters_character_id_mail_mail_id_recipient_type',
    )


class GetCharactersCharacterIdMailMailIdOk(BaseModel):
    body: Optional[str] = Field(
        None,
        description="Mail's body",
        title='get_characters_character_id_mail_mail_id_body',
    )
    from_: Optional[int] = Field(
        None,
        alias='from',
        description='From whom the mail was sent',
        title='get_characters_character_id_mail_mail_id_from',
    )
    labels: Optional[List[Label]] = Field(
        None,
        description='Labels attached to the mail',
        max_items=25,
        title='get_characters_character_id_mail_mail_id_labels',
    )
    read: Optional[bool] = Field(
        None,
        description='Whether the mail is flagged as read',
        title='get_characters_character_id_mail_mail_id_read',
    )
    recipients: Optional[List[Recipient]] = Field(
        None,
        description='Recipients of the mail',
        max_items=52,
        min_items=0,
        title='get_characters_character_id_mail_mail_id_recipients',
        unique_items=True,
    )
    subject: Optional[str] = Field(
        None,
        description='Mail subject',
        title='get_characters_character_id_mail_mail_id_subject',
    )
    timestamp: Optional[datetime] = Field(
        None,
        description='When the mail was sent',
        title='get_characters_character_id_mail_mail_id_timestamp',
    )


class Headers200_get_characters_character_id_mail_mail_id(ModelBaseEVECelery):
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


class Response200_get_characters_character_id_mail_mail_id(ModelCachedResponse):
    """
    Contents of a mail

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        {
          "body": "blah blah blah",
          "from": 90000001,
          "labels": [
            2,
            32
          ],
          "read": true,
          "subject": "test",
          "timestamp": "2015-09-30T16:07:00Z"
        }

    """

    headers: Headers200_get_characters_character_id_mail_mail_id = Field(
        ..., description='The response headers for this request.'
    )
    body: GetCharactersCharacterIdMailMailIdOk = Field(
        ..., description='The response body for this request.'
    )
