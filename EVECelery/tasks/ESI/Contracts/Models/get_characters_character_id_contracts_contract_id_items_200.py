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


class GetCharactersCharacterIdContractsContractIdItemsOkItem(BaseModel):
    is_included: bool = Field(
        ...,
        description='true if the contract issuer has submitted this item with the contract, false if the isser is asking for this item in the contract',
        title='get_characters_character_id_contracts_contract_id_items_is_included',
    )
    is_singleton: bool = Field(
        ...,
        description='is_singleton boolean',
        title='get_characters_character_id_contracts_contract_id_items_is_singleton',
    )
    quantity: int = Field(
        ...,
        description='Number of items in the stack',
        title='get_characters_character_id_contracts_contract_id_items_quantity',
    )
    raw_quantity: Optional[int] = Field(
        None,
        description='-1 indicates that the item is a singleton (non-stackable). If the item happens to be a Blueprint, -1 is an Original and -2 is a Blueprint Copy',
        title='get_characters_character_id_contracts_contract_id_items_raw_quantity',
    )
    record_id: int = Field(
        ...,
        description='Unique ID for the item',
        title='get_characters_character_id_contracts_contract_id_items_record_id',
    )
    type_id: int = Field(
        ...,
        description='Type ID for item',
        title='get_characters_character_id_contracts_contract_id_items_type_id',
    )


class GetCharactersCharacterIdContractsContractIdItemsOk(BaseModel):
    __root__: List[GetCharactersCharacterIdContractsContractIdItemsOkItem] = Field(
        ...,
        description='200 ok array',
        max_items=5000,
        title='get_characters_character_id_contracts_contract_id_items_ok',
    )


class Headers200_get_characters_character_id_contracts_contract_id_items(
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


class Response200_get_characters_character_id_contracts_contract_id_items(
    ModelCachedResponse
):
    """
    A list of items in this contract

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "is_included": true,
            "is_singleton": false,
            "quantity": 1,
            "record_id": 123456,
            "type_id": 587
          }
        ]

    """

    headers: Headers200_get_characters_character_id_contracts_contract_id_items = Field(
        ..., description='The response headers for this request.'
    )
    body: GetCharactersCharacterIdContractsContractIdItemsOk = Field(
        ..., description='The response body for this request.'
    )
