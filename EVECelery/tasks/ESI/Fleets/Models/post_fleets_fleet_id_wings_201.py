"""
A model definition module returned by an ESI task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Models.py'.
"""
from __future__ import annotations
from EVECelery.tasks.BaseTasks.Models.ModelsBase import ModelBaseEVECelery
from EVECelery.tasks.BaseTasks.Models.ModelsCached import ModelCachedResponse
from pydantic import BaseModel, Field


class PostFleetsFleetIdWingsCreated(BaseModel):
    wing_id: int = Field(
        ...,
        description='The wing_id of the newly created wing',
        title='post_fleets_fleet_id_wings_wing_id',
    )


class Headers201_post_fleets_fleet_id_wings(ModelBaseEVECelery):
    """
    Headers for response code 201
    """

    pass


class Response201_post_fleets_fleet_id_wings(ModelCachedResponse):
    """
    Wing created

    Response for code 201. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        {
          "wing_id": 123
        }

    """

    headers: Headers201_post_fleets_fleet_id_wings = Field(
        ..., description='The response headers for this request.'
    )
    body: PostFleetsFleetIdWingsCreated = Field(
        ..., description='The response body for this request.'
    )
