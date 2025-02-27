# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["AccountAddFileParams"]


class AccountAddFileParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    account_id: Required[Annotated[str, PropertyInfo(alias="AccountId")]]
    """Unique identifier of the account to which the file will be uploaded to."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    data: Required[Annotated[str, PropertyInfo(alias="Data")]]
    """Uploaded file data serialized in base64 format."""

    name: Required[Annotated[str, PropertyInfo(alias="Name")]]
    """Uploaded file name."""

    type: Required[Annotated[str, PropertyInfo(alias="Type")]]
    """Content type of the uploaded file following defined by its MIME type."""

    chain_id: Annotated[Optional[str], PropertyInfo(alias="ChainId")]
    """Unique identifier of the chain.

    Required when using
    [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
    ignored otherwise.
    """
