"""
Task directory module for adding task objects as attributes to a namespace for easy access and code inspection.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/TaskDirectory.py'.
"""

from .get_universe_ancestries import get_universe_ancestries
from .get_universe_asteroid_belts_asteroid_belt_id import (
    get_universe_asteroid_belts_asteroid_belt_id,
)
from .get_universe_bloodlines import get_universe_bloodlines
from .get_universe_categories import get_universe_categories
from .get_universe_categories_category_id import get_universe_categories_category_id
from .get_universe_constellations import get_universe_constellations
from .get_universe_constellations_constellation_id import (
    get_universe_constellations_constellation_id,
)
from .get_universe_factions import get_universe_factions
from .get_universe_graphics import get_universe_graphics
from .get_universe_graphics_graphic_id import get_universe_graphics_graphic_id
from .get_universe_groups import get_universe_groups
from .get_universe_groups_group_id import get_universe_groups_group_id
from .post_universe_ids import post_universe_ids
from .get_universe_moons_moon_id import get_universe_moons_moon_id
from .post_universe_names import post_universe_names
from .get_universe_planets_planet_id import get_universe_planets_planet_id
from .get_universe_races import get_universe_races
from .get_universe_regions import get_universe_regions
from .get_universe_regions_region_id import get_universe_regions_region_id
from .get_universe_stargates_stargate_id import get_universe_stargates_stargate_id
from .get_universe_stars_star_id import get_universe_stars_star_id
from .get_universe_stations_station_id import get_universe_stations_station_id
from .get_universe_structures import get_universe_structures
from .get_universe_structures_structure_id import get_universe_structures_structure_id
from .get_universe_system_jumps import get_universe_system_jumps
from .get_universe_system_kills import get_universe_system_kills
from .get_universe_systems import get_universe_systems
from .get_universe_systems_system_id import get_universe_systems_system_id
from .get_universe_types import get_universe_types
from .get_universe_types_type_id import get_universe_types_type_id


