# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import date, datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = [
    "BillUpdateResponse",
    "Bill",
    "BillOrderItem",
    "BillOrderItemAmount",
    "BillOrderItemAmountBreakdown",
    "BillOrderItemAmountBreakdownItem",
    "BillOrderItemAmountTaxValue",
    "BillOrderItemData",
    "BillOrderItemDataValue",
    "BillOrderItemDataValueRebateOrderItemData",
    "BillOrderItemDataValueProductOrderItemData",
    "BillOrderItemOriginalAmount",
    "BillOrderItemOriginalAmountBreakdown",
    "BillOrderItemOriginalAmountBreakdownItem",
    "BillOrderItemOriginalAmountTaxValue",
    "BillOrderItemUnitAmount",
    "BillOrderItemUnitAmountBreakdown",
    "BillOrderItemUnitAmountBreakdownItem",
    "BillOrderItemUnitAmountTaxValue",
    "BillPaymentItem",
    "BillPaymentItemAmount",
    "BillPaymentItemAmountBreakdown",
    "BillPaymentItemAmountBreakdownItem",
    "BillPaymentItemAmountTaxValue",
    "BillPaymentItemAmountDefault",
    "BillPaymentItemAmountDefaultBreakdown",
    "BillPaymentItemAmountDefaultBreakdownItem",
    "BillPaymentItemAmountDefaultTaxValue",
    "BillPaymentItemData",
    "BillPaymentItemDataValue",
    "BillPaymentItemDataValuePaymentCardPaymentData",
    "BillPaymentItemDataValueInvoicePaymentData",
    "BillPaymentItemOriginalAmount",
    "BillPaymentItemOriginalAmountBreakdown",
    "BillPaymentItemOriginalAmountBreakdownItem",
    "BillPaymentItemOriginalAmountTaxValue",
    "BillPayment",
    "BillPaymentAmount",
    "BillPaymentAmountBreakdown",
    "BillPaymentAmountBreakdownItem",
    "BillPaymentAmountTaxValue",
    "BillRevenue",
    "BillRevenueAmount",
    "BillRevenueAmountBreakdown",
    "BillRevenueAmountBreakdownItem",
    "BillRevenueAmountTaxValue",
    "BillAssigneeData",
    "BillAssigneeDataValue",
    "BillAssigneeDataValueBillCompanyData",
    "BillAssigneeDataValueBillCompanyDataAddress",
    "BillAssigneeDataValueBillCustomerData",
    "BillAssigneeDataValueBillCustomerDataAddress",
    "BillAssociatedAccountData",
    "BillAssociatedAccountDataBillCompanyData",
    "BillAssociatedAccountDataBillCompanyDataAddress",
    "BillAssociatedAccountDataBillCustomerData",
    "BillAssociatedAccountDataBillCustomerDataAddress",
    "BillCompanyDetails",
    "BillCompanyDetailsAddress",
    "BillEnterpriseData",
    "BillOptions",
    "BillOwnerData",
    "BillOwnerDataValue",
    "BillOwnerDataValueBillCompanyData",
    "BillOwnerDataValueBillCompanyDataAddress",
    "BillOwnerDataValueBillCustomerData",
    "BillOwnerDataValueBillCustomerDataAddress",
]


class BillOrderItemAmountBreakdownItem(BaseModel):
    net_value: float = FieldInfo(alias="NetValue")
    """The net value that the tax is calculated from."""

    tax_value: float = FieldInfo(alias="TaxValue")
    """The value of the tax."""

    tax_rate_code: Optional[str] = FieldInfo(alias="TaxRateCode", default=None)
    """Tax rate code for the item. `null` for untaxed amounts."""


class BillOrderItemAmountBreakdown(BaseModel):
    items: List[BillOrderItemAmountBreakdownItem] = FieldInfo(alias="Items")
    """Tax breakdown items per each tax rate applied."""


class BillOrderItemAmountTaxValue(BaseModel):
    value: float = FieldInfo(alias="Value")
    """Amount of tax applied."""

    code: Optional[str] = FieldInfo(alias="Code", default=None)
    """Code corresponding to tax type."""


class BillOrderItemAmount(BaseModel):
    breakdown: BillOrderItemAmountBreakdown = FieldInfo(alias="Breakdown")
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

    tax_values: List[BillOrderItemAmountTaxValue] = FieldInfo(alias="TaxValues")
    """The tax values applied."""

    net: Optional[float] = FieldInfo(alias="Net", default=None)

    tax: Optional[float] = FieldInfo(alias="Tax", default=None)

    tax_rate: Optional[float] = FieldInfo(alias="TaxRate", default=None)

    value: Optional[float] = FieldInfo(alias="Value", default=None)


class BillOrderItemDataValueRebateOrderItemData(BaseModel):
    rebated_item_id: Optional[str] = FieldInfo(alias="RebatedItemId", default=None)


class BillOrderItemDataValueProductOrderItemData(BaseModel):
    age_category_id: Optional[str] = FieldInfo(alias="AgeCategoryId", default=None)

    product_id: Optional[str] = FieldInfo(alias="ProductId", default=None)


BillOrderItemDataValue: TypeAlias = Union[
    BillOrderItemDataValueRebateOrderItemData, BillOrderItemDataValueProductOrderItemData
]


class BillOrderItemData(BaseModel):
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

    value: Optional[BillOrderItemDataValue] = None


