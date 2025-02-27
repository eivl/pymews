# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["AvailabilityBlockAddResult", "AvailabilityBlock", "AvailabilityBlockBudget"]


class AvailabilityBlockBudget(BaseModel):
    currency: str = FieldInfo(alias="Currency")

    net: Optional[float] = FieldInfo(alias="Net", default=None)

    tax: Optional[float] = FieldInfo(alias="Tax", default=None)

    tax_rate: Optional[float] = FieldInfo(alias="TaxRate", default=None)

    value: Optional[float] = FieldInfo(alias="Value", default=None)


class AvailabilityBlock(BaseModel):
    availability_block_number: str = FieldInfo(alias="AvailabilityBlockNumber")
    """Unique number for a specific availability block within the Mews system."""

    created_utc: str = FieldInfo(alias="CreatedUtc")
    """Creation date and time of the block in UTC timezone in ISO 8601 format."""

    first_time_unit_start_utc: str = FieldInfo(alias="FirstTimeUnitStartUtc")
    """
    Start of the time interval, expressed as the timestamp for the start of the
    first time unit, in UTC timezone ISO 8601 format. See
    [Time units](https://mews-systems.gitbook.io/connector-api/concepts/time-units).
    """

    is_active: bool = FieldInfo(alias="IsActive")
    """Whether the `Availability Block` is still active."""

    last_time_unit_start_utc: str = FieldInfo(alias="LastTimeUnitStartUtc")
    """
    End of the time interval, expressed as the timestamp for the start of the last
    time unit, in UTC timezone ISO 8601 format. See
    [Time units](https://mews-systems.gitbook.io/connector-api/concepts/time-units).
    """

    pickup_distribution: Literal["AllInOneGroup", "IndividualGroups"] = FieldInfo(alias="PickupDistribution")
    """
    AllInOneGroup (All created reservations in the block are added to the same
    reservation group.)

    IndividualGroups (Reservations can be picked up in multiple groups, with up to
    750 reservations per group.)

    - `AllInOneGroup` - All created reservations in the block are added to the same
      reservation group.
    - `IndividualGroups` - Reservations can be picked up in multiple groups, with up
      to 750 reservations per group.
    """

    release_strategy: Literal["FixedRelease", "RollingRelease", "None"] = FieldInfo(alias="ReleaseStrategy")
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

    state: Literal["Confirmed", "Optional", "Inquired", "Canceled"] = FieldInfo(alias="State")
    """Confirmed (The block deducts availability and can have reservations assigned.)

    Optional (The block deducts availability and cannot have reservations assigned.)

    Inquired (The block does not deduct availability and cannot have reservations
    assigned (waitlist).)

    Canceled (The block does not deduct availability and cannot have reservations
    assigned (waitlist).)

    - `Confirmed` - The block deducts availability and can have reservations
      assigned.
    - `Optional` - The block deducts availability and cannot have reservations
      assigned.
    - `Inquired` - The block does not deduct availability and cannot have
      reservations assigned (waitlist).
    - `Canceled` - The block does not deduct availability and cannot have
      reservations assigned (waitlist).
    """

    updated_utc: str = FieldInfo(alias="UpdatedUtc")
    """Last update date and time of the block in UTC timezone in ISO 8601 format."""

    booker_id: Optional[str] = FieldInfo(alias="BookerId", default=None)
    """Unique identifier of the `Customer` on whose behalf the block was made."""

    budget: Optional[AvailabilityBlockBudget] = FieldInfo(alias="Budget", default=None)
    """Total price of the reservation."""

    company_id: Optional[str] = FieldInfo(alias="CompanyId", default=None)
    """Unique identifier of the `Company` linked to the block."""

    enterprise_id: Optional[str] = FieldInfo(alias="EnterpriseId", default=None)
    """
    Unique identifier of the
    [enterprise](https://mews-systems.gitbook.io/connector-api/operations/enterprises#enterprise).
    """

    external_identifier: Optional[str] = FieldInfo(alias="ExternalIdentifier", default=None)
    """Identifier of the block from external system."""

    id: Optional[str] = FieldInfo(alias="Id", default=None)
    """Unique identifier of the availability block."""

    name: Optional[str] = FieldInfo(alias="Name", default=None)
    """The name of the block in Mews."""

    notes: Optional[str] = FieldInfo(alias="Notes", default=None)
    """Additional notes of the block."""

    quote_id: Optional[str] = FieldInfo(alias="QuoteId", default=None)
    """
    Unique identifier of the Mews Events quote associated with the availability
    block.
    """

    rate_id: Optional[str] = FieldInfo(alias="RateId", default=None)
    """Unique identifier of the `Rate` the block is assigned to."""

    released_utc: Optional[str] = FieldInfo(alias="ReleasedUtc", default=None)
    """
    The moment when the block and its availability is released in UTC timezone in
    ISO 8601 format. Mutually exclusive with `RollingReleaseOffset`; the block will
    not be automatically released if neither `ReleasedUtc` nor
    `RollingReleaseOffsetUtc` is specified.
    """

    reservation_purpose: Optional[Literal["Leisure", "Business", "Student"]] = FieldInfo(
        alias="ReservationPurpose", default=None
    )
    """Leisure

    Business

    Student
    """

    rolling_release_offset: Optional[str] = FieldInfo(alias="RollingReleaseOffset", default=None)
    """
    Exact offset from the start of availability adjustments to the moment the
    individual days in the adjustment should be released, in ISO 8601 duration
    format. Mutually exclusive with `ReleasedUtc`; the block will not be
    automatically released if neither `ReleasedUtc` nor `RollingReleaseOffsetUtc` is
    specified.
    """

    service_id: Optional[str] = FieldInfo(alias="ServiceId", default=None)
    """Unique identifier of the `Service` the block is assigned to."""

    travel_agency_id: Optional[str] = FieldInfo(alias="TravelAgencyId", default=None)
    """
    Unique identifier of `Company`with `Travel agency contract` the Availability
    Block is related to.
    """

    voucher_id: Optional[str] = FieldInfo(alias="VoucherId", default=None)
    """Unique identifier of the `Voucher` used to access specified private `Rate`."""


class AvailabilityBlockAddResult(BaseModel):
    availability_blocks: List[AvailabilityBlock] = FieldInfo(alias="AvailabilityBlocks")
    """Availability blocks."""
