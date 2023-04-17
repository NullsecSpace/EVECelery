"""
Task directory module for adding task objects as attributes to a namespace for easy access and code inspection.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/TaskDirectory.py'.
"""

from .post_characters_character_id_contacts import post_characters_character_id_contacts


class TaskDirectory(object):
    """
    Directory for quickly finding tasks with easy access to documentation and code inspection

    This task directory contains all tasks as attributes that are categorized with 'Contacts'.
    """

    @property
    def post_characters_character_id_contacts(
        self,
    ) -> post_characters_character_id_contacts:
        """
        Add contacts


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Contacts.post_characters_character_id_contacts.post_characters_character_id_contacts.get_sync`,
        :func:`~EVECelery.tasks.ESI.Contacts.post_characters_character_id_contacts.post_characters_character_id_contacts.run`, and
        :class:`~EVECelery.tasks.ESI.Contacts.post_characters_character_id_contacts.post_characters_character_id_contacts`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return post_characters_character_id_contacts()
