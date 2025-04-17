# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = [
    "RestrictionListResponse",
    "Restriction",
    "RestrictionConditions",
    "RestrictionConditionsHours",
    "RestrictionExceptions",
    "RestrictionExceptionsMaxPrice",
    "RestrictionExceptionsMinPrice",
]


class RestrictionConditionsHours(BaseModel):
    eight: bool = FieldInfo(alias="Eight")
    """Hour 8 enabled"""

    eighteen: bool = FieldInfo(alias="Eighteen")
    """Hour 18 enabled"""

    eleven: bool = FieldInfo(alias="Eleven")
    """Hour 11 enabled"""

    fifteen: bool = FieldInfo(alias="Fifteen")
    """Hour 15 enabled"""

    five: bool = FieldInfo(alias="Five")
    """Hour 5 enabled"""

    four: bool = FieldInfo(alias="Four")
    """Hour 4 enabled"""

    fourteen: bool = FieldInfo(alias="Fourteen")
    """Hour 14 enabled"""

    nine: bool = FieldInfo(alias="Nine")
    """Hour 9 enabled"""

    nineteen: bool = FieldInfo(alias="Nineteen")
    """Hour 19 enabled"""

    one: bool = FieldInfo(alias="One")
    """Hour 1 enabled"""

    seven: bool = FieldInfo(alias="Seven")
    """Hour 7 enabled"""

    seventeen: bool = FieldInfo(alias="Seventeen")
    """Hour 17 enabled"""

    six: bool = FieldInfo(alias="Six")
    """Hour 6 enabled"""

    sixteen: bool = FieldInfo(alias="Sixteen")
    """Hour 16 enabled"""

    ten: bool = FieldInfo(alias="Ten")
    """Hour 10 enabled"""

    thirteen: bool = FieldInfo(alias="Thirteen")
    """Hour 13 enabled"""

    three: bool = FieldInfo(alias="Three")
    """Hour 3 enabled"""

    twelve: bool = FieldInfo(alias="Twelve")
    """Hour 12 enabled"""

    twenty: bool = FieldInfo(alias="Twenty")
    """Hour 20 enabled"""

    twenty_one: bool = FieldInfo(alias="TwentyOne")
    """Hour 21 enabled"""

    twenty_three: bool = FieldInfo(alias="TwentyThree")
    """Hour 23 enabled"""

    twenty_two: bool = FieldInfo(alias="TwentyTwo")
    """Hour 22 enabled"""

    two: bool = FieldInfo(alias="Two")
    """Hour 2 enabled"""

    zero: bool = FieldInfo(alias="Zero")
    """Hour 0 enabled"""


class RestrictionConditions(BaseModel):
    type: Literal["Stay", "Start", "End"] = FieldInfo(alias="Type")
    """Stay (Guests can't stay within specified dates.)

    Start (Guests can't check in within specified dates.)

    End (Guests can't check out within specified dates.)

    - `Stay` - Guests can't stay within specified dates.
    - `Start` - Guests can't check in within specified dates.
    - `End` - Guests can't check out within specified dates.
    """

    base_rate_id: Optional[str] = FieldInfo(alias="BaseRateId", default=None)
    """Unique identifier of the restricted base `Rate`."""

    days: Optional[List[str]] = FieldInfo(alias="Days", default=None)
    """The restricted days of week.

    Defaults to all days when not provided. Ignored when the service uses a time
    unit longer than a day.
    """

    end_utc: Optional[str] = FieldInfo(alias="EndUtc", default=None)
    """
    End date of the restriction time interval, specified in ISO 8601 format and
    adjusted to UTC - see
    [Datetimes](https://mews-systems.gitbook.io/connector-api/guidelines/serialization#datetimes)
    for important information on format and implementation.
    """

    exact_rate_id: Optional[str] = FieldInfo(alias="ExactRateId", default=None)
    """Unique identifier of the restricted exact `Rate`."""

    hours: Optional[RestrictionConditionsHours] = FieldInfo(alias="Hours", default=None)
    """The restricted hours. Defaults to all hours when not provided."""

    rate_group_id: Optional[str] = FieldInfo(alias="RateGroupId", default=None)
    """Unique identifier of the restricted `Rate group`."""

    resource_category_id: Optional[str] = FieldInfo(alias="ResourceCategoryId", default=None)
    """Unique identifier of the restricted `Resource category`."""

    resource_category_type: Optional[
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
    ] = FieldInfo(alias="ResourceCategoryType", default=None)
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

    start_utc: Optional[str] = FieldInfo(alias="StartUtc", default=None)
    """
    Start date of the restriction time interval, specified in ISO 8601 format and
    adjusted to UTC - see
    [Datetimes](https://mews-systems.gitbook.io/connector-api/guidelines/serialization#datetimes)
    for important information on format and implementation.
    """


