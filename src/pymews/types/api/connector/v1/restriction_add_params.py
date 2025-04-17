# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = [
    "RestrictionAddParams",
    "Restriction",
    "RestrictionConditions",
    "RestrictionConditionsHours",
    "RestrictionExceptions",
    "RestrictionExceptionsMaxPrice",
    "RestrictionExceptionsMinPrice",
]


class RestrictionAddParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    restrictions: Required[Annotated[Iterable[Restriction], PropertyInfo(alias="Restrictions")]]
    """Parameters of restrictions."""

    service_id: Required[Annotated[str, PropertyInfo(alias="ServiceId")]]
    """
    Unique identifier of the
    [Service](https://mews-systems.gitbook.io/connector-api/operations/services/#service)
    restrictions will be added in.
    """


class RestrictionConditionsHours(TypedDict, total=False):
    eight: Required[Annotated[bool, PropertyInfo(alias="Eight")]]
    """Hour 8 enabled"""

    eighteen: Required[Annotated[bool, PropertyInfo(alias="Eighteen")]]
    """Hour 18 enabled"""

    eleven: Required[Annotated[bool, PropertyInfo(alias="Eleven")]]
    """Hour 11 enabled"""

    fifteen: Required[Annotated[bool, PropertyInfo(alias="Fifteen")]]
    """Hour 15 enabled"""

    five: Required[Annotated[bool, PropertyInfo(alias="Five")]]
    """Hour 5 enabled"""

    four: Required[Annotated[bool, PropertyInfo(alias="Four")]]
    """Hour 4 enabled"""

    fourteen: Required[Annotated[bool, PropertyInfo(alias="Fourteen")]]
    """Hour 14 enabled"""

    nine: Required[Annotated[bool, PropertyInfo(alias="Nine")]]
    """Hour 9 enabled"""

    nineteen: Required[Annotated[bool, PropertyInfo(alias="Nineteen")]]
    """Hour 19 enabled"""

    one: Required[Annotated[bool, PropertyInfo(alias="One")]]
    """Hour 1 enabled"""

    seven: Required[Annotated[bool, PropertyInfo(alias="Seven")]]
    """Hour 7 enabled"""

    seventeen: Required[Annotated[bool, PropertyInfo(alias="Seventeen")]]
    """Hour 17 enabled"""

    six: Required[Annotated[bool, PropertyInfo(alias="Six")]]
    """Hour 6 enabled"""

    sixteen: Required[Annotated[bool, PropertyInfo(alias="Sixteen")]]
    """Hour 16 enabled"""

    ten: Required[Annotated[bool, PropertyInfo(alias="Ten")]]
    """Hour 10 enabled"""

    thirteen: Required[Annotated[bool, PropertyInfo(alias="Thirteen")]]
    """Hour 13 enabled"""

    three: Required[Annotated[bool, PropertyInfo(alias="Three")]]
    """Hour 3 enabled"""

    twelve: Required[Annotated[bool, PropertyInfo(alias="Twelve")]]
    """Hour 12 enabled"""

    twenty: Required[Annotated[bool, PropertyInfo(alias="Twenty")]]
    """Hour 20 enabled"""

    twenty_one: Required[Annotated[bool, PropertyInfo(alias="TwentyOne")]]
    """Hour 21 enabled"""

    twenty_three: Required[Annotated[bool, PropertyInfo(alias="TwentyThree")]]
    """Hour 23 enabled"""

    twenty_two: Required[Annotated[bool, PropertyInfo(alias="TwentyTwo")]]
    """Hour 22 enabled"""

    two: Required[Annotated[bool, PropertyInfo(alias="Two")]]
    """Hour 2 enabled"""

    zero: Required[Annotated[bool, PropertyInfo(alias="Zero")]]
    """Hour 0 enabled"""


class RestrictionConditions(TypedDict, total=False):
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

    days: Annotated[Optional[List[str]], PropertyInfo(alias="Days")]
    """The restricted days of week.

    Defaults to all days when not provided. Ignored when the service uses a time
    unit longer than a day.
    """

    end_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="EndUtc", format="iso8601")]
    """
    End date of the time interval for which the restriction conditions should be
    applied. This must be in UTC timezone in ISO 8601 format - see
    [Datetimes](https://mews-systems.gitbook.io/connector-api/guidelines/serialization#datetimes).
    """

    exact_rate_id: Annotated[Optional[str], PropertyInfo(alias="ExactRateId")]
    """Unique identifier of the exact `Rate` to which the restriction applies."""

    hours: Annotated[Optional[RestrictionConditionsHours], PropertyInfo(alias="Hours")]
    """The restricted hours. Defaults to all hours when not provided."""

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


class RestrictionExceptionsMaxPrice(TypedDict, total=False):
    currency: Required[Annotated[str, PropertyInfo(alias="Currency")]]

    net: Annotated[Optional[float], PropertyInfo(alias="Net")]

    tax: Annotated[Optional[float], PropertyInfo(alias="Tax")]

    tax_rate: Annotated[Optional[float], PropertyInfo(alias="TaxRate")]

    value: Annotated[Optional[float], PropertyInfo(alias="Value")]


class RestrictionExceptionsMinPrice(TypedDict, total=False):
    currency: Required[Annotated[str, PropertyInfo(alias="Currency")]]

    net: Annotated[Optional[float], PropertyInfo(alias="Net")]

    tax: Annotated[Optional[float], PropertyInfo(alias="Tax")]

    tax_rate: Annotated[Optional[float], PropertyInfo(alias="TaxRate")]

    value: Annotated[Optional[float], PropertyInfo(alias="Value")]


class RestrictionExceptions(TypedDict, total=False):
    max_advance: Annotated[Union[str, datetime, None], PropertyInfo(alias="MaxAdvance", format="iso8601")]
    """
    The maximum time before the reservation starts, you can reserve in ISO 8601
    duration format.
    """

    max_length: Annotated[Union[str, datetime, None], PropertyInfo(alias="MaxLength", format="iso8601")]
    """Maximal reservation length in ISO 8601 duration format."""

    max_price: Annotated[Optional[RestrictionExceptionsMaxPrice], PropertyInfo(alias="MaxPrice")]
    """Total price of the reservation."""

    min_advance: Annotated[Union[str, datetime, None], PropertyInfo(alias="MinAdvance", format="iso8601")]
    """
    The minimum time before the reservation starts, you can reserve in ISO 8601
    duration format.
    """

    min_length: Annotated[Union[str, datetime, None], PropertyInfo(alias="MinLength", format="iso8601")]
    """Minimal reservation length in ISO 8601 duration format."""

    min_price: Annotated[Optional[RestrictionExceptionsMinPrice], PropertyInfo(alias="MinPrice")]
    """Total price of the reservation."""


class Restriction(TypedDict, total=False):
    conditions: Required[Annotated[RestrictionConditions, PropertyInfo(alias="Conditions")]]
    """
    The conditions or rules that must be met by a reservation for the restriction to
    apply.
    """

    exceptions: Annotated[Optional[RestrictionExceptions], PropertyInfo(alias="Exceptions")]
    """
    The rules that prevent the restriction from applying to a reservation, even when
    all conditions have been met.
    """

    external_identifier: Annotated[Optional[str], PropertyInfo(alias="ExternalIdentifier")]
    """External identifier of the restriction."""

    identifier: Annotated[Optional[str], PropertyInfo(alias="Identifier")]
    """Identifier of the restriction within the transaction."""
