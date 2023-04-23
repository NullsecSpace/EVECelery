"""
A model definition module returned by an ESI task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Models.py'.
"""
from __future__ import annotations
from EVECelery.tasks.BaseTasks.Models.ModelsBase import ModelBaseEVECelery
from EVECelery.tasks.BaseTasks.Models.ModelsCached import ModelCachedResponse
from typing import List, Literal

from pydantic import BaseModel, Field, conint


class GetCorporationsCorporationIdBlueprintsOkItem(BaseModel):
    item_id: int = Field(
        ...,
        description='Unique ID for this item.',
        title='get_corporations_corporation_id_blueprints_item_id',
    )
    location_flag: Literal[
        'AssetSafety',
        'AutoFit',
        'Bonus',
        'Booster',
        'BoosterBay',
        'Capsule',
        'Cargo',
        'CorpDeliveries',
        'CorpSAG1',
        'CorpSAG2',
        'CorpSAG3',
        'CorpSAG4',
        'CorpSAG5',
        'CorpSAG6',
        'CorpSAG7',
        'CrateLoot',
        'Deliveries',
        'DroneBay',
        'DustBattle',
        'DustDatabank',
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
        'Impounded',
        'JunkyardReprocessed',
        'JunkyardTrashed',
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
        'OfficeFolder',
        'Pilot',
        'PlanetSurface',
        'QuafeBay',
        'QuantumCoreRoom',
        'Reward',
        'RigSlot0',
        'RigSlot1',
        'RigSlot2',
        'RigSlot3',
        'RigSlot4',
        'RigSlot5',
        'RigSlot6',
        'RigSlot7',
        'SecondaryStorage',
        'ServiceSlot0',
        'ServiceSlot1',
        'ServiceSlot2',
        'ServiceSlot3',
        'ServiceSlot4',
        'ServiceSlot5',
        'ServiceSlot6',
        'ServiceSlot7',
        'ShipHangar',
        'ShipOffline',
        'Skill',
        'SkillInTraining',
        'SpecializedAmmoHold',
        'SpecializedCommandCenterHold',
        'SpecializedFuelBay',
        'SpecializedGasHold',
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
        'StructureActive',
        'StructureFuel',
        'StructureInactive',
        'StructureOffline',
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
        'Wallet',
        'Wardrobe',
    ] = Field(
        ...,
        description='Type of the location_id',
        title='get_corporations_corporation_id_blueprints_location_flag',
    )
    location_id: int = Field(
        ...,
        description='References a station, a ship or an item_id if this blueprint is located within a container.',
        title='get_corporations_corporation_id_blueprints_location_id',
    )
    material_efficiency: conint(ge=0, le=25) = Field(
        ...,
        description='Material Efficiency Level of the blueprint.',
        title='get_corporations_corporation_id_blueprints_material_efficiency',
    )
    quantity: conint(ge=-2) = Field(
        ...,
        description='A range of numbers with a minimum of -2 and no maximum value where -1 is an original and -2 is a copy. It can be a positive integer if it is a stack of blueprint originals fresh from the market (e.g. no activities performed on them yet).',
        title='get_corporations_corporation_id_blueprints_quantity',
    )
    runs: conint(ge=-1) = Field(
        ...,
        description='Number of runs remaining if the blueprint is a copy, -1 if it is an original.',
        title='get_corporations_corporation_id_blueprints_runs',
    )
    time_efficiency: conint(ge=0, le=20) = Field(
        ...,
        description='Time Efficiency Level of the blueprint.',
        title='get_corporations_corporation_id_blueprints_time_efficiency',
    )
    type_id: int = Field(
        ...,
        description='type_id integer',
        title='get_corporations_corporation_id_blueprints_type_id',
    )


class GetCorporationsCorporationIdBlueprintsOk(BaseModel):
    __root__: List[GetCorporationsCorporationIdBlueprintsOkItem] = Field(
        ...,
        description='200 ok array',
        max_items=1000,
        title='get_corporations_corporation_id_blueprints_ok',
    )


class Headers200_get_corporations_corporation_id_blueprints(ModelBaseEVECelery):
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


class Response200_get_corporations_corporation_id_blueprints(ModelCachedResponse):
    """
    List of corporation blueprints

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "item_id": 1000000010495,
            "location_flag": "CorpSAG1",
            "location_id": 60014719,
            "material_efficiency": 0,
            "quantity": 1,
            "runs": -1,
            "time_efficiency": 0,
            "type_id": 691
          }
        ]

    """

    headers: Headers200_get_corporations_corporation_id_blueprints = Field(
        ..., description='The response headers for this request.'
    )
    body: GetCorporationsCorporationIdBlueprintsOk = Field(
        ..., description='The response body for this request.'
    )
