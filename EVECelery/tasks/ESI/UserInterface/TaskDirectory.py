"""
Task directory module for adding task objects as attributes to a namespace for easy access and code inspection.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/TaskDirectory.py'.
"""

from .post_ui_autopilot_waypoint import post_ui_autopilot_waypoint
from .post_ui_openwindow_contract import post_ui_openwindow_contract
from .post_ui_openwindow_information import post_ui_openwindow_information
from .post_ui_openwindow_marketdetails import post_ui_openwindow_marketdetails


class TaskDirectory(object):
    """
    Directory for quickly finding tasks with easy access to documentation and code inspection

    This task directory contains all tasks as attributes that are categorized with 'UserInterface'.
    """

    @property
    def post_ui_autopilot_waypoint(self) -> post_ui_autopilot_waypoint:
        """
        Set Autopilot Waypoint


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.UserInterface.post_ui_autopilot_waypoint.post_ui_autopilot_waypoint.get_sync`,
        :func:`~EVECelery.tasks.ESI.UserInterface.post_ui_autopilot_waypoint.post_ui_autopilot_waypoint.run`, and
        :class:`~EVECelery.tasks.ESI.UserInterface.post_ui_autopilot_waypoint.post_ui_autopilot_waypoint`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return post_ui_autopilot_waypoint()

    @property
    def post_ui_openwindow_contract(self) -> post_ui_openwindow_contract:
        """
        Open Contract Window


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.UserInterface.post_ui_openwindow_contract.post_ui_openwindow_contract.get_sync`,
        :func:`~EVECelery.tasks.ESI.UserInterface.post_ui_openwindow_contract.post_ui_openwindow_contract.run`, and
        :class:`~EVECelery.tasks.ESI.UserInterface.post_ui_openwindow_contract.post_ui_openwindow_contract`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return post_ui_openwindow_contract()

    @property
    def post_ui_openwindow_information(self) -> post_ui_openwindow_information:
        """
        Open Information Window


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.UserInterface.post_ui_openwindow_information.post_ui_openwindow_information.get_sync`,
        :func:`~EVECelery.tasks.ESI.UserInterface.post_ui_openwindow_information.post_ui_openwindow_information.run`, and
        :class:`~EVECelery.tasks.ESI.UserInterface.post_ui_openwindow_information.post_ui_openwindow_information`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return post_ui_openwindow_information()

    @property
    def post_ui_openwindow_marketdetails(self) -> post_ui_openwindow_marketdetails:
        """
        Open Market Details


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.UserInterface.post_ui_openwindow_marketdetails.post_ui_openwindow_marketdetails.get_sync`,
        :func:`~EVECelery.tasks.ESI.UserInterface.post_ui_openwindow_marketdetails.post_ui_openwindow_marketdetails.run`, and
        :class:`~EVECelery.tasks.ESI.UserInterface.post_ui_openwindow_marketdetails.post_ui_openwindow_marketdetails`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return post_ui_openwindow_marketdetails()
