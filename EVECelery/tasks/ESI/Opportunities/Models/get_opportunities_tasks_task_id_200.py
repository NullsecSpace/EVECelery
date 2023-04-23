"""
A model definition module returned by an ESI task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Models.py'.
"""
from __future__ import annotations
from EVECelery.tasks.BaseTasks.Models.ModelsBase import ModelBaseEVECelery
from EVECelery.tasks.BaseTasks.Models.ModelsCached import ModelCachedResponse
from pydantic import BaseModel, Field


class GetOpportunitiesTasksTaskIdOk(BaseModel):
    description: str = Field(
        ...,
        description='description string',
        title='get_opportunities_tasks_task_id_description',
    )
    name: str = Field(
        ..., description='name string', title='get_opportunities_tasks_task_id_name'
    )
    notification: str = Field(
        ...,
        description='notification string',
        title='get_opportunities_tasks_task_id_notification',
    )
    task_id: int = Field(
        ...,
        description='task_id integer',
        title='get_opportunities_tasks_task_id_task_id',
    )


class Headers200_get_opportunities_tasks_task_id(ModelBaseEVECelery):
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


class Response200_get_opportunities_tasks_task_id(ModelCachedResponse):
    """
    Details of an opportunities task

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        {
          "description": "To use station services...",
          "name": "Dock in the station",
          "notification": "Completed:<br>Docked in a station!",
          "task_id": 10
        }

    """

    headers: Headers200_get_opportunities_tasks_task_id = Field(
        ..., description='The response headers for this request.'
    )
    body: GetOpportunitiesTasksTaskIdOk = Field(
        ..., description='The response body for this request.'
    )
