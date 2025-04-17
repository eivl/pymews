# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["CustomerSearchParams", "Extent"]


class CustomerSearchParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    extent: Annotated[Optional[Extent], PropertyInfo(alias="Extent")]

    name: Annotated[Optional[str], PropertyInfo(alias="Name")]
    """Name to search by (applies to first name, last name, and full name)."""

    resource_id: Annotated[Optional[str], PropertyInfo(alias="ResourceId")]
    """
    Identifier of
    [Resource](https://mews-systems.gitbook.io/connector-api/operations/resources/#resource)
    to search by (members of reservation assigned there will be returned).
    """


class Extent(TypedDict, total=False):
    addresses: Annotated[Optional[bool], PropertyInfo(alias="Addresses")]
    """Whether the response should contain addresses of customers."""

    customers: Annotated[Optional[bool], PropertyInfo(alias="Customers")]
    """Whether the response should contain information about customers."""

    documents: Annotated[Optional[bool], PropertyInfo(alias="Documents")]
    """Whether the response should contain identity documents of customers."""
