# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = [
    "ReservationUpdateParams",
    "ReservationUpdate",
    "ReservationUpdateAssignedResourceID",
    "ReservationUpdateAssignedResourceLocked",
    "ReservationUpdateAvailabilityBlockID",
    "ReservationUpdateBookerID",
    "ReservationUpdateBusinessSegmentID",
    "ReservationUpdateChannelNumber",
    "ReservationUpdateCompanyID",
    "ReservationUpdateCreditCardID",
    "ReservationUpdateEndUtc",
    "ReservationUpdateOptions",
    "ReservationUpdateOptionsOwnerCheckedIn",
    "ReservationUpdatePersonCounts",
    "ReservationUpdatePersonCountsValue",
    "ReservationUpdatePurpose",
    "ReservationUpdateRateID",
    "ReservationUpdateReleasedUtc",
    "ReservationUpdateRequestedCategoryID",
    "ReservationUpdateStartUtc",
    "ReservationUpdateTimeUnitPrices",
    "ReservationUpdateTimeUnitPricesValue",
    "ReservationUpdateTimeUnitPricesValueAmount",
    "ReservationUpdateTravelAgencyID",
    "AssignedResourceID",
    "AssignedResourceLocked",
    "AvailabilityBlockID",
    "BookerID",
    "BusinessSegmentID",
    "ChannelNumber",
    "CompanyID",
    "CreditCardID",
    "EndUtc",
    "Options",
    "OptionsOwnerCheckedIn",
    "PersonCounts",
    "PersonCountsValue",
    "Purpose",
    "RateID",
    "ReleasedUtc",
    "RequestedCategoryID",
    "StartUtc",
    "TimeUnitPrices",
    "TimeUnitPricesValue",
    "TimeUnitPricesValueAmount",
    "TravelAgencyID",
]


class ReservationUpdateParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    reservation_id: Required[Annotated[str, PropertyInfo(alias="ReservationId")]]
    """Unique identifier of the reservation."""

    reservation_updates: Required[Annotated[Iterable[ReservationUpdate], PropertyInfo(alias="ReservationUpdates")]]
    """Array of properties to be updated in each reservation specified."""

    apply_cancellation_fee: Annotated[Optional[bool], PropertyInfo(alias="ApplyCancellationFee")]
    """
    Whether the cancellation fees should be applied according to rate cancellation
    policies. If not specified, the cancellation fees are applied.
    """

    assigned_resource_id: Annotated[Optional[AssignedResourceID], PropertyInfo(alias="AssignedResourceId")]
    """Identifier of the assigned `Resource`."""

    assigned_resource_locked: Annotated[Optional[AssignedResourceLocked], PropertyInfo(alias="AssignedResourceLocked")]
    """Whether the reservation should be locked to the assigned `Resource`.

    Unlocking and assigning reservation to new `Resource` can be done in one call.
    """

    availability_block_id: Annotated[Optional[AvailabilityBlockID], PropertyInfo(alias="AvailabilityBlockId")]
    """Unique identifier of the `AvailabilityBlock` the reservation is assigned to."""

    booker_id: Annotated[Optional[BookerID], PropertyInfo(alias="BookerId")]
    """Identifier of the `Customer` on whose behalf the reservation was made.

    (or `null` if the booker should not be updated).
    """

    business_segment_id: Annotated[Optional[BusinessSegmentID], PropertyInfo(alias="BusinessSegmentId")]
    """
    Identifier of the reservation `BusinessSegment` (or `null` if the business
    segment should not be updated).
    """

    channel_number: Annotated[Optional[ChannelNumber], PropertyInfo(alias="ChannelNumber")]
    """Number of the reservation within the Channel (i.e.

    OTA, GDS, CRS, etc) in case the reservation group originates there (e.g.
    Booking.com confirmation number) (or `null` if the channel number should not be
    updated).
    """

    check_overbooking: Annotated[Optional[bool], PropertyInfo(alias="CheckOverbooking")]
    """
    Indicates whether the system will check and prevent a booking being made in the
    case of an overbooking, i.e. where there is an insufficient number of resources
    available to meet the request.
    """

    check_rate_applicability: Annotated[Optional[bool], PropertyInfo(alias="CheckRateApplicability")]
    """
    Indicates whether the system will check and prevent a booking being made using a
    restricted rate, e.g. a private rate. The default is true, i.e. the system will
    normally check for this unless the property is set to false.
    """

    company_id: Annotated[Optional[CompanyID], PropertyInfo(alias="CompanyId")]
    """
    Identifier of the `Company` on behalf of which the reservation was made (or
    `null` if company should not be updated).
    """

    credit_card_id: Annotated[Optional[CreditCardID], PropertyInfo(alias="CreditCardId")]
    """Identifier of `CreditCard` belonging to `Customer` who owns the reservation.

    (or `null` if the credit card should not be updated).
    """

    end_utc: Annotated[Optional[EndUtc], PropertyInfo(alias="EndUtc")]
    """Reservation end in UTC timezone in ISO 8601 format.

    (or `null` if the end time should not be updated).
    """

    enterprise_id: Annotated[Optional[str], PropertyInfo(alias="EnterpriseId")]
    """Unique identifier of the enterprise.

    Required when using
    [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
    ignored otherwise.
    """

    options: Annotated[Optional[Options], PropertyInfo(alias="Options")]
    """Options of the reservations."""

    person_counts: Annotated[Optional[PersonCounts], PropertyInfo(alias="PersonCounts")]
    """Number of people per age category the reservation is for.

    If supplied, the person counts will be replaced. (or `null` if the person counts
    should not be updated).
    """

    purpose: Annotated[Optional[Purpose], PropertyInfo(alias="Purpose")]
    """`Purpose` of the reservation (or `null` if the purpose should not be updated)."""

    rate_id: Annotated[Optional[RateID], PropertyInfo(alias="RateId")]
    """
    Identifier of the reservation `Rate` (or `null` if the rate should not be
    updated).
    """

    reason: Annotated[Optional[str], PropertyInfo(alias="Reason")]
    """Reason for updating the reservation.

    Required when updating the price of the reservation.
    """

    released_utc: Annotated[Optional[ReleasedUtc], PropertyInfo(alias="ReleasedUtc")]
    """
    Date when the optional reservation is released in UTC timezone in ISO 8601
    format. (or `null` if the release time should not be updated).
    """

    reprice: Annotated[Optional[bool], PropertyInfo(alias="Reprice")]
    """
    Whether the price should be updated to latest value for date/rate/category
    combination set in Mews. If not specified, the reservation price is updated.
    """

    requested_category_id: Annotated[Optional[RequestedCategoryID], PropertyInfo(alias="RequestedCategoryId")]
    """
    Identifier of the requested `ResourceCategory` (or `null` if resource category
    should not be updated).
    """

    start_utc: Annotated[Optional[StartUtc], PropertyInfo(alias="StartUtc")]
    """Reservation start in UTC timezone in ISO 8601 format.

    (or `null` if the start time should not be updated).
    """

    time_unit_prices: Annotated[Optional[TimeUnitPrices], PropertyInfo(alias="TimeUnitPrices")]
    """Prices for time units of the reservation.

    E.g. prices for the first or second night. (or `null` if the unit amounts should
    not be updated).
    """

    travel_agency_id: Annotated[Optional[TravelAgencyID], PropertyInfo(alias="TravelAgencyId")]
    """
    Identifier of the `Company` that mediated the reservation (or `null` if travel
    agency should not be updated).
    """


