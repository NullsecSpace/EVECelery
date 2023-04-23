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


class GetCharactersCharacterIdWalletJournalOkItem(BaseModel):
    amount: Optional[float] = Field(
        None,
        description='The amount of ISK given or taken from the wallet as a result of the given transaction. Positive when ISK is deposited into the wallet and negative when ISK is withdrawn',
        title='get_characters_character_id_wallet_journal_amount',
    )
    balance: Optional[float] = Field(
        None,
        description='Wallet balance after transaction occurred',
        title='get_characters_character_id_wallet_journal_balance',
    )
    context_id: Optional[int] = Field(
        None,
        description='An ID that gives extra context to the particular transaction. Because of legacy reasons the context is completely different per ref_type and means different things. It is also possible to not have a context_id',
        title='get_characters_character_id_wallet_journal_context_id',
    )
    context_id_type: Optional[
        Literal[
            'structure_id',
            'station_id',
            'market_transaction_id',
            'character_id',
            'corporation_id',
            'alliance_id',
            'eve_system',
            'industry_job_id',
            'contract_id',
            'planet_id',
            'system_id',
            'type_id',
        ]
    ] = Field(
        None,
        description='The type of the given context_id if present',
        title='get_characters_character_id_wallet_journal_context_id_type',
    )
    date: datetime = Field(
        ...,
        description='Date and time of transaction',
        title='get_characters_character_id_wallet_journal_date',
    )
    description: str = Field(
        ...,
        description='The reason for the transaction, mirrors what is seen in the client',
        title='get_characters_character_id_wallet_journal_description',
    )
    first_party_id: Optional[int] = Field(
        None,
        description='The id of the first party involved in the transaction. This attribute has no consistency and is different or non existant for particular ref_types. The description attribute will help make sense of what this attribute means. For more info about the given ID it can be dropped into the /universe/names/ ESI route to determine its type and name',
        title='get_characters_character_id_wallet_journal_first_party_id',
    )
    id: int = Field(
        ...,
        description='Unique journal reference ID',
        title='get_characters_character_id_wallet_journal_id',
    )
    reason: Optional[str] = Field(
        None,
        description='The user stated reason for the transaction. Only applies to some ref_types',
        title='get_characters_character_id_wallet_journal_reason',
    )
    ref_type: Literal[
        'acceleration_gate_fee',
        'advertisement_listing_fee',
        'agent_donation',
        'agent_location_services',
        'agent_miscellaneous',
        'agent_mission_collateral_paid',
        'agent_mission_collateral_refunded',
        'agent_mission_reward',
        'agent_mission_reward_corporation_tax',
        'agent_mission_time_bonus_reward',
        'agent_mission_time_bonus_reward_corporation_tax',
        'agent_security_services',
        'agent_services_rendered',
        'agents_preward',
        'alliance_maintainance_fee',
        'alliance_registration_fee',
        'asset_safety_recovery_tax',
        'bounty',
        'bounty_prize',
        'bounty_prize_corporation_tax',
        'bounty_prizes',
        'bounty_reimbursement',
        'bounty_surcharge',
        'brokers_fee',
        'clone_activation',
        'clone_transfer',
        'contraband_fine',
        'contract_auction_bid',
        'contract_auction_bid_corp',
        'contract_auction_bid_refund',
        'contract_auction_sold',
        'contract_brokers_fee',
        'contract_brokers_fee_corp',
        'contract_collateral',
        'contract_collateral_deposited_corp',
        'contract_collateral_payout',
        'contract_collateral_refund',
        'contract_deposit',
        'contract_deposit_corp',
        'contract_deposit_refund',
        'contract_deposit_sales_tax',
        'contract_price',
        'contract_price_payment_corp',
        'contract_reversal',
        'contract_reward',
        'contract_reward_deposited',
        'contract_reward_deposited_corp',
        'contract_reward_refund',
        'contract_sales_tax',
        'copying',
        'corporate_reward_payout',
        'corporate_reward_tax',
        'corporation_account_withdrawal',
        'corporation_bulk_payment',
        'corporation_dividend_payment',
        'corporation_liquidation',
        'corporation_logo_change_cost',
        'corporation_payment',
        'corporation_registration_fee',
        'courier_mission_escrow',
        'cspa',
        'cspaofflinerefund',
        'daily_challenge_reward',
        'datacore_fee',
        'dna_modification_fee',
        'docking_fee',
        'duel_wager_escrow',
        'duel_wager_payment',
        'duel_wager_refund',
        'ess_escrow_transfer',
        'external_trade_delivery',
        'external_trade_freeze',
        'external_trade_thaw',
        'factory_slot_rental_fee',
        'flux_payout',
        'flux_tax',
        'flux_ticket_repayment',
        'flux_ticket_sale',
        'gm_cash_transfer',
        'industry_job_tax',
        'infrastructure_hub_maintenance',
        'inheritance',
        'insurance',
        'item_trader_payment',
        'jump_clone_activation_fee',
        'jump_clone_installation_fee',
        'kill_right_fee',
        'lp_store',
        'manufacturing',
        'market_escrow',
        'market_fine_paid',
        'market_provider_tax',
        'market_transaction',
        'medal_creation',
        'medal_issued',
        'milestone_reward_payment',
        'mission_completion',
        'mission_cost',
        'mission_expiration',
        'mission_reward',
        'office_rental_fee',
        'operation_bonus',
        'opportunity_reward',
        'planetary_construction',
        'planetary_export_tax',
        'planetary_import_tax',
        'player_donation',
        'player_trading',
        'project_discovery_reward',
        'project_discovery_tax',
        'reaction',
        'redeemed_isk_token',
        'release_of_impounded_property',
        'repair_bill',
        'reprocessing_tax',
        'researching_material_productivity',
        'researching_technology',
        'researching_time_productivity',
        'resource_wars_reward',
        'reverse_engineering',
        'season_challenge_reward',
        'security_processing_fee',
        'shares',
        'skill_purchase',
        'sovereignity_bill',
        'store_purchase',
        'store_purchase_refund',
        'structure_gate_jump',
        'transaction_tax',
        'upkeep_adjustment_fee',
        'war_ally_contract',
        'war_fee',
        'war_fee_surrender',
    ] = Field(
        ...,
        description='"The transaction type for the given. transaction. Different transaction types will populate different attributes."',
        title='get_characters_character_id_wallet_journal_ref_type',
    )
    second_party_id: Optional[int] = Field(
        None,
        description='The id of the second party involved in the transaction. This attribute has no consistency and is different or non existant for particular ref_types. The description attribute will help make sense of what this attribute means. For more info about the given ID it can be dropped into the /universe/names/ ESI route to determine its type and name',
        title='get_characters_character_id_wallet_journal_second_party_id',
    )
    tax: Optional[float] = Field(
        None,
        description='Tax amount received. Only applies to tax related transactions',
        title='get_characters_character_id_wallet_journal_tax',
    )
    tax_receiver_id: Optional[int] = Field(
        None,
        description='The corporation ID receiving any tax paid. Only applies to tax related transactions',
        title='get_characters_character_id_wallet_journal_tax_receiver_id',
    )


class GetCharactersCharacterIdWalletJournalOk(BaseModel):
    __root__: List[GetCharactersCharacterIdWalletJournalOkItem] = Field(
        ...,
        description='Wallet journal entries',
        max_items=2500,
        title='get_characters_character_id_wallet_journal_ok',
    )


class Headers200_get_characters_character_id_wallet_journal(ModelBaseEVECelery):
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
    X_Pages: int | None = Field(description="Maximum page number", alias="X-Pages")


class Response200_get_characters_character_id_wallet_journal(ModelCachedResponse):
    """
    Journal entries

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "amount": -100000,
            "balance": 500000.4316,
            "context_id": 4,
            "context_id_type": "contract_id",
            "date": "2018-02-23T14:31:32Z",
            "description": "Contract Deposit",
            "first_party_id": 2112625428,
            "id": 89,
            "ref_type": "contract_deposit",
            "second_party_id": 1000132
          }
        ]

    """

    headers: Headers200_get_characters_character_id_wallet_journal = Field(
        ..., description='The response headers for this request.'
    )
    body: GetCharactersCharacterIdWalletJournalOk = Field(
        ..., description='The response body for this request.'
    )
