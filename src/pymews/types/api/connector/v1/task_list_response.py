# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["TaskListResponse", "Task"]


class Task(BaseModel):
    closed_utc: str = FieldInfo(alias="ClosedUtc")
    """Last update date and time of the task in UTC timezone in ISO 8601 format."""

    created_utc: str = FieldInfo(alias="CreatedUtc")
    """Creation date and time of the task in UTC timezone in ISO 8601 format."""

    deadline_utc: str = FieldInfo(alias="DeadlineUtc")
    """Deadline date and time of the task in UTC timezone in ISO 8601 format."""

    name: str = FieldInfo(alias="Name")
    """Name (or title) of the task."""

    state: str = FieldInfo(alias="State")
    """State of the task."""

    department_id: Optional[str] = FieldInfo(alias="DepartmentId", default=None)
    """Unique identifier of the Department the task is addressed to."""

    description: Optional[str] = FieldInfo(alias="Description", default=None)
    """Further description of the task."""

    enterprise_id: Optional[str] = FieldInfo(alias="EnterpriseId", default=None)
    """Unique identifier of the enterprise.

    Required when using Portfolio Access Tokens, ignored otherwise.
    """

    id: Optional[str] = FieldInfo(alias="Id", default=None)
    """Unique identifier of the task."""

    service_order_id: Optional[str] = FieldInfo(alias="ServiceOrderId", default=None)
    """
    Unique identifier of the service order (reservation or product service order)
    the task is linked with.
    """


class TaskListResponse(BaseModel):
    tasks: List[Task] = FieldInfo(alias="Tasks")
    """The filtered tasks."""

    cursor: Optional[str] = FieldInfo(alias="Cursor", default=None)
    """
    Unique identifier of the item one newer in time order than the items to be
    returned. If Cursor is not specified, i.e. null, then the latest or most recent
    items will be returned.
    """
