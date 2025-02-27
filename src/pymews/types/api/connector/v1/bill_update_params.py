# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["BillUpdateParams", "BillsUpdate", "BillsUpdateAccountID", "BillsUpdateAssociatedAccountIDs"]


class BillUpdateParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    bills_updates: Required[Annotated[Iterable[BillsUpdate], PropertyInfo(alias="BillsUpdates")]]
    """Information about bills to be updated."""

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


class BillsUpdateAccountID(TypedDict, total=False):
    value: Annotated[str, PropertyInfo(alias="Value")]


class BillsUpdateAssociatedAccountIDs(TypedDict, total=False):
    value: Annotated[Optional[List[str]], PropertyInfo(alias="Value")]
    """
    Unique identifiers of the `Customer` or `Company` that are associated to the
    bill. Set to `null` to remove all associated accounts. Note that only single
    associated account is currently supported.
    """


class BillsUpdate(TypedDict, total=False):
    bill_id: Required[Annotated[str, PropertyInfo(alias="BillId")]]
    """Unique identifier of the bill to update."""

    account_id: Annotated[Optional[BillsUpdateAccountID], PropertyInfo(alias="AccountId")]
    """
    Unique identifier of the account (`Customer` or `Company`) the bill is issued to
    (or null if the account should not be updated).
    """

    associated_account_ids: Annotated[
        Optional[BillsUpdateAssociatedAccountIDs], PropertyInfo(alias="AssociatedAccountIds")
    ]
    """
    Has same structure as
    [Array of strings update value](https://mews-systems.gitbook.io/connector-api/operations/_objects#array-of-strings-update-value).
    """
