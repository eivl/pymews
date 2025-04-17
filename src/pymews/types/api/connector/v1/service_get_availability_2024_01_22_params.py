# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["ServiceGetAvailability2024_01_22Params"]


class ServiceGetAvailability2024_01_22Params(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    first_time_unit_start_utc: Required[
        Annotated[Union[str, datetime], PropertyInfo(alias="FirstTimeUnitStartUtc", format="iso8601")]
    ]
    """
    Start of the time interval, expressed as the timestamp for the start of the
    first
    [time unit](https://mews-systems.gitbook.io/connector-api/concepts/time-units/),
    in UTC timezone ISO 8601 format.
    """

    last_time_unit_start_utc: Required[
        Annotated[Union[str, datetime], PropertyInfo(alias="LastTimeUnitStartUtc", format="iso8601")]
    ]
    """
    End of the time interval, expressed as the timestamp for the start of the last
    [time unit](https://mews-systems.gitbook.io/connector-api/concepts/time-units/),
    in UTC timezone ISO 8601 format. The maximum size of time interval depends on
    the service's
    [time unit](https://mews-systems.gitbook.io/connector-api/concepts/time-units/):
    367 hours if hours, 367 days if days, or 60 months if months.
    """

    metrics: Required[
        Annotated[
            List[
                Literal[
                    "OutOfOrderBlocks",
                    "PublicAvailabilityAdjustment",
                    "OtherServiceReservationCount",
                    "Occupied",
                    "ConfirmedReservations",
                    "OptionalReservations",
                    "BlockAvailability",
                    "AllocatedBlockAvailability",
                    "UsableResources",
                    "ActiveResources",
                ]
            ],
            PropertyInfo(alias="Metrics"),
        ]
    ]
    """
    Set of
    [Service availability metrics](https://mews-systems.gitbook.io/connector-api/operations/services/#service-availability-metrics)
    to be returned.
    """

    service_id: Required[Annotated[str, PropertyInfo(alias="ServiceId")]]
    """
    Unique identifier of the
    [Service](https://mews-systems.gitbook.io/connector-api/operations/services/#service)
    whose availability should be returned.
    """
