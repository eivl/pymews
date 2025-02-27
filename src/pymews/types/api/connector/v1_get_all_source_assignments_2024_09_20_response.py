# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["V1GetAllSourceAssignments2024_09_20Response", "SourceAssignment"]


class SourceAssignment(BaseModel):
    id: str = FieldInfo(alias="Id")
    """Unique identifier of the source assignment."""

    is_primary: bool = FieldInfo(alias="IsPrimary")
    """Specifies whether the source is primary for the `Reservation`."""

    reservation_id: str = FieldInfo(alias="ReservationId")
    """Unique identifier of the `Reservation`."""

    source_id: str = FieldInfo(alias="SourceId")
    """Unique identifier of the `Source`."""


class V1GetAllSourceAssignments2024_09_20Response(BaseModel):
    source_assignments: List[SourceAssignment] = FieldInfo(alias="SourceAssignments")
    """Assignments between `Reservation` and `Source`."""

    cursor: Optional[str] = FieldInfo(alias="Cursor", default=None)
    """
    Opaque pagination cursor which can be used in `Limitation` to fetch newer source
    assignments.
    """
