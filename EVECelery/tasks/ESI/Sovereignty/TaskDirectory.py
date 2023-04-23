"""
Task directory module for adding task objects as attributes to a namespace for easy access and code inspection.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/TaskDirectory.py'.
"""

from .get_sovereignty_campaigns import get_sovereignty_campaigns
from .get_sovereignty_map import get_sovereignty_map
from .get_sovereignty_structures import get_sovereignty_structures


class TaskDirectory(object):
    """
    Directory for quickly finding tasks with easy access to documentation and code inspection

    This task directory contains all tasks as attributes that are categorized with 'Sovereignty'.
    """

    @property
    def get_sovereignty_campaigns(self) -> get_sovereignty_campaigns:
        """
        List sovereignty campaigns


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Sovereignty.get_sovereignty_campaigns.get_sovereignty_campaigns.get_sync`,
        :func:`~EVECelery.tasks.ESI.Sovereignty.get_sovereignty_campaigns.get_sovereignty_campaigns.run`, and
        :class:`~EVECelery.tasks.ESI.Sovereignty.get_sovereignty_campaigns.get_sovereignty_campaigns`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_sovereignty_campaigns()

    @property
    def get_sovereignty_map(self) -> get_sovereignty_map:
        """
        List sovereignty of systems


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Sovereignty.get_sovereignty_map.get_sovereignty_map.get_sync`,
        :func:`~EVECelery.tasks.ESI.Sovereignty.get_sovereignty_map.get_sovereignty_map.run`, and
        :class:`~EVECelery.tasks.ESI.Sovereignty.get_sovereignty_map.get_sovereignty_map`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_sovereignty_map()

    @property
    def get_sovereignty_structures(self) -> get_sovereignty_structures:
        """
        List sovereignty structures


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Sovereignty.get_sovereignty_structures.get_sovereignty_structures.get_sync`,
        :func:`~EVECelery.tasks.ESI.Sovereignty.get_sovereignty_structures.get_sovereignty_structures.run`, and
        :class:`~EVECelery.tasks.ESI.Sovereignty.get_sovereignty_structures.get_sovereignty_structures`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_sovereignty_structures()
