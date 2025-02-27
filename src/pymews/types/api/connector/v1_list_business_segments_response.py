# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["V1ListBusinessSegmentsResponse", "BusinessSegment"]


class BusinessSegment(BaseModel):
    created_utc: datetime = FieldInfo(alias="CreatedUtc")
    """
    Creation date and time of the business segment in UTC timezone in ISO 8601
    format.
    """

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the business segment."""

    is_active: bool = FieldInfo(alias="IsActive")
    """Whether the business segment is still active."""

    name: str = FieldInfo(alias="Name")
    """Name of the business segment."""

    service_id: str = FieldInfo(alias="ServiceId")
    """Unique identifier of the `Service`."""

    updated_utc: datetime = FieldInfo(alias="UpdatedUtc")
    """
    Last update date and time of the business segment in UTC timezone in ISO 8601
    format.
    """


class V1ListBusinessSegmentsResponse(BaseModel):
    business_segments: List[BusinessSegment] = FieldInfo(alias="BusinessSegments")
    """Business segments."""

    cursor: Optional[str] = FieldInfo(alias="Cursor", default=None)
    """Unique identifier of the last and hence oldest business segment item returned.

    This can be used in Limitation in a subsequent request to fetch the next batch
    of older business segment.
    """
