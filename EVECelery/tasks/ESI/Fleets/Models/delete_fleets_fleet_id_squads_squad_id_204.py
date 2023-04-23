"""
A model definition module returned by an ESI task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Models.py'.
"""
from __future__ import annotations
from EVECelery.tasks.BaseTasks.Models.ModelsBase import ModelBaseEVECelery
from EVECelery.tasks.BaseTasks.Models.ModelsCached import ModelCachedResponse
from pydantic import Field


from typing import Any

from pydantic import BaseModel


class Model(BaseModel):
    __root__: Any


class Headers204_delete_fleets_fleet_id_squads_squad_id(ModelBaseEVECelery):
    """
    Headers for response code 204
    """

    pass


class Response204_delete_fleets_fleet_id_squads_squad_id(ModelCachedResponse):
    """
    Squad deleted

    Response for code 204. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        {}

    """

    headers: Headers204_delete_fleets_fleet_id_squads_squad_id = Field(
        ..., description='The response headers for this request.'
    )
    body: Model = Field(..., description='The response body for this request.')
