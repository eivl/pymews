# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["V1ListLedgerBalancesParams", "Date", "Limitation"]


class V1ListLedgerBalancesParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    date: Required[Annotated[Date, PropertyInfo(alias="Date")]]
    """Date interval over which the ledger balances are created."""

    ledger_types: Required[
        Annotated[
            List[Literal["Revenue", "Tax", "Payment", "Deposit", "Guest", "City"]], PropertyInfo(alias="LedgerTypes")
        ]
    ]
    """Accounting ledger types to which ledger balances belong."""

    limitation: Required[Annotated[Limitation, PropertyInfo(alias="Limitation")]]
    """Limitation on the quantity of data returned."""

    enterprise_ids: Annotated[Optional[List[str]], PropertyInfo(alias="EnterpriseIds")]
    """Unique identifiers of the Enterprises.

    If not specified, the operation returns data for all enterprises within scope of
    the Access Token.
    """


class Date(TypedDict, total=False):
    end: Required[Annotated[Union[str, date], PropertyInfo(alias="End", format="iso8601")]]

    start: Required[Annotated[Union[str, date], PropertyInfo(alias="Start", format="iso8601")]]


class Limitation(TypedDict, total=False):
    count: Required[Annotated[int, PropertyInfo(alias="Count")]]

    cursor: Annotated[Optional[str], PropertyInfo(alias="Cursor")]
