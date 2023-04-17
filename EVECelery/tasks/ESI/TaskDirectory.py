"""
Task directory module for adding task objects as attributes to a namespace for easy access and code inspection.
This injection module is the root directory for ESI tasks and imports / instantiates all other task directory classes containing task objects.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/RootTaskDirectory.py'.
"""

from .Alliance.TaskDirectory import TaskDirectory as AllianceTaskDirectory
from .Skills.TaskDirectory import TaskDirectory as SkillsTaskDirectory
from .Calendar.TaskDirectory import TaskDirectory as CalendarTaskDirectory
from .Character.TaskDirectory import TaskDirectory as CharacterTaskDirectory
from .Fleets.TaskDirectory import TaskDirectory as FleetsTaskDirectory
from .Clones.TaskDirectory import TaskDirectory as ClonesTaskDirectory
from .Location.TaskDirectory import TaskDirectory as LocationTaskDirectory
from .Search.TaskDirectory import TaskDirectory as SearchTaskDirectory
from .Corporation.TaskDirectory import TaskDirectory as CorporationTaskDirectory
from .Dogma.TaskDirectory import TaskDirectory as DogmaTaskDirectory
from .Market.TaskDirectory import TaskDirectory as MarketTaskDirectory
from .Opportunities.TaskDirectory import TaskDirectory as OpportunitiesTaskDirectory
from .Routes.TaskDirectory import TaskDirectory as RoutesTaskDirectory
from .Status.TaskDirectory import TaskDirectory as StatusTaskDirectory
from .Universe.TaskDirectory import TaskDirectory as UniverseTaskDirectory
from .PlanetaryInteraction.TaskDirectory import (
    TaskDirectory as PlanetaryInteractionTaskDirectory,
)
from .Wars.TaskDirectory import TaskDirectory as WarsTaskDirectory


class TaskDirectory(object):
    """
    ESI directory for quickly finding other tasks

    This task directory contains all subdirectories of ESI task categories.
    """

    @property
    def Alliance(self) -> AllianceTaskDirectory:
        """
        Subdirectory for ESI tasks categorized as "Alliance"


        :return: The task directory for all Alliance ESI tasks

        """
        return AllianceTaskDirectory()

    @property
    def Skills(self) -> SkillsTaskDirectory:
        """
        Subdirectory for ESI tasks categorized as "Skills"


        :return: The task directory for all Skills ESI tasks

        """
        return SkillsTaskDirectory()

    @property
    def Calendar(self) -> CalendarTaskDirectory:
        """
        Subdirectory for ESI tasks categorized as "Calendar"


        :return: The task directory for all Calendar ESI tasks

        """
        return CalendarTaskDirectory()

    @property
    def Character(self) -> CharacterTaskDirectory:
        """
        Subdirectory for ESI tasks categorized as "Character"


        :return: The task directory for all Character ESI tasks

        """
        return CharacterTaskDirectory()

    @property
    def Fleets(self) -> FleetsTaskDirectory:
        """
        Subdirectory for ESI tasks categorized as "Fleets"


        :return: The task directory for all Fleets ESI tasks

        """
        return FleetsTaskDirectory()

    @property
    def Clones(self) -> ClonesTaskDirectory:
        """
        Subdirectory for ESI tasks categorized as "Clones"


        :return: The task directory for all Clones ESI tasks

        """
        return ClonesTaskDirectory()

    @property
    def Location(self) -> LocationTaskDirectory:
        """
        Subdirectory for ESI tasks categorized as "Location"


        :return: The task directory for all Location ESI tasks

        """
        return LocationTaskDirectory()

    @property
    def Search(self) -> SearchTaskDirectory:
        """
        Subdirectory for ESI tasks categorized as "Search"


        :return: The task directory for all Search ESI tasks

        """
        return SearchTaskDirectory()

    @property
    def Corporation(self) -> CorporationTaskDirectory:
        """
        Subdirectory for ESI tasks categorized as "Corporation"


        :return: The task directory for all Corporation ESI tasks

        """
        return CorporationTaskDirectory()

    @property
    def Dogma(self) -> DogmaTaskDirectory:
        """
        Subdirectory for ESI tasks categorized as "Dogma"


        :return: The task directory for all Dogma ESI tasks

        """
        return DogmaTaskDirectory()

    @property
    def Market(self) -> MarketTaskDirectory:
        """
        Subdirectory for ESI tasks categorized as "Market"


        :return: The task directory for all Market ESI tasks

        """
        return MarketTaskDirectory()

    @property
    def Opportunities(self) -> OpportunitiesTaskDirectory:
        """
        Subdirectory for ESI tasks categorized as "Opportunities"


        :return: The task directory for all Opportunities ESI tasks

        """
        return OpportunitiesTaskDirectory()

    @property
    def Routes(self) -> RoutesTaskDirectory:
        """
        Subdirectory for ESI tasks categorized as "Routes"


        :return: The task directory for all Routes ESI tasks

        """
        return RoutesTaskDirectory()

    @property
    def Status(self) -> StatusTaskDirectory:
        """
        Subdirectory for ESI tasks categorized as "Status"


        :return: The task directory for all Status ESI tasks

        """
        return StatusTaskDirectory()

    @property
    def Universe(self) -> UniverseTaskDirectory:
        """
        Subdirectory for ESI tasks categorized as "Universe"


        :return: The task directory for all Universe ESI tasks

        """
        return UniverseTaskDirectory()

    @property
    def PlanetaryInteraction(self) -> PlanetaryInteractionTaskDirectory:
        """
        Subdirectory for ESI tasks categorized as "PlanetaryInteraction"


        :return: The task directory for all PlanetaryInteraction ESI tasks

        """
        return PlanetaryInteractionTaskDirectory()

    @property
    def Wars(self) -> WarsTaskDirectory:
        """
        Subdirectory for ESI tasks categorized as "Wars"


        :return: The task directory for all Wars ESI tasks

        """
        return WarsTaskDirectory()
