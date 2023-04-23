"""
A model definition module returned by an ESI task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Models.py'.
"""
from __future__ import annotations
from EVECelery.tasks.BaseTasks.Models.ModelsBase import ModelBaseEVECelery
from EVECelery.tasks.BaseTasks.Models.ModelsCached import ModelCachedResponse
from typing import Optional

from pydantic import BaseModel, Field


class GetDogmaAttributesAttributeIdOk(BaseModel):
    attribute_id: int = Field(
        ...,
        description='attribute_id integer',
        title='get_dogma_attributes_attribute_id_attribute_id',
    )
    default_value: Optional[float] = Field(
        None,
        description='default_value number',
        title='get_dogma_attributes_attribute_id_default_value',
    )
    description: Optional[str] = Field(
        None,
        description='description string',
        title='get_dogma_attributes_attribute_id_description',
    )
    display_name: Optional[str] = Field(
        None,
        description='display_name string',
        title='get_dogma_attributes_attribute_id_display_name',
    )
    high_is_good: Optional[bool] = Field(
        None,
        description='high_is_good boolean',
        title='get_dogma_attributes_attribute_id_high_is_good',
    )
    icon_id: Optional[int] = Field(
        None,
        description='icon_id integer',
        title='get_dogma_attributes_attribute_id_icon_id',
    )
    name: Optional[str] = Field(
        None, description='name string', title='get_dogma_attributes_attribute_id_name'
    )
    published: Optional[bool] = Field(
        None,
        description='published boolean',
        title='get_dogma_attributes_attribute_id_published',
    )
    stackable: Optional[bool] = Field(
        None,
        description='stackable boolean',
        title='get_dogma_attributes_attribute_id_stackable',
    )
    unit_id: Optional[int] = Field(
        None,
        description='unit_id integer',
        title='get_dogma_attributes_attribute_id_unit_id',
    )


class Headers200_get_dogma_attributes_attribute_id(ModelBaseEVECelery):
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


class Response200_get_dogma_attributes_attribute_id(ModelCachedResponse):
    """
    Information about a dogma attribute

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        {
          "attribute_id": 20,
          "default_value": 1,
          "description": "Factor by which topspeed increases.",
          "display_name": "Maximum Velocity Bonus",
          "high_is_good": true,
          "icon_id": 1389,
          "name": "speedFactor",
          "published": true,
          "unit_id": 124
        }

    """

    headers: Headers200_get_dogma_attributes_attribute_id = Field(
        ..., description='The response headers for this request.'
    )
    body: GetDogmaAttributesAttributeIdOk = Field(
        ..., description='The response body for this request.'
    )
