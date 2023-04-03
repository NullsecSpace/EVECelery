"""
Attribute injection module for adding task objects as attributes to a namespace for easy access and code inspection.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/AttributeInjection.py'.
"""

{% for m in module_names -%}
from .{{ m }} import {{m}}
{% endfor %}

class {{ package_name }}(object):
    """
    Attribute injection class for adding task objects as attributes to a namespace for easy access and code inspection.
    """
    {% for m in module_names -%}
    @property
    def {{ m }}(self) -> {{ m }}:
        return {{ m }}()
    {% else %}
    pass
    {% endfor %}
