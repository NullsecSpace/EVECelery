"""
Task directory module for adding task objects as attributes to a namespace for easy access and code inspection.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/TaskDirectory.py'.
"""

from .get_characters_character_id_opportunities import (
    get_characters_character_id_opportunities,
)
from .get_opportunities_groups import get_opportunities_groups
from .get_opportunities_groups_group_id import get_opportunities_groups_group_id
from .get_opportunities_tasks import get_opportunities_tasks
from .get_opportunities_tasks_task_id import get_opportunities_tasks_task_id


class TaskDirectory(object):
    """
    Directory for quickly finding tasks with easy access to documentation and code inspection

    This task directory contains all tasks as attributes that are categorized with 'Opportunities'.
    """

    @property
    def get_characters_character_id_opportunities(
        self,
    ) -> get_characters_character_id_opportunities:
        """
        Get a character's completed tasks


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Opportunities.get_characters_character_id_opportunities.get_characters_character_id_opportunities.get_sync`,
        :func:`~EVECelery.tasks.ESI.Opportunities.get_characters_character_id_opportunities.get_characters_character_id_opportunities.run`, and
        :class:`~EVECelery.tasks.ESI.Opportunities.get_characters_character_id_opportunities.get_characters_character_id_opportunities`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_characters_character_id_opportunities()

    @property
    def get_opportunities_groups(self) -> get_opportunities_groups:
        """
        Get opportunities groups


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Opportunities.get_opportunities_groups.get_opportunities_groups.get_sync`,
        :func:`~EVECelery.tasks.ESI.Opportunities.get_opportunities_groups.get_opportunities_groups.run`, and
        :class:`~EVECelery.tasks.ESI.Opportunities.get_opportunities_groups.get_opportunities_groups`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_opportunities_groups()

    @property
    def get_opportunities_groups_group_id(self) -> get_opportunities_groups_group_id:
        """
        Get opportunities group


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Opportunities.get_opportunities_groups_group_id.get_opportunities_groups_group_id.get_sync`,
        :func:`~EVECelery.tasks.ESI.Opportunities.get_opportunities_groups_group_id.get_opportunities_groups_group_id.run`, and
        :class:`~EVECelery.tasks.ESI.Opportunities.get_opportunities_groups_group_id.get_opportunities_groups_group_id`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_opportunities_groups_group_id()

    @property
    def get_opportunities_tasks(self) -> get_opportunities_tasks:
        """
        Get opportunities tasks


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Opportunities.get_opportunities_tasks.get_opportunities_tasks.get_sync`,
        :func:`~EVECelery.tasks.ESI.Opportunities.get_opportunities_tasks.get_opportunities_tasks.run`, and
        :class:`~EVECelery.tasks.ESI.Opportunities.get_opportunities_tasks.get_opportunities_tasks`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_opportunities_tasks()

    @property
    def get_opportunities_tasks_task_id(self) -> get_opportunities_tasks_task_id:
        """
        Get opportunities task


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Opportunities.get_opportunities_tasks_task_id.get_opportunities_tasks_task_id.get_sync`,
        :func:`~EVECelery.tasks.ESI.Opportunities.get_opportunities_tasks_task_id.get_opportunities_tasks_task_id.run`, and
        :class:`~EVECelery.tasks.ESI.Opportunities.get_opportunities_tasks_task_id.get_opportunities_tasks_task_id`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_opportunities_tasks_task_id()
