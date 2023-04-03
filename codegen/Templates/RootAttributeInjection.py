"""
Attribute injection module for adding task objects as attributes to a namespace for easy access and code inspection.
This injection module is the root and imports / instantiates all other injection classes containing task objects.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/RootAttributeInjection.py'.
"""

{% for p in package_names -%}
from .{{ p }}.AttributeInjection import AttributeInjection as {{ p }}_AttributeInjection
{% endfor %}

class AttributeInjection(object):
    """
    Root injection class for adding task objects as attributes to a namespace for easy access and code inspection.

    This class creates sub attribute injection classes containing task objects.
    This root attribute injection class contains no task objects.
    """
    {% for p in package_names -%}
    @property
    def {{ p }}(self) -> {{ p }}_AttributeInjection:
        return {{ p }}_AttributeInjection()
    {% else %}
    pass
    {% endfor %}
