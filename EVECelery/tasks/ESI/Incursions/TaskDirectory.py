"""
Task directory module for adding task objects as attributes to a namespace for easy access and code inspection.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/TaskDirectory.py'.
"""

from .get_incursions import get_incursions


class TaskDirectory(object):
    """
    Directory for quickly finding tasks with easy access to documentation and code inspection

    This task directory contains all tasks as attributes that are categorized with 'Incursions'.
    """

    @property
    def get_incursions(self) -> get_incursions:
        """
        List incursions


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Incursions.get_incursions.get_incursions.get_sync`,
        :func:`~EVECelery.tasks.ESI.Incursions.get_incursions.get_incursions.run`, and
        :class:`~EVECelery.tasks.ESI.Incursions.get_incursions.get_incursions`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_incursions()
