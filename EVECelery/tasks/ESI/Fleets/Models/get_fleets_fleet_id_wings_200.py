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


class Squad(BaseModel):
    id: int = Field(
        ..., description='id integer', title='get_fleets_fleet_id_wings_squad_id'
    )
    name: str = Field(
        ..., description='name string', title='get_fleets_fleet_id_wings_squad_name'
    )


class GetFleetsFleetIdWingsOkItem(BaseModel):
    id: int = Field(..., description='id integer', title='get_fleets_fleet_id_wings_id')
    name: str = Field(
        ..., description='name string', title='get_fleets_fleet_id_wings_name'
    )
    squads: List[Squad] = Field(
        ...,
        description='squads array',
        max_items=25,
        title='get_fleets_fleet_id_wings_squads',
    )


class GetFleetsFleetIdWingsOk(BaseModel):
    __root__: List[GetFleetsFleetIdWingsOkItem] = Field(
        ...,
        description='200 ok array',
        max_items=25,
        title='get_fleets_fleet_id_wings_ok',
    )


class Headers200_get_fleets_fleet_id_wings(ModelBaseEVECelery):
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


class Response200_get_fleets_fleet_id_wings(ModelCachedResponse):
    """
    A list of fleet wings

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "id": 2073711261968,
            "name": "Wing 1",
            "squads": [
              {
                "id": 3129411261968,
                "name": "Squad 1"
              }
            ]
          }
        ]

    """

    headers: Headers200_get_fleets_fleet_id_wings = Field(
        ..., description='The response headers for this request.'
    )
    body: GetFleetsFleetIdWingsOk = Field(
        ..., description='The response body for this request.'
    )