class BillOrderItemOriginalAmountBreakdownItem(BaseModel):
    net_value: float = FieldInfo(alias="NetValue")
    """The net value that the tax is calculated from."""

    tax_value: float = FieldInfo(alias="TaxValue")
    """The value of the tax."""

    tax_rate_code: Optional[str] = FieldInfo(alias="TaxRateCode", default=None)
    """Tax rate code for the item. `null` for untaxed amounts."""


class BillOrderItemOriginalAmountBreakdown(BaseModel):
    items: List[BillOrderItemOriginalAmountBreakdownItem] = FieldInfo(alias="Items")
    """Tax breakdown items per each tax rate applied."""


class BillOrderItemOriginalAmountTaxValue(BaseModel):
    value: float = FieldInfo(alias="Value")
    """Amount of tax applied."""

    code: Optional[str] = FieldInfo(alias="Code", default=None)
    """Code corresponding to tax type."""


class BillOrderItemOriginalAmount(BaseModel):
    breakdown: BillOrderItemOriginalAmountBreakdown = FieldInfo(alias="Breakdown")
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

    tax_values: List[BillOrderItemOriginalAmountTaxValue] = FieldInfo(alias="TaxValues")
    """The tax values applied."""

    net: Optional[float] = FieldInfo(alias="Net", default=None)

    tax: Optional[float] = FieldInfo(alias="Tax", default=None)

    tax_rate: Optional[float] = FieldInfo(alias="TaxRate", default=None)

    value: Optional[float] = FieldInfo(alias="Value", default=None)


class BillOrderItemUnitAmountBreakdownItem(BaseModel):
    net_value: float = FieldInfo(alias="NetValue")
    """The net value that the tax is calculated from."""

    tax_value: float = FieldInfo(alias="TaxValue")
    """The value of the tax."""

    tax_rate_code: Optional[str] = FieldInfo(alias="TaxRateCode", default=None)
    """Tax rate code for the item. `null` for untaxed amounts."""


class BillOrderItemUnitAmountBreakdown(BaseModel):
    items: List[BillOrderItemUnitAmountBreakdownItem] = FieldInfo(alias="Items")
    """Tax breakdown items per each tax rate applied."""


class BillOrderItemUnitAmountTaxValue(BaseModel):
    value: float = FieldInfo(alias="Value")
    """Amount of tax applied."""

    code: Optional[str] = FieldInfo(alias="Code", default=None)
    """Code corresponding to tax type."""


class BillOrderItemUnitAmount(BaseModel):
    breakdown: BillOrderItemUnitAmountBreakdown = FieldInfo(alias="Breakdown")
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

    tax_values: List[BillOrderItemUnitAmountTaxValue] = FieldInfo(alias="TaxValues")
    """The tax values applied."""


class BillOrderItem(BaseModel):
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

    amount: Optional[BillOrderItemAmount] = FieldInfo(alias="Amount", default=None)

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

    data: Optional[BillOrderItemData] = FieldInfo(alias="Data", default=None)
    """Additional data specific to particular order item."""

    id: Optional[str] = FieldInfo(alias="Id", default=None)
    """Unique identifier of the item."""

    order_id: Optional[str] = FieldInfo(alias="OrderId", default=None)
    """
    Unique identifier of the order (or
    [Reservation](https://mews-systems.gitbook.io/connector-api/operations/reservations/#reservation-ver-2023-06-06)
    which is a special type of order) the item belongs to.
    """

    original_amount: Optional[BillOrderItemOriginalAmount] = FieldInfo(alias="OriginalAmount", default=None)

    revenue_type: Optional[str] = FieldInfo(alias="RevenueType", default=None)
    """Revenue type of the item."""

    start_utc: Optional[date] = FieldInfo(alias="StartUtc", default=None)

    unit_amount: Optional[BillOrderItemUnitAmount] = FieldInfo(alias="UnitAmount", default=None)

    unit_count: Optional[int] = FieldInfo(alias="UnitCount", default=None)
    """Unit count of item, i.e. the number of sub-items or units, if applicable."""

    updated_utc: Optional[date] = FieldInfo(alias="UpdatedUtc", default=None)

    updater_profile_id: Optional[str] = FieldInfo(alias="UpdaterProfileId", default=None)


class BillPaymentItemAmountBreakdownItem(BaseModel):
    net_value: float = FieldInfo(alias="NetValue")
    """The net value that the tax is calculated from."""

    tax_value: float = FieldInfo(alias="TaxValue")
    """The value of the tax."""

    tax_rate_code: Optional[str] = FieldInfo(alias="TaxRateCode", default=None)
    """Tax rate code for the item. `null` for untaxed amounts."""


class BillPaymentItemAmountBreakdown(BaseModel):
    items: List[BillPaymentItemAmountBreakdownItem] = FieldInfo(alias="Items")
    """Tax breakdown items per each tax rate applied."""


class BillPaymentItemAmountTaxValue(BaseModel):
    value: float = FieldInfo(alias="Value")
    """Amount of tax applied."""

    code: Optional[str] = FieldInfo(alias="Code", default=None)
    """Code corresponding to tax type."""


class BillPaymentItemAmount(BaseModel):
    breakdown: BillPaymentItemAmountBreakdown = FieldInfo(alias="Breakdown")
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

    tax_values: List[BillPaymentItemAmountTaxValue] = FieldInfo(alias="TaxValues")
    """The tax values applied."""

    net: Optional[float] = FieldInfo(alias="Net", default=None)

    tax: Optional[float] = FieldInfo(alias="Tax", default=None)

    tax_rate: Optional[float] = FieldInfo(alias="TaxRate", default=None)

    value: Optional[float] = FieldInfo(alias="Value", default=None)


