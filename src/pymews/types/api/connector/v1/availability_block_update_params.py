# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = [
    "AvailabilityBlockUpdateParams",
    "AvailabilityBlock",
    "AvailabilityBlockBookerID",
    "AvailabilityBlockBudget",
    "AvailabilityBlockBudgetValue",
    "AvailabilityBlockCancellationReason",
    "AvailabilityBlockCancellationReasonDetail",
    "AvailabilityBlockCompanyID",
    "AvailabilityBlockExternalIdentifier",
    "AvailabilityBlockFirstTimeUnitStartUtc",
    "AvailabilityBlockLastTimeUnitStartUtc",
    "AvailabilityBlockName",
    "AvailabilityBlockNotes",
    "AvailabilityBlockQuoteID",
    "AvailabilityBlockReleasedUtc",
    "AvailabilityBlockReleaseStrategy",
    "AvailabilityBlockReservationPurpose",
    "AvailabilityBlockRollingReleaseOffset",
    "AvailabilityBlockState",
    "AvailabilityBlockTravelAgencyID",
]


class AvailabilityBlockUpdateParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    availability_blocks: Required[Annotated[Iterable[AvailabilityBlock], PropertyInfo(alias="AvailabilityBlocks")]]
    """Availability blocks to be updated."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    enterprise_id: Annotated[Optional[str], PropertyInfo(alias="EnterpriseId")]
    """Unique identifier of the enterprise.

    Required when using
    [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
    ignored otherwise.
    """


class AvailabilityBlockBookerID(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AvailabilityBlockBudgetValue(TypedDict, total=False):
    currency: Required[Annotated[str, PropertyInfo(alias="Currency")]]

    net: Annotated[Optional[float], PropertyInfo(alias="Net")]

    tax: Annotated[Optional[float], PropertyInfo(alias="Tax")]

    tax_rate: Annotated[Optional[float], PropertyInfo(alias="TaxRate")]

    value: Annotated[Optional[float], PropertyInfo(alias="Value")]


class AvailabilityBlockBudget(TypedDict, total=False):
    value: Annotated[Optional[AvailabilityBlockBudgetValue], PropertyInfo(alias="Value")]
    """Total price of the reservation."""


class AvailabilityBlockCancellationReason(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AvailabilityBlockCancellationReasonDetail(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AvailabilityBlockCompanyID(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AvailabilityBlockExternalIdentifier(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AvailabilityBlockFirstTimeUnitStartUtc(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AvailabilityBlockLastTimeUnitStartUtc(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AvailabilityBlockName(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AvailabilityBlockNotes(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AvailabilityBlockQuoteID(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AvailabilityBlockReleasedUtc(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AvailabilityBlockReleaseStrategy(TypedDict, total=False):
    value: Annotated[Literal["FixedRelease", "RollingRelease", "None"], PropertyInfo(alias="Value")]
    """The strategy for automatic release of the availability block.

    FixedRelease (The availability block is released at a fixed time.)

    RollingRelease (Each availability adjustment is released at a fixed offset from
    its start.)

    None (The availability block is not automatically released.)

    - `FixedRelease` - The availability block is released at a fixed time.
    - `RollingRelease` - Each availability adjustment is released at a fixed offset
      from its start.
    - `None` - The availability block is not automatically released.
    """


class AvailabilityBlockReservationPurpose(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AvailabilityBlockRollingReleaseOffset(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AvailabilityBlockState(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AvailabilityBlockTravelAgencyID(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AvailabilityBlock(TypedDict, total=False):
    availability_block_id: Annotated[str, PropertyInfo(alias="AvailabilityBlockId")]
    """
    Unique identifier of the
    [Availability block](https://mews-systems.gitbook.io/connector-api/operations/availabilityblocks#availability-block).
    """

    booker_id: Annotated[Optional[AvailabilityBlockBookerID], PropertyInfo(alias="BookerId")]
    """
    Unique identifier of the Booker as a creator of an availability block (or `null`
    if not updated).
    """

    budget: Annotated[Optional[AvailabilityBlockBudget], PropertyInfo(alias="Budget")]
    """
    The tentative budget for the total price of reservations (or `null` if not
    updated).
    """

    cancellation_reason: Annotated[
        Optional[AvailabilityBlockCancellationReason], PropertyInfo(alias="CancellationReason")
    ]
    """Cancellation reason of the availability block (or `null` if not updated)."""

    cancellation_reason_detail: Annotated[
        Optional[AvailabilityBlockCancellationReasonDetail], PropertyInfo(alias="CancellationReasonDetail")
    ]
    """
    Cancellation reason detail of the availability block (or `null` if not updated).
    """

    company_id: Annotated[Optional[AvailabilityBlockCompanyID], PropertyInfo(alias="CompanyId")]
    """
    Unique identifier of the
    [Company](https://mews-systems.gitbook.io/connector-api/operations/companies#company)
    (or `null` if not updated).
    """

    external_identifier: Annotated[
        Optional[AvailabilityBlockExternalIdentifier], PropertyInfo(alias="ExternalIdentifier")
    ]
    """
    Identifier of the block from external system (or `null` if the identifier should
    not be updated).
    """

    first_time_unit_start_utc: Annotated[
        Optional[AvailabilityBlockFirstTimeUnitStartUtc], PropertyInfo(alias="FirstTimeUnitStartUtc")
    ]
    """
    Start of the time interval, expressed as the timestamp for the start of the
    first time unit, in UTC timezone ISO 8601 format (or `null` if the start time
    should not be updated).
    """

    last_time_unit_start_utc: Annotated[
        Optional[AvailabilityBlockLastTimeUnitStartUtc], PropertyInfo(alias="LastTimeUnitStartUtc")
    ]
    """
    End of the time interval, expressed as the timestamp for the start of the last
    time unit, in UTC timezone ISO 8601 format (or `null` if the end time should not
    be updated).
    """

    name: Annotated[Optional[AvailabilityBlockName], PropertyInfo(alias="Name")]
    """The name of the block (or `null` if the name should not be updated)."""

    notes: Annotated[Optional[AvailabilityBlockNotes], PropertyInfo(alias="Notes")]
    """Additional notes of the block (or `null` if not updated)."""

    quote_id: Annotated[Optional[AvailabilityBlockQuoteID], PropertyInfo(alias="QuoteId")]
    """
    Unique identifier of the Mews Events quote associated with the availability
    block (or `null` if not updated).
    """

    released_utc: Annotated[Optional[AvailabilityBlockReleasedUtc], PropertyInfo(alias="ReleasedUtc")]
    """
    The moment when the block and its availability is released, in UTC timezone ISO
    8601 format. Required if `ReleaseStrategy` is set to `FixedRelease`, or used
    when `ReleaseStrategy` update is unspecified.
    """

    release_strategy: Annotated[Optional[AvailabilityBlockReleaseStrategy], PropertyInfo(alias="ReleaseStrategy")]
    """
    The strategy for automatic release of the availability block (or `null` if not
    updated).
    """

    reservation_purpose: Annotated[
        Optional[AvailabilityBlockReservationPurpose], PropertyInfo(alias="ReservationPurpose")
    ]
    """The purpose of the block (or `null` if not updated)."""

    rolling_release_offset: Annotated[
        Optional[AvailabilityBlockRollingReleaseOffset], PropertyInfo(alias="RollingReleaseOffset")
    ]
    """
    Exact offset from the start of availability adjustments to the moment the
    availability adjustment should be released, in ISO 8601 duration format.
    Required if `ReleaseStrategy` is set to `RollingRelease`, ignored otherwise.
    """

    state: Annotated[Optional[AvailabilityBlockState], PropertyInfo(alias="State")]
    """State of the availability block (or `null` if not updated)."""

    travel_agency_id: Annotated[Optional[AvailabilityBlockTravelAgencyID], PropertyInfo(alias="TravelAgencyId")]
    """Unique identifier of the travel agency (i.e.

    `Company`; or `null` if not updated).
    """
