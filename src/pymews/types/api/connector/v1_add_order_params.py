# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = [
    "V1AddOrderParams",
    "Item",
    "ItemUnitAmount",
    "ItemCategory",
    "Options",
    "ProductOrder",
    "ProductOrderUnitAmount",
]


class V1AddOrderParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    service_id: Required[Annotated[str, PropertyInfo(alias="ServiceId")]]
    """
    Identifier of the
    [Service](https://mews-systems.gitbook.io/connector-api/operations/services/#service)
    to be ordered.
    """

    account_id: Annotated[Optional[str], PropertyInfo(alias="AccountId")]
    """
    Identifier of the
    [Customer](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer)
    or
    [Company](https://mews-systems.gitbook.io/connector-api/operations/companies/#company)
    to be charged. Company billing may not be enabled for your integration.
    """

    bill_id: Annotated[Optional[str], PropertyInfo(alias="BillId")]
    """
    Identifier of the
    [Bill](https://mews-systems.gitbook.io/connector-api/operations/bills/#bill) to
    which the created order will be assigned. The bill needs to be issued to the
    same account as the order.
    """

    business_segment_id: Annotated[Optional[str], PropertyInfo(alias="BusinessSegmentId")]

    consumption_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="ConsumptionUtc", format="iso8601")]
    """Date and time of the order consumption in UTC timezone in ISO 8601 format.

    If not specified, current date and time is used. Please note, as order
    consumption is one-time event, the optional parameters StartUtc and EndUtc in
    [Product order parameters](https://mews-systems.gitbook.io/connector-api/operations/#product-order-parameters)
    should not be used.
    """

    customer_id: Annotated[Optional[str], PropertyInfo(alias="CustomerId")]
    """
    Identifier of the
    [Customer](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer)
    to be charged. **Deprecated!**
    """

    enterprise_id: Annotated[Optional[str], PropertyInfo(alias="EnterpriseId")]
    """
    Unique identifier of the
    [Enterprise](https://mews-systems.gitbook.io/connector-api/operations/enterprises/#enterprise).
    Required when using a
    [Portfolio Access Token](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
    ignored otherwise.
    """

    items: Annotated[Optional[Iterable[Item]], PropertyInfo(alias="Items")]
    """Parameters of the ordered custom items."""

    linked_reservation_id: Annotated[Optional[str], PropertyInfo(alias="LinkedReservationId")]

    notes: Annotated[Optional[str], PropertyInfo(alias="Notes")]
    """Additional notes of the order."""

    options: Annotated[Optional[Options], PropertyInfo(alias="Options")]

    product_orders: Annotated[Optional[Iterable[ProductOrder]], PropertyInfo(alias="ProductOrders")]
    """Parameters of the ordered products."""


class ItemUnitAmount(TypedDict, total=False):
    currency: Required[Annotated[str, PropertyInfo(alias="Currency")]]

    tax_codes: Required[Annotated[List[str], PropertyInfo(alias="TaxCodes")]]

    gross_value: Annotated[Optional[float], PropertyInfo(alias="GrossValue")]

    net_value: Annotated[Optional[float], PropertyInfo(alias="NetValue")]


class ItemCategory(TypedDict, total=False):
    code: Annotated[Optional[str], PropertyInfo(alias="Code")]

    name: Annotated[Optional[str], PropertyInfo(alias="Name")]


class Item(TypedDict, total=False):
    name: Required[Annotated[str, PropertyInfo(alias="Name")]]

    unit_amount: Required[Annotated[ItemUnitAmount, PropertyInfo(alias="UnitAmount")]]
    """Price of the product that overrides the price defined in Mews."""

    unit_count: Required[Annotated[int, PropertyInfo(alias="UnitCount")]]

    accounting_category_id: Annotated[Optional[str], PropertyInfo(alias="AccountingCategoryId")]

    category: Annotated[Optional[ItemCategory], PropertyInfo(alias="Category")]

    external_identifier: Annotated[Optional[str], PropertyInfo(alias="ExternalIdentifier")]


class Options(TypedDict, total=False):
    disable_item_grouping: Annotated[bool, PropertyInfo(alias="DisableItemGrouping")]


class ProductOrderUnitAmount(TypedDict, total=False):
    currency: Required[Annotated[str, PropertyInfo(alias="Currency")]]

    tax_codes: Required[Annotated[List[str], PropertyInfo(alias="TaxCodes")]]

    gross_value: Annotated[Optional[float], PropertyInfo(alias="GrossValue")]

    net_value: Annotated[Optional[float], PropertyInfo(alias="NetValue")]


class ProductOrder(TypedDict, total=False):
    product_id: Required[Annotated[str, PropertyInfo(alias="ProductId")]]

    count: Annotated[Optional[int], PropertyInfo(alias="Count")]

    end_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="EndUtc", format="iso8601")]

    external_identifier: Annotated[Optional[str], PropertyInfo(alias="ExternalIdentifier")]

    start_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="StartUtc", format="iso8601")]

    unit_amount: Annotated[Optional[ProductOrderUnitAmount], PropertyInfo(alias="UnitAmount")]
    """Price of the product that overrides the price defined in Mews."""
