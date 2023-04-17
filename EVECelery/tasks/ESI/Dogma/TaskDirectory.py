"""
Task directory module for adding task objects as attributes to a namespace for easy access and code inspection.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/TaskDirectory.py'.
"""

from .get_dogma_attributes import get_dogma_attributes
from .get_dogma_attributes_attribute_id import get_dogma_attributes_attribute_id
from .get_dogma_effects import get_dogma_effects


class TaskDirectory(object):
    """
    Directory for quickly finding tasks with easy access to documentation and code inspection

    This task directory contains all tasks as attributes that are categorized with 'Dogma'.
    """

    @property
    def get_dogma_attributes(self) -> get_dogma_attributes:
        """
        Get attributes


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Dogma.get_dogma_attributes.get_dogma_attributes.get_sync`,
        :func:`~EVECelery.tasks.ESI.Dogma.get_dogma_attributes.get_dogma_attributes.run`, and
        :class:`~EVECelery.tasks.ESI.Dogma.get_dogma_attributes.get_dogma_attributes`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_dogma_attributes()

    @property
    def get_dogma_attributes_attribute_id(self) -> get_dogma_attributes_attribute_id:
        """
        Get attribute information


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Dogma.get_dogma_attributes_attribute_id.get_dogma_attributes_attribute_id.get_sync`,
        :func:`~EVECelery.tasks.ESI.Dogma.get_dogma_attributes_attribute_id.get_dogma_attributes_attribute_id.run`, and
        :class:`~EVECelery.tasks.ESI.Dogma.get_dogma_attributes_attribute_id.get_dogma_attributes_attribute_id`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_dogma_attributes_attribute_id()

    @property
    def get_dogma_effects(self) -> get_dogma_effects:
        """
        Get effects


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Dogma.get_dogma_effects.get_dogma_effects.get_sync`,
        :func:`~EVECelery.tasks.ESI.Dogma.get_dogma_effects.get_dogma_effects.run`, and
        :class:`~EVECelery.tasks.ESI.Dogma.get_dogma_effects.get_dogma_effects`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_dogma_effects()
