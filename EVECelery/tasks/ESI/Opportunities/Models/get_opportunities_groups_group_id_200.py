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


class GetOpportunitiesGroupsGroupIdOk(BaseModel):
    connected_groups: List[int] = Field(
        ...,
        description='The groups that are connected to this group on the opportunities map',
        max_items=50,
        title='get_opportunities_groups_group_id_connected_groups',
    )
    description: str = Field(
        ...,
        description='description string',
        title='get_opportunities_groups_group_id_description',
    )
    group_id: int = Field(
        ...,
        description='group_id integer',
        title='get_opportunities_groups_group_id_group_id',
    )
    name: str = Field(
        ..., description='name string', title='get_opportunities_groups_group_id_name'
    )
    notification: str = Field(
        ...,
        description='notification string',
        title='get_opportunities_groups_group_id_notification',
    )
    required_tasks: List[int] = Field(
        ...,
        description='Tasks need to complete for this group',
        max_items=100,
        title='get_opportunities_groups_group_id_required_tasks',
    )


class Headers200_get_opportunities_groups_group_id(ModelBaseEVECelery):
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


class Response200_get_opportunities_groups_group_id(ModelCachedResponse):
    """
    Details of an opportunities group

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        {
          "connected_groups": [
            100
          ],
          "description": "As a capsuleer...",
          "group_id": 103,
          "name": "Welcome to New Eden",
          "notification": "Completed:<br>Welcome to New Eden",
          "required_tasks": [
            19
          ]
        }

    """

    headers: Headers200_get_opportunities_groups_group_id = Field(
        ..., description='The response headers for this request.'
    )
    body: GetOpportunitiesGroupsGroupIdOk = Field(
        ..., description='The response body for this request.'
    )
