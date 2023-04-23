"""
Task directory module for adding task objects as attributes to a namespace for easy access and code inspection.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/TaskDirectory.py'.
"""

from .get_characters_character_id_wallet import get_characters_character_id_wallet
from .get_characters_character_id_wallet_journal import (
    get_characters_character_id_wallet_journal,
)
from .get_characters_character_id_wallet_transactions import (
    get_characters_character_id_wallet_transactions,
)
from .get_corporations_corporation_id_wallets import (
    get_corporations_corporation_id_wallets,
)
from .get_corporations_corporation_id_wallets_division_journal import (
    get_corporations_corporation_id_wallets_division_journal,
)
from .get_corporations_corporation_id_wallets_division_transactions import (
    get_corporations_corporation_id_wallets_division_transactions,
)


class TaskDirectory(object):
    """
    Directory for quickly finding tasks with easy access to documentation and code inspection

    This task directory contains all tasks as attributes that are categorized with 'Wallet'.
    """

    @property
    def get_characters_character_id_wallet(self) -> get_characters_character_id_wallet:
        """
        Get a character's wallet balance


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Wallet.get_characters_character_id_wallet.get_characters_character_id_wallet.get_sync`,
        :func:`~EVECelery.tasks.ESI.Wallet.get_characters_character_id_wallet.get_characters_character_id_wallet.run`, and
        :class:`~EVECelery.tasks.ESI.Wallet.get_characters_character_id_wallet.get_characters_character_id_wallet`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_characters_character_id_wallet()

    @property
    def get_characters_character_id_wallet_journal(
        self,
    ) -> get_characters_character_id_wallet_journal:
        """
        Get character wallet journal


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Wallet.get_characters_character_id_wallet_journal.get_characters_character_id_wallet_journal.get_sync`,
        :func:`~EVECelery.tasks.ESI.Wallet.get_characters_character_id_wallet_journal.get_characters_character_id_wallet_journal.run`, and
        :class:`~EVECelery.tasks.ESI.Wallet.get_characters_character_id_wallet_journal.get_characters_character_id_wallet_journal`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_characters_character_id_wallet_journal()

    @property
    def get_characters_character_id_wallet_transactions(
        self,
    ) -> get_characters_character_id_wallet_transactions:
        """
        Get wallet transactions


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Wallet.get_characters_character_id_wallet_transactions.get_characters_character_id_wallet_transactions.get_sync`,
        :func:`~EVECelery.tasks.ESI.Wallet.get_characters_character_id_wallet_transactions.get_characters_character_id_wallet_transactions.run`, and
        :class:`~EVECelery.tasks.ESI.Wallet.get_characters_character_id_wallet_transactions.get_characters_character_id_wallet_transactions`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_characters_character_id_wallet_transactions()

    @property
    def get_corporations_corporation_id_wallets(
        self,
    ) -> get_corporations_corporation_id_wallets:
        """
        Returns a corporation's wallet balance


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Wallet.get_corporations_corporation_id_wallets.get_corporations_corporation_id_wallets.get_sync`,
        :func:`~EVECelery.tasks.ESI.Wallet.get_corporations_corporation_id_wallets.get_corporations_corporation_id_wallets.run`, and
        :class:`~EVECelery.tasks.ESI.Wallet.get_corporations_corporation_id_wallets.get_corporations_corporation_id_wallets`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_corporations_corporation_id_wallets()

    @property
    def get_corporations_corporation_id_wallets_division_journal(
        self,
    ) -> get_corporations_corporation_id_wallets_division_journal:
        """
        Get corporation wallet journal


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Wallet.get_corporations_corporation_id_wallets_division_journal.get_corporations_corporation_id_wallets_division_journal.get_sync`,
        :func:`~EVECelery.tasks.ESI.Wallet.get_corporations_corporation_id_wallets_division_journal.get_corporations_corporation_id_wallets_division_journal.run`, and
        :class:`~EVECelery.tasks.ESI.Wallet.get_corporations_corporation_id_wallets_division_journal.get_corporations_corporation_id_wallets_division_journal`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_corporations_corporation_id_wallets_division_journal()

    @property
    def get_corporations_corporation_id_wallets_division_transactions(
        self,
    ) -> get_corporations_corporation_id_wallets_division_transactions:
        """
        Get corporation wallet transactions


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Wallet.get_corporations_corporation_id_wallets_division_transactions.get_corporations_corporation_id_wallets_division_transactions.get_sync`,
        :func:`~EVECelery.tasks.ESI.Wallet.get_corporations_corporation_id_wallets_division_transactions.get_corporations_corporation_id_wallets_division_transactions.run`, and
        :class:`~EVECelery.tasks.ESI.Wallet.get_corporations_corporation_id_wallets_division_transactions.get_corporations_corporation_id_wallets_division_transactions`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_corporations_corporation_id_wallets_division_transactions()
