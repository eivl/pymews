# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["BillAddParams", "Bill"]


class BillAddParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    bills: Required[Annotated[Iterable[Bill], PropertyInfo(alias="Bills")]]
    """Information about bills to be created."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    enterprise_id: Annotated[Optional[str], PropertyInfo(alias="EnterpriseId")]
    """Unique identifier of the enterprise.

    Required when using
    [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
    ignored otherwise.
    """


class Bill(TypedDict, total=False):
    account_id: Required[Annotated[str, PropertyInfo(alias="AccountId")]]
    """Unique identifier of the account (`Customer` or `Company`) the bill is issued
    to.

    Company billing may not be enabled for your integration.
    """

    associated_account_id: Annotated[Optional[str], PropertyInfo(alias="AssociatedAccountId")]
    """Account that has a possible link with the owner of the bill."""

    name: Annotated[Optional[str], PropertyInfo(alias="Name")]
    """Name of the newly created bill."""
