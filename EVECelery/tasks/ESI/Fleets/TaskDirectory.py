"""
Task directory module for adding task objects as attributes to a namespace for easy access and code inspection.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/TaskDirectory.py'.
"""

from .get_characters_character_id_fleet import get_characters_character_id_fleet
from .get_fleets_fleet_id import get_fleets_fleet_id
from .get_fleets_fleet_id_members import get_fleets_fleet_id_members
from .delete_fleets_fleet_id_members_member_id import (
    delete_fleets_fleet_id_members_member_id,
)
from .delete_fleets_fleet_id_squads_squad_id import (
    delete_fleets_fleet_id_squads_squad_id,
)
from .get_fleets_fleet_id_wings import get_fleets_fleet_id_wings
from .post_fleets_fleet_id_wings import post_fleets_fleet_id_wings
from .delete_fleets_fleet_id_wings_wing_id import delete_fleets_fleet_id_wings_wing_id
from .post_fleets_fleet_id_wings_wing_id_squads import (
    post_fleets_fleet_id_wings_wing_id_squads,
)


class TaskDirectory(object):
    """
    Directory for quickly finding tasks with easy access to documentation and code inspection

    This task directory contains all tasks as attributes that are categorized with 'Fleets'.
    """

    @property
    def get_characters_character_id_fleet(self) -> get_characters_character_id_fleet:
        """
        Get character fleet info


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Fleets.get_characters_character_id_fleet.get_characters_character_id_fleet.get_sync`,
        :func:`~EVECelery.tasks.ESI.Fleets.get_characters_character_id_fleet.get_characters_character_id_fleet.run`, and
        :class:`~EVECelery.tasks.ESI.Fleets.get_characters_character_id_fleet.get_characters_character_id_fleet`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_characters_character_id_fleet()

    @property
    def get_fleets_fleet_id(self) -> get_fleets_fleet_id:
        """
        Get fleet information


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Fleets.get_fleets_fleet_id.get_fleets_fleet_id.get_sync`,
        :func:`~EVECelery.tasks.ESI.Fleets.get_fleets_fleet_id.get_fleets_fleet_id.run`, and
        :class:`~EVECelery.tasks.ESI.Fleets.get_fleets_fleet_id.get_fleets_fleet_id`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_fleets_fleet_id()

    @property
    def get_fleets_fleet_id_members(self) -> get_fleets_fleet_id_members:
        """
        Get fleet members


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Fleets.get_fleets_fleet_id_members.get_fleets_fleet_id_members.get_sync`,
        :func:`~EVECelery.tasks.ESI.Fleets.get_fleets_fleet_id_members.get_fleets_fleet_id_members.run`, and
        :class:`~EVECelery.tasks.ESI.Fleets.get_fleets_fleet_id_members.get_fleets_fleet_id_members`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_fleets_fleet_id_members()

    @property
    def delete_fleets_fleet_id_members_member_id(
        self,
    ) -> delete_fleets_fleet_id_members_member_id:
        """
        Kick fleet member


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Fleets.delete_fleets_fleet_id_members_member_id.delete_fleets_fleet_id_members_member_id.get_sync`,
        :func:`~EVECelery.tasks.ESI.Fleets.delete_fleets_fleet_id_members_member_id.delete_fleets_fleet_id_members_member_id.run`, and
        :class:`~EVECelery.tasks.ESI.Fleets.delete_fleets_fleet_id_members_member_id.delete_fleets_fleet_id_members_member_id`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return delete_fleets_fleet_id_members_member_id()

    @property
    def delete_fleets_fleet_id_squads_squad_id(
        self,
    ) -> delete_fleets_fleet_id_squads_squad_id:
        """
        Delete fleet squad


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Fleets.delete_fleets_fleet_id_squads_squad_id.delete_fleets_fleet_id_squads_squad_id.get_sync`,
        :func:`~EVECelery.tasks.ESI.Fleets.delete_fleets_fleet_id_squads_squad_id.delete_fleets_fleet_id_squads_squad_id.run`, and
        :class:`~EVECelery.tasks.ESI.Fleets.delete_fleets_fleet_id_squads_squad_id.delete_fleets_fleet_id_squads_squad_id`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return delete_fleets_fleet_id_squads_squad_id()

    @property
    def get_fleets_fleet_id_wings(self) -> get_fleets_fleet_id_wings:
        """
        Get fleet wings


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Fleets.get_fleets_fleet_id_wings.get_fleets_fleet_id_wings.get_sync`,
        :func:`~EVECelery.tasks.ESI.Fleets.get_fleets_fleet_id_wings.get_fleets_fleet_id_wings.run`, and
        :class:`~EVECelery.tasks.ESI.Fleets.get_fleets_fleet_id_wings.get_fleets_fleet_id_wings`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_fleets_fleet_id_wings()

    @property
    def post_fleets_fleet_id_wings(self) -> post_fleets_fleet_id_wings:
        """
        Create fleet wing


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Fleets.post_fleets_fleet_id_wings.post_fleets_fleet_id_wings.get_sync`,
        :func:`~EVECelery.tasks.ESI.Fleets.post_fleets_fleet_id_wings.post_fleets_fleet_id_wings.run`, and
        :class:`~EVECelery.tasks.ESI.Fleets.post_fleets_fleet_id_wings.post_fleets_fleet_id_wings`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return post_fleets_fleet_id_wings()

    @property
    def delete_fleets_fleet_id_wings_wing_id(
        self,
    ) -> delete_fleets_fleet_id_wings_wing_id:
        """
        Delete fleet wing


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Fleets.delete_fleets_fleet_id_wings_wing_id.delete_fleets_fleet_id_wings_wing_id.get_sync`,
        :func:`~EVECelery.tasks.ESI.Fleets.delete_fleets_fleet_id_wings_wing_id.delete_fleets_fleet_id_wings_wing_id.run`, and
        :class:`~EVECelery.tasks.ESI.Fleets.delete_fleets_fleet_id_wings_wing_id.delete_fleets_fleet_id_wings_wing_id`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return delete_fleets_fleet_id_wings_wing_id()

    @property
    def post_fleets_fleet_id_wings_wing_id_squads(
        self,
    ) -> post_fleets_fleet_id_wings_wing_id_squads:
        """
        Create fleet squad


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Fleets.post_fleets_fleet_id_wings_wing_id_squads.post_fleets_fleet_id_wings_wing_id_squads.get_sync`,
        :func:`~EVECelery.tasks.ESI.Fleets.post_fleets_fleet_id_wings_wing_id_squads.post_fleets_fleet_id_wings_wing_id_squads.run`, and
        :class:`~EVECelery.tasks.ESI.Fleets.post_fleets_fleet_id_wings_wing_id_squads.post_fleets_fleet_id_wings_wing_id_squads`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return post_fleets_fleet_id_wings_wing_id_squads()
