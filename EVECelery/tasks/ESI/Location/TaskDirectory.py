"""
Task directory module for adding task objects as attributes to a namespace for easy access and code inspection.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/TaskDirectory.py'.
"""

from .get_characters_character_id_location import get_characters_character_id_location
from .get_characters_character_id_online import get_characters_character_id_online
from .get_characters_character_id_ship import get_characters_character_id_ship


class TaskDirectory(object):
    """
    Directory for quickly finding tasks with easy access to documentation and code inspection

    This task directory contains all tasks as attributes that are categorized with 'Location'.
    """

    @property
    def get_characters_character_id_location(
        self,
    ) -> get_characters_character_id_location:
        """
        Get character location


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Location.get_characters_character_id_location.get_characters_character_id_location.get_sync`,
        :func:`~EVECelery.tasks.ESI.Location.get_characters_character_id_location.get_characters_character_id_location.run`, and
        :class:`~EVECelery.tasks.ESI.Location.get_characters_character_id_location.get_characters_character_id_location`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_characters_character_id_location()

    @property
    def get_characters_character_id_online(self) -> get_characters_character_id_online:
        """
        Get character online


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Location.get_characters_character_id_online.get_characters_character_id_online.get_sync`,
        :func:`~EVECelery.tasks.ESI.Location.get_characters_character_id_online.get_characters_character_id_online.run`, and
        :class:`~EVECelery.tasks.ESI.Location.get_characters_character_id_online.get_characters_character_id_online`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_characters_character_id_online()

    @property
    def get_characters_character_id_ship(self) -> get_characters_character_id_ship:
        """
        Get current ship


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Location.get_characters_character_id_ship.get_characters_character_id_ship.get_sync`,
        :func:`~EVECelery.tasks.ESI.Location.get_characters_character_id_ship.get_characters_character_id_ship.run`, and
        :class:`~EVECelery.tasks.ESI.Location.get_characters_character_id_ship.get_characters_character_id_ship`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_characters_character_id_ship()
