# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["V1ListAvailabilityAdjustmentsResponse", "AvailabilityAdjustment", "AvailabilityAdjustmentPaxCount"]


class AvailabilityAdjustmentPaxCount(BaseModel):
    person_count: int = FieldInfo(alias="PersonCount")
    """Predicted guest count that will be assigned to the Resource.

    The guest count must fit within the Resource Category maximum capacity.
    """

    unit_count: int = FieldInfo(alias="UnitCount")
    """Positive number of adjustments that are assigned to `PersonCount`.

    The sum of all `UnitCount` in `PaxCounts` should match the adjustment value
    applied to the interval.
    """


class AvailabilityAdjustment(BaseModel):
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

    pax_counts: Optional[List[AvailabilityAdjustmentPaxCount]] = FieldInfo(alias="PaxCounts", default=None)
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


class V1ListAvailabilityAdjustmentsResponse(BaseModel):
    availability_adjustments: List[AvailabilityAdjustment] = FieldInfo(alias="AvailabilityAdjustments")
    """Availability adjustments."""

    cursor: Optional[str] = FieldInfo(alias="Cursor", default=None)
    """
    Unique identifier of the item one newer in time order than the items to be
    returned. If Cursor is not specified, i.e. null, then the latest or most recent
    items will be returned.
    """
