# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = [
    "ServiceGetAvailability2024_01_22Response",
    "ResourceCategoryAvailability",
    "ResourceCategoryAvailabilityMetrics",
]


class ResourceCategoryAvailabilityMetrics(BaseModel):
    active_resources: Optional[List[int]] = FieldInfo(alias="ActiveResources", default=None)

    allocated_block_availability: Optional[List[int]] = FieldInfo(alias="AllocatedBlockAvailability", default=None)

    block_availability: Optional[List[int]] = FieldInfo(alias="BlockAvailability", default=None)

    confirmed_reservations: Optional[List[int]] = FieldInfo(alias="ConfirmedReservations", default=None)

    occupied: Optional[List[int]] = FieldInfo(alias="Occupied", default=None)

    optional_reservations: Optional[List[int]] = FieldInfo(alias="OptionalReservations", default=None)

    other_service_reservation_count: Optional[List[int]] = FieldInfo(alias="OtherServiceReservationCount", default=None)

    out_of_order_blocks: Optional[List[int]] = FieldInfo(alias="OutOfOrderBlocks", default=None)

    public_availability_adjustment: Optional[List[int]] = FieldInfo(alias="PublicAvailabilityAdjustment", default=None)

    usable_resources: Optional[List[int]] = FieldInfo(alias="UsableResources", default=None)


class ResourceCategoryAvailability(BaseModel):
    metrics: ResourceCategoryAvailabilityMetrics = FieldInfo(alias="Metrics")
    """
    Dictionary keys are names of
    [Service availability metrics](https://mews-systems.gitbook.io/connector-api/operations/services#service-availability-metrics),
    values are arrays of integers with metric values for corresponding time unit in
    `TimeUnitStartsUtc`.
    """

    resource_category_id: str = FieldInfo(alias="ResourceCategoryId")
    """
    Unique identifier of the
    [Resource category](https://mews-systems.gitbook.io/connector-api/operations/resources#resource-category).
    """


class ServiceGetAvailability2024_01_22Response(BaseModel):
    resource_category_availabilities: List[ResourceCategoryAvailability] = FieldInfo(
        alias="ResourceCategoryAvailabilities"
    )
    """Resource category availabilities.

    Can be empty if no resource categories are assigned to the service.
    """

    time_unit_starts_utc: List[str] = FieldInfo(alias="TimeUnitStartsUtc")
    """
    Set of all time units covered by the time interval; expressed in UTC timezone
    ISO 8601 format.
    """
