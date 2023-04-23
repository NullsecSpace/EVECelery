"""
Task directory module for adding task objects as attributes to a namespace for easy access and code inspection.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/TaskDirectory.py'.
"""

from .get_characters_character_id_assets import get_characters_character_id_assets
from .post_characters_character_id_assets_locations import (
    post_characters_character_id_assets_locations,
)
from .post_characters_character_id_assets_names import (
    post_characters_character_id_assets_names,
)
from .get_corporations_corporation_id_assets import (
    get_corporations_corporation_id_assets,
)
from .post_corporations_corporation_id_assets_locations import (
    post_corporations_corporation_id_assets_locations,
)
from .post_corporations_corporation_id_assets_names import (
    post_corporations_corporation_id_assets_names,
)


class TaskDirectory(object):
    """
    Directory for quickly finding tasks with easy access to documentation and code inspection

    This task directory contains all tasks as attributes that are categorized with 'Assets'.
    """

    @property
    def get_characters_character_id_assets(self) -> get_characters_character_id_assets:
        """
        Get character assets


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Assets.get_characters_character_id_assets.get_characters_character_id_assets.get_sync`,
        :func:`~EVECelery.tasks.ESI.Assets.get_characters_character_id_assets.get_characters_character_id_assets.run`, and
        :class:`~EVECelery.tasks.ESI.Assets.get_characters_character_id_assets.get_characters_character_id_assets`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_characters_character_id_assets()

    @property
    def post_characters_character_id_assets_locations(
        self,
    ) -> post_characters_character_id_assets_locations:
        """
        Get character asset locations


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Assets.post_characters_character_id_assets_locations.post_characters_character_id_assets_locations.get_sync`,
        :func:`~EVECelery.tasks.ESI.Assets.post_characters_character_id_assets_locations.post_characters_character_id_assets_locations.run`, and
        :class:`~EVECelery.tasks.ESI.Assets.post_characters_character_id_assets_locations.post_characters_character_id_assets_locations`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return post_characters_character_id_assets_locations()

    @property
    def post_characters_character_id_assets_names(
        self,
    ) -> post_characters_character_id_assets_names:
        """
        Get character asset names


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Assets.post_characters_character_id_assets_names.post_characters_character_id_assets_names.get_sync`,
        :func:`~EVECelery.tasks.ESI.Assets.post_characters_character_id_assets_names.post_characters_character_id_assets_names.run`, and
        :class:`~EVECelery.tasks.ESI.Assets.post_characters_character_id_assets_names.post_characters_character_id_assets_names`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return post_characters_character_id_assets_names()

    @property
    def get_corporations_corporation_id_assets(
        self,
    ) -> get_corporations_corporation_id_assets:
        """
        Get corporation assets


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Assets.get_corporations_corporation_id_assets.get_corporations_corporation_id_assets.get_sync`,
        :func:`~EVECelery.tasks.ESI.Assets.get_corporations_corporation_id_assets.get_corporations_corporation_id_assets.run`, and
        :class:`~EVECelery.tasks.ESI.Assets.get_corporations_corporation_id_assets.get_corporations_corporation_id_assets`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_corporations_corporation_id_assets()

    @property
    def post_corporations_corporation_id_assets_locations(
        self,
    ) -> post_corporations_corporation_id_assets_locations:
        """
        Get corporation asset locations


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Assets.post_corporations_corporation_id_assets_locations.post_corporations_corporation_id_assets_locations.get_sync`,
        :func:`~EVECelery.tasks.ESI.Assets.post_corporations_corporation_id_assets_locations.post_corporations_corporation_id_assets_locations.run`, and
        :class:`~EVECelery.tasks.ESI.Assets.post_corporations_corporation_id_assets_locations.post_corporations_corporation_id_assets_locations`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return post_corporations_corporation_id_assets_locations()

    @property
    def post_corporations_corporation_id_assets_names(
        self,
    ) -> post_corporations_corporation_id_assets_names:
        """
        Get corporation asset names


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Assets.post_corporations_corporation_id_assets_names.post_corporations_corporation_id_assets_names.get_sync`,
        :func:`~EVECelery.tasks.ESI.Assets.post_corporations_corporation_id_assets_names.post_corporations_corporation_id_assets_names.run`, and
        :class:`~EVECelery.tasks.ESI.Assets.post_corporations_corporation_id_assets_names.post_corporations_corporation_id_assets_names`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return post_corporations_corporation_id_assets_names()
