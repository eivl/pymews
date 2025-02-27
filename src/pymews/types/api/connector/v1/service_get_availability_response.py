# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["ServiceGetAvailabilityResponse", "CategoryAvailability"]


class CategoryAvailability(BaseModel):
    adjustments: List[int] = FieldInfo(alias="Adjustments")
    """
    Relative availability adjustments set for resource category in the covered
    dates.
    """

    availabilities: List[int] = FieldInfo(alias="Availabilities")
    """Absolute availabilities of the resource category in the covered dates."""

    category_id: str = FieldInfo(alias="CategoryId")
    """
    Unique identifier of the
    [Resource category](https://mews-systems.gitbook.io/connector-api/operations/resources#resource-category).
    """


class ServiceGetAvailabilityResponse(BaseModel):
    category_availabilities: List[CategoryAvailability] = FieldInfo(alias="CategoryAvailabilities")
    """Resource category availabilities."""

    time_unit_starts_utc: List[str] = FieldInfo(alias="TimeUnitStartsUtc")
    """
    Set of all time units covered by the time interval; expressed in UTC timezone
    ISO 8601 format.
    """

    dates_utc: Optional[List[str]] = FieldInfo(alias="DatesUtc", default=None)
