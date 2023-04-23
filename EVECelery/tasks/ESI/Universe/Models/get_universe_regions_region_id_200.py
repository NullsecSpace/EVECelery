"""
A model definition module returned by an ESI task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Models.py'.
"""
from __future__ import annotations
from EVECelery.tasks.BaseTasks.Models.ModelsBase import ModelBaseEVECelery
from EVECelery.tasks.BaseTasks.Models.ModelsCached import ModelCachedResponse
from typing import List, Optional

from pydantic import BaseModel, Field


class GetUniverseRegionsRegionIdOk(BaseModel):
    constellations: List[int] = Field(
        ...,
        description='constellations array',
        max_items=1000,
        title='get_universe_regions_region_id_constellations',
    )
    description: Optional[str] = Field(
        None,
        description='description string',
        title='get_universe_regions_region_id_description',
    )
    name: str = Field(
        ..., description='name string', title='get_universe_regions_region_id_name'
    )
    region_id: int = Field(
        ...,
        description='region_id integer',
        title='get_universe_regions_region_id_region_id',
    )


class Headers200_get_universe_regions_region_id(ModelBaseEVECelery):
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


class Response200_get_universe_regions_region_id(ModelCachedResponse):
    """
    Information about a region

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        {
          "constellations": [
            20000302,
            20000303
          ],
          "description": "It has long been an established fact of civilization...",
          "name": "Metropolis",
          "region_id": 10000042
        }

    """

    headers: Headers200_get_universe_regions_region_id = Field(
        ..., description='The response headers for this request.'
    )
    body: GetUniverseRegionsRegionIdOk = Field(
        ..., description='The response body for this request.'
    )
