"""
A model definition module returned by an ESI task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Models.py'.
"""
from __future__ import annotations
from EVECelery.tasks.BaseTasks.Models.ModelsBase import ModelBaseEVECelery
from EVECelery.tasks.BaseTasks.Models.ModelsCached import ModelCachedResponse
from pydantic import BaseModel, Field


class GetUniverseSchematicsSchematicIdOk(BaseModel):
    cycle_time: int = Field(
        ...,
        description='Time in seconds to process a run',
        title='get_universe_schematics_schematic_id_cycle_time',
    )
    schematic_name: str = Field(
        ...,
        description='schematic_name string',
        title='get_universe_schematics_schematic_id_schematic_name',
    )


class Headers200_get_universe_schematics_schematic_id(ModelBaseEVECelery):
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


class Response200_get_universe_schematics_schematic_id(ModelCachedResponse):
    """
    Public data about a schematic

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        {
          "cycle_time": 1800,
          "schematic_name": "Bacteria"
        }

    """

    headers: Headers200_get_universe_schematics_schematic_id = Field(
        ..., description='The response headers for this request.'
    )
    body: GetUniverseSchematicsSchematicIdOk = Field(
        ..., description='The response body for this request.'
    )
