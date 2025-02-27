# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import date
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = [
    "CustomerGetOpenItemsResponse",
    "Customer",
    "CustomerItem",
    "CustomerItemAmount",
    "CustomerItemAmountBreakdown",
    "CustomerItemAmountBreakdownItem",
    "CustomerItemAmountTaxValue",
    "CustomerOrderItem",
    "CustomerOrderItemAmount",
    "CustomerOrderItemAmountBreakdown",
    "CustomerOrderItemAmountBreakdownItem",
    "CustomerOrderItemAmountTaxValue",
    "CustomerOrderItemData",
    "CustomerOrderItemDataValue",
    "CustomerOrderItemDataValueRebateOrderItemData",
    "CustomerOrderItemDataValueProductOrderItemData",
    "CustomerOrderItemOriginalAmount",
    "CustomerOrderItemOriginalAmountBreakdown",
    "CustomerOrderItemOriginalAmountBreakdownItem",
    "CustomerOrderItemOriginalAmountTaxValue",
    "CustomerOrderItemUnitAmount",
    "CustomerOrderItemUnitAmountBreakdown",
    "CustomerOrderItemUnitAmountBreakdownItem",
    "CustomerOrderItemUnitAmountTaxValue",
    "CustomerPaymentItem",
    "CustomerPaymentItemAmount",
    "CustomerPaymentItemAmountBreakdown",
    "CustomerPaymentItemAmountBreakdownItem",
    "CustomerPaymentItemAmountTaxValue",
    "CustomerPaymentItemAmountDefault",
    "CustomerPaymentItemAmountDefaultBreakdown",
    "CustomerPaymentItemAmountDefaultBreakdownItem",
    "CustomerPaymentItemAmountDefaultTaxValue",
    "CustomerPaymentItemData",
    "CustomerPaymentItemDataValue",
    "CustomerPaymentItemDataValuePaymentCardPaymentData",
    "CustomerPaymentItemDataValueInvoicePaymentData",
    "CustomerPaymentItemOriginalAmount",
    "CustomerPaymentItemOriginalAmountBreakdown",
    "CustomerPaymentItemOriginalAmountBreakdownItem",
    "CustomerPaymentItemOriginalAmountTaxValue",
]


class CustomerItemAmountBreakdownItem(BaseModel):
    net_value: float = FieldInfo(alias="NetValue")
    """The net value that the tax is calculated from."""

    tax_value: float = FieldInfo(alias="TaxValue")
    """The value of the tax."""

    tax_rate_code: Optional[str] = FieldInfo(alias="TaxRateCode", default=None)
    """Tax rate code for the item. `null` for untaxed amounts."""


class CustomerItemAmountBreakdown(BaseModel):
    items: List[CustomerItemAmountBreakdownItem] = FieldInfo(alias="Items")
    """Tax breakdown items per each tax rate applied."""


class CustomerItemAmountTaxValue(BaseModel):
    value: float = FieldInfo(alias="Value")
    """Amount of tax applied."""

    code: Optional[str] = FieldInfo(alias="Code", default=None)
    """Code corresponding to tax type."""


class CustomerItemAmount(BaseModel):
    breakdown: CustomerItemAmountBreakdown = FieldInfo(alias="Breakdown")
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

    tax_values: List[CustomerItemAmountTaxValue] = FieldInfo(alias="TaxValues")
    """The tax values applied."""

    net: Optional[float] = FieldInfo(alias="Net", default=None)

    tax: Optional[float] = FieldInfo(alias="Tax", default=None)

    tax_rate: Optional[float] = FieldInfo(alias="TaxRate", default=None)

    value: Optional[float] = FieldInfo(alias="Value", default=None)


