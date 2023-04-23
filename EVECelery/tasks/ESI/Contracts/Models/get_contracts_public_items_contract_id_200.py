"""
A model definition module returned by an ESI task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Models.py'.
"""
from __future__ import annotations
from EVECelery.tasks.BaseTasks.Models.ModelsBase import ModelBaseEVECelery
from EVECelery.tasks.BaseTasks.Models.ModelsCached import ModelCachedResponse
from typing import List, Optional

from pydantic import BaseModel, Field, conint


class GetContractsPublicItemsContractIdOkItem(BaseModel):
    is_blueprint_copy: Optional[bool] = Field(
        None,
        description='is_blueprint_copy boolean',
        title='get_contracts_public_items_contract_id_is_blueprint_copy',
    )
    is_included: bool = Field(
        ...,
        description='true if the contract issuer has submitted this item with the contract, false if the isser is asking for this item in the contract',
        title='get_contracts_public_items_contract_id_is_included',
    )
    item_id: Optional[int] = Field(
        None,
        description='Unique ID for the item being sold. Not present if item is being requested by contract rather than sold with contract',
        title='get_contracts_public_items_contract_id_item_id',
    )
    material_efficiency: Optional[conint(ge=0, le=25)] = Field(
        None,
        description='Material Efficiency Level of the blueprint',
        title='get_contracts_public_items_contract_id_material_efficiency',
    )
    quantity: int = Field(
        ...,
        description='Number of items in the stack',
        title='get_contracts_public_items_contract_id_quantity',
    )
    record_id: int = Field(
        ...,
        description='Unique ID for the item, used by the contract system',
        title='get_contracts_public_items_contract_id_record_id',
    )
    runs: Optional[conint(ge=-1)] = Field(
        None,
        description='Number of runs remaining if the blueprint is a copy, -1 if it is an original',
        title='get_contracts_public_items_contract_id_runs',
    )
    time_efficiency: Optional[conint(ge=0, le=20)] = Field(
        None,
        description='Time Efficiency Level of the blueprint',
        title='get_contracts_public_items_contract_id_time_efficiency',
    )
    type_id: int = Field(
        ...,
        description='Type ID for item',
        title='get_contracts_public_items_contract_id_type_id',
    )


class GetContractsPublicItemsContractIdOk(BaseModel):
    __root__: List[GetContractsPublicItemsContractIdOkItem] = Field(
        ...,
        description='200 ok array',
        max_items=1000,
        title='get_contracts_public_items_contract_id_ok',
    )


class Headers200_get_contracts_public_items_contract_id(ModelBaseEVECelery):
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


class Response200_get_contracts_public_items_contract_id(ModelCachedResponse):
    """
    A list of items in this contract

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "is_included": true,
            "item_id": 123456,
            "quantity": 1,
            "record_id": 123456,
            "type_id": 587
          }
        ]

    """

    headers: Headers200_get_contracts_public_items_contract_id = Field(
        ..., description='The response headers for this request.'
    )
    body: GetContractsPublicItemsContractIdOk = Field(
        ..., description='The response body for this request.'
    )
