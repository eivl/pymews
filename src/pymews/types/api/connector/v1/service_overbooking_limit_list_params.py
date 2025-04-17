# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["ServiceOverbookingLimitListParams", "Limitation", "CollidingUtc", "UpdatedUtc"]


class ServiceOverbookingLimitListParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    limitation: Required[Annotated[Limitation, PropertyInfo(alias="Limitation")]]
    """Limitation on the quantity of data returned."""

    service_ids: Required[Annotated[List[str], PropertyInfo(alias="ServiceIds")]]
    """
    Unique identifiers of `Services` associated with the service overbooking limits.
    """

    activity_states: Annotated[Optional[List[Literal["Deleted", "Active"]]], PropertyInfo(alias="ActivityStates")]
    """Whether to return only active, only deleted, or both types of record.

    If not specified, only active records will be returned.
    """

    colliding_utc: Annotated[Optional[CollidingUtc], PropertyInfo(alias="CollidingUtc")]
    """Interval in which the service overbooking limit is active."""

    enterprise_ids: Annotated[Optional[List[str]], PropertyInfo(alias="EnterpriseIds")]
    """Unique identifiers of the Enterprises.

    If not specified, the operation returns data for all enterprises within scope of
    the Access Token.
    """

    service_overbooking_limit_ids: Annotated[Optional[List[str]], PropertyInfo(alias="ServiceOverbookingLimitIds")]
    """Unique identifiers of the service overbooking limits."""

    updated_utc: Annotated[Optional[UpdatedUtc], PropertyInfo(alias="UpdatedUtc")]
    """Interval in which the service overbooking limits were updated."""


class Limitation(TypedDict, total=False):
    count: Required[Annotated[int, PropertyInfo(alias="Count")]]

    cursor: Annotated[Optional[str], PropertyInfo(alias="Cursor")]


class CollidingUtc(TypedDict, total=False):
    end_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="EndUtc", format="iso8601")]

    start_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="StartUtc", format="iso8601")]


class UpdatedUtc(TypedDict, total=False):
    end_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="EndUtc", format="iso8601")]

    start_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="StartUtc", format="iso8601")]
