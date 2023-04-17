"""
Task directory module for adding task objects as attributes to a namespace for easy access and code inspection.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/TaskDirectory.py'.
"""

from .get_characters_character_id_fatigue import get_characters_character_id_fatigue
from .get_characters_character_id_portrait import get_characters_character_id_portrait
from .get_characters_character_id_roles import get_characters_character_id_roles


class TaskDirectory(object):
    """
    Directory for quickly finding tasks with easy access to documentation and code inspection

    This task directory contains all tasks as attributes that are categorized with 'Character'.
    """

    @property
    def get_characters_character_id_fatigue(
        self,
    ) -> get_characters_character_id_fatigue:
        """
        Get jump fatigue


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Character.get_characters_character_id_fatigue.get_characters_character_id_fatigue.get_sync`,
        :func:`~EVECelery.tasks.ESI.Character.get_characters_character_id_fatigue.get_characters_character_id_fatigue.run`, and
        :class:`~EVECelery.tasks.ESI.Character.get_characters_character_id_fatigue.get_characters_character_id_fatigue`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_characters_character_id_fatigue()

    @property
    def get_characters_character_id_portrait(
        self,
    ) -> get_characters_character_id_portrait:
        """
        Get character portraits


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Character.get_characters_character_id_portrait.get_characters_character_id_portrait.get_sync`,
        :func:`~EVECelery.tasks.ESI.Character.get_characters_character_id_portrait.get_characters_character_id_portrait.run`, and
        :class:`~EVECelery.tasks.ESI.Character.get_characters_character_id_portrait.get_characters_character_id_portrait`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_characters_character_id_portrait()

    @property
    def get_characters_character_id_roles(self) -> get_characters_character_id_roles:
        """
        Get character corporation roles


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Character.get_characters_character_id_roles.get_characters_character_id_roles.get_sync`,
        :func:`~EVECelery.tasks.ESI.Character.get_characters_character_id_roles.get_characters_character_id_roles.run`, and
        :class:`~EVECelery.tasks.ESI.Character.get_characters_character_id_roles.get_characters_character_id_roles`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_characters_character_id_roles()
