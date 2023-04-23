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


class Position(BaseModel):
    x: float = Field(
        ..., description='x number', title='get_universe_stations_station_id_x'
    )
    y: float = Field(
        ..., description='y number', title='get_universe_stations_station_id_y'
    )
    z: float = Field(
        ..., description='z number', title='get_universe_stations_station_id_z'
    )


class GetUniverseStationsStationIdOk(BaseModel):
    max_dockable_ship_volume: float = Field(
        ...,
        description='max_dockable_ship_volume number',
        title='get_universe_stations_station_id_max_dockable_ship_volume',
    )
    name: str = Field(
        ..., description='name string', title='get_universe_stations_station_id_name'
    )
    office_rental_cost: float = Field(
        ...,
        description='office_rental_cost number',
        title='get_universe_stations_station_id_office_rental_cost',
    )
    owner: Optional[int] = Field(
        None,
        description='ID of the corporation that controls this station',
        title='get_universe_stations_station_id_owner',
    )
    position: Position = Field(
        ...,
        description='position object',
        title='get_universe_stations_station_id_position',
    )
    race_id: Optional[int] = Field(
        None,
        description='race_id integer',
        title='get_universe_stations_station_id_race_id',
    )
    reprocessing_efficiency: float = Field(
        ...,
        description='reprocessing_efficiency number',
        title='get_universe_stations_station_id_reprocessing_efficiency',
    )
    reprocessing_stations_take: float = Field(
        ...,
        description='reprocessing_stations_take number',
        title='get_universe_stations_station_id_reprocessing_stations_take',
    )
    services: List[
        Literal[
            'bounty-missions',
            'assasination-missions',
            'courier-missions',
            'interbus',
            'reprocessing-plant',
            'refinery',
            'market',
            'black-market',
            'stock-exchange',
            'cloning',
            'surgery',
            'dna-therapy',
            'repair-facilities',
            'factory',
            'labratory',
            'gambling',
            'fitting',
            'paintshop',
            'news',
            'storage',
            'insurance',
            'docking',
            'office-rental',
            'jump-clone-facility',
            'loyalty-point-store',
            'navy-offices',
            'security-offices',
        ]
    ] = Field(
        ...,
        description='services array',
        max_items=30,
        title='get_universe_stations_station_id_services',
    )
    station_id: int = Field(
        ...,
        description='station_id integer',
        title='get_universe_stations_station_id_station_id',
    )
    system_id: int = Field(
        ...,
        description='The solar system this station is in',
        title='get_universe_stations_station_id_system_id',
    )
    type_id: int = Field(
        ...,
        description='type_id integer',
        title='get_universe_stations_station_id_type_id',
    )


class Headers200_get_universe_stations_station_id(ModelBaseEVECelery):
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


class Response200_get_universe_stations_station_id(ModelCachedResponse):
    """
    Information about a station

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        {
          "max_dockable_ship_volume": 50000000,
          "name": "Jakanerva III - Moon 15 - Prompt Delivery Storage",
          "office_rental_cost": 10000,
          "owner": 1000003,
          "position": {
            "x": 165632286720,
            "y": 2771804160,
            "z": -2455331266560
          },
          "race_id": 1,
          "reprocessing_efficiency": 0.5,
          "reprocessing_stations_take": 0.05,
          "services": [
            "courier-missions",
            "reprocessing-plant",
            "market",
            "repair-facilities",
            "fitting",
            "news",
            "storage",
            "insurance",
            "docking",
            "office-rental",
            "loyalty-point-store",
            "navy-offices"
          ],
          "station_id": 60000277,
          "system_id": 30000148,
          "type_id": 1531
        }

    """

    headers: Headers200_get_universe_stations_station_id = Field(
        ..., description='The response headers for this request.'
    )
    body: GetUniverseStationsStationIdOk = Field(
        ..., description='The response body for this request.'
    )
