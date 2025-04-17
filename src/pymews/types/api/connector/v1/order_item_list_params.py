# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["OrderItemListParams", "Limitation", "CanceledUtc", "ClosedUtc", "ConsumedUtc", "CreatedUtc", "UpdatedUtc"]


class OrderItemListParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    limitation: Required[Annotated[Limitation, PropertyInfo(alias="Limitation")]]
    """Limitation on the quantity of data returned."""

    accounting_states: Annotated[
        Optional[List[Literal["Open", "Closed", "Inactive", "Canceled"]]], PropertyInfo(alias="AccountingStates")
    ]
    """Accounting state of the item."""

    bill_ids: Annotated[Optional[List[str]], PropertyInfo(alias="BillIds")]
    """
    Unique identifiers of the
    [Bills](https://mews-systems.gitbook.io/connector-api/operations/bills/#bill) to
    which order item is assigned. Required if no other filter is provided.
    """

    canceled_utc: Annotated[Optional[CanceledUtc], PropertyInfo(alias="CanceledUtc")]
    """
    Interval in which the
    [Order item](https://mews-systems.gitbook.io/connector-api/operations/orderitems/#order-item)
    was canceled. Required if no other filter is provided.
    """

    closed_utc: Annotated[Optional[ClosedUtc], PropertyInfo(alias="ClosedUtc")]
    """
    Interval in which the
    [Order item](https://mews-systems.gitbook.io/connector-api/operations/orderitems/#order-item)
    was closed. Required if no other filter is provided.
    """

    consumed_utc: Annotated[Optional[ConsumedUtc], PropertyInfo(alias="ConsumedUtc")]
    """
    Interval in which the
    [Order item](https://mews-systems.gitbook.io/connector-api/operations/orderitems/#order-item)
    was consumed. Required if no other filter is provided.
    """

    created_utc: Annotated[Optional[CreatedUtc], PropertyInfo(alias="CreatedUtc")]
    """
    Interval in which the
    [Order item](https://mews-systems.gitbook.io/connector-api/operations/orderitems/#order-item)
    was created. Required if no other filter is provided.
    """

    currency: Annotated[Optional[str], PropertyInfo(alias="Currency")]
    """
    ISO-4217 code of the
    [Currency](https://mews-systems.gitbook.io/connector-api/operations/currencies/#currency)
    the item costs should be converted to.
    """

    enterprise_ids: Annotated[Optional[List[str]], PropertyInfo(alias="EnterpriseIds")]
    """Unique identifiers of the Enterprises.

    If not specified, the operation returns data for all enterprises within scope of
    the Access Token.
    """

    order_item_ids: Annotated[Optional[List[str]], PropertyInfo(alias="OrderItemIds")]
    """
    Unique identifiers of the
    [Order items](https://mews-systems.gitbook.io/connector-api/operations/orderitems/#order-item).
    Required if no other filter is provided.
    """

    service_ids: Annotated[Optional[List[str]], PropertyInfo(alias="ServiceIds")]
    """
    Unique identifiers of the
    [Services](https://mews-systems.gitbook.io/connector-api/operations/services/#service).
    Required if no other filter is provided.
    """

    service_order_ids: Annotated[Optional[List[str]], PropertyInfo(alias="ServiceOrderIds")]
    """
    Unique identifiers of the service orders
    ([product service orders](https://mews-systems.gitbook.io/connector-api/operations/productserviceorders/#product-service-order)
    or
    [reservations](https://mews-systems.gitbook.io/connector-api/operations/reservations/#reservation-ver-2023-06-06)).
    Required if no other filter is provided.
    """

    types: Annotated[
        Optional[
            List[
                Literal[
                    "CancellationFee",
                    "NightRebate",
                    "ProductOrderRebate",
                    "AdditionalExpenseRebate",
                    "Deposit",
                    "ExchangeRateDifference",
                    "CustomItem",
                    "ServiceCharge",
                    "CityTax",
                    "CityTaxDiscount",
                    "SpaceOrder",
                    "ProductOrder",
                    "Surcharge",
                    "TaxCorrection",
                    "ResourceUpgradeFee",
                    "InvoiceFee",
                    "MulticurrencyFee",
                    "AllowanceDiscount",
                ]
            ]
        ],
        PropertyInfo(alias="Types"),
    ]
    """Order item type, e.g. whether product order or space order."""

    updated_utc: Annotated[Optional[UpdatedUtc], PropertyInfo(alias="UpdatedUtc")]
    """
    Interval in which the
    [Order item](https://mews-systems.gitbook.io/connector-api/operations/orderitems/#order-item)
    was updated. Required if no other filter is provided.
    """


class Limitation(TypedDict, total=False):
    count: Required[Annotated[int, PropertyInfo(alias="Count")]]

    cursor: Annotated[Optional[str], PropertyInfo(alias="Cursor")]


class CanceledUtc(TypedDict, total=False):
    end_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="EndUtc", format="iso8601")]

    start_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="StartUtc", format="iso8601")]


class ClosedUtc(TypedDict, total=False):
    end_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="EndUtc", format="iso8601")]

    start_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="StartUtc", format="iso8601")]


class ConsumedUtc(TypedDict, total=False):
    end_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="EndUtc", format="iso8601")]

    start_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="StartUtc", format="iso8601")]


class CreatedUtc(TypedDict, total=False):
    end_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="EndUtc", format="iso8601")]

    start_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="StartUtc", format="iso8601")]


class UpdatedUtc(TypedDict, total=False):
    end_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="EndUtc", format="iso8601")]

    start_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="StartUtc", format="iso8601")]
