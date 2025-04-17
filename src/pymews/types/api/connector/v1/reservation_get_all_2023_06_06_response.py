# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["ReservationGetAll2023_06_06Response", "Reservation", "ReservationOptions", "ReservationPersonCount"]


class ReservationOptions(BaseModel):
    all_companions_checked_in: bool = FieldInfo(alias="AllCompanionsCheckedIn")
    """All companions of the reservation checked in."""

    any_companion_checked_in: bool = FieldInfo(alias="AnyCompanionCheckedIn")
    """Any of the companions of the reservation checked in."""

    connector_check_in: bool = FieldInfo(alias="ConnectorCheckIn")
    """Check in was done via Connector API."""

    owner_checked_in: bool = FieldInfo(alias="OwnerCheckedIn")
    """Owner of the reservation checked in."""


class ReservationPersonCount(BaseModel):
    age_category_id: str = FieldInfo(alias="AgeCategoryId")
    """
    Unique identifier of the
    [Age category](https://mews-systems.gitbook.io/connector-api/operations/agecategories#age-category).
    """

    count: int = FieldInfo(alias="Count")
    """Number of people of a given age category. Only positive value is accepted."""


class Reservation(BaseModel):
    account_id: str = FieldInfo(alias="AccountId")
    """Unique identifier of the Customer or Company who owns the reservation, i.e.

    the main guest linked to the reservation.
    """

    account_type: Literal["Company", "Customer"] = FieldInfo(alias="AccountType")

    created_utc: datetime = FieldInfo(alias="CreatedUtc")
    """Creation date and time of the reservation in UTC timezone."""

    creator_profile_id: str = FieldInfo(alias="CreatorProfileId")
    """Unique identifier of the user who created the reservation."""

    end_utc: datetime = FieldInfo(alias="EndUtc")
    """Scheduled end time of reservation in UTC timezone in ISO 8601 format"""

    group_id: str = FieldInfo(alias="GroupId")
    """Unique identifier of the Reservation group."""

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the reservation."""

    number: str = FieldInfo(alias="Number")
    """Confirmation number of the reservation in Mews."""

    options: ReservationOptions = FieldInfo(alias="Options")
    """Options of the reservation."""

    origin: Literal["Distributor", "ChannelManager", "Commander", "Import", "Connector", "Navigator"] = FieldInfo(
        alias="Origin"
    )
    """Distributor (From the Mews Booking Engine or Booking Engine API.)

    ChannelManager (From a channel manager.)

    Commander (From Mews Operations.)

    Import (From an import process.)

    Connector (From the Mews Connector API.)

    Navigator (From Mews Guest Services.)

    - `Distributor` - From the Mews Booking Engine or Booking Engine API.
    - `ChannelManager` - From a channel manager.
    - `Commander` - From Mews Operations.
    - `Import` - From an import process.
    - `Connector` - From the Mews Connector API.
    - `Navigator` - From Mews Guest Services.
    """

    person_counts: List[ReservationPersonCount] = FieldInfo(alias="PersonCounts")
    """Number of people per age category the reservation was booked for."""

    rate_id: str = FieldInfo(alias="RateId")
    """Identifier of the reservation `Rate`."""

    requested_resource_category_id: str = FieldInfo(alias="RequestedResourceCategoryId")
    """Unique identifier of the Resource category."""

    scheduled_end_utc: datetime = FieldInfo(alias="ScheduledEndUtc")
    """Scheduled end time of reservation in UTC timezone in ISO 8601 format."""

    scheduled_start_utc: datetime = FieldInfo(alias="ScheduledStartUtc")
    """Scheduled start time of reservation in UTC timezone."""

    service_id: str = FieldInfo(alias="ServiceId")
    """Unique identifier of the `Service` that reservation is made against."""

    start_utc: datetime = FieldInfo(alias="StartUtc")
    """
    Reservation start or check-in time (if it's earlier than scheduled start) in UTC
    timezone in ISO 8601 format.
    """

    state: Literal["Inquired", "Confirmed", "Started", "Processed", "Canceled", "Optional", "Requested"] = FieldInfo(
        alias="State"
    )
    """Inquired (Confirmed neither by the customer nor enterprise.)

    Confirmed (Confirmed by both parties, before check-in.)

    Started (Checked in.)

    Processed (Checked out.)

    Canceled (Canceled.)

    Optional (Confirmed by enterprise but not by the guest (the enterprise is
    holding resource for the guest).)

    Requested (Confirmed by the customer but not by the enterprise (waitlist).)

    - `Inquired` - Confirmed neither by the customer nor enterprise.
    - `Confirmed` - Confirmed by both parties, before check-in.
    - `Started` - Checked in.
    - `Processed` - Checked out.
    - `Canceled` - Canceled.
    - `Optional` - Confirmed by enterprise but not by the guest (the enterprise is
      holding resource for the guest).
    - `Requested` - Confirmed by the customer but not by the enterprise (waitlist).
    """

    updated_utc: datetime = FieldInfo(alias="UpdatedUtc")
    """Last update date and time of the reservation in UTC timezone."""

    updater_profile_id: str = FieldInfo(alias="UpdaterProfileId")
    """Unique identifier of the user who updated the reservation."""

    actual_end_utc: Optional[datetime] = FieldInfo(alias="ActualEndUtc", default=None)
    """Actual end time of reservation in UTC timezone in ISO 8601 format."""

    actual_start_utc: Optional[datetime] = FieldInfo(alias="ActualStartUtc", default=None)
    """Actual customer check-in time of reservation in UTC timezone."""

    assigned_resource_id: Optional[str] = FieldInfo(alias="AssignedResourceId", default=None)
    """Identifier of the assigned Resource."""

    assigned_resource_locked: Optional[bool] = FieldInfo(alias="AssignedResourceLocked", default=None)
    """Whether the reservation is locked to the assigned Resource and cannot be moved."""

    availability_block_id: Optional[str] = FieldInfo(alias="AvailabilityBlockId", default=None)
    """Unique identifier of the Availability block the reservation is assigned to."""

    booker_id: Optional[str] = FieldInfo(alias="BookerId", default=None)
    """
    Unique identifier of the booker who made the reservation on behalf of the
    reservation owner, in the special case where the booker is also a registered
    customer in Mews.
    """

    business_segment_id: Optional[str] = FieldInfo(alias="BusinessSegmentId", default=None)
    """Identifier of the reservation `BusinessSegment`."""

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
    """Other

    ConfirmationMissed

    BookedElsewhere

    ForceMajeure

    GuestComplaint

    NoShow

    PriceTooHigh

    ServiceNotAvailable

    InputError

    InvalidPayment

    TravelAgency

    RequestedByGuest

    Update

    BookingAbandoned

    RequestedByBooker
    """

    cancelled_utc: Optional[datetime] = FieldInfo(alias="CancelledUtc", default=None)
    """Cancellation date and time in UTC timezone."""

    channel_manager_number: Optional[str] = FieldInfo(alias="ChannelManagerNumber", default=None)
    """Unique number of the reservation within the reservation group."""

    channel_number: Optional[str] = FieldInfo(alias="ChannelNumber", default=None)
    """Number of the reservation within the Channel (i.e.

    OTA, GDS, CRS, etc) in case the reservation group originates there (e.g.
    Booking.com confirmation number).
    """

    commander_origin: Optional[Literal["InPerson", "Channel", "Phone", "Email", "Website", "Message", "CallCenter"]] = (
        FieldInfo(alias="CommanderOrigin", default=None)
    )
    """InPerson

    Channel

    Phone

    Email

    Website

    Message

    CallCenter
    """

    credit_card_id: Optional[str] = FieldInfo(alias="CreditCardId", default=None)
    """Unique identifier of the Credit card."""

    origin_details: Optional[str] = FieldInfo(alias="OriginDetails", default=None)
    """Details about the reservation `Origin`."""

    partner_company_id: Optional[str] = FieldInfo(alias="PartnerCompanyId", default=None)
    """Identifier of the `Company` on behalf of which the reservation was made."""

    purpose: Optional[Literal["Leisure", "Business", "Student"]] = FieldInfo(alias="Purpose", default=None)
    """Leisure

    Business

    Student
    """

    qr_code_data: Optional[str] = FieldInfo(alias="QrCodeData", default=None)
    """QR code data of the reservation."""

    released_utc: Optional[datetime] = FieldInfo(alias="ReleasedUtc", default=None)
    """Date when the optional reservation is released in UTC timezone."""

    travel_agency_id: Optional[str] = FieldInfo(alias="TravelAgencyId", default=None)
    """Identifier of the Travel Agency (`Company`) that mediated the reservation."""

    voucher_id: Optional[str] = FieldInfo(alias="VoucherId", default=None)
    """Unique identifier of the `Voucher` that has been used to create reservation."""


class ReservationGetAll2023_06_06Response(BaseModel):
    reservations: List[Reservation] = FieldInfo(alias="Reservations")
    """The reservations of the enterprise."""

    cursor: Optional[str] = FieldInfo(alias="Cursor", default=None)
    """
    Unique identifier of the item one newer in time order than the items to be
    returned. If Cursor is not specified, i.e. null, then the latest or most recent
    items will be returned.
    """
