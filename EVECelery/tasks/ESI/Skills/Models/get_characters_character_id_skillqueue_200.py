"""
A model definition module returned by an ESI task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Models.py'.
"""
from __future__ import annotations
from EVECelery.tasks.BaseTasks.Models.ModelsBase import ModelBaseEVECelery
from EVECelery.tasks.BaseTasks.Models.ModelsCached import ModelCachedResponse
from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field, conint


class GetCharactersCharacterIdSkillqueueOkItem(BaseModel):
    finish_date: Optional[datetime] = Field(
        None,
        description='Date on which training of the skill will complete. Omitted if the skill queue is paused.',
        title='get_characters_character_id_skillqueue_finish_date',
    )
    finished_level: conint(ge=0, le=5) = Field(
        ...,
        description='finished_level integer',
        title='get_characters_character_id_skillqueue_finished_level',
    )
    level_end_sp: Optional[int] = Field(
        None,
        description='level_end_sp integer',
        title='get_characters_character_id_skillqueue_level_end_sp',
    )
    level_start_sp: Optional[int] = Field(
        None,
        description="Amount of SP that was in the skill when it started training it's current level. Used to calculate % of current level complete.",
        title='get_characters_character_id_skillqueue_level_start_sp',
    )
    queue_position: int = Field(
        ...,
        description='queue_position integer',
        title='get_characters_character_id_skillqueue_queue_position',
    )
    skill_id: int = Field(
        ...,
        description='skill_id integer',
        title='get_characters_character_id_skillqueue_skill_id',
    )
    start_date: Optional[datetime] = Field(
        None,
        description='start_date string',
        title='get_characters_character_id_skillqueue_start_date',
    )
    training_start_sp: Optional[int] = Field(
        None,
        description='training_start_sp integer',
        title='get_characters_character_id_skillqueue_training_start_sp',
    )


class GetCharactersCharacterIdSkillqueueOk(BaseModel):
    __root__: List[GetCharactersCharacterIdSkillqueueOkItem] = Field(
        ...,
        description='200 ok array',
        max_items=150,
        title='get_characters_character_id_skillqueue_ok',
    )


class Headers200_get_characters_character_id_skillqueue(ModelBaseEVECelery):
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


class Response200_get_characters_character_id_skillqueue(ModelCachedResponse):
    """
    The current skill queue, sorted ascending by finishing time

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "finish_date": "2016-06-29T10:47:00Z",
            "finished_level": 3,
            "queue_position": 0,
            "skill_id": 1,
            "start_date": "2016-06-29T10:46:00Z"
          },
          {
            "finish_date": "2016-07-15T10:47:00Z",
            "finished_level": 4,
            "queue_position": 1,
            "skill_id": 1,
            "start_date": "2016-06-29T10:47:00Z"
          },
          {
            "finish_date": "2016-08-30T10:47:00Z",
            "finished_level": 2,
            "queue_position": 2,
            "skill_id": 2,
            "start_date": "2016-07-15T10:47:00Z"
          }
        ]

    """

    headers: Headers200_get_characters_character_id_skillqueue = Field(
        ..., description='The response headers for this request.'
    )
    body: GetCharactersCharacterIdSkillqueueOk = Field(
        ..., description='The response body for this request.'
    )
