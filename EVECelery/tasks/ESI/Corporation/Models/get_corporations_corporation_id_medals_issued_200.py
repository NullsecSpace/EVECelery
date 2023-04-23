"""
A model definition module returned by an ESI task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Models.py'.
"""
from __future__ import annotations
from EVECelery.tasks.BaseTasks.Models.ModelsBase import ModelBaseEVECelery
from EVECelery.tasks.BaseTasks.Models.ModelsCached import ModelCachedResponse
from datetime import datetime
from typing import List, Literal

from pydantic import BaseModel, Field, constr


class GetCorporationsCorporationIdMedalsIssuedOkItem(BaseModel):
    character_id: int = Field(
        ...,
        description='ID of the character who was rewarded this medal',
        title='get_corporations_corporation_id_medals_issued_character_id',
    )
    issued_at: datetime = Field(
        ...,
        description='issued_at string',
        title='get_corporations_corporation_id_medals_issued_issued_at',
    )
    issuer_id: int = Field(
        ...,
        description='ID of the character who issued the medal',
        title='get_corporations_corporation_id_medals_issued_issuer_id',
    )
    medal_id: int = Field(
        ...,
        description='medal_id integer',
        title='get_corporations_corporation_id_medals_issued_medal_id',
    )
    reason: constr(max_length=1000) = Field(
        ...,
        description='reason string',
        title='get_corporations_corporation_id_medals_issued_reason',
    )
    status: Literal['private', 'public'] = Field(
        ...,
        description='status string',
        title='get_corporations_corporation_id_medals_issued_status',
    )


class GetCorporationsCorporationIdMedalsIssuedOk(BaseModel):
    __root__: List[GetCorporationsCorporationIdMedalsIssuedOkItem] = Field(
        ...,
        description='200 ok array',
        max_items=1000,
        title='get_corporations_corporation_id_medals_issued_ok',
    )


class Headers200_get_corporations_corporation_id_medals_issued(ModelBaseEVECelery):
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


class Response200_get_corporations_corporation_id_medals_issued(ModelCachedResponse):
    """
    A list of issued medals

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "character_id": 45678,
            "issued_at": "2017-10-10T14:00:00Z",
            "issuer_id": 67890,
            "medal_id": 123,
            "reason": "Awesome Reason",
            "status": "private"
          }
        ]

    """

    headers: Headers200_get_corporations_corporation_id_medals_issued = Field(
        ..., description='The response headers for this request.'
    )
    body: GetCorporationsCorporationIdMedalsIssuedOk = Field(
        ..., description='The response body for this request.'
    )
