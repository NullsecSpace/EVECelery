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


class GetUniverseBloodlinesOkItem(BaseModel):
    bloodline_id: int = Field(
        ...,
        description='bloodline_id integer',
        title='get_universe_bloodlines_bloodline_id',
    )
    charisma: int = Field(
        ..., description='charisma integer', title='get_universe_bloodlines_charisma'
    )
    corporation_id: int = Field(
        ...,
        description='corporation_id integer',
        title='get_universe_bloodlines_corporation_id',
    )
    description: str = Field(
        ...,
        description='description string',
        title='get_universe_bloodlines_description',
    )
    intelligence: int = Field(
        ...,
        description='intelligence integer',
        title='get_universe_bloodlines_intelligence',
    )
    memory: int = Field(
        ..., description='memory integer', title='get_universe_bloodlines_memory'
    )
    name: str = Field(
        ..., description='name string', title='get_universe_bloodlines_name'
    )
    perception: int = Field(
        ...,
        description='perception integer',
        title='get_universe_bloodlines_perception',
    )
    race_id: int = Field(
        ..., description='race_id integer', title='get_universe_bloodlines_race_id'
    )
    ship_type_id: int = Field(
        ...,
        description='ship_type_id integer',
        title='get_universe_bloodlines_ship_type_id',
    )
    willpower: int = Field(
        ..., description='willpower integer', title='get_universe_bloodlines_willpower'
    )


class GetUniverseBloodlinesOk(BaseModel):
    __root__: List[GetUniverseBloodlinesOkItem] = Field(
        ...,
        description='200 ok array',
        max_items=100,
        title='get_universe_bloodlines_ok',
    )


class Headers200_get_universe_bloodlines(ModelBaseEVECelery):
    """
    Headers for response code 200
    """

    Cache_Control: str | None = Field(
        description="The caching mechanism used", alias="Cache-Control"
    )
    Content_Language: str | None = Field(
        description="The language used in the response", alias="Content-Language"
    )
    ETag: str | None = Field(description="RFC7232 compliant entity tag")
    Expires: str | None = Field(description="RFC7231 formatted datetime string")
    Last_Modified: str | None = Field(
        description="RFC7231 formatted datetime string", alias="Last-Modified"
    )


class Response200_get_universe_bloodlines(ModelCachedResponse):
    """
    A list of bloodlines

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "bloodline_id": 1,
            "charisma": 6,
            "corporation_id": 1000006,
            "description": "The Deteis are regarded as ...",
            "intelligence": 7,
            "memory": 7,
            "name": "Deteis",
            "perception": 5,
            "race_id": 1,
            "ship_type_id": 601,
            "willpower": 5
          }
        ]

    """

    headers: Headers200_get_universe_bloodlines = Field(
        ..., description='The response headers for this request.'
    )
    body: GetUniverseBloodlinesOk = Field(
        ..., description='The response body for this request.'
    )
