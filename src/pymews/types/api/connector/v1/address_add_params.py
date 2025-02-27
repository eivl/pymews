# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["AddressAddParams", "Address"]


class AddressAddParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    addresses: Required[Annotated[Iterable[Address], PropertyInfo(alias="Addresses")]]
    """Collection of addresses to be created."""

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


class Address(TypedDict, total=False):
    account_id: Required[Annotated[str, PropertyInfo(alias="AccountId")]]
    """Unique identifier of a Company or a Customer within the enterprise."""

    city: Annotated[Optional[str], PropertyInfo(alias="City")]
    """The city."""

    country_code: Annotated[Optional[str], PropertyInfo(alias="CountryCode")]
    """ISO 3166-1 alpha-2 code of the Country."""

    country_subdivision_code: Annotated[Optional[str], PropertyInfo(alias="CountrySubdivisionCode")]
    """ISO 3166-2 code of the administrative division, e.g. `DE-BW`."""

    latitude: Annotated[Optional[float], PropertyInfo(alias="Latitude")]
    """The latitude in range of -90 to 90."""

    line1: Annotated[Optional[str], PropertyInfo(alias="Line1")]
    """First line of the address."""

    line2: Annotated[Optional[str], PropertyInfo(alias="Line2")]
    """Second line of the address."""

    longitude: Annotated[Optional[float], PropertyInfo(alias="Longitude")]
    """The longitude in range of -180 to 180."""

    postal_code: Annotated[Optional[str], PropertyInfo(alias="PostalCode")]
    """Postal code."""
