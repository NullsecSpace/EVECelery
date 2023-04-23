"""
A model definition module returned by an ESI task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Models.py'.
"""
from __future__ import annotations
from EVECelery.tasks.BaseTasks.Models.ModelsBase import ModelBaseEVECelery
from EVECelery.tasks.BaseTasks.Models.ModelsCached import ModelCachedResponse
from typing import List, Optional

from pydantic import BaseModel, Field


class Agent(BaseModel):
    id: Optional[int] = Field(
        None, description='id integer', title='post_universe_ids_id'
    )
    name: Optional[str] = Field(
        None, description='name string', title='post_universe_ids_name'
    )


class Alliance(BaseModel):
    id: Optional[int] = Field(
        None, description='id integer', title='post_universe_ids_alliance_id'
    )
    name: Optional[str] = Field(
        None, description='name string', title='post_universe_ids_alliance_name'
    )


class Character(BaseModel):
    id: Optional[int] = Field(
        None, description='id integer', title='post_universe_ids_character_id'
    )
    name: Optional[str] = Field(
        None, description='name string', title='post_universe_ids_character_name'
    )


class Constellation(BaseModel):
    id: Optional[int] = Field(
        None, description='id integer', title='post_universe_ids_constellation_id'
    )
    name: Optional[str] = Field(
        None, description='name string', title='post_universe_ids_constellation_name'
    )


class Corporation(BaseModel):
    id: Optional[int] = Field(
        None, description='id integer', title='post_universe_ids_corporation_id'
    )
    name: Optional[str] = Field(
        None, description='name string', title='post_universe_ids_corporation_name'
    )


class Faction(BaseModel):
    id: Optional[int] = Field(
        None, description='id integer', title='post_universe_ids_faction_id'
    )
    name: Optional[str] = Field(
        None, description='name string', title='post_universe_ids_faction_name'
    )


class InventoryType(BaseModel):
    id: Optional[int] = Field(
        None, description='id integer', title='post_universe_ids_inventory_type_id'
    )
    name: Optional[str] = Field(
        None, description='name string', title='post_universe_ids_inventory_type_name'
    )


class Region(BaseModel):
    id: Optional[int] = Field(
        None, description='id integer', title='post_universe_ids_region_id'
    )
    name: Optional[str] = Field(
        None, description='name string', title='post_universe_ids_region_name'
    )


class Station(BaseModel):
    id: Optional[int] = Field(
        None, description='id integer', title='post_universe_ids_station_id'
    )
    name: Optional[str] = Field(
        None, description='name string', title='post_universe_ids_station_name'
    )


class System(BaseModel):
    id: Optional[int] = Field(
        None, description='id integer', title='post_universe_ids_system_id'
    )
    name: Optional[str] = Field(
        None, description='name string', title='post_universe_ids_system_name'
    )


class PostUniverseIdsOk(BaseModel):
    agents: Optional[List[Agent]] = Field(
        None,
        description='agents array',
        max_items=500,
        title='post_universe_ids_agents',
    )
    alliances: Optional[List[Alliance]] = Field(
        None,
        description='alliances array',
        max_items=500,
        title='post_universe_ids_alliances',
    )
    characters: Optional[List[Character]] = Field(
        None,
        description='characters array',
        max_items=500,
        title='post_universe_ids_characters',
    )
    constellations: Optional[List[Constellation]] = Field(
        None,
        description='constellations array',
        max_items=500,
        title='post_universe_ids_constellations',
    )
    corporations: Optional[List[Corporation]] = Field(
        None,
        description='corporations array',
        max_items=500,
        title='post_universe_ids_corporations',
    )
    factions: Optional[List[Faction]] = Field(
        None,
        description='factions array',
        max_items=500,
        title='post_universe_ids_factions',
    )
    inventory_types: Optional[List[InventoryType]] = Field(
        None,
        description='inventory_types array',
        max_items=500,
        title='post_universe_ids_inventory_types',
    )
    regions: Optional[List[Region]] = Field(
        None,
        description='regions array',
        max_items=500,
        title='post_universe_ids_regions',
    )
    stations: Optional[List[Station]] = Field(
        None,
        description='stations array',
        max_items=500,
        title='post_universe_ids_stations',
    )
    systems: Optional[List[System]] = Field(
        None,
        description='systems array',
        max_items=500,
        title='post_universe_ids_systems',
    )


class Headers200_post_universe_ids(ModelBaseEVECelery):
    """
    Headers for response code 200
    """

    Content_Language: str | None = Field(
        description="The language used in the response", alias="Content-Language"
    )


class Response200_post_universe_ids(ModelCachedResponse):
    """
    List of id/name associations for a set of names divided by category. Any name passed in that did not have a match will be ommitted

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        {
          "characters": [
            {
              "id": 95465499,
              "name": "CCP Bartender"
            },
            {
              "id": 2112625428,
              "name": "CCP Zoetrope"
            }
          ],
          "systems": [
            {
              "id": 30000142,
              "name": "Jita"
            }
          ]
        }

    """

    headers: Headers200_post_universe_ids = Field(
        ..., description='The response headers for this request.'
    )
    body: PostUniverseIdsOk = Field(
        ..., description='The response body for this request.'
    )
