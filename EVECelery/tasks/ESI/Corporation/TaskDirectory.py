"""
Task directory module for adding task objects as attributes to a namespace for easy access and code inspection.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/TaskDirectory.py'.
"""

from .get_corporations_npccorps import get_corporations_npccorps
from .get_corporations_corporation_id import get_corporations_corporation_id
from .get_corporations_corporation_id_alliancehistory import (
    get_corporations_corporation_id_alliancehistory,
)
from .get_corporations_corporation_id_blueprints import (
    get_corporations_corporation_id_blueprints,
)
from .get_corporations_corporation_id_containers_logs import (
    get_corporations_corporation_id_containers_logs,
)
from .get_corporations_corporation_id_divisions import (
    get_corporations_corporation_id_divisions,
)
from .get_corporations_corporation_id_facilities import (
    get_corporations_corporation_id_facilities,
)
from .get_corporations_corporation_id_icons import get_corporations_corporation_id_icons
from .get_corporations_corporation_id_medals import (
    get_corporations_corporation_id_medals,
)
from .get_corporations_corporation_id_medals_issued import (
    get_corporations_corporation_id_medals_issued,
)
from .get_corporations_corporation_id_members import (
    get_corporations_corporation_id_members,
)
from .get_corporations_corporation_id_members_limit import (
    get_corporations_corporation_id_members_limit,
)
from .get_corporations_corporation_id_members_titles import (
    get_corporations_corporation_id_members_titles,
)
from .get_corporations_corporation_id_membertracking import (
    get_corporations_corporation_id_membertracking,
)
from .get_corporations_corporation_id_roles import get_corporations_corporation_id_roles
from .get_corporations_corporation_id_roles_history import (
    get_corporations_corporation_id_roles_history,
)
from .get_corporations_corporation_id_shareholders import (
    get_corporations_corporation_id_shareholders,
)
from .get_corporations_corporation_id_standings import (
    get_corporations_corporation_id_standings,
)
from .get_corporations_corporation_id_starbases import (
    get_corporations_corporation_id_starbases,
)
from .get_corporations_corporation_id_starbases_starbase_id import (
    get_corporations_corporation_id_starbases_starbase_id,
)
from .get_corporations_corporation_id_structures import (
    get_corporations_corporation_id_structures,
)
from .get_corporations_corporation_id_titles import (
    get_corporations_corporation_id_titles,
)


