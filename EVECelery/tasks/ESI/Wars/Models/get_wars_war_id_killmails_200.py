"""
A model definition module returned by an ESI task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Models.py'.
"""
from __future__ import annotations
from EVECelery.tasks.BaseTasks.Models.ModelsBase import ModelBaseEVECelery
from EVECelery.tasks.BaseTasks.Models.ModelsCached import ModelCachedResponse
from typing import List

from pydantic import BaseModel, Field


class GetWarsWarIdKillmailsOkItem(BaseModel):
    killmail_hash: str = Field(
        ...,
        description='A hash of this killmail',
        title='get_wars_war_id_killmails_killmail_hash',
    )
    killmail_id: int = Field(
        ...,
        description='ID of this killmail',
        title='get_wars_war_id_killmails_killmail_id',
    )


class GetWarsWarIdKillmailsOk(BaseModel):
    __root__: List[GetWarsWarIdKillmailsOkItem] = Field(
        ...,
        description='200 ok array',
        max_items=2000,
        title='get_wars_war_id_killmails_ok',
    )


class Headers200_get_wars_war_id_killmails(ModelBaseEVECelery):
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


class Response200_get_wars_war_id_killmails(ModelCachedResponse):
    """
    A list of killmail IDs and hashes

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "killmail_hash": "8eef5e8fb6b88fe3407c489df33822b2e3b57a5e",
            "killmail_id": 2
          },
          {
            "killmail_hash": "b41ccb498ece33d64019f64c0db392aa3aa701fb",
            "killmail_id": 1
          }
        ]

    """

    headers: Headers200_get_wars_war_id_killmails = Field(
        ..., description='The response headers for this request.'
    )
    body: GetWarsWarIdKillmailsOk = Field(
        ..., description='The response body for this request.'
    )
