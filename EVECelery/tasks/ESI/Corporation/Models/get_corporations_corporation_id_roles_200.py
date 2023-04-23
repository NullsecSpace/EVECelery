"""
A model definition module returned by an ESI task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Models.py'.
"""
from __future__ import annotations
from EVECelery.tasks.BaseTasks.Models.ModelsBase import ModelBaseEVECelery
from EVECelery.tasks.BaseTasks.Models.ModelsCached import ModelCachedResponse
from typing import List, Literal, Optional

from pydantic import BaseModel, Field


class GetCorporationsCorporationIdRolesOkItem(BaseModel):
    character_id: int = Field(
        ...,
        description='character_id integer',
        title='get_corporations_corporation_id_roles_character_id',
    )
    grantable_roles: Optional[
        List[
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
        ]
    ] = Field(
        None,
        description='grantable_roles array',
        max_items=50,
        title='get_corporations_corporation_id_roles_grantable_roles',
    )
    grantable_roles_at_base: Optional[
        List[
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
        ]
    ] = Field(
        None,
        description='grantable_roles_at_base array',
        max_items=50,
        title='get_corporations_corporation_id_roles_grantable_roles_at_base',
    )
    grantable_roles_at_hq: Optional[
        List[
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
        ]
    ] = Field(
        None,
        description='grantable_roles_at_hq array',
        max_items=50,
        title='get_corporations_corporation_id_roles_grantable_roles_at_hq',
    )
    grantable_roles_at_other: Optional[
        List[
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
        ]
    ] = Field(
        None,
        description='grantable_roles_at_other array',
        max_items=50,
        title='get_corporations_corporation_id_roles_grantable_roles_at_other',
    )
    roles: Optional[
        List[
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
        ]
    ] = Field(
        None,
        description='roles array',
        max_items=50,
        title='get_corporations_corporation_id_roles_roles',
    )
    roles_at_base: Optional[
        List[
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
        ]
    ] = Field(
        None,
        description='roles_at_base array',
        max_items=50,
        title='get_corporations_corporation_id_roles_roles_at_base',
    )
    roles_at_hq: Optional[
        List[
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
        ]
    ] = Field(
        None,
        description='roles_at_hq array',
        max_items=50,
        title='get_corporations_corporation_id_roles_roles_at_hq',
    )
    roles_at_other: Optional[
        List[
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
        ]
    ] = Field(
        None,
        description='roles_at_other array',
        max_items=50,
        title='get_corporations_corporation_id_roles_roles_at_other',
    )


class GetCorporationsCorporationIdRolesOk(BaseModel):
    __root__: List[GetCorporationsCorporationIdRolesOkItem] = Field(
        ...,
        description='200 ok array',
        max_items=12601,
        title='get_corporations_corporation_id_roles_ok',
    )


class Headers200_get_corporations_corporation_id_roles(ModelBaseEVECelery):
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


class Response200_get_corporations_corporation_id_roles(ModelCachedResponse):
    """
    List of member character ID's and roles

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "character_id": 1000171,
            "roles": [
              "Director",
              "Station_Manager"
            ]
          }
        ]

    """

    headers: Headers200_get_corporations_corporation_id_roles = Field(
        ..., description='The response headers for this request.'
    )
    body: GetCorporationsCorporationIdRolesOk = Field(
        ..., description='The response body for this request.'
    )
