# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = [
    "ReservationGetAll2023_06_06Params",
    "Limitation",
    "ActualStartUtc",
    "CollidingUtc",
    "CreatedUtc",
    "ScheduledEndUtc",
    "ScheduledStartUtc",
    "UpdatedUtc",
]


class ReservationGetAll2023_06_06Params(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    limitation: Required[Annotated[Limitation, PropertyInfo(alias="Limitation")]]
    """Limitation on the quantity of data returned."""

    account_ids: Annotated[Optional[List[str]], PropertyInfo(alias="AccountIds")]
    """
    Unique identifiers of accounts (currently only
    [Customers](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer),
    in the future also
    [Companies](https://mews-systems.gitbook.io/connector-api/operations/companies/#company))
    the reservation is associated with.
    """

    actual_start_utc: Annotated[Optional[ActualStartUtc], PropertyInfo(alias="ActualStartUtc")]
    """Interval filtering Reservations by their actual start (check-in) time.

    Cannot be used with `ScheduledStartUtc`. Note that the filter applies only to
    started or processed reservations.
    """

    assigned_resource_ids: Annotated[Optional[List[str]], PropertyInfo(alias="AssignedResourceIds")]
    """
    Unique identifiers of the
    [Resources](https://mews-systems.gitbook.io/connector-api/operations/resources#resource)
    assigned to the reservations.
    """

    availability_block_ids: Annotated[Optional[List[str]], PropertyInfo(alias="AvailabilityBlockIds")]
    """Unique identifiers of the `Availability blocks` assigned to the reservations."""

    colliding_utc: Annotated[Optional[CollidingUtc], PropertyInfo(alias="CollidingUtc")]
    """Interval in which the reservations are active.

    This is defined for a `Reservation` as the period between the reservation's
    scheduled start time `ScheduledStartUtc` and its scheduled end time `EndUtc`.
    Reservation is selected if any part of its interval intersects with the interval
    specified in `CollidingUtc
    """

    created_utc: Annotated[Optional[CreatedUtc], PropertyInfo(alias="CreatedUtc")]
    """
    Interval in which the
    [Reservation](https://mews-systems.gitbook.io/connector-api/operations/reservations/#reservation-ver-2023-06-06)
    was created.
    """

    enterprise_ids: Annotated[Optional[List[str]], PropertyInfo(alias="EnterpriseIds")]
    """Unique identifiers of the Enterprises.

    If not specified, the operation returns data for all enterprises within scope of
    the Access Token.
    """

    numbers: Annotated[Optional[List[str]], PropertyInfo(alias="Numbers")]
    """A list of reservation numbers.

    Each number uniquely identifies a reservation within the system
    """

    reservation_group_ids: Annotated[Optional[List[str]], PropertyInfo(alias="ReservationGroupIds")]
    """
    Unique identifiers of
    [Reservation groups](https://mews-systems.gitbook.io/connector-api/operations/#reservation-group).
    """

    reservation_ids: Annotated[Optional[List[str]], PropertyInfo(alias="ReservationIds")]
    """
    Unique identifiers of the
    [Reservations](https://mews-systems.gitbook.io/connector-api/operations/#reservation-ver-2023-06-06).
    """

    scheduled_end_utc: Annotated[Optional[ScheduledEndUtc], PropertyInfo(alias="ScheduledEndUtc")]
    """Interval filtering Reservations by their scheduled end time."""

    scheduled_start_utc: Annotated[Optional[ScheduledStartUtc], PropertyInfo(alias="ScheduledStartUtc")]
    """Interval filtering Reservations by their scheduled start time.

    Cannot be used with `ActualStartUtc`.
    """

    service_ids: Annotated[Optional[List[str]], PropertyInfo(alias="ServiceIds")]
    """
    Unique identifiers of the
    [Services](https://mews-systems.gitbook.io/connector-api/operations/services/#service).
    If not provided, all bookable services are used.
    """

    states: Annotated[
        Optional[List[Literal["Inquired", "Confirmed", "Started", "Processed", "Canceled", "Optional", "Requested"]]],
        PropertyInfo(alias="States"),
    ]
    """A list of service order states to filter by."""

    updated_utc: Annotated[Optional[UpdatedUtc], PropertyInfo(alias="UpdatedUtc")]
    """Interval in which the `Reservations` were updated."""


class Limitation(TypedDict, total=False):
    count: Required[Annotated[int, PropertyInfo(alias="Count")]]

    cursor: Annotated[Optional[str], PropertyInfo(alias="Cursor")]


class ActualStartUtc(TypedDict, total=False):
    end_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="EndUtc", format="iso8601")]

    start_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="StartUtc", format="iso8601")]


class CollidingUtc(TypedDict, total=False):
    end_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="EndUtc", format="iso8601")]

    start_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="StartUtc", format="iso8601")]


class CreatedUtc(TypedDict, total=False):
    end_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="EndUtc", format="iso8601")]

    start_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="StartUtc", format="iso8601")]


class ScheduledEndUtc(TypedDict, total=False):
    end_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="EndUtc", format="iso8601")]

    start_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="StartUtc", format="iso8601")]


class ScheduledStartUtc(TypedDict, total=False):
    end_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="EndUtc", format="iso8601")]

    start_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="StartUtc", format="iso8601")]


class UpdatedUtc(TypedDict, total=False):
    end_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="EndUtc", format="iso8601")]

    start_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="StartUtc", format="iso8601")]
