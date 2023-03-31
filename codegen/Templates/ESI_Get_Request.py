from EVECelery.tasks.BaseTasks.ESIResqust import ESIRequest
from EVECelery.exceptions.tasks import InputValidationError
from pydantic import BaseModel, Field
from typing import Union


class {{ m.class_name }}(ESIRequest):
    """
     {{ m.summary | indent(width=4)}}
    """

    def route(self, {{ m.pathParams|join(', ', attribute='function_param') }}) -> str:
        """
        ESI route with input request parameters

        {% for i in m.pathParams -%}
        {{ i.function_docstring }}
        {% endfor %}
        :return: ESI route with request path parameters if any
        :rtype: str
        """
        return f"{{ m.path }}"

    def ttl_404(self) -> int:
        """
        TTL for 4xx errors if not provided in headers.
        """
        return {{ m.default_cache_ttl }}  # current esi x-cached-seconds header

    def run(self, {{ m.requestParams|join(', ', attribute='function_param') }}):
        """
        {{ m.summary | indent(width=8)}}

        {{ m.description | indent(width=8)}}

        {% for i in m.requestParams -%}
        {{ i.function_docstring }}
        {% endfor %}
        """

