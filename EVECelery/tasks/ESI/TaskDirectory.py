"""
Task directory module for adding task objects as attributes to a namespace for easy access and code inspection.
This injection module is the root directory for ESI tasks and imports / instantiates all other task directory classes containing task objects.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/RootTaskDirectory.py'.
"""

from .Alliance.TaskDirectory import TaskDirectory as AllianceTaskDirectory
from .Contacts.TaskDirectory import TaskDirectory as ContactsTaskDirectory
from .Character.TaskDirectory import TaskDirectory as CharacterTaskDirectory
from .Assets.TaskDirectory import TaskDirectory as AssetsTaskDirectory
from .Skills.TaskDirectory import TaskDirectory as SkillsTaskDirectory
from .Bookmarks.TaskDirectory import TaskDirectory as BookmarksTaskDirectory
from .Calendar.TaskDirectory import TaskDirectory as CalendarTaskDirectory
from .Clones.TaskDirectory import TaskDirectory as ClonesTaskDirectory
from .Contracts.TaskDirectory import TaskDirectory as ContractsTaskDirectory
from .Fittings.TaskDirectory import TaskDirectory as FittingsTaskDirectory
from .Fleets.TaskDirectory import TaskDirectory as FleetsTaskDirectory
from .FactionWarfare.TaskDirectory import TaskDirectory as FactionWarfareTaskDirectory
from .Industry.TaskDirectory import TaskDirectory as IndustryTaskDirectory
from .Killmails.TaskDirectory import TaskDirectory as KillmailsTaskDirectory
from .Location.TaskDirectory import TaskDirectory as LocationTaskDirectory
from .Loyalty.TaskDirectory import TaskDirectory as LoyaltyTaskDirectory
from .Mail.TaskDirectory import TaskDirectory as MailTaskDirectory
from .Opportunities.TaskDirectory import TaskDirectory as OpportunitiesTaskDirectory
from .Market.TaskDirectory import TaskDirectory as MarketTaskDirectory
from .PlanetaryInteraction.TaskDirectory import (
    TaskDirectory as PlanetaryInteractionTaskDirectory,
)
from .Search.TaskDirectory import TaskDirectory as SearchTaskDirectory
from .Wallet.TaskDirectory import TaskDirectory as WalletTaskDirectory
from .Corporation.TaskDirectory import TaskDirectory as CorporationTaskDirectory
from .Dogma.TaskDirectory import TaskDirectory as DogmaTaskDirectory
from .Incursions.TaskDirectory import TaskDirectory as IncursionsTaskDirectory
from .Insurance.TaskDirectory import TaskDirectory as InsuranceTaskDirectory
from .Routes.TaskDirectory import TaskDirectory as RoutesTaskDirectory
from .Sovereignty.TaskDirectory import TaskDirectory as SovereigntyTaskDirectory
from .Status.TaskDirectory import TaskDirectory as StatusTaskDirectory
from .UserInterface.TaskDirectory import TaskDirectory as UserInterfaceTaskDirectory
from .Universe.TaskDirectory import TaskDirectory as UniverseTaskDirectory
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
    def Contacts(self) -> ContactsTaskDirectory:
        """
        Subdirectory for ESI tasks categorized as "Contacts"


        :return: The task directory for all Contacts ESI tasks

        """
        return ContactsTaskDirectory()

    @property
    def Character(self) -> CharacterTaskDirectory:
        """
        Subdirectory for ESI tasks categorized as "Character"


        :return: The task directory for all Character ESI tasks

        """
        return CharacterTaskDirectory()

    @property
    def Assets(self) -> AssetsTaskDirectory:
        """
        Subdirectory for ESI tasks categorized as "Assets"


        :return: The task directory for all Assets ESI tasks

        """
        return AssetsTaskDirectory()

    @property
    def Skills(self) -> SkillsTaskDirectory:
        """
        Subdirectory for ESI tasks categorized as "Skills"


        :return: The task directory for all Skills ESI tasks

        """
        return SkillsTaskDirectory()

    @property
    def Bookmarks(self) -> BookmarksTaskDirectory:
        """
        Subdirectory for ESI tasks categorized as "Bookmarks"


        :return: The task directory for all Bookmarks ESI tasks

        """
        return BookmarksTaskDirectory()

    @property
    def Calendar(self) -> CalendarTaskDirectory:
        """
        Subdirectory for ESI tasks categorized as "Calendar"


        :return: The task directory for all Calendar ESI tasks

        """
        return CalendarTaskDirectory()

    @property
    def Clones(self) -> ClonesTaskDirectory:
        """
        Subdirectory for ESI tasks categorized as "Clones"


        :return: The task directory for all Clones ESI tasks

        """
        return ClonesTaskDirectory()

    @property
    def Contracts(self) -> ContractsTaskDirectory:
        """
        Subdirectory for ESI tasks categorized as "Contracts"


        :return: The task directory for all Contracts ESI tasks

        """
        return ContractsTaskDirectory()

    @property
    def Fittings(self) -> FittingsTaskDirectory:
        """
        Subdirectory for ESI tasks categorized as "Fittings"


        :return: The task directory for all Fittings ESI tasks

        """
        return FittingsTaskDirectory()

    @property
    def Fleets(self) -> FleetsTaskDirectory:
        """
        Subdirectory for ESI tasks categorized as "Fleets"


        :return: The task directory for all Fleets ESI tasks

        """
        return FleetsTaskDirectory()

    @property
    def FactionWarfare(self) -> FactionWarfareTaskDirectory:
        """
        Subdirectory for ESI tasks categorized as "FactionWarfare"


        :return: The task directory for all FactionWarfare ESI tasks

        """
        return FactionWarfareTaskDirectory()

    @property
    def Industry(self) -> IndustryTaskDirectory:
        """
        Subdirectory for ESI tasks categorized as "Industry"


        :return: The task directory for all Industry ESI tasks

        """
        return IndustryTaskDirectory()

    @property
    def Killmails(self) -> KillmailsTaskDirectory:
        """
        Subdirectory for ESI tasks categorized as "Killmails"


        :return: The task directory for all Killmails ESI tasks

        """
        return KillmailsTaskDirectory()

    @property
    def Location(self) -> LocationTaskDirectory:
        """
        Subdirectory for ESI tasks categorized as "Location"


        :return: The task directory for all Location ESI tasks

        """
        return LocationTaskDirectory()

    @property
    def Loyalty(self) -> LoyaltyTaskDirectory:
        """
        Subdirectory for ESI tasks categorized as "Loyalty"


        :return: The task directory for all Loyalty ESI tasks

        """
        return LoyaltyTaskDirectory()

    @property
    def Mail(self) -> MailTaskDirectory:
        """
        Subdirectory for ESI tasks categorized as "Mail"


        :return: The task directory for all Mail ESI tasks

        """
        return MailTaskDirectory()

    @property
    def Opportunities(self) -> OpportunitiesTaskDirectory:
        """
        Subdirectory for ESI tasks categorized as "Opportunities"


        :return: The task directory for all Opportunities ESI tasks

        """
        return OpportunitiesTaskDirectory()

    @property
    def Market(self) -> MarketTaskDirectory:
        """
        Subdirectory for ESI tasks categorized as "Market"


        :return: The task directory for all Market ESI tasks

        """
        return MarketTaskDirectory()

    @property
    def PlanetaryInteraction(self) -> PlanetaryInteractionTaskDirectory:
        """
        Subdirectory for ESI tasks categorized as "PlanetaryInteraction"


        :return: The task directory for all PlanetaryInteraction ESI tasks

        """
        return PlanetaryInteractionTaskDirectory()

    @property
    def Search(self) -> SearchTaskDirectory:
        """
        Subdirectory for ESI tasks categorized as "Search"


        :return: The task directory for all Search ESI tasks

        """
        return SearchTaskDirectory()

    @property
    def Wallet(self) -> WalletTaskDirectory:
        """
        Subdirectory for ESI tasks categorized as "Wallet"


        :return: The task directory for all Wallet ESI tasks

        """
        return WalletTaskDirectory()

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
    def Incursions(self) -> IncursionsTaskDirectory:
        """
        Subdirectory for ESI tasks categorized as "Incursions"


        :return: The task directory for all Incursions ESI tasks

        """
        return IncursionsTaskDirectory()

    @property
    def Insurance(self) -> InsuranceTaskDirectory:
        """
        Subdirectory for ESI tasks categorized as "Insurance"


        :return: The task directory for all Insurance ESI tasks

        """
        return InsuranceTaskDirectory()

    @property
    def Routes(self) -> RoutesTaskDirectory:
        """
        Subdirectory for ESI tasks categorized as "Routes"


        :return: The task directory for all Routes ESI tasks

        """
        return RoutesTaskDirectory()

    @property
    def Sovereignty(self) -> SovereigntyTaskDirectory:
        """
        Subdirectory for ESI tasks categorized as "Sovereignty"


        :return: The task directory for all Sovereignty ESI tasks

        """
        return SovereigntyTaskDirectory()

    @property
    def Status(self) -> StatusTaskDirectory:
        """
        Subdirectory for ESI tasks categorized as "Status"


        :return: The task directory for all Status ESI tasks

        """
        return StatusTaskDirectory()

    @property
    def UserInterface(self) -> UserInterfaceTaskDirectory:
        """
        Subdirectory for ESI tasks categorized as "UserInterface"


        :return: The task directory for all UserInterface ESI tasks

        """
        return UserInterfaceTaskDirectory()

    @property
    def Universe(self) -> UniverseTaskDirectory:
        """
        Subdirectory for ESI tasks categorized as "Universe"


        :return: The task directory for all Universe ESI tasks

        """
        return UniverseTaskDirectory()

    @property
    def Wars(self) -> WarsTaskDirectory:
        """
        Subdirectory for ESI tasks categorized as "Wars"


        :return: The task directory for all Wars ESI tasks

        """
        return WarsTaskDirectory()
