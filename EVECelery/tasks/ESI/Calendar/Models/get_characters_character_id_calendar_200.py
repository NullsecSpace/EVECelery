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


class GetCharactersCharacterIdCalendarOkItem(BaseModel):
    event_date: Optional[datetime] = Field(
        None,
        description='event_date string',
        title='get_characters_character_id_calendar_event_date',
    )
    event_id: Optional[int] = Field(
        None,
        description='event_id integer',
        title='get_characters_character_id_calendar_event_id',
    )
    event_response: Optional[
        Literal['declined', 'not_responded', 'accepted', 'tentative']
    ] = Field(
        None,
        description='event_response string',
        title='get_characters_character_id_calendar_event_response',
    )
    importance: Optional[int] = Field(
        None,
        description='importance integer',
        title='get_characters_character_id_calendar_importance',
    )
    title: Optional[str] = Field(
        None,
        description='title string',
        title='get_characters_character_id_calendar_title',
    )


class GetCharactersCharacterIdCalendarOk(BaseModel):
    __root__: List[GetCharactersCharacterIdCalendarOkItem] = Field(
        ...,
        description='Up to 50 events from now or the event you requested',
        max_items=50,
        title='get_characters_character_id_calendar_ok',
    )


class Headers200_get_characters_character_id_calendar(ModelBaseEVECelery):
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


class Response200_get_characters_character_id_calendar(ModelCachedResponse):
    """
    A collection of event summaries

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "event_date": "2016-06-26T20:00:00Z",
            "event_id": 1386435,
            "event_response": "accepted",
            "importance": 0,
            "title": "o7 The EVE Online Show"
          }
        ]

    """

    headers: Headers200_get_characters_character_id_calendar = Field(
        ..., description='The response headers for this request.'
    )
    body: GetCharactersCharacterIdCalendarOk = Field(
        ..., description='The response body for this request.'
    )
