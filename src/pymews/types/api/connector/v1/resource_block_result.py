# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["ResourceBlockResult", "ResourceBlock"]


class ResourceBlock(BaseModel):
    assigned_resource_id: str = FieldInfo(alias="AssignedResourceId")
    """
    Unique identifier of the assigned
    [Resource](https://mews-systems.gitbook.io/connector-api/operations/resources/#resource).
    """

    created_utc: str = FieldInfo(alias="CreatedUtc")
    """Creation date and time of the block in UTC timezone in ISO 8601 format."""

    end_utc: str = FieldInfo(alias="EndUtc")
    """End of the block in UTC timezone in ISO 8601 format."""

    enterprise_id: str = FieldInfo(alias="EnterpriseId")

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the block."""

    is_active: bool = FieldInfo(alias="IsActive")
    """Whether the block is still active."""

    name: str = FieldInfo(alias="Name")
    """Name of the resource block."""

    start_utc: str = FieldInfo(alias="StartUtc")
    """Start of the block in UTC timezone in ISO 8601 format."""

    type: Literal["OutOfOrder", "InternalUse"] = FieldInfo(alias="Type")

    updated_utc: str = FieldInfo(alias="UpdatedUtc")
    """Last update date and time of the block in UTC timezone in ISO 8601 format."""

    notes: Optional[str] = FieldInfo(alias="Notes", default=None)
    """Note describing the resource block."""


class ResourceBlockResult(BaseModel):
    resource_blocks: List[ResourceBlock] = FieldInfo(alias="ResourceBlocks")
    """Resource blocks added."""

    cursor: Optional[str] = FieldInfo(alias="Cursor", default=None)
