# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["V1ListSourcesResponse", "Source"]


class Source(BaseModel):
    code: int = FieldInfo(alias="Code")
    """Code of the source."""

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the source."""

    name: str = FieldInfo(alias="Name")
    """Name of the source."""

    type: Literal[
        "OnlineTravelAgency",
        "CentralReservationSystem",
        "GlobalDistributionSystem",
        "AlternativeDistributionSystem",
        "SalesAndCateringSystem",
        "PropertyManagementSystem",
        "TourOperatorSystem",
        "OnlineBookingEngine",
        "Kiosk",
        "Agent",
    ] = FieldInfo(alias="Type")
    """Type of the source."""

    updated_utc: datetime = FieldInfo(alias="UpdatedUtc")
    """
    Date and time when the source was last updated, expressed in UTC timezone in ISO
    8601 format.
    """


class V1ListSourcesResponse(BaseModel):
    sources: List[Source] = FieldInfo(alias="Sources")
    """The reservation sources."""

    cursor: Optional[str] = FieldInfo(alias="Cursor", default=None)
    """Unique identifier of the last and hence oldest source returned.

    This can be used in
    [Limitation](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/#limitation)
    in a subsequent request to fetch the next batch of older sources.
    """
