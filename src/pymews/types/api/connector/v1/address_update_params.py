# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = [
    "AddressUpdateParams",
    "AddressUpdate",
    "AddressUpdateCity",
    "AddressUpdateCountryCode",
    "AddressUpdateCountrySubdivisionCode",
    "AddressUpdateLine1",
    "AddressUpdateLine2",
    "AddressUpdatePostalCode",
]


class AddressUpdateParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    address_updates: Required[Annotated[Iterable[AddressUpdate], PropertyInfo(alias="AddressUpdates")]]
    """Collection of addresses to be updated."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    chain_id: Annotated[Optional[str], PropertyInfo(alias="ChainId")]
    """Unique identifier of the chain.

    Required when using
    [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
    ignored otherwise.
    """


class AddressUpdateCity(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AddressUpdateCountryCode(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AddressUpdateCountrySubdivisionCode(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AddressUpdateLine1(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AddressUpdateLine2(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AddressUpdatePostalCode(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AddressUpdate(TypedDict, total=False):
    address_id: Required[Annotated[str, PropertyInfo(alias="AddressId")]]
    """Unique identifier of the address."""

    city: Annotated[Optional[AddressUpdateCity], PropertyInfo(alias="City")]
    """The city."""

    country_code: Annotated[Optional[AddressUpdateCountryCode], PropertyInfo(alias="CountryCode")]
    """ISO 3166-1 alpha-2 code of the Country."""

    country_subdivision_code: Annotated[
        Optional[AddressUpdateCountrySubdivisionCode], PropertyInfo(alias="CountrySubdivisionCode")
    ]
    """ISO 3166-2 code of the administrative division, e.g. `DE-BW`."""

    line1: Annotated[Optional[AddressUpdateLine1], PropertyInfo(alias="Line1")]
    """First line of the address."""

    line2: Annotated[Optional[AddressUpdateLine2], PropertyInfo(alias="Line2")]
    """Second line of the address."""

    postal_code: Annotated[Optional[AddressUpdatePostalCode], PropertyInfo(alias="PostalCode")]
    """Postal code."""
