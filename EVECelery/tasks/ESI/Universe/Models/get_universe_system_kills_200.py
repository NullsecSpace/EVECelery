"""
A model definition module returned by an ESI task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Models.py'.
"""
from __future__ import annotations
from EVECelery.tasks.BaseTasks.Models.ModelsBase import ModelBaseEVECelery
from EVECelery.tasks.BaseTasks.Models.ModelsCached import ModelCachedResponse
from typing import List

from pydantic import BaseModel, Field


class GetUniverseSystemKillsOkItem(BaseModel):
    npc_kills: int = Field(
        ...,
        description='Number of NPC ships killed in this system',
        title='get_universe_system_kills_npc_kills',
    )
    pod_kills: int = Field(
        ...,
        description='Number of pods killed in this system',
        title='get_universe_system_kills_pod_kills',
    )
    ship_kills: int = Field(
        ...,
        description='Number of player ships killed in this system',
        title='get_universe_system_kills_ship_kills',
    )
    system_id: int = Field(
        ...,
        description='system_id integer',
        title='get_universe_system_kills_system_id',
    )


class GetUniverseSystemKillsOk(BaseModel):
    __root__: List[GetUniverseSystemKillsOkItem] = Field(
        ...,
        description='200 ok array',
        max_items=10000,
        title='get_universe_system_kills_ok',
    )


class Headers200_get_universe_system_kills(ModelBaseEVECelery):
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


class Response200_get_universe_system_kills(ModelCachedResponse):
    """
    A list of systems and number of ship, pod and NPC kills

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "npc_kills": 0,
            "pod_kills": 24,
            "ship_kills": 42,
            "system_id": 30002410
          }
        ]

    """

    headers: Headers200_get_universe_system_kills = Field(
        ..., description='The response headers for this request.'
    )
    body: GetUniverseSystemKillsOk = Field(
        ..., description='The response body for this request.'
    )
