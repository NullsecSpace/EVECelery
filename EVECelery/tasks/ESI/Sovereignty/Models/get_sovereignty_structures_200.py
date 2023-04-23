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


class GetSovereigntyStructuresOkItem(BaseModel):
    alliance_id: int = Field(
        ...,
        description='The alliance that owns the structure.\n',
        title='get_sovereignty_structures_alliance_id',
    )
    solar_system_id: int = Field(
        ...,
        description='Solar system in which the structure is located.\n',
        title='get_sovereignty_structures_solar_system_id',
    )
    structure_id: int = Field(
        ...,
        description='Unique item ID for this structure.',
        title='get_sovereignty_structures_structure_id',
    )
    structure_type_id: int = Field(
        ...,
        description='A reference to the type of structure this is.\n',
        title='get_sovereignty_structures_structure_type_id',
    )
    vulnerability_occupancy_level: Optional[float] = Field(
        None,
        description='The occupancy level for the next or current vulnerability window. This takes into account all development indexes and capital system bonuses. Also known as Activity Defense Multiplier from in the client. It increases the time that attackers must spend using their entosis links on the structure.\n',
        title='get_sovereignty_structures_vulnerability_occupancy_level',
    )
    vulnerable_end_time: Optional[datetime] = Field(
        None,
        description="The time at which the next or current vulnerability window ends. At the end of a vulnerability window the next window is recalculated and locked in along with the vulnerabilityOccupancyLevel. If the structure is not in 100% entosis control of the defender, it will go in to 'overtime' and stay vulnerable for as long as that situation persists. Only once the defenders have 100% entosis control and has the vulnerableEndTime passed does the vulnerability interval expire and a new one is calculated.\n",
        title='get_sovereignty_structures_vulnerable_end_time',
    )
    vulnerable_start_time: Optional[datetime] = Field(
        None,
        description='The next time at which the structure will become vulnerable. Or the start time of the current window if current time is between this and vulnerableEndTime.\n',
        title='get_sovereignty_structures_vulnerable_start_time',
    )


class GetSovereigntyStructuresOk(BaseModel):
    __root__: List[GetSovereigntyStructuresOkItem] = Field(
        ...,
        description='200 ok array',
        max_items=10000,
        title='get_sovereignty_structures_ok',
    )


class Headers200_get_sovereignty_structures(ModelBaseEVECelery):
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


class Response200_get_sovereignty_structures(ModelCachedResponse):
    """
    A list of sovereignty structures

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "alliance_id": 498125261,
            "solar_system_id": 30000570,
            "structure_id": 1018253388776,
            "structure_type_id": 32226,
            "vulnerability_occupancy_level": 2,
            "vulnerable_end_time": "2016-10-29T05:30:00Z",
            "vulnerable_start_time": "2016-10-28T20:30:00Z"
          }
        ]

    """

    headers: Headers200_get_sovereignty_structures = Field(
        ..., description='The response headers for this request.'
    )
    body: GetSovereigntyStructuresOk = Field(
        ..., description='The response body for this request.'
    )
