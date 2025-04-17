# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["ExportListResponse", "Export", "ExportFile"]


class ExportFile(BaseModel):
    size_in_bytes: int = FieldInfo(alias="SizeInBytes")
    """Total size of the exported file in bytes."""

    url: str = FieldInfo(alias="Url")
    """URL of the exported file for download in JSON Lines format."""


class Export(BaseModel):
    entity_type: Literal[
        "OrderItem",
        "Payment",
        "Reservation",
        "Customer",
        "Company",
        "Bill",
        "AvailabilityAdjustment",
        "AvailabilityBlock",
        "ResourceBlock",
    ] = FieldInfo(alias="EntityType")
    """Type of exported entities"""

    files: List[ExportFile] = FieldInfo(alias="Files")
    """Files with exported data. Empty if no files are available."""

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the export."""

    status: Literal["Pending", "Processing", "Success", "Failed", "Expired"] = FieldInfo(alias="Status")
    """Current status of the export."""

    expires_utc: Optional[datetime] = FieldInfo(alias="ExpiresUtc", default=None)
    """Expiration date and time of the export in UTC timezone in ISO 8601 format.

    After this time the Exported files may no longer be available for download.
    """


class ExportListResponse(BaseModel):
    exports: List[Export] = FieldInfo(alias="Exports")
    """Requested exports."""
