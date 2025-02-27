# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from . import customer as _customer
from ....._models import BaseModel

__all__ = [
    "CustomerSearchResponse",
    "Customer",
    "CustomerReservation",
    "CustomerReservationOptions",
    "CustomerReservationPersonCount",
    "Document",
]


class CustomerReservationOptions(BaseModel):
    all_companions_checked_in: bool = FieldInfo(alias="AllCompanionsCheckedIn")
    """All companions of the reservation checked in."""

    any_companion_checked_in: bool = FieldInfo(alias="AnyCompanionCheckedIn")
    """Any companion of the reservation checked in."""

    owner_checked_in: bool = FieldInfo(alias="OwnerCheckedIn")
    """Owner of the reservation checked in."""


class CustomerReservationPersonCount(BaseModel):
    age_category_id: str = FieldInfo(alias="AgeCategoryId")
    """
    Unique identifier of the
    [Age category](https://mews-systems.gitbook.io/connector-api/operations/agecategories#age-category).
    """

    count: int = FieldInfo(alias="Count")
    """Number of people of a given age category. Only positive value is accepted."""


class CustomerReservation(BaseModel):
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

    options: CustomerReservationOptions = FieldInfo(alias="Options")
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

    person_counts: List[CustomerReservationPersonCount] = FieldInfo(alias="PersonCounts")
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


class Customer(BaseModel):
    customer: _customer.Customer = FieldInfo(alias="Customer")
    """The found customer."""

    reservation: Optional[CustomerReservation] = FieldInfo(alias="Reservation", default=None)


class Document(BaseModel):
    customer_id: Optional[str] = FieldInfo(alias="CustomerId", default=None)
    """Identifier of the `Customer`."""

    expiration: Optional[date] = FieldInfo(alias="Expiration", default=None)
    """Expiration date in ISO 8601 format."""

    id: Optional[str] = FieldInfo(alias="Id", default=None)
    """Unique identifier of the document."""

    identity_document_support_number: Optional[str] = FieldInfo(alias="IdentityDocumentSupportNumber", default=None)
    """Identity document support number.

    Only required for Spanish identity cards in Spanish hotels.
    """

    issuance: Optional[date] = FieldInfo(alias="Issuance", default=None)
    """Date of issuance in ISO 8601 format."""

    issuing_city: Optional[str] = FieldInfo(alias="IssuingCity", default=None)
    """City where the document was issued."""

    issuing_country_code: Optional[str] = FieldInfo(alias="IssuingCountryCode", default=None)
    """ISO 3166-1 code of the `Country`."""

    number: Optional[str] = FieldInfo(alias="Number", default=None)
    """Number of the document (e.g. passport number)."""

    type: Optional[Literal["IdentityCard", "Passport", "Visa", "DriversLicense"]] = FieldInfo(
        alias="Type", default=None
    )
    """IdentityCard

    Passport

    Visa

    DriversLicense
    """


class CustomerSearchResponse(BaseModel):
    customers: List[Customer] = FieldInfo(alias="Customers")
    """The customer search results."""

    documents: Optional[List[Document]] = FieldInfo(alias="Documents", default=None)
    """The identity documents of customers."""
