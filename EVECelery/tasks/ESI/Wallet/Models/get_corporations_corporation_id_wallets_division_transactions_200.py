"""
A model definition module returned by an ESI task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Models.py'.
"""
from __future__ import annotations
from EVECelery.tasks.BaseTasks.Models.ModelsBase import ModelBaseEVECelery
from EVECelery.tasks.BaseTasks.Models.ModelsCached import ModelCachedResponse
from datetime import datetime
from typing import List

from pydantic import BaseModel, Field


class GetCorporationsCorporationIdWalletsDivisionTransactionsOkItem(BaseModel):
    client_id: int = Field(
        ...,
        description='client_id integer',
        title='get_corporations_corporation_id_wallets_division_transactions_client_id',
    )
    date: datetime = Field(
        ...,
        description='Date and time of transaction',
        title='get_corporations_corporation_id_wallets_division_transactions_date',
    )
    is_buy: bool = Field(
        ...,
        description='is_buy boolean',
        title='get_corporations_corporation_id_wallets_division_transactions_is_buy',
    )
    journal_ref_id: int = Field(
        ...,
        description='-1 if there is no corresponding wallet journal entry',
        title='get_corporations_corporation_id_wallets_division_transactions_journal_ref_id',
    )
    location_id: int = Field(
        ...,
        description='location_id integer',
        title='get_corporations_corporation_id_wallets_division_transactions_location_id',
    )
    quantity: int = Field(
        ...,
        description='quantity integer',
        title='get_corporations_corporation_id_wallets_division_transactions_quantity',
    )
    transaction_id: int = Field(
        ...,
        description='Unique transaction ID',
        title='get_corporations_corporation_id_wallets_division_transactions_transaction_id',
    )
    type_id: int = Field(
        ...,
        description='type_id integer',
        title='get_corporations_corporation_id_wallets_division_transactions_type_id',
    )
    unit_price: float = Field(
        ...,
        description='Amount paid per unit',
        title='get_corporations_corporation_id_wallets_division_transactions_unit_price',
    )


class GetCorporationsCorporationIdWalletsDivisionTransactionsOk(BaseModel):
    __root__: List[
        GetCorporationsCorporationIdWalletsDivisionTransactionsOkItem
    ] = Field(
        ...,
        description='Wallet transactions',
        max_items=2500,
        title='get_corporations_corporation_id_wallets_division_transactions_ok',
    )


class Headers200_get_corporations_corporation_id_wallets_division_transactions(
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


class Response200_get_corporations_corporation_id_wallets_division_transactions(
    ModelCachedResponse
):
    """
    Wallet transactions

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "client_id": 54321,
            "date": "2016-10-24T09:00:00Z",
            "is_buy": true,
            "journal_ref_id": 67890,
            "location_id": 60014719,
            "quantity": 1,
            "transaction_id": 1234567890,
            "type_id": 587,
            "unit_price": 1
          }
        ]

    """

    headers: Headers200_get_corporations_corporation_id_wallets_division_transactions = Field(
        ..., description='The response headers for this request.'
    )
    body: GetCorporationsCorporationIdWalletsDivisionTransactionsOk = Field(
        ..., description='The response body for this request.'
    )
