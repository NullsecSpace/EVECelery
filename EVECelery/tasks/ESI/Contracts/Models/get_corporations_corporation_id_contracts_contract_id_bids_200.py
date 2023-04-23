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


class GetCorporationsCorporationIdContractsContractIdBidsOkItem(BaseModel):
    amount: float = Field(
        ...,
        description='The amount bid, in ISK',
        title='get_corporations_corporation_id_contracts_contract_id_bids_amount',
    )
    bid_id: int = Field(
        ...,
        description='Unique ID for the bid',
        title='get_corporations_corporation_id_contracts_contract_id_bids_bid_id',
    )
    bidder_id: int = Field(
        ...,
        description='Character ID of the bidder',
        title='get_corporations_corporation_id_contracts_contract_id_bids_bidder_id',
    )
    date_bid: datetime = Field(
        ...,
        description='Datetime when the bid was placed',
        title='get_corporations_corporation_id_contracts_contract_id_bids_date_bid',
    )


class GetCorporationsCorporationIdContractsContractIdBidsOk(BaseModel):
    __root__: List[GetCorporationsCorporationIdContractsContractIdBidsOkItem] = Field(
        ...,
        description='200 ok array',
        max_items=1000,
        title='get_corporations_corporation_id_contracts_contract_id_bids_ok',
    )


class Headers200_get_corporations_corporation_id_contracts_contract_id_bids(
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
    X_Pages: int | None = Field(description="Maximum page number", alias="X-Pages")


class Response200_get_corporations_corporation_id_contracts_contract_id_bids(
    ModelCachedResponse
):
    """
    A list of bids

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "amount": 1.23,
            "bid_id": 1,
            "bidder_id": 123,
            "date_bid": "2017-01-01T10:10:10Z"
          }
        ]

    """

    headers: Headers200_get_corporations_corporation_id_contracts_contract_id_bids = (
        Field(..., description='The response headers for this request.')
    )
    body: GetCorporationsCorporationIdContractsContractIdBidsOk = Field(
        ..., description='The response body for this request.'
    )
