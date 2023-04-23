"""
A model definition module returned by an ESI task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Models.py'.
"""
from __future__ import annotations
from EVECelery.tasks.BaseTasks.Models.ModelsBase import ModelBaseEVECelery
from EVECelery.tasks.BaseTasks.Models.ModelsCached import ModelCachedResponse
from pydantic import BaseModel, Field


class GetCharactersCharacterIdShipOk(BaseModel):
    ship_item_id: int = Field(
        ...,
        description="Item id's are unique to a ship and persist until it is repackaged. This value can be used to track repeated uses of a ship, or detect when a pilot changes into a different instance of the same ship type.",
        title='get_characters_character_id_ship_ship_item_id',
    )
    ship_name: str = Field(
        ...,
        description='ship_name string',
        title='get_characters_character_id_ship_ship_name',
    )
    ship_type_id: int = Field(
        ...,
        description='ship_type_id integer',
        title='get_characters_character_id_ship_ship_type_id',
    )


class Headers200_get_characters_character_id_ship(ModelBaseEVECelery):
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


class Response200_get_characters_character_id_ship(ModelCachedResponse):
    """
    Get the current ship type, name and id

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        {
          "ship_item_id": 1000000016991,
          "ship_name": "SPACESHIPS!!!",
          "ship_type_id": 1233
        }

    """

    headers: Headers200_get_characters_character_id_ship = Field(
        ..., description='The response headers for this request.'
    )
    body: GetCharactersCharacterIdShipOk = Field(
        ..., description='The response body for this request.'
    )
