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


class GetCorporationCorporationIdMiningExtractionsOkItem(BaseModel):
    chunk_arrival_time: datetime = Field(
        ...,
        description='The time at which the chunk being extracted will arrive and can be fractured by the moon mining drill.\n',
        title='get_corporation_corporation_id_mining_extractions_chunk_arrival_time',
    )
    extraction_start_time: datetime = Field(
        ...,
        description='The time at which the current extraction was initiated.\n',
        title='get_corporation_corporation_id_mining_extractions_extraction_start_time',
    )
    moon_id: int = Field(
        ...,
        description='moon_id integer',
        title='get_corporation_corporation_id_mining_extractions_moon_id',
    )
    natural_decay_time: datetime = Field(
        ...,
        description='The time at which the chunk being extracted will naturally fracture if it is not first fractured by the moon mining drill.\n',
        title='get_corporation_corporation_id_mining_extractions_natural_decay_time',
    )
    structure_id: int = Field(
        ...,
        description='structure_id integer',
        title='get_corporation_corporation_id_mining_extractions_structure_id',
    )


class GetCorporationCorporationIdMiningExtractionsOk(BaseModel):
    __root__: List[GetCorporationCorporationIdMiningExtractionsOkItem] = Field(
        ...,
        description='200 ok array',
        max_items=1000,
        title='get_corporation_corporation_id_mining_extractions_ok',
    )


class Headers200_get_corporation_corporation_id_mining_extractions(ModelBaseEVECelery):
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


class Response200_get_corporation_corporation_id_mining_extractions(
    ModelCachedResponse
):
    """
    A list of chunk timers

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "chunk_arrival_time": "2017-10-17T11:00:59Z",
            "extraction_start_time": "2017-10-11T10:37:04Z",
            "moon_id": 40307229,
            "natural_decay_time": "2017-10-17T14:00:59Z",
            "structure_id": 1000000010579
          }
        ]

    """

    headers: Headers200_get_corporation_corporation_id_mining_extractions = Field(
        ..., description='The response headers for this request.'
    )
    body: GetCorporationCorporationIdMiningExtractionsOk = Field(
        ..., description='The response body for this request.'
    )
