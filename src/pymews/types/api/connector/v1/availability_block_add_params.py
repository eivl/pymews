# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["AvailabilityBlockAddParams", "AvailabilityBlock", "AvailabilityBlockBudget"]


class AvailabilityBlockAddParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    availability_blocks: Required[Annotated[Iterable[AvailabilityBlock], PropertyInfo(alias="AvailabilityBlocks")]]
    """Availability blocks to be added."""

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


class AvailabilityBlockBudget(TypedDict, total=False):
    currency: Required[Annotated[str, PropertyInfo(alias="Currency")]]

    net: Annotated[Optional[float], PropertyInfo(alias="Net")]

    tax: Annotated[Optional[float], PropertyInfo(alias="Tax")]

    tax_rate: Annotated[Optional[float], PropertyInfo(alias="TaxRate")]

    value: Annotated[Optional[float], PropertyInfo(alias="Value")]


class AvailabilityBlock(TypedDict, total=False):
    first_time_unit_start_utc: Required[Annotated[str, PropertyInfo(alias="FirstTimeUnitStartUtc")]]
    """
    Start of the time interval, expressed as the timestamp for the start of the
    first time unit, in UTC timezone ISO 8601 format.
    """

    last_time_unit_start_utc: Required[Annotated[str, PropertyInfo(alias="LastTimeUnitStartUtc")]]
    """
    End of the time interval, expressed as the timestamp for the start of the first
    time unit, in UTC timezone ISO 8601 format.
    """

    rate_id: Required[Annotated[str, PropertyInfo(alias="RateId")]]
    """
    Unique identifier of the
    [Rate](https://mews-systems.gitbook.io/connector-api/operations/rates#rate) to
    assign block to.
    """

    service_id: Required[Annotated[str, PropertyInfo(alias="ServiceId")]]
    """
    Unique identifier of the
    [Service](https://mews-systems.gitbook.io/connector-api/operations/services#service)
    to assign block to.
    """

    state: Required[Annotated[Literal["Confirmed", "Optional", "Inquired", "Canceled"], PropertyInfo(alias="State")]]
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

    booker_id: Annotated[Optional[str], PropertyInfo(alias="BookerId")]
    """Unique identifier of the Booker as a creator of an availability block."""

    budget: Annotated[Optional[AvailabilityBlockBudget], PropertyInfo(alias="Budget")]
    """Total price of the reservation."""

    company_id: Annotated[Optional[str], PropertyInfo(alias="CompanyId")]
    """
    Unique identifier of
    [Company](https://mews-systems.gitbook.io/connector-api/operations/companies#company).
    """

    external_identifier: Annotated[Optional[str], PropertyInfo(alias="ExternalIdentifier")]
    """Identifier of the block from external system."""

    name: Annotated[Optional[str], PropertyInfo(alias="Name")]
    """The name of the block."""

    notes: Annotated[Optional[str], PropertyInfo(alias="Notes")]
    """Additional notes of the block."""

    quote_id: Annotated[Optional[str], PropertyInfo(alias="QuoteId")]
    """
    Unique identifier of the Mews Events quote associated with the availability
    block.
    """

    released_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="ReleasedUtc", format="iso8601")]
    """
    The moment when the block and its availability is released, in UTC timezone ISO
    8601 format. Takes precedence over `RollingReleaseOffset`.
    """

    reservation_purpose: Annotated[
        Optional[Literal["Leisure", "Business", "Student"]], PropertyInfo(alias="ReservationPurpose")
    ]
    """Leisure

    Business

    Student
    """

    rolling_release_offset: Annotated[Optional[str], PropertyInfo(alias="RollingReleaseOffset")]
    """
    Exact offset from the start of availability adjustments to the moment the
    availability adjustment should be released, in ISO 8601 duration format. Ignored
    if `ReleasedUtc` is specified.
    """

    travel_agency_id: Annotated[Optional[str], PropertyInfo(alias="TravelAgencyId")]
    """Unique identifier of travel agency (`Company` with a `TravelAgencyContract`)."""

    voucher_code: Annotated[Optional[str], PropertyInfo(alias="VoucherCode")]
    """
    Voucher code providing access to specified private
    [Rate](https://mews-systems.gitbook.io/connector-api/operations/rates#rate).
    """