class CustomerItem(BaseModel):
    account_id: Optional[str] = FieldInfo(alias="AccountId", default=None)

    accounting_category_id: Optional[str] = FieldInfo(alias="AccountingCategoryId", default=None)

    amount: Optional[CustomerItemAmount] = FieldInfo(alias="Amount", default=None)

    bill_id: Optional[str] = FieldInfo(alias="BillId", default=None)

    closed_utc: Optional[str] = FieldInfo(alias="ClosedUtc", default=None)

    consumption_utc: Optional[str] = FieldInfo(alias="ConsumptionUtc", default=None)

    credit_card_id: Optional[str] = FieldInfo(alias="CreditCardId", default=None)

    customer_id: Optional[str] = FieldInfo(alias="CustomerId", default=None)

    id: Optional[str] = FieldInfo(alias="Id", default=None)

    invoice_id: Optional[str] = FieldInfo(alias="InvoiceId", default=None)

    name: Optional[str] = FieldInfo(alias="Name", default=None)

    notes: Optional[str] = FieldInfo(alias="Notes", default=None)

    order_id: Optional[str] = FieldInfo(alias="OrderId", default=None)

    product_id: Optional[str] = FieldInfo(alias="ProductId", default=None)

    service_id: Optional[str] = FieldInfo(alias="ServiceId", default=None)

    state: Optional[str] = FieldInfo(alias="State", default=None)

    sub_state: Optional[str] = FieldInfo(alias="SubState", default=None)

    sub_type: Optional[str] = FieldInfo(alias="SubType", default=None)

    tax_exemption_reason_code: Optional[str] = FieldInfo(alias="TaxExemptionReasonCode", default=None)
    """Code of tax exemption reason.

    **Restricted!** This property is currently intended for Mews' internal usage and
    may be subject to change.
    """

    type: Optional[str] = FieldInfo(alias="Type", default=None)


class CustomerOrderItemAmountBreakdownItem(BaseModel):
    net_value: float = FieldInfo(alias="NetValue")
    """The net value that the tax is calculated from."""

    tax_value: float = FieldInfo(alias="TaxValue")
    """The value of the tax."""

    tax_rate_code: Optional[str] = FieldInfo(alias="TaxRateCode", default=None)
    """Tax rate code for the item. `null` for untaxed amounts."""


class CustomerOrderItemAmountBreakdown(BaseModel):
    items: List[CustomerOrderItemAmountBreakdownItem] = FieldInfo(alias="Items")
    """Tax breakdown items per each tax rate applied."""


class CustomerOrderItemAmountTaxValue(BaseModel):
    value: float = FieldInfo(alias="Value")
    """Amount of tax applied."""

    code: Optional[str] = FieldInfo(alias="Code", default=None)
    """Code corresponding to tax type."""


class CustomerOrderItemAmount(BaseModel):
    breakdown: CustomerOrderItemAmountBreakdown = FieldInfo(alias="Breakdown")
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

    tax_values: List[CustomerOrderItemAmountTaxValue] = FieldInfo(alias="TaxValues")
    """The tax values applied."""

    net: Optional[float] = FieldInfo(alias="Net", default=None)

    tax: Optional[float] = FieldInfo(alias="Tax", default=None)

    tax_rate: Optional[float] = FieldInfo(alias="TaxRate", default=None)

    value: Optional[float] = FieldInfo(alias="Value", default=None)


class CustomerOrderItemDataValueRebateOrderItemData(BaseModel):
    rebated_item_id: Optional[str] = FieldInfo(alias="RebatedItemId", default=None)


class CustomerOrderItemDataValueProductOrderItemData(BaseModel):
    age_category_id: Optional[str] = FieldInfo(alias="AgeCategoryId", default=None)

    product_id: Optional[str] = FieldInfo(alias="ProductId", default=None)


CustomerOrderItemDataValue: TypeAlias = Union[
    CustomerOrderItemDataValueRebateOrderItemData, CustomerOrderItemDataValueProductOrderItemData
]


class CustomerOrderItemData(BaseModel):
    discriminator: Optional[
        Literal[
            "CancellationFee",
            "Rebate",
            "Deposit",
            "ExchangeRateDifference",
            "CustomItem",
            "Surcharge",
            "SurchargeDiscount",
            "SpaceOrder",
            "ProductOrder",
            "Other",
            "TaxCorrection",
            "ResourceUpgradeFee",
            "InvoiceFee",
        ]
    ] = None

    value: Optional[CustomerOrderItemDataValue] = None


class CustomerOrderItemOriginalAmountBreakdownItem(BaseModel):
    net_value: float = FieldInfo(alias="NetValue")
    """The net value that the tax is calculated from."""

    tax_value: float = FieldInfo(alias="TaxValue")
    """The value of the tax."""

    tax_rate_code: Optional[str] = FieldInfo(alias="TaxRateCode", default=None)
    """Tax rate code for the item. `null` for untaxed amounts."""


class CustomerOrderItemOriginalAmountBreakdown(BaseModel):
    items: List[CustomerOrderItemOriginalAmountBreakdownItem] = FieldInfo(alias="Items")
    """Tax breakdown items per each tax rate applied."""


class CustomerOrderItemOriginalAmountTaxValue(BaseModel):
    value: float = FieldInfo(alias="Value")
    """Amount of tax applied."""

    code: Optional[str] = FieldInfo(alias="Code", default=None)
    """Code corresponding to tax type."""


