# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = [
    "OrderItemListResponse",
    "OrderItem",
    "OrderItemAmount",
    "OrderItemAmountBreakdown",
    "OrderItemAmountBreakdownItem",
    "OrderItemAmountTaxValue",
    "OrderItemOptions",
    "OrderItemOriginalAmount",
    "OrderItemOriginalAmountBreakdown",
    "OrderItemOriginalAmountBreakdownItem",
    "OrderItemOriginalAmountTaxValue",
    "OrderItemUnitAmount",
    "OrderItemUnitAmountBreakdown",
    "OrderItemUnitAmountBreakdownItem",
    "OrderItemUnitAmountTaxValue",
    "OrderItemData",
    "OrderItemDataProduct",
    "OrderItemDataRebate",
]


class OrderItemAmountBreakdownItem(BaseModel):
    net_value: float = FieldInfo(alias="NetValue")
    """The net value that the tax is calculated from."""

    tax_value: float = FieldInfo(alias="TaxValue")
    """The value of the tax."""

    tax_rate_code: Optional[str] = FieldInfo(alias="TaxRateCode", default=None)
    """Tax rate code for the item. `null` for untaxed amounts."""


class OrderItemAmountBreakdown(BaseModel):
    items: List[OrderItemAmountBreakdownItem] = FieldInfo(alias="Items")
    """Tax breakdown items per each tax rate applied."""


class OrderItemAmountTaxValue(BaseModel):
    value: float = FieldInfo(alias="Value")
    """Amount of tax applied."""

    code: Optional[str] = FieldInfo(alias="Code", default=None)
    """Code corresponding to tax type."""


class OrderItemAmount(BaseModel):
    breakdown: OrderItemAmountBreakdown = FieldInfo(alias="Breakdown")
    """Information about individual tax amounts."""

    currency: str = FieldInfo(alias="Currency")
    """
    ISO-4217 code of the
    [Currency](https://mews-systems.gitbook.io/connector-api/operations/currencies/#currency).
    """

    gross_value: float = FieldInfo(alias="GrossValue")
    """Gross value including all taxes."""

    net_value: float = FieldInfo(alias="NetValue")
    """Net value without taxes."""

    tax_values: List[OrderItemAmountTaxValue] = FieldInfo(alias="TaxValues")
    """The tax values applied."""


class OrderItemOptions(BaseModel):
    canceled_with_reservation: bool = FieldInfo(alias="CanceledWithReservation")
    """Order item was canceled with reservation cancellation."""


class OrderItemOriginalAmountBreakdownItem(BaseModel):
    net_value: float = FieldInfo(alias="NetValue")
    """The net value that the tax is calculated from."""

    tax_value: float = FieldInfo(alias="TaxValue")
    """The value of the tax."""

    tax_rate_code: Optional[str] = FieldInfo(alias="TaxRateCode", default=None)
    """Tax rate code for the item. `null` for untaxed amounts."""


class OrderItemOriginalAmountBreakdown(BaseModel):
    items: List[OrderItemOriginalAmountBreakdownItem] = FieldInfo(alias="Items")
    """Tax breakdown items per each tax rate applied."""


class OrderItemOriginalAmountTaxValue(BaseModel):
    value: float = FieldInfo(alias="Value")
    """Amount of tax applied."""

    code: Optional[str] = FieldInfo(alias="Code", default=None)
    """Code corresponding to tax type."""


class OrderItemOriginalAmount(BaseModel):
    breakdown: OrderItemOriginalAmountBreakdown = FieldInfo(alias="Breakdown")
    """Information about individual tax amounts."""

    currency: str = FieldInfo(alias="Currency")
    """
    ISO-4217 code of the
    [Currency](https://mews-systems.gitbook.io/connector-api/operations/currencies/#currency).
    """

    gross_value: float = FieldInfo(alias="GrossValue")
    """Gross value including all taxes."""

    net_value: float = FieldInfo(alias="NetValue")
    """Net value without taxes."""

    tax_values: List[OrderItemOriginalAmountTaxValue] = FieldInfo(alias="TaxValues")
    """The tax values applied."""


class OrderItemUnitAmountBreakdownItem(BaseModel):
    net_value: float = FieldInfo(alias="NetValue")
    """The net value that the tax is calculated from."""

    tax_value: float = FieldInfo(alias="TaxValue")
    """The value of the tax."""

    tax_rate_code: Optional[str] = FieldInfo(alias="TaxRateCode", default=None)
    """Tax rate code for the item. `null` for untaxed amounts."""


class OrderItemUnitAmountBreakdown(BaseModel):
    items: List[OrderItemUnitAmountBreakdownItem] = FieldInfo(alias="Items")
    """Tax breakdown items per each tax rate applied."""


class OrderItemUnitAmountTaxValue(BaseModel):
    value: float = FieldInfo(alias="Value")
    """Amount of tax applied."""

    code: Optional[str] = FieldInfo(alias="Code", default=None)
    """Code corresponding to tax type."""


