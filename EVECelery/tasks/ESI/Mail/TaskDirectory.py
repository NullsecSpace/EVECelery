"""
Task directory module for adding task objects as attributes to a namespace for easy access and code inspection.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/TaskDirectory.py'.
"""

from .get_characters_character_id_mail import get_characters_character_id_mail
from .get_characters_character_id_mail_labels import (
    get_characters_character_id_mail_labels,
)
from .delete_characters_character_id_mail_labels_label_id import (
    delete_characters_character_id_mail_labels_label_id,
)
from .get_characters_character_id_mail_lists import (
    get_characters_character_id_mail_lists,
)
from .delete_characters_character_id_mail_mail_id import (
    delete_characters_character_id_mail_mail_id,
)
from .get_characters_character_id_mail_mail_id import (
    get_characters_character_id_mail_mail_id,
)


class TaskDirectory(object):
    """
    Directory for quickly finding tasks with easy access to documentation and code inspection

    This task directory contains all tasks as attributes that are categorized with 'Mail'.
    """

    @property
    def get_characters_character_id_mail(self) -> get_characters_character_id_mail:
        """
        Return mail headers


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Mail.get_characters_character_id_mail.get_characters_character_id_mail.get_sync`,
        :func:`~EVECelery.tasks.ESI.Mail.get_characters_character_id_mail.get_characters_character_id_mail.run`, and
        :class:`~EVECelery.tasks.ESI.Mail.get_characters_character_id_mail.get_characters_character_id_mail`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_characters_character_id_mail()

    @property
    def get_characters_character_id_mail_labels(
        self,
    ) -> get_characters_character_id_mail_labels:
        """
        Get mail labels and unread counts


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Mail.get_characters_character_id_mail_labels.get_characters_character_id_mail_labels.get_sync`,
        :func:`~EVECelery.tasks.ESI.Mail.get_characters_character_id_mail_labels.get_characters_character_id_mail_labels.run`, and
        :class:`~EVECelery.tasks.ESI.Mail.get_characters_character_id_mail_labels.get_characters_character_id_mail_labels`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_characters_character_id_mail_labels()

    @property
    def delete_characters_character_id_mail_labels_label_id(
        self,
    ) -> delete_characters_character_id_mail_labels_label_id:
        """
        Delete a mail label


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Mail.delete_characters_character_id_mail_labels_label_id.delete_characters_character_id_mail_labels_label_id.get_sync`,
        :func:`~EVECelery.tasks.ESI.Mail.delete_characters_character_id_mail_labels_label_id.delete_characters_character_id_mail_labels_label_id.run`, and
        :class:`~EVECelery.tasks.ESI.Mail.delete_characters_character_id_mail_labels_label_id.delete_characters_character_id_mail_labels_label_id`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return delete_characters_character_id_mail_labels_label_id()

    @property
    def get_characters_character_id_mail_lists(
        self,
    ) -> get_characters_character_id_mail_lists:
        """
        Return mailing list subscriptions


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Mail.get_characters_character_id_mail_lists.get_characters_character_id_mail_lists.get_sync`,
        :func:`~EVECelery.tasks.ESI.Mail.get_characters_character_id_mail_lists.get_characters_character_id_mail_lists.run`, and
        :class:`~EVECelery.tasks.ESI.Mail.get_characters_character_id_mail_lists.get_characters_character_id_mail_lists`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_characters_character_id_mail_lists()

    @property
    def delete_characters_character_id_mail_mail_id(
        self,
    ) -> delete_characters_character_id_mail_mail_id:
        """
        Delete a mail


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Mail.delete_characters_character_id_mail_mail_id.delete_characters_character_id_mail_mail_id.get_sync`,
        :func:`~EVECelery.tasks.ESI.Mail.delete_characters_character_id_mail_mail_id.delete_characters_character_id_mail_mail_id.run`, and
        :class:`~EVECelery.tasks.ESI.Mail.delete_characters_character_id_mail_mail_id.delete_characters_character_id_mail_mail_id`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return delete_characters_character_id_mail_mail_id()

    @property
    def get_characters_character_id_mail_mail_id(
        self,
    ) -> get_characters_character_id_mail_mail_id:
        """
        Return a mail


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Mail.get_characters_character_id_mail_mail_id.get_characters_character_id_mail_mail_id.get_sync`,
        :func:`~EVECelery.tasks.ESI.Mail.get_characters_character_id_mail_mail_id.get_characters_character_id_mail_mail_id.run`, and
        :class:`~EVECelery.tasks.ESI.Mail.get_characters_character_id_mail_mail_id.get_characters_character_id_mail_mail_id`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_characters_character_id_mail_mail_id()
