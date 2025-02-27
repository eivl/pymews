# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import date, datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = [
    "AccountingItemResult",
    "AccountingItem",
    "AccountingItemAmount",
    "AccountingItemAmountBreakdown",
    "AccountingItemAmountBreakdownItem",
    "AccountingItemAmountTaxValue",
    "CreditCardTransaction",
    "CreditCardTransactionChargedAmount",
    "CreditCardTransactionChargedAmountBreakdown",
    "CreditCardTransactionChargedAmountBreakdownItem",
    "CreditCardTransactionChargedAmountTaxValue",
    "CreditCardTransactionAdjustedFee",
    "CreditCardTransactionAdjustedFeeBreakdown",
    "CreditCardTransactionAdjustedFeeBreakdownItem",
    "CreditCardTransactionAdjustedFeeTaxValue",
    "CreditCardTransactionFee",
    "CreditCardTransactionFeeBreakdown",
    "CreditCardTransactionFeeBreakdownItem",
    "CreditCardTransactionFeeTaxValue",
    "CreditCardTransactionSettledAmount",
    "CreditCardTransactionSettledAmountBreakdown",
    "CreditCardTransactionSettledAmountBreakdownItem",
    "CreditCardTransactionSettledAmountTaxValue",
    "OrderItem",
    "OrderItemAmount",
    "OrderItemAmountBreakdown",
    "OrderItemAmountBreakdownItem",
    "OrderItemAmountTaxValue",
    "OrderItemData",
    "OrderItemDataValue",
    "OrderItemDataValueRebateOrderItemData",
    "OrderItemDataValueProductOrderItemData",
    "OrderItemOriginalAmount",
    "OrderItemOriginalAmountBreakdown",
    "OrderItemOriginalAmountBreakdownItem",
    "OrderItemOriginalAmountTaxValue",
    "OrderItemUnitAmount",
    "OrderItemUnitAmountBreakdown",
    "OrderItemUnitAmountBreakdownItem",
    "OrderItemUnitAmountTaxValue",
    "PaymentItem",
    "PaymentItemAmount",
    "PaymentItemAmountBreakdown",
    "PaymentItemAmountBreakdownItem",
    "PaymentItemAmountTaxValue",
    "PaymentItemAmountDefault",
    "PaymentItemAmountDefaultBreakdown",
    "PaymentItemAmountDefaultBreakdownItem",
    "PaymentItemAmountDefaultTaxValue",
    "PaymentItemData",
    "PaymentItemDataValue",
    "PaymentItemDataValuePaymentCardPaymentData",
    "PaymentItemDataValueInvoicePaymentData",
    "PaymentItemOriginalAmount",
    "PaymentItemOriginalAmountBreakdown",
    "PaymentItemOriginalAmountBreakdownItem",
    "PaymentItemOriginalAmountTaxValue",
]


class AccountingItemAmountBreakdownItem(BaseModel):
    net_value: float = FieldInfo(alias="NetValue")
    """The net value that the tax is calculated from."""

    tax_value: float = FieldInfo(alias="TaxValue")
    """The value of the tax."""

    tax_rate_code: Optional[str] = FieldInfo(alias="TaxRateCode", default=None)
    """Tax rate code for the item. `null` for untaxed amounts."""


class AccountingItemAmountBreakdown(BaseModel):
    items: List[AccountingItemAmountBreakdownItem] = FieldInfo(alias="Items")
    """Tax breakdown items per each tax rate applied."""


class AccountingItemAmountTaxValue(BaseModel):
    value: float = FieldInfo(alias="Value")
    """Amount of tax applied."""

    code: Optional[str] = FieldInfo(alias="Code", default=None)
    """Code corresponding to tax type."""


class AccountingItemAmount(BaseModel):
    breakdown: AccountingItemAmountBreakdown = FieldInfo(alias="Breakdown")
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

    tax_values: List[AccountingItemAmountTaxValue] = FieldInfo(alias="TaxValues")
    """The tax values applied."""

    net: Optional[float] = FieldInfo(alias="Net", default=None)

    tax: Optional[float] = FieldInfo(alias="Tax", default=None)

    tax_rate: Optional[float] = FieldInfo(alias="TaxRate", default=None)

    value: Optional[float] = FieldInfo(alias="Value", default=None)