class CustomerOrderItemOriginalAmount(BaseModel):
    breakdown: CustomerOrderItemOriginalAmountBreakdown = FieldInfo(alias="Breakdown")
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

    tax_values: List[CustomerOrderItemOriginalAmountTaxValue] = FieldInfo(alias="TaxValues")
    """The tax values applied."""

    net: Optional[float] = FieldInfo(alias="Net", default=None)

    tax: Optional[float] = FieldInfo(alias="Tax", default=None)

    tax_rate: Optional[float] = FieldInfo(alias="TaxRate", default=None)

    value: Optional[float] = FieldInfo(alias="Value", default=None)


class CustomerOrderItemUnitAmountBreakdownItem(BaseModel):
    net_value: float = FieldInfo(alias="NetValue")
    """The net value that the tax is calculated from."""

    tax_value: float = FieldInfo(alias="TaxValue")
    """The value of the tax."""

    tax_rate_code: Optional[str] = FieldInfo(alias="TaxRateCode", default=None)
    """Tax rate code for the item. `null` for untaxed amounts."""


class CustomerOrderItemUnitAmountBreakdown(BaseModel):
    items: List[CustomerOrderItemUnitAmountBreakdownItem] = FieldInfo(alias="Items")
    """Tax breakdown items per each tax rate applied."""


class CustomerOrderItemUnitAmountTaxValue(BaseModel):
    value: float = FieldInfo(alias="Value")
    """Amount of tax applied."""

    code: Optional[str] = FieldInfo(alias="Code", default=None)
    """Code corresponding to tax type."""


class CustomerOrderItemUnitAmount(BaseModel):
    breakdown: CustomerOrderItemUnitAmountBreakdown = FieldInfo(alias="Breakdown")
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

    tax_values: List[CustomerOrderItemUnitAmountTaxValue] = FieldInfo(alias="TaxValues")
    """The tax values applied."""


class CustomerOrderItem(BaseModel):
    account_id: Optional[str] = FieldInfo(alias="AccountId", default=None)
    """
    Unique identifier of the account (for example
    [Customer](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer))
    the item belongs to.
    """

    accounting_category_id: Optional[str] = FieldInfo(alias="AccountingCategoryId", default=None)
    """
    Unique identifier of the
    [Accounting category](https://mews-systems.gitbook.io/connector-api/operations/accountingcategories/#accounting-category)
    the item belongs to.
    """

    accounting_state: Optional[str] = FieldInfo(alias="AccountingState", default=None)
    """Accounting state of the item."""

    amount: Optional[CustomerOrderItemAmount] = FieldInfo(alias="Amount", default=None)

    bill_id: Optional[str] = FieldInfo(alias="BillId", default=None)
    """
    Unique identifier of the
    [Bill](https://mews-systems.gitbook.io/connector-api/operations/bills/#bill) the
    item is assigned to.
    """

    canceled_utc: Optional[date] = FieldInfo(alias="CanceledUtc", default=None)

    closed_utc: Optional[date] = FieldInfo(alias="ClosedUtc", default=None)
    """Date and time of the item bill closure in UTC timezone in ISO 8601 format."""

    consumed_utc: Optional[date] = FieldInfo(alias="ConsumedUtc", default=None)
    """Date and time of the item consumption in UTC timezone in ISO 8601 format."""

    created_utc: Optional[date] = FieldInfo(alias="CreatedUtc", default=None)

    creator_profile_id: Optional[str] = FieldInfo(alias="CreatorProfileId", default=None)

    data: Optional[CustomerOrderItemData] = FieldInfo(alias="Data", default=None)
    """Additional data specific to particular order item."""

    id: Optional[str] = FieldInfo(alias="Id", default=None)
    """Unique identifier of the item."""

    order_id: Optional[str] = FieldInfo(alias="OrderId", default=None)
    """
    Unique identifier of the order (or
    [Reservation](https://mews-systems.gitbook.io/connector-api/operations/reservations/#reservation-ver-2023-06-06)
    which is a special type of order) the item belongs to.
    """

    original_amount: Optional[CustomerOrderItemOriginalAmount] = FieldInfo(alias="OriginalAmount", default=None)

    revenue_type: Optional[str] = FieldInfo(alias="RevenueType", default=None)
    """Revenue type of the item."""

    start_utc: Optional[date] = FieldInfo(alias="StartUtc", default=None)

    unit_amount: Optional[CustomerOrderItemUnitAmount] = FieldInfo(alias="UnitAmount", default=None)

    unit_count: Optional[int] = FieldInfo(alias="UnitCount", default=None)
    """Unit count of item, i.e. the number of sub-items or units, if applicable."""

    updated_utc: Optional[date] = FieldInfo(alias="UpdatedUtc", default=None)

    updater_profile_id: Optional[str] = FieldInfo(alias="UpdaterProfileId", default=None)


