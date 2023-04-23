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


class GetUniverseGraphicsGraphicIdOk(BaseModel):
    collision_file: Optional[str] = Field(
        None,
        description='collision_file string',
        title='get_universe_graphics_graphic_id_collision_file',
    )
    graphic_file: Optional[str] = Field(
        None,
        description='graphic_file string',
        title='get_universe_graphics_graphic_id_graphic_file',
    )
    graphic_id: int = Field(
        ...,
        description='graphic_id integer',
        title='get_universe_graphics_graphic_id_graphic_id',
    )
    icon_folder: Optional[str] = Field(
        None,
        description='icon_folder string',
        title='get_universe_graphics_graphic_id_icon_folder',
    )
    sof_dna: Optional[str] = Field(
        None,
        description='sof_dna string',
        title='get_universe_graphics_graphic_id_sof_dna',
    )
    sof_fation_name: Optional[str] = Field(
        None,
        description='sof_fation_name string',
        title='get_universe_graphics_graphic_id_sof_fation_name',
    )
    sof_hull_name: Optional[str] = Field(
        None,
        description='sof_hull_name string',
        title='get_universe_graphics_graphic_id_sof_hull_name',
    )
    sof_race_name: Optional[str] = Field(
        None,
        description='sof_race_name string',
        title='get_universe_graphics_graphic_id_sof_race_name',
    )


class Headers200_get_universe_graphics_graphic_id(ModelBaseEVECelery):
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


class Response200_get_universe_graphics_graphic_id(ModelCachedResponse):
    """
    Information about a graphic

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        {
          "graphic_file": "res:/dx9/model/worldobject/planet/moon.red",
          "graphic_id": 10
        }

    """

    headers: Headers200_get_universe_graphics_graphic_id = Field(
        ..., description='The response headers for this request.'
    )
    body: GetUniverseGraphicsGraphicIdOk = Field(
        ..., description='The response body for this request.'
    )
