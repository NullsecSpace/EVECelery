"""
Task directory module for adding task objects as attributes to a namespace for easy access and code inspection.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/TaskDirectory.py'.
"""

from .get_markets_groups import get_markets_groups
from .get_markets_groups_market_group_id import get_markets_groups_market_group_id
from .get_markets_region_id_types import get_markets_region_id_types


class TaskDirectory(object):
    """
    Directory for quickly finding tasks with easy access to documentation and code inspection

    This task directory contains all tasks as attributes that are categorized with 'Market'.
    """

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
