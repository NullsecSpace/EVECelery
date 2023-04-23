"""
A model definition module returned by an ESI task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Models.py'.
"""
from __future__ import annotations
from EVECelery.tasks.BaseTasks.Models.ModelsBase import ModelBaseEVECelery
from EVECelery.tasks.BaseTasks.Models.ModelsCached import ModelCachedResponse
from typing import Literal

from pydantic import BaseModel, Field


class GetUniverseStarsStarIdOk(BaseModel):
    age: int = Field(
        ..., description='Age of star in years', title='get_universe_stars_star_id_age'
    )
    luminosity: float = Field(
        ...,
        description='luminosity number',
        title='get_universe_stars_star_id_luminosity',
    )
    name: str = Field(
        ..., description='name string', title='get_universe_stars_star_id_name'
    )
    radius: int = Field(
        ..., description='radius integer', title='get_universe_stars_star_id_radius'
    )
    solar_system_id: int = Field(
        ...,
        description='solar_system_id integer',
        title='get_universe_stars_star_id_solar_system_id',
    )
    spectral_class: Literal[
        'K2 V',
        'K4 V',
        'G2 V',
        'G8 V',
        'M7 V',
        'K7 V',
        'M2 V',
        'K5 V',
        'M3 V',
        'G0 V',
        'G7 V',
        'G3 V',
        'F9 V',
        'G5 V',
        'F6 V',
        'K8 V',
        'K9 V',
        'K6 V',
        'G9 V',
        'G6 V',
        'G4 VI',
        'G4 V',
        'F8 V',
        'F2 V',
        'F1 V',
        'K3 V',
        'F0 VI',
        'G1 VI',
        'G0 VI',
        'K1 V',
        'M4 V',
        'M1 V',
        'M6 V',
        'M0 V',
        'K2 IV',
        'G2 VI',
        'K0 V',
        'K5 IV',
        'F5 VI',
        'G6 VI',
        'F6 VI',
        'F2 IV',
        'G3 VI',
        'M8 V',
        'F1 VI',
        'K1 IV',
        'F7 V',
        'G5 VI',
        'M5 V',
        'G7 VI',
        'F5 V',
        'F4 VI',
        'F8 VI',
        'K3 IV',
        'F4 IV',
        'F0 V',
        'G7 IV',
        'G8 VI',
        'F2 VI',
        'F4 V',
        'F7 VI',
        'F3 V',
        'G1 V',
        'G9 VI',
        'F3 IV',
        'F9 VI',
        'M9 V',
        'K0 IV',
        'F1 IV',
        'G4 IV',
        'F3 VI',
        'K4 IV',
        'G5 IV',
        'G3 IV',
        'G1 IV',
        'K7 IV',
        'G0 IV',
        'K6 IV',
        'K9 IV',
        'G2 IV',
        'F9 IV',
        'F0 IV',
        'K8 IV',
        'G8 IV',
        'F6 IV',
        'F5 IV',
        'A0',
        'A0IV',
        'A0IV2',
    ] = Field(
        ...,
        description='spectral_class string',
        title='get_universe_stars_star_id_spectral_class',
    )
    temperature: int = Field(
        ...,
        description='temperature integer',
        title='get_universe_stars_star_id_temperature',
    )
    type_id: int = Field(
        ..., description='type_id integer', title='get_universe_stars_star_id_type_id'
    )


class Headers200_get_universe_stars_star_id(ModelBaseEVECelery):
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


class Response200_get_universe_stars_star_id(ModelCachedResponse):
    """
    Information about a star

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        {
          "age": 9398686722,
          "luminosity": 0.06615000218153,
          "name": "BKG-Q2 - Star",
          "radius": 346600000,
          "solar_system_id": 30004333,
          "spectral_class": "K2 V",
          "temperature": 3953,
          "type_id": 45033
        }

    """

    headers: Headers200_get_universe_stars_star_id = Field(
        ..., description='The response headers for this request.'
    )
    body: GetUniverseStarsStarIdOk = Field(
        ..., description='The response body for this request.'
    )
