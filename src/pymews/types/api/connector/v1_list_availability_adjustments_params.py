# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["V1ListAvailabilityAdjustmentsParams", "Limitation", "UpdatedUtc"]


class V1ListAvailabilityAdjustmentsParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    limitation: Required[Annotated[Limitation, PropertyInfo(alias="Limitation")]]
    """Limitation on the quantity of data returned."""

    activity_states: Annotated[Optional[List[Literal["Deleted", "Active"]]], PropertyInfo(alias="ActivityStates")]
    """Whether to return only active, only deleted, or both types of record.

    If not specified, only active records will be returned.
    """

    availability_adjustment_ids: Annotated[Optional[List[str]], PropertyInfo(alias="AvailabilityAdjustmentIds")]
    """
    Unique identifiers of the requested
    [Availability adjustments](https://mews-systems.gitbook.io/connector-api/operations/#availability-adjustment).
    """

    enterprise_ids: Annotated[Optional[List[str]], PropertyInfo(alias="EnterpriseIds")]
    """Unique identifiers of the Enterprises.

    If not specified, the operation returns data for all enterprises within scope of
    the Access Token.
    """

    updated_utc: Annotated[Optional[UpdatedUtc], PropertyInfo(alias="UpdatedUtc")]
    """Interval in which the availability adjustments were updated."""


class Limitation(TypedDict, total=False):
    count: Required[Annotated[int, PropertyInfo(alias="Count")]]

    cursor: Annotated[Optional[str], PropertyInfo(alias="Cursor")]


class UpdatedUtc(TypedDict, total=False):
    end_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="EndUtc", format="iso8601")]

    start_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="StartUtc", format="iso8601")]
