"""
A model definition module returned by an ESI task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Models.py'.
"""
from __future__ import annotations
from EVECelery.tasks.BaseTasks.Models.ModelsBase import ModelBaseEVECelery
from EVECelery.tasks.BaseTasks.Models.ModelsCached import ModelCachedResponse
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class GetStatusOk(BaseModel):
    players: int = Field(
        ..., description='Current online player count', title='get_status_players'
    )
    server_version: str = Field(
        ..., description='Running version as string', title='get_status_server_version'
    )
    start_time: datetime = Field(
        ..., description='Server start timestamp', title='get_status_start_time'
    )
    vip: Optional[bool] = Field(
        None, description='If the server is in VIP mode', title='get_status_vip'
    )


class Headers200_get_status(ModelBaseEVECelery):
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


class Response200_get_status(ModelCachedResponse):
    """
    Server status

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        {
          "players": 12345,
          "server_version": "1132976",
          "start_time": "2017-01-02T12:34:56Z"
        }

    """

    headers: Headers200_get_status = Field(
        ..., description='The response headers for this request.'
    )
    body: GetStatusOk = Field(..., description='The response body for this request.')
