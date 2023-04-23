"""
A model definition module returned by an ESI task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Models.py'.
"""
from __future__ import annotations
from EVECelery.tasks.BaseTasks.Models.ModelsBase import ModelBaseEVECelery
from EVECelery.tasks.BaseTasks.Models.ModelsCached import ModelCachedResponse
from datetime import datetime
from typing import List, Literal, Optional

from pydantic import BaseModel, Field


class GetCharactersCharacterIdNotificationsOkItem(BaseModel):
    is_read: Optional[bool] = Field(
        None,
        description='is_read boolean',
        title='get_characters_character_id_notifications_is_read',
    )
    notification_id: int = Field(
        ...,
        description='notification_id integer',
        title='get_characters_character_id_notifications_notification_id',
    )
    sender_id: int = Field(
        ...,
        description='sender_id integer',
        title='get_characters_character_id_notifications_sender_id',
    )
    sender_type: Literal[
        'character', 'corporation', 'alliance', 'faction', 'other'
    ] = Field(
        ...,
        description='sender_type string',
        title='get_characters_character_id_notifications_sender_type',
    )
    text: Optional[str] = Field(
        None,
        description='text string',
        title='get_characters_character_id_notifications_text',
    )
    timestamp: datetime = Field(
        ...,
        description='timestamp string',
        title='get_characters_character_id_notifications_timestamp',
    )
    type: Literal[
        'AcceptedAlly',
        'AcceptedSurrender',
        'AgentRetiredTrigravian',
        'AllAnchoringMsg',
        'AllMaintenanceBillMsg',
        'AllStrucInvulnerableMsg',
        'AllStructVulnerableMsg',
        'AllWarCorpJoinedAllianceMsg',
        'AllWarDeclaredMsg',
        'AllWarInvalidatedMsg',
        'AllWarRetractedMsg',
        'AllWarSurrenderMsg',
        'AllianceCapitalChanged',
        'AllianceWarDeclaredV2',
        'AllyContractCancelled',
        'AllyJoinedWarAggressorMsg',
        'AllyJoinedWarAllyMsg',
        'AllyJoinedWarDefenderMsg',
        'BattlePunishFriendlyFire',
        'BillOutOfMoneyMsg',
        'BillPaidCorpAllMsg',
        'BountyClaimMsg',
        'BountyESSShared',
        'BountyESSTaken',
        'BountyPlacedAlliance',
        'BountyPlacedChar',
        'BountyPlacedCorp',
        'BountyYourBountyClaimed',
        'BuddyConnectContactAdd',
        'CharAppAcceptMsg',
        'CharAppRejectMsg',
        'CharAppWithdrawMsg',
        'CharLeftCorpMsg',
        'CharMedalMsg',
        'CharTerminationMsg',
        'CloneActivationMsg',
        'CloneActivationMsg2',
        'CloneMovedMsg',
        'CloneRevokedMsg1',
        'CloneRevokedMsg2',
        'CombatOperationFinished',
        'ContactAdd',
        'ContactEdit',
        'ContainerPasswordMsg',
        'ContractRegionChangedToPochven',
        'CorpAllBillMsg',
        'CorpAppAcceptMsg',
        'CorpAppInvitedMsg',
        'CorpAppNewMsg',
        'CorpAppRejectCustomMsg',
        'CorpAppRejectMsg',
        'CorpBecameWarEligible',
        'CorpDividendMsg',
        'CorpFriendlyFireDisableTimerCompleted',
        'CorpFriendlyFireDisableTimerStarted',
        'CorpFriendlyFireEnableTimerCompleted',
        'CorpFriendlyFireEnableTimerStarted',
        'CorpKicked',
        'CorpLiquidationMsg',
        'CorpNewCEOMsg',
        'CorpNewsMsg',
        'CorpNoLongerWarEligible',
        'CorpOfficeExpirationMsg',
        'CorpStructLostMsg',
        'CorpTaxChangeMsg',
        'CorpVoteCEORevokedMsg',
        'CorpVoteMsg',
        'CorpWarDeclaredMsg',
        'CorpWarDeclaredV2',
        'CorpWarFightingLegalMsg',
        'CorpWarInvalidatedMsg',
        'CorpWarRetractedMsg',
        'CorpWarSurrenderMsg',
        'CustomsMsg',
        'DeclareWar',
        'DistrictAttacked',
        'DustAppAcceptedMsg',
        'ESSMainBankLink',
        'EntosisCaptureStarted',
        'ExpertSystemExpired',
        'ExpertSystemExpiryImminent',
        'FWAllianceKickMsg',
        'FWAllianceWarningMsg',
        'FWCharKickMsg',
        'FWCharRankGainMsg',
        'FWCharRankLossMsg',
        'FWCharWarningMsg',
        'FWCorpJoinMsg',
        'FWCorpKickMsg',
        'FWCorpLeaveMsg',
        'FWCorpWarningMsg',
        'FacWarCorpJoinRequestMsg',
        'FacWarCorpJoinWithdrawMsg',
        'FacWarCorpLeaveRequestMsg',
        'FacWarCorpLeaveWithdrawMsg',
        'FacWarLPDisqualifiedEvent',
        'FacWarLPDisqualifiedKill',
        'FacWarLPPayoutEvent',
        'FacWarLPPayoutKill',
        'GameTimeAdded',
        'GameTimeReceived',
        'GameTimeSent',
        'GiftReceived',
        'IHubDestroyedByBillFailure',
        'IncursionCompletedMsg',
        'IndustryOperationFinished',
        'IndustryTeamAuctionLost',
        'IndustryTeamAuctionWon',
        'InfrastructureHubBillAboutToExpire',
        'InsuranceExpirationMsg',
        'InsuranceFirstShipMsg',
        'InsuranceInvalidatedMsg',
        'InsuranceIssuedMsg',
        'InsurancePayoutMsg',
        'InvasionCompletedMsg',
        'InvasionSystemLogin',
        'InvasionSystemStart',
        'JumpCloneDeletedMsg1',
        'JumpCloneDeletedMsg2',
        'KillReportFinalBlow',
        'KillReportVictim',
        'KillRightAvailable',
        'KillRightAvailableOpen',
        'KillRightEarned',
        'KillRightUnavailable',
        'KillRightUnavailableOpen',
        'KillRightUsed',
        'LocateCharMsg',
        'MadeWarMutual',
        'MercOfferRetractedMsg',
        'MercOfferedNegotiationMsg',
        'MissionCanceledTriglavian',
        'MissionOfferExpirationMsg',
        'MissionTimeoutMsg',
        'MoonminingAutomaticFracture',
        'MoonminingExtractionCancelled',
        'MoonminingExtractionFinished',
        'MoonminingExtractionStarted',
        'MoonminingLaserFired',
        'MutualWarExpired',
        'MutualWarInviteAccepted',
        'MutualWarInviteRejected',
        'MutualWarInviteSent',
        'NPCStandingsGained',
        'NPCStandingsLost',
        'OfferToAllyRetracted',
        'OfferedSurrender',
        'OfferedToAlly',
        'OfficeLeaseCanceledInsufficientStandings',
        'OldLscMessages',
        'OperationFinished',
        'OrbitalAttacked',
        'OrbitalReinforced',
        'OwnershipTransferred',
        'RaffleCreated',
        'RaffleExpired',
        'RaffleFinished',
        'ReimbursementMsg',
        'ResearchMissionAvailableMsg',
        'RetractsWar',
        'SeasonalChallengeCompleted',
        'SovAllClaimAquiredMsg',
        'SovAllClaimLostMsg',
        'SovCommandNodeEventStarted',
        'SovCorpBillLateMsg',
        'SovCorpClaimFailMsg',
        'SovDisruptorMsg',
        'SovStationEnteredFreeport',
        'SovStructureDestroyed',
        'SovStructureReinforced',
        'SovStructureSelfDestructCancel',
        'SovStructureSelfDestructFinished',
        'SovStructureSelfDestructRequested',
        'SovereigntyIHDamageMsg',
        'SovereigntySBUDamageMsg',
        'SovereigntyTCUDamageMsg',
        'StationAggressionMsg1',
        'StationAggressionMsg2',
        'StationConquerMsg',
        'StationServiceDisabled',
        'StationServiceEnabled',
        'StationStateChangeMsg',
        'StoryLineMissionAvailableMsg',
        'StructureAnchoring',
        'StructureCourierContractChanged',
        'StructureDestroyed',
        'StructureFuelAlert',
        'StructureImpendingAbandonmentAssetsAtRisk',
        'StructureItemsDelivered',
        'StructureItemsMovedToSafety',
        'StructureLostArmor',
        'StructureLostShields',
        'StructureOnline',
        'StructureServicesOffline',
        'StructureUnanchoring',
        'StructureUnderAttack',
        'StructureWentHighPower',
        'StructureWentLowPower',
        'StructuresJobsCancelled',
        'StructuresJobsPaused',
        'StructuresReinforcementChanged',
        'TowerAlertMsg',
        'TowerResourceAlertMsg',
        'TransactionReversalMsg',
        'TutorialMsg',
        'WarAdopted ',
        'WarAllyInherited',
        'WarAllyOfferDeclinedMsg',
        'WarConcordInvalidates',
        'WarDeclared',
        'WarEndedHqSecurityDrop',
        'WarHQRemovedFromSpace',
        'WarInherited',
        'WarInvalid',
        'WarRetracted',
        'WarRetractedByConcord',
        'WarSurrenderDeclinedMsg',
        'WarSurrenderOfferMsg',
    ] = Field(
        ...,
        description='type string',
        title='get_characters_character_id_notifications_type',
    )