class CustomerPaymentItemAmountBreakdownItem(BaseModel):
    net_value: float = FieldInfo(alias="NetValue")
    """The net value that the tax is calculated from."""

    tax_value: float = FieldInfo(alias="TaxValue")
    """The value of the tax."""

    tax_rate_code: Optional[str] = FieldInfo(alias="TaxRateCode", default=None)
    """Tax rate code for the item. `null` for untaxed amounts."""


class CustomerPaymentItemAmountBreakdown(BaseModel):
    items: List[CustomerPaymentItemAmountBreakdownItem] = FieldInfo(alias="Items")
    """Tax breakdown items per each tax rate applied."""


class CustomerPaymentItemAmountTaxValue(BaseModel):
    value: float = FieldInfo(alias="Value")
    """Amount of tax applied."""

    code: Optional[str] = FieldInfo(alias="Code", default=None)
    """Code corresponding to tax type."""


class CustomerPaymentItemAmount(BaseModel):
    breakdown: CustomerPaymentItemAmountBreakdown = FieldInfo(alias="Breakdown")
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

    tax_values: List[CustomerPaymentItemAmountTaxValue] = FieldInfo(alias="TaxValues")
    """The tax values applied."""

    net: Optional[float] = FieldInfo(alias="Net", default=None)

    tax: Optional[float] = FieldInfo(alias="Tax", default=None)

    tax_rate: Optional[float] = FieldInfo(alias="TaxRate", default=None)

    value: Optional[float] = FieldInfo(alias="Value", default=None)


class CustomerPaymentItemAmountDefaultBreakdownItem(BaseModel):
    net_value: float = FieldInfo(alias="NetValue")
    """The net value that the tax is calculated from."""

    tax_value: float = FieldInfo(alias="TaxValue")
    """The value of the tax."""

    tax_rate_code: Optional[str] = FieldInfo(alias="TaxRateCode", default=None)
    """Tax rate code for the item. `null` for untaxed amounts."""


class CustomerPaymentItemAmountDefaultBreakdown(BaseModel):
    items: List[CustomerPaymentItemAmountDefaultBreakdownItem] = FieldInfo(alias="Items")
    """Tax breakdown items per each tax rate applied."""


class CustomerPaymentItemAmountDefaultTaxValue(BaseModel):
    value: float = FieldInfo(alias="Value")
    """Amount of tax applied."""

    code: Optional[str] = FieldInfo(alias="Code", default=None)
    """Code corresponding to tax type."""


class CustomerPaymentItemAmountDefault(BaseModel):
    breakdown: CustomerPaymentItemAmountDefaultBreakdown = FieldInfo(alias="Breakdown")
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

    tax_values: List[CustomerPaymentItemAmountDefaultTaxValue] = FieldInfo(alias="TaxValues")
    """The tax values applied."""

    net: Optional[float] = FieldInfo(alias="Net", default=None)

    tax: Optional[float] = FieldInfo(alias="Tax", default=None)

    tax_rate: Optional[float] = FieldInfo(alias="TaxRate", default=None)

    value: Optional[float] = FieldInfo(alias="Value", default=None)


class CustomerPaymentItemDataValuePaymentCardPaymentData(BaseModel):
    payment_card_id: Optional[str] = FieldInfo(alias="PaymentCardId", default=None)


class CustomerPaymentItemDataValueInvoicePaymentData(BaseModel):
    invoice_id: Optional[str] = FieldInfo(alias="InvoiceId", default=None)


CustomerPaymentItemDataValue: TypeAlias = Union[
    CustomerPaymentItemDataValuePaymentCardPaymentData, CustomerPaymentItemDataValueInvoicePaymentData
]


class CustomerPaymentItemData(BaseModel):
    discriminator: Optional[
        Literal[
            "CreditCard",
            "Invoice",
            "Cash",
            "Unspecified",
            "BadDebts",
            "WireTransfer",
            "ExchangeRateDifference",
            "ExchangeRoundingDifference",
            "BankCharges",
            "Cheque",
            "Other",
        ]
    ] = None

    value: Optional[CustomerPaymentItemDataValue] = None


