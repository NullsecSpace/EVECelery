"""
Task directory module for adding task objects as attributes to a namespace for easy access and code inspection.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/TaskDirectory.py'.
"""

from .get_characters_character_id_fw_stats import get_characters_character_id_fw_stats
from .get_corporations_corporation_id_fw_stats import (
    get_corporations_corporation_id_fw_stats,
)
from .get_fw_leaderboards import get_fw_leaderboards
from .get_fw_leaderboards_characters import get_fw_leaderboards_characters
from .get_fw_leaderboards_corporations import get_fw_leaderboards_corporations
from .get_fw_stats import get_fw_stats
from .get_fw_systems import get_fw_systems
from .get_fw_wars import get_fw_wars


class TaskDirectory(object):
    """
    Directory for quickly finding tasks with easy access to documentation and code inspection

    This task directory contains all tasks as attributes that are categorized with 'FactionWarfare'.
    """

    @property
    def get_characters_character_id_fw_stats(
        self,
    ) -> get_characters_character_id_fw_stats:
        """
        Overview of a character involved in faction warfare


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.FactionWarfare.get_characters_character_id_fw_stats.get_characters_character_id_fw_stats.get_sync`,
        :func:`~EVECelery.tasks.ESI.FactionWarfare.get_characters_character_id_fw_stats.get_characters_character_id_fw_stats.run`, and
        :class:`~EVECelery.tasks.ESI.FactionWarfare.get_characters_character_id_fw_stats.get_characters_character_id_fw_stats`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_characters_character_id_fw_stats()

    @property
    def get_corporations_corporation_id_fw_stats(
        self,
    ) -> get_corporations_corporation_id_fw_stats:
        """
        Overview of a corporation involved in faction warfare


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.FactionWarfare.get_corporations_corporation_id_fw_stats.get_corporations_corporation_id_fw_stats.get_sync`,
        :func:`~EVECelery.tasks.ESI.FactionWarfare.get_corporations_corporation_id_fw_stats.get_corporations_corporation_id_fw_stats.run`, and
        :class:`~EVECelery.tasks.ESI.FactionWarfare.get_corporations_corporation_id_fw_stats.get_corporations_corporation_id_fw_stats`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_corporations_corporation_id_fw_stats()

    @property
    def get_fw_leaderboards(self) -> get_fw_leaderboards:
        """
        List of the top factions in faction warfare


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.FactionWarfare.get_fw_leaderboards.get_fw_leaderboards.get_sync`,
        :func:`~EVECelery.tasks.ESI.FactionWarfare.get_fw_leaderboards.get_fw_leaderboards.run`, and
        :class:`~EVECelery.tasks.ESI.FactionWarfare.get_fw_leaderboards.get_fw_leaderboards`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_fw_leaderboards()

    @property
    def get_fw_leaderboards_characters(self) -> get_fw_leaderboards_characters:
        """
        List of the top pilots in faction warfare


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.FactionWarfare.get_fw_leaderboards_characters.get_fw_leaderboards_characters.get_sync`,
        :func:`~EVECelery.tasks.ESI.FactionWarfare.get_fw_leaderboards_characters.get_fw_leaderboards_characters.run`, and
        :class:`~EVECelery.tasks.ESI.FactionWarfare.get_fw_leaderboards_characters.get_fw_leaderboards_characters`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_fw_leaderboards_characters()

    @property
    def get_fw_leaderboards_corporations(self) -> get_fw_leaderboards_corporations:
        """
        List of the top corporations in faction warfare


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.FactionWarfare.get_fw_leaderboards_corporations.get_fw_leaderboards_corporations.get_sync`,
        :func:`~EVECelery.tasks.ESI.FactionWarfare.get_fw_leaderboards_corporations.get_fw_leaderboards_corporations.run`, and
        :class:`~EVECelery.tasks.ESI.FactionWarfare.get_fw_leaderboards_corporations.get_fw_leaderboards_corporations`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_fw_leaderboards_corporations()

    @property
    def get_fw_stats(self) -> get_fw_stats:
        """
        An overview of statistics about factions involved in faction warfare


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.FactionWarfare.get_fw_stats.get_fw_stats.get_sync`,
        :func:`~EVECelery.tasks.ESI.FactionWarfare.get_fw_stats.get_fw_stats.run`, and
        :class:`~EVECelery.tasks.ESI.FactionWarfare.get_fw_stats.get_fw_stats`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_fw_stats()

    @property
    def get_fw_systems(self) -> get_fw_systems:
        """
        Ownership of faction warfare systems


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.FactionWarfare.get_fw_systems.get_fw_systems.get_sync`,
        :func:`~EVECelery.tasks.ESI.FactionWarfare.get_fw_systems.get_fw_systems.run`, and
        :class:`~EVECelery.tasks.ESI.FactionWarfare.get_fw_systems.get_fw_systems`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_fw_systems()

    @property
    def get_fw_wars(self) -> get_fw_wars:
        """
        Data about which NPC factions are at war


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.FactionWarfare.get_fw_wars.get_fw_wars.get_sync`,
        :func:`~EVECelery.tasks.ESI.FactionWarfare.get_fw_wars.get_fw_wars.run`, and
        :class:`~EVECelery.tasks.ESI.FactionWarfare.get_fw_wars.get_fw_wars`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_fw_wars()
