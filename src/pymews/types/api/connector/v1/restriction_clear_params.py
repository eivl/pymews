# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["RestrictionClearParams", "Data", "DataDays"]


class RestrictionClearParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    data: Required[Annotated[Iterable[Data], PropertyInfo(alias="Data")]]
    """
    Details of the matching conditions and time intervals for clearing restrictions.
    """

    service_id: Required[Annotated[str, PropertyInfo(alias="ServiceId")]]
    """
    Unique identifier of the
    [Service](https://mews-systems.gitbook.io/connector-api/operations/services#service)
    to which the restrictions apply.
    """


class DataDays(TypedDict, total=False):
    friday: Required[Annotated[bool, PropertyInfo(alias="Friday")]]
    """Friday enabled"""

    monday: Required[Annotated[bool, PropertyInfo(alias="Monday")]]
    """Monday enabled"""

    saturday: Required[Annotated[bool, PropertyInfo(alias="Saturday")]]
    """Saturday enabled"""

    sunday: Required[Annotated[bool, PropertyInfo(alias="Sunday")]]
    """Sunday enabled"""

    thursday: Required[Annotated[bool, PropertyInfo(alias="Thursday")]]
    """Thursday enabled"""

    tuesday: Required[Annotated[bool, PropertyInfo(alias="Tuesday")]]
    """Tuesday enabled"""

    wednesday: Required[Annotated[bool, PropertyInfo(alias="Wednesday")]]
    """Wednesday enabled"""


class Data(TypedDict, total=False):
    days: Required[Annotated[DataDays, PropertyInfo(alias="Days")]]
    """The days of week to which the restriction applies."""

    type: Required[Annotated[Literal["Stay", "Start", "End"], PropertyInfo(alias="Type")]]
    """Stay (Guests can't stay within specified dates.)

    Start (Guests can't check in within specified dates.)

    End (Guests can't check out within specified dates.)

    - `Stay` - Guests can't stay within specified dates.
    - `Start` - Guests can't check in within specified dates.
    - `End` - Guests can't check out within specified dates.
    """

    base_rate_id: Annotated[Optional[str], PropertyInfo(alias="BaseRateId")]
    """Unique identifier of the base `Rate` to which the restriction applies."""

    end_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="EndUtc", format="iso8601")]
    """
    End date of the time interval for which the restriction conditions should be
    applied. This must be in UTC timezone in ISO 8601 format - see
    [Datetimes](https://mews-systems.gitbook.io/connector-api/guidelines/serialization#datetimes).
    """

    exact_rate_id: Annotated[Optional[str], PropertyInfo(alias="ExactRateId")]
    """Unique identifier of the exact `Rate` to which the restriction applies."""

    rate_group_id: Annotated[Optional[str], PropertyInfo(alias="RateGroupId")]
    """Unique identifier of the `Rate group` to which the restriction applies."""

    resource_category_id: Annotated[Optional[str], PropertyInfo(alias="ResourceCategoryId")]
    """Unique identifier of the `Resource category` to which the restriction applies."""

    resource_category_type: Annotated[
        Optional[
            Literal[
                "Room",
                "Bed",
                "Dorm",
                "Apartment",
                "Suite",
                "Villa",
                "Site",
                "Office",
                "MeetingRoom",
                "ParkingSpot",
                "Desk",
                "TeamArea",
                "Membership",
                "Tent",
                "CaravanOrRV",
                "UnequippedCampsite",
                "Bike",
                "ExtraBed",
                "Cot",
                "Crib",
                "ConferenceRoom",
                "Rooftop",
                "Garden",
                "Restaurant",
                "Amphitheater",
                "PrivateSpaces",
            ]
        ],
        PropertyInfo(alias="ResourceCategoryType"),
    ]
    """Room

    Bed

    Dorm

    Apartment

    Suite

    Villa

    Site

    Office

    MeetingRoom

    ParkingSpot

    Desk

    TeamArea

    Membership

    Tent

    CaravanOrRV

    UnequippedCampsite

    Bike

    ExtraBed

    Cot

    Crib

    ConferenceRoom

    Rooftop

    Garden

    Restaurant

    Amphitheater

    PrivateSpaces
    """

    start_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="StartUtc", format="iso8601")]
    """
    Start date of the time interval for which the restriction conditions should be
    applied. This must be in UTC timezone in ISO 8601 format - see
    [Datetimes](https://mews-systems.gitbook.io/connector-api/guidelines/serialization#datetimes).
    """