class OrderItemUnitAmount(BaseModel):
    breakdown: OrderItemUnitAmountBreakdown = FieldInfo(alias="Breakdown")
    """Information about individual tax amounts."""

    currency: str = FieldInfo(alias="Currency")
    """
    ISO-4217 code of the
    [Currency](https://mews-systems.gitbook.io/connector-api/operations/currencies/#currency).
    """

    gross_value: float = FieldInfo(alias="GrossValue")
    """Gross value including all taxes."""

    net_value: float = FieldInfo(alias="NetValue")
    """Net value without taxes."""

    tax_values: List[OrderItemUnitAmountTaxValue] = FieldInfo(alias="TaxValues")
    """The tax values applied."""


class OrderItemDataProduct(BaseModel):
    product_id: str = FieldInfo(alias="ProductId")
    """
    Unique identifier of the
    [Product](https://mews-systems.gitbook.io/connector-api/operations/products/#product).
    """

    age_category_id: Optional[str] = FieldInfo(alias="AgeCategoryId", default=None)
    """
    Unique identifier of the
    [Age Category](https://mews-systems.gitbook.io/connector-api/operations/agecategories/#age-category).
    """


class OrderItemDataRebate(BaseModel):
    product_id: str = FieldInfo(alias="ProductId")
    """
    Unique identifier of the
    [Product](https://mews-systems.gitbook.io/connector-api/operations/products/#product)
    of the original rebated
    [Order item](https://mews-systems.gitbook.io/connector-api/operations/orderitems/#order-item).
    """

    rebated_item_id: str = FieldInfo(alias="RebatedItemId")
    """
    Unique identifier of
    [Order item](https://mews-systems.gitbook.io/connector-api/operations/orderitems/#order-item)
    which has been rebated by current item.
    """


class OrderItemData(BaseModel):
    discriminator: Optional[Literal["Rebate", "Product"]] = FieldInfo(alias="Discriminator", default=None)
    """Rebate

    Product
    """

    product: Optional[OrderItemDataProduct] = FieldInfo(alias="Product", default=None)
    """Contains additional data in the case of product item."""

    rebate: Optional[OrderItemDataRebate] = FieldInfo(alias="Rebate", default=None)
    """Contains additional data in the case of rebate item."""


