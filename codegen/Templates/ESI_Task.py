{% set model_names = [] %}
{% for r in m.responses_success %}
{{ model_names.append('Response%s_%s'| format(r.code, m.class_name)) or ''}}
{% endfor %}

{% set model_docstring_links = [] %}
{% for m in model_names %}
{{ model_docstring_links.append(':class:`%s`'| format(m)) or ''}}
{% endfor %}
"""
A task definition module with associated response models returned by the task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Task.py'.
"""

from typing import Union, Optional
from pydantic import validate_arguments
from EVECelery.tasks.BaseTasks.TaskESI import TaskESI
{% for r in m.responses_success %}
from .Models.{{ m.class_name }}_{{ r.code }} import Response{{ r.code }}_{{ m.class_name }}
{% endfor %}

class {{ m.class_name }}(TaskESI):
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
        {{ i.function_docstring|indent(width=8) }}
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
    def get_sync(self, {{ m.requestParams|join(', ', attribute='function_param') }}{{ ',' if m.requestParams |length > 0  else '' }}kwargs_apply_async: Optional[dict] = None, kwargs_get: Optional[dict] = None) -> Union[{{ model_names|join(', ') }}]:
        """
        {{ m.summary | indent(width=8)}}

        {{ m.description | indent(width=8)}}


        NOTE: This function calls the task and blocks until the result is available. This function is a wrapper around Celery's `task.apply_async() <https://docs.celeryq.dev/en/stable/reference/celery.app.task.html?highlight=apply_async#celery.app.task.Task.apply_async>`_
        and `AsyncResult.get() <https://docs.celeryq.dev/en/stable/reference/celery.result.html#celery.result.AsyncResult.get>`_ methods.
        Instead of a dictionary, this function returns a pydantic model to more easily see what returned data responses look like, what is optionally returned, etc.

        If you would instead like to return an async result, use Celery's `apply_async() <https://docs.celeryq.dev/en/stable/reference/celery.app.task.html?highlight=apply_async#celery.app.task.Task.apply_async>`_ method on this task.

        {% for i in m.requestParams -%}
        {{ i.function_docstring|indent(width=8) }}
        {% endfor -%}
        :param Optional[dict] kwargs_apply_async: Dictionary of keyword arguments passed to `task.apply_async() <https://docs.celeryq.dev/en/stable/reference/celery.app.task.html?highlight=apply_async#celery.app.task.Task.apply_async>`_
        :param Optional[dict] kwargs_get: Dictionary of keyword arguments passed to `AsyncResult.get() <https://docs.celeryq.dev/en/stable/reference/celery.result.html#celery.result.AsyncResult.get>`_
        :return: The response from ESI as a pydantic object. The response model will follow the structure of {{ model_docstring_links | join(' or ') }}.
        """
        return super().get_sync({{ m.requestParams|join(', ', attribute='param_pass') }}{{ ',' if m.requestParams |length > 0  else '' }}kwargs_apply_async=kwargs_apply_async, kwargs_get=kwargs_get)

    @validate_arguments
    def run(self, {{ m.requestParams|join(', ', attribute='function_param') }}{{ ',' if m.requestParams |length > 0  else '' }}**kwargs) -> dict:
        """
        The task body that runs on the EVECelery worker

        This is the task body that runs on the EVECelery worker.

        IMPORTANT NOTE: You should not directly call this function from your client code as it will run within the context of your client and won't be sent to the message broker to run on a worker node.
        To correctly call this task body, see `Celery's documentation <https://docs.celeryq.dev/en/stable/userguide/calling.html>`_ on methods for calling tasks.

        See also this task's :func:`get_sync` which is a wrapper function around Celery's apply_async().get() call.

        {{ m.summary | indent(width=8)}}

        {{ m.description | indent(width=8)}}

        {% for i in m.requestParams -%}
        {{ i.function_docstring|indent(width=8) }}
        {% endfor %}
        :return: The response from ESI as a JSON dictionary. The response dictionary will follow the structure of {{ model_docstring_links | join(' or ') }}.
        """
        return super().run({{ m.requestParams|join(', ', attribute='param_pass') }}{{ ', **kwargs' if m.requestParams |length > 0  else '**kwargs' }})
