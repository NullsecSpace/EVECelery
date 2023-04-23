"""
A model definition module returned by an ESI task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Models.py'.
"""
from __future__ import annotations
from EVECelery.tasks.BaseTasks.Models.ModelsBase import ModelBaseEVECelery
from EVECelery.tasks.BaseTasks.Models.ModelsCached import ModelCachedResponse
from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field


class GetCharactersCharacterIdCalendarEventIdOk(BaseModel):
    date: datetime = Field(
        ...,
        description='date string',
        title='get_characters_character_id_calendar_event_id_date',
    )
    duration: int = Field(
        ...,
        description='Length in minutes',
        title='get_characters_character_id_calendar_event_id_duration',
    )
    event_id: int = Field(
        ...,
        description='event_id integer',
        title='get_characters_character_id_calendar_event_id_event_id',
    )
    importance: int = Field(
        ...,
        description='importance integer',
        title='get_characters_character_id_calendar_event_id_importance',
    )
    owner_id: int = Field(
        ...,
        description='owner_id integer',
        title='get_characters_character_id_calendar_event_id_owner_id',
    )
    owner_name: str = Field(
        ...,
        description='owner_name string',
        title='get_characters_character_id_calendar_event_id_owner_name',
    )
    owner_type: Literal[
        'eve_server', 'corporation', 'faction', 'character', 'alliance'
    ] = Field(
        ...,
        description='owner_type string',
        title='get_characters_character_id_calendar_event_id_owner_type',
    )
    response: str = Field(
        ...,
        description='response string',
        title='get_characters_character_id_calendar_event_id_response',
    )
    text: str = Field(
        ...,
        description='text string',
        title='get_characters_character_id_calendar_event_id_text',
    )
    title: str = Field(
        ...,
        description='title string',
        title='get_characters_character_id_calendar_event_id_title',
    )


class Headers200_get_characters_character_id_calendar_event_id(ModelBaseEVECelery):
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


class Response200_get_characters_character_id_calendar_event_id(ModelCachedResponse):
    """
    Full details of a specific event

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        {
          "date": "2016-06-26T21:00:00Z",
          "duration": 60,
          "event_id": 1386435,
          "importance": 1,
          "owner_id": 1,
          "owner_name": "EVE System",
          "owner_type": "eve_server",
          "response": "Undecided",
          "text": "o7: The EVE Online Show features latest developer news, fast paced action, community overviews and a lot more with CCP Guard and CCP Mimic. Join the thrilling o7 live broadcast at 20:00 EVE time (=UTC) on <a href=\"http://www.twitch.tv/ccp\">EVE TV</a>. Don't miss it!",
          "title": "o7 The EVE Online Show"
        }

    """

    headers: Headers200_get_characters_character_id_calendar_event_id = Field(
        ..., description='The response headers for this request.'
    )
    body: GetCharactersCharacterIdCalendarEventIdOk = Field(
        ..., description='The response body for this request.'
    )
