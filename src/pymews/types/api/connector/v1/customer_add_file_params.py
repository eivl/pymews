# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["CustomerAddFileParams"]


class CustomerAddFileParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    customer_id: Required[Annotated[str, PropertyInfo(alias="CustomerId")]]
    """
    Unique identifier of the
    [Customer](https://mews-systems.gitbook.io/connector-api/operations/#customer).
    """

    data: Required[Annotated[str, PropertyInfo(alias="Data")]]
    """Base64-encoded data of the file."""

    name: Required[Annotated[str, PropertyInfo(alias="Name")]]
    """Name of the file."""

    type: Required[Annotated[str, PropertyInfo(alias="Type")]]
    """MIME type of the file (e.g. `application/pdf`)."""

    chain_id: Annotated[Optional[str], PropertyInfo(alias="ChainId")]
    """Unique identifier of the chain.

    Required when using
    [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
    ignored otherwise.
    """
