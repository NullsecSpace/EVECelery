"""
A model definition module returned by an ESI task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Models.py'.
"""
from __future__ import annotations
from EVECelery.tasks.BaseTasks.Models.ModelsBase import ModelBaseEVECelery
from EVECelery.tasks.BaseTasks.Models.ModelsCached import ModelCachedResponse
from typing import List, Literal, Optional

from pydantic import BaseModel, Field, conint, constr


class Label(BaseModel):
    color: Optional[
        Literal[
            '#0000fe',
            '#006634',
            '#0099ff',
            '#00ff33',
            '#01ffff',
            '#349800',
            '#660066',
            '#666666',
            '#999999',
            '#99ffff',
            '#9a0000',
            '#ccff9a',
            '#e6e6e6',
            '#fe0000',
            '#ff6600',
            '#ffff01',
            '#ffffcd',
            '#ffffff',
        ]
    ] = Field(
        '#ffffff',
        description='color string',
        title='get_characters_character_id_mail_labels_color',
    )
    label_id: Optional[conint(ge=0)] = Field(
        None,
        description='label_id integer',
        title='get_characters_character_id_mail_labels_label_id',
    )
    name: Optional[constr(max_length=40)] = Field(
        None,
        description='name string',
        title='get_characters_character_id_mail_labels_name',
    )
    unread_count: Optional[conint(ge=0)] = Field(
        None,
        description='unread_count integer',
        title='get_characters_character_id_mail_labels_unread_count',
    )


class GetCharactersCharacterIdMailLabelsOk(BaseModel):
    labels: Optional[List[Label]] = Field(
        None,
        description='labels array',
        max_items=30,
        title='get_characters_character_id_mail_labels_labels',
    )
    total_unread_count: Optional[conint(ge=0)] = Field(
        None,
        description='total_unread_count integer',
        title='get_characters_character_id_mail_labels_total_unread_count',
    )


class Headers200_get_characters_character_id_mail_labels(ModelBaseEVECelery):
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


class Response200_get_characters_character_id_mail_labels(ModelCachedResponse):
    """
    A list of mail labels and unread counts

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        {
          "labels": [
            {
              "color": "#660066",
              "label_id": 16,
              "name": "PINK",
              "unread_count": 4
            },
            {
              "color": "#ffffff",
              "label_id": 17,
              "name": "WHITE",
              "unread_count": 1
            }
          ],
          "total_unread_count": 5
        }

    """

    headers: Headers200_get_characters_character_id_mail_labels = Field(
        ..., description='The response headers for this request.'
    )
    body: GetCharactersCharacterIdMailLabelsOk = Field(
        ..., description='The response body for this request.'
    )
