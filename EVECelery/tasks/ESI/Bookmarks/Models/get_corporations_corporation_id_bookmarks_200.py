"""
A model definition module returned by an ESI task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Models.py'.
"""
from __future__ import annotations
from EVECelery.tasks.BaseTasks.Models.ModelsBase import ModelBaseEVECelery
from EVECelery.tasks.BaseTasks.Models.ModelsCached import ModelCachedResponse
from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field


class Coordinates(BaseModel):
    x: float = Field(
        ..., description='x number', title='get_corporations_corporation_id_bookmarks_x'
    )
    y: float = Field(
        ..., description='y number', title='get_corporations_corporation_id_bookmarks_y'
    )
    z: float = Field(
        ..., description='z number', title='get_corporations_corporation_id_bookmarks_z'
    )


class Item(BaseModel):
    item_id: int = Field(
        ...,
        description='item_id integer',
        title='get_corporations_corporation_id_bookmarks_item_id',
    )
    type_id: int = Field(
        ...,
        description='type_id integer',
        title='get_corporations_corporation_id_bookmarks_type_id',
    )


class GetCorporationsCorporationIdBookmarksOkItem(BaseModel):
    bookmark_id: int = Field(
        ...,
        description='bookmark_id integer',
        title='get_corporations_corporation_id_bookmarks_bookmark_id',
    )
    coordinates: Optional[Coordinates] = Field(
        None,
        description='Optional object that is returned if a bookmark was made on a planet or a random location in space.',
        title='get_corporations_corporation_id_bookmarks_coordinates',
    )
    created: datetime = Field(
        ...,
        description='created string',
        title='get_corporations_corporation_id_bookmarks_created',
    )
    creator_id: int = Field(
        ...,
        description='creator_id integer',
        title='get_corporations_corporation_id_bookmarks_creator_id',
    )
    folder_id: Optional[int] = Field(
        None,
        description='folder_id integer',
        title='get_corporations_corporation_id_bookmarks_folder_id',
    )
    item: Optional[Item] = Field(
        None,
        description='Optional object that is returned if a bookmark was made on a particular item.',
        title='get_corporations_corporation_id_bookmarks_item',
    )
    label: str = Field(
        ...,
        description='label string',
        title='get_corporations_corporation_id_bookmarks_label',
    )
    location_id: int = Field(
        ...,
        description='location_id integer',
        title='get_corporations_corporation_id_bookmarks_location_id',
    )
    notes: str = Field(
        ...,
        description='notes string',
        title='get_corporations_corporation_id_bookmarks_notes',
    )


class GetCorporationsCorporationIdBookmarksOk(BaseModel):
    __root__: List[GetCorporationsCorporationIdBookmarksOkItem] = Field(
        ...,
        description='200 ok array',
        max_items=1000,
        title='get_corporations_corporation_id_bookmarks_ok',
    )


class Headers200_get_corporations_corporation_id_bookmarks(ModelBaseEVECelery):
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


class Response200_get_corporations_corporation_id_bookmarks(ModelCachedResponse):
    """
    List of corporation owned bookmarks

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "bookmark_id": 4,
            "created": "2016-08-09T11:57:47Z",
            "creator_id": 2112625428,
            "folder_id": 5,
            "item": {
              "item_id": 50006722,
              "type_id": 29633
            },
            "label": "Stargate",
            "location_id": 30003430,
            "notes": "This is a stargate"
          },
          {
            "bookmark_id": 5,
            "coordinates": {
              "x": -2958928814000,
              "y": -338367275823,
              "z": 2114538075090
            },
            "created": "2016-08-09T11:57:47Z",
            "creator_id": 2112625428,
            "folder_id": 5,
            "label": "Random location",
            "location_id": 30003430,
            "notes": "This is a random location in space"
          }
        ]

    """

    headers: Headers200_get_corporations_corporation_id_bookmarks = Field(
        ..., description='The response headers for this request.'
    )
    body: GetCorporationsCorporationIdBookmarksOk = Field(
        ..., description='The response body for this request.'
    )
