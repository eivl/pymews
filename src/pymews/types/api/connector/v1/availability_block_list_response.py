# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = [
    "AvailabilityBlockListResponse",
    "Adjustment",
    "AdjustmentPaxCount",
    "AvailabilityBlock",
    "AvailabilityBlockBudget",
    "Rate",
    "ServiceOrder",
    "ServiceOrderOptions",
    "ServiceOrderPersonCount",
]


class AdjustmentPaxCount(BaseModel):
    person_count: int = FieldInfo(alias="PersonCount")
    """Predicted guest count that will be assigned to the Resource.

    The guest count must fit within the Resource Category maximum capacity.
    """

    unit_count: int = FieldInfo(alias="UnitCount")
    """Positive number of adjustments that are assigned to `PersonCount`.

    The sum of all `UnitCount` in `PaxCounts` should match the adjustment value
    applied to the interval.
    """


class Adjustment(BaseModel):
    activity_state: Literal["Deleted", "Active"] = FieldInfo(alias="ActivityState")
    """Deleted

    Active
    """

    first_time_unit_start_utc: datetime = FieldInfo(alias="FirstTimeUnitStartUtc")
    """
    Start of the time interval, expressed as the timestamp for the start of the
    first
    [time unit](https://mews-systems.gitbook.io/connector-api/operations/services/#time-unit),
    in UTC timezone ISO 8601 format.
    """

    id: str = FieldInfo(alias="Id")
    """
    Unique identifier of the
    [Availability adjustment](https://mews-systems.gitbook.io/connector-api/operations/#availability-adjustment).
    """

    is_active: bool = FieldInfo(alias="IsActive")
    """Whether the availability adjustment is still active."""

    last_time_unit_start_utc: datetime = FieldInfo(alias="LastTimeUnitStartUtc")
    """
    End of the time interval, expressed as the timestamp for the start of the last
    [time unit](https://mews-systems.gitbook.io/connector-api/operations/services/#time-unit),
    in UTC timezone ISO 8601 format.
    """

    resource_category_id: str = FieldInfo(alias="ResourceCategoryId")
    """
    Unique identifier of the
    [Resource category](https://mews-systems.gitbook.io/connector-api/operations/resources/#resource-category)
    whose availability is updated.
    """

    unit_count: int = FieldInfo(alias="UnitCount")
    """Adjustment value applied on the interval."""

    updated_utc: datetime = FieldInfo(alias="UpdatedUtc")
    """Last update date and time of the adjustment in UTC timezone in ISO 8601 format."""

    availability_block_id: Optional[str] = FieldInfo(alias="AvailabilityBlockId", default=None)
    """
    Unique identifier of the
    [Availability block](https://mews-systems.gitbook.io/connector-api/operations/availabilityblocks/#availability-block)
    which the availability adjustment belongs to.
    """

    end_utc: Optional[str] = FieldInfo(alias="EndUtc", default=None)
    """End of the interval in UTC timezone in ISO 8601 format."""

    pax_counts: Optional[List[AdjustmentPaxCount]] = FieldInfo(alias="PaxCounts", default=None)
    """Collection of predicted occupancy of availability adjustments.

    Relates to how many adjustments are assigned to each count of guests.
    """

    release_override_utc: Optional[datetime] = FieldInfo(alias="ReleaseOverrideUtc", default=None)
    """
    Exact moment the availability adjustment is released; overrides the release
    strategy of the associated availability block.
    """

    start_utc: Optional[str] = FieldInfo(alias="StartUtc", default=None)
    """Start of the interval in UTC timezone in ISO 8601 format."""


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


