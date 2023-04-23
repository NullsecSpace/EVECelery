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

from pydantic import BaseModel, Field, conint


class Link(BaseModel):
    destination_pin_id: int = Field(
        ...,
        description='destination_pin_id integer',
        title='get_characters_character_id_planets_planet_id_destination_pin_id',
    )
    link_level: conint(ge=0, le=10) = Field(
        ...,
        description='link_level integer',
        title='get_characters_character_id_planets_planet_id_link_level',
    )
    source_pin_id: int = Field(
        ...,
        description='source_pin_id integer',
        title='get_characters_character_id_planets_planet_id_source_pin_id',
    )


class Content(BaseModel):
    amount: int = Field(
        ...,
        description='amount integer',
        title='get_characters_character_id_planets_planet_id_amount',
    )
    type_id: int = Field(
        ...,
        description='type_id integer',
        title='get_characters_character_id_planets_planet_id_content_type_id',
    )


class Head(BaseModel):
    head_id: conint(ge=0, le=9) = Field(
        ...,
        description='head_id integer',
        title='get_characters_character_id_planets_planet_id_head_id',
    )
    latitude: float = Field(
        ...,
        description='latitude number',
        title='get_characters_character_id_planets_planet_id_head_latitude',
    )
    longitude: float = Field(
        ...,
        description='longitude number',
        title='get_characters_character_id_planets_planet_id_head_longitude',
    )


class ExtractorDetails(BaseModel):
    cycle_time: Optional[int] = Field(
        None,
        description='in seconds',
        title='get_characters_character_id_planets_planet_id_cycle_time',
    )
    head_radius: Optional[float] = Field(
        None,
        description='head_radius number',
        title='get_characters_character_id_planets_planet_id_head_radius',
    )
    heads: List[Head] = Field(
        ...,
        description='heads array',
        max_items=10,
        title='get_characters_character_id_planets_planet_id_heads',
    )
    product_type_id: Optional[int] = Field(
        None,
        description='product_type_id integer',
        title='get_characters_character_id_planets_planet_id_product_type_id',
    )
    qty_per_cycle: Optional[int] = Field(
        None,
        description='qty_per_cycle integer',
        title='get_characters_character_id_planets_planet_id_qty_per_cycle',
    )


class FactoryDetails(BaseModel):
    schematic_id: int = Field(
        ...,
        description='schematic_id integer',
        title='get_characters_character_id_planets_planet_id_factory_details_schematic_id',
    )


class Pin(BaseModel):
    contents: Optional[List[Content]] = Field(
        None,
        description='contents array',
        max_items=90,
        title='get_characters_character_id_planets_planet_id_contents',
    )
    expiry_time: Optional[datetime] = Field(
        None,
        description='expiry_time string',
        title='get_characters_character_id_planets_planet_id_expiry_time',
    )
    extractor_details: Optional[ExtractorDetails] = Field(
        None,
        description='extractor_details object',
        title='get_characters_character_id_planets_planet_id_extractor_details',
    )
    factory_details: Optional[FactoryDetails] = Field(
        None,
        description='factory_details object',
        title='get_characters_character_id_planets_planet_id_factory_details',
    )
    install_time: Optional[datetime] = Field(
        None,
        description='install_time string',
        title='get_characters_character_id_planets_planet_id_install_time',
    )
    last_cycle_start: Optional[datetime] = Field(
        None,
        description='last_cycle_start string',
        title='get_characters_character_id_planets_planet_id_last_cycle_start',
    )
    latitude: float = Field(
        ...,
        description='latitude number',
        title='get_characters_character_id_planets_planet_id_latitude',
    )
    longitude: float = Field(
        ...,
        description='longitude number',
        title='get_characters_character_id_planets_planet_id_longitude',
    )
    pin_id: int = Field(
        ...,
        description='pin_id integer',
        title='get_characters_character_id_planets_planet_id_pin_id',
    )
    schematic_id: Optional[int] = Field(
        None,
        description='schematic_id integer',
        title='get_characters_character_id_planets_planet_id_schematic_id',
    )
    type_id: int = Field(
        ...,
        description='type_id integer',
        title='get_characters_character_id_planets_planet_id_type_id',
    )


class Route(BaseModel):
    content_type_id: int = Field(
        ...,
        description='content_type_id integer',
        title='get_characters_character_id_planets_planet_id_route_content_type_id',
    )
    destination_pin_id: int = Field(
        ...,
        description='destination_pin_id integer',
        title='get_characters_character_id_planets_planet_id_route_destination_pin_id',
    )
    quantity: float = Field(
        ...,
        description='quantity number',
        title='get_characters_character_id_planets_planet_id_quantity',
    )
    route_id: int = Field(
        ...,
        description='route_id integer',
        title='get_characters_character_id_planets_planet_id_route_id',
    )
    source_pin_id: int = Field(
        ...,
        description='source_pin_id integer',
        title='get_characters_character_id_planets_planet_id_route_source_pin_id',
    )
    waypoints: Optional[List[int]] = Field(
        None,
        description='list of pin ID waypoints',
        max_items=5,
        title='get_characters_character_id_planets_planet_id_waypoints',
    )


class GetCharactersCharacterIdPlanetsPlanetIdOk(BaseModel):
    links: List[Link] = Field(
        ...,
        description='links array',
        max_items=500,
        title='get_characters_character_id_planets_planet_id_links',
    )
    pins: List[Pin] = Field(
        ...,
        description='pins array',
        max_items=100,
        title='get_characters_character_id_planets_planet_id_pins',
    )
    routes: List[Route] = Field(
        ...,
        description='routes array',
        max_items=1000,
        title='get_characters_character_id_planets_planet_id_routes',
    )


class Headers200_get_characters_character_id_planets_planet_id(ModelBaseEVECelery):
    """
    Headers for response code 200
    """

    pass


class Response200_get_characters_character_id_planets_planet_id(ModelCachedResponse):
    """
    Colony layout

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        {
          "links": [
            {
              "destination_pin_id": 1000000017022,
              "link_level": 0,
              "source_pin_id": 1000000017021
            }
          ],
          "pins": [
            {
              "latitude": 1.55087844973,
              "longitude": 0.717145933308,
              "pin_id": 1000000017021,
              "type_id": 2254
            },
            {
              "latitude": 1.53360639935,
              "longitude": 0.709775584394,
              "pin_id": 1000000017022,
              "type_id": 2256
            }
          ],
          "routes": [
            {
              "content_type_id": 2393,
              "destination_pin_id": 1000000017030,
              "quantity": 20,
              "route_id": 4,
              "source_pin_id": 1000000017029
            }
          ]
        }

    """

    headers: Headers200_get_characters_character_id_planets_planet_id = Field(
        ..., description='The response headers for this request.'
    )
    body: GetCharactersCharacterIdPlanetsPlanetIdOk = Field(
        ..., description='The response body for this request.'
    )
