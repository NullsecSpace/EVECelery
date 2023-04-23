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


class Fuel(BaseModel):
    quantity: int = Field(
        ...,
        description='quantity integer',
        title='get_corporations_corporation_id_starbases_starbase_id_quantity',
    )
    type_id: int = Field(
        ...,
        description='type_id integer',
        title='get_corporations_corporation_id_starbases_starbase_id_type_id',
    )


class GetCorporationsCorporationIdStarbasesStarbaseIdOk(BaseModel):
    allow_alliance_members: bool = Field(
        ...,
        description='allow_alliance_members boolean',
        title='get_corporations_corporation_id_starbases_starbase_id_allow_alliance_members',
    )
    allow_corporation_members: bool = Field(
        ...,
        description='allow_corporation_members boolean',
        title='get_corporations_corporation_id_starbases_starbase_id_allow_corporation_members',
    )
    anchor: Literal[
        'alliance_member',
        'config_starbase_equipment_role',
        'corporation_member',
        'starbase_fuel_technician_role',
    ] = Field(
        ...,
        description='Who can anchor starbase (POS) and its structures',
        title='get_corporations_corporation_id_starbases_starbase_id_anchor',
    )
    attack_if_at_war: bool = Field(
        ...,
        description='attack_if_at_war boolean',
        title='get_corporations_corporation_id_starbases_starbase_id_attack_if_at_war',
    )
    attack_if_other_security_status_dropping: bool = Field(
        ...,
        description='attack_if_other_security_status_dropping boolean',
        title='get_corporations_corporation_id_starbases_starbase_id_attack_if_other_security_status_dropping',
    )
    attack_security_status_threshold: Optional[float] = Field(
        None,
        description="Starbase (POS) will attack if target's security standing is lower than this value",
        title='get_corporations_corporation_id_starbases_starbase_id_attack_security_status_threshold',
    )
    attack_standing_threshold: Optional[float] = Field(
        None,
        description="Starbase (POS) will attack if target's standing is lower than this value",
        title='get_corporations_corporation_id_starbases_starbase_id_attack_standing_threshold',
    )
    fuel_bay_take: Literal[
        'alliance_member',
        'config_starbase_equipment_role',
        'corporation_member',
        'starbase_fuel_technician_role',
    ] = Field(
        ...,
        description="Who can take fuel blocks out of the starbase (POS)'s fuel bay",
        title='get_corporations_corporation_id_starbases_starbase_id_fuel_bay_take',
    )
    fuel_bay_view: Literal[
        'alliance_member',
        'config_starbase_equipment_role',
        'corporation_member',
        'starbase_fuel_technician_role',
    ] = Field(
        ...,
        description="Who can view the starbase (POS)'s fule bay. Characters either need to have required role or belong to the starbase (POS) owner's corporation or alliance, as described by the enum, all other access settings follows the same scheme",
        title='get_corporations_corporation_id_starbases_starbase_id_fuel_bay_view',
    )
    fuels: Optional[List[Fuel]] = Field(
        None,
        description='Fuel blocks and other things that will be consumed when operating a starbase (POS)',
        max_items=20,
        title='get_corporations_corporation_id_starbases_starbase_id_fuels',
    )
    offline: Literal[
        'alliance_member',
        'config_starbase_equipment_role',
        'corporation_member',
        'starbase_fuel_technician_role',
    ] = Field(
        ...,
        description='Who can offline starbase (POS) and its structures',
        title='get_corporations_corporation_id_starbases_starbase_id_offline',
    )
    online: Literal[
        'alliance_member',
        'config_starbase_equipment_role',
        'corporation_member',
        'starbase_fuel_technician_role',
    ] = Field(
        ...,
        description='Who can online starbase (POS) and its structures',
        title='get_corporations_corporation_id_starbases_starbase_id_online',
    )
    unanchor: Literal[
        'alliance_member',
        'config_starbase_equipment_role',
        'corporation_member',
        'starbase_fuel_technician_role',
    ] = Field(
        ...,
        description='Who can unanchor starbase (POS) and its structures',
        title='get_corporations_corporation_id_starbases_starbase_id_unanchor',
    )
    use_alliance_standings: bool = Field(
        ...,
        description="True if the starbase (POS) is using alliance standings, otherwise using corporation's",
        title='get_corporations_corporation_id_starbases_starbase_id_use_alliance_standings',
    )


class Headers200_get_corporations_corporation_id_starbases_starbase_id(
    ModelBaseEVECelery
):
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


class Response200_get_corporations_corporation_id_starbases_starbase_id(
    ModelCachedResponse
):
    """
    List of starbases (POSes)

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        {
          "allow_alliance_members": false,
          "allow_corporation_members": true,
          "anchor": "config_starbase_equipment_role",
          "attack_if_at_war": true,
          "attack_if_other_security_status_dropping": false,
          "fuel_bay_take": "config_starbase_equipment_role",
          "fuel_bay_view": "config_starbase_equipment_role",
          "offline": "config_starbase_equipment_role",
          "online": "config_starbase_equipment_role",
          "unanchor": "config_starbase_equipment_role",
          "use_alliance_standings": false
        }

    """

    headers: Headers200_get_corporations_corporation_id_starbases_starbase_id = Field(
        ..., description='The response headers for this request.'
    )
    body: GetCorporationsCorporationIdStarbasesStarbaseIdOk = Field(
        ..., description='The response body for this request.'
    )
