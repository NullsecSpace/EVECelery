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

from pydantic import BaseModel, Field


class Aggressor(BaseModel):
    alliance_id: Optional[int] = Field(
        None,
        description='Alliance ID if and only if the aggressor is an alliance',
        title='get_wars_war_id_alliance_id',
    )
    corporation_id: Optional[int] = Field(
        None,
        description='Corporation ID if and only if the aggressor is a corporation',
        title='get_wars_war_id_corporation_id',
    )
    isk_destroyed: float = Field(
        ...,
        description='ISK value of ships the aggressor has destroyed',
        title='get_wars_war_id_isk_destroyed',
    )
    ships_killed: int = Field(
        ...,
        description='The number of ships the aggressor has killed',
        title='get_wars_war_id_ships_killed',
    )


class Allie(BaseModel):
    alliance_id: Optional[int] = Field(
        None,
        description='Alliance ID if and only if this ally is an alliance',
        title='get_wars_war_id_ally_alliance_id',
    )
    corporation_id: Optional[int] = Field(
        None,
        description='Corporation ID if and only if this ally is a corporation',
        title='get_wars_war_id_ally_corporation_id',
    )


class Defender(BaseModel):
    alliance_id: Optional[int] = Field(
        None,
        description='Alliance ID if and only if the defender is an alliance',
        title='get_wars_war_id_defender_alliance_id',
    )
    corporation_id: Optional[int] = Field(
        None,
        description='Corporation ID if and only if the defender is a corporation',
        title='get_wars_war_id_defender_corporation_id',
    )
    isk_destroyed: float = Field(
        ...,
        description='ISK value of ships the defender has killed',
        title='get_wars_war_id_defender_isk_destroyed',
    )
    ships_killed: int = Field(
        ...,
        description='The number of ships the defender has killed',
        title='get_wars_war_id_defender_ships_killed',
    )


class GetWarsWarIdOk(BaseModel):
    aggressor: Aggressor = Field(
        ...,
        description='The aggressor corporation or alliance that declared this war, only contains either corporation_id or alliance_id',
        title='get_wars_war_id_aggressor',
    )
    allies: Optional[List[Allie]] = Field(
        None,
        description='allied corporations or alliances, each object contains either corporation_id or alliance_id',
        max_items=10000,
        title='get_wars_war_id_allies',
    )
    declared: datetime = Field(
        ...,
        description='Time that the war was declared',
        title='get_wars_war_id_declared',
    )
    defender: Defender = Field(
        ...,
        description='The defending corporation or alliance that declared this war, only contains either corporation_id or alliance_id',
        title='get_wars_war_id_defender',
    )
    finished: Optional[datetime] = Field(
        None,
        description='Time the war ended and shooting was no longer allowed',
        title='get_wars_war_id_finished',
    )
    id: int = Field(
        ..., description='ID of the specified war', title='get_wars_war_id_id'
    )
    mutual: bool = Field(
        ...,
        description='Was the war declared mutual by both parties',
        title='get_wars_war_id_mutual',
    )
    open_for_allies: bool = Field(
        ...,
        description='Is the war currently open for allies or not',
        title='get_wars_war_id_open_for_allies',
    )
    retracted: Optional[datetime] = Field(
        None,
        description='Time the war was retracted but both sides could still shoot each other',
        title='get_wars_war_id_retracted',
    )
    started: Optional[datetime] = Field(
        None,
        description='Time when the war started and both sides could shoot each other',
        title='get_wars_war_id_started',
    )


class Headers200_get_wars_war_id(ModelBaseEVECelery):
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


class Response200_get_wars_war_id(ModelCachedResponse):
    """
    Details about a war

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        {
          "aggressor": {
            "corporation_id": 986665792,
            "isk_destroyed": 0,
            "ships_killed": 0
          },
          "declared": "2004-05-22T05:20:00Z",
          "defender": {
            "corporation_id": 1001562011,
            "isk_destroyed": 0,
            "ships_killed": 0
          },
          "id": 1941,
          "mutual": false,
          "open_for_allies": false
        }

    """

    headers: Headers200_get_wars_war_id = Field(
        ..., description='The response headers for this request.'
    )
    body: GetWarsWarIdOk = Field(..., description='The response body for this request.')
