"""
A model definition module returned by an ESI task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Models.py'.
"""
from __future__ import annotations
from EVECelery.tasks.BaseTasks.Models.ModelsBase import ModelBaseEVECelery
from EVECelery.tasks.BaseTasks.Models.ModelsCached import ModelCachedResponse
from typing import List, Optional

from pydantic import BaseModel, Field, conint, constr


class HangarItem(BaseModel):
    division: Optional[conint(ge=1, le=7)] = Field(
        None,
        description='division integer',
        title='get_corporations_corporation_id_divisions_division',
    )
    name: Optional[constr(max_length=50)] = Field(
        None,
        description='name string',
        title='get_corporations_corporation_id_divisions_name',
    )


class WalletItem(BaseModel):
    division: Optional[conint(ge=1, le=7)] = Field(
        None,
        description='division integer',
        title='get_corporations_corporation_id_divisions_wallet_division',
    )
    name: Optional[constr(max_length=50)] = Field(
        None,
        description='name string',
        title='get_corporations_corporation_id_divisions_wallet_name',
    )


class GetCorporationsCorporationIdDivisionsOk(BaseModel):
    hangar: Optional[List[HangarItem]] = Field(
        None,
        description='hangar array',
        max_items=7,
        title='get_corporations_corporation_id_divisions_hangar',
    )
    wallet: Optional[List[WalletItem]] = Field(
        None,
        description='wallet array',
        max_items=7,
        title='get_corporations_corporation_id_divisions_wallet',
    )


class Headers200_get_corporations_corporation_id_divisions(ModelBaseEVECelery):
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


class Response200_get_corporations_corporation_id_divisions(ModelCachedResponse):
    """
    List of corporation division names

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        {
          "hangar": [
            {
              "division": 1,
              "name": "Awesome Hangar 1"
            }
          ],
          "wallet": [
            {
              "division": 1,
              "name": "Rich Wallet 1"
            }
          ]
        }

    """

    headers: Headers200_get_corporations_corporation_id_divisions = Field(
        ..., description='The response headers for this request.'
    )
    body: GetCorporationsCorporationIdDivisionsOk = Field(
        ..., description='The response body for this request.'
    )
