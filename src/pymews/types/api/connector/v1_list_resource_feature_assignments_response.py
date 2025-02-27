# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["V1ListResourceFeatureAssignmentsResponse", "ResourceFeatureAssignment"]


class ResourceFeatureAssignment(BaseModel):
    created_utc: datetime = FieldInfo(alias="CreatedUtc")
    """Creation date and time of the assignment in UTC timezone in ISO 8601 format."""

    feature_id: str = FieldInfo(alias="FeatureId")
    """
    Unique identifier of the
    [Resource feature](https://mews-systems.gitbook.io/connector-api/operations/#resource-feature)
    assigned to the Resource.
    """

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the assignment."""

    is_active: bool = FieldInfo(alias="IsActive")
    """Whether the assignment is still active."""

    resource_id: str = FieldInfo(alias="ResourceId")
    """
    Unique identifier of the
    [Resource](https://mews-systems.gitbook.io/connector-api/operations/resources/#resource).
    """

    updated_utc: datetime = FieldInfo(alias="UpdatedUtc")
    """Last update date and time of the assignment in UTC timezone in ISO 8601 format."""


class V1ListResourceFeatureAssignmentsResponse(BaseModel):
    resource_feature_assignments: List[ResourceFeatureAssignment] = FieldInfo(alias="ResourceFeatureAssignments")
    """Resource feature assignments."""

    cursor: Optional[str] = FieldInfo(alias="Cursor", default=None)
    """
    Unique identifier of the last and hence oldest resource feature assignments
    returned. This can be used in
    [Limitation](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/#limitation)
    in a subsequent request to fetch the next batch of older resource feature
    assignments.
    """
