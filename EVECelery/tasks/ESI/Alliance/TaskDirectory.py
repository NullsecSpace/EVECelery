"""
Task directory module for adding task objects as attributes to a namespace for easy access and code inspection.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/TaskDirectory.py'.
"""

from .get_alliances import get_alliances
from .get_alliances_alliance_id import get_alliances_alliance_id
from .get_alliances_alliance_id_corporations import (
    get_alliances_alliance_id_corporations,
)
from .get_alliances_alliance_id_icons import get_alliances_alliance_id_icons


class TaskDirectory(object):
    """
    Directory for quickly finding tasks with easy access to documentation and code inspection

    This task directory contains all tasks as attributes that are categorized with 'Alliance'.
    """

    @property
    def get_alliances(self) -> get_alliances:
        """
        List all alliances


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Alliance.get_alliances.get_alliances.get_sync`,
        :func:`~EVECelery.tasks.ESI.Alliance.get_alliances.get_alliances.run`, and
        :class:`~EVECelery.tasks.ESI.Alliance.get_alliances.get_alliances`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_alliances()

    @property
    def get_alliances_alliance_id(self) -> get_alliances_alliance_id:
        """
        Get alliance information


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Alliance.get_alliances_alliance_id.get_alliances_alliance_id.get_sync`,
        :func:`~EVECelery.tasks.ESI.Alliance.get_alliances_alliance_id.get_alliances_alliance_id.run`, and
        :class:`~EVECelery.tasks.ESI.Alliance.get_alliances_alliance_id.get_alliances_alliance_id`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_alliances_alliance_id()

    @property
    def get_alliances_alliance_id_corporations(
        self,
    ) -> get_alliances_alliance_id_corporations:
        """
        List alliance's corporations


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Alliance.get_alliances_alliance_id_corporations.get_alliances_alliance_id_corporations.get_sync`,
        :func:`~EVECelery.tasks.ESI.Alliance.get_alliances_alliance_id_corporations.get_alliances_alliance_id_corporations.run`, and
        :class:`~EVECelery.tasks.ESI.Alliance.get_alliances_alliance_id_corporations.get_alliances_alliance_id_corporations`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_alliances_alliance_id_corporations()

    @property
    def get_alliances_alliance_id_icons(self) -> get_alliances_alliance_id_icons:
        """
        Get alliance icon


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Alliance.get_alliances_alliance_id_icons.get_alliances_alliance_id_icons.get_sync`,
        :func:`~EVECelery.tasks.ESI.Alliance.get_alliances_alliance_id_icons.get_alliances_alliance_id_icons.run`, and
        :class:`~EVECelery.tasks.ESI.Alliance.get_alliances_alliance_id_icons.get_alliances_alliance_id_icons`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_alliances_alliance_id_icons()
