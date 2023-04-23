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


class GetCorporationsCorporationIdStandingsOkItem(BaseModel):
    from_id: int = Field(
        ...,
        description='from_id integer',
        title='get_corporations_corporation_id_standings_from_id',
    )
    from_type: Literal['agent', 'npc_corp', 'faction'] = Field(
        ...,
        description='from_type string',
        title='get_corporations_corporation_id_standings_from_type',
    )
    standing: float = Field(
        ...,
        description='standing number',
        title='get_corporations_corporation_id_standings_standing',
    )


class GetCorporationsCorporationIdStandingsOk(BaseModel):
    __root__: List[GetCorporationsCorporationIdStandingsOkItem] = Field(
        ...,
        description='200 ok array',
        max_items=1000,
        title='get_corporations_corporation_id_standings_ok',
    )


class Headers200_get_corporations_corporation_id_standings(ModelBaseEVECelery):
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
    X_Pages: int | None = Field(description="Maximum page number", alias="X-Pages")


class Response200_get_corporations_corporation_id_standings(ModelCachedResponse):
    """
    A list of standings

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "from_id": 3009841,
            "from_type": "agent",
            "standing": 0.1
          },
          {
            "from_id": 1000061,
            "from_type": "npc_corp",
            "standing": 0
          },
          {
            "from_id": 500003,
            "from_type": "faction",
            "standing": -1
          }
        ]

    """

    headers: Headers200_get_corporations_corporation_id_standings = Field(
        ..., description='The response headers for this request.'
    )
    body: GetCorporationsCorporationIdStandingsOk = Field(
        ..., description='The response body for this request.'
    )
