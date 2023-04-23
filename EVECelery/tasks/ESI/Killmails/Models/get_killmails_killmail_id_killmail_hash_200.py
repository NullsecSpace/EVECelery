"""
A model definition module returned by an ESI task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Models.py'.
"""
from __future__ import annotations
from EVECelery.tasks.BaseTasks.Models.ModelsBase import ModelBaseEVECelery
from EVECelery.tasks.BaseTasks.Models.ModelsCached import ModelCachedResponse
from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field


class Attacker(BaseModel):
    alliance_id: Optional[int] = Field(
        None,
        description='alliance_id integer',
        title='get_killmails_killmail_id_killmail_hash_alliance_id',
    )
    character_id: Optional[int] = Field(
        None,
        description='character_id integer',
        title='get_killmails_killmail_id_killmail_hash_character_id',
    )
    corporation_id: Optional[int] = Field(
        None,
        description='corporation_id integer',
        title='get_killmails_killmail_id_killmail_hash_corporation_id',
    )
    damage_done: int = Field(
        ...,
        description='damage_done integer',
        title='get_killmails_killmail_id_killmail_hash_damage_done',
    )
    faction_id: Optional[int] = Field(
        None,
        description='faction_id integer',
        title='get_killmails_killmail_id_killmail_hash_faction_id',
    )
    final_blow: bool = Field(
        ...,
        description='Was the attacker the one to achieve the final blow\n',
        title='get_killmails_killmail_id_killmail_hash_final_blow',
    )
    security_status: float = Field(
        ...,
        description='Security status for the attacker\n',
        title='get_killmails_killmail_id_killmail_hash_security_status',
    )
    ship_type_id: Optional[int] = Field(
        None,
        description='What ship was the attacker flying\n',
        title='get_killmails_killmail_id_killmail_hash_ship_type_id',
    )
    weapon_type_id: Optional[int] = Field(
        None,
        description='What weapon was used by the attacker for the kill\n',
        title='get_killmails_killmail_id_killmail_hash_weapon_type_id',
    )


class Item1(BaseModel):
    flag: int = Field(
        ...,
        description='flag integer',
        title='get_killmails_killmail_id_killmail_hash_item_flag',
    )
    item_type_id: int = Field(
        ...,
        description='item_type_id integer',
        title='get_killmails_killmail_id_killmail_hash_item_item_type_id',
    )
    quantity_destroyed: Optional[int] = Field(
        None,
        description='quantity_destroyed integer',
        title='get_killmails_killmail_id_killmail_hash_item_quantity_destroyed',
    )
    quantity_dropped: Optional[int] = Field(
        None,
        description='quantity_dropped integer',
        title='get_killmails_killmail_id_killmail_hash_item_quantity_dropped',
    )
    singleton: int = Field(
        ...,
        description='singleton integer',
        title='get_killmails_killmail_id_killmail_hash_item_singleton',
    )


class Item(BaseModel):
    flag: int = Field(
        ...,
        description='Flag for the location of the item\n',
        title='get_killmails_killmail_id_killmail_hash_flag',
    )
    item_type_id: int = Field(
        ...,
        description='item_type_id integer',
        title='get_killmails_killmail_id_killmail_hash_item_type_id',
    )
    items: Optional[List[Item1]] = Field(
        None,
        description='items array',
        max_items=10000,
        title='get_killmails_killmail_id_killmail_hash_item_items',
    )
    quantity_destroyed: Optional[int] = Field(
        None,
        description='How many of the item were destroyed if any\n',
        title='get_killmails_killmail_id_killmail_hash_quantity_destroyed',
    )
    quantity_dropped: Optional[int] = Field(
        None,
        description='How many of the item were dropped if any\n',
        title='get_killmails_killmail_id_killmail_hash_quantity_dropped',
    )
    singleton: int = Field(
        ...,
        description='singleton integer',
        title='get_killmails_killmail_id_killmail_hash_singleton',
    )


class Position(BaseModel):
    x: float = Field(
        ..., description='x number', title='get_killmails_killmail_id_killmail_hash_x'
    )
    y: float = Field(
        ..., description='y number', title='get_killmails_killmail_id_killmail_hash_y'
    )
    z: float = Field(
        ..., description='z number', title='get_killmails_killmail_id_killmail_hash_z'
    )


