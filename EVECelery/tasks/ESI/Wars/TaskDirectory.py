"""
Task directory module for adding task objects as attributes to a namespace for easy access and code inspection.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/TaskDirectory.py'.
"""

from .get_wars import get_wars


class TaskDirectory(object):
    """
    Directory for quickly finding tasks with easy access to documentation and code inspection

    This task directory contains all tasks as attributes that are categorized with 'Wars'.
    """

    @property
    def get_wars(self) -> get_wars:
        """
        List wars


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Wars.get_wars.get_wars.get_sync`,
        :func:`~EVECelery.tasks.ESI.Wars.get_wars.get_wars.run`, and
        :class:`~EVECelery.tasks.ESI.Wars.get_wars.get_wars`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_wars()
