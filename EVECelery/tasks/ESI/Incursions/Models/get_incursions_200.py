"""
A model definition module returned by an ESI task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Models.py'.
"""
from __future__ import annotations
from EVECelery.tasks.BaseTasks.Models.ModelsBase import ModelBaseEVECelery
from EVECelery.tasks.BaseTasks.Models.ModelsCached import ModelCachedResponse
from typing import List, Literal

from pydantic import BaseModel, Field


class GetIncursionsOkItem(BaseModel):
    constellation_id: int = Field(
        ...,
        description='The constellation id in which this incursion takes place',
        title='get_incursions_constellation_id',
    )
    faction_id: int = Field(
        ..., description="The attacking faction's id", title='get_incursions_faction_id'
    )
    has_boss: bool = Field(
        ...,
        description='Whether the final encounter has boss or not',
        title='get_incursions_has_boss',
    )
    infested_solar_systems: List[int] = Field(
        ...,
        description='A list of infested solar system ids that are a part of this incursion',
        max_items=100,
        title='get_incursions_infested_solar_systems',
    )
    influence: float = Field(
        ...,
        description='Influence of this incursion as a float from 0 to 1',
        title='get_incursions_influence',
    )
    staging_solar_system_id: int = Field(
        ...,
        description='Staging solar system for this incursion',
        title='get_incursions_staging_solar_system_id',
    )
    state: Literal['withdrawing', 'mobilizing', 'established'] = Field(
        ..., description='The state of this incursion', title='get_incursions_state'
    )
    type: str = Field(
        ..., description='The type of this incursion', title='get_incursions_type'
    )


class GetIncursionsOk(BaseModel):
    __root__: List[GetIncursionsOkItem] = Field(
        ..., description='200 ok array', max_items=100, title='get_incursions_ok'
    )


class Headers200_get_incursions(ModelBaseEVECelery):
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


class Response200_get_incursions(ModelCachedResponse):
    """
    A list of incursions

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "constellation_id": 20000607,
            "faction_id": 500019,
            "has_boss": true,
            "infested_solar_systems": [
              30004148,
              30004149,
              30004150,
              30004151,
              30004152,
              30004153,
              30004154
            ],
            "influence": 0.9,
            "staging_solar_system_id": 30004154,
            "state": "mobilizing",
            "type": "Incursion"
          }
        ]

    """

    headers: Headers200_get_incursions = Field(
        ..., description='The response headers for this request.'
    )
    body: GetIncursionsOk = Field(
        ..., description='The response body for this request.'
    )
