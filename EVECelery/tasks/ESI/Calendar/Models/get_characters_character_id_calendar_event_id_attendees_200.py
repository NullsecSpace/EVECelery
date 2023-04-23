"""
A model definition module returned by an ESI task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Models.py'.
"""
from __future__ import annotations
from EVECelery.tasks.BaseTasks.Models.ModelsBase import ModelBaseEVECelery
from EVECelery.tasks.BaseTasks.Models.ModelsCached import ModelCachedResponse
from typing import List, Literal, Optional

from pydantic import BaseModel, Field


class GetCharactersCharacterIdCalendarEventIdAttendeesOkItem(BaseModel):
    character_id: Optional[int] = Field(
        None,
        description='character_id integer',
        title='get_characters_character_id_calendar_event_id_attendees_character_id',
    )
    event_response: Optional[
        Literal['declined', 'not_responded', 'accepted', 'tentative']
    ] = Field(
        None,
        description='event_response string',
        title='get_characters_character_id_calendar_event_id_attendees_event_response',
    )


class GetCharactersCharacterIdCalendarEventIdAttendeesOk(BaseModel):
    __root__: List[GetCharactersCharacterIdCalendarEventIdAttendeesOkItem] = Field(
        ...,
        description='List of attendees for a given event',
        max_items=100,
        title='get_characters_character_id_calendar_event_id_attendees_ok',
    )


class Headers200_get_characters_character_id_calendar_event_id_attendees(
    ModelBaseEVECelery
):
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


class Response200_get_characters_character_id_calendar_event_id_attendees(
    ModelCachedResponse
):
    """
    List of attendees

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "character_id": 2112625428,
            "event_response": "accepted"
          },
          {
            "character_id": 95465499,
            "event_response": "tentative"
          }
        ]

    """

    headers: Headers200_get_characters_character_id_calendar_event_id_attendees = Field(
        ..., description='The response headers for this request.'
    )
    body: GetCharactersCharacterIdCalendarEventIdAttendeesOk = Field(
        ..., description='The response body for this request.'
    )
