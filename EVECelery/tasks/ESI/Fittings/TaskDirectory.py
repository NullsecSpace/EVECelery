"""
Task directory module for adding task objects as attributes to a namespace for easy access and code inspection.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/TaskDirectory.py'.
"""

from .get_characters_character_id_fittings import get_characters_character_id_fittings
from .delete_characters_character_id_fittings_fitting_id import (
    delete_characters_character_id_fittings_fitting_id,
)


class TaskDirectory(object):
    """
    Directory for quickly finding tasks with easy access to documentation and code inspection

    This task directory contains all tasks as attributes that are categorized with 'Fittings'.
    """

    @property
    def get_characters_character_id_fittings(
        self,
    ) -> get_characters_character_id_fittings:
        """
        Get fittings


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Fittings.get_characters_character_id_fittings.get_characters_character_id_fittings.get_sync`,
        :func:`~EVECelery.tasks.ESI.Fittings.get_characters_character_id_fittings.get_characters_character_id_fittings.run`, and
        :class:`~EVECelery.tasks.ESI.Fittings.get_characters_character_id_fittings.get_characters_character_id_fittings`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_characters_character_id_fittings()

    @property
    def delete_characters_character_id_fittings_fitting_id(
        self,
    ) -> delete_characters_character_id_fittings_fitting_id:
        """
        Delete fitting


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Fittings.delete_characters_character_id_fittings_fitting_id.delete_characters_character_id_fittings_fitting_id.get_sync`,
        :func:`~EVECelery.tasks.ESI.Fittings.delete_characters_character_id_fittings_fitting_id.delete_characters_character_id_fittings_fitting_id.run`, and
        :class:`~EVECelery.tasks.ESI.Fittings.delete_characters_character_id_fittings_fitting_id.delete_characters_character_id_fittings_fitting_id`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return delete_characters_character_id_fittings_fitting_id()
