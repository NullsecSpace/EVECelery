"""
Task directory module for adding task objects as attributes to a namespace for easy access and code inspection.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/TaskDirectory.py'.
"""

from .get_universe_schematics_schematic_id import get_universe_schematics_schematic_id


class TaskDirectory(object):
    """
    Directory for quickly finding tasks with easy access to documentation and code inspection

    This task directory contains all tasks as attributes that are categorized with 'PlanetaryInteraction'.
    """

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
