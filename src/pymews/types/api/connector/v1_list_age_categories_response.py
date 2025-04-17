# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["V1ListAgeCategoriesResponse", "AgeCategory"]


class AgeCategory(BaseModel):
    classification: Literal["Adult", "Child"] = FieldInfo(alias="Classification")
    """Adult

    Child
    """

    created_utc: datetime = FieldInfo(alias="CreatedUtc")
    """Creation date and time of the age category in UTC timezone in ISO 8601 format."""

    id: str = FieldInfo(alias="Id")
    """Unique identifier of age category."""

    is_active: bool = FieldInfo(alias="IsActive")
    """Whether the age category is still active."""

    names: Dict[str, str] = FieldInfo(alias="Names")
    """All translations of the name of the age category."""

    service_id: str = FieldInfo(alias="ServiceId")
    """
    Unique identifier of
    [Service](https://mews-systems.gitbook.io/connector-api/operations/services/#service)
    the age category belongs to.
    """

    updated_utc: datetime = FieldInfo(alias="UpdatedUtc")
    """
    Last update date and time of the age category in UTC timezone in ISO 8601
    format.
    """

    external_identifier: Optional[str] = FieldInfo(alias="ExternalIdentifier", default=None)
    """Identifier of the age category from external system."""

    maximal_age: Optional[int] = FieldInfo(alias="MaximalAge", default=None)
    """Maximal age for the age category."""

    minimal_age: Optional[int] = FieldInfo(alias="MinimalAge", default=None)
    """Minimal age for the age category."""

    short_names: Optional[Dict[str, str]] = FieldInfo(alias="ShortNames", default=None)
    """All translations of the short name of the age category."""


class V1ListAgeCategoriesResponse(BaseModel):
    age_categories: List[AgeCategory] = FieldInfo(alias="AgeCategories")
    """Age category of the enterprise."""

    cursor: Optional[str] = FieldInfo(alias="Cursor", default=None)
    """
    Unique identifier of the item one newer in time order than the items to be
    returned. If Cursor is not specified, i.e. null, then the latest or most recent
    items will be returned.
    """
