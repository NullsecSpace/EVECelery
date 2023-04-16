"""
Task directory module for adding task objects as attributes to a namespace for easy access and code inspection.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/TaskDirectory.py'.
"""

{% for m in module_names -%}
from .{{ m }} import {{ m }}
{% endfor %}

class TaskDirectory(object):
    """
    Directory for quickly finding tasks with easy access to documentation and code inspection

    This task directory contains all tasks as attributes that are categorized with '{{ package_name }}'.
    """
    {% for m in module_names -%}
    @property
    def {{ m }}(self) -> {{ m }}:
        """
        {{ module_models.get(m).summary | indent(width=8)}}


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.{{package_name}}.{{ m }}.{{ m }}.get_sync`,
        :func:`~EVECelery.tasks.ESI.{{package_name}}.{{ m }}.{{ m }}.run`, and
        :class:`~EVECelery.tasks.ESI.{{package_name}}.{{ m }}.{{ m }}`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return {{ m }}()
    {% else %}
    pass
    {% endfor %}
