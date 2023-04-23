"""
Task directory module for adding task objects as attributes to a namespace for easy access and code inspection.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/TaskDirectory.py'.
"""

from .get_characters_character_id_planets import get_characters_character_id_planets
from .get_characters_character_id_planets_planet_id import (
    get_characters_character_id_planets_planet_id,
)
from .get_corporations_corporation_id_customs_offices import (
    get_corporations_corporation_id_customs_offices,
)
from .get_universe_schematics_schematic_id import get_universe_schematics_schematic_id


class TaskDirectory(object):
    """
    Directory for quickly finding tasks with easy access to documentation and code inspection

    This task directory contains all tasks as attributes that are categorized with 'PlanetaryInteraction'.
    """

    @property
    def get_characters_character_id_planets(
        self,
    ) -> get_characters_character_id_planets:
        """
        Get colonies


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.PlanetaryInteraction.get_characters_character_id_planets.get_characters_character_id_planets.get_sync`,
        :func:`~EVECelery.tasks.ESI.PlanetaryInteraction.get_characters_character_id_planets.get_characters_character_id_planets.run`, and
        :class:`~EVECelery.tasks.ESI.PlanetaryInteraction.get_characters_character_id_planets.get_characters_character_id_planets`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_characters_character_id_planets()

    @property
    def get_characters_character_id_planets_planet_id(
        self,
    ) -> get_characters_character_id_planets_planet_id:
        """
        Get colony layout


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.PlanetaryInteraction.get_characters_character_id_planets_planet_id.get_characters_character_id_planets_planet_id.get_sync`,
        :func:`~EVECelery.tasks.ESI.PlanetaryInteraction.get_characters_character_id_planets_planet_id.get_characters_character_id_planets_planet_id.run`, and
        :class:`~EVECelery.tasks.ESI.PlanetaryInteraction.get_characters_character_id_planets_planet_id.get_characters_character_id_planets_planet_id`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_characters_character_id_planets_planet_id()

    @property
    def get_corporations_corporation_id_customs_offices(
        self,
    ) -> get_corporations_corporation_id_customs_offices:
        """
        List corporation customs offices


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.PlanetaryInteraction.get_corporations_corporation_id_customs_offices.get_corporations_corporation_id_customs_offices.get_sync`,
        :func:`~EVECelery.tasks.ESI.PlanetaryInteraction.get_corporations_corporation_id_customs_offices.get_corporations_corporation_id_customs_offices.run`, and
        :class:`~EVECelery.tasks.ESI.PlanetaryInteraction.get_corporations_corporation_id_customs_offices.get_corporations_corporation_id_customs_offices`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_corporations_corporation_id_customs_offices()

    @property
    def get_universe_schematics_schematic_id(
        self,
    ) -> get_universe_schematics_schematic_id:
        """
        Get schematic information


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.PlanetaryInteraction.get_universe_schematics_schematic_id.get_universe_schematics_schematic_id.get_sync`,
        :func:`~EVECelery.tasks.ESI.PlanetaryInteraction.get_universe_schematics_schematic_id.get_universe_schematics_schematic_id.run`, and
        :class:`~EVECelery.tasks.ESI.PlanetaryInteraction.get_universe_schematics_schematic_id.get_universe_schematics_schematic_id`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_universe_schematics_schematic_id()