class AccountingItem(BaseModel):
    account_id: Optional[str] = FieldInfo(alias="AccountId", default=None)

    accounting_category_id: Optional[str] = FieldInfo(alias="AccountingCategoryId", default=None)

    amount: Optional[AccountingItemAmount] = FieldInfo(alias="Amount", default=None)

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


class CreditCardTransactionChargedAmountBreakdownItem(BaseModel):
    net_value: float = FieldInfo(alias="NetValue")
    """The net value that the tax is calculated from."""

    tax_value: float = FieldInfo(alias="TaxValue")
    """The value of the tax."""

    tax_rate_code: Optional[str] = FieldInfo(alias="TaxRateCode", default=None)
    """Tax rate code for the item. `null` for untaxed amounts."""


class CreditCardTransactionChargedAmountBreakdown(BaseModel):
    items: List[CreditCardTransactionChargedAmountBreakdownItem] = FieldInfo(alias="Items")
    """Tax breakdown items per each tax rate applied."""


class CreditCardTransactionChargedAmountTaxValue(BaseModel):
    value: float = FieldInfo(alias="Value")
    """Amount of tax applied."""

    code: Optional[str] = FieldInfo(alias="Code", default=None)
    """Code corresponding to tax type."""


class CreditCardTransactionChargedAmount(BaseModel):
    breakdown: CreditCardTransactionChargedAmountBreakdown = FieldInfo(alias="Breakdown")
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

    tax_values: List[CreditCardTransactionChargedAmountTaxValue] = FieldInfo(alias="TaxValues")
    """The tax values applied."""

    net: Optional[float] = FieldInfo(alias="Net", default=None)

    tax: Optional[float] = FieldInfo(alias="Tax", default=None)

    tax_rate: Optional[float] = FieldInfo(alias="TaxRate", default=None)

    value: Optional[float] = FieldInfo(alias="Value", default=None)


class CreditCardTransactionAdjustedFeeBreakdownItem(BaseModel):
    net_value: float = FieldInfo(alias="NetValue")
    """The net value that the tax is calculated from."""

    tax_value: float = FieldInfo(alias="TaxValue")
    """The value of the tax."""

    tax_rate_code: Optional[str] = FieldInfo(alias="TaxRateCode", default=None)
    """Tax rate code for the item. `null` for untaxed amounts."""


class CreditCardTransactionAdjustedFeeBreakdown(BaseModel):
    items: List[CreditCardTransactionAdjustedFeeBreakdownItem] = FieldInfo(alias="Items")
    """Tax breakdown items per each tax rate applied."""


class CreditCardTransactionAdjustedFeeTaxValue(BaseModel):
    value: float = FieldInfo(alias="Value")
    """Amount of tax applied."""

    code: Optional[str] = FieldInfo(alias="Code", default=None)
    """Code corresponding to tax type."""


class CreditCardTransactionAdjustedFee(BaseModel):
    breakdown: CreditCardTransactionAdjustedFeeBreakdown = FieldInfo(alias="Breakdown")
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

    tax_values: List[CreditCardTransactionAdjustedFeeTaxValue] = FieldInfo(alias="TaxValues")
    """The tax values applied."""

    net: Optional[float] = FieldInfo(alias="Net", default=None)

    tax: Optional[float] = FieldInfo(alias="Tax", default=None)

    tax_rate: Optional[float] = FieldInfo(alias="TaxRate", default=None)

    value: Optional[float] = FieldInfo(alias="Value", default=None)


class CreditCardTransactionFeeBreakdownItem(BaseModel):
    net_value: float = FieldInfo(alias="NetValue")
    """The net value that the tax is calculated from."""

    tax_value: float = FieldInfo(alias="TaxValue")
    """The value of the tax."""

    tax_rate_code: Optional[str] = FieldInfo(alias="TaxRateCode", default=None)
    """Tax rate code for the item. `null` for untaxed amounts."""


class CreditCardTransactionFeeBreakdown(BaseModel):
    items: List[CreditCardTransactionFeeBreakdownItem] = FieldInfo(alias="Items")
    """Tax breakdown items per each tax rate applied."""