class OrderItem(BaseModel):
    accounting_state: Literal["Open", "Closed", "Inactive", "Canceled"] = FieldInfo(alias="AccountingState")
    """
    Open (Order items which carry a non-zero value, are open, and have not been
    closed on a bill or invoice.)

    Closed (Order items which carry a non-zero value and have been closed on a bill
    or invoice.)

    Inactive (Order items which are either of zero value and have not been canceled,
    if the state of the payment item is Pending or Failed, or items of optional
    reservations. Until the reservation is confirmed, all its accounting items are
    Inactive.)

    Canceled (Order items which have been canceled, regardless of whether the item
    is of zero value.)

    - `Open` - Order items which carry a non-zero value, are open, and have not been
      closed on a bill or invoice.
    - `Closed` - Order items which carry a non-zero value and have been closed on a
      bill or invoice.
    - `Inactive` - Order items which are either of zero value and have not been
      canceled, if the state of the payment item is Pending or Failed, or items of
      optional reservations. Until the reservation is confirmed, all its accounting
      items are Inactive.
    - `Canceled` - Order items which have been canceled, regardless of whether the
      item is of zero value.
    """

    amount: OrderItemAmount = FieldInfo(alias="Amount")

    consumed_utc: datetime = FieldInfo(alias="ConsumedUtc")
    """Date and time of the item consumption in UTC timezone in ISO 8601 format."""

    created_utc: datetime = FieldInfo(alias="CreatedUtc")
    """
    Creation date and time of the order item created in UTC timezone in ISO 8601
    format.
    """

    creator_profile_id: str = FieldInfo(alias="CreatorProfileId")
    """Unique identifier of the user who created the order item."""

    enterprise_id: str = FieldInfo(alias="EnterpriseId")
    """
    Unique identifier of the
    [Enterprise](https://mews-systems.gitbook.io/connector-api/operations/enterprises/#enterprise).
    """

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the order item."""

    options: OrderItemOptions = FieldInfo(alias="Options")
    """Options of the order item."""

    original_amount: OrderItemOriginalAmount = FieldInfo(alias="OriginalAmount")

    revenue_type: Literal["Service", "Product", "Additional"] = FieldInfo(alias="RevenueType")
    """Revenue type.

    Service

    Product

    Additional
    """

    service_id: str = FieldInfo(alias="ServiceId")
    """
    Unique identifier of the
    [Service](https://mews-systems.gitbook.io/connector-api/operations/services/#service)
    the order item is assigned to.
    """

    service_order_id: str = FieldInfo(alias="ServiceOrderId")
    """
    Unique identifier of the
    [Service order](https://mews-systems.gitbook.io/connector-api/operations/serviceorders/#service-order)
    the order item is assigned to.
    """

    type: Literal[
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
    ] = FieldInfo(alias="Type")
    """CancellationFee

    NightRebate

    ProductOrderRebate

    AdditionalExpenseRebate

    Deposit

    ExchangeRateDifference

    CustomItem

    ServiceCharge

    CityTax

    CityTaxDiscount

    SpaceOrder

    ProductOrder

    Surcharge

    TaxCorrection

    ResourceUpgradeFee

    InvoiceFee

    MulticurrencyFee

    AllowanceDiscount
    """

    unit_amount: OrderItemUnitAmount = FieldInfo(alias="UnitAmount")

    unit_count: int = FieldInfo(alias="UnitCount")
    """Unit count of item, i.e. the number of sub-items or units, if applicable."""

    updated_utc: datetime = FieldInfo(alias="UpdatedUtc")
    """Last update date and time of the order item in UTC timezone in ISO 8601 format."""

    updater_profile_id: str = FieldInfo(alias="UpdaterProfileId")
    """Unique identifier of the user who updated the order item."""

    account_id: Optional[str] = FieldInfo(alias="AccountId", default=None)
    """
    Unique identifier of the account (for example
    [Customer](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer))
    the order item belongs to.
    """

    accounting_category_id: Optional[str] = FieldInfo(alias="AccountingCategoryId", default=None)
    """
    Unique identifier of the
    [Accounting category](https://mews-systems.gitbook.io/connector-api/operations/accountingcategories/#accounting-category)
    the order item belongs to.
    """

    account_type: Optional[Literal["Company", "Customer"]] = FieldInfo(alias="AccountType", default=None)
    """Company

    Customer
    """

    bill_id: Optional[str] = FieldInfo(alias="BillId", default=None)
    """
    Unique identifier of the
    [Bill](https://mews-systems.gitbook.io/connector-api/operations/bills/#bill) the
    order item is assigned to.
    """

    billing_name: Optional[str] = FieldInfo(alias="BillingName", default=None)
    """Name of the order item for billing purposes."""

    canceled_utc: Optional[datetime] = FieldInfo(alias="CanceledUtc", default=None)
    """
    Cancellation date and time of the order item in UTC timezone in ISO 8601 format.
    """

    claimed_utc: Optional[datetime] = FieldInfo(alias="ClaimedUtc", default=None)
    """
    Date and time when the order item was claimed in UTC timezone in ISO 8601
    format.
    """

    closed_utc: Optional[datetime] = FieldInfo(alias="ClosedUtc", default=None)
    """Date and time of the item bill closure in UTC timezone in ISO 8601 format."""

    data: Optional[OrderItemData] = FieldInfo(alias="Data", default=None)
    """Additional order item data."""

    external_identifier: Optional[str] = FieldInfo(alias="ExternalIdentifier", default=None)
    """Identifier of the entity from external system."""

    notes: Optional[str] = FieldInfo(alias="Notes", default=None)
    """Additional notes."""

    start_utc: Optional[datetime] = FieldInfo(alias="StartUtc", default=None)
    """Start of the order item in UTC timezone in ISO 8601 format."""

    tax_exemption_legal_reference: Optional[str] = FieldInfo(alias="TaxExemptionLegalReference", default=None)
    """Legal reference that states why this order item is exempt from tax."""

    tax_exemption_reason: Optional[Literal["IT_N1", "IT_N2_2", "IT_N3_5", "IT_N4", "IT_N5"]] = FieldInfo(
        alias="TaxExemptionReason", default=None
    )
    """IT_N1 (N1 - Escluse ex art.15)

    IT_N2_2 (N2.2 - Non soggette – altri casi)

    IT_N3_5 (N3.5 - Non imponibili – a seguito di dichiarazioni d’intento)

    IT_N4 (N4 - Esenti)

    IT_N5 (N5 - Regime del margine / IVA non esposta in fattura)

    - `IT_N1` - N1 - Escluse ex art.15
    - `IT_N2_2` - N2.2 - Non soggette – altri casi
    - `IT_N3_5` - N3.5 - Non imponibili – a seguito di dichiarazioni d’intento
    - `IT_N4` - N4 - Esenti
    - `IT_N5` - N5 - Regime del margine / IVA non esposta in fattura
    """


class OrderItemListResponse(BaseModel):
    order_items: List[OrderItem] = FieldInfo(alias="OrderItems")
    """Set of requested order items."""

    cursor: Optional[str] = FieldInfo(alias="Cursor", default=None)
    """Unique identifier of the last and hence oldest order item returned.

    This can be used in
    [Limitation](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/#limitation)
    in a subsequent request to fetch the next batch of older order items.
    """