class RestrictionExceptionsMaxPrice(BaseModel):
    currency: str = FieldInfo(alias="Currency")

    net: Optional[float] = FieldInfo(alias="Net", default=None)

    tax: Optional[float] = FieldInfo(alias="Tax", default=None)

    tax_rate: Optional[float] = FieldInfo(alias="TaxRate", default=None)

    value: Optional[float] = FieldInfo(alias="Value", default=None)


class RestrictionExceptionsMinPrice(BaseModel):
    currency: str = FieldInfo(alias="Currency")

    net: Optional[float] = FieldInfo(alias="Net", default=None)

    tax: Optional[float] = FieldInfo(alias="Tax", default=None)

    tax_rate: Optional[float] = FieldInfo(alias="TaxRate", default=None)

    value: Optional[float] = FieldInfo(alias="Value", default=None)


class RestrictionExceptions(BaseModel):
    max_advance: Optional[str] = FieldInfo(alias="MaxAdvance", default=None)
    """
    The maximum time before the reservation starts, you can reserve in ISO 8601
    duration format.
    """

    max_length: Optional[str] = FieldInfo(alias="MaxLength", default=None)
    """Maximal reservation length in ISO 8601 duration format."""

    max_price: Optional[RestrictionExceptionsMaxPrice] = FieldInfo(alias="MaxPrice", default=None)
    """Total price of the reservation."""

    min_advance: Optional[str] = FieldInfo(alias="MinAdvance", default=None)
    """
    The minimum time before the reservation starts, you can reserve in ISO 8601
    duration format.
    """

    min_length: Optional[str] = FieldInfo(alias="MinLength", default=None)
    """Minimal reservation length in ISO 8601 duration format."""

    min_price: Optional[RestrictionExceptionsMinPrice] = FieldInfo(alias="MinPrice", default=None)
    """Total price of the reservation."""


class Restriction(BaseModel):
    conditions: RestrictionConditions = FieldInfo(alias="Conditions")
    """
    The conditions or rules that must be met by a reservation for the restriction to
    apply.
    """

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the restriction."""

    origin: Literal["User", "Integration"] = FieldInfo(alias="Origin")
    """User (Restriction was created by a user in Mews.)

    Integration (Restriction was created by a 3rd-party integration.)

    - `User` - Restriction was created by a user in Mews.
    - `Integration` - Restriction was created by a 3rd-party integration.
    """

    service_id: str = FieldInfo(alias="ServiceId")
    """Unique identifier of the `Service`."""

    exceptions: Optional[RestrictionExceptions] = FieldInfo(alias="Exceptions", default=None)
    """
    The rules that prevent the restriction from applying to a reservation, even when
    all conditions have been met.
    """

    external_identifier: Optional[str] = FieldInfo(alias="ExternalIdentifier", default=None)
    """External identifier of the restriction."""


class RestrictionListResponse(BaseModel):
    restrictions: List[Restriction] = FieldInfo(alias="Restrictions")
    """Restrictions of the default service."""

    cursor: Optional[str] = FieldInfo(alias="Cursor", default=None)
    """
    Unique identifier of the item one newer in time order than the items to be
    returned. If Cursor is not specified, i.e. null, then the latest or most recent
    items will be returned.
    """
