# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["TaskAddParams"]


class TaskAddParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    deadline_utc: Required[Annotated[Union[str, datetime], PropertyInfo(alias="DeadlineUtc", format="iso8601")]]
    """Deadline of the task in UTC timezone in ISO 8601 format."""

    name: Required[Annotated[str, PropertyInfo(alias="Name")]]
    """Name (or title) of the task."""

    department_id: Annotated[Optional[str], PropertyInfo(alias="DepartmentId")]
    """
    Unique identifier of the
    [Department](https://mews-systems.gitbook.io/connector-api/operations/departments/#department)
    the task is addressed to.
    """

    description: Annotated[Optional[str], PropertyInfo(alias="Description")]
    """Further decription of the task."""

    service_order_id: Annotated[Optional[str], PropertyInfo(alias="ServiceOrderId")]
    """
    Unique identifier of the service order (reservation or product service order)
    the task is linked with.
    """