class BillPaymentItemAmountDefaultBreakdownItem(BaseModel):
    net_value: float = FieldInfo(alias="NetValue")
    """The net value that the tax is calculated from."""

    tax_value: float = FieldInfo(alias="TaxValue")
    """The value of the tax."""

    tax_rate_code: Optional[str] = FieldInfo(alias="TaxRateCode", default=None)
    """Tax rate code for the item. `null` for untaxed amounts."""


class BillPaymentItemAmountDefaultBreakdown(BaseModel):
    items: List[BillPaymentItemAmountDefaultBreakdownItem] = FieldInfo(alias="Items")
    """Tax breakdown items per each tax rate applied."""


class BillPaymentItemAmountDefaultTaxValue(BaseModel):
    value: float = FieldInfo(alias="Value")
    """Amount of tax applied."""

    code: Optional[str] = FieldInfo(alias="Code", default=None)
    """Code corresponding to tax type."""


class BillPaymentItemAmountDefault(BaseModel):
    breakdown: BillPaymentItemAmountDefaultBreakdown = FieldInfo(alias="Breakdown")
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

    tax_values: List[BillPaymentItemAmountDefaultTaxValue] = FieldInfo(alias="TaxValues")
    """The tax values applied."""

    net: Optional[float] = FieldInfo(alias="Net", default=None)

    tax: Optional[float] = FieldInfo(alias="Tax", default=None)

    tax_rate: Optional[float] = FieldInfo(alias="TaxRate", default=None)

    value: Optional[float] = FieldInfo(alias="Value", default=None)


class BillPaymentItemDataValuePaymentCardPaymentData(BaseModel):
    payment_card_id: Optional[str] = FieldInfo(alias="PaymentCardId", default=None)


class BillPaymentItemDataValueInvoicePaymentData(BaseModel):
    invoice_id: Optional[str] = FieldInfo(alias="InvoiceId", default=None)


BillPaymentItemDataValue: TypeAlias = Union[
    BillPaymentItemDataValuePaymentCardPaymentData, BillPaymentItemDataValueInvoicePaymentData
]


class BillPaymentItemData(BaseModel):
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

    value: Optional[BillPaymentItemDataValue] = None


class BillPaymentItemOriginalAmountBreakdownItem(BaseModel):
    net_value: float = FieldInfo(alias="NetValue")
    """The net value that the tax is calculated from."""

    tax_value: float = FieldInfo(alias="TaxValue")
    """The value of the tax."""

    tax_rate_code: Optional[str] = FieldInfo(alias="TaxRateCode", default=None)
    """Tax rate code for the item. `null` for untaxed amounts."""


class BillPaymentItemOriginalAmountBreakdown(BaseModel):
    items: List[BillPaymentItemOriginalAmountBreakdownItem] = FieldInfo(alias="Items")
    """Tax breakdown items per each tax rate applied."""


class BillPaymentItemOriginalAmountTaxValue(BaseModel):
    value: float = FieldInfo(alias="Value")
    """Amount of tax applied."""

    code: Optional[str] = FieldInfo(alias="Code", default=None)
    """Code corresponding to tax type."""


class BillPaymentItemOriginalAmount(BaseModel):
    breakdown: BillPaymentItemOriginalAmountBreakdown = FieldInfo(alias="Breakdown")
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

    tax_values: List[BillPaymentItemOriginalAmountTaxValue] = FieldInfo(alias="TaxValues")
    """The tax values applied."""

    net: Optional[float] = FieldInfo(alias="Net", default=None)

    tax: Optional[float] = FieldInfo(alias="Tax", default=None)

    tax_rate: Optional[float] = FieldInfo(alias="TaxRate", default=None)

    value: Optional[float] = FieldInfo(alias="Value", default=None)


class BillPaymentItem(BaseModel):
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

    amount: Optional[BillPaymentItemAmount] = FieldInfo(alias="Amount", default=None)

    amount_default: Optional[BillPaymentItemAmountDefault] = FieldInfo(alias="AmountDefault", default=None)

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

    data: Optional[BillPaymentItemData] = FieldInfo(alias="Data", default=None)
    """Additional data specific to particular payment item."""

    id: Optional[str] = FieldInfo(alias="Id", default=None)
    """Unique identifier of the item."""

    identifier: Optional[str] = FieldInfo(alias="Identifier", default=None)

    notes: Optional[str] = FieldInfo(alias="Notes", default=None)
    """Additional notes."""

    original_amount: Optional[BillPaymentItemOriginalAmount] = FieldInfo(alias="OriginalAmount", default=None)

    settlement_id: Optional[str] = FieldInfo(alias="SettlementId", default=None)
    """
    Identifier of the settled payment from the external system (ApplePay/GooglePay).
    """

    state: Optional[str] = FieldInfo(alias="State", default=None)
    """Payment state of the item."""


class BillPaymentAmountBreakdownItem(BaseModel):
    net_value: float = FieldInfo(alias="NetValue")
    """The net value that the tax is calculated from."""

    tax_value: float = FieldInfo(alias="TaxValue")
    """The value of the tax."""

    tax_rate_code: Optional[str] = FieldInfo(alias="TaxRateCode", default=None)
    """Tax rate code for the item. `null` for untaxed amounts."""


