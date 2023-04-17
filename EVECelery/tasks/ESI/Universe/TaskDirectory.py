"""
Task directory module for adding task objects as attributes to a namespace for easy access and code inspection.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/TaskDirectory.py'.
"""

from .get_universe_categories import get_universe_categories
from .get_universe_categories_category_id import get_universe_categories_category_id
from .get_universe_constellations import get_universe_constellations
from .get_universe_graphics import get_universe_graphics
from .get_universe_graphics_graphic_id import get_universe_graphics_graphic_id
from .get_universe_groups import get_universe_groups
from .get_universe_groups_group_id import get_universe_groups_group_id
from .get_universe_regions import get_universe_regions
from .get_universe_regions_region_id import get_universe_regions_region_id
from .get_universe_stars_star_id import get_universe_stars_star_id
from .get_universe_structures import get_universe_structures
from .get_universe_systems import get_universe_systems
from .get_universe_types import get_universe_types


class TaskDirectory(object):
    """
    Directory for quickly finding tasks with easy access to documentation and code inspection

    This task directory contains all tasks as attributes that are categorized with 'Universe'.
    """

    @property
    def get_universe_categories(self) -> get_universe_categories:
        """
        Get item categories


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Universe.get_universe_categories.get_universe_categories.get_sync`,
        :func:`~EVECelery.tasks.ESI.Universe.get_universe_categories.get_universe_categories.run`, and
        :class:`~EVECelery.tasks.ESI.Universe.get_universe_categories.get_universe_categories`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_universe_categories()

    @property
    def get_universe_categories_category_id(
        self,
    ) -> get_universe_categories_category_id:
        """
        Get item category information


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Universe.get_universe_categories_category_id.get_universe_categories_category_id.get_sync`,
        :func:`~EVECelery.tasks.ESI.Universe.get_universe_categories_category_id.get_universe_categories_category_id.run`, and
        :class:`~EVECelery.tasks.ESI.Universe.get_universe_categories_category_id.get_universe_categories_category_id`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_universe_categories_category_id()

    @property
    def get_universe_constellations(self) -> get_universe_constellations:
        """
        Get constellations


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Universe.get_universe_constellations.get_universe_constellations.get_sync`,
        :func:`~EVECelery.tasks.ESI.Universe.get_universe_constellations.get_universe_constellations.run`, and
        :class:`~EVECelery.tasks.ESI.Universe.get_universe_constellations.get_universe_constellations`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_universe_constellations()

    @property
    def get_universe_graphics(self) -> get_universe_graphics:
        """
        Get graphics


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Universe.get_universe_graphics.get_universe_graphics.get_sync`,
        :func:`~EVECelery.tasks.ESI.Universe.get_universe_graphics.get_universe_graphics.run`, and
        :class:`~EVECelery.tasks.ESI.Universe.get_universe_graphics.get_universe_graphics`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_universe_graphics()

    @property
    def get_universe_graphics_graphic_id(self) -> get_universe_graphics_graphic_id:
        """
        Get graphic information


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Universe.get_universe_graphics_graphic_id.get_universe_graphics_graphic_id.get_sync`,
        :func:`~EVECelery.tasks.ESI.Universe.get_universe_graphics_graphic_id.get_universe_graphics_graphic_id.run`, and
        :class:`~EVECelery.tasks.ESI.Universe.get_universe_graphics_graphic_id.get_universe_graphics_graphic_id`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_universe_graphics_graphic_id()

    @property
    def get_universe_groups(self) -> get_universe_groups:
        """
        Get item groups


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Universe.get_universe_groups.get_universe_groups.get_sync`,
        :func:`~EVECelery.tasks.ESI.Universe.get_universe_groups.get_universe_groups.run`, and
        :class:`~EVECelery.tasks.ESI.Universe.get_universe_groups.get_universe_groups`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_universe_groups()

    @property
    def get_universe_groups_group_id(self) -> get_universe_groups_group_id:
        """
        Get item group information


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Universe.get_universe_groups_group_id.get_universe_groups_group_id.get_sync`,
        :func:`~EVECelery.tasks.ESI.Universe.get_universe_groups_group_id.get_universe_groups_group_id.run`, and
        :class:`~EVECelery.tasks.ESI.Universe.get_universe_groups_group_id.get_universe_groups_group_id`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_universe_groups_group_id()

    @property
    def get_universe_regions(self) -> get_universe_regions:
        """
        Get regions


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Universe.get_universe_regions.get_universe_regions.get_sync`,
        :func:`~EVECelery.tasks.ESI.Universe.get_universe_regions.get_universe_regions.run`, and
        :class:`~EVECelery.tasks.ESI.Universe.get_universe_regions.get_universe_regions`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_universe_regions()

    @property
    def get_universe_regions_region_id(self) -> get_universe_regions_region_id:
        """
        Get region information


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Universe.get_universe_regions_region_id.get_universe_regions_region_id.get_sync`,
        :func:`~EVECelery.tasks.ESI.Universe.get_universe_regions_region_id.get_universe_regions_region_id.run`, and
        :class:`~EVECelery.tasks.ESI.Universe.get_universe_regions_region_id.get_universe_regions_region_id`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_universe_regions_region_id()

    @property
    def get_universe_stars_star_id(self) -> get_universe_stars_star_id:
        """
        Get star information


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Universe.get_universe_stars_star_id.get_universe_stars_star_id.get_sync`,
        :func:`~EVECelery.tasks.ESI.Universe.get_universe_stars_star_id.get_universe_stars_star_id.run`, and
        :class:`~EVECelery.tasks.ESI.Universe.get_universe_stars_star_id.get_universe_stars_star_id`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_universe_stars_star_id()

    @property
    def get_universe_structures(self) -> get_universe_structures:
        """
        List all public structures


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Universe.get_universe_structures.get_universe_structures.get_sync`,
        :func:`~EVECelery.tasks.ESI.Universe.get_universe_structures.get_universe_structures.run`, and
        :class:`~EVECelery.tasks.ESI.Universe.get_universe_structures.get_universe_structures`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_universe_structures()

    @property
    def get_universe_systems(self) -> get_universe_systems:
        """
        Get solar systems


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Universe.get_universe_systems.get_universe_systems.get_sync`,
        :func:`~EVECelery.tasks.ESI.Universe.get_universe_systems.get_universe_systems.run`, and
        :class:`~EVECelery.tasks.ESI.Universe.get_universe_systems.get_universe_systems`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_universe_systems()

    @property
    def get_universe_types(self) -> get_universe_types:
        """
        Get types


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Universe.get_universe_types.get_universe_types.get_sync`,
        :func:`~EVECelery.tasks.ESI.Universe.get_universe_types.get_universe_types.run`, and
        :class:`~EVECelery.tasks.ESI.Universe.get_universe_types.get_universe_types`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_universe_types()
