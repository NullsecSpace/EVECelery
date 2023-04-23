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


class GetCharactersCharacterIdAgentsResearchOkItem(BaseModel):
    agent_id: int = Field(
        ...,
        description='agent_id integer',
        title='get_characters_character_id_agents_research_agent_id',
    )
    points_per_day: float = Field(
        ...,
        description='points_per_day number',
        title='get_characters_character_id_agents_research_points_per_day',
    )
    remainder_points: float = Field(
        ...,
        description='remainder_points number',
        title='get_characters_character_id_agents_research_remainder_points',
    )
    skill_type_id: int = Field(
        ...,
        description='skill_type_id integer',
        title='get_characters_character_id_agents_research_skill_type_id',
    )
    started_at: datetime = Field(
        ...,
        description='started_at string',
        title='get_characters_character_id_agents_research_started_at',
    )


class GetCharactersCharacterIdAgentsResearchOk(BaseModel):
    __root__: List[GetCharactersCharacterIdAgentsResearchOkItem] = Field(
        ...,
        description='200 ok array',
        max_items=1000,
        title='get_characters_character_id_agents_research_ok',
    )


class Headers200_get_characters_character_id_agents_research(ModelBaseEVECelery):
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


class Response200_get_characters_character_id_agents_research(ModelCachedResponse):
    """
    A list of agents research information

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "agent_id": 3009358,
            "points_per_day": 53.5346162146776,
            "remainder_points": 53604.0634303189,
            "skill_type_id": 11450,
            "started_at": "2017-03-23T14:47:00Z"
          }
        ]

    """

    headers: Headers200_get_characters_character_id_agents_research = Field(
        ..., description='The response headers for this request.'
    )
    body: GetCharactersCharacterIdAgentsResearchOk = Field(
        ..., description='The response body for this request.'
    )
