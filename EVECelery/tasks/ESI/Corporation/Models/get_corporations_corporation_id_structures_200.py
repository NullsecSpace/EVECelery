"""
A model definition module returned by an ESI task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Models.py'.
"""
from __future__ import annotations
from EVECelery.tasks.BaseTasks.Models.ModelsBase import ModelBaseEVECelery
from EVECelery.tasks.BaseTasks.Models.ModelsCached import ModelCachedResponse
from datetime import datetime
from typing import List, Literal, Optional

from pydantic import BaseModel, Field, conint


class Service(BaseModel):
    name: str = Field(
        ...,
        description='name string',
        title='get_corporations_corporation_id_structures_service_name',
    )
    state: Literal['online', 'offline', 'cleanup'] = Field(
        ...,
        description='state string',
        title='get_corporations_corporation_id_structures_service_state',
    )


class GetCorporationsCorporationIdStructuresOkItem(BaseModel):
    corporation_id: int = Field(
        ...,
        description='ID of the corporation that owns the structure',
        title='get_corporations_corporation_id_structures_corporation_id',
    )
    fuel_expires: Optional[datetime] = Field(
        None,
        description='Date on which the structure will run out of fuel',
        title='get_corporations_corporation_id_structures_fuel_expires',
    )
    name: Optional[str] = Field(
        None,
        description='The structure name',
        title='get_corporations_corporation_id_structures_name',
    )
    next_reinforce_apply: Optional[datetime] = Field(
        None,
        description="The date and time when the structure's newly requested reinforcement times (e.g. next_reinforce_hour and next_reinforce_day) will take effect",
        title='get_corporations_corporation_id_structures_next_reinforce_apply',
    )
    next_reinforce_hour: Optional[conint(ge=0, le=23)] = Field(
        None,
        description='The requested change to reinforce_hour that will take effect at the time shown by next_reinforce_apply',
        title='get_corporations_corporation_id_structures_next_reinforce_hour',
    )
    profile_id: int = Field(
        ...,
        description='The id of the ACL profile for this citadel',
        title='get_corporations_corporation_id_structures_profile_id',
    )
    reinforce_hour: Optional[conint(ge=0, le=23)] = Field(
        None,
        description='The hour of day that determines the four hour window when the structure will randomly exit its reinforcement periods and become vulnerable to attack against its armor and/or hull. The structure will become vulnerable at a random time that is +/- 2 hours centered on the value of this property',
        title='get_corporations_corporation_id_structures_reinforce_hour',
    )
    services: Optional[List[Service]] = Field(
        None,
        description='Contains a list of service upgrades, and their state',
        max_items=10,
        title='get_corporations_corporation_id_structures_services',
    )
    state: Literal[
        'anchor_vulnerable',
        'anchoring',
        'armor_reinforce',
        'armor_vulnerable',
        'deploy_vulnerable',
        'fitting_invulnerable',
        'hull_reinforce',
        'hull_vulnerable',
        'online_deprecated',
        'onlining_vulnerable',
        'shield_vulnerable',
        'unanchored',
        'unknown',
    ] = Field(
        ...,
        description='state string',
        title='get_corporations_corporation_id_structures_state',
    )
    state_timer_end: Optional[datetime] = Field(
        None,
        description="Date at which the structure will move to it's next state",
        title='get_corporations_corporation_id_structures_state_timer_end',
    )
    state_timer_start: Optional[datetime] = Field(
        None,
        description="Date at which the structure entered it's current state",
        title='get_corporations_corporation_id_structures_state_timer_start',
    )
    structure_id: int = Field(
        ...,
        description='The Item ID of the structure',
        title='get_corporations_corporation_id_structures_structure_id',
    )
    system_id: int = Field(
        ...,
        description='The solar system the structure is in',
        title='get_corporations_corporation_id_structures_system_id',
    )
    type_id: int = Field(
        ...,
        description='The type id of the structure',
        title='get_corporations_corporation_id_structures_type_id',
    )
    unanchors_at: Optional[datetime] = Field(
        None,
        description='Date at which the structure will unanchor',
        title='get_corporations_corporation_id_structures_unanchors_at',
    )


class GetCorporationsCorporationIdStructuresOk(BaseModel):
    __root__: List[GetCorporationsCorporationIdStructuresOkItem] = Field(
        ...,
        description='200 ok array',
        max_items=250,
        title='get_corporations_corporation_id_structures_ok',
    )


class Headers200_get_corporations_corporation_id_structures(ModelBaseEVECelery):
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
    X_Pages: int | None = Field(description="Maximum page number", alias="X-Pages")


class Response200_get_corporations_corporation_id_structures(ModelCachedResponse):
    """
    List of corporation structures' information

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "corporation_id": 667531913,
            "name": "example name",
            "profile_id": 11237,
            "reinforce_hour": 22,
            "state": "shield_vulnerable",
            "structure_id": 1021975535893,
            "system_id": 30004763,
            "type_id": 35833
          }
        ]

    """

    headers: Headers200_get_corporations_corporation_id_structures = Field(
        ..., description='The response headers for this request.'
    )
    body: GetCorporationsCorporationIdStructuresOk = Field(
        ..., description='The response body for this request.'
    )
