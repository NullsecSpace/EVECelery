"""
A model definition module returned by an ESI task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Models.py'.
"""
from __future__ import annotations
from EVECelery.tasks.BaseTasks.Models.ModelsBase import ModelBaseEVECelery
from EVECelery.tasks.BaseTasks.Models.ModelsCached import ModelCachedResponse
from typing import List, Literal

from pydantic import BaseModel, Field


class Item(BaseModel):
    flag: Literal[
        'Cargo',
        'DroneBay',
        'FighterBay',
        'HiSlot0',
        'HiSlot1',
        'HiSlot2',
        'HiSlot3',
        'HiSlot4',
        'HiSlot5',
        'HiSlot6',
        'HiSlot7',
        'Invalid',
        'LoSlot0',
        'LoSlot1',
        'LoSlot2',
        'LoSlot3',
        'LoSlot4',
        'LoSlot5',
        'LoSlot6',
        'LoSlot7',
        'MedSlot0',
        'MedSlot1',
        'MedSlot2',
        'MedSlot3',
        'MedSlot4',
        'MedSlot5',
        'MedSlot6',
        'MedSlot7',
        'RigSlot0',
        'RigSlot1',
        'RigSlot2',
        'ServiceSlot0',
        'ServiceSlot1',
        'ServiceSlot2',
        'ServiceSlot3',
        'ServiceSlot4',
        'ServiceSlot5',
        'ServiceSlot6',
        'ServiceSlot7',
        'SubSystemSlot0',
        'SubSystemSlot1',
        'SubSystemSlot2',
        'SubSystemSlot3',
    ] = Field(
        ...,
        description='flag string',
        title='get_characters_character_id_fittings_flag',
    )
    quantity: int = Field(
        ...,
        description='quantity integer',
        title='get_characters_character_id_fittings_quantity',
    )
    type_id: int = Field(
        ...,
        description='type_id integer',
        title='get_characters_character_id_fittings_type_id',
    )


class GetCharactersCharacterIdFittingsOkItem(BaseModel):
    description: str = Field(
        ...,
        description='description string',
        title='get_characters_character_id_fittings_description',
    )
    fitting_id: int = Field(
        ...,
        description='fitting_id integer',
        title='get_characters_character_id_fittings_fitting_id',
    )
    items: List[Item] = Field(
        ...,
        description='items array',
        max_items=512,
        title='get_characters_character_id_fittings_items',
    )
    name: str = Field(
        ...,
        description='name string',
        title='get_characters_character_id_fittings_name',
    )
    ship_type_id: int = Field(
        ...,
        description='ship_type_id integer',
        title='get_characters_character_id_fittings_ship_type_id',
    )


class GetCharactersCharacterIdFittingsOk(BaseModel):
    __root__: List[GetCharactersCharacterIdFittingsOkItem] = Field(
        ...,
        description='200 ok array',
        max_items=512,
        title='get_characters_character_id_fittings_ok',
    )


class Headers200_get_characters_character_id_fittings(ModelBaseEVECelery):
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


class Response200_get_characters_character_id_fittings(ModelCachedResponse):
    """
    A list of fittings

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "description": "Awesome Vindi fitting",
            "fitting_id": 1,
            "items": [
              {
                "flag": "Cargo",
                "quantity": 1,
                "type_id": 1234
              }
            ],
            "name": "Best Vindicator",
            "ship_type_id": 123
          }
        ]

    """

    headers: Headers200_get_characters_character_id_fittings = Field(
        ..., description='The response headers for this request.'
    )
    body: GetCharactersCharacterIdFittingsOk = Field(
        ..., description='The response body for this request.'
    )