class TaskDirectory(object):
    """
    Directory for quickly finding tasks with easy access to documentation and code inspection

    This task directory contains all tasks as attributes that are categorized with 'Universe'.
    """

    @property
    def get_universe_ancestries(self) -> get_universe_ancestries:
        """
        Get ancestries


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Universe.get_universe_ancestries.get_universe_ancestries.get_sync`,
        :func:`~EVECelery.tasks.ESI.Universe.get_universe_ancestries.get_universe_ancestries.run`, and
        :class:`~EVECelery.tasks.ESI.Universe.get_universe_ancestries.get_universe_ancestries`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_universe_ancestries()

    @property
    def get_universe_asteroid_belts_asteroid_belt_id(
        self,
    ) -> get_universe_asteroid_belts_asteroid_belt_id:
        """
        Get asteroid belt information


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Universe.get_universe_asteroid_belts_asteroid_belt_id.get_universe_asteroid_belts_asteroid_belt_id.get_sync`,
        :func:`~EVECelery.tasks.ESI.Universe.get_universe_asteroid_belts_asteroid_belt_id.get_universe_asteroid_belts_asteroid_belt_id.run`, and
        :class:`~EVECelery.tasks.ESI.Universe.get_universe_asteroid_belts_asteroid_belt_id.get_universe_asteroid_belts_asteroid_belt_id`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_universe_asteroid_belts_asteroid_belt_id()

    @property
    def get_universe_bloodlines(self) -> get_universe_bloodlines:
        """
        Get bloodlines


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Universe.get_universe_bloodlines.get_universe_bloodlines.get_sync`,
        :func:`~EVECelery.tasks.ESI.Universe.get_universe_bloodlines.get_universe_bloodlines.run`, and
        :class:`~EVECelery.tasks.ESI.Universe.get_universe_bloodlines.get_universe_bloodlines`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_universe_bloodlines()

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
    def get_universe_constellations_constellation_id(
        self,
    ) -> get_universe_constellations_constellation_id:
        """
        Get constellation information


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Universe.get_universe_constellations_constellation_id.get_universe_constellations_constellation_id.get_sync`,
        :func:`~EVECelery.tasks.ESI.Universe.get_universe_constellations_constellation_id.get_universe_constellations_constellation_id.run`, and
        :class:`~EVECelery.tasks.ESI.Universe.get_universe_constellations_constellation_id.get_universe_constellations_constellation_id`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_universe_constellations_constellation_id()

    @property
    def get_universe_factions(self) -> get_universe_factions:
        """
        Get factions


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Universe.get_universe_factions.get_universe_factions.get_sync`,
        :func:`~EVECelery.tasks.ESI.Universe.get_universe_factions.get_universe_factions.run`, and
        :class:`~EVECelery.tasks.ESI.Universe.get_universe_factions.get_universe_factions`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_universe_factions()

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
    def post_universe_ids(self) -> post_universe_ids:
        """
        Bulk names to IDs


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Universe.post_universe_ids.post_universe_ids.get_sync`,
        :func:`~EVECelery.tasks.ESI.Universe.post_universe_ids.post_universe_ids.run`, and
        :class:`~EVECelery.tasks.ESI.Universe.post_universe_ids.post_universe_ids`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return post_universe_ids()

    @property
    def get_universe_moons_moon_id(self) -> get_universe_moons_moon_id:
        """
        Get moon information


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Universe.get_universe_moons_moon_id.get_universe_moons_moon_id.get_sync`,
        :func:`~EVECelery.tasks.ESI.Universe.get_universe_moons_moon_id.get_universe_moons_moon_id.run`, and
        :class:`~EVECelery.tasks.ESI.Universe.get_universe_moons_moon_id.get_universe_moons_moon_id`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_universe_moons_moon_id()

    @property
    def post_universe_names(self) -> post_universe_names:
        """
        Get names and categories for a set of IDs


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Universe.post_universe_names.post_universe_names.get_sync`,
        :func:`~EVECelery.tasks.ESI.Universe.post_universe_names.post_universe_names.run`, and
        :class:`~EVECelery.tasks.ESI.Universe.post_universe_names.post_universe_names`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return post_universe_names()

    @property
    def get_universe_planets_planet_id(self) -> get_universe_planets_planet_id:
        """
        Get planet information


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Universe.get_universe_planets_planet_id.get_universe_planets_planet_id.get_sync`,
        :func:`~EVECelery.tasks.ESI.Universe.get_universe_planets_planet_id.get_universe_planets_planet_id.run`, and
        :class:`~EVECelery.tasks.ESI.Universe.get_universe_planets_planet_id.get_universe_planets_planet_id`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_universe_planets_planet_id()

    @property
    def get_universe_races(self) -> get_universe_races:
        """
        Get character races


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Universe.get_universe_races.get_universe_races.get_sync`,
        :func:`~EVECelery.tasks.ESI.Universe.get_universe_races.get_universe_races.run`, and
        :class:`~EVECelery.tasks.ESI.Universe.get_universe_races.get_universe_races`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_universe_races()

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
    def get_universe_stargates_stargate_id(self) -> get_universe_stargates_stargate_id:
        """
        Get stargate information


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Universe.get_universe_stargates_stargate_id.get_universe_stargates_stargate_id.get_sync`,
        :func:`~EVECelery.tasks.ESI.Universe.get_universe_stargates_stargate_id.get_universe_stargates_stargate_id.run`, and
        :class:`~EVECelery.tasks.ESI.Universe.get_universe_stargates_stargate_id.get_universe_stargates_stargate_id`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_universe_stargates_stargate_id()

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
    def get_universe_stations_station_id(self) -> get_universe_stations_station_id:
        """
        Get station information


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Universe.get_universe_stations_station_id.get_universe_stations_station_id.get_sync`,
        :func:`~EVECelery.tasks.ESI.Universe.get_universe_stations_station_id.get_universe_stations_station_id.run`, and
        :class:`~EVECelery.tasks.ESI.Universe.get_universe_stations_station_id.get_universe_stations_station_id`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_universe_stations_station_id()

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
    def get_universe_structures_structure_id(
        self,
    ) -> get_universe_structures_structure_id:
        """
        Get structure information


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Universe.get_universe_structures_structure_id.get_universe_structures_structure_id.get_sync`,
        :func:`~EVECelery.tasks.ESI.Universe.get_universe_structures_structure_id.get_universe_structures_structure_id.run`, and
        :class:`~EVECelery.tasks.ESI.Universe.get_universe_structures_structure_id.get_universe_structures_structure_id`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_universe_structures_structure_id()

    @property
    def get_universe_system_jumps(self) -> get_universe_system_jumps:
        """
        Get system jumps


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Universe.get_universe_system_jumps.get_universe_system_jumps.get_sync`,
        :func:`~EVECelery.tasks.ESI.Universe.get_universe_system_jumps.get_universe_system_jumps.run`, and
        :class:`~EVECelery.tasks.ESI.Universe.get_universe_system_jumps.get_universe_system_jumps`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_universe_system_jumps()

    @property
    def get_universe_system_kills(self) -> get_universe_system_kills:
        """
        Get system kills


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Universe.get_universe_system_kills.get_universe_system_kills.get_sync`,
        :func:`~EVECelery.tasks.ESI.Universe.get_universe_system_kills.get_universe_system_kills.run`, and
        :class:`~EVECelery.tasks.ESI.Universe.get_universe_system_kills.get_universe_system_kills`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_universe_system_kills()

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
    def get_universe_systems_system_id(self) -> get_universe_systems_system_id:
        """
        Get solar system information


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Universe.get_universe_systems_system_id.get_universe_systems_system_id.get_sync`,
        :func:`~EVECelery.tasks.ESI.Universe.get_universe_systems_system_id.get_universe_systems_system_id.run`, and
        :class:`~EVECelery.tasks.ESI.Universe.get_universe_systems_system_id.get_universe_systems_system_id`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_universe_systems_system_id()

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

    @property
    def get_universe_types_type_id(self) -> get_universe_types_type_id:
        """
        Get type information


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Universe.get_universe_types_type_id.get_universe_types_type_id.get_sync`,
        :func:`~EVECelery.tasks.ESI.Universe.get_universe_types_type_id.get_universe_types_type_id.run`, and
        :class:`~EVECelery.tasks.ESI.Universe.get_universe_types_type_id.get_universe_types_type_id`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_universe_types_type_id()