class BillPaymentAmountBreakdown(BaseModel):
    items: List[BillPaymentAmountBreakdownItem] = FieldInfo(alias="Items")
    """Tax breakdown items per each tax rate applied."""


class BillPaymentAmountTaxValue(BaseModel):
    value: float = FieldInfo(alias="Value")
    """Amount of tax applied."""

    code: Optional[str] = FieldInfo(alias="Code", default=None)
    """Code corresponding to tax type."""


class BillPaymentAmount(BaseModel):
    breakdown: BillPaymentAmountBreakdown = FieldInfo(alias="Breakdown")
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

    tax_values: List[BillPaymentAmountTaxValue] = FieldInfo(alias="TaxValues")
    """The tax values applied."""

    net: Optional[float] = FieldInfo(alias="Net", default=None)

    tax: Optional[float] = FieldInfo(alias="Tax", default=None)

    tax_rate: Optional[float] = FieldInfo(alias="TaxRate", default=None)

    value: Optional[float] = FieldInfo(alias="Value", default=None)


class BillPayment(BaseModel):
    account_id: Optional[str] = FieldInfo(alias="AccountId", default=None)

    accounting_category_id: Optional[str] = FieldInfo(alias="AccountingCategoryId", default=None)

    amount: Optional[BillPaymentAmount] = FieldInfo(alias="Amount", default=None)

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


class BillRevenueAmountBreakdownItem(BaseModel):
    net_value: float = FieldInfo(alias="NetValue")
    """The net value that the tax is calculated from."""

    tax_value: float = FieldInfo(alias="TaxValue")
    """The value of the tax."""

    tax_rate_code: Optional[str] = FieldInfo(alias="TaxRateCode", default=None)
    """Tax rate code for the item. `null` for untaxed amounts."""


class BillRevenueAmountBreakdown(BaseModel):
    items: List[BillRevenueAmountBreakdownItem] = FieldInfo(alias="Items")
    """Tax breakdown items per each tax rate applied."""


class BillRevenueAmountTaxValue(BaseModel):
    value: float = FieldInfo(alias="Value")
    """Amount of tax applied."""

    code: Optional[str] = FieldInfo(alias="Code", default=None)
    """Code corresponding to tax type."""


class BillRevenueAmount(BaseModel):
    breakdown: BillRevenueAmountBreakdown = FieldInfo(alias="Breakdown")
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

    tax_values: List[BillRevenueAmountTaxValue] = FieldInfo(alias="TaxValues")
    """The tax values applied."""

    net: Optional[float] = FieldInfo(alias="Net", default=None)

    tax: Optional[float] = FieldInfo(alias="Tax", default=None)

    tax_rate: Optional[float] = FieldInfo(alias="TaxRate", default=None)

    value: Optional[float] = FieldInfo(alias="Value", default=None)


class BillRevenue(BaseModel):
    account_id: Optional[str] = FieldInfo(alias="AccountId", default=None)

    accounting_category_id: Optional[str] = FieldInfo(alias="AccountingCategoryId", default=None)

    amount: Optional[BillRevenueAmount] = FieldInfo(alias="Amount", default=None)

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


class BillAssigneeDataValueBillCompanyDataAddress(BaseModel):
    city: Optional[str] = FieldInfo(alias="City", default=None)

    country_code: Optional[str] = FieldInfo(alias="CountryCode", default=None)

    line1: Optional[str] = FieldInfo(alias="Line1", default=None)

    line2: Optional[str] = FieldInfo(alias="Line2", default=None)

    postal_code: Optional[str] = FieldInfo(alias="PostalCode", default=None)

    subdivision_code: Optional[str] = FieldInfo(alias="SubdivisionCode", default=None)


class BillAssigneeDataValueBillCompanyData(BaseModel):
    id: Optional[str] = FieldInfo(alias="Id", default=None)
    """ID of the `Company`."""

    name: str = FieldInfo(alias="Name")
    """Name of the company."""

    additional_tax_identifier: Optional[str] = FieldInfo(alias="AdditionalTaxIdentifier", default=None)
    """Additional tax identifier of the company."""

    address: Optional[BillAssigneeDataValueBillCompanyDataAddress] = FieldInfo(alias="Address", default=None)
    """Address of the company."""

    billing_code: Optional[str] = FieldInfo(alias="BillingCode", default=None)
    """A unique code for Mews to list on invoices it sends to the company."""

    department: Optional[str] = FieldInfo(alias="Department", default=None)
    """Department of the company."""

    duns: Optional[str] = FieldInfo(alias="DUNS", default=None)
    """DUNS of the company."""

    fiscal_identifier: Optional[str] = FieldInfo(alias="FiscalIdentifier", default=None)
    """Fiscal identifier of the company."""

    invoicing_email: Optional[str] = FieldInfo(alias="InvoicingEmail", default=None)
    """Invoicing email of the company."""

    legal_identifiers: Optional[Dict[str, str]] = FieldInfo(alias="LegalIdentifiers", default=None)
    """The set of `LegalIdentifiers` for the company."""

    tax_identifier: Optional[str] = FieldInfo(alias="TaxIdentifier", default=None)
    """Tax identifier of the company."""

    telephone: Optional[str] = FieldInfo(alias="Telephone", default=None)
    """Company telephone number."""