class CreditCardTransactionFeeTaxValue(BaseModel):
    value: float = FieldInfo(alias="Value")
    """Amount of tax applied."""

    code: Optional[str] = FieldInfo(alias="Code", default=None)
    """Code corresponding to tax type."""


class CreditCardTransactionFee(BaseModel):
    breakdown: CreditCardTransactionFeeBreakdown = FieldInfo(alias="Breakdown")
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

    tax_values: List[CreditCardTransactionFeeTaxValue] = FieldInfo(alias="TaxValues")
    """The tax values applied."""

    net: Optional[float] = FieldInfo(alias="Net", default=None)

    tax: Optional[float] = FieldInfo(alias="Tax", default=None)

    tax_rate: Optional[float] = FieldInfo(alias="TaxRate", default=None)

    value: Optional[float] = FieldInfo(alias="Value", default=None)


class CreditCardTransactionSettledAmountBreakdownItem(BaseModel):
    net_value: float = FieldInfo(alias="NetValue")
    """The net value that the tax is calculated from."""

    tax_value: float = FieldInfo(alias="TaxValue")
    """The value of the tax."""

    tax_rate_code: Optional[str] = FieldInfo(alias="TaxRateCode", default=None)
    """Tax rate code for the item. `null` for untaxed amounts."""


class CreditCardTransactionSettledAmountBreakdown(BaseModel):
    items: List[CreditCardTransactionSettledAmountBreakdownItem] = FieldInfo(alias="Items")
    """Tax breakdown items per each tax rate applied."""


class CreditCardTransactionSettledAmountTaxValue(BaseModel):
    value: float = FieldInfo(alias="Value")
    """Amount of tax applied."""

    code: Optional[str] = FieldInfo(alias="Code", default=None)
    """Code corresponding to tax type."""


class CreditCardTransactionSettledAmount(BaseModel):
    breakdown: CreditCardTransactionSettledAmountBreakdown = FieldInfo(alias="Breakdown")
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

    tax_values: List[CreditCardTransactionSettledAmountTaxValue] = FieldInfo(alias="TaxValues")
    """The tax values applied."""

    net: Optional[float] = FieldInfo(alias="Net", default=None)

    tax: Optional[float] = FieldInfo(alias="Tax", default=None)

    tax_rate: Optional[float] = FieldInfo(alias="TaxRate", default=None)

    value: Optional[float] = FieldInfo(alias="Value", default=None)


class CreditCardTransaction(BaseModel):
    charged_amount: CreditCardTransactionChargedAmount = FieldInfo(alias="ChargedAmount")

    payment_id: str = FieldInfo(alias="PaymentId")
    """Unique identifier of the `PaymentItem`."""

    adjusted_fee: Optional[CreditCardTransactionAdjustedFee] = FieldInfo(alias="AdjustedFee", default=None)

    fee: Optional[CreditCardTransactionFee] = FieldInfo(alias="Fee", default=None)

    settled_amount: Optional[CreditCardTransactionSettledAmount] = FieldInfo(alias="SettledAmount", default=None)

    settled_utc: Optional[datetime] = FieldInfo(alias="SettledUtc", default=None)
    """Settlement date and time in UTC timezone in ISO 8601 format."""

    settlement_id: Optional[str] = FieldInfo(alias="SettlementId", default=None)
    """Identifier of the settlement."""


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

    net: Optional[float] = FieldInfo(alias="Net", default=None)

    tax: Optional[float] = FieldInfo(alias="Tax", default=None)

    tax_rate: Optional[float] = FieldInfo(alias="TaxRate", default=None)

    value: Optional[float] = FieldInfo(alias="Value", default=None)


class OrderItemDataValueRebateOrderItemData(BaseModel):
    rebated_item_id: Optional[str] = FieldInfo(alias="RebatedItemId", default=None)


class OrderItemDataValueProductOrderItemData(BaseModel):
    age_category_id: Optional[str] = FieldInfo(alias="AgeCategoryId", default=None)

    product_id: Optional[str] = FieldInfo(alias="ProductId", default=None)


OrderItemDataValue: TypeAlias = Union[OrderItemDataValueRebateOrderItemData, OrderItemDataValueProductOrderItemData]


