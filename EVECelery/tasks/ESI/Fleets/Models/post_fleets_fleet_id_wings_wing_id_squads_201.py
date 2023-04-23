"""
A model definition module returned by an ESI task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Models.py'.
"""
from __future__ import annotations
from EVECelery.tasks.BaseTasks.Models.ModelsBase import ModelBaseEVECelery
from EVECelery.tasks.BaseTasks.Models.ModelsCached import ModelCachedResponse
from pydantic import BaseModel, Field


class PostFleetsFleetIdWingsWingIdSquadsCreated(BaseModel):
    squad_id: int = Field(
        ...,
        description='The squad_id of the newly created squad',
        title='post_fleets_fleet_id_wings_wing_id_squads_squad_id',
    )


class Headers201_post_fleets_fleet_id_wings_wing_id_squads(ModelBaseEVECelery):
    """
    Headers for response code 201
    """

    pass


class Response201_post_fleets_fleet_id_wings_wing_id_squads(ModelCachedResponse):
    """
    Squad created

    Response for code 201. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        {
          "squad_id": 123
        }

    """

    headers: Headers201_post_fleets_fleet_id_wings_wing_id_squads = Field(
        ..., description='The response headers for this request.'
    )
    body: PostFleetsFleetIdWingsWingIdSquadsCreated = Field(
        ..., description='The response body for this request.'
    )
