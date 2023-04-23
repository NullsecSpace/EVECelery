"""
A model definition module returned by an ESI task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Models.py'.
"""
from __future__ import annotations
from EVECelery.tasks.BaseTasks.Models.ModelsBase import ModelBaseEVECelery
from EVECelery.tasks.BaseTasks.Models.ModelsCached import ModelCachedResponse
from datetime import datetime
from typing import List, Literal

from pydantic import BaseModel, Field


class GetCorporationsCorporationIdRolesHistoryOkItem(BaseModel):
    changed_at: datetime = Field(
        ...,
        description='changed_at string',
        title='get_corporations_corporation_id_roles_history_changed_at',
    )
    character_id: int = Field(
        ...,
        description='The character whose roles are changed',
        title='get_corporations_corporation_id_roles_history_character_id',
    )
    issuer_id: int = Field(
        ...,
        description='ID of the character who issued this change',
        title='get_corporations_corporation_id_roles_history_issuer_id',
    )
    new_roles: List[
        Literal[
            'Account_Take_1',
            'Account_Take_2',
            'Account_Take_3',
            'Account_Take_4',
            'Account_Take_5',
            'Account_Take_6',
            'Account_Take_7',
            'Accountant',
            'Auditor',
            'Communications_Officer',
            'Config_Equipment',
            'Config_Starbase_Equipment',
            'Container_Take_1',
            'Container_Take_2',
            'Container_Take_3',
            'Container_Take_4',
            'Container_Take_5',
            'Container_Take_6',
            'Container_Take_7',
            'Contract_Manager',
            'Diplomat',
            'Director',
            'Factory_Manager',
            'Fitting_Manager',
            'Hangar_Query_1',
            'Hangar_Query_2',
            'Hangar_Query_3',
            'Hangar_Query_4',
            'Hangar_Query_5',
            'Hangar_Query_6',
            'Hangar_Query_7',
            'Hangar_Take_1',
            'Hangar_Take_2',
            'Hangar_Take_3',
            'Hangar_Take_4',
            'Hangar_Take_5',
            'Hangar_Take_6',
            'Hangar_Take_7',
            'Junior_Accountant',
            'Personnel_Manager',
            'Rent_Factory_Facility',
            'Rent_Office',
            'Rent_Research_Facility',
            'Security_Officer',
            'Starbase_Defense_Operator',
            'Starbase_Fuel_Technician',
            'Station_Manager',
            'Trader',
        ]
    ] = Field(
        ...,
        description='new_roles array',
        max_items=50,
        title='get_corporations_corporation_id_roles_history_new_roles',
    )
    old_roles: List[
        Literal[
            'Account_Take_1',
            'Account_Take_2',
            'Account_Take_3',
            'Account_Take_4',
            'Account_Take_5',
            'Account_Take_6',
            'Account_Take_7',
            'Accountant',
            'Auditor',
            'Communications_Officer',
            'Config_Equipment',
            'Config_Starbase_Equipment',
            'Container_Take_1',
            'Container_Take_2',
            'Container_Take_3',
            'Container_Take_4',
            'Container_Take_5',
            'Container_Take_6',
            'Container_Take_7',
            'Contract_Manager',
            'Diplomat',
            'Director',
            'Factory_Manager',
            'Fitting_Manager',
            'Hangar_Query_1',
            'Hangar_Query_2',
            'Hangar_Query_3',
            'Hangar_Query_4',
            'Hangar_Query_5',
            'Hangar_Query_6',
            'Hangar_Query_7',
            'Hangar_Take_1',
            'Hangar_Take_2',
            'Hangar_Take_3',
            'Hangar_Take_4',
            'Hangar_Take_5',
            'Hangar_Take_6',
            'Hangar_Take_7',
            'Junior_Accountant',
            'Personnel_Manager',
            'Rent_Factory_Facility',
            'Rent_Office',
            'Rent_Research_Facility',
            'Security_Officer',
            'Starbase_Defense_Operator',
            'Starbase_Fuel_Technician',
            'Station_Manager',
            'Trader',
        ]
    ] = Field(
        ...,
        description='old_roles array',
        max_items=50,
        title='get_corporations_corporation_id_roles_history_old_roles',
    )
    role_type: Literal[
        'grantable_roles',
        'grantable_roles_at_base',
        'grantable_roles_at_hq',
        'grantable_roles_at_other',
        'roles',
        'roles_at_base',
        'roles_at_hq',
        'roles_at_other',
    ] = Field(
        ...,
        description='role_type string',
        title='get_corporations_corporation_id_roles_history_role_type',
    )


class GetCorporationsCorporationIdRolesHistoryOk(BaseModel):
    __root__: List[GetCorporationsCorporationIdRolesHistoryOkItem] = Field(
        ...,
        description='200 ok array',
        max_items=1000,
        title='get_corporations_corporation_id_roles_history_ok',
    )


class Headers200_get_corporations_corporation_id_roles_history(ModelBaseEVECelery):
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
    X_Pages: int | None = Field(description="Maximum page number", alias="X-Pages")


class Response200_get_corporations_corporation_id_roles_history(ModelCachedResponse):
    """
    List of role changes

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "changed_at": "2016-10-25T14:46:00Z",
            "character_id": 12345,
            "issuer_id": 45678,
            "new_roles": [
              "Station_Manager"
            ],
            "old_roles": [
              "Diplomat"
            ],
            "role_type": "roles"
          }
        ]

    """

    headers: Headers200_get_corporations_corporation_id_roles_history = Field(
        ..., description='The response headers for this request.'
    )
    body: GetCorporationsCorporationIdRolesHistoryOk = Field(
        ..., description='The response body for this request.'
    )
