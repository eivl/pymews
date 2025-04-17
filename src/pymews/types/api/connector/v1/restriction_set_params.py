# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["RestrictionSetParams", "Data", "DataDays", "DataMaxPrice", "DataMinPrice"]


class RestrictionSetParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    data: Required[Annotated[Iterable[Data], PropertyInfo(alias="Data")]]
    """Parameters of restrictions."""

    service_id: Required[Annotated[str, PropertyInfo(alias="ServiceId")]]
    """
    Unique identifier of the
    [Service](https://mews-systems.gitbook.io/connector-api/operations/services#service)
    restrictions will be set in.
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


class DataMaxPrice(TypedDict, total=False):
    currency: Required[Annotated[str, PropertyInfo(alias="Currency")]]

    value: Required[Annotated[float, PropertyInfo(alias="Value")]]


class DataMinPrice(TypedDict, total=False):
    currency: Required[Annotated[str, PropertyInfo(alias="Currency")]]

    value: Required[Annotated[float, PropertyInfo(alias="Value")]]


class Data(TypedDict, total=False):
    days: Required[Annotated[DataDays, PropertyInfo(alias="Days")]]
    """The restricted days of week."""

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

    max_advance: Annotated[Union[str, datetime, None], PropertyInfo(alias="MaxAdvance", format="iso8601")]
    """
    The maximum time before the reservation starts, you can reserve in ISO 8601
    duration format.
    """

    max_length: Annotated[Union[str, datetime, None], PropertyInfo(alias="MaxLength", format="iso8601")]
    """Maximal reservation length in ISO 8601 duration format."""

    max_price: Annotated[Optional[DataMaxPrice], PropertyInfo(alias="MaxPrice")]
    """Absolute value of the fee."""

    min_advance: Annotated[Union[str, datetime, None], PropertyInfo(alias="MinAdvance", format="iso8601")]
    """
    The minimum time before the reservation starts, you can reserve in ISO 8601
    duration format.
    """

    min_length: Annotated[Union[str, datetime, None], PropertyInfo(alias="MinLength", format="iso8601")]
    """Minimal reservation length in ISO 8601 duration format."""

    min_price: Annotated[Optional[DataMinPrice], PropertyInfo(alias="MinPrice")]
    """Absolute value of the fee."""

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
