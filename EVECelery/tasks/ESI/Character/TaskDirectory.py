"""
Task directory module for adding task objects as attributes to a namespace for easy access and code inspection.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/TaskDirectory.py'.
"""

from .post_characters_affiliation import post_characters_affiliation
from .get_characters_character_id import get_characters_character_id
from .get_characters_character_id_agents_research import (
    get_characters_character_id_agents_research,
)
from .get_characters_character_id_blueprints import (
    get_characters_character_id_blueprints,
)
from .get_characters_character_id_corporationhistory import (
    get_characters_character_id_corporationhistory,
)
from .post_characters_character_id_cspa import post_characters_character_id_cspa
from .get_characters_character_id_fatigue import get_characters_character_id_fatigue
from .get_characters_character_id_medals import get_characters_character_id_medals
from .get_characters_character_id_notifications import (
    get_characters_character_id_notifications,
)
from .get_characters_character_id_notifications_contacts import (
    get_characters_character_id_notifications_contacts,
)
from .get_characters_character_id_portrait import get_characters_character_id_portrait
from .get_characters_character_id_roles import get_characters_character_id_roles
from .get_characters_character_id_standings import get_characters_character_id_standings
from .get_characters_character_id_titles import get_characters_character_id_titles


class TaskDirectory(object):
    """
    Directory for quickly finding tasks with easy access to documentation and code inspection

    This task directory contains all tasks as attributes that are categorized with 'Character'.
    """

    @property
    def post_characters_affiliation(self) -> post_characters_affiliation:
        """
        Character affiliation


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Character.post_characters_affiliation.post_characters_affiliation.get_sync`,
        :func:`~EVECelery.tasks.ESI.Character.post_characters_affiliation.post_characters_affiliation.run`, and
        :class:`~EVECelery.tasks.ESI.Character.post_characters_affiliation.post_characters_affiliation`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return post_characters_affiliation()

    @property
    def get_characters_character_id(self) -> get_characters_character_id:
        """
        Get character's public information


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Character.get_characters_character_id.get_characters_character_id.get_sync`,
        :func:`~EVECelery.tasks.ESI.Character.get_characters_character_id.get_characters_character_id.run`, and
        :class:`~EVECelery.tasks.ESI.Character.get_characters_character_id.get_characters_character_id`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_characters_character_id()

    @property
    def get_characters_character_id_agents_research(
        self,
    ) -> get_characters_character_id_agents_research:
        """
        Get agents research


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Character.get_characters_character_id_agents_research.get_characters_character_id_agents_research.get_sync`,
        :func:`~EVECelery.tasks.ESI.Character.get_characters_character_id_agents_research.get_characters_character_id_agents_research.run`, and
        :class:`~EVECelery.tasks.ESI.Character.get_characters_character_id_agents_research.get_characters_character_id_agents_research`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_characters_character_id_agents_research()

    @property
    def get_characters_character_id_blueprints(
        self,
    ) -> get_characters_character_id_blueprints:
        """
        Get blueprints


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Character.get_characters_character_id_blueprints.get_characters_character_id_blueprints.get_sync`,
        :func:`~EVECelery.tasks.ESI.Character.get_characters_character_id_blueprints.get_characters_character_id_blueprints.run`, and
        :class:`~EVECelery.tasks.ESI.Character.get_characters_character_id_blueprints.get_characters_character_id_blueprints`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_characters_character_id_blueprints()

    @property
    def get_characters_character_id_corporationhistory(
        self,
    ) -> get_characters_character_id_corporationhistory:
        """
        Get corporation history


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Character.get_characters_character_id_corporationhistory.get_characters_character_id_corporationhistory.get_sync`,
        :func:`~EVECelery.tasks.ESI.Character.get_characters_character_id_corporationhistory.get_characters_character_id_corporationhistory.run`, and
        :class:`~EVECelery.tasks.ESI.Character.get_characters_character_id_corporationhistory.get_characters_character_id_corporationhistory`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_characters_character_id_corporationhistory()

    @property
    def post_characters_character_id_cspa(self) -> post_characters_character_id_cspa:
        """
        Calculate a CSPA charge cost


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Character.post_characters_character_id_cspa.post_characters_character_id_cspa.get_sync`,
        :func:`~EVECelery.tasks.ESI.Character.post_characters_character_id_cspa.post_characters_character_id_cspa.run`, and
        :class:`~EVECelery.tasks.ESI.Character.post_characters_character_id_cspa.post_characters_character_id_cspa`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return post_characters_character_id_cspa()

    @property
    def get_characters_character_id_fatigue(
        self,
    ) -> get_characters_character_id_fatigue:
        """
        Get jump fatigue


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Character.get_characters_character_id_fatigue.get_characters_character_id_fatigue.get_sync`,
        :func:`~EVECelery.tasks.ESI.Character.get_characters_character_id_fatigue.get_characters_character_id_fatigue.run`, and
        :class:`~EVECelery.tasks.ESI.Character.get_characters_character_id_fatigue.get_characters_character_id_fatigue`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_characters_character_id_fatigue()

    @property
    def get_characters_character_id_medals(self) -> get_characters_character_id_medals:
        """
        Get medals


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Character.get_characters_character_id_medals.get_characters_character_id_medals.get_sync`,
        :func:`~EVECelery.tasks.ESI.Character.get_characters_character_id_medals.get_characters_character_id_medals.run`, and
        :class:`~EVECelery.tasks.ESI.Character.get_characters_character_id_medals.get_characters_character_id_medals`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_characters_character_id_medals()

    @property
    def get_characters_character_id_notifications(
        self,
    ) -> get_characters_character_id_notifications:
        """
        Get character notifications


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Character.get_characters_character_id_notifications.get_characters_character_id_notifications.get_sync`,
        :func:`~EVECelery.tasks.ESI.Character.get_characters_character_id_notifications.get_characters_character_id_notifications.run`, and
        :class:`~EVECelery.tasks.ESI.Character.get_characters_character_id_notifications.get_characters_character_id_notifications`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_characters_character_id_notifications()

    @property
    def get_characters_character_id_notifications_contacts(
        self,
    ) -> get_characters_character_id_notifications_contacts:
        """
        Get new contact notifications


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Character.get_characters_character_id_notifications_contacts.get_characters_character_id_notifications_contacts.get_sync`,
        :func:`~EVECelery.tasks.ESI.Character.get_characters_character_id_notifications_contacts.get_characters_character_id_notifications_contacts.run`, and
        :class:`~EVECelery.tasks.ESI.Character.get_characters_character_id_notifications_contacts.get_characters_character_id_notifications_contacts`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_characters_character_id_notifications_contacts()

    @property
    def get_characters_character_id_portrait(
        self,
    ) -> get_characters_character_id_portrait:
        """
        Get character portraits


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Character.get_characters_character_id_portrait.get_characters_character_id_portrait.get_sync`,
        :func:`~EVECelery.tasks.ESI.Character.get_characters_character_id_portrait.get_characters_character_id_portrait.run`, and
        :class:`~EVECelery.tasks.ESI.Character.get_characters_character_id_portrait.get_characters_character_id_portrait`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_characters_character_id_portrait()

    @property
    def get_characters_character_id_roles(self) -> get_characters_character_id_roles:
        """
        Get character corporation roles


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Character.get_characters_character_id_roles.get_characters_character_id_roles.get_sync`,
        :func:`~EVECelery.tasks.ESI.Character.get_characters_character_id_roles.get_characters_character_id_roles.run`, and
        :class:`~EVECelery.tasks.ESI.Character.get_characters_character_id_roles.get_characters_character_id_roles`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_characters_character_id_roles()

    @property
    def get_characters_character_id_standings(
        self,
    ) -> get_characters_character_id_standings:
        """
        Get standings


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Character.get_characters_character_id_standings.get_characters_character_id_standings.get_sync`,
        :func:`~EVECelery.tasks.ESI.Character.get_characters_character_id_standings.get_characters_character_id_standings.run`, and
        :class:`~EVECelery.tasks.ESI.Character.get_characters_character_id_standings.get_characters_character_id_standings`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_characters_character_id_standings()

    @property
    def get_characters_character_id_titles(self) -> get_characters_character_id_titles:
        """
        Get character corporation titles


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Character.get_characters_character_id_titles.get_characters_character_id_titles.get_sync`,
        :func:`~EVECelery.tasks.ESI.Character.get_characters_character_id_titles.get_characters_character_id_titles.run`, and
        :class:`~EVECelery.tasks.ESI.Character.get_characters_character_id_titles.get_characters_character_id_titles`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_characters_character_id_titles()