class BillAssigneeDataValueBillCustomerDataAddress(BaseModel):
    city: Optional[str] = FieldInfo(alias="City", default=None)

    country_code: Optional[str] = FieldInfo(alias="CountryCode", default=None)

    line1: Optional[str] = FieldInfo(alias="Line1", default=None)

    line2: Optional[str] = FieldInfo(alias="Line2", default=None)

    postal_code: Optional[str] = FieldInfo(alias="PostalCode", default=None)

    subdivision_code: Optional[str] = FieldInfo(alias="SubdivisionCode", default=None)


class BillAssigneeDataValueBillCustomerData(BaseModel):
    id: str = FieldInfo(alias="Id")
    """ID of the `Customer` to whom the bill was assigned."""

    last_name: str = FieldInfo(alias="LastName")
    """Last name of the customer."""

    address: Optional[BillAssigneeDataValueBillCustomerDataAddress] = FieldInfo(alias="Address", default=None)
    """Address of the customer."""

    billing_code: Optional[str] = FieldInfo(alias="BillingCode", default=None)
    """A unique code for Mews to list on invoices it sends to the customer."""

    first_name: Optional[str] = FieldInfo(alias="FirstName", default=None)
    """First name of the customer."""

    legal_identifiers: Optional[Dict[str, str]] = FieldInfo(alias="LegalIdentifiers", default=None)
    """The set of `LegalIdentifiers` for the customer."""

    second_last_name: Optional[str] = FieldInfo(alias="SecondLastName", default=None)
    """Second last name of the customer."""

    title_prefix: Optional[Literal["Mister", "Miss", "Misses"]] = FieldInfo(alias="TitlePrefix", default=None)
    """Type of the title prefix of the customer.

    Note that the value should not be used as-is, but localized. For example, the
    value `Misses` should be displayed as `Mrs.` in English and `Fr.` in German.

    Mister (Mr.)

    Miss (Ms.)

    Misses (Mrs.)

    - `Mister` - Mr.
    - `Miss` - Ms.
    - `Misses` - Mrs.
    """


BillAssigneeDataValue: TypeAlias = Union[BillAssigneeDataValueBillCompanyData, BillAssigneeDataValueBillCustomerData]


class BillAssigneeData(BaseModel):
    discriminator: Optional[Literal["BillCustomerData", "BillCompanyData"]] = None

    value: Optional[BillAssigneeDataValue] = None


class BillAssociatedAccountDataBillCompanyDataAddress(BaseModel):
    city: Optional[str] = FieldInfo(alias="City", default=None)

    country_code: Optional[str] = FieldInfo(alias="CountryCode", default=None)

    line1: Optional[str] = FieldInfo(alias="Line1", default=None)

    line2: Optional[str] = FieldInfo(alias="Line2", default=None)

    postal_code: Optional[str] = FieldInfo(alias="PostalCode", default=None)

    subdivision_code: Optional[str] = FieldInfo(alias="SubdivisionCode", default=None)


class BillAssociatedAccountDataBillCompanyData(BaseModel):
    id: Optional[str] = FieldInfo(alias="Id", default=None)
    """ID of the `Company`."""

    name: str = FieldInfo(alias="Name")
    """Name of the company."""

    additional_tax_identifier: Optional[str] = FieldInfo(alias="AdditionalTaxIdentifier", default=None)
    """Additional tax identifier of the company."""

    address: Optional[BillAssociatedAccountDataBillCompanyDataAddress] = FieldInfo(alias="Address", default=None)
    """Address of the company."""

    billing_code: Optional[str] = FieldInfo(alias="BillingCode", default=None)
    """A unique code for Mews to list on invoices it sends to the company."""

    department: Optional[str] = FieldInfo(alias="Department", default=None)
    """Department of the company."""

    duns: Optional[str] = FieldInfo(alias="DUNS", default=None)
    """DUNS of the company."""

    fiscal_identifier: Optional[str] = FieldInfo(alias="FiscalIdentifier", default=None)
    """Fiscal identifier of the company."""

    invoicing_email: Optional[str] = FieldInfo(alias="InvoicingEmail", default=None)
    """Invoicing email of the company."""

    legal_identifiers: Optional[Dict[str, str]] = FieldInfo(alias="LegalIdentifiers", default=None)
    """The set of `LegalIdentifiers` for the company."""

    tax_identifier: Optional[str] = FieldInfo(alias="TaxIdentifier", default=None)
    """Tax identifier of the company."""

    telephone: Optional[str] = FieldInfo(alias="Telephone", default=None)
    """Company telephone number."""


class BillAssociatedAccountDataBillCustomerDataAddress(BaseModel):
    city: Optional[str] = FieldInfo(alias="City", default=None)

    country_code: Optional[str] = FieldInfo(alias="CountryCode", default=None)

    line1: Optional[str] = FieldInfo(alias="Line1", default=None)

    line2: Optional[str] = FieldInfo(alias="Line2", default=None)

    postal_code: Optional[str] = FieldInfo(alias="PostalCode", default=None)

    subdivision_code: Optional[str] = FieldInfo(alias="SubdivisionCode", default=None)


