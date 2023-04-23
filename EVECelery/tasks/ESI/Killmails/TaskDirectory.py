"""
Task directory module for adding task objects as attributes to a namespace for easy access and code inspection.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/TaskDirectory.py'.
"""

from .get_characters_character_id_killmails_recent import (
    get_characters_character_id_killmails_recent,
)
from .get_corporations_corporation_id_killmails_recent import (
    get_corporations_corporation_id_killmails_recent,
)
from .get_killmails_killmail_id_killmail_hash import (
    get_killmails_killmail_id_killmail_hash,
)


class TaskDirectory(object):
    """
    Directory for quickly finding tasks with easy access to documentation and code inspection

    This task directory contains all tasks as attributes that are categorized with 'Killmails'.
    """

    @property
    def get_characters_character_id_killmails_recent(
        self,
    ) -> get_characters_character_id_killmails_recent:
        """
        Get a character's recent kills and losses


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Killmails.get_characters_character_id_killmails_recent.get_characters_character_id_killmails_recent.get_sync`,
        :func:`~EVECelery.tasks.ESI.Killmails.get_characters_character_id_killmails_recent.get_characters_character_id_killmails_recent.run`, and
        :class:`~EVECelery.tasks.ESI.Killmails.get_characters_character_id_killmails_recent.get_characters_character_id_killmails_recent`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_characters_character_id_killmails_recent()

    @property
    def get_corporations_corporation_id_killmails_recent(
        self,
    ) -> get_corporations_corporation_id_killmails_recent:
        """
        Get a corporation's recent kills and losses


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Killmails.get_corporations_corporation_id_killmails_recent.get_corporations_corporation_id_killmails_recent.get_sync`,
        :func:`~EVECelery.tasks.ESI.Killmails.get_corporations_corporation_id_killmails_recent.get_corporations_corporation_id_killmails_recent.run`, and
        :class:`~EVECelery.tasks.ESI.Killmails.get_corporations_corporation_id_killmails_recent.get_corporations_corporation_id_killmails_recent`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_corporations_corporation_id_killmails_recent()

    @property
    def get_killmails_killmail_id_killmail_hash(
        self,
    ) -> get_killmails_killmail_id_killmail_hash:
        """
        Get a single killmail


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Killmails.get_killmails_killmail_id_killmail_hash.get_killmails_killmail_id_killmail_hash.get_sync`,
        :func:`~EVECelery.tasks.ESI.Killmails.get_killmails_killmail_id_killmail_hash.get_killmails_killmail_id_killmail_hash.run`, and
        :class:`~EVECelery.tasks.ESI.Killmails.get_killmails_killmail_id_killmail_hash.get_killmails_killmail_id_killmail_hash`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_killmails_killmail_id_killmail_hash()