class TaskDirectory(object):
    """
    Directory for quickly finding tasks with easy access to documentation and code inspection

    This task directory contains all tasks as attributes that are categorized with 'Corporation'.
    """

    @property
    def get_corporations_npccorps(self) -> get_corporations_npccorps:
        """
        Get npc corporations


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Corporation.get_corporations_npccorps.get_corporations_npccorps.get_sync`,
        :func:`~EVECelery.tasks.ESI.Corporation.get_corporations_npccorps.get_corporations_npccorps.run`, and
        :class:`~EVECelery.tasks.ESI.Corporation.get_corporations_npccorps.get_corporations_npccorps`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_corporations_npccorps()

    @property
    def get_corporations_corporation_id(self) -> get_corporations_corporation_id:
        """
        Get corporation information


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id.get_corporations_corporation_id.get_sync`,
        :func:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id.get_corporations_corporation_id.run`, and
        :class:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id.get_corporations_corporation_id`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_corporations_corporation_id()

    @property
    def get_corporations_corporation_id_alliancehistory(
        self,
    ) -> get_corporations_corporation_id_alliancehistory:
        """
        Get alliance history


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id_alliancehistory.get_corporations_corporation_id_alliancehistory.get_sync`,
        :func:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id_alliancehistory.get_corporations_corporation_id_alliancehistory.run`, and
        :class:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id_alliancehistory.get_corporations_corporation_id_alliancehistory`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_corporations_corporation_id_alliancehistory()

    @property
    def get_corporations_corporation_id_blueprints(
        self,
    ) -> get_corporations_corporation_id_blueprints:
        """
        Get corporation blueprints


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id_blueprints.get_corporations_corporation_id_blueprints.get_sync`,
        :func:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id_blueprints.get_corporations_corporation_id_blueprints.run`, and
        :class:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id_blueprints.get_corporations_corporation_id_blueprints`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_corporations_corporation_id_blueprints()

    @property
    def get_corporations_corporation_id_containers_logs(
        self,
    ) -> get_corporations_corporation_id_containers_logs:
        """
        Get all corporation ALSC logs


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id_containers_logs.get_corporations_corporation_id_containers_logs.get_sync`,
        :func:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id_containers_logs.get_corporations_corporation_id_containers_logs.run`, and
        :class:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id_containers_logs.get_corporations_corporation_id_containers_logs`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_corporations_corporation_id_containers_logs()

    @property
    def get_corporations_corporation_id_divisions(
        self,
    ) -> get_corporations_corporation_id_divisions:
        """
        Get corporation divisions


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id_divisions.get_corporations_corporation_id_divisions.get_sync`,
        :func:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id_divisions.get_corporations_corporation_id_divisions.run`, and
        :class:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id_divisions.get_corporations_corporation_id_divisions`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_corporations_corporation_id_divisions()

    @property
    def get_corporations_corporation_id_facilities(
        self,
    ) -> get_corporations_corporation_id_facilities:
        """
        Get corporation facilities


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id_facilities.get_corporations_corporation_id_facilities.get_sync`,
        :func:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id_facilities.get_corporations_corporation_id_facilities.run`, and
        :class:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id_facilities.get_corporations_corporation_id_facilities`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_corporations_corporation_id_facilities()

    @property
    def get_corporations_corporation_id_icons(
        self,
    ) -> get_corporations_corporation_id_icons:
        """
        Get corporation icon


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id_icons.get_corporations_corporation_id_icons.get_sync`,
        :func:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id_icons.get_corporations_corporation_id_icons.run`, and
        :class:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id_icons.get_corporations_corporation_id_icons`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_corporations_corporation_id_icons()

    @property
    def get_corporations_corporation_id_medals(
        self,
    ) -> get_corporations_corporation_id_medals:
        """
        Get corporation medals


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id_medals.get_corporations_corporation_id_medals.get_sync`,
        :func:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id_medals.get_corporations_corporation_id_medals.run`, and
        :class:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id_medals.get_corporations_corporation_id_medals`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_corporations_corporation_id_medals()

    @property
    def get_corporations_corporation_id_medals_issued(
        self,
    ) -> get_corporations_corporation_id_medals_issued:
        """
        Get corporation issued medals


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id_medals_issued.get_corporations_corporation_id_medals_issued.get_sync`,
        :func:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id_medals_issued.get_corporations_corporation_id_medals_issued.run`, and
        :class:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id_medals_issued.get_corporations_corporation_id_medals_issued`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_corporations_corporation_id_medals_issued()

    @property
    def get_corporations_corporation_id_members(
        self,
    ) -> get_corporations_corporation_id_members:
        """
        Get corporation members


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id_members.get_corporations_corporation_id_members.get_sync`,
        :func:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id_members.get_corporations_corporation_id_members.run`, and
        :class:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id_members.get_corporations_corporation_id_members`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_corporations_corporation_id_members()

    @property
    def get_corporations_corporation_id_members_limit(
        self,
    ) -> get_corporations_corporation_id_members_limit:
        """
        Get corporation member limit


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id_members_limit.get_corporations_corporation_id_members_limit.get_sync`,
        :func:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id_members_limit.get_corporations_corporation_id_members_limit.run`, and
        :class:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id_members_limit.get_corporations_corporation_id_members_limit`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_corporations_corporation_id_members_limit()

    @property
    def get_corporations_corporation_id_members_titles(
        self,
    ) -> get_corporations_corporation_id_members_titles:
        """
        Get corporation's members' titles


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id_members_titles.get_corporations_corporation_id_members_titles.get_sync`,
        :func:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id_members_titles.get_corporations_corporation_id_members_titles.run`, and
        :class:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id_members_titles.get_corporations_corporation_id_members_titles`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_corporations_corporation_id_members_titles()

    @property
    def get_corporations_corporation_id_membertracking(
        self,
    ) -> get_corporations_corporation_id_membertracking:
        """
        Track corporation members


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id_membertracking.get_corporations_corporation_id_membertracking.get_sync`,
        :func:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id_membertracking.get_corporations_corporation_id_membertracking.run`, and
        :class:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id_membertracking.get_corporations_corporation_id_membertracking`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_corporations_corporation_id_membertracking()

    @property
    def get_corporations_corporation_id_roles(
        self,
    ) -> get_corporations_corporation_id_roles:
        """
        Get corporation member roles


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id_roles.get_corporations_corporation_id_roles.get_sync`,
        :func:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id_roles.get_corporations_corporation_id_roles.run`, and
        :class:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id_roles.get_corporations_corporation_id_roles`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_corporations_corporation_id_roles()

    @property
    def get_corporations_corporation_id_roles_history(
        self,
    ) -> get_corporations_corporation_id_roles_history:
        """
        Get corporation member roles history


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id_roles_history.get_corporations_corporation_id_roles_history.get_sync`,
        :func:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id_roles_history.get_corporations_corporation_id_roles_history.run`, and
        :class:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id_roles_history.get_corporations_corporation_id_roles_history`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_corporations_corporation_id_roles_history()

    @property
    def get_corporations_corporation_id_shareholders(
        self,
    ) -> get_corporations_corporation_id_shareholders:
        """
        Get corporation shareholders


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id_shareholders.get_corporations_corporation_id_shareholders.get_sync`,
        :func:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id_shareholders.get_corporations_corporation_id_shareholders.run`, and
        :class:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id_shareholders.get_corporations_corporation_id_shareholders`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_corporations_corporation_id_shareholders()

    @property
    def get_corporations_corporation_id_standings(
        self,
    ) -> get_corporations_corporation_id_standings:
        """
        Get corporation standings


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id_standings.get_corporations_corporation_id_standings.get_sync`,
        :func:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id_standings.get_corporations_corporation_id_standings.run`, and
        :class:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id_standings.get_corporations_corporation_id_standings`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_corporations_corporation_id_standings()

    @property
    def get_corporations_corporation_id_starbases(
        self,
    ) -> get_corporations_corporation_id_starbases:
        """
        Get corporation starbases (POSes)


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id_starbases.get_corporations_corporation_id_starbases.get_sync`,
        :func:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id_starbases.get_corporations_corporation_id_starbases.run`, and
        :class:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id_starbases.get_corporations_corporation_id_starbases`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_corporations_corporation_id_starbases()

    @property
    def get_corporations_corporation_id_starbases_starbase_id(
        self,
    ) -> get_corporations_corporation_id_starbases_starbase_id:
        """
        Get starbase (POS) detail


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id_starbases_starbase_id.get_corporations_corporation_id_starbases_starbase_id.get_sync`,
        :func:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id_starbases_starbase_id.get_corporations_corporation_id_starbases_starbase_id.run`, and
        :class:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id_starbases_starbase_id.get_corporations_corporation_id_starbases_starbase_id`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_corporations_corporation_id_starbases_starbase_id()

    @property
    def get_corporations_corporation_id_structures(
        self,
    ) -> get_corporations_corporation_id_structures:
        """
        Get corporation structures


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id_structures.get_corporations_corporation_id_structures.get_sync`,
        :func:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id_structures.get_corporations_corporation_id_structures.run`, and
        :class:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id_structures.get_corporations_corporation_id_structures`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_corporations_corporation_id_structures()

    @property
    def get_corporations_corporation_id_titles(
        self,
    ) -> get_corporations_corporation_id_titles:
        """
        Get corporation titles


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id_titles.get_corporations_corporation_id_titles.get_sync`,
        :func:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id_titles.get_corporations_corporation_id_titles.run`, and
        :class:`~EVECelery.tasks.ESI.Corporation.get_corporations_corporation_id_titles.get_corporations_corporation_id_titles`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_corporations_corporation_id_titles()
