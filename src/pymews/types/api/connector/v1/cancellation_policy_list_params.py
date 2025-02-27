# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["CancellationPolicyListParams", "Limitation", "UpdatedUtc"]


class CancellationPolicyListParams(TypedDict, total=False):
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
    [Service](https://mews-systems.gitbook.io/connector-api/operations/services/#service).
    """

    activity_states: Annotated[Optional[List[Literal["Deleted", "Active"]]], PropertyInfo(alias="ActivityStates")]
    """Whether to return only active, only deleted, or both types of record.

    If not specified, only active records will be returned.
    """

    cancellation_policy_ids: Annotated[Optional[List[str]], PropertyInfo(alias="CancellationPolicyIds")]
    """
    Unique identifiers of the
    [Cancellation Policy](https://mews-systems.gitbook.io/connector-api/operations/#cancellationpolicy).
    Required if no other filter is provided.
    """

    enterprise_ids: Annotated[Optional[List[str]], PropertyInfo(alias="EnterpriseIds")]
    """Unique identifiers of the Enterprises.

    If not specified, the operation returns data for all enterprises within scope of
    the Access Token.
    """

    rate_group_ids: Annotated[Optional[List[str]], PropertyInfo(alias="RateGroupIds")]
    """
    Unique identifiers of the
    [Rate group](https://mews-systems.gitbook.io/connector-api/operations/rates/#rategroup).
    Required if no other filter is provided.
    """

    updated_utc: Annotated[Optional[UpdatedUtc], PropertyInfo(alias="UpdatedUtc")]
    """Interval in which the Cancellation Policy was updated.

    Required if no other filter is provided.
    """


class Limitation(TypedDict, total=False):
    count: Required[Annotated[int, PropertyInfo(alias="Count")]]

    cursor: Annotated[Optional[str], PropertyInfo(alias="Cursor")]


class UpdatedUtc(TypedDict, total=False):
    end_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="EndUtc", format="iso8601")]

    start_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="StartUtc", format="iso8601")]
