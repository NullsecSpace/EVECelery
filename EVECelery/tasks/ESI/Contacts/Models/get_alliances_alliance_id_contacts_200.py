"""
A model definition module returned by an ESI task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Models.py'.
"""
from __future__ import annotations
from EVECelery.tasks.BaseTasks.Models.ModelsBase import ModelBaseEVECelery
from EVECelery.tasks.BaseTasks.Models.ModelsCached import ModelCachedResponse
from typing import List, Literal, Optional

from pydantic import BaseModel, Field


class GetAlliancesAllianceIdContactsOkItem(BaseModel):
    contact_id: int = Field(
        ...,
        description='contact_id integer',
        title='get_alliances_alliance_id_contacts_contact_id',
    )
    contact_type: Literal['character', 'corporation', 'alliance', 'faction'] = Field(
        ...,
        description='contact_type string',
        title='get_alliances_alliance_id_contacts_contact_type',
    )
    label_ids: Optional[List[int]] = Field(
        None,
        description='label_ids array',
        max_items=63,
        title='get_alliances_alliance_id_contacts_label_ids',
    )
    standing: float = Field(
        ...,
        description='Standing of the contact',
        title='get_alliances_alliance_id_contacts_standing',
    )


class GetAlliancesAllianceIdContactsOk(BaseModel):
    __root__: List[GetAlliancesAllianceIdContactsOkItem] = Field(
        ...,
        description='200 ok array',
        max_items=1000,
        title='get_alliances_alliance_id_contacts_ok',
    )


class Headers200_get_alliances_alliance_id_contacts(ModelBaseEVECelery):
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


class Response200_get_alliances_alliance_id_contacts(ModelCachedResponse):
    """
    A list of contacts

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "contact_id": 2112625428,
            "contact_type": "character",
            "standing": 9.9
          }
        ]

    """

    headers: Headers200_get_alliances_alliance_id_contacts = Field(
        ..., description='The response headers for this request.'
    )
    body: GetAlliancesAllianceIdContactsOk = Field(
        ..., description='The response body for this request.'
    )
