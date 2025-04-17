# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["ServiceOverbookingLimitListResponse", "ServiceOverbookingLimit"]


class ServiceOverbookingLimit(BaseModel):
    created_utc: datetime = FieldInfo(alias="CreatedUtc")
    """
    Timestamp in UTC timezone ISO 8601 format when the service overbooking was
    created.
    """

    first_time_unit_start_utc: datetime = FieldInfo(alias="FirstTimeUnitStartUtc")
    """
    Start of the time interval, expressed as the timestamp for the start of the
    first
    [time unit](https://mews-systems.gitbook.io/connector-api/concepts/time-units/),
    in UTC timezone ISO 8601 format.
    """

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the service overbooking limit."""

    is_active: bool = FieldInfo(alias="IsActive")
    """Whether the service overbooking limit is still active."""

    last_time_unit_start_utc: datetime = FieldInfo(alias="LastTimeUnitStartUtc")
    """
    End of the time interval, expressed as the timestamp for the start of the last
    [time unit](https://mews-systems.gitbook.io/connector-api/concepts/time-units/),
    in UTC timezone ISO 8601 format.
    """

    limit: int = FieldInfo(alias="Limit")
    """Number of overbookings allowed for the `Service`."""

    service_id: str = FieldInfo(alias="ServiceId")
    """Unique identifier of the `Service`."""

    updated_utc: datetime = FieldInfo(alias="UpdatedUtc")
    """
    Timestamp in UTC timezone ISO 8601 format when the service overbooking was
    updated.
    """


class ServiceOverbookingLimitListResponse(BaseModel):
    service_overbooking_limits: List[ServiceOverbookingLimit] = FieldInfo(alias="ServiceOverbookingLimits")
    """Service overbooking limits of the default service."""

    cursor: Optional[str] = FieldInfo(alias="Cursor", default=None)
    """
    Unique identifier of the item one newer in time order than the items to be
    returned. If Cursor is not specified, i.e. null, then the latest or most recent
    items will be returned.
    """
