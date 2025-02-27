# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["ResourceBlockListParams", "Extent", "Limitation", "CollidingUtc", "CreatedUtc", "UpdatedUtc"]


class ResourceBlockListParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    extent: Required[Annotated[Extent, PropertyInfo(alias="Extent")]]
    """Extent of data to be returned."""

    limitation: Required[Annotated[Limitation, PropertyInfo(alias="Limitation")]]
    """Limitation on the quantity of data returned."""

    assigned_resource_ids: Annotated[Optional[List[str]], PropertyInfo(alias="AssignedResourceIds")]
    """
    Unique identifiers of the requested Assigned
    [Resources](https://mews-systems.gitbook.io/connector-api/operations/resources/#resource).
    """

    colliding_utc: Annotated[Optional[CollidingUtc], PropertyInfo(alias="CollidingUtc")]

    created_utc: Annotated[Optional[CreatedUtc], PropertyInfo(alias="CreatedUtc")]

    enterprise_ids: Annotated[Optional[List[str]], PropertyInfo(alias="EnterpriseIds")]
    """Unique identifiers of the Enterprises.

    If not specified, the operation returns data for all enterprises within scope of
    the Access Token.
    """

    resource_block_ids: Annotated[Optional[List[str]], PropertyInfo(alias="ResourceBlockIds")]
    """
    Unique identifiers of the requested
    [Resource blocks](https://mews-systems.gitbook.io/connector-api/operations/#resource-block).
    """

    updated_utc: Annotated[Optional[UpdatedUtc], PropertyInfo(alias="UpdatedUtc")]


class Extent(TypedDict, total=False):
    inactive: Annotated[bool, PropertyInfo(alias="Inactive")]


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
