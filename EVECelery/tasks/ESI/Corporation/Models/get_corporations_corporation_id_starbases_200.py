"""
A model definition module returned by an ESI task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Models.py'.
"""
from __future__ import annotations
from EVECelery.tasks.BaseTasks.Models.ModelsBase import ModelBaseEVECelery
from EVECelery.tasks.BaseTasks.Models.ModelsCached import ModelCachedResponse
from datetime import datetime
from typing import List, Literal, Optional

from pydantic import BaseModel, Field


class GetCorporationsCorporationIdStarbasesOkItem(BaseModel):
    moon_id: Optional[int] = Field(
        None,
        description='The moon this starbase (POS) is anchored on, unanchored POSes do not have this information',
        title='get_corporations_corporation_id_starbases_moon_id',
    )
    onlined_since: Optional[datetime] = Field(
        None,
        description='When the POS onlined, for starbases (POSes) in online state',
        title='get_corporations_corporation_id_starbases_onlined_since',
    )
    reinforced_until: Optional[datetime] = Field(
        None,
        description='When the POS will be out of reinforcement, for starbases (POSes) in reinforced state',
        title='get_corporations_corporation_id_starbases_reinforced_until',
    )
    starbase_id: int = Field(
        ...,
        description='Unique ID for this starbase (POS)',
        title='get_corporations_corporation_id_starbases_starbase_id',
    )
    state: Optional[
        Literal['offline', 'online', 'onlining', 'reinforced', 'unanchoring']
    ] = Field(
        None,
        description='state string',
        title='get_corporations_corporation_id_starbases_state',
    )
    system_id: int = Field(
        ...,
        description='The solar system this starbase (POS) is in, unanchored POSes have this information',
        title='get_corporations_corporation_id_starbases_system_id',
    )
    type_id: int = Field(
        ...,
        description='Starbase (POS) type',
        title='get_corporations_corporation_id_starbases_type_id',
    )
    unanchor_at: Optional[datetime] = Field(
        None,
        description='When the POS started unanchoring, for starbases (POSes) in unanchoring state',
        title='get_corporations_corporation_id_starbases_unanchor_at',
    )


class GetCorporationsCorporationIdStarbasesOk(BaseModel):
    __root__: List[GetCorporationsCorporationIdStarbasesOkItem] = Field(
        ...,
        description='200 ok array',
        max_items=1000,
        title='get_corporations_corporation_id_starbases_ok',
    )


class Headers200_get_corporations_corporation_id_starbases(ModelBaseEVECelery):
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


class Response200_get_corporations_corporation_id_starbases(ModelCachedResponse):
    """
    List of starbases (POSes)

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "starbase_id": 12345,
            "system_id": 123456,
            "type_id": 456
          }
        ]

    """

    headers: Headers200_get_corporations_corporation_id_starbases = Field(
        ..., description='The response headers for this request.'
    )
    body: GetCorporationsCorporationIdStarbasesOk = Field(
        ..., description='The response body for this request.'
    )