class BillAssociatedAccountDataBillCustomerData(BaseModel):
    id: str = FieldInfo(alias="Id")
    """ID of the `Customer` to whom the bill was assigned."""

    last_name: str = FieldInfo(alias="LastName")
    """Last name of the customer."""

    address: Optional[BillAssociatedAccountDataBillCustomerDataAddress] = FieldInfo(alias="Address", default=None)
    """Address of the customer."""

    billing_code: Optional[str] = FieldInfo(alias="BillingCode", default=None)
    """A unique code for Mews to list on invoices it sends to the customer."""

    first_name: Optional[str] = FieldInfo(alias="FirstName", default=None)
    """First name of the customer."""

    legal_identifiers: Optional[Dict[str, str]] = FieldInfo(alias="LegalIdentifiers", default=None)
    """The set of `LegalIdentifiers` for the customer."""

    second_last_name: Optional[str] = FieldInfo(alias="SecondLastName", default=None)
    """Second last name of the customer."""

    title_prefix: Optional[Literal["Mister", "Miss", "Misses"]] = FieldInfo(alias="TitlePrefix", default=None)
    """Type of the title prefix of the customer.

    Note that the value should not be used as-is, but localized. For example, the
    value `Misses` should be displayed as `Mrs.` in English and `Fr.` in German.

    Mister (Mr.)

    Miss (Ms.)

    Misses (Mrs.)

    - `Mister` - Mr.
    - `Miss` - Ms.
    - `Misses` - Mrs.
    """


class BillAssociatedAccountData(BaseModel):
    bill_company_data: Optional[BillAssociatedAccountDataBillCompanyData] = FieldInfo(
        alias="BillCompanyData", default=None
    )

    bill_customer_data: Optional[BillAssociatedAccountDataBillCustomerData] = FieldInfo(
        alias="BillCustomerData", default=None
    )
    """Associated account bill data for customer."""

    discriminator: Optional[Literal["BillCustomerData", "BillCompanyData"]] = FieldInfo(
        alias="Discriminator", default=None
    )


class BillCompanyDetailsAddress(BaseModel):
    city: Optional[str] = FieldInfo(alias="City", default=None)

    country_code: Optional[str] = FieldInfo(alias="CountryCode", default=None)

    line1: Optional[str] = FieldInfo(alias="Line1", default=None)

    line2: Optional[str] = FieldInfo(alias="Line2", default=None)

    postal_code: Optional[str] = FieldInfo(alias="PostalCode", default=None)

    subdivision_code: Optional[str] = FieldInfo(alias="SubdivisionCode", default=None)


class BillCompanyDetails(BaseModel):
    id: Optional[str] = FieldInfo(alias="Id", default=None)
    """ID of the `Company`."""

    name: str = FieldInfo(alias="Name")
    """Name of the company."""

    additional_tax_identifier: Optional[str] = FieldInfo(alias="AdditionalTaxIdentifier", default=None)
    """Additional tax identifier of the company."""

    address: Optional[BillCompanyDetailsAddress] = FieldInfo(alias="Address", default=None)
    """Address of the company."""

    billing_code: Optional[str] = FieldInfo(alias="BillingCode", default=None)
    """A unique code for Mews to list on invoices it sends to the company."""

    department: Optional[str] = FieldInfo(alias="Department", default=None)
    """Department of the company."""

    duns: Optional[str] = FieldInfo(alias="DUNS", default=None)
    """DUNS of the company."""

    fiscal_identifier: Optional[str] = FieldInfo(alias="FiscalIdentifier", default=None)
    """Fiscal identifier of the company."""

    invoicing_email: Optional[str] = FieldInfo(alias="InvoicingEmail", default=None)
    """Invoicing email of the company."""

    legal_identifiers: Optional[Dict[str, str]] = FieldInfo(alias="LegalIdentifiers", default=None)
    """The set of `LegalIdentifiers` for the company."""

    tax_identifier: Optional[str] = FieldInfo(alias="TaxIdentifier", default=None)
    """Tax identifier of the company."""

    telephone: Optional[str] = FieldInfo(alias="Telephone", default=None)
    """Company telephone number."""


class BillEnterpriseData(BaseModel):
    additional_tax_identifier: Optional[str] = FieldInfo(alias="AdditionalTaxIdentifier", default=None)
    """Enterprise additional tax identifier."""

    bank_account: Optional[str] = FieldInfo(alias="BankAccount", default=None)
    """Enterprise bank account."""

    bank_name: Optional[str] = FieldInfo(alias="BankName", default=None)
    """Enterprise bank name."""

    bic: Optional[str] = FieldInfo(alias="Bic", default=None)
    """Enterprise BIC (Bank Identifier Code)."""

    company_name: Optional[str] = FieldInfo(alias="CompanyName", default=None)
    """Enterprise company name."""

    iban: Optional[str] = FieldInfo(alias="Iban", default=None)
    """Enterprise IBAN (International Bank Account Number)."""


class BillOptions(BaseModel):
    display_cid: Optional[bool] = FieldInfo(alias="DisplayCid", default=None)
    """Display CID number on bill, only applicable for `BillType` of `Invoice`."""

    display_customer: Optional[bool] = FieldInfo(alias="DisplayCustomer", default=None)
    """Display customer information on a bill."""

    display_taxation: Optional[bool] = FieldInfo(alias="DisplayTaxation", default=None)
    """Display taxation detail on a bill."""

    rebated: Optional[bool] = FieldInfo(alias="Rebated", default=None)
    """Whether the bill is rebated (both fully or partially)."""

    track_receivable: Optional[bool] = FieldInfo(alias="TrackReceivable", default=None)
    """
    Tracking of payments is enabled for bill, only applicable for `BillType` of
    `Invoice`.
    """


