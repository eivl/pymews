# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["CompanyContractAddParams", "TravelAgencyContract", "TravelAgencyContractOptions"]


class CompanyContractAddParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    travel_agency_contracts: Required[
        Annotated[Iterable[TravelAgencyContract], PropertyInfo(alias="TravelAgencyContracts")]
    ]
    """Information about travel agency contracts to be created."""


class TravelAgencyContractOptions(TypedDict, total=False):
    include_cancellation_fee_in_commission_estimate: Annotated[
        bool, PropertyInfo(alias="IncludeCancellationFeeInCommissionEstimate")
    ]

    skip_automatic_settlement: Annotated[bool, PropertyInfo(alias="SkipAutomaticSettlement")]


class TravelAgencyContract(TypedDict, total=False):
    company_id: Required[Annotated[str, PropertyInfo(alias="CompanyId")]]

    service_id: Required[Annotated[str, PropertyInfo(alias="ServiceId")]]

    accounting_code: Annotated[Optional[str], PropertyInfo(alias="AccountingCode")]

    additional_contact_info: Annotated[Optional[str], PropertyInfo(alias="AdditionalContactInfo")]

    channel_manager_absolute_adjustment: Annotated[
        Optional[float], PropertyInfo(alias="ChannelManagerAbsoluteAdjustment")
    ]

    channel_manager_business_segment_id: Annotated[Optional[str], PropertyInfo(alias="ChannelManagerBusinessSegmentId")]

    channel_manager_relative_adjustment: Annotated[
        Optional[float], PropertyInfo(alias="ChannelManagerRelativeAdjustment")
    ]

    commission: Annotated[Optional[float], PropertyInfo(alias="Commission")]

    commission_included: Annotated[Optional[bool], PropertyInfo(alias="CommissionIncluded")]

    contact_email: Annotated[Optional[str], PropertyInfo(alias="ContactEmail")]

    contact_person: Annotated[Optional[str], PropertyInfo(alias="ContactPerson")]

    invoice_due_interval: Annotated[Optional[str], PropertyInfo(alias="InvoiceDueInterval")]

    notes: Annotated[Optional[str], PropertyInfo(alias="Notes")]

    options: Annotated[Optional[TravelAgencyContractOptions], PropertyInfo(alias="Options")]
    """Options of the travel agency contract."""
