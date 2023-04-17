"""
Task directory module for adding task objects as attributes to a namespace for easy access and code inspection.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/TaskDirectory.py'.
"""

from .get_characters_character_id_search import get_characters_character_id_search


class TaskDirectory(object):
    """
    Directory for quickly finding tasks with easy access to documentation and code inspection

    This task directory contains all tasks as attributes that are categorized with 'Search'.
    """

    @property
    def get_characters_character_id_search(self) -> get_characters_character_id_search:
        """
        Search on a string


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Search.get_characters_character_id_search.get_characters_character_id_search.get_sync`,
        :func:`~EVECelery.tasks.ESI.Search.get_characters_character_id_search.get_characters_character_id_search.run`, and
        :class:`~EVECelery.tasks.ESI.Search.get_characters_character_id_search.get_characters_character_id_search`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_characters_character_id_search()
