# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = [
    "ReservationAddParams",
    "Reservation",
    "ReservationPersonCount",
    "ReservationProductOrder",
    "ReservationProductOrderUnitAmount",
    "ReservationTimeUnitAmount",
    "ReservationTimeUnitPrice",
    "ReservationTimeUnitPriceAmount",
]


class ReservationAddParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    reservations: Required[Annotated[Iterable[Reservation], PropertyInfo(alias="Reservations")]]
    """Parameters of the new reservations."""

    service_id: Required[Annotated[str, PropertyInfo(alias="ServiceId")]]
    """Unique identifier of the `Service` to be reserved."""

    check_overbooking: Annotated[Optional[bool], PropertyInfo(alias="CheckOverbooking")]
    """
    Indicates whether the system will check and prevent a booking being made in the
    case of an overbooking, i.e. where there is an insufficient number of resources
    available to meet the request. The default is `true`, i.e. the system will
    normally check for this unless the property is set to `false`.
    """

    check_rate_applicability: Annotated[Optional[bool], PropertyInfo(alias="CheckRateApplicability")]
    """
    Indicates whether the system will check and prevent a booking being made using a
    restricted rate, e.g. a private rate. The default is `true`, i.e. the system
    will normally check for this unless the property is set to `false`.
    """

    enterprise_id: Annotated[Optional[str], PropertyInfo(alias="EnterpriseId")]
    """Unique identifier of the enterprise.

    Required when using
    [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
    ignored otherwise.
    """

    group_id: Annotated[Optional[str], PropertyInfo(alias="GroupId")]
    """Unique identifier of the `ReservationGroup` where the reservations are added.

    If not specified, a new group is created.
    """

    group_name: Annotated[Optional[str], PropertyInfo(alias="GroupName")]
    """Name of the `ReservationGroup` where the reservations are added to.

    If `GroupId` is specified, this field is ignored. If not specified, the group
    name is automatically created.
    """

    send_confirmation_email: Annotated[Optional[bool], PropertyInfo(alias="SendConfirmationEmail")]
    """Whether the confirmation email is sent. Default value is `true`."""


class ReservationPersonCount(TypedDict, total=False):
    age_category_id: Required[Annotated[str, PropertyInfo(alias="AgeCategoryId")]]
    """
    Unique identifier of the
    [Age category](https://mews-systems.gitbook.io/connector-api/operations/agecategories#age-category).
    """

    count: Required[Annotated[int, PropertyInfo(alias="Count")]]
    """Number of people of a given age category. Only positive value is accepted."""


class ReservationProductOrderUnitAmount(TypedDict, total=False):
    currency: Required[Annotated[str, PropertyInfo(alias="Currency")]]

    tax_codes: Required[Annotated[List[str], PropertyInfo(alias="TaxCodes")]]

    gross_value: Annotated[Optional[float], PropertyInfo(alias="GrossValue")]

    net_value: Annotated[Optional[float], PropertyInfo(alias="NetValue")]


class ReservationProductOrder(TypedDict, total=False):
    product_id: Required[Annotated[str, PropertyInfo(alias="ProductId")]]

    count: Annotated[Optional[int], PropertyInfo(alias="Count")]

    end_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="EndUtc", format="iso8601")]

    external_identifier: Annotated[Optional[str], PropertyInfo(alias="ExternalIdentifier")]

    start_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="StartUtc", format="iso8601")]

    unit_amount: Annotated[Optional[ReservationProductOrderUnitAmount], PropertyInfo(alias="UnitAmount")]
    """Price of the product that overrides the price defined in Mews."""


class ReservationTimeUnitAmount(TypedDict, total=False):
    currency: Required[Annotated[str, PropertyInfo(alias="Currency")]]

    tax_codes: Required[Annotated[List[str], PropertyInfo(alias="TaxCodes")]]

    gross_value: Annotated[Optional[float], PropertyInfo(alias="GrossValue")]

    net_value: Annotated[Optional[float], PropertyInfo(alias="NetValue")]


class ReservationTimeUnitPriceAmount(TypedDict, total=False):
    currency: Required[Annotated[str, PropertyInfo(alias="Currency")]]

    tax_codes: Required[Annotated[List[str], PropertyInfo(alias="TaxCodes")]]

    gross_value: Annotated[Optional[float], PropertyInfo(alias="GrossValue")]

    net_value: Annotated[Optional[float], PropertyInfo(alias="NetValue")]


