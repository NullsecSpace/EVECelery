"""
Task directory module for adding task objects as attributes to a namespace for easy access and code inspection.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/TaskDirectory.py'.
"""

from .get_characters_character_id_calendar import get_characters_character_id_calendar
from .get_characters_character_id_calendar_event_id import (
    get_characters_character_id_calendar_event_id,
)
from .get_characters_character_id_calendar_event_id_attendees import (
    get_characters_character_id_calendar_event_id_attendees,
)


class TaskDirectory(object):
    """
    Directory for quickly finding tasks with easy access to documentation and code inspection

    This task directory contains all tasks as attributes that are categorized with 'Calendar'.
    """

    @property
    def get_characters_character_id_calendar(
        self,
    ) -> get_characters_character_id_calendar:
        """
        List calendar event summaries


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Calendar.get_characters_character_id_calendar.get_characters_character_id_calendar.get_sync`,
        :func:`~EVECelery.tasks.ESI.Calendar.get_characters_character_id_calendar.get_characters_character_id_calendar.run`, and
        :class:`~EVECelery.tasks.ESI.Calendar.get_characters_character_id_calendar.get_characters_character_id_calendar`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_characters_character_id_calendar()

    @property
    def get_characters_character_id_calendar_event_id(
        self,
    ) -> get_characters_character_id_calendar_event_id:
        """
        Get an event


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Calendar.get_characters_character_id_calendar_event_id.get_characters_character_id_calendar_event_id.get_sync`,
        :func:`~EVECelery.tasks.ESI.Calendar.get_characters_character_id_calendar_event_id.get_characters_character_id_calendar_event_id.run`, and
        :class:`~EVECelery.tasks.ESI.Calendar.get_characters_character_id_calendar_event_id.get_characters_character_id_calendar_event_id`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_characters_character_id_calendar_event_id()

    @property
    def get_characters_character_id_calendar_event_id_attendees(
        self,
    ) -> get_characters_character_id_calendar_event_id_attendees:
        """
        Get attendees


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Calendar.get_characters_character_id_calendar_event_id_attendees.get_characters_character_id_calendar_event_id_attendees.get_sync`,
        :func:`~EVECelery.tasks.ESI.Calendar.get_characters_character_id_calendar_event_id_attendees.get_characters_character_id_calendar_event_id_attendees.run`, and
        :class:`~EVECelery.tasks.ESI.Calendar.get_characters_character_id_calendar_event_id_attendees.get_characters_character_id_calendar_event_id_attendees`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_characters_character_id_calendar_event_id_attendees()
