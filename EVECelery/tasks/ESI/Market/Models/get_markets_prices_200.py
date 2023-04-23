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


class GetMarketsPricesOkItem(BaseModel):
    adjusted_price: Optional[float] = Field(
        None,
        description='adjusted_price number',
        title='get_markets_prices_adjusted_price',
    )
    average_price: Optional[float] = Field(
        None,
        description='average_price number',
        title='get_markets_prices_average_price',
    )
    type_id: int = Field(
        ..., description='type_id integer', title='get_markets_prices_type_id'
    )


class GetMarketsPricesOk(BaseModel):
    __root__: List[GetMarketsPricesOkItem] = Field(
        ..., description='200 ok array', max_items=20000, title='get_markets_prices_ok'
    )


class Headers200_get_markets_prices(ModelBaseEVECelery):
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


class Response200_get_markets_prices(ModelCachedResponse):
    """
    A list of prices

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "adjusted_price": 306988.09,
            "average_price": 306292.67,
            "type_id": 32772
          }
        ]

    """

    headers: Headers200_get_markets_prices = Field(
        ..., description='The response headers for this request.'
    )
    body: GetMarketsPricesOk = Field(
        ..., description='The response body for this request.'
    )
