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


class GetCharactersCharacterIdSearchOk(BaseModel):
    agent: Optional[List[int]] = Field(
        None,
        description='agent array',
        max_items=500,
        title='get_characters_character_id_search_agent',
    )
    alliance: Optional[List[int]] = Field(
        None,
        description='alliance array',
        max_items=500,
        title='get_characters_character_id_search_alliance',
    )
    character: Optional[List[int]] = Field(
        None,
        description='character array',
        max_items=500,
        title='get_characters_character_id_search_character',
    )
    constellation: Optional[List[int]] = Field(
        None,
        description='constellation array',
        max_items=500,
        title='get_characters_character_id_search_constellation',
    )
    corporation: Optional[List[int]] = Field(
        None,
        description='corporation array',
        max_items=500,
        title='get_characters_character_id_search_corporation',
    )
    faction: Optional[List[int]] = Field(
        None,
        description='faction array',
        max_items=500,
        title='get_characters_character_id_search_faction',
    )
    inventory_type: Optional[List[int]] = Field(
        None,
        description='inventory_type array',
        max_items=500,
        title='get_characters_character_id_search_inventory_type',
    )
    region: Optional[List[int]] = Field(
        None,
        description='region array',
        max_items=500,
        title='get_characters_character_id_search_region',
    )
    solar_system: Optional[List[int]] = Field(
        None,
        description='solar_system array',
        max_items=500,
        title='get_characters_character_id_search_solar_system',
    )
    station: Optional[List[int]] = Field(
        None,
        description='station array',
        max_items=500,
        title='get_characters_character_id_search_station',
    )
    structure: Optional[List[int]] = Field(
        None,
        description='structure array',
        max_items=500,
        title='get_characters_character_id_search_structure',
    )


class Headers200_get_characters_character_id_search(ModelBaseEVECelery):
    """
    Headers for response code 200
    """

    Cache_Control: str | None = Field(
        description="The caching mechanism used", alias="Cache-Control"
    )
    Content_Language: str | None = Field(
        description="The language used in the response", alias="Content-Language"
    )
    ETag: str | None = Field(description="RFC7232 compliant entity tag")
    Expires: str | None = Field(description="RFC7231 formatted datetime string")
    Last_Modified: str | None = Field(
        description="RFC7231 formatted datetime string", alias="Last-Modified"
    )


class Response200_get_characters_character_id_search(ModelCachedResponse):
    """
    A list of search results

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        {
          "solar_system": [
            30002510
          ],
          "station": [
            60004588,
            60004594,
            60005725,
            60009106,
            60012721,
            60012724,
            60012727
          ]
        }

    """

    headers: Headers200_get_characters_character_id_search = Field(
        ..., description='The response headers for this request.'
    )
    body: GetCharactersCharacterIdSearchOk = Field(
        ..., description='The response body for this request.'
    )
