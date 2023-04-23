"""
A model definition module returned by an ESI task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Models.py'.
"""
from __future__ import annotations
from EVECelery.tasks.BaseTasks.Models.ModelsBase import ModelBaseEVECelery
from EVECelery.tasks.BaseTasks.Models.ModelsCached import ModelCachedResponse
from typing import Optional

from pydantic import BaseModel, Field


class GetAlliancesAllianceIdIconsOk(BaseModel):
    px128x128: Optional[str] = Field(
        None,
        description='px128x128 string',
        title='get_alliances_alliance_id_icons_px128x128',
    )
    px64x64: Optional[str] = Field(
        None,
        description='px64x64 string',
        title='get_alliances_alliance_id_icons_px64x64',
    )


class Headers200_get_alliances_alliance_id_icons(ModelBaseEVECelery):
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


class Response200_get_alliances_alliance_id_icons(ModelCachedResponse):
    """
    Icon URLs for the given alliance id and server

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        {
          "px128x128": "https://images.evetech.net/Alliance/503818424_128.png",
          "px64x64": "https://images.evetech.net/Alliance/503818424_64.png"
        }

    """

    headers: Headers200_get_alliances_alliance_id_icons = Field(
        ..., description='The response headers for this request.'
    )
    body: GetAlliancesAllianceIdIconsOk = Field(
        ..., description='The response body for this request.'
    )
