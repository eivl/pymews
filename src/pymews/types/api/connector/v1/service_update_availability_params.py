# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = [
    "ServiceUpdateAvailabilityParams",
    "AvailabilityUpdate",
    "AvailabilityUpdateUnitCountAdjustment",
    "AvailabilityUpdatePaxCount",
]


class ServiceUpdateAvailabilityParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    availability_updates: Required[Annotated[Iterable[AvailabilityUpdate], PropertyInfo(alias="AvailabilityUpdates")]]
    """Availability updates."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    service_id: Required[Annotated[str, PropertyInfo(alias="ServiceId")]]
    """
    Unique identifier of the
    [Service](https://mews-systems.gitbook.io/connector-api/operations/#service) to
    update.
    """


class AvailabilityUpdateUnitCountAdjustment(TypedDict, total=False):
    value: Annotated[Optional[int], PropertyInfo(alias="Value")]


class AvailabilityUpdatePaxCount(TypedDict, total=False):
    person_count: Required[Annotated[int, PropertyInfo(alias="PersonCount")]]
    """Predicted guest count that will be assigned to the Resource.

    The guest count must fit within the Resource Category maximum capacity.
    """

    unit_count: Required[Annotated[int, PropertyInfo(alias="UnitCount")]]
    """Positive number of adjustments that are assigned to `PersonCount`.

    The sum of all `UnitCount` in `PaxCounts` should match the adjustment value
    applied to the interval.
    """


class AvailabilityUpdate(TypedDict, total=False):
    first_time_unit_start_utc: Required[
        Annotated[Union[str, datetime], PropertyInfo(alias="FirstTimeUnitStartUtc", format="iso8601")]
    ]
    """
    Start of the time interval, expressed as the timestamp for the start of the
    first
    [time unit](https://mews-systems.gitbook.io/connector-api/concepts/time-units),
    in UTC timezone ISO 8601 format.
    """

    last_time_unit_start_utc: Required[
        Annotated[Union[str, datetime], PropertyInfo(alias="LastTimeUnitStartUtc", format="iso8601")]
    ]
    """
    End of the time interval, expressed as the timestamp for the start of the last
    [time unit](https://mews-systems.gitbook.io/connector-api/concepts/time-units),
    in UTC timezone ISO 8601 format. The maximum size of time interval depends on
    the service's
    [time unit](https://mews-systems.gitbook.io/connector-api/concepts/time-units):
    367 hours if hours, 367 days if days, or 60 months if months.
    """

    resource_category_id: Required[Annotated[str, PropertyInfo(alias="ResourceCategoryId")]]
    """
    Unique identifier of the
    [Resource category](https://mews-systems.gitbook.io/connector-api/operations/resources#resource-category)
    whose availability to update.
    """

    unit_count_adjustment: Required[
        Annotated[AvailabilityUpdateUnitCountAdjustment, PropertyInfo(alias="UnitCountAdjustment")]
    ]
    """
    Adjustment value to be applied on the interval, can be both positive and
    negative (relative adjustment, not an absolute number). If specified without
    `Value` parameter, removes all adjustments within the interval.
    """

    availability_block_id: Annotated[Optional[str], PropertyInfo(alias="AvailabilityBlockId")]
    """
    Unique identifier of the
    [Availability block](https://mews-systems.gitbook.io/connector-api/operations/availabilityblocks#availability-block)
    whose availability to update.
    """

    end_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="EndUtc", format="iso8601")]

    pax_counts: Annotated[Optional[Iterable[AvailabilityUpdatePaxCount]], PropertyInfo(alias="PaxCounts")]
    """Collection of predicted occupancy of availability adjustments.

    Relates how many adjustments are assigned to each count of guests.
    """

    start_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="StartUtc", format="iso8601")]
