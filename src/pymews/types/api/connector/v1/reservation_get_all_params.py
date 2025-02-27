# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["ReservationGetAllParams", "Extent", "Limitation"]


class ReservationGetAllParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    extent: Required[Annotated[Extent, PropertyInfo(alias="Extent")]]
    """Extent of data to be returned.

    E.g. it is possible to specify that together with the reservations, customers,
    groups and rates should be also returned.
    """

    limitation: Required[Annotated[Limitation, PropertyInfo(alias="Limitation")]]
    """Limitation on the quantity of data returned."""

    service_ids: Required[Annotated[List[str], PropertyInfo(alias="ServiceIds")]]
    """
    Unique identifiers of the
    [Services](https://mews-systems.gitbook.io/connector-api/operations/services/#service)
    from which the reservations are requested.
    """

    assigned_resource_ids: Annotated[Optional[List[str]], PropertyInfo(alias="AssignedResourceIds")]
    """
    Unique identifiers of
    [Resources](https://mews-systems.gitbook.io/connector-api/operations/resources/#resource)
    assigned to the reservations.
    """

    business_segment_ids: Annotated[Optional[List[str]], PropertyInfo(alias="BusinessSegmentIds")]
    """
    Unique identifiers of
    [Business segments](https://mews-systems.gitbook.io/connector-api/operations/businesssegments/#business-segment)
    assigned to the reservations.
    """

    channel_numbers: Annotated[Optional[List[str]], PropertyInfo(alias="ChannelNumbers")]
    """Set of numbers or references used by the Channel (i.e.

    OTA, GDS, CRS, etc.) in case the reservation group originates there, e.g.
    Booking.com confirmation numbers.
    """

    currency: Annotated[Optional[str], PropertyInfo(alias="Currency")]
    """
    ISO-4217 code of the
    [Currency](https://mews-systems.gitbook.io/connector-api/operations/currencies/#currency)
    the item costs should be converted to.
    """

    customer_ids: Annotated[Optional[List[str]], PropertyInfo(alias="CustomerIds")]
    """
    Unique identifiers of the
    [Customers](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer)
    which own the reservations.
    """

    end_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="EndUtc", format="iso8601")]
    """End of the interval in UTC timezone in ISO 8601 format.

    Required when used in conjunction with the TimeFilter or States search
    parameter.
    """

    group_ids: Annotated[Optional[List[str]], PropertyInfo(alias="GroupIds")]
    """
    Unique identifiers of the requested
    [Reservation groups](https://mews-systems.gitbook.io/connector-api/operations/#reservation-group).
    """

    numbers: Annotated[Optional[List[str]], PropertyInfo(alias="Numbers")]
    """
    Confirmation numbers of
    [Reservations](https://mews-systems.gitbook.io/connector-api/operations/#reservation-ver-2017-04-12).
    """

    rate_ids: Annotated[Optional[List[str]], PropertyInfo(alias="RateIds")]
    """
    Unique identifiers of
    [Rates](https://mews-systems.gitbook.io/connector-api/operations/rates/#rate)
    assigned to the reservations.
    """

    reservation_ids: Annotated[Optional[List[str]], PropertyInfo(alias="ReservationIds")]
    """
    Unique identifiers of the requested
    [Reservations](https://mews-systems.gitbook.io/connector-api/operations/#reservation-ver-2017-04-12).
    """

    service_id: Annotated[Optional[str], PropertyInfo(alias="ServiceId")]

    start_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="StartUtc", format="iso8601")]
    """Start of the interval in UTC timezone in ISO 8601 format.

    Required when used in conjunction with the TimeFilter or States search
    parameter.
    """

    states: Annotated[
        Optional[List[Literal["Enquired", "Confirmed", "Started", "Processed", "Canceled", "Optional", "Requested"]]],
        PropertyInfo(alias="States"),
    ]
    """States the reservations should be in.

    If not specified, reservations in Confirmed, Started or Processed states or
    reservations specified by ReservationIds regardless of state are returned.
    """

    time_filter: Annotated[
        Optional[Literal["Colliding", "Created", "Updated", "Start", "End", "Overlapping", "Canceled"]],
        PropertyInfo(alias="TimeFilter"),
    ]
    """Time filter of the interval.

    If not specified, reservations Colliding with the interval are returned.

    - `Colliding` - Reservations whose intervals collide with the specified
      interval.
    - `Created` - Reservations created within the specified interval.
    - `Updated` - Reservations updated within the specified interval.
    - `Start` - Reservations starting (arriving) within the specified interval.
    - `End` - Reservations ending (departing) within the specified interval.
    - `Overlapping` - Reservations whose intervals contain the specified interval.
    - `Canceled` - Reservations canceled within the specified interval.
    """


class Extent(TypedDict, total=False):
    accounting_states: Annotated[
        Optional[List[Literal["Open", "Closed", "Inactive", "Canceled"]]], PropertyInfo(alias="AccountingStates")
    ]
    """States the items should be in.

    If not specified, items in `Open` or `Closed` states are returned.
    """

    business_segments: Annotated[Optional[bool], PropertyInfo(alias="BusinessSegments")]
    """Whether the response should contain business segmentation."""

    companies: Annotated[Optional[bool], PropertyInfo(alias="Companies")]
    """Whether the response should contain companies."""

    customer_adresses: Annotated[Optional[bool], PropertyInfo(alias="CustomerAdresses")]
    """Whether the response should contain addresses of the customers."""

    customer_identity_documents: Annotated[Optional[bool], PropertyInfo(alias="CustomerIdentityDocuments")]
    """Whether the response should contain identity documents of the customers."""

    customers: Annotated[Optional[bool], PropertyInfo(alias="Customers")]
    """Whether the response should contain customers of the reservations."""

    items: Annotated[Optional[bool], PropertyInfo(alias="Items")]
    """Whether the response should contain accounting items."""

    notes: Annotated[Optional[bool], PropertyInfo(alias="Notes")]
    """Whether the response should contain notes."""

    order_items: Annotated[Optional[bool], PropertyInfo(alias="OrderItems")]
    """Whether the response should contain reservation items."""

    products: Annotated[Optional[bool], PropertyInfo(alias="Products")]
    """Whether the response should contain products orderable with the reservations."""

    qr_code_data: Annotated[Optional[bool], PropertyInfo(alias="QrCodeData")]
    """Whether the response should contain QR code data."""

    rates: Annotated[Optional[bool], PropertyInfo(alias="Rates")]
    """Whether the response should contain rates and rate groups."""

    reservation_groups: Annotated[Optional[bool], PropertyInfo(alias="ReservationGroups")]
    """Whether the response should contain groups of the reservations."""

    reservations: Annotated[Optional[bool], PropertyInfo(alias="Reservations")]
    """Whether the response should contain reservations."""

    resource_categories: Annotated[Optional[bool], PropertyInfo(alias="ResourceCategories")]
    """Whether the response should contain resource categories."""

    resource_category_assignments: Annotated[Optional[bool], PropertyInfo(alias="ResourceCategoryAssignments")]
    """Whether the response should contain assignments of the resources to categories."""

    resources: Annotated[Optional[bool], PropertyInfo(alias="Resources")]
    """Whether the response should contain resources."""

    services: Annotated[Optional[bool], PropertyInfo(alias="Services")]
    """Whether the response should contain services reserved by the reservations."""


class Limitation(TypedDict, total=False):
    count: Required[Annotated[int, PropertyInfo(alias="Count")]]

    cursor: Annotated[Optional[str], PropertyInfo(alias="Cursor")]
