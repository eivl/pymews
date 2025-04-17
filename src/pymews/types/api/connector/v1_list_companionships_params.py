# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["V1ListCompanionshipsParams", "Extent", "Limitation", "UpdatedUtc"]


class V1ListCompanionshipsParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    extent: Required[Annotated[Extent, PropertyInfo(alias="Extent")]]
    """Extent of data to be returned.

    E.g. it is possible to specify that together with the companionships, customers,
    reservations, and reservation groups should be also returned.
    """

    limitation: Required[Annotated[Limitation, PropertyInfo(alias="Limitation")]]
    """Limitation on the quantity of data returned."""

    companionship_ids: Annotated[Optional[List[str]], PropertyInfo(alias="CompanionshipIds")]
    """
    Unique identifiers of
    [Companionship](https://mews-systems.gitbook.io/connector-api/operations/#companionship).
    """

    customer_ids: Annotated[Optional[List[str]], PropertyInfo(alias="CustomerIds")]
    """
    Unique identifiers of
    [Customers](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer).
    """

    enterprise_ids: Annotated[Optional[List[str]], PropertyInfo(alias="EnterpriseIds")]
    """Unique identifiers of the Enterprises.

    If not specified, the operation returns data for all enterprises within scope of
    the Access Token.
    """

    reservation_group_ids: Annotated[Optional[List[str]], PropertyInfo(alias="ReservationGroupIds")]
    """
    Unique identifiers of
    [Reservation groups](https://mews-systems.gitbook.io/connector-api/operations/reservations/#reservation-group).
    """

    reservation_ids: Annotated[Optional[List[str]], PropertyInfo(alias="ReservationIds")]
    """Unique identifiers of reservations."""

    updated_utc: Annotated[Optional[UpdatedUtc], PropertyInfo(alias="UpdatedUtc")]


class Extent(TypedDict, total=False):
    customers: Annotated[bool, PropertyInfo(alias="Customers")]

    reservation_groups: Annotated[bool, PropertyInfo(alias="ReservationGroups")]

    reservations: Annotated[bool, PropertyInfo(alias="Reservations")]


class Limitation(TypedDict, total=False):
    count: Required[Annotated[int, PropertyInfo(alias="Count")]]

    cursor: Annotated[Optional[str], PropertyInfo(alias="Cursor")]


class UpdatedUtc(TypedDict, total=False):
    end_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="EndUtc", format="iso8601")]

    start_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="StartUtc", format="iso8601")]
