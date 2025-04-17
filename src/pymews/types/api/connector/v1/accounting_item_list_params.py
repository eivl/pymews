# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["AccountingItemListParams", "Extent", "ClosedUtc", "ConsumedUtc", "UpdatedUtc"]


class AccountingItemListParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    end_utc: Required[Annotated[Union[str, datetime], PropertyInfo(alias="EndUtc", format="iso8601")]]

    extent: Required[Annotated[Extent, PropertyInfo(alias="Extent")]]
    """Extent of data to be returned.

    E.g. it is possible to specify that together with the accounting items, credit
    card transactions should be also returned.
    """

    start_utc: Required[Annotated[Union[str, datetime], PropertyInfo(alias="StartUtc", format="iso8601")]]

    closed_utc: Annotated[Optional[ClosedUtc], PropertyInfo(alias="ClosedUtc")]

    consumed_utc: Annotated[Optional[ConsumedUtc], PropertyInfo(alias="ConsumedUtc")]

    currency: Annotated[Optional[str], PropertyInfo(alias="Currency")]
    """
    ISO-4217 code of the
    [Currency](https://mews-systems.gitbook.io/connector-api/operations/currencies/#currency)
    the item costs should be converted to.
    """

    item_ids: Annotated[Optional[List[str]], PropertyInfo(alias="ItemIds")]
    """Unique identifiers of the Accounting items.

    Required if no other filter is provided.
    """

    rebated_item_ids: Annotated[Optional[List[str]], PropertyInfo(alias="RebatedItemIds")]
    """Unique identifiers of the Accounting items we are finding rebates for.

    Required if no other filter is provided.
    """

    states: Annotated[Optional[List[str]], PropertyInfo(alias="States")]
    """States the accounting items should be in.

    If not specified, accounting items in Open or Closed states are returned.
    """

    time_filter: Annotated[Optional[str], PropertyInfo(alias="TimeFilter")]

    updated_utc: Annotated[Optional[UpdatedUtc], PropertyInfo(alias="UpdatedUtc")]


class Extent(TypedDict, total=False):
    accounting_items: Annotated[bool, PropertyInfo(alias="AccountingItems")]

    credit_card_transactions: Annotated[bool, PropertyInfo(alias="CreditCardTransactions")]

    order_items: Annotated[bool, PropertyInfo(alias="OrderItems")]

    payment_items: Annotated[bool, PropertyInfo(alias="PaymentItems")]


class ClosedUtc(TypedDict, total=False):
    end_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="EndUtc", format="iso8601")]

    start_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="StartUtc", format="iso8601")]


class ConsumedUtc(TypedDict, total=False):
    end_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="EndUtc", format="iso8601")]

    start_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="StartUtc", format="iso8601")]


class UpdatedUtc(TypedDict, total=False):
    end_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="EndUtc", format="iso8601")]

    start_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="StartUtc", format="iso8601")]