class CustomerPaymentItemOriginalAmountBreakdownItem(BaseModel):
    net_value: float = FieldInfo(alias="NetValue")
    """The net value that the tax is calculated from."""

    tax_value: float = FieldInfo(alias="TaxValue")
    """The value of the tax."""

    tax_rate_code: Optional[str] = FieldInfo(alias="TaxRateCode", default=None)
    """Tax rate code for the item. `null` for untaxed amounts."""


class CustomerPaymentItemOriginalAmountBreakdown(BaseModel):
    items: List[CustomerPaymentItemOriginalAmountBreakdownItem] = FieldInfo(alias="Items")
    """Tax breakdown items per each tax rate applied."""


class CustomerPaymentItemOriginalAmountTaxValue(BaseModel):
    value: float = FieldInfo(alias="Value")
    """Amount of tax applied."""

    code: Optional[str] = FieldInfo(alias="Code", default=None)
    """Code corresponding to tax type."""


class CustomerPaymentItemOriginalAmount(BaseModel):
    breakdown: CustomerPaymentItemOriginalAmountBreakdown = FieldInfo(alias="Breakdown")
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

    tax_values: List[CustomerPaymentItemOriginalAmountTaxValue] = FieldInfo(alias="TaxValues")
    """The tax values applied."""

    net: Optional[float] = FieldInfo(alias="Net", default=None)

    tax: Optional[float] = FieldInfo(alias="Tax", default=None)

    tax_rate: Optional[float] = FieldInfo(alias="TaxRate", default=None)

    value: Optional[float] = FieldInfo(alias="Value", default=None)


class CustomerPaymentItem(BaseModel):
    account_id: Optional[str] = FieldInfo(alias="AccountId", default=None)
    """
    Unique identifier of the account (for example
    [Customer](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer))
    the item belongs to.
    """

    accounting_category_id: Optional[str] = FieldInfo(alias="AccountingCategoryId", default=None)
    """
    Unique identifier of the
    [Accounting category](https://mews-systems.gitbook.io/connector-api/operations/accountingcategories/#accounting-category)
    the item belongs to.
    """

    accounting_state: Optional[str] = FieldInfo(alias="AccountingState", default=None)
    """Accounting state of the item."""

    amount: Optional[CustomerPaymentItemAmount] = FieldInfo(alias="Amount", default=None)

    amount_default: Optional[CustomerPaymentItemAmountDefault] = FieldInfo(alias="AmountDefault", default=None)

    bill_id: Optional[str] = FieldInfo(alias="BillId", default=None)
    """
    Unique identifier of the
    [Bill](https://mews-systems.gitbook.io/connector-api/operations/bills/#bill) the
    item is assigned to.
    """

    closed_utc: Optional[str] = FieldInfo(alias="ClosedUtc", default=None)
    """Date and time of the item bill closure in UTC timezone in ISO 8601 format."""

    consumed_utc: Optional[str] = FieldInfo(alias="ConsumedUtc", default=None)
    """Date and time of the item consumption in UTC timezone in ISO 8601 format."""

    data: Optional[CustomerPaymentItemData] = FieldInfo(alias="Data", default=None)
    """Additional data specific to particular payment item."""

    id: Optional[str] = FieldInfo(alias="Id", default=None)
    """Unique identifier of the item."""

    identifier: Optional[str] = FieldInfo(alias="Identifier", default=None)

    notes: Optional[str] = FieldInfo(alias="Notes", default=None)
    """Additional notes."""

    original_amount: Optional[CustomerPaymentItemOriginalAmount] = FieldInfo(alias="OriginalAmount", default=None)

    settlement_id: Optional[str] = FieldInfo(alias="SettlementId", default=None)
    """
    Identifier of the settled payment from the external system (ApplePay/GooglePay).
    """

    state: Optional[str] = FieldInfo(alias="State", default=None)
    """Payment state of the item."""


class Customer(BaseModel):
    customer_id: str = FieldInfo(alias="CustomerId")
    """Unique identifier of the `Customer`."""

    items: List[CustomerItem] = FieldInfo(alias="Items")

    order_items: List[CustomerOrderItem] = FieldInfo(alias="OrderItems")
    """The open order items (consumed items such as nights or products)."""

    payment_items: List[CustomerPaymentItem] = FieldInfo(alias="PaymentItems")
    """The open payment items (such as cash, credit card payments or invoices)."""


class CustomerGetOpenItemsResponse(BaseModel):
    customers: Optional[List[Customer]] = FieldInfo(alias="Customers", default=None)
    """The customers with their items."""
