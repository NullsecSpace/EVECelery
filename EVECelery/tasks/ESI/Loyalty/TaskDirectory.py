"""
Task directory module for adding task objects as attributes to a namespace for easy access and code inspection.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/TaskDirectory.py'.
"""

from .get_characters_character_id_loyalty_points import (
    get_characters_character_id_loyalty_points,
)
from .get_loyalty_stores_corporation_id_offers import (
    get_loyalty_stores_corporation_id_offers,
)


class TaskDirectory(object):
    """
    Directory for quickly finding tasks with easy access to documentation and code inspection

    This task directory contains all tasks as attributes that are categorized with 'Loyalty'.
    """

    @property
    def get_characters_character_id_loyalty_points(
        self,
    ) -> get_characters_character_id_loyalty_points:
        """
        Get loyalty points


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Loyalty.get_characters_character_id_loyalty_points.get_characters_character_id_loyalty_points.get_sync`,
        :func:`~EVECelery.tasks.ESI.Loyalty.get_characters_character_id_loyalty_points.get_characters_character_id_loyalty_points.run`, and
        :class:`~EVECelery.tasks.ESI.Loyalty.get_characters_character_id_loyalty_points.get_characters_character_id_loyalty_points`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_characters_character_id_loyalty_points()

    @property
    def get_loyalty_stores_corporation_id_offers(
        self,
    ) -> get_loyalty_stores_corporation_id_offers:
        """
        List loyalty store offers


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Loyalty.get_loyalty_stores_corporation_id_offers.get_loyalty_stores_corporation_id_offers.get_sync`,
        :func:`~EVECelery.tasks.ESI.Loyalty.get_loyalty_stores_corporation_id_offers.get_loyalty_stores_corporation_id_offers.run`, and
        :class:`~EVECelery.tasks.ESI.Loyalty.get_loyalty_stores_corporation_id_offers.get_loyalty_stores_corporation_id_offers`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_loyalty_stores_corporation_id_offers()