class BillOwnerDataValueBillCompanyDataAddress(BaseModel):
    city: Optional[str] = FieldInfo(alias="City", default=None)

    country_code: Optional[str] = FieldInfo(alias="CountryCode", default=None)

    line1: Optional[str] = FieldInfo(alias="Line1", default=None)

    line2: Optional[str] = FieldInfo(alias="Line2", default=None)

    postal_code: Optional[str] = FieldInfo(alias="PostalCode", default=None)

    subdivision_code: Optional[str] = FieldInfo(alias="SubdivisionCode", default=None)


class BillOwnerDataValueBillCompanyData(BaseModel):
    id: Optional[str] = FieldInfo(alias="Id", default=None)
    """ID of the `Company`."""

    name: str = FieldInfo(alias="Name")
    """Name of the company."""

    additional_tax_identifier: Optional[str] = FieldInfo(alias="AdditionalTaxIdentifier", default=None)
    """Additional tax identifier of the company."""

    address: Optional[BillOwnerDataValueBillCompanyDataAddress] = FieldInfo(alias="Address", default=None)
    """Address of the company."""

    billing_code: Optional[str] = FieldInfo(alias="BillingCode", default=None)
    """A unique code for Mews to list on invoices it sends to the company."""

    department: Optional[str] = FieldInfo(alias="Department", default=None)
    """Department of the company."""

    duns: Optional[str] = FieldInfo(alias="DUNS", default=None)
    """DUNS of the company."""

    fiscal_identifier: Optional[str] = FieldInfo(alias="FiscalIdentifier", default=None)
    """Fiscal identifier of the company."""

    invoicing_email: Optional[str] = FieldInfo(alias="InvoicingEmail", default=None)
    """Invoicing email of the company."""

    legal_identifiers: Optional[Dict[str, str]] = FieldInfo(alias="LegalIdentifiers", default=None)
    """The set of `LegalIdentifiers` for the company."""

    tax_identifier: Optional[str] = FieldInfo(alias="TaxIdentifier", default=None)
    """Tax identifier of the company."""

    telephone: Optional[str] = FieldInfo(alias="Telephone", default=None)
    """Company telephone number."""


class BillOwnerDataValueBillCustomerDataAddress(BaseModel):
    city: Optional[str] = FieldInfo(alias="City", default=None)

    country_code: Optional[str] = FieldInfo(alias="CountryCode", default=None)

    line1: Optional[str] = FieldInfo(alias="Line1", default=None)

    line2: Optional[str] = FieldInfo(alias="Line2", default=None)

    postal_code: Optional[str] = FieldInfo(alias="PostalCode", default=None)

    subdivision_code: Optional[str] = FieldInfo(alias="SubdivisionCode", default=None)


class BillOwnerDataValueBillCustomerData(BaseModel):
    id: str = FieldInfo(alias="Id")
    """ID of the `Customer` to whom the bill was assigned."""

    last_name: str = FieldInfo(alias="LastName")
    """Last name of the customer."""

    address: Optional[BillOwnerDataValueBillCustomerDataAddress] = FieldInfo(alias="Address", default=None)
    """Address of the customer."""

    billing_code: Optional[str] = FieldInfo(alias="BillingCode", default=None)
    """A unique code for Mews to list on invoices it sends to the customer."""

    first_name: Optional[str] = FieldInfo(alias="FirstName", default=None)
    """First name of the customer."""

    legal_identifiers: Optional[Dict[str, str]] = FieldInfo(alias="LegalIdentifiers", default=None)
    """The set of `LegalIdentifiers` for the customer."""

    second_last_name: Optional[str] = FieldInfo(alias="SecondLastName", default=None)
    """Second last name of the customer."""

    title_prefix: Optional[Literal["Mister", "Miss", "Misses"]] = FieldInfo(alias="TitlePrefix", default=None)
    """Type of the title prefix of the customer.

    Note that the value should not be used as-is, but localized. For example, the
    value `Misses` should be displayed as `Mrs.` in English and `Fr.` in German.

    Mister (Mr.)

    Miss (Ms.)

    Misses (Mrs.)

    - `Mister` - Mr.
    - `Miss` - Ms.
    - `Misses` - Mrs.
    """


BillOwnerDataValue: TypeAlias = Union[BillOwnerDataValueBillCompanyData, BillOwnerDataValueBillCustomerData]


class BillOwnerData(BaseModel):
    discriminator: Optional[Literal["BillCustomerData", "BillCompanyData"]] = None

    value: Optional[BillOwnerDataValue] = None


