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


class GetCharactersCharacterIdAssetsOkItem(BaseModel):
    is_blueprint_copy: Optional[bool] = Field(
        None,
        description='is_blueprint_copy boolean',
        title='get_characters_character_id_assets_is_blueprint_copy',
    )
    is_singleton: bool = Field(
        ...,
        description='is_singleton boolean',
        title='get_characters_character_id_assets_is_singleton',
    )
    item_id: int = Field(
        ...,
        description='item_id integer',
        title='get_characters_character_id_assets_item_id',
    )
    location_flag: Literal[
        'AssetSafety',
        'AutoFit',
        'BoosterBay',
        'Cargo',
        'CorpseBay',
        'Deliveries',
        'DroneBay',
        'FighterBay',
        'FighterTube0',
        'FighterTube1',
        'FighterTube2',
        'FighterTube3',
        'FighterTube4',
        'FleetHangar',
        'FrigateEscapeBay',
        'Hangar',
        'HangarAll',
        'HiSlot0',
        'HiSlot1',
        'HiSlot2',
        'HiSlot3',
        'HiSlot4',
        'HiSlot5',
        'HiSlot6',
        'HiSlot7',
        'HiddenModifiers',
        'Implant',
        'LoSlot0',
        'LoSlot1',
        'LoSlot2',
        'LoSlot3',
        'LoSlot4',
        'LoSlot5',
        'LoSlot6',
        'LoSlot7',
        'Locked',
        'MedSlot0',
        'MedSlot1',
        'MedSlot2',
        'MedSlot3',
        'MedSlot4',
        'MedSlot5',
        'MedSlot6',
        'MedSlot7',
        'QuafeBay',
        'RigSlot0',
        'RigSlot1',
        'RigSlot2',
        'RigSlot3',
        'RigSlot4',
        'RigSlot5',
        'RigSlot6',
        'RigSlot7',
        'ShipHangar',
        'Skill',
        'SpecializedAmmoHold',
        'SpecializedAsteroidHold',
        'SpecializedCommandCenterHold',
        'SpecializedFuelBay',
        'SpecializedGasHold',
        'SpecializedIceHold',
        'SpecializedIndustrialShipHold',
        'SpecializedLargeShipHold',
        'SpecializedMaterialBay',
        'SpecializedMediumShipHold',
        'SpecializedMineralHold',
        'SpecializedOreHold',
        'SpecializedPlanetaryCommoditiesHold',
        'SpecializedSalvageHold',
        'SpecializedShipHold',
        'SpecializedSmallShipHold',
        'StructureDeedBay',
        'SubSystemBay',
        'SubSystemSlot0',
        'SubSystemSlot1',
        'SubSystemSlot2',
        'SubSystemSlot3',
        'SubSystemSlot4',
        'SubSystemSlot5',
        'SubSystemSlot6',
        'SubSystemSlot7',
        'Unlocked',
        'Wardrobe',
    ] = Field(
        ...,
        description='location_flag string',
        title='get_characters_character_id_assets_location_flag',
    )
    location_id: int = Field(
        ...,
        description='location_id integer',
        title='get_characters_character_id_assets_location_id',
    )
    location_type: Literal['station', 'solar_system', 'item', 'other'] = Field(
        ...,
        description='location_type string',
        title='get_characters_character_id_assets_location_type',
    )
    quantity: int = Field(
        ...,
        description='quantity integer',
        title='get_characters_character_id_assets_quantity',
    )
    type_id: int = Field(
        ...,
        description='type_id integer',
        title='get_characters_character_id_assets_type_id',
    )


class GetCharactersCharacterIdAssetsOk(BaseModel):
    __root__: List[GetCharactersCharacterIdAssetsOkItem] = Field(
        ...,
        description='200 ok array',
        max_items=1000,
        title='get_characters_character_id_assets_ok',
    )


class Headers200_get_characters_character_id_assets(ModelBaseEVECelery):
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


class Response200_get_characters_character_id_assets(ModelCachedResponse):
    """
    A flat list of the users assets

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "is_blueprint_copy": true,
            "is_singleton": true,
            "item_id": 1000000016835,
            "location_flag": "Hangar",
            "location_id": 60002959,
            "location_type": "station",
            "quantity": 1,
            "type_id": 3516
          }
        ]

    """

    headers: Headers200_get_characters_character_id_assets = Field(
        ..., description='The response headers for this request.'
    )
    body: GetCharactersCharacterIdAssetsOk = Field(
        ..., description='The response body for this request.'
    )
