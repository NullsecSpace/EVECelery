"""
Task directory module for adding task objects as attributes to a namespace for easy access and code inspection.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/TaskDirectory.py'.
"""

from .get_alliances_alliance_id_contacts import get_alliances_alliance_id_contacts
from .get_alliances_alliance_id_contacts_labels import (
    get_alliances_alliance_id_contacts_labels,
)
from .delete_characters_character_id_contacts import (
    delete_characters_character_id_contacts,
)
from .get_characters_character_id_contacts import get_characters_character_id_contacts
from .post_characters_character_id_contacts import post_characters_character_id_contacts
from .put_characters_character_id_contacts import put_characters_character_id_contacts
from .get_characters_character_id_contacts_labels import (
    get_characters_character_id_contacts_labels,
)
from .get_corporations_corporation_id_contacts import (
    get_corporations_corporation_id_contacts,
)
from .get_corporations_corporation_id_contacts_labels import (
    get_corporations_corporation_id_contacts_labels,
)


class TaskDirectory(object):
    """
    Directory for quickly finding tasks with easy access to documentation and code inspection

    This task directory contains all tasks as attributes that are categorized with 'Contacts'.
    """

    @property
    def get_alliances_alliance_id_contacts(self) -> get_alliances_alliance_id_contacts:
        """
        Get alliance contacts


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Contacts.get_alliances_alliance_id_contacts.get_alliances_alliance_id_contacts.get_sync`,
        :func:`~EVECelery.tasks.ESI.Contacts.get_alliances_alliance_id_contacts.get_alliances_alliance_id_contacts.run`, and
        :class:`~EVECelery.tasks.ESI.Contacts.get_alliances_alliance_id_contacts.get_alliances_alliance_id_contacts`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_alliances_alliance_id_contacts()

    @property
    def get_alliances_alliance_id_contacts_labels(
        self,
    ) -> get_alliances_alliance_id_contacts_labels:
        """
        Get alliance contact labels


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Contacts.get_alliances_alliance_id_contacts_labels.get_alliances_alliance_id_contacts_labels.get_sync`,
        :func:`~EVECelery.tasks.ESI.Contacts.get_alliances_alliance_id_contacts_labels.get_alliances_alliance_id_contacts_labels.run`, and
        :class:`~EVECelery.tasks.ESI.Contacts.get_alliances_alliance_id_contacts_labels.get_alliances_alliance_id_contacts_labels`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_alliances_alliance_id_contacts_labels()

    @property
    def delete_characters_character_id_contacts(
        self,
    ) -> delete_characters_character_id_contacts:
        """
        Delete contacts


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Contacts.delete_characters_character_id_contacts.delete_characters_character_id_contacts.get_sync`,
        :func:`~EVECelery.tasks.ESI.Contacts.delete_characters_character_id_contacts.delete_characters_character_id_contacts.run`, and
        :class:`~EVECelery.tasks.ESI.Contacts.delete_characters_character_id_contacts.delete_characters_character_id_contacts`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return delete_characters_character_id_contacts()

    @property
    def get_characters_character_id_contacts(
        self,
    ) -> get_characters_character_id_contacts:
        """
        Get contacts


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Contacts.get_characters_character_id_contacts.get_characters_character_id_contacts.get_sync`,
        :func:`~EVECelery.tasks.ESI.Contacts.get_characters_character_id_contacts.get_characters_character_id_contacts.run`, and
        :class:`~EVECelery.tasks.ESI.Contacts.get_characters_character_id_contacts.get_characters_character_id_contacts`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_characters_character_id_contacts()

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

    @property
    def put_characters_character_id_contacts(
        self,
    ) -> put_characters_character_id_contacts:
        """
        Edit contacts


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Contacts.put_characters_character_id_contacts.put_characters_character_id_contacts.get_sync`,
        :func:`~EVECelery.tasks.ESI.Contacts.put_characters_character_id_contacts.put_characters_character_id_contacts.run`, and
        :class:`~EVECelery.tasks.ESI.Contacts.put_characters_character_id_contacts.put_characters_character_id_contacts`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return put_characters_character_id_contacts()

    @property
    def get_characters_character_id_contacts_labels(
        self,
    ) -> get_characters_character_id_contacts_labels:
        """
        Get contact labels


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Contacts.get_characters_character_id_contacts_labels.get_characters_character_id_contacts_labels.get_sync`,
        :func:`~EVECelery.tasks.ESI.Contacts.get_characters_character_id_contacts_labels.get_characters_character_id_contacts_labels.run`, and
        :class:`~EVECelery.tasks.ESI.Contacts.get_characters_character_id_contacts_labels.get_characters_character_id_contacts_labels`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_characters_character_id_contacts_labels()

    @property
    def get_corporations_corporation_id_contacts(
        self,
    ) -> get_corporations_corporation_id_contacts:
        """
        Get corporation contacts


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Contacts.get_corporations_corporation_id_contacts.get_corporations_corporation_id_contacts.get_sync`,
        :func:`~EVECelery.tasks.ESI.Contacts.get_corporations_corporation_id_contacts.get_corporations_corporation_id_contacts.run`, and
        :class:`~EVECelery.tasks.ESI.Contacts.get_corporations_corporation_id_contacts.get_corporations_corporation_id_contacts`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_corporations_corporation_id_contacts()

    @property
    def get_corporations_corporation_id_contacts_labels(
        self,
    ) -> get_corporations_corporation_id_contacts_labels:
        """
        Get corporation contact labels


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Contacts.get_corporations_corporation_id_contacts_labels.get_corporations_corporation_id_contacts_labels.get_sync`,
        :func:`~EVECelery.tasks.ESI.Contacts.get_corporations_corporation_id_contacts_labels.get_corporations_corporation_id_contacts_labels.run`, and
        :class:`~EVECelery.tasks.ESI.Contacts.get_corporations_corporation_id_contacts_labels.get_corporations_corporation_id_contacts_labels`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_corporations_corporation_id_contacts_labels()