class ReservationUpdateAssignedResourceID(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class ReservationUpdateAssignedResourceLocked(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class ReservationUpdateAvailabilityBlockID(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class ReservationUpdateBookerID(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class ReservationUpdateBusinessSegmentID(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class ReservationUpdateChannelNumber(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class ReservationUpdateCompanyID(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class ReservationUpdateCreditCardID(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class ReservationUpdateEndUtc(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class ReservationUpdateOptionsOwnerCheckedIn(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class ReservationUpdateOptions(TypedDict, total=False):
    owner_checked_in: Annotated[Optional[ReservationUpdateOptionsOwnerCheckedIn], PropertyInfo(alias="OwnerCheckedIn")]
    """True if the owner of the reservation is checked in.

    (or `null` if the value should not be updated).
    """


class ReservationUpdatePersonCountsValue(TypedDict, total=False):
    age_category_id: Required[Annotated[str, PropertyInfo(alias="AgeCategoryId")]]
    """
    Unique identifier of the
    [Age category](https://mews-systems.gitbook.io/connector-api/operations/agecategories#age-category).
    """

    count: Required[Annotated[int, PropertyInfo(alias="Count")]]
    """Number of people of a given age category. Only positive value is accepted."""


class ReservationUpdatePersonCounts(TypedDict, total=False):
    value: Annotated[Optional[Iterable[ReservationUpdatePersonCountsValue]], PropertyInfo(alias="Value")]


class ReservationUpdatePurpose(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class ReservationUpdateRateID(TypedDict, total=False):
    value: Annotated[str, PropertyInfo(alias="Value")]


class ReservationUpdateReleasedUtc(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class ReservationUpdateRequestedCategoryID(TypedDict, total=False):
    value: Annotated[str, PropertyInfo(alias="Value")]


class ReservationUpdateStartUtc(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class ReservationUpdateTimeUnitPricesValueAmount(TypedDict, total=False):
    currency: Required[Annotated[str, PropertyInfo(alias="Currency")]]

    tax_codes: Required[Annotated[List[str], PropertyInfo(alias="TaxCodes")]]

    gross_value: Annotated[Optional[float], PropertyInfo(alias="GrossValue")]

    net_value: Annotated[Optional[float], PropertyInfo(alias="NetValue")]


class ReservationUpdateTimeUnitPricesValue(TypedDict, total=False):
    amount: Annotated[Optional[ReservationUpdateTimeUnitPricesValueAmount], PropertyInfo(alias="Amount")]
    """Price of the product that overrides the price defined in Mews."""

    index: Annotated[int, PropertyInfo(alias="Index")]
    """Index of the unit.

    Indexing starts with `0`. E.g. the first night of the reservation has index `0`.
    """


class ReservationUpdateTimeUnitPrices(TypedDict, total=False):
    value: Annotated[Optional[Iterable[ReservationUpdateTimeUnitPricesValue]], PropertyInfo(alias="Value")]


class ReservationUpdateTravelAgencyID(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class ReservationUpdate(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    reservation_id: Required[Annotated[str, PropertyInfo(alias="ReservationId")]]
    """Unique identifier of the reservation."""

    assigned_resource_id: Annotated[
        Optional[ReservationUpdateAssignedResourceID], PropertyInfo(alias="AssignedResourceId")
    ]
    """Identifier of the assigned `Resource`."""

    assigned_resource_locked: Annotated[
        Optional[ReservationUpdateAssignedResourceLocked], PropertyInfo(alias="AssignedResourceLocked")
    ]
    """Whether the reservation should be locked to the assigned `Resource`.

    Unlocking and assigning reservation to new `Resource` can be done in one call.
    """

    availability_block_id: Annotated[
        Optional[ReservationUpdateAvailabilityBlockID], PropertyInfo(alias="AvailabilityBlockId")
    ]
    """Unique identifier of the `AvailabilityBlock` the reservation is assigned to."""

    booker_id: Annotated[Optional[ReservationUpdateBookerID], PropertyInfo(alias="BookerId")]
    """Identifier of the `Customer` on whose behalf the reservation was made.

    (or `null` if the booker should not be updated).
    """

    business_segment_id: Annotated[
        Optional[ReservationUpdateBusinessSegmentID], PropertyInfo(alias="BusinessSegmentId")
    ]
    """
    Identifier of the reservation `BusinessSegment` (or `null` if the business
    segment should not be updated).
    """

    channel_number: Annotated[Optional[ReservationUpdateChannelNumber], PropertyInfo(alias="ChannelNumber")]
    """Number of the reservation within the Channel (i.e.

    OTA, GDS, CRS, etc) in case the reservation group originates there (e.g.
    Booking.com confirmation number) (or `null` if the channel number should not be
    updated).
    """

    company_id: Annotated[Optional[ReservationUpdateCompanyID], PropertyInfo(alias="CompanyId")]
    """
    Identifier of the `Company` on behalf of which the reservation was made (or
    `null` if company should not be updated).
    """

    credit_card_id: Annotated[Optional[ReservationUpdateCreditCardID], PropertyInfo(alias="CreditCardId")]
    """Identifier of `CreditCard` belonging to `Customer` who owns the reservation.

    (or `null` if the credit card should not be updated).
    """

    end_utc: Annotated[Optional[ReservationUpdateEndUtc], PropertyInfo(alias="EndUtc")]
    """Reservation end in UTC timezone in ISO 8601 format.

    (or `null` if the end time should not be updated).
    """

    enterprise_id: Annotated[Optional[str], PropertyInfo(alias="EnterpriseId")]
    """Unique identifier of the enterprise.

    Required when using
    [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
    ignored otherwise.
    """

    options: Annotated[Optional[ReservationUpdateOptions], PropertyInfo(alias="Options")]
    """Options of the reservations."""

    person_counts: Annotated[Optional[ReservationUpdatePersonCounts], PropertyInfo(alias="PersonCounts")]
    """Number of people per age category the reservation is for.

    If supplied, the person counts will be replaced. (or `null` if the person counts
    should not be updated).
    """

    purpose: Annotated[Optional[ReservationUpdatePurpose], PropertyInfo(alias="Purpose")]
    """`Purpose` of the reservation (or `null` if the purpose should not be updated)."""

    rate_id: Annotated[Optional[ReservationUpdateRateID], PropertyInfo(alias="RateId")]
    """
    Identifier of the reservation `Rate` (or `null` if the rate should not be
    updated).
    """

    released_utc: Annotated[Optional[ReservationUpdateReleasedUtc], PropertyInfo(alias="ReleasedUtc")]
    """
    Date when the optional reservation is released in UTC timezone in ISO 8601
    format. (or `null` if the release time should not be updated).
    """

    requested_category_id: Annotated[
        Optional[ReservationUpdateRequestedCategoryID], PropertyInfo(alias="RequestedCategoryId")
    ]
    """
    Identifier of the requested `ResourceCategory` (or `null` if resource category
    should not be updated).
    """

    start_utc: Annotated[Optional[ReservationUpdateStartUtc], PropertyInfo(alias="StartUtc")]
    """Reservation start in UTC timezone in ISO 8601 format.

    (or `null` if the start time should not be updated).
    """

    time_unit_prices: Annotated[Optional[ReservationUpdateTimeUnitPrices], PropertyInfo(alias="TimeUnitPrices")]
    """Prices for time units of the reservation.

    E.g. prices for the first or second night. (or `null` if the unit amounts should
    not be updated).
    """

    travel_agency_id: Annotated[Optional[ReservationUpdateTravelAgencyID], PropertyInfo(alias="TravelAgencyId")]
    """
    Identifier of the `Company` that mediated the reservation (or `null` if travel
    agency should not be updated).
    """


class AssignedResourceID(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AssignedResourceLocked(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class AvailabilityBlockID(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class BookerID(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class BusinessSegmentID(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class ChannelNumber(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class CompanyID(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class CreditCardID(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class EndUtc(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class OptionsOwnerCheckedIn(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class Options(TypedDict, total=False):
    owner_checked_in: Annotated[Optional[OptionsOwnerCheckedIn], PropertyInfo(alias="OwnerCheckedIn")]
    """True if the owner of the reservation is checked in.

    (or `null` if the value should not be updated).
    """


class PersonCountsValue(TypedDict, total=False):
    age_category_id: Required[Annotated[str, PropertyInfo(alias="AgeCategoryId")]]
    """
    Unique identifier of the
    [Age category](https://mews-systems.gitbook.io/connector-api/operations/agecategories#age-category).
    """

    count: Required[Annotated[int, PropertyInfo(alias="Count")]]
    """Number of people of a given age category. Only positive value is accepted."""


class PersonCounts(TypedDict, total=False):
    value: Annotated[Optional[Iterable[PersonCountsValue]], PropertyInfo(alias="Value")]


class Purpose(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class RateID(TypedDict, total=False):
    value: Annotated[str, PropertyInfo(alias="Value")]


class ReleasedUtc(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class RequestedCategoryID(TypedDict, total=False):
    value: Annotated[str, PropertyInfo(alias="Value")]


class StartUtc(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class TimeUnitPricesValueAmount(TypedDict, total=False):
    currency: Required[Annotated[str, PropertyInfo(alias="Currency")]]

    tax_codes: Required[Annotated[List[str], PropertyInfo(alias="TaxCodes")]]

    gross_value: Annotated[Optional[float], PropertyInfo(alias="GrossValue")]

    net_value: Annotated[Optional[float], PropertyInfo(alias="NetValue")]


class TimeUnitPricesValue(TypedDict, total=False):
    amount: Annotated[Optional[TimeUnitPricesValueAmount], PropertyInfo(alias="Amount")]
    """Price of the product that overrides the price defined in Mews."""

    index: Annotated[int, PropertyInfo(alias="Index")]
    """Index of the unit.

    Indexing starts with `0`. E.g. the first night of the reservation has index `0`.
    """


class TimeUnitPrices(TypedDict, total=False):
    value: Annotated[Optional[Iterable[TimeUnitPricesValue]], PropertyInfo(alias="Value")]


class TravelAgencyID(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]
