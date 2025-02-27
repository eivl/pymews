# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["V1GetAllSourceAssignmentsResponse", "SourceAssignment"]


class SourceAssignment(BaseModel):
    id: str = FieldInfo(alias="Id")
    """Unique identifier of the source assignement."""

    is_primary: bool = FieldInfo(alias="IsPrimary")
    """
    Specifies the primary source for the
    [Reservation group](https://mews-systems.gitbook.io/connector-api/operations/reservations/#reservation-group).
    """

    reservation_group_id: str = FieldInfo(alias="ReservationGroupId")
    """
    Unique identifier of the
    [Reservation group](https://mews-systems.gitbook.io/connector-api/operations/reservations/#reservation-group).
    """

    source_id: str = FieldInfo(alias="SourceId")
    """
    Unique identifier of the
    [Source](https://mews-systems.gitbook.io/connector-api/operations/sources/#source).
    """


class V1GetAllSourceAssignmentsResponse(BaseModel):
    cursor: str = FieldInfo(alias="Cursor")
    """Unique identifier of the last and hence oldest source assignment returned.

    This can be used in `Limitation` in a subsequent request to fetch the next batch
    of older source assignments.
    """

    source_assignments: List[SourceAssignment] = FieldInfo(alias="SourceAssignments")
    """Assignments between reservation group and sources."""
