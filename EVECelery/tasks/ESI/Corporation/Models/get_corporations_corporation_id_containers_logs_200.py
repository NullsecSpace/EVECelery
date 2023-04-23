"""
A model definition module returned by an ESI task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Models.py'.
"""
from __future__ import annotations
from EVECelery.tasks.BaseTasks.Models.ModelsBase import ModelBaseEVECelery
from EVECelery.tasks.BaseTasks.Models.ModelsCached import ModelCachedResponse
from datetime import datetime
from typing import List, Literal, Optional

from pydantic import BaseModel, Field


class GetCorporationsCorporationIdContainersLogsOkItem(BaseModel):
    action: Literal[
        'add',
        'assemble',
        'configure',
        'enter_password',
        'lock',
        'move',
        'repackage',
        'set_name',
        'set_password',
        'unlock',
    ] = Field(
        ...,
        description='action string',
        title='get_corporations_corporation_id_containers_logs_action',
    )
    character_id: int = Field(
        ...,
        description='ID of the character who performed the action.',
        title='get_corporations_corporation_id_containers_logs_character_id',
    )
    container_id: int = Field(
        ...,
        description='ID of the container',
        title='get_corporations_corporation_id_containers_logs_container_id',
    )
    container_type_id: int = Field(
        ...,
        description='Type ID of the container',
        title='get_corporations_corporation_id_containers_logs_container_type_id',
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
        description='location_flag string',
        title='get_corporations_corporation_id_containers_logs_location_flag',
    )
    location_id: int = Field(
        ...,
        description='location_id integer',
        title='get_corporations_corporation_id_containers_logs_location_id',
    )
    logged_at: datetime = Field(
        ...,
        description='Timestamp when this log was created',
        title='get_corporations_corporation_id_containers_logs_logged_at',
    )
    new_config_bitmask: Optional[int] = Field(
        None,
        description='new_config_bitmask integer',
        title='get_corporations_corporation_id_containers_logs_new_config_bitmask',
    )
    old_config_bitmask: Optional[int] = Field(
        None,
        description='old_config_bitmask integer',
        title='get_corporations_corporation_id_containers_logs_old_config_bitmask',
    )
    password_type: Optional[Literal['config', 'general']] = Field(
        None,
        description='Type of password set if action is of type SetPassword or EnterPassword',
        title='get_corporations_corporation_id_containers_logs_password_type',
    )
    quantity: Optional[int] = Field(
        None,
        description='Quantity of the item being acted upon',
        title='get_corporations_corporation_id_containers_logs_quantity',
    )
    type_id: Optional[int] = Field(
        None,
        description='Type ID of the item being acted upon',
        title='get_corporations_corporation_id_containers_logs_type_id',
    )


class GetCorporationsCorporationIdContainersLogsOk(BaseModel):
    __root__: List[GetCorporationsCorporationIdContainersLogsOkItem] = Field(
        ...,
        description='200 ok array',
        max_items=1000,
        title='get_corporations_corporation_id_containers_logs_ok',
    )


class Headers200_get_corporations_corporation_id_containers_logs(ModelBaseEVECelery):
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


class Response200_get_corporations_corporation_id_containers_logs(ModelCachedResponse):
    """
    List of corporation ALSC logs

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "action": "set_password",
            "character_id": 2112625428,
            "container_id": 1000000012279,
            "container_type_id": 17365,
            "location_flag": "CorpSAG1",
            "location_id": 1000000012278,
            "logged_at": "2017-10-10T14:00:00Z",
            "password_type": "general"
          },
          {
            "action": "lock",
            "character_id": 2112625428,
            "container_id": 1000000012279,
            "container_type_id": 17365,
            "location_flag": "CorpSAG1",
            "location_id": 1000000012278,
            "logged_at": "2017-10-11T12:04:33Z",
            "quantity": 30,
            "type_id": 1230
          },
          {
            "action": "configure",
            "character_id": 2112625428,
            "container_id": 1000000012279,
            "container_type_id": 17365,
            "location_flag": "CorpSAG2",
            "location_id": 1000000012278,
            "logged_at": "2017-10-11T12:06:29Z",
            "new_config_bitmask": 31,
            "old_config_bitmask": 23
          }
        ]

    """

    headers: Headers200_get_corporations_corporation_id_containers_logs = Field(
        ..., description='The response headers for this request.'
    )
    body: GetCorporationsCorporationIdContainersLogsOk = Field(
        ..., description='The response body for this request.'
    )
