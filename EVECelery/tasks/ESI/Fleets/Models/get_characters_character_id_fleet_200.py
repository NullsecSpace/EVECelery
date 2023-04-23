"""
A model definition module returned by an ESI task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Models.py'.
"""
from __future__ import annotations
from EVECelery.tasks.BaseTasks.Models.ModelsBase import ModelBaseEVECelery
from EVECelery.tasks.BaseTasks.Models.ModelsCached import ModelCachedResponse
from typing import Literal

from pydantic import BaseModel, Field


class GetCharactersCharacterIdFleetOk(BaseModel):
    fleet_id: int = Field(
        ...,
        description="The character's current fleet ID",
        title='get_characters_character_id_fleet_fleet_id',
    )
    role: Literal[
        'fleet_commander', 'squad_commander', 'squad_member', 'wing_commander'
    ] = Field(
        ...,
        description='Member’s role in fleet',
        title='get_characters_character_id_fleet_role',
    )
    squad_id: int = Field(
        ...,
        description='ID of the squad the member is in. If not applicable, will be set to -1',
        title='get_characters_character_id_fleet_squad_id',
    )
    wing_id: int = Field(
        ...,
        description='ID of the wing the member is in. If not applicable, will be set to -1',
        title='get_characters_character_id_fleet_wing_id',
    )


class Headers200_get_characters_character_id_fleet(ModelBaseEVECelery):
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


class Response200_get_characters_character_id_fleet(ModelCachedResponse):
    """
    Details about the character's fleet

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        {
          "fleet_id": 1234567890,
          "role": "fleet_commander",
          "squad_id": -1,
          "wing_id": -1
        }

    """

    headers: Headers200_get_characters_character_id_fleet = Field(
        ..., description='The response headers for this request.'
    )
    body: GetCharactersCharacterIdFleetOk = Field(
        ..., description='The response body for this request.'
    )
