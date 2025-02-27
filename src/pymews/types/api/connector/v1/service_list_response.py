# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = [
    "ServiceListResponse",
    "Service",
    "ServiceData",
    "ServiceDataValue",
    "ServiceDataValueBookableServiceData",
    "ServiceDataValueAdditionalServiceData",
    "ServiceDataValueAdditionalServiceDataPromotions",
    "ServiceOptions",
    "ServicePromotions",
]


class ServiceDataValueBookableServiceData(BaseModel):
    end_offset: str = FieldInfo(alias="EndOffset")
    """
    Offset from the end of the
    [time unit](https://mews-systems.gitbook.io/connector-api/concepts/time-units/)
    which defines the default end of the service; expressed in ISO 8601 duration
    format.
    """

    occupancy_end_offset: str = FieldInfo(alias="OccupancyEndOffset")
    """
    Offset from the end of the
    [time unit](https://mews-systems.gitbook.io/connector-api/concepts/time-units/)
    which defines the occupancy end of the service; expressed in ISO 8601 duration
    format. 'Occupancy end' is used for availability and reporting purposes, it
    implies the time at which the booked resource is no longer considered occupied.
    """

    occupancy_start_offset: str = FieldInfo(alias="OccupancyStartOffset")
    """
    Offset from the start of the
    [time unit](https://mews-systems.gitbook.io/connector-api/concepts/time-units/)
    which defines the occupancy start of the service; expressed in ISO 8601 duration
    format. 'Occupancy start' is used for availability and reporting purposes, it
    implies the time at which the booked resource is considered occupied.
    """

    start_offset: str = FieldInfo(alias="StartOffset")
    """
    Offset from the start of the
    [time unit](https://mews-systems.gitbook.io/connector-api/concepts/time-units/)
    which defines the default start of the service; expressed in ISO 8601 duration
    format.
    """

    time_unit: Literal["Day", "Month", "Hour"] = FieldInfo(alias="TimeUnit")
    """Day

    Month

    Hour
    """

    time_unit_period: Literal["Day", "Month", "Hour"] = FieldInfo(alias="TimeUnitPeriod")
    """Day

    Month

    Hour
    """


class ServiceDataValueAdditionalServiceDataPromotions(BaseModel):
    after_check_in: bool = FieldInfo(alias="AfterCheckIn")
    """Whether it can be promoted after check-in."""

    after_check_out: bool = FieldInfo(alias="AfterCheckOut")
    """Whether it can be promoted after check-out."""

    before_check_in: bool = FieldInfo(alias="BeforeCheckIn")
    """Whether it can be promoted before check-in."""

    before_check_out: bool = FieldInfo(alias="BeforeCheckOut")
    """Whether it can be promoted before check-out."""

    during_check_out: bool = FieldInfo(alias="DuringCheckOut")
    """Whether it can be promoted during check-out."""

    during_stay: bool = FieldInfo(alias="DuringStay")
    """Whether it can be promoted during stay."""


class ServiceDataValueAdditionalServiceData(BaseModel):
    promotions: ServiceDataValueAdditionalServiceDataPromotions = FieldInfo(alias="Promotions")


ServiceDataValue: TypeAlias = Union[ServiceDataValueBookableServiceData, ServiceDataValueAdditionalServiceData]


class ServiceData(BaseModel):
    discriminator: Optional[Literal["Bookable", "Additional"]] = None

    value: Optional[ServiceDataValue] = None


class ServiceOptions(BaseModel):
    bill_as_package: bool = FieldInfo(alias="BillAsPackage")
    """Products should be displayed as a single package instead of individual items."""


class ServicePromotions(BaseModel):
    after_check_in: bool = FieldInfo(alias="AfterCheckIn")
    """Whether it can be promoted after check-in."""

    after_check_out: bool = FieldInfo(alias="AfterCheckOut")
    """Whether it can be promoted after check-out."""

    before_check_in: bool = FieldInfo(alias="BeforeCheckIn")
    """Whether it can be promoted before check-in."""

    before_check_out: bool = FieldInfo(alias="BeforeCheckOut")
    """Whether it can be promoted before check-out."""

    during_check_out: bool = FieldInfo(alias="DuringCheckOut")
    """Whether it can be promoted during check-out."""

    during_stay: bool = FieldInfo(alias="DuringStay")
    """Whether it can be promoted during stay."""


class Service(BaseModel):
    created_utc: datetime = FieldInfo(alias="CreatedUtc")
    """Creation date and time of the service in UTC timezone in ISO 8601 format."""

    data: ServiceData = FieldInfo(alias="Data")
    """Additional information about the specific service."""

    enterprise_id: str = FieldInfo(alias="EnterpriseId")
    """
    Unique identifier of the
    [Enterprise](https://mews-systems.gitbook.io/connector-api/operations/enterprises/#enterprise).
    """

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the service."""

    is_active: bool = FieldInfo(alias="IsActive")
    """Whether the service is still active."""

    name: str = FieldInfo(alias="Name")
    """Name of the service."""

    names: Dict[str, str] = FieldInfo(alias="Names")
    """All translations of the name."""

    options: ServiceOptions = FieldInfo(alias="Options")
    """Options of the service."""

    ordering: int = FieldInfo(alias="Ordering")
    """Order value for presentation purposes."""

    updated_utc: datetime = FieldInfo(alias="UpdatedUtc")
    """Last update date and time of the service in UTC timezone in ISO 8601 format."""

    end_time: Optional[str] = FieldInfo(alias="EndTime", default=None)

    external_identifier: Optional[str] = FieldInfo(alias="ExternalIdentifier", default=None)
    """Identifier of the service from external system."""

    promotions: Optional[ServicePromotions] = FieldInfo(alias="Promotions", default=None)

    start_time: Optional[str] = FieldInfo(alias="StartTime", default=None)

    type: Optional[str] = FieldInfo(alias="Type", default=None)


class ServiceListResponse(BaseModel):
    services: List[Service] = FieldInfo(alias="Services")
    """Services offered by the enterprise."""

    cursor: Optional[str] = FieldInfo(alias="Cursor", default=None)
    """
    Unique identifier of the item one newer in time order than the items to be
    returned. If Cursor is not specified, i.e. null, then the latest or most recent
    items will be returned.
    """
