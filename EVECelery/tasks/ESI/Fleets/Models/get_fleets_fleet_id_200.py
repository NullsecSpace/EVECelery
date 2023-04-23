"""
A model definition module returned by an ESI task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Models.py'.
"""
from __future__ import annotations
from EVECelery.tasks.BaseTasks.Models.ModelsBase import ModelBaseEVECelery
from EVECelery.tasks.BaseTasks.Models.ModelsCached import ModelCachedResponse
from pydantic import BaseModel, Field


class GetFleetsFleetIdOk(BaseModel):
    is_free_move: bool = Field(
        ...,
        description='Is free-move enabled',
        title='get_fleets_fleet_id_is_free_move',
    )
    is_registered: bool = Field(
        ...,
        description='Does the fleet have an active fleet advertisement',
        title='get_fleets_fleet_id_is_registered',
    )
    is_voice_enabled: bool = Field(
        ...,
        description='Is EVE Voice enabled',
        title='get_fleets_fleet_id_is_voice_enabled',
    )
    motd: str = Field(
        ...,
        description='Fleet MOTD in CCP flavoured HTML',
        title='get_fleets_fleet_id_motd',
    )


class Headers200_get_fleets_fleet_id(ModelBaseEVECelery):
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


class Response200_get_fleets_fleet_id(ModelCachedResponse):
    """
    Details about a fleet

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        {
          "is_free_move": false,
          "is_registered": false,
          "is_voice_enabled": false,
          "motd": "This is an <b>awesome</b> fleet!"
        }

    """

    headers: Headers200_get_fleets_fleet_id = Field(
        ..., description='The response headers for this request.'
    )
    body: GetFleetsFleetIdOk = Field(
        ..., description='The response body for this request.'
    )
