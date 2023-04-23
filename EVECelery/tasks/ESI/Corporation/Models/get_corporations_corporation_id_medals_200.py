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

from pydantic import BaseModel, Field, constr


class GetCorporationsCorporationIdMedalsOkItem(BaseModel):
    created_at: datetime = Field(
        ...,
        description='created_at string',
        title='get_corporations_corporation_id_medals_created_at',
    )
    creator_id: int = Field(
        ...,
        description='ID of the character who created this medal',
        title='get_corporations_corporation_id_medals_creator_id',
    )
    description: constr(max_length=1000) = Field(
        ...,
        description='description string',
        title='get_corporations_corporation_id_medals_description',
    )
    medal_id: int = Field(
        ...,
        description='medal_id integer',
        title='get_corporations_corporation_id_medals_medal_id',
    )
    title: constr(max_length=100) = Field(
        ...,
        description='title string',
        title='get_corporations_corporation_id_medals_title',
    )


class GetCorporationsCorporationIdMedalsOk(BaseModel):
    __root__: List[GetCorporationsCorporationIdMedalsOkItem] = Field(
        ...,
        description='200 ok array',
        max_items=1000,
        title='get_corporations_corporation_id_medals_ok',
    )


class Headers200_get_corporations_corporation_id_medals(ModelBaseEVECelery):
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


class Response200_get_corporations_corporation_id_medals(ModelCachedResponse):
    """
    A list of medals

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "created_at": "2017-10-10T14:00:00Z",
            "creator_id": 46578,
            "description": "An Awesome Medal",
            "medal_id": 123,
            "title": "Awesome Medal"
          }
        ]

    """

    headers: Headers200_get_corporations_corporation_id_medals = Field(
        ..., description='The response headers for this request.'
    )
    body: GetCorporationsCorporationIdMedalsOk = Field(
        ..., description='The response body for this request.'
    )