class ReservationTimeUnitPrice(TypedDict, total=False):
    amount: Annotated[Optional[ReservationTimeUnitPriceAmount], PropertyInfo(alias="Amount")]
    """Price of the product that overrides the price defined in Mews."""

    index: Annotated[int, PropertyInfo(alias="Index")]
    """Index of the unit.

    Indexing starts with `0`. E.g. the first night of the reservation has index `0`.
    """


class Reservation(TypedDict, total=False):
    customer_id: Required[Annotated[str, PropertyInfo(alias="CustomerId")]]
    """Unique identifier of the `Customer` who owns the reservation."""

    end_utc: Required[Annotated[Union[str, datetime], PropertyInfo(alias="EndUtc", format="iso8601")]]
    """Reservation end in UTC timezone in ISO 8601 format."""

    person_counts: Required[Annotated[Iterable[ReservationPersonCount], PropertyInfo(alias="PersonCounts")]]
    """Number of people per age category the reservation was booked for.

    At least one category with valid count must be provided.
    """

    rate_id: Required[Annotated[str, PropertyInfo(alias="RateId")]]
    """Identifier of the reservation `Rate`."""

    requested_category_id: Required[Annotated[str, PropertyInfo(alias="RequestedCategoryId")]]
    """Identifier of the requested `ResourceCategory`."""

    start_utc: Required[Annotated[Union[str, datetime], PropertyInfo(alias="StartUtc", format="iso8601")]]
    """Reservation start in UTC timezone in ISO 8601 format."""

    adult_count: Annotated[int, PropertyInfo(alias="AdultCount")]

    availability_block_id: Annotated[Optional[str], PropertyInfo(alias="AvailabilityBlockId")]
    """Unique identifier of the `AvailabilityBlock` the reservation is assigned to."""

    booker_id: Annotated[Optional[str], PropertyInfo(alias="BookerId")]
    """Unique identifier of the `Customer` on whose behalf the reservation was made."""

    business_segment_id: Annotated[Optional[str], PropertyInfo(alias="BusinessSegmentId")]
    """Identifier of the reservation `BusinessSegment`."""

    channel_number: Annotated[Optional[str], PropertyInfo(alias="ChannelNumber")]

    child_count: Annotated[int, PropertyInfo(alias="ChildCount")]

    company_id: Annotated[Optional[str], PropertyInfo(alias="CompanyId")]
    """Identifier of the `Company` on behalf of which the reservation was made."""

    credit_card_id: Annotated[Optional[str], PropertyInfo(alias="CreditCardId")]
    """
    Identifier of `CreditCard` belonging either to the `Customer` who owns the
    reservation or to the `Booker`.
    """

    identifier: Annotated[Optional[str], PropertyInfo(alias="Identifier")]
    """Identifier of the reservation within the transaction."""

    notes: Annotated[Optional[str], PropertyInfo(alias="Notes")]
    """Additional notes."""

    product_orders: Annotated[Optional[Iterable[ReservationProductOrder]], PropertyInfo(alias="ProductOrders")]
    """Parameters of the products ordered together with the reservation."""

    released_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="ReleasedUtc", format="iso8601")]
    """
    Release date and time of an unconfirmed reservation in UTC timezone in ISO 8601
    format.
    """

    state: Annotated[
        Optional[Literal["Inquired", "Confirmed", "Started", "Processed", "Canceled", "Optional", "Requested"]],
        PropertyInfo(alias="State"),
    ]
    """
    State of the newly created reservation (either `Optional`, `Enquired` or
    `Confirmed`). If not specified, `Confirmed` is used.

    - `Inquired` - Confirmed neither by the customer nor enterprise.
    - `Confirmed` - Confirmed by both parties, before check-in.
    - `Started` - Checked in.
    - `Processed` - Checked out.
    - `Canceled` - Canceled.
    - `Optional` - Confirmed by enterprise but not by the guest (the enterprise is
      holding resource for the guest).
    - `Requested` - Confirmed by the customer but not by the enterprise (waitlist).
    """

    time_unit_amount: Annotated[Optional[ReservationTimeUnitAmount], PropertyInfo(alias="TimeUnitAmount")]
    """Price of the product that overrides the price defined in Mews."""

    time_unit_prices: Annotated[Optional[Iterable[ReservationTimeUnitPrice]], PropertyInfo(alias="TimeUnitPrices")]
    """Prices for time units of the reservation.

    E.g. prices for the first or second night.
    """

    travel_agency_id: Annotated[Optional[str], PropertyInfo(alias="TravelAgencyId")]
    """Identifier of the `Company` that mediated the reservation."""

    voucher_code: Annotated[Optional[str], PropertyInfo(alias="VoucherCode")]
    """
    Voucher code value providing access to specified private `Rate` applied to this
    reservation.
    """