class Rate(BaseModel):
    group_id: str = FieldInfo(alias="GroupId")
    """Unique identifier of `Rate Group` where the rate belongs."""

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the rate."""

    is_active: bool = FieldInfo(alias="IsActive")
    """Whether the rate is still active."""

    is_base_rate: bool = FieldInfo(alias="IsBaseRate")
    """Whether the rate is a base rate."""

    is_enabled: bool = FieldInfo(alias="IsEnabled")
    """Whether the rate is currently available to customers."""

    is_public: bool = FieldInfo(alias="IsPublic")
    """Whether the rate is publicly available."""

    names: Dict[str, str] = FieldInfo(alias="Names")
    """All translations of the name."""

    service_id: str = FieldInfo(alias="ServiceId")
    """Unique identifier of the `Service`."""

    type: Literal["Public", "Private", "AvailabilityBlock"] = FieldInfo(alias="Type")
    """Public

    Private

    AvailabilityBlock
    """

    updated_utc: datetime = FieldInfo(alias="UpdatedUtc")
    """Interval in which the rates were updated."""

    base_rate_id: Optional[str] = FieldInfo(alias="BaseRateId", default=None)
    """Unique identifier of the base `Rate`."""

    business_segment_id: Optional[str] = FieldInfo(alias="BusinessSegmentId", default=None)
    """Unique identifier of the `Business Segment`."""

    description: Optional[Dict[str, str]] = FieldInfo(alias="Description", default=None)
    """All translations of the description of the rate."""

    external_identifier: Optional[str] = FieldInfo(alias="ExternalIdentifier", default=None)
    """Identifier of the rate from external system."""

    external_names: Optional[Dict[str, str]] = FieldInfo(alias="ExternalNames", default=None)
    """All translations of the external name of the rate."""

    name: Optional[str] = FieldInfo(alias="Name", default=None)
    """Name of the rate (in the default language)."""

    short_name: Optional[str] = FieldInfo(alias="ShortName", default=None)
    """Short name of the rate (in the default language)."""


class ServiceOrderOptions(BaseModel):
    all_companions_checked_in: bool = FieldInfo(alias="AllCompanionsCheckedIn")
    """All companions of the reservation checked in."""

    any_companion_checked_in: bool = FieldInfo(alias="AnyCompanionCheckedIn")
    """Any companion of the reservation checked in."""

    owner_checked_in: bool = FieldInfo(alias="OwnerCheckedIn")
    """Owner of the reservation checked in."""


class ServiceOrderPersonCount(BaseModel):
    age_category_id: str = FieldInfo(alias="AgeCategoryId")
    """
    Unique identifier of the
    [Age category](https://mews-systems.gitbook.io/connector-api/operations/agecategories#age-category).
    """

    count: int = FieldInfo(alias="Count")
    """Number of people of a given age category. Only positive value is accepted."""


class ServiceOrder(BaseModel):
    assigned_resource_locked: bool = FieldInfo(alias="AssignedResourceLocked")
    """Whether the reservation is locked to the assigned Resource and cannot be moved."""

    companion_ids: List[str] = FieldInfo(alias="CompanionIds")
    """Unique identifiers of the `Customer`s that will use the resource."""

    created_utc: str = FieldInfo(alias="CreatedUtc")
    """Creation date and time of the reservation in UTC timezone in ISO 8601 format."""

    customer_id: str = FieldInfo(alias="CustomerId")
    """Unique identifier of the Customer who owns the reservation."""

    end_utc: str = FieldInfo(alias="EndUtc")
    """End of the reservation (departure) in UTC timezone in ISO 8601 format."""

    group_id: str = FieldInfo(alias="GroupId")
    """Unique identifier of the Reservation group."""

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the reservation."""

    number: str = FieldInfo(alias="Number")
    """Confirmation number of the reservation in Mews."""

    options: ServiceOrderOptions = FieldInfo(alias="Options")
    """Options of the reservation."""

    origin: Literal[
        "Distributor",
        "ChannelManager",
        "Import",
        "Connector",
        "Navigator",
        "CommanderInPerson",
        "CommanderChannel",
        "CommanderPhone",
        "CommanderEmail",
        "CommanderWebsite",
        "CommanderMessage",
        "CommanderCallCenter",
    ] = FieldInfo(alias="Origin")
    """
    - `Distributor` - From the Mews Booking Engine or Booking Engine API.
    - `ChannelManager` - From a channel manager.
    - `Import` - From an import process.
    - `Connector` - From the Mews Connector API.
    - `Navigator` - From Mews Guest Services.
    - `CommanderInPerson` - From Mews Operations, in person.
    - `CommanderChannel` - From Mews Operations, via channel.
    - `CommanderPhone` - From Mews Operations, via telephone.
    - `CommanderEmail` - From Mews Operations, via email.
    - `CommanderWebsite` - From Mews Operations, via website.
    - `CommanderMessage` - From Mews Operations, via message person.
    - `CommanderCallCenter` - From Mews Operations, via call center.
    """

    owner_id: str = FieldInfo(alias="OwnerId")
    """Unique identifier of the Customer or Company who owns the reservation."""

    person_counts: List[ServiceOrderPersonCount] = FieldInfo(alias="PersonCounts")
    """Number of people per age category the reservation was booked for."""

    rate_id: str = FieldInfo(alias="RateId")
    """Identifier of the reservation Rate."""

    requested_category_id: str = FieldInfo(alias="RequestedCategoryId")
    """Identifier of the requested Resource category."""

    service_id: str = FieldInfo(alias="ServiceId")
    """Unique identifier of the Service that is reserved."""

    start_utc: str = FieldInfo(alias="StartUtc")
    """Start of the reservation in UTC timezone in ISO 8601 format.

    This is either the scheduled reservation start time, or the actual customer
    check-in time if this is earlier than the scheduled start time.
    """

    state: Literal["Enquired", "Confirmed", "Started", "Processed", "Canceled", "Optional", "Requested"] = FieldInfo(
        alias="State"
    )

    updated_utc: str = FieldInfo(alias="UpdatedUtc")
    """
    Last update date and time of the reservation in UTC timezone in ISO 8601 format.
    """

    adult_count: Optional[int] = FieldInfo(alias="AdultCount", default=None)
    """Count of adults the reservation was booked for."""

    assigned_resource_id: Optional[str] = FieldInfo(alias="AssignedResourceId", default=None)
    """Identifier of the assigned Resource."""

    assigned_space_id: Optional[str] = FieldInfo(alias="AssignedSpaceId", default=None)
    """Identifier of the assigned Space."""

    assigned_space_locked: Optional[bool] = FieldInfo(alias="AssignedSpaceLocked", default=None)
    """Whether the reservation is locked to the assigned Space and cannot be moved."""

    availability_block_id: Optional[str] = FieldInfo(alias="AvailabilityBlockId", default=None)
    """Unique identifier of the Availability block the reservation is assigned to."""

    booker_id: Optional[str] = FieldInfo(alias="BookerId", default=None)
    """Unique identifier of the Customer on whose behalf the reservation was made."""

    business_segment_id: Optional[str] = FieldInfo(alias="BusinessSegmentId", default=None)
    """Identifier of the reservation Business segment."""

    cancellation_reason: Optional[
        Literal[
            "Other",
            "ConfirmationMissed",
            "BookedElsewhere",
            "ForceMajeure",
            "GuestComplaint",
            "NoShow",
            "PriceTooHigh",
            "ServiceNotAvailable",
            "InputError",
            "InvalidPayment",
            "TravelAgency",
            "RequestedByGuest",
            "Update",
            "BookingAbandoned",
            "RequestedByBooker",
        ]
    ] = FieldInfo(alias="CancellationReason", default=None)
    """Cancellation reason of the reservation."""

    cancelled_utc: Optional[str] = FieldInfo(alias="CancelledUtc", default=None)
    """Cancellation date and time in UTC timezone in ISO 8601 format."""

    channel_manager: Optional[str] = FieldInfo(alias="ChannelManager", default=None)
    """Name of the Channel manager (e.g. AvailPro, SiteMinder, TravelClick, etc)."""

    channel_manager_group_number: Optional[str] = FieldInfo(alias="ChannelManagerGroupNumber", default=None)
    """
    Number of the reservation group within a Channel manager that transferred the
    reservation from Channel to Mews.
    """

    channel_manager_id: Optional[str] = FieldInfo(alias="ChannelManagerId", default=None)
    """Channel Manager number."""

    channel_manager_number: Optional[str] = FieldInfo(alias="ChannelManagerNumber", default=None)
    """Unique number of the reservation within the reservation group."""

    channel_number: Optional[str] = FieldInfo(alias="ChannelNumber", default=None)
    """Number of the reservation within the Channel (i.e.

    OTA, GDS, CRS, etc) in case the reservation group originates there (e.g.
    Booking.com confirmation number).
    """

    child_count: Optional[int] = FieldInfo(alias="ChildCount", default=None)
    """Count of children the reservation was booked for."""

    company_id: Optional[str] = FieldInfo(alias="CompanyId", default=None)
    """Identifier of the Company on behalf of which the reservation was made."""

    credit_card_id: Optional[str] = FieldInfo(alias="CreditCardId", default=None)
    """Unique identifier of the Credit card."""

    origin_details: Optional[str] = FieldInfo(alias="OriginDetails", default=None)
    """Details about the reservation origin."""

    purpose: Optional[Literal["Leisure", "Business", "Student"]] = FieldInfo(alias="Purpose", default=None)
    """Purpose of the reservation."""

    released_utc: Optional[str] = FieldInfo(alias="ReleasedUtc", default=None)
    """
    Date when the optional reservation is released in UTC timezone in ISO 8601
    format.
    """

    travel_agency_id: Optional[str] = FieldInfo(alias="TravelAgencyId", default=None)
    """Identifier of the Company that mediated the reservation."""

    voucher_id: Optional[str] = FieldInfo(alias="VoucherId", default=None)
    """Unique identifier of the Voucher that has been used to create reservation."""


class AvailabilityBlockListResponse(BaseModel):
    adjustments: Optional[List[Adjustment]] = FieldInfo(alias="Adjustments", default=None)
    """Availability adjustments of availability blocks."""

    availability_blocks: Optional[List[AvailabilityBlock]] = FieldInfo(alias="AvailabilityBlocks", default=None)
    """Availability blocks."""

    cursor: Optional[str] = FieldInfo(alias="Cursor", default=None)
    """Unique identifier of the last returned availability block.

    This can be used in Limitation in a subsequent request to fetch the next batch
    of availability block.
    """

    rates: Optional[List[Rate]] = FieldInfo(alias="Rates", default=None)
    """`Rates` assigned to the block."""

    service_orders: Optional[List[ServiceOrder]] = FieldInfo(alias="ServiceOrders", default=None)
    """Service orders (for example reservations) linked to availability blocks."""
