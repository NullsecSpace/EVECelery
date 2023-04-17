"""
Task directory module for adding task objects as attributes to a namespace for easy access and code inspection.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/TaskDirectory.py'.
"""

from .get_corporations_npccorps import get_corporations_npccorps
from .get_corporations_corporation_id_icons import get_corporations_corporation_id_icons
from .get_corporations_corporation_id_members import (
    get_corporations_corporation_id_members,
)


class TaskDirectory(object):
    """
    Directory for quickly finding tasks with easy access to documentation and code inspection

    This task directory contains all tasks as attributes that are categorized with 'Corporation'.
    """

    @property
    def get_corporations_npccorps(self) -> get_corporations_npccorps:
        """
        Get npc corporations


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Corporation.get_corporations_npccorps.get_corporations_npccorps.get_sync`,
        :func:`~EVECelery.tasks.ESI.Corporation.get_corporations_npccorps.get_corporations_npccorps.run`, and
        :class:`~EVECelery.tasks.ESI.Corporation.get_corporations_npccorps.get_corporations_npccorps`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_corporations_npccorps()

    @property
    def get_corporations_corporation_id_icons(
        self,
    ) -> get_corporations_corporation_id_icons:
        """
        Get corporation icon


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id_icons.get_corporations_corporation_id_icons.get_sync`,
        :func:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id_icons.get_corporations_corporation_id_icons.run`, and
        :class:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id_icons.get_corporations_corporation_id_icons`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_corporations_corporation_id_icons()

    @property
    def get_corporations_corporation_id_members(
        self,
    ) -> get_corporations_corporation_id_members:
        """
        Get corporation members


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id_members.get_corporations_corporation_id_members.get_sync`,
        :func:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id_members.get_corporations_corporation_id_members.run`, and
        :class:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id_members.get_corporations_corporation_id_members`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_corporations_corporation_id_members()
