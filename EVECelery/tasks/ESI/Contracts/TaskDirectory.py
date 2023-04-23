"""
Task directory module for adding task objects as attributes to a namespace for easy access and code inspection.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/TaskDirectory.py'.
"""

from .get_characters_character_id_contracts import get_characters_character_id_contracts
from .get_characters_character_id_contracts_contract_id_bids import (
    get_characters_character_id_contracts_contract_id_bids,
)
from .get_characters_character_id_contracts_contract_id_items import (
    get_characters_character_id_contracts_contract_id_items,
)
from .get_contracts_public_bids_contract_id import get_contracts_public_bids_contract_id
from .get_contracts_public_items_contract_id import (
    get_contracts_public_items_contract_id,
)
from .get_contracts_public_region_id import get_contracts_public_region_id
from .get_corporations_corporation_id_contracts import (
    get_corporations_corporation_id_contracts,
)
from .get_corporations_corporation_id_contracts_contract_id_bids import (
    get_corporations_corporation_id_contracts_contract_id_bids,
)
from .get_corporations_corporation_id_contracts_contract_id_items import (
    get_corporations_corporation_id_contracts_contract_id_items,
)


class TaskDirectory(object):
    """
    Directory for quickly finding tasks with easy access to documentation and code inspection

    This task directory contains all tasks as attributes that are categorized with 'Contracts'.
    """

    @property
    def get_characters_character_id_contracts(
        self,
    ) -> get_characters_character_id_contracts:
        """
        Get contracts


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Contracts.get_characters_character_id_contracts.get_characters_character_id_contracts.get_sync`,
        :func:`~EVECelery.tasks.ESI.Contracts.get_characters_character_id_contracts.get_characters_character_id_contracts.run`, and
        :class:`~EVECelery.tasks.ESI.Contracts.get_characters_character_id_contracts.get_characters_character_id_contracts`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_characters_character_id_contracts()

    @property
    def get_characters_character_id_contracts_contract_id_bids(
        self,
    ) -> get_characters_character_id_contracts_contract_id_bids:
        """
        Get contract bids


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Contracts.get_characters_character_id_contracts_contract_id_bids.get_characters_character_id_contracts_contract_id_bids.get_sync`,
        :func:`~EVECelery.tasks.ESI.Contracts.get_characters_character_id_contracts_contract_id_bids.get_characters_character_id_contracts_contract_id_bids.run`, and
        :class:`~EVECelery.tasks.ESI.Contracts.get_characters_character_id_contracts_contract_id_bids.get_characters_character_id_contracts_contract_id_bids`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_characters_character_id_contracts_contract_id_bids()

    @property
    def get_characters_character_id_contracts_contract_id_items(
        self,
    ) -> get_characters_character_id_contracts_contract_id_items:
        """
        Get contract items


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Contracts.get_characters_character_id_contracts_contract_id_items.get_characters_character_id_contracts_contract_id_items.get_sync`,
        :func:`~EVECelery.tasks.ESI.Contracts.get_characters_character_id_contracts_contract_id_items.get_characters_character_id_contracts_contract_id_items.run`, and
        :class:`~EVECelery.tasks.ESI.Contracts.get_characters_character_id_contracts_contract_id_items.get_characters_character_id_contracts_contract_id_items`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_characters_character_id_contracts_contract_id_items()

    @property
    def get_contracts_public_bids_contract_id(
        self,
    ) -> get_contracts_public_bids_contract_id:
        """
        Get public contract bids


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Contracts.get_contracts_public_bids_contract_id.get_contracts_public_bids_contract_id.get_sync`,
        :func:`~EVECelery.tasks.ESI.Contracts.get_contracts_public_bids_contract_id.get_contracts_public_bids_contract_id.run`, and
        :class:`~EVECelery.tasks.ESI.Contracts.get_contracts_public_bids_contract_id.get_contracts_public_bids_contract_id`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_contracts_public_bids_contract_id()

    @property
    def get_contracts_public_items_contract_id(
        self,
    ) -> get_contracts_public_items_contract_id:
        """
        Get public contract items


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Contracts.get_contracts_public_items_contract_id.get_contracts_public_items_contract_id.get_sync`,
        :func:`~EVECelery.tasks.ESI.Contracts.get_contracts_public_items_contract_id.get_contracts_public_items_contract_id.run`, and
        :class:`~EVECelery.tasks.ESI.Contracts.get_contracts_public_items_contract_id.get_contracts_public_items_contract_id`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_contracts_public_items_contract_id()

    @property
    def get_contracts_public_region_id(self) -> get_contracts_public_region_id:
        """
        Get public contracts


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Contracts.get_contracts_public_region_id.get_contracts_public_region_id.get_sync`,
        :func:`~EVECelery.tasks.ESI.Contracts.get_contracts_public_region_id.get_contracts_public_region_id.run`, and
        :class:`~EVECelery.tasks.ESI.Contracts.get_contracts_public_region_id.get_contracts_public_region_id`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_contracts_public_region_id()

    @property
    def get_corporations_corporation_id_contracts(
        self,
    ) -> get_corporations_corporation_id_contracts:
        """
        Get corporation contracts


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Contracts.get_corporations_corporation_id_contracts.get_corporations_corporation_id_contracts.get_sync`,
        :func:`~EVECelery.tasks.ESI.Contracts.get_corporations_corporation_id_contracts.get_corporations_corporation_id_contracts.run`, and
        :class:`~EVECelery.tasks.ESI.Contracts.get_corporations_corporation_id_contracts.get_corporations_corporation_id_contracts`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_corporations_corporation_id_contracts()

    @property
    def get_corporations_corporation_id_contracts_contract_id_bids(
        self,
    ) -> get_corporations_corporation_id_contracts_contract_id_bids:
        """
        Get corporation contract bids


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Contracts.get_corporations_corporation_id_contracts_contract_id_bids.get_corporations_corporation_id_contracts_contract_id_bids.get_sync`,
        :func:`~EVECelery.tasks.ESI.Contracts.get_corporations_corporation_id_contracts_contract_id_bids.get_corporations_corporation_id_contracts_contract_id_bids.run`, and
        :class:`~EVECelery.tasks.ESI.Contracts.get_corporations_corporation_id_contracts_contract_id_bids.get_corporations_corporation_id_contracts_contract_id_bids`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_corporations_corporation_id_contracts_contract_id_bids()

    @property
    def get_corporations_corporation_id_contracts_contract_id_items(
        self,
    ) -> get_corporations_corporation_id_contracts_contract_id_items:
        """
        Get corporation contract items


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Contracts.get_corporations_corporation_id_contracts_contract_id_items.get_corporations_corporation_id_contracts_contract_id_items.get_sync`,
        :func:`~EVECelery.tasks.ESI.Contracts.get_corporations_corporation_id_contracts_contract_id_items.get_corporations_corporation_id_contracts_contract_id_items.run`, and
        :class:`~EVECelery.tasks.ESI.Contracts.get_corporations_corporation_id_contracts_contract_id_items.get_corporations_corporation_id_contracts_contract_id_items`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_corporations_corporation_id_contracts_contract_id_items()
