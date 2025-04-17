# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["ReservationAddProductParams", "UnitAmount"]


class ReservationAddProductParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    count: Required[Annotated[int, PropertyInfo(alias="Count")]]
    """The amount of the products to be added.

    Note that if the product is charged e.g. per night, count 1 means a single
    product every night. Count 2 means two products every night.
    """

    product_id: Required[Annotated[str, PropertyInfo(alias="ProductId")]]
    """
    Unique identifier of the
    [Product](https://mews-systems.gitbook.io/connector-api/operations/products/#product).
    """

    reservation_id: Required[Annotated[str, PropertyInfo(alias="ReservationId")]]
    """Unique identifier of the reservation."""

    end_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="EndUtc", format="iso8601")]
    """Product end in UTC timezone in ISO 8601 format.

    For products with charging Once and PerPerson must be set to same value as
    StartUtc.
    """

    start_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="StartUtc", format="iso8601")]
    """Product start in UTC timezone in ISO 8601 format.

    For products with charging Once and PerPerson must be set to same value as
    EndUtc.
    """

    unit_amount: Annotated[Optional[UnitAmount], PropertyInfo(alias="UnitAmount")]
    """Price of the product that overrides the price defined in Mews."""


class UnitAmount(TypedDict, total=False):
    currency: Required[Annotated[str, PropertyInfo(alias="Currency")]]

    tax_codes: Required[Annotated[List[str], PropertyInfo(alias="TaxCodes")]]

    gross_value: Annotated[Optional[float], PropertyInfo(alias="GrossValue")]

    net_value: Annotated[Optional[float], PropertyInfo(alias="NetValue")]
