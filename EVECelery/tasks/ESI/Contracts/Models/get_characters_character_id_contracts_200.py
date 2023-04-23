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


class GetCharactersCharacterIdContractsOkItem(BaseModel):
    acceptor_id: int = Field(
        ...,
        description='Who will accept the contract',
        title='get_characters_character_id_contracts_acceptor_id',
    )
    assignee_id: int = Field(
        ...,
        description='ID to whom the contract is assigned, can be alliance, corporation or character ID',
        title='get_characters_character_id_contracts_assignee_id',
    )
    availability: Literal['public', 'personal', 'corporation', 'alliance'] = Field(
        ...,
        description='To whom the contract is available',
        title='get_characters_character_id_contracts_availability',
    )
    buyout: Optional[float] = Field(
        None,
        description='Buyout price (for Auctions only)',
        title='get_characters_character_id_contracts_buyout',
    )
    collateral: Optional[float] = Field(
        None,
        description='Collateral price (for Couriers only)',
        title='get_characters_character_id_contracts_collateral',
    )
    contract_id: int = Field(
        ...,
        description='contract_id integer',
        title='get_characters_character_id_contracts_contract_id',
    )
    date_accepted: Optional[datetime] = Field(
        None,
        description='Date of confirmation of contract',
        title='get_characters_character_id_contracts_date_accepted',
    )
    date_completed: Optional[datetime] = Field(
        None,
        description='Date of completed of contract',
        title='get_characters_character_id_contracts_date_completed',
    )
    date_expired: datetime = Field(
        ...,
        description='Expiration date of the contract',
        title='get_characters_character_id_contracts_date_expired',
    )
    date_issued: datetime = Field(
        ...,
        description='Сreation date of the contract',
        title='get_characters_character_id_contracts_date_issued',
    )
    days_to_complete: Optional[int] = Field(
        None,
        description='Number of days to perform the contract',
        title='get_characters_character_id_contracts_days_to_complete',
    )
    end_location_id: Optional[int] = Field(
        None,
        description='End location ID (for Couriers contract)',
        title='get_characters_character_id_contracts_end_location_id',
    )
    for_corporation: bool = Field(
        ...,
        description="true if the contract was issued on behalf of the issuer's corporation",
        title='get_characters_character_id_contracts_for_corporation',
    )
    issuer_corporation_id: int = Field(
        ...,
        description="Character's corporation ID for the issuer",
        title='get_characters_character_id_contracts_issuer_corporation_id',
    )
    issuer_id: int = Field(
        ...,
        description='Character ID for the issuer',
        title='get_characters_character_id_contracts_issuer_id',
    )
    price: Optional[float] = Field(
        None,
        description='Price of contract (for ItemsExchange and Auctions)',
        title='get_characters_character_id_contracts_price',
    )
    reward: Optional[float] = Field(
        None,
        description='Remuneration for contract (for Couriers only)',
        title='get_characters_character_id_contracts_reward',
    )
    start_location_id: Optional[int] = Field(
        None,
        description='Start location ID (for Couriers contract)',
        title='get_characters_character_id_contracts_start_location_id',
    )
    status: Literal[
        'outstanding',
        'in_progress',
        'finished_issuer',
        'finished_contractor',
        'finished',
        'cancelled',
        'rejected',
        'failed',
        'deleted',
        'reversed',
    ] = Field(
        ...,
        description='Status of the the contract',
        title='get_characters_character_id_contracts_status',
    )
    title: Optional[str] = Field(
        None,
        description='Title of the contract',
        title='get_characters_character_id_contracts_title',
    )
    type: Literal['unknown', 'item_exchange', 'auction', 'courier', 'loan'] = Field(
        ...,
        description='Type of the contract',
        title='get_characters_character_id_contracts_type',
    )
    volume: Optional[float] = Field(
        None,
        description='Volume of items in the contract',
        title='get_characters_character_id_contracts_volume',
    )


class GetCharactersCharacterIdContractsOk(BaseModel):
    __root__: List[GetCharactersCharacterIdContractsOkItem] = Field(
        ...,
        description='200 ok array',
        max_items=1000,
        title='get_characters_character_id_contracts_ok',
    )


class Headers200_get_characters_character_id_contracts(ModelBaseEVECelery):
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


class Response200_get_characters_character_id_contracts(ModelCachedResponse):
    """
    A list of contracts

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "acceptor_id": 0,
            "assignee_id": 0,
            "availability": "public",
            "buyout": 10000000000.01,
            "contract_id": 1,
            "date_accepted": "2017-06-06T13:12:32Z",
            "date_completed": "2017-06-06T13:12:32Z",
            "date_expired": "2017-06-13T13:12:32Z",
            "date_issued": "2017-06-06T13:12:32Z",
            "days_to_complete": 0,
            "end_location_id": 60014719,
            "for_corporation": true,
            "issuer_corporation_id": 456,
            "issuer_id": 123,
            "price": 1000000.01,
            "reward": 0.01,
            "start_location_id": 60014719,
            "status": "outstanding",
            "type": "auction",
            "volume": 0.01
          }
        ]

    """

    headers: Headers200_get_characters_character_id_contracts = Field(
        ..., description='The response headers for this request.'
    )
    body: GetCharactersCharacterIdContractsOk = Field(
        ..., description='The response body for this request.'
    )
