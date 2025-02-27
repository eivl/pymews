# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = [
    "AvailabilityBlockListParams",
    "Extent",
    "Limitation",
    "CollidingUtc",
    "CreatedUtc",
    "ReleasedUtc",
    "UpdatedUtc",
]


class AvailabilityBlockListParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    extent: Required[Annotated[Extent, PropertyInfo(alias="Extent")]]

    limitation: Required[Annotated[Limitation, PropertyInfo(alias="Limitation")]]
    """Limitation on the quantity of data returned."""

    activity_states: Annotated[Optional[List[str]], PropertyInfo(alias="ActivityStates")]
    """Whether to return only active, only deleted or both records."""

    availability_block_ids: Annotated[Optional[List[str]], PropertyInfo(alias="AvailabilityBlockIds")]
    """Unique identifiers of the requested `Availability blocks`."""

    colliding_utc: Annotated[Optional[CollidingUtc], PropertyInfo(alias="CollidingUtc")]
    """Interval in which the `Availability blocks` are active."""

    created_utc: Annotated[Optional[CreatedUtc], PropertyInfo(alias="CreatedUtc")]
    """Interval in which the availability blocks were created."""

    enterprise_ids: Annotated[Optional[List[str]], PropertyInfo(alias="EnterpriseIds")]
    """Unique identifiers of the Enterprises.

    If not specified, the operation returns data for all enterprises within scope of
    the Access Token.
    """

    external_identifiers: Annotated[Optional[List[str]], PropertyInfo(alias="ExternalIdentifiers")]
    """Identifiers of `Availability blocks` from external systems."""

    released_utc: Annotated[Optional[ReleasedUtc], PropertyInfo(alias="ReleasedUtc")]
    """Interval in which the `Availability blocks`are released."""

    service_ids: Annotated[Optional[List[str]], PropertyInfo(alias="ServiceIds")]
    """
    Unique identifiers of the `Services` to which `Availability blocks` are
    assigned.
    """

    states: Annotated[
        Optional[List[Literal["Confirmed", "Optional", "Inquired", "Canceled"]]], PropertyInfo(alias="States")
    ]
    """States the availability blocks should be in."""

    updated_utc: Annotated[Optional[UpdatedUtc], PropertyInfo(alias="UpdatedUtc")]
    """Interval in which the `Availability blocks` were updated."""


class Extent(TypedDict, total=False):
    adjustments: Annotated[Optional[bool], PropertyInfo(alias="Adjustments")]
    """
    Whether the response should contain individual availability adjustments related
    to availability blocks.
    """

    availability_blocks: Annotated[Optional[bool], PropertyInfo(alias="AvailabilityBlocks")]
    """Whether the response should contain the general availability blocks."""

    rates: Annotated[Optional[bool], PropertyInfo(alias="Rates")]
    """Whether the response should contain rates related to availability blocks."""

    service_orders: Annotated[Optional[bool], PropertyInfo(alias="ServiceOrders")]
    """
    Whether the response should contain reservations related to availability blocks.
    """


class Limitation(TypedDict, total=False):
    count: Required[Annotated[int, PropertyInfo(alias="Count")]]

    cursor: Annotated[Optional[str], PropertyInfo(alias="Cursor")]


class CollidingUtc(TypedDict, total=False):
    end_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="EndUtc", format="iso8601")]

    start_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="StartUtc", format="iso8601")]


class CreatedUtc(TypedDict, total=False):
    end_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="EndUtc", format="iso8601")]

    start_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="StartUtc", format="iso8601")]


class ReleasedUtc(TypedDict, total=False):
    end_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="EndUtc", format="iso8601")]

    start_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="StartUtc", format="iso8601")]


class UpdatedUtc(TypedDict, total=False):
    end_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="EndUtc", format="iso8601")]

    start_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="StartUtc", format="iso8601")]
