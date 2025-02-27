# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["V1ListResourceCategoryAssignmentsParams", "Limitation", "UpdatedUtc"]


class V1ListResourceCategoryAssignmentsParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    limitation: Required[Annotated[Limitation, PropertyInfo(alias="Limitation")]]
    """Limitation on the quantity of data returned."""

    resource_category_ids: Required[Annotated[List[str], PropertyInfo(alias="ResourceCategoryIds")]]
    """
    Unique identifiers of
    [Resource categories](https://mews-systems.gitbook.io/connector-api/operations/#resource-category)
    to which the resource category assignment belong.
    """

    activity_states: Annotated[Optional[List[Literal["Deleted", "Active"]]], PropertyInfo(alias="ActivityStates")]
    """Whether to return only active, only deleted or both records."""

    enterprise_ids: Annotated[Optional[List[str]], PropertyInfo(alias="EnterpriseIds")]
    """Unique identifiers of the Enterprises.

    If not specified, the operation returns data for all enterprises within scope of
    the Access Token.
    """

    resource_category_assignment_ids: Annotated[
        Optional[List[str]], PropertyInfo(alias="ResourceCategoryAssignmentIds")
    ]
    """
    Unique identifiers of
    [Resource category assignment](https://mews-systems.gitbook.io/connector-api/operations/resourcecategories/#resource-category-assignment).
    """

    resource_ids: Annotated[Optional[List[str]], PropertyInfo(alias="ResourceIds")]
    """
    Unique identifiers of resources to which the resource category assignments
    belong.
    """

    updated_utc: Annotated[Optional[UpdatedUtc], PropertyInfo(alias="UpdatedUtc")]
    """Interval in which the resource category assignments were updated."""


class Limitation(TypedDict, total=False):
    count: Required[Annotated[int, PropertyInfo(alias="Count")]]

    cursor: Annotated[Optional[str], PropertyInfo(alias="Cursor")]


class UpdatedUtc(TypedDict, total=False):
    end_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="EndUtc", format="iso8601")]

    start_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="StartUtc", format="iso8601")]