class GetCharactersCharacterIdNotificationsOk(BaseModel):
    __root__: List[GetCharactersCharacterIdNotificationsOkItem] = Field(
        ...,
        description='200 ok array',
        max_items=500,
        title='get_characters_character_id_notifications_ok',
    )


class Headers200_get_characters_character_id_notifications(ModelBaseEVECelery):
    """
    Headers for response code 200
    """

    Cache_Control: str | None = Field(
        description="The caching mechanism used", alias="Cache-Control"
    )
    ETag: str | None = Field(description="RFC7232 compliant entity tag")
    Expires: str | None = Field(description="RFC7231 formatted datetime string")
    Last_Modified: str | None = Field(
        description="RFC7231 formatted datetime string", alias="Last-Modified"
    )


class Response200_get_characters_character_id_notifications(ModelCachedResponse):
    """
    Returns your recent notifications

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "is_read": true,
            "notification_id": 1,
            "sender_id": 1000132,
            "sender_type": "corporation",
            "text": "amount: 3731016.4000000004\\nitemID: 1024881021663\\npayout: 1\\n",
            "timestamp": "2017-08-16T10:08:00Z",
            "type": "InsurancePayoutMsg"
          }
        ]

    """

    headers: Headers200_get_characters_character_id_notifications = Field(
        ..., description='The response headers for this request.'
    )
    body: GetCharactersCharacterIdNotificationsOk = Field(
        ..., description='The response body for this request.'
    )
