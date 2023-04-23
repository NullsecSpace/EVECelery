"""
Task directory module for adding task objects as attributes to a namespace for easy access and code inspection.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/TaskDirectory.py'.
"""

from .get_characters_character_id_industry_jobs import (
    get_characters_character_id_industry_jobs,
)
from .get_characters_character_id_mining import get_characters_character_id_mining
from .get_corporation_corporation_id_mining_extractions import (
    get_corporation_corporation_id_mining_extractions,
)
from .get_corporation_corporation_id_mining_observers import (
    get_corporation_corporation_id_mining_observers,
)
from .get_corporation_corporation_id_mining_observers_observer_id import (
    get_corporation_corporation_id_mining_observers_observer_id,
)
from .get_corporations_corporation_id_industry_jobs import (
    get_corporations_corporation_id_industry_jobs,
)
from .get_industry_facilities import get_industry_facilities
from .get_industry_systems import get_industry_systems


class TaskDirectory(object):
    """
    Directory for quickly finding tasks with easy access to documentation and code inspection

    This task directory contains all tasks as attributes that are categorized with 'Industry'.
    """

    @property
    def get_characters_character_id_industry_jobs(
        self,
    ) -> get_characters_character_id_industry_jobs:
        """
        List character industry jobs


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Industry.get_characters_character_id_industry_jobs.get_characters_character_id_industry_jobs.get_sync`,
        :func:`~EVECelery.tasks.ESI.Industry.get_characters_character_id_industry_jobs.get_characters_character_id_industry_jobs.run`, and
        :class:`~EVECelery.tasks.ESI.Industry.get_characters_character_id_industry_jobs.get_characters_character_id_industry_jobs`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_characters_character_id_industry_jobs()

    @property
    def get_characters_character_id_mining(self) -> get_characters_character_id_mining:
        """
        Character mining ledger


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Industry.get_characters_character_id_mining.get_characters_character_id_mining.get_sync`,
        :func:`~EVECelery.tasks.ESI.Industry.get_characters_character_id_mining.get_characters_character_id_mining.run`, and
        :class:`~EVECelery.tasks.ESI.Industry.get_characters_character_id_mining.get_characters_character_id_mining`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_characters_character_id_mining()

    @property
    def get_corporation_corporation_id_mining_extractions(
        self,
    ) -> get_corporation_corporation_id_mining_extractions:
        """
        Moon extraction timers


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Industry.get_corporation_corporation_id_mining_extractions.get_corporation_corporation_id_mining_extractions.get_sync`,
        :func:`~EVECelery.tasks.ESI.Industry.get_corporation_corporation_id_mining_extractions.get_corporation_corporation_id_mining_extractions.run`, and
        :class:`~EVECelery.tasks.ESI.Industry.get_corporation_corporation_id_mining_extractions.get_corporation_corporation_id_mining_extractions`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_corporation_corporation_id_mining_extractions()

    @property
    def get_corporation_corporation_id_mining_observers(
        self,
    ) -> get_corporation_corporation_id_mining_observers:
        """
        Corporation mining observers


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Industry.get_corporation_corporation_id_mining_observers.get_corporation_corporation_id_mining_observers.get_sync`,
        :func:`~EVECelery.tasks.ESI.Industry.get_corporation_corporation_id_mining_observers.get_corporation_corporation_id_mining_observers.run`, and
        :class:`~EVECelery.tasks.ESI.Industry.get_corporation_corporation_id_mining_observers.get_corporation_corporation_id_mining_observers`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_corporation_corporation_id_mining_observers()

    @property
    def get_corporation_corporation_id_mining_observers_observer_id(
        self,
    ) -> get_corporation_corporation_id_mining_observers_observer_id:
        """
        Observed corporation mining


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Industry.get_corporation_corporation_id_mining_observers_observer_id.get_corporation_corporation_id_mining_observers_observer_id.get_sync`,
        :func:`~EVECelery.tasks.ESI.Industry.get_corporation_corporation_id_mining_observers_observer_id.get_corporation_corporation_id_mining_observers_observer_id.run`, and
        :class:`~EVECelery.tasks.ESI.Industry.get_corporation_corporation_id_mining_observers_observer_id.get_corporation_corporation_id_mining_observers_observer_id`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_corporation_corporation_id_mining_observers_observer_id()

    @property
    def get_corporations_corporation_id_industry_jobs(
        self,
    ) -> get_corporations_corporation_id_industry_jobs:
        """
        List corporation industry jobs


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Industry.get_corporations_corporation_id_industry_jobs.get_corporations_corporation_id_industry_jobs.get_sync`,
        :func:`~EVECelery.tasks.ESI.Industry.get_corporations_corporation_id_industry_jobs.get_corporations_corporation_id_industry_jobs.run`, and
        :class:`~EVECelery.tasks.ESI.Industry.get_corporations_corporation_id_industry_jobs.get_corporations_corporation_id_industry_jobs`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_corporations_corporation_id_industry_jobs()

    @property
    def get_industry_facilities(self) -> get_industry_facilities:
        """
        List industry facilities


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Industry.get_industry_facilities.get_industry_facilities.get_sync`,
        :func:`~EVECelery.tasks.ESI.Industry.get_industry_facilities.get_industry_facilities.run`, and
        :class:`~EVECelery.tasks.ESI.Industry.get_industry_facilities.get_industry_facilities`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_industry_facilities()

    @property
    def get_industry_systems(self) -> get_industry_systems:
        """
        List solar system cost indices


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Industry.get_industry_systems.get_industry_systems.get_sync`,
        :func:`~EVECelery.tasks.ESI.Industry.get_industry_systems.get_industry_systems.run`, and
        :class:`~EVECelery.tasks.ESI.Industry.get_industry_systems.get_industry_systems`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_industry_systems()
