"""
A model definition module returned by an ESI task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Models.py'.
"""
from __future__ import annotations
from EVECelery.tasks.BaseTasks.Models.ModelsBase import ModelBaseEVECelery
from EVECelery.tasks.BaseTasks.Models.ModelsCached import ModelCachedResponse
{{ r.body_module }}


class Headers{{ r.code }}_{{ task_name }}(ModelBaseEVECelery):
    """
    Headers for response code {{ r.code }}
    """

    {% for p in r.header_properties -%}
    {{ p.pydantic_field }}
    {% else %}
    pass
    {% endfor %}

class Response{{ r.code }}_{{ task_name }}(ModelCachedResponse):
    """
    {{ r.description | indent(width=4)}}

    Response for code {{ r.code }}. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        {{ r.example | indent(width=8)}}

    """

    headers: Headers{{ r.code }}_{{ task_name }} = Field(..., description='The response headers for this request.')
    body: {{ r.body_root_class }} = Field(..., description='The response body for this request.')
