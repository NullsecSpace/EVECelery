"""
Task directory module for adding task objects as attributes to a namespace for easy access and code inspection.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/TaskDirectory.py'.
"""

from .get_characters_character_id_orders import get_characters_character_id_orders
from .get_characters_character_id_orders_history import (
    get_characters_character_id_orders_history,
)
from .get_corporations_corporation_id_orders import (
    get_corporations_corporation_id_orders,
)
from .get_corporations_corporation_id_orders_history import (
    get_corporations_corporation_id_orders_history,
)
from .get_markets_groups import get_markets_groups
from .get_markets_groups_market_group_id import get_markets_groups_market_group_id
from .get_markets_prices import get_markets_prices
from .get_markets_structures_structure_id import get_markets_structures_structure_id
from .get_markets_region_id_history import get_markets_region_id_history
from .get_markets_region_id_orders import get_markets_region_id_orders
from .get_markets_region_id_types import get_markets_region_id_types


class TaskDirectory(object):
    """
    Directory for quickly finding tasks with easy access to documentation and code inspection

    This task directory contains all tasks as attributes that are categorized with 'Market'.
    """

    @property
    def get_characters_character_id_orders(self) -> get_characters_character_id_orders:
        """
        List open orders from a character


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Market.get_characters_character_id_orders.get_characters_character_id_orders.get_sync`,
        :func:`~EVECelery.tasks.ESI.Market.get_characters_character_id_orders.get_characters_character_id_orders.run`, and
        :class:`~EVECelery.tasks.ESI.Market.get_characters_character_id_orders.get_characters_character_id_orders`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_characters_character_id_orders()

    @property
    def get_characters_character_id_orders_history(
        self,
    ) -> get_characters_character_id_orders_history:
        """
        List historical orders by a character


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Market.get_characters_character_id_orders_history.get_characters_character_id_orders_history.get_sync`,
        :func:`~EVECelery.tasks.ESI.Market.get_characters_character_id_orders_history.get_characters_character_id_orders_history.run`, and
        :class:`~EVECelery.tasks.ESI.Market.get_characters_character_id_orders_history.get_characters_character_id_orders_history`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_characters_character_id_orders_history()

    @property
    def get_corporations_corporation_id_orders(
        self,
    ) -> get_corporations_corporation_id_orders:
        """
        List open orders from a corporation


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Market.get_corporations_corporation_id_orders.get_corporations_corporation_id_orders.get_sync`,
        :func:`~EVECelery.tasks.ESI.Market.get_corporations_corporation_id_orders.get_corporations_corporation_id_orders.run`, and
        :class:`~EVECelery.tasks.ESI.Market.get_corporations_corporation_id_orders.get_corporations_corporation_id_orders`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_corporations_corporation_id_orders()

    @property
    def get_corporations_corporation_id_orders_history(
        self,
    ) -> get_corporations_corporation_id_orders_history:
        """
        List historical orders from a corporation


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Market.get_corporations_corporation_id_orders_history.get_corporations_corporation_id_orders_history.get_sync`,
        :func:`~EVECelery.tasks.ESI.Market.get_corporations_corporation_id_orders_history.get_corporations_corporation_id_orders_history.run`, and
        :class:`~EVECelery.tasks.ESI.Market.get_corporations_corporation_id_orders_history.get_corporations_corporation_id_orders_history`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_corporations_corporation_id_orders_history()

    @property
    def get_markets_groups(self) -> get_markets_groups:
        """
        Get item groups


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Market.get_markets_groups.get_markets_groups.get_sync`,
        :func:`~EVECelery.tasks.ESI.Market.get_markets_groups.get_markets_groups.run`, and
        :class:`~EVECelery.tasks.ESI.Market.get_markets_groups.get_markets_groups`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_markets_groups()

    @property
    def get_markets_groups_market_group_id(self) -> get_markets_groups_market_group_id:
        """
        Get item group information


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Market.get_markets_groups_market_group_id.get_markets_groups_market_group_id.get_sync`,
        :func:`~EVECelery.tasks.ESI.Market.get_markets_groups_market_group_id.get_markets_groups_market_group_id.run`, and
        :class:`~EVECelery.tasks.ESI.Market.get_markets_groups_market_group_id.get_markets_groups_market_group_id`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_markets_groups_market_group_id()

    @property
    def get_markets_prices(self) -> get_markets_prices:
        """
        List market prices


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Market.get_markets_prices.get_markets_prices.get_sync`,
        :func:`~EVECelery.tasks.ESI.Market.get_markets_prices.get_markets_prices.run`, and
        :class:`~EVECelery.tasks.ESI.Market.get_markets_prices.get_markets_prices`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_markets_prices()

    @property
    def get_markets_structures_structure_id(
        self,
    ) -> get_markets_structures_structure_id:
        """
        List orders in a structure


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Market.get_markets_structures_structure_id.get_markets_structures_structure_id.get_sync`,
        :func:`~EVECelery.tasks.ESI.Market.get_markets_structures_structure_id.get_markets_structures_structure_id.run`, and
        :class:`~EVECelery.tasks.ESI.Market.get_markets_structures_structure_id.get_markets_structures_structure_id`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_markets_structures_structure_id()

    @property
    def get_markets_region_id_history(self) -> get_markets_region_id_history:
        """
        List historical market statistics in a region


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Market.get_markets_region_id_history.get_markets_region_id_history.get_sync`,
        :func:`~EVECelery.tasks.ESI.Market.get_markets_region_id_history.get_markets_region_id_history.run`, and
        :class:`~EVECelery.tasks.ESI.Market.get_markets_region_id_history.get_markets_region_id_history`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_markets_region_id_history()

    @property
    def get_markets_region_id_orders(self) -> get_markets_region_id_orders:
        """
        List orders in a region


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Market.get_markets_region_id_orders.get_markets_region_id_orders.get_sync`,
        :func:`~EVECelery.tasks.ESI.Market.get_markets_region_id_orders.get_markets_region_id_orders.run`, and
        :class:`~EVECelery.tasks.ESI.Market.get_markets_region_id_orders.get_markets_region_id_orders`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_markets_region_id_orders()

    @property
    def get_markets_region_id_types(self) -> get_markets_region_id_types:
        """
        List type IDs relevant to a market


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Market.get_markets_region_id_types.get_markets_region_id_types.get_sync`,
        :func:`~EVECelery.tasks.ESI.Market.get_markets_region_id_types.get_markets_region_id_types.run`, and
        :class:`~EVECelery.tasks.ESI.Market.get_markets_region_id_types.get_markets_region_id_types`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_markets_region_id_types()
