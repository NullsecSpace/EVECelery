"""
A model definition module returned by an ESI task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Models.py'.
"""
from __future__ import annotations
from EVECelery.tasks.BaseTasks.Models.ModelsBase import ModelBaseEVECelery
from EVECelery.tasks.BaseTasks.Models.ModelsCached import ModelCachedResponse
from typing import List, Optional

from pydantic import BaseModel, Field


class Skill(BaseModel):
    active_skill_level: int = Field(
        ...,
        description='active_skill_level integer',
        title='get_characters_character_id_skills_active_skill_level',
    )
    skill_id: int = Field(
        ...,
        description='skill_id integer',
        title='get_characters_character_id_skills_skill_id',
    )
    skillpoints_in_skill: int = Field(
        ...,
        description='skillpoints_in_skill integer',
        title='get_characters_character_id_skills_skillpoints_in_skill',
    )
    trained_skill_level: int = Field(
        ...,
        description='trained_skill_level integer',
        title='get_characters_character_id_skills_trained_skill_level',
    )


class GetCharactersCharacterIdSkillsOk(BaseModel):
    skills: List[Skill] = Field(
        ...,
        description='skills array',
        max_items=1000,
        title='get_characters_character_id_skills_skills',
    )
    total_sp: int = Field(
        ...,
        description='total_sp integer',
        title='get_characters_character_id_skills_total_sp',
    )
    unallocated_sp: Optional[int] = Field(
        None,
        description='Skill points available to be assigned',
        title='get_characters_character_id_skills_unallocated_sp',
    )


class Headers200_get_characters_character_id_skills(ModelBaseEVECelery):
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


class Response200_get_characters_character_id_skills(ModelCachedResponse):
    """
    Known skills for the character

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        {
          "skills": [
            {
              "active_skill_level": 3,
              "skill_id": 1,
              "skillpoints_in_skill": 10000,
              "trained_skill_level": 4
            },
            {
              "active_skill_level": 1,
              "skill_id": 2,
              "skillpoints_in_skill": 10000,
              "trained_skill_level": 1
            }
          ],
          "total_sp": 20000
        }

    """

    headers: Headers200_get_characters_character_id_skills = Field(
        ..., description='The response headers for this request.'
    )
    body: GetCharactersCharacterIdSkillsOk = Field(
        ..., description='The response body for this request.'
    )
