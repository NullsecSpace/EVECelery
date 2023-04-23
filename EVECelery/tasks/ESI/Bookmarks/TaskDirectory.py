"""
Task directory module for adding task objects as attributes to a namespace for easy access and code inspection.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/TaskDirectory.py'.
"""

from .get_characters_character_id_bookmarks import get_characters_character_id_bookmarks
from .get_characters_character_id_bookmarks_folders import (
    get_characters_character_id_bookmarks_folders,
)
from .get_corporations_corporation_id_bookmarks import (
    get_corporations_corporation_id_bookmarks,
)
from .get_corporations_corporation_id_bookmarks_folders import (
    get_corporations_corporation_id_bookmarks_folders,
)


class TaskDirectory(object):
    """
    Directory for quickly finding tasks with easy access to documentation and code inspection

    This task directory contains all tasks as attributes that are categorized with 'Bookmarks'.
    """

    @property
    def get_characters_character_id_bookmarks(
        self,
    ) -> get_characters_character_id_bookmarks:
        """
        List bookmarks


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Bookmarks.get_characters_character_id_bookmarks.get_characters_character_id_bookmarks.get_sync`,
        :func:`~EVECelery.tasks.ESI.Bookmarks.get_characters_character_id_bookmarks.get_characters_character_id_bookmarks.run`, and
        :class:`~EVECelery.tasks.ESI.Bookmarks.get_characters_character_id_bookmarks.get_characters_character_id_bookmarks`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_characters_character_id_bookmarks()

    @property
    def get_characters_character_id_bookmarks_folders(
        self,
    ) -> get_characters_character_id_bookmarks_folders:
        """
        List bookmark folders


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Bookmarks.get_characters_character_id_bookmarks_folders.get_characters_character_id_bookmarks_folders.get_sync`,
        :func:`~EVECelery.tasks.ESI.Bookmarks.get_characters_character_id_bookmarks_folders.get_characters_character_id_bookmarks_folders.run`, and
        :class:`~EVECelery.tasks.ESI.Bookmarks.get_characters_character_id_bookmarks_folders.get_characters_character_id_bookmarks_folders`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_characters_character_id_bookmarks_folders()

    @property
    def get_corporations_corporation_id_bookmarks(
        self,
    ) -> get_corporations_corporation_id_bookmarks:
        """
        List corporation bookmarks


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Bookmarks.get_corporations_corporation_id_bookmarks.get_corporations_corporation_id_bookmarks.get_sync`,
        :func:`~EVECelery.tasks.ESI.Bookmarks.get_corporations_corporation_id_bookmarks.get_corporations_corporation_id_bookmarks.run`, and
        :class:`~EVECelery.tasks.ESI.Bookmarks.get_corporations_corporation_id_bookmarks.get_corporations_corporation_id_bookmarks`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_corporations_corporation_id_bookmarks()

    @property
    def get_corporations_corporation_id_bookmarks_folders(
        self,
    ) -> get_corporations_corporation_id_bookmarks_folders:
        """
        List corporation bookmark folders


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Bookmarks.get_corporations_corporation_id_bookmarks_folders.get_corporations_corporation_id_bookmarks_folders.get_sync`,
        :func:`~EVECelery.tasks.ESI.Bookmarks.get_corporations_corporation_id_bookmarks_folders.get_corporations_corporation_id_bookmarks_folders.run`, and
        :class:`~EVECelery.tasks.ESI.Bookmarks.get_corporations_corporation_id_bookmarks_folders.get_corporations_corporation_id_bookmarks_folders`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_corporations_corporation_id_bookmarks_folders()
