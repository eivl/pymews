# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["ServiceOverbookingLimitSetParams", "SetServiceOverbookingLimit"]


class ServiceOverbookingLimitSetParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    service_id: Required[Annotated[str, PropertyInfo(alias="ServiceId")]]
    """
    Unique identifier of the
    [Service](https://mews-systems.gitbook.io/connector-api/operations/services#service)
    overbooking limits will be set in.
    """

    set_service_overbooking_limits: Required[
        Annotated[Iterable[SetServiceOverbookingLimit], PropertyInfo(alias="SetServiceOverbookingLimits")]
    ]
    """Collection of service overbooking limits to be set."""

    enterprise_id: Annotated[Optional[str], PropertyInfo(alias="EnterpriseId")]
    """Unique identifier of the enterprise.

    Required when using
    [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
    ignored otherwise.
    """


class SetServiceOverbookingLimit(TypedDict, total=False):
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
    367 days.
    """

    limit: Required[Annotated[int, PropertyInfo(alias="Limit")]]
    """Number of overbookings allowed for the `Service`. Must be non-negative."""
