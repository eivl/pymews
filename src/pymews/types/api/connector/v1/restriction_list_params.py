# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["RestrictionListParams", "Limitation", "CollidingUtc", "CreatedUtc", "UpdatedUtc"]


class RestrictionListParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    limitation: Required[Annotated[Limitation, PropertyInfo(alias="Limitation")]]
    """Limitation on the quantity of data returned."""

    service_ids: Required[Annotated[List[str], PropertyInfo(alias="ServiceIds")]]
    """Unique identifiers of the `Service` from which the restrictions are requested."""

    base_rate_ids: Annotated[Optional[List[str]], PropertyInfo(alias="BaseRateIds")]
    """Unique identifiers of `Rate`.

    Returns only those restrictions which have matching `BaseRateId` set in
    `Restriction Condition`.
    """

    colliding_utc: Annotated[Optional[CollidingUtc], PropertyInfo(alias="CollidingUtc")]
    """Interval in which the `Restriction` is active."""

    created_utc: Annotated[Optional[CreatedUtc], PropertyInfo(alias="CreatedUtc")]
    """Interval in which the `Restriction` was created."""

    end_utc: Annotated[Optional[str], PropertyInfo(alias="EndUtc")]

    enterprise_ids: Annotated[Optional[List[str]], PropertyInfo(alias="EnterpriseIds")]
    """Unique identifiers of the Enterprises.

    If not specified, the operation returns data for all enterprises within scope of
    the Access Token.
    """

    exact_rate_ids: Annotated[Optional[List[str]], PropertyInfo(alias="ExactRateIds")]
    """Unique identifiers of `Rate`.

    Returns only those restrictions which have matching `ExactRateId` set in
    `Restriction Condition`.
    """

    origin: Annotated[Optional[Literal["User", "Integration"]], PropertyInfo(alias="Origin")]
    """Restriction origin.

    Returns only those restrictions which have matching Origin or all if not
    specified.

    - `User` - Restriction was created by a user in Mews.
    - `Integration` - Restriction was created by a 3rd-party integration.
    """

    rate_ids: Annotated[Optional[List[str]], PropertyInfo(alias="RateIds")]
    """Unique identifiers of `Rate`.

    Returns all restrictions that affect the given rates, i.e. ones without any
    `Restriction Conditions`, ones assigned directly to specified rates, ones
    assigned to `Rate group` of specified rates, or ones inherited from base
    rates.`.
    """

    resource_category_ids: Annotated[Optional[List[str]], PropertyInfo(alias="ResourceCategoryIds")]
    """Unique identifiers of `Resource category`."""

    restriction_ids: Annotated[Optional[List[str]], PropertyInfo(alias="RestrictionIds")]
    """Unique identifiers of the `Restriction`."""

    start_utc: Annotated[Optional[str], PropertyInfo(alias="StartUtc")]

    time_filter: Annotated[Optional[str], PropertyInfo(alias="TimeFilter")]

    updated_utc: Annotated[Optional[UpdatedUtc], PropertyInfo(alias="UpdatedUtc")]
    """Interval in which the `Restriction` was updated."""


class Limitation(TypedDict, total=False):
    count: Required[Annotated[int, PropertyInfo(alias="Count")]]

    cursor: Annotated[Optional[str], PropertyInfo(alias="Cursor")]


class CollidingUtc(TypedDict, total=False):
    end_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="EndUtc", format="iso8601")]

    start_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="StartUtc", format="iso8601")]


class CreatedUtc(TypedDict, total=False):
    end_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="EndUtc", format="iso8601")]

    start_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="StartUtc", format="iso8601")]


class UpdatedUtc(TypedDict, total=False):
    end_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="EndUtc", format="iso8601")]

    start_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="StartUtc", format="iso8601")]