class OrderItemData(BaseModel):
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

    value: Optional[OrderItemDataValue] = None


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

    net: Optional[float] = FieldInfo(alias="Net", default=None)

    tax: Optional[float] = FieldInfo(alias="Tax", default=None)

    tax_rate: Optional[float] = FieldInfo(alias="TaxRate", default=None)

    value: Optional[float] = FieldInfo(alias="Value", default=None)


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


class OrderItem(BaseModel):
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

    amount: Optional[OrderItemAmount] = FieldInfo(alias="Amount", default=None)

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

    data: Optional[OrderItemData] = FieldInfo(alias="Data", default=None)
    """Additional data specific to particular order item."""

    id: Optional[str] = FieldInfo(alias="Id", default=None)
    """Unique identifier of the item."""

    order_id: Optional[str] = FieldInfo(alias="OrderId", default=None)
    """
    Unique identifier of the order (or
    [Reservation](https://mews-systems.gitbook.io/connector-api/operations/reservations/#reservation-ver-2023-06-06)
    which is a special type of order) the item belongs to.
    """

    original_amount: Optional[OrderItemOriginalAmount] = FieldInfo(alias="OriginalAmount", default=None)

    revenue_type: Optional[str] = FieldInfo(alias="RevenueType", default=None)
    """Revenue type of the item."""

    start_utc: Optional[date] = FieldInfo(alias="StartUtc", default=None)

    unit_amount: Optional[OrderItemUnitAmount] = FieldInfo(alias="UnitAmount", default=None)

    unit_count: Optional[int] = FieldInfo(alias="UnitCount", default=None)
    """Unit count of item, i.e. the number of sub-items or units, if applicable."""

    updated_utc: Optional[date] = FieldInfo(alias="UpdatedUtc", default=None)

    updater_profile_id: Optional[str] = FieldInfo(alias="UpdaterProfileId", default=None)


class PaymentItemAmountBreakdownItem(BaseModel):
    net_value: float = FieldInfo(alias="NetValue")
    """The net value that the tax is calculated from."""

    tax_value: float = FieldInfo(alias="TaxValue")
    """The value of the tax."""

    tax_rate_code: Optional[str] = FieldInfo(alias="TaxRateCode", default=None)
    """Tax rate code for the item. `null` for untaxed amounts."""


class PaymentItemAmountBreakdown(BaseModel):
    items: List[PaymentItemAmountBreakdownItem] = FieldInfo(alias="Items")
    """Tax breakdown items per each tax rate applied."""


class PaymentItemAmountTaxValue(BaseModel):
    value: float = FieldInfo(alias="Value")
    """Amount of tax applied."""

    code: Optional[str] = FieldInfo(alias="Code", default=None)
    """Code corresponding to tax type."""


class PaymentItemAmount(BaseModel):
    breakdown: PaymentItemAmountBreakdown = FieldInfo(alias="Breakdown")
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

    tax_values: List[PaymentItemAmountTaxValue] = FieldInfo(alias="TaxValues")
    """The tax values applied."""

    net: Optional[float] = FieldInfo(alias="Net", default=None)

    tax: Optional[float] = FieldInfo(alias="Tax", default=None)

    tax_rate: Optional[float] = FieldInfo(alias="TaxRate", default=None)

    value: Optional[float] = FieldInfo(alias="Value", default=None)


class PaymentItemAmountDefaultBreakdownItem(BaseModel):
    net_value: float = FieldInfo(alias="NetValue")
    """The net value that the tax is calculated from."""

    tax_value: float = FieldInfo(alias="TaxValue")
    """The value of the tax."""

    tax_rate_code: Optional[str] = FieldInfo(alias="TaxRateCode", default=None)
    """Tax rate code for the item. `null` for untaxed amounts."""


class PaymentItemAmountDefaultBreakdown(BaseModel):
    items: List[PaymentItemAmountDefaultBreakdownItem] = FieldInfo(alias="Items")
    """Tax breakdown items per each tax rate applied."""


class PaymentItemAmountDefaultTaxValue(BaseModel):
    value: float = FieldInfo(alias="Value")
    """Amount of tax applied."""

    code: Optional[str] = FieldInfo(alias="Code", default=None)
    """Code corresponding to tax type."""


