# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = [
    "CompanyContractUpdateParams",
    "TravelAgencyContractUpdate",
    "TravelAgencyContractUpdateAccountingCode",
    "TravelAgencyContractUpdateAdditionalContactInfo",
    "TravelAgencyContractUpdateChannelManagerAbsoluteAdjustment",
    "TravelAgencyContractUpdateChannelManagerBusinessSegmentID",
    "TravelAgencyContractUpdateChannelManagerRelativeAdjustment",
    "TravelAgencyContractUpdateCommission",
    "TravelAgencyContractUpdateCommissionIncluded",
    "TravelAgencyContractUpdateContactEmail",
    "TravelAgencyContractUpdateContactPerson",
    "TravelAgencyContractUpdateInvoiceDueInterval",
    "TravelAgencyContractUpdateNotes",
    "TravelAgencyContractUpdateOptions",
    "TravelAgencyContractUpdateOptionsIncludeCancellationFeeInCommissionEstimate",
    "TravelAgencyContractUpdateOptionsSkipAutomaticSettlement",
]


class CompanyContractUpdateParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    travel_agency_contract_updates: Required[
        Annotated[Iterable[TravelAgencyContractUpdate], PropertyInfo(alias="TravelAgencyContractUpdates")]
    ]
    """Information about travel agency contracts to be updated."""


class TravelAgencyContractUpdateAccountingCode(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class TravelAgencyContractUpdateAdditionalContactInfo(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class TravelAgencyContractUpdateChannelManagerAbsoluteAdjustment(TypedDict, total=False):
    value: Annotated[Optional[float], PropertyInfo(alias="Value")]


class TravelAgencyContractUpdateChannelManagerBusinessSegmentID(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class TravelAgencyContractUpdateChannelManagerRelativeAdjustment(TypedDict, total=False):
    value: Annotated[Optional[float], PropertyInfo(alias="Value")]


class TravelAgencyContractUpdateCommission(TypedDict, total=False):
    value: Annotated[Optional[float], PropertyInfo(alias="Value")]


class TravelAgencyContractUpdateCommissionIncluded(TypedDict, total=False):
    value: Annotated[Optional[bool], PropertyInfo(alias="Value")]


class TravelAgencyContractUpdateContactEmail(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class TravelAgencyContractUpdateContactPerson(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class TravelAgencyContractUpdateInvoiceDueInterval(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class TravelAgencyContractUpdateNotes(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class TravelAgencyContractUpdateOptionsIncludeCancellationFeeInCommissionEstimate(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class TravelAgencyContractUpdateOptionsSkipAutomaticSettlement(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class TravelAgencyContractUpdateOptions(TypedDict, total=False):
    include_cancellation_fee_in_commission_estimate: Annotated[
        Optional[TravelAgencyContractUpdateOptionsIncludeCancellationFeeInCommissionEstimate],
        PropertyInfo(alias="IncludeCancellationFeeInCommissionEstimate"),
    ]

    skip_automatic_settlement: Annotated[
        Optional[TravelAgencyContractUpdateOptionsSkipAutomaticSettlement],
        PropertyInfo(alias="SkipAutomaticSettlement"),
    ]


class TravelAgencyContractUpdate(TypedDict, total=False):
    travel_agency_contract_id: Required[Annotated[str, PropertyInfo(alias="TravelAgencyContractId")]]

    accounting_code: Annotated[Optional[TravelAgencyContractUpdateAccountingCode], PropertyInfo(alias="AccountingCode")]

    additional_contact_info: Annotated[
        Optional[TravelAgencyContractUpdateAdditionalContactInfo], PropertyInfo(alias="AdditionalContactInfo")
    ]

    channel_manager_absolute_adjustment: Annotated[
        Optional[TravelAgencyContractUpdateChannelManagerAbsoluteAdjustment],
        PropertyInfo(alias="ChannelManagerAbsoluteAdjustment"),
    ]

    channel_manager_business_segment_id: Annotated[
        Optional[TravelAgencyContractUpdateChannelManagerBusinessSegmentID],
        PropertyInfo(alias="ChannelManagerBusinessSegmentId"),
    ]

    channel_manager_relative_adjustment: Annotated[
        Optional[TravelAgencyContractUpdateChannelManagerRelativeAdjustment],
        PropertyInfo(alias="ChannelManagerRelativeAdjustment"),
    ]

    commission: Annotated[Optional[TravelAgencyContractUpdateCommission], PropertyInfo(alias="Commission")]

    commission_included: Annotated[
        Optional[TravelAgencyContractUpdateCommissionIncluded], PropertyInfo(alias="CommissionIncluded")
    ]

    contact_email: Annotated[Optional[TravelAgencyContractUpdateContactEmail], PropertyInfo(alias="ContactEmail")]

    contact_person: Annotated[Optional[TravelAgencyContractUpdateContactPerson], PropertyInfo(alias="ContactPerson")]

    invoice_due_interval: Annotated[
        Optional[TravelAgencyContractUpdateInvoiceDueInterval], PropertyInfo(alias="InvoiceDueInterval")
    ]

    notes: Annotated[Optional[TravelAgencyContractUpdateNotes], PropertyInfo(alias="Notes")]

    options: Annotated[Optional[TravelAgencyContractUpdateOptions], PropertyInfo(alias="Options")]
