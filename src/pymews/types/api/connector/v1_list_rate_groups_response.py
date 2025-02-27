# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["V1ListRateGroupsResponse", "RateGroup"]


class RateGroup(BaseModel):
    created_utc: datetime = FieldInfo(alias="CreatedUtc")
    """Creation date and time of the rate group in UTC timezone in ISO 8601 format."""

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the rate group."""

    is_active: bool = FieldInfo(alias="IsActive")
    """Whether the rate group is still active."""

    names: Dict[str, str] = FieldInfo(alias="Names")
    """All translations of the name."""

    ordering: int = FieldInfo(alias="Ordering")
    """Ordering of the rate group."""

    service_id: str = FieldInfo(alias="ServiceId")
    """
    Unique identifier of the
    [Service](https://mews-systems.gitbook.io/connector-api/operations/services/#service)
    the rate group belongs to.
    """

    updated_utc: datetime = FieldInfo(alias="UpdatedUtc")
    """Last update date and time of the rate group in UTC timezone in ISO 8601 format."""

    descriptions: Optional[Dict[str, str]] = FieldInfo(alias="Descriptions", default=None)
    """All translations of the description."""

    external_identifier: Optional[str] = FieldInfo(alias="ExternalIdentifier", default=None)
    """Identifier of the rate group from external system."""

    short_names: Optional[Dict[str, str]] = FieldInfo(alias="ShortNames", default=None)
    """All translations of the short name."""


class V1ListRateGroupsResponse(BaseModel):
    rate_groups: List[RateGroup] = FieldInfo(alias="RateGroups")
    """The filtered rate groups."""

    cursor: Optional[str] = FieldInfo(alias="Cursor", default=None)
    """Unique identifier of the last and hence oldest rate group returned.

    This can be used in
    [Limitation](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/#limitation)
    in a subsequent request to fetch the next batch of older rate groups.
    """