class PaymentItemAmountDefault(BaseModel):
    breakdown: PaymentItemAmountDefaultBreakdown = FieldInfo(alias="Breakdown")
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

    tax_values: List[PaymentItemAmountDefaultTaxValue] = FieldInfo(alias="TaxValues")
    """The tax values applied."""

    net: Optional[float] = FieldInfo(alias="Net", default=None)

    tax: Optional[float] = FieldInfo(alias="Tax", default=None)

    tax_rate: Optional[float] = FieldInfo(alias="TaxRate", default=None)

    value: Optional[float] = FieldInfo(alias="Value", default=None)


class PaymentItemDataValuePaymentCardPaymentData(BaseModel):
    payment_card_id: Optional[str] = FieldInfo(alias="PaymentCardId", default=None)


class PaymentItemDataValueInvoicePaymentData(BaseModel):
    invoice_id: Optional[str] = FieldInfo(alias="InvoiceId", default=None)


PaymentItemDataValue: TypeAlias = Union[
    PaymentItemDataValuePaymentCardPaymentData, PaymentItemDataValueInvoicePaymentData
]


class PaymentItemData(BaseModel):
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

    value: Optional[PaymentItemDataValue] = None


class PaymentItemOriginalAmountBreakdownItem(BaseModel):
    net_value: float = FieldInfo(alias="NetValue")
    """The net value that the tax is calculated from."""

    tax_value: float = FieldInfo(alias="TaxValue")
    """The value of the tax."""

    tax_rate_code: Optional[str] = FieldInfo(alias="TaxRateCode", default=None)
    """Tax rate code for the item. `null` for untaxed amounts."""


class PaymentItemOriginalAmountBreakdown(BaseModel):
    items: List[PaymentItemOriginalAmountBreakdownItem] = FieldInfo(alias="Items")
    """Tax breakdown items per each tax rate applied."""


class PaymentItemOriginalAmountTaxValue(BaseModel):
    value: float = FieldInfo(alias="Value")
    """Amount of tax applied."""

    code: Optional[str] = FieldInfo(alias="Code", default=None)
    """Code corresponding to tax type."""


class PaymentItemOriginalAmount(BaseModel):
    breakdown: PaymentItemOriginalAmountBreakdown = FieldInfo(alias="Breakdown")
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

    tax_values: List[PaymentItemOriginalAmountTaxValue] = FieldInfo(alias="TaxValues")
    """The tax values applied."""

    net: Optional[float] = FieldInfo(alias="Net", default=None)

    tax: Optional[float] = FieldInfo(alias="Tax", default=None)

    tax_rate: Optional[float] = FieldInfo(alias="TaxRate", default=None)

    value: Optional[float] = FieldInfo(alias="Value", default=None)


class PaymentItem(BaseModel):
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

    amount: Optional[PaymentItemAmount] = FieldInfo(alias="Amount", default=None)

    amount_default: Optional[PaymentItemAmountDefault] = FieldInfo(alias="AmountDefault", default=None)

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

    data: Optional[PaymentItemData] = FieldInfo(alias="Data", default=None)
    """Additional data specific to particular payment item."""

    id: Optional[str] = FieldInfo(alias="Id", default=None)
    """Unique identifier of the item."""

    identifier: Optional[str] = FieldInfo(alias="Identifier", default=None)

    notes: Optional[str] = FieldInfo(alias="Notes", default=None)
    """Additional notes."""

    original_amount: Optional[PaymentItemOriginalAmount] = FieldInfo(alias="OriginalAmount", default=None)

    settlement_id: Optional[str] = FieldInfo(alias="SettlementId", default=None)
    """
    Identifier of the settled payment from the external system (ApplePay/GooglePay).
    """

    state: Optional[str] = FieldInfo(alias="State", default=None)
    """Payment state of the item."""


class AccountingItemResult(BaseModel):
    accounting_items: Optional[List[AccountingItem]] = FieldInfo(alias="AccountingItems", default=None)

    credit_card_transactions: Optional[List[CreditCardTransaction]] = FieldInfo(
        alias="CreditCardTransactions", default=None
    )
    """The credit card payment transactions."""

    order_items: Optional[List[OrderItem]] = FieldInfo(alias="OrderItems", default=None)
    """Updated order items (consumed items such as nights or products)."""

    payment_items: Optional[List[PaymentItem]] = FieldInfo(alias="PaymentItems", default=None)
    """Updated payment items (such as cash, credit card payments or invoices)."""
