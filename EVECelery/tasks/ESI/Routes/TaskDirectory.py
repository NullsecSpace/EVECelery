"""
Task directory module for adding task objects as attributes to a namespace for easy access and code inspection.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/TaskDirectory.py'.
"""

from .get_route_origin_destination import get_route_origin_destination


class TaskDirectory(object):
    """
    Directory for quickly finding tasks with easy access to documentation and code inspection

    This task directory contains all tasks as attributes that are categorized with 'Routes'.
    """

    @property
    def get_route_origin_destination(self) -> get_route_origin_destination:
        """
        Get route


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Routes.get_route_origin_destination.get_route_origin_destination.get_sync`,
        :func:`~EVECelery.tasks.ESI.Routes.get_route_origin_destination.get_route_origin_destination.run`, and
        :class:`~EVECelery.tasks.ESI.Routes.get_route_origin_destination.get_route_origin_destination`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_route_origin_destination()