class Victim(BaseModel):
    alliance_id: Optional[int] = Field(
        None,
        description='alliance_id integer',
        title='get_killmails_killmail_id_killmail_hash_victim_alliance_id',
    )
    character_id: Optional[int] = Field(
        None,
        description='character_id integer',
        title='get_killmails_killmail_id_killmail_hash_victim_character_id',
    )
    corporation_id: Optional[int] = Field(
        None,
        description='corporation_id integer',
        title='get_killmails_killmail_id_killmail_hash_victim_corporation_id',
    )
    damage_taken: int = Field(
        ...,
        description='How much total damage was taken by the victim\n',
        title='get_killmails_killmail_id_killmail_hash_damage_taken',
    )
    faction_id: Optional[int] = Field(
        None,
        description='faction_id integer',
        title='get_killmails_killmail_id_killmail_hash_victim_faction_id',
    )
    items: Optional[List[Item]] = Field(
        None,
        description='items array',
        max_items=10000,
        title='get_killmails_killmail_id_killmail_hash_items',
    )
    position: Optional[Position] = Field(
        None,
        description='Coordinates of the victim in Cartesian space relative to the Sun\n',
        title='get_killmails_killmail_id_killmail_hash_position',
    )
    ship_type_id: int = Field(
        ...,
        description='The ship that the victim was piloting and was destroyed\n',
        title='get_killmails_killmail_id_killmail_hash_victim_ship_type_id',
    )


class GetKillmailsKillmailIdKillmailHashOk(BaseModel):
    attackers: List[Attacker] = Field(
        ...,
        description='attackers array',
        max_items=10000,
        title='get_killmails_killmail_id_killmail_hash_attackers',
    )
    killmail_id: int = Field(
        ...,
        description='ID of the killmail',
        title='get_killmails_killmail_id_killmail_hash_killmail_id',
    )
    killmail_time: datetime = Field(
        ...,
        description='Time that the victim was killed and the killmail generated\n',
        title='get_killmails_killmail_id_killmail_hash_killmail_time',
    )
    moon_id: Optional[int] = Field(
        None,
        description='Moon if the kill took place at one',
        title='get_killmails_killmail_id_killmail_hash_moon_id',
    )
    solar_system_id: int = Field(
        ...,
        description='Solar system that the kill took place in\n',
        title='get_killmails_killmail_id_killmail_hash_solar_system_id',
    )
    victim: Victim = Field(
        ...,
        description='victim object',
        title='get_killmails_killmail_id_killmail_hash_victim',
    )
    war_id: Optional[int] = Field(
        None,
        description='War if the killmail is generated in relation to an official war\n',
        title='get_killmails_killmail_id_killmail_hash_war_id',
    )


class Headers200_get_killmails_killmail_id_killmail_hash(ModelBaseEVECelery):
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


class Response200_get_killmails_killmail_id_killmail_hash(ModelCachedResponse):
    """
    A killmail

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        {
          "attackers": [
            {
              "character_id": 95810944,
              "corporation_id": 1000179,
              "damage_done": 5745,
              "faction_id": 500003,
              "final_blow": true,
              "security_status": -0.3,
              "ship_type_id": 17841,
              "weapon_type_id": 3074
            }
          ],
          "killmail_id": 56733821,
          "killmail_time": "2016-10-22T17:13:36Z",
          "solar_system_id": 30002976,
          "victim": {
            "alliance_id": 621338554,
            "character_id": 92796241,
            "corporation_id": 841363671,
            "damage_taken": 5745,
            "items": [
              {
                "flag": 20,
                "item_type_id": 5973,
                "quantity_dropped": 1,
                "singleton": 0
              }
            ],
            "position": {
              "x": 452186600569.4748,
              "y": 146704961490.90222,
              "z": 109514596532.54477
            },
            "ship_type_id": 17812
          }
        }

    """

    headers: Headers200_get_killmails_killmail_id_killmail_hash = Field(
        ..., description='The response headers for this request.'
    )
    body: GetKillmailsKillmailIdKillmailHashOk = Field(
        ..., description='The response body for this request.'
    )
