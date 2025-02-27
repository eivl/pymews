# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["RateListParams", "Limitation", "Extent", "UpdatedUtc"]


class RateListParams(TypedDict, total=False):
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
    Unique identifiers of the
    [Services](https://mews-systems.gitbook.io/connector-api/operations/services/#service)
    from which the rates are requested.
    """

    activity_states: Annotated[Optional[List[Literal["Deleted", "Active"]]], PropertyInfo(alias="ActivityStates")]
    """Whether to return only active, only deleted, or both types of record.

    If not specified, both active and deleted will be returned.
    """

    enterprise_ids: Annotated[Optional[List[str]], PropertyInfo(alias="EnterpriseIds")]
    """Unique identifiers of the Enterprises.

    If not specified, the operation returns data for all enterprises within scope of
    the Access Token.
    """

    extent: Annotated[Optional[Extent], PropertyInfo(alias="Extent")]
    """Extent of data to be returned."""

    external_identifiers: Annotated[Optional[List[str]], PropertyInfo(alias="ExternalIdentifiers")]
    """
    Identifiers of
    [Rate](https://mews-systems.gitbook.io/connector-api/operations/#rate) from
    external systems.
    """

    rate_ids: Annotated[Optional[List[str]], PropertyInfo(alias="RateIds")]
    """
    Unique identifiers of the requested
    [Rates](https://mews-systems.gitbook.io/connector-api/operations/rates/#rate).
    """

    updated_utc: Annotated[Optional[UpdatedUtc], PropertyInfo(alias="UpdatedUtc")]
    """Interval in which `Rate` was updated."""


class Limitation(TypedDict, total=False):
    count: Required[Annotated[int, PropertyInfo(alias="Count")]]

    cursor: Annotated[Optional[str], PropertyInfo(alias="Cursor")]


class Extent(TypedDict, total=False):
    availability_block_assignments: Annotated[bool, PropertyInfo(alias="AvailabilityBlockAssignments")]
    """Whether the response should contain availability block assignments."""

    rate_groups: Annotated[Optional[bool], PropertyInfo(alias="RateGroups")]
    """Whether the response should contain rate groups."""

    rates: Annotated[Optional[bool], PropertyInfo(alias="Rates")]
    """Whether the response should contain rates."""


class UpdatedUtc(TypedDict, total=False):
    end_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="EndUtc", format="iso8601")]

    start_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="StartUtc", format="iso8601")]
