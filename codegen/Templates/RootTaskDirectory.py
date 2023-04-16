"""
Task directory module for adding task objects as attributes to a namespace for easy access and code inspection.
This injection module is the root directory for ESI tasks and imports / instantiates all other task directory classes containing task objects.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/RootTaskDirectory.py'.
"""

{% for p in package_names -%}
from .{{ p }}.TaskDirectory import TaskDirectory as {{ p }}TaskDirectory
{% endfor %}

class TaskDirectory(object):
    """
    ESI directory for quickly finding other tasks

    This task directory contains all subdirectories of ESI task categories.
    """
    {% for p in package_names -%}
    @property
    def {{ p }}(self) -> {{ p }}TaskDirectory:
        """
        Subdirectory for ESI tasks categorized as "{{ p }}"


        :return: The task directory for all {{ p }} ESI tasks

        """
        return {{ p }}TaskDirectory()
    {% else %}
    pass
    {% endfor %}
