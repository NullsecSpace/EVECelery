from EVECelery.tasks.BaseTasks.ESIResqust import ESIRequest
from EVECelery.exceptions.tasks import InputValidationError
from pydantic import BaseModel, Field, validate_arguments
from typing import Union

{% for r in m.responses_success -%}
class ModelResponseHeaders{{ r.code }}(BaseModel):
    """
    Headers for response code {{ r.code }}
    """

    {% for p in r.header_properties -%}
    {{ p.pydantic_field }}
    {% endfor %}

class ModelResponse{{r.code}}(BaseModel):
    """
    {{ r.description | indent(width=4)}}

    Response for response code {{ r.code }}. This is the response body model that also contains the headers.

    -----Example responses:
    {{ r.example | indent(width=4)}}

    """
    headers: ModelResponseHeaders{{ r.code }} = Field(..., description='The response headers for this request.')
    {% for p in r.body_properties -%}
    {{p.pydantic_field}}
    {% endfor %}
{% endfor %}


class {{ m.class_name }}(ESIRequest):
    """
    {{ m.summary | indent(width=4)}}
    """

    def request_method(self) -> str:
        """
        Returns the type of request made to ESI

        This method will return the request method (get, post, etc.) made to ESI.
        :return: Request method passed to requests.request()
        """
        return "{{ m.method }}"

    def route(self, {{ m.pathParams|join(', ', attribute='function_param') }}{{ ', **kwargs' if m.pathParams |length > 0  else '**kwargs' }}) -> str:
        """
        ESI route with input request parameters

        {% for i in m.pathParams -%}
        {{ i.function_docstring }}
        {% endfor %}
        :return: ESI route with request path parameters if any
        """
        return f"{{ m.path }}"

    def cache_ttl_default(self) -> int:
        """
        TTL for when cache is unspecified.

        :return: The number of seconds to cache a response
        """
        return {{ m.default_cache_ttl }}  # current esi x-cached-seconds header

    @validate_arguments
    def run(self, {{ m.requestParams|join(', ', attribute='function_param') }}{{ ', **kwargs' if m.requestParams |length > 0  else '**kwargs' }}):
        """
        {{ m.summary | indent(width=8)}}

        {{ m.description | indent(width=8)}}

        {% for i in m.requestParams -%}
        {{ i.function_docstring }}
        {% endfor %}
        """
        return super().run({{ m.requestParams|join(', ', attribute='param_pass') }}{{ ', **kwargs' if m.requestParams |length > 0  else '**kwargs' }})