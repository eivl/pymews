# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["TaskListParams", "Limitation", "ClosedUtc", "CreatedUtc", "DeadlineUtc"]


class TaskListParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    limitation: Required[Annotated[Limitation, PropertyInfo(alias="Limitation")]]
    """Limitation on the quantity of data returned."""

    closed_utc: Annotated[Optional[ClosedUtc], PropertyInfo(alias="ClosedUtc")]
    """Interval in which the Task was closed."""

    created_utc: Annotated[Optional[CreatedUtc], PropertyInfo(alias="CreatedUtc")]
    """Interval in which the Task was created."""

    deadline_utc: Annotated[Optional[DeadlineUtc], PropertyInfo(alias="DeadlineUtc")]
    """Interval in which the Task has a deadline."""

    department_ids: Annotated[Optional[List[str]], PropertyInfo(alias="DepartmentIds")]
    """
    Unique identifiers of
    [Departments](https://mews-systems.gitbook.io/connector-api/operations/departments/#department).
    Not possible to be used standalone, needs to be used in combination with other
    filters.
    """

    enterprise_ids: Annotated[Optional[List[str]], PropertyInfo(alias="EnterpriseIds")]
    """Unique identifiers of the Enterprises.

    If not specified, the operation returns data for all enterprises within scope of
    the Access Token.
    """

    service_order_ids: Annotated[Optional[List[str]], PropertyInfo(alias="ServiceOrderIds")]
    """Unique identifiers of service orders (reservations or product service orders)."""

    task_ids: Annotated[Optional[List[str]], PropertyInfo(alias="TaskIds")]
    """
    Unique identifiers of
    [Tasks](https://mews-systems.gitbook.io/connector-api/operations/#task).
    """


class Limitation(TypedDict, total=False):
    count: Required[Annotated[int, PropertyInfo(alias="Count")]]

    cursor: Annotated[Optional[str], PropertyInfo(alias="Cursor")]


class ClosedUtc(TypedDict, total=False):
    end_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="EndUtc", format="iso8601")]

    start_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="StartUtc", format="iso8601")]


class CreatedUtc(TypedDict, total=False):
    end_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="EndUtc", format="iso8601")]

    start_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="StartUtc", format="iso8601")]


class DeadlineUtc(TypedDict, total=False):
    end_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="EndUtc", format="iso8601")]

    start_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="StartUtc", format="iso8601")]
