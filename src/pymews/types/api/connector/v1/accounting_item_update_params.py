# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = [
    "AccountingItemUpdateParams",
    "AccountingItemUpdate",
    "AccountingItemUpdateBillID",
    "AccountingItemUpdateAccountID",
]


class AccountingItemUpdateParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    accounting_item_updates: Required[
        Annotated[Iterable[AccountingItemUpdate], PropertyInfo(alias="AccountingItemUpdates")]
    ]
    """List of requested updates."""

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


class AccountingItemUpdateBillID(TypedDict, total=False):
    value: Annotated[str, PropertyInfo(alias="Value")]


class AccountingItemUpdateAccountID(TypedDict, total=False):
    value: Annotated[str, PropertyInfo(alias="Value")]


class AccountingItemUpdate(TypedDict, total=False):
    accounting_item_id: Required[Annotated[str, PropertyInfo(alias="AccountingItemId")]]

    bill_id: Required[Annotated[AccountingItemUpdateBillID, PropertyInfo(alias="BillId")]]

    account_id: Annotated[Optional[AccountingItemUpdateAccountID], PropertyInfo(alias="AccountId")]
