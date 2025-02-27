# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["V1ListOutletsResponse", "Outlet"]


class Outlet(BaseModel):
    created_utc: datetime = FieldInfo(alias="CreatedUtc")
    """Creation date and time of the outlet in UTC timezone in ISO 8601 format."""

    enterprise_id: str = FieldInfo(alias="EnterpriseId")
    """
    Unique identifier of the
    [Enterprise](https://mews-systems.gitbook.io/connector-api/operations/enterprises/#enterprise).
    """

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the outlet."""

    is_active: bool = FieldInfo(alias="IsActive")
    """Whether the outlet is still active."""

    name: str = FieldInfo(alias="Name")
    """Name of the outlet."""

    updated_utc: datetime = FieldInfo(alias="UpdatedUtc")
    """Last update date and time of the outlet in UTC timezone in ISO 8601 format."""


class V1ListOutletsResponse(BaseModel):
    outlets: List[Outlet] = FieldInfo(alias="Outlets")
    """The outlets of the enterprise."""

    cursor: Optional[str] = FieldInfo(alias="Cursor", default=None)
    """
    Unique identifier of the item one newer in time order than the items to be
    returned. If Cursor is not specified, i.e. null, then the latest or most recent
    items will be returned.
    """
