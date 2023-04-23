"""
A model definition module returned by an ESI task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Models.py'.
"""
from __future__ import annotations
from EVECelery.tasks.BaseTasks.Models.ModelsBase import ModelBaseEVECelery
from EVECelery.tasks.BaseTasks.Models.ModelsCached import ModelCachedResponse
from datetime import date
from typing import List, Literal

from pydantic import BaseModel, Field


class GetCorporationCorporationIdMiningObserversOkItem(BaseModel):
    last_updated: date = Field(
        ...,
        description='last_updated string',
        title='get_corporation_corporation_id_mining_observers_last_updated',
    )
    observer_id: int = Field(
        ...,
        description='The entity that was observing the asteroid field when it was mined.\n',
        title='get_corporation_corporation_id_mining_observers_observer_id',
    )
    observer_type: Literal['structure'] = Field(
        ...,
        description='The category of the observing entity',
        title='get_corporation_corporation_id_mining_observers_observer_type',
    )


class GetCorporationCorporationIdMiningObserversOk(BaseModel):
    __root__: List[GetCorporationCorporationIdMiningObserversOkItem] = Field(
        ...,
        description='200 ok array',
        max_items=1000,
        title='get_corporation_corporation_id_mining_observers_ok',
    )


class Headers200_get_corporation_corporation_id_mining_observers(ModelBaseEVECelery):
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


class Response200_get_corporation_corporation_id_mining_observers(ModelCachedResponse):
    """
    Observer list of a corporation

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "last_updated": "2017-09-19",
            "observer_id": 1,
            "observer_type": "structure"
          }
        ]

    """

    headers: Headers200_get_corporation_corporation_id_mining_observers = Field(
        ..., description='The response headers for this request.'
    )
    body: GetCorporationCorporationIdMiningObserversOk = Field(
        ..., description='The response body for this request.'
    )
