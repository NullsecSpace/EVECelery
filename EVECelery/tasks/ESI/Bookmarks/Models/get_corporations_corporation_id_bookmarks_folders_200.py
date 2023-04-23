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


class GetCorporationsCorporationIdBookmarksFoldersOkItem(BaseModel):
    creator_id: Optional[int] = Field(
        None,
        description='creator_id integer',
        title='get_corporations_corporation_id_bookmarks_folders_creator_id',
    )
    folder_id: int = Field(
        ...,
        description='folder_id integer',
        title='get_corporations_corporation_id_bookmarks_folders_folder_id',
    )
    name: str = Field(
        ...,
        description='name string',
        title='get_corporations_corporation_id_bookmarks_folders_name',
    )


class GetCorporationsCorporationIdBookmarksFoldersOk(BaseModel):
    __root__: List[GetCorporationsCorporationIdBookmarksFoldersOkItem] = Field(
        ...,
        description='200 ok array',
        max_items=1000,
        title='get_corporations_corporation_id_bookmarks_folders_ok',
    )


class Headers200_get_corporations_corporation_id_bookmarks_folders(ModelBaseEVECelery):
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


class Response200_get_corporations_corporation_id_bookmarks_folders(
    ModelCachedResponse
):
    """
    List of corporation owned bookmark folders

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "folder_id": 5,
            "name": "Important Locations"
          }
        ]

    """

    headers: Headers200_get_corporations_corporation_id_bookmarks_folders = Field(
        ..., description='The response headers for this request.'
    )
    body: GetCorporationsCorporationIdBookmarksFoldersOk = Field(
        ..., description='The response body for this request.'
    )