class Bill(BaseModel):
    account_id: str = FieldInfo(alias="AccountId")
    """
    Unique identifier of the account (`Customer` or `Company`) the bill is issued
    to.
    """

    associated_account_ids: Optional[List[str]] = FieldInfo(alias="AssociatedAccountIds", default=None)
    """
    Unique identifiers of the `Customers` or `Companies` that are associated to the
    bill.
    """

    correction_state: Literal["Bill", "CorrectiveBill"] = FieldInfo(alias="CorrectionState")
    """Bill (Regular bill.)

    CorrectiveBill (Corrective bill, i.e. the `CorrectionType` is either `Edit`,
    `Cancellation`, or `ReceivablePaymentsBalance`.)

    - `Bill` - Regular bill.
    - `CorrectiveBill` - Corrective bill, i.e. the `CorrectionType` is either
      `Edit`, `Cancellation`, or `ReceivablePaymentsBalance`.
    """

    created_utc: datetime = FieldInfo(alias="CreatedUtc")
    """Date and time of the bill creation in UTC timezone in ISO 8601 format."""

    enterprise_id: str = FieldInfo(alias="EnterpriseId")
    """Unique identifier of the `Enterprise`."""

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the bill."""

    order_items: Optional[List[BillOrderItem]] = FieldInfo(alias="OrderItems", default=None)
    """The order items (consumed items such as nights or products) on the bill."""

    payment_items: Optional[List[BillPaymentItem]] = FieldInfo(alias="PaymentItems", default=None)
    """The payment items (such as cash, credit card payments or invoices) on the bill."""

    payments: Optional[List[BillPayment]] = FieldInfo(alias="Payments", default=None)

    revenue: Optional[List[BillRevenue]] = FieldInfo(alias="Revenue", default=None)

    state: Literal["Open", "Closed"] = FieldInfo(alias="State")
    """Whether the bill is `Open` or `Closed`."""

    type: Literal["Receipt", "Invoice"] = FieldInfo(alias="Type")
    """After a bill is closed, the Bill Type is set to `Receipt` or `Invoice`.

    `Receipt` indicates that the bill has been fully paid and the balance is zero.
    `Invoice` indicates that the bill has not yet been fully paid but an invoice has
    been issued. Prior to closing, Bill Type should not be used.

    - `Receipt` - Default; the bill has been paid in full; only applicable after the
      bill is closed.
    - `Invoice` - Bill has not been paid in full but an invoice has been issued to
      request payment.
    """

    updated_utc: datetime = FieldInfo(alias="UpdatedUtc")
    """
    Date and time when the bill was last updated, in UTC timezone in ISO 8601
    format.
    """

    assignee_data: Optional[BillAssigneeData] = FieldInfo(alias="AssigneeData", default=None)

    associated_account_data: Optional[List[BillAssociatedAccountData]] = FieldInfo(
        alias="AssociatedAccountData", default=None
    )
    """Additional information about the associated account of the bill.

    Can be a `Customer` or `Company`. Persisted at the time of closing of the bill.
    Currently only one account can be associated with a bill, but this may be
    extended in future.
    """

    company_details: Optional[BillCompanyDetails] = FieldInfo(alias="CompanyDetails", default=None)

    company_id: Optional[str] = FieldInfo(alias="CompanyId", default=None)
    """
    Unique identifier of the `Company` specified in `CompanyDetails` or the
    `Company` the bill is issued to.
    """

    corrected_bill_id: Optional[str] = FieldInfo(alias="CorrectedBillId", default=None)
    """The ID of the bill that the corrective bill corrects.

    If the corrected bill was deleted, this field is `null`.
    """

    correction_type: Optional[
        Literal["Cancellation", "Edit", "CreditNote", "Reinstatement", "ReceivablePaymentsBalance"]
    ] = FieldInfo(alias="CorrectionType", default=None)
    """Cancellation

    Edit

    CreditNote

    Reinstatement

    ReceivablePaymentsBalance
    """

    counter_id: Optional[str] = FieldInfo(alias="CounterId", default=None)
    """Unique identifier of the bill `Counter`."""

    customer_id: Optional[str] = FieldInfo(alias="CustomerId", default=None)
    """Unique identifier of the `Customer` the bill is issued to."""

    due_utc: Optional[datetime] = FieldInfo(alias="DueUtc", default=None)
    """Bill due date and time in UTC timezone in ISO 8601 format."""

    enterprise_data: Optional[BillEnterpriseData] = FieldInfo(alias="EnterpriseData", default=None)
    """
    Additional information about the enterprise issuing the bill, including bank
    account details. Persisted at the time of closing of the bill.
    """

    issued_utc: Optional[datetime] = FieldInfo(alias="IssuedUtc", default=None)
    """Date and time of the bill issuance in UTC timezone in ISO 8601 format."""

    last_reminder_date_utc: Optional[datetime] = FieldInfo(alias="LastReminderDateUtc", default=None)
    """
    Date and time when an email reminder to pay an invoice was last sent, in UTC
    timezone in ISO 8601 format.
    """

    name: Optional[str] = FieldInfo(alias="Name", default=None)
    """Name of the bill."""

    notes: Optional[str] = FieldInfo(alias="Notes", default=None)
    """Additional notes."""

    number: Optional[str] = FieldInfo(alias="Number", default=None)
    """Number of the bill."""

    options: Optional[BillOptions] = FieldInfo(alias="Options", default=None)
    """Options of the bill."""

    owner_data: Optional[BillOwnerData] = FieldInfo(alias="OwnerData", default=None)
    """Additional information about owner of the bill.

    Can be a
    [Customer](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer)
    or
    [Company](https://mews-systems.gitbook.io/connector-api/operations/companies/#company).
    Persisted at the time of closing of the bill.
    """

    paid_utc: Optional[datetime] = FieldInfo(alias="PaidUtc", default=None)
    """Date when the bill was paid in UTC timezone in ISO 8601 format."""

    purchase_order_number: Optional[str] = FieldInfo(alias="PurchaseOrderNumber", default=None)
    """Unique number of the purchase order from the buyer."""

    taxed_utc: Optional[datetime] = FieldInfo(alias="TaxedUtc", default=None)
    """Taxation date of the bill in UTC timezone in ISO 8601 format."""

    variable_symbol: Optional[str] = FieldInfo(alias="VariableSymbol", default=None)
    """Variable symbol of the bill."""


class BillUpdateResponse(BaseModel):
    bills: List[Bill] = FieldInfo(alias="Bills")
    """Updated bills."""
