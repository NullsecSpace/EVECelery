"""
Task directory module for adding task objects as attributes to a namespace for easy access and code inspection.
This injection module is the root and imports / instantiates all other task directory classes containing task objects.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/RootTaskDirectory.py'.
"""

{% for p in package_names -%}
from .{{ p }}.TaskDirectory import TaskDirectory as {{ p }}TaskDirectory
{% endfor %}

class TaskDirectory(object):
    """
    Root directory for quickly finding other task directories

    This root task directory contains all subdirectories containing tasks as attributes.
    """
    {% for m in package_names -%}
    {{m}}: {{m}}TaskDirectory = {{m}}TaskDirectory()
    {% endfor %}
