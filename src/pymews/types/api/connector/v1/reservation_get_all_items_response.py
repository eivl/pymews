# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import date
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = [
    "ReservationGetAllItemsResponse",
    "Reservation",
    "ReservationItem",
    "ReservationItemAmount",
    "ReservationItemAmountBreakdown",
    "ReservationItemAmountBreakdownItem",
    "ReservationItemAmountTaxValue",
    "ReservationOrderItem",
    "ReservationOrderItemAmount",
    "ReservationOrderItemAmountBreakdown",
    "ReservationOrderItemAmountBreakdownItem",
    "ReservationOrderItemAmountTaxValue",
    "ReservationOrderItemData",
    "ReservationOrderItemDataValue",
    "ReservationOrderItemDataValueRebateOrderItemData",
    "ReservationOrderItemDataValueProductOrderItemData",
    "ReservationOrderItemOriginalAmount",
    "ReservationOrderItemOriginalAmountBreakdown",
    "ReservationOrderItemOriginalAmountBreakdownItem",
    "ReservationOrderItemOriginalAmountTaxValue",
    "ReservationOrderItemUnitAmount",
    "ReservationOrderItemUnitAmountBreakdown",
    "ReservationOrderItemUnitAmountBreakdownItem",
    "ReservationOrderItemUnitAmountTaxValue",
]


class ReservationItemAmountBreakdownItem(BaseModel):
    net_value: float = FieldInfo(alias="NetValue")
    """The net value that the tax is calculated from."""

    tax_value: float = FieldInfo(alias="TaxValue")
    """The value of the tax."""

    tax_rate_code: Optional[str] = FieldInfo(alias="TaxRateCode", default=None)
    """Tax rate code for the item. `null` for untaxed amounts."""


class ReservationItemAmountBreakdown(BaseModel):
    items: List[ReservationItemAmountBreakdownItem] = FieldInfo(alias="Items")
    """Tax breakdown items per each tax rate applied."""


class ReservationItemAmountTaxValue(BaseModel):
    value: float = FieldInfo(alias="Value")
    """Amount of tax applied."""

    code: Optional[str] = FieldInfo(alias="Code", default=None)
    """Code corresponding to tax type."""


class ReservationItemAmount(BaseModel):
    breakdown: ReservationItemAmountBreakdown = FieldInfo(alias="Breakdown")
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

    tax_values: List[ReservationItemAmountTaxValue] = FieldInfo(alias="TaxValues")
    """The tax values applied."""

    net: Optional[float] = FieldInfo(alias="Net", default=None)

    tax: Optional[float] = FieldInfo(alias="Tax", default=None)

    tax_rate: Optional[float] = FieldInfo(alias="TaxRate", default=None)

    value: Optional[float] = FieldInfo(alias="Value", default=None)


class ReservationItem(BaseModel):
    account_id: Optional[str] = FieldInfo(alias="AccountId", default=None)

    accounting_category_id: Optional[str] = FieldInfo(alias="AccountingCategoryId", default=None)

    amount: Optional[ReservationItemAmount] = FieldInfo(alias="Amount", default=None)

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


class ReservationOrderItemAmountBreakdownItem(BaseModel):
    net_value: float = FieldInfo(alias="NetValue")
    """The net value that the tax is calculated from."""

    tax_value: float = FieldInfo(alias="TaxValue")
    """The value of the tax."""

    tax_rate_code: Optional[str] = FieldInfo(alias="TaxRateCode", default=None)
    """Tax rate code for the item. `null` for untaxed amounts."""


class ReservationOrderItemAmountBreakdown(BaseModel):
    items: List[ReservationOrderItemAmountBreakdownItem] = FieldInfo(alias="Items")
    """Tax breakdown items per each tax rate applied."""


class ReservationOrderItemAmountTaxValue(BaseModel):
    value: float = FieldInfo(alias="Value")
    """Amount of tax applied."""

    code: Optional[str] = FieldInfo(alias="Code", default=None)
    """Code corresponding to tax type."""


class ReservationOrderItemAmount(BaseModel):
    breakdown: ReservationOrderItemAmountBreakdown = FieldInfo(alias="Breakdown")
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

    tax_values: List[ReservationOrderItemAmountTaxValue] = FieldInfo(alias="TaxValues")
    """The tax values applied."""

    net: Optional[float] = FieldInfo(alias="Net", default=None)

    tax: Optional[float] = FieldInfo(alias="Tax", default=None)

    tax_rate: Optional[float] = FieldInfo(alias="TaxRate", default=None)

    value: Optional[float] = FieldInfo(alias="Value", default=None)


class ReservationOrderItemDataValueRebateOrderItemData(BaseModel):
    rebated_item_id: Optional[str] = FieldInfo(alias="RebatedItemId", default=None)


class ReservationOrderItemDataValueProductOrderItemData(BaseModel):
    age_category_id: Optional[str] = FieldInfo(alias="AgeCategoryId", default=None)

    product_id: Optional[str] = FieldInfo(alias="ProductId", default=None)


ReservationOrderItemDataValue: TypeAlias = Union[
    ReservationOrderItemDataValueRebateOrderItemData, ReservationOrderItemDataValueProductOrderItemData
]


class ReservationOrderItemData(BaseModel):
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

    value: Optional[ReservationOrderItemDataValue] = None


class ReservationOrderItemOriginalAmountBreakdownItem(BaseModel):
    net_value: float = FieldInfo(alias="NetValue")
    """The net value that the tax is calculated from."""

    tax_value: float = FieldInfo(alias="TaxValue")
    """The value of the tax."""

    tax_rate_code: Optional[str] = FieldInfo(alias="TaxRateCode", default=None)
    """Tax rate code for the item. `null` for untaxed amounts."""


class ReservationOrderItemOriginalAmountBreakdown(BaseModel):
    items: List[ReservationOrderItemOriginalAmountBreakdownItem] = FieldInfo(alias="Items")
    """Tax breakdown items per each tax rate applied."""


class ReservationOrderItemOriginalAmountTaxValue(BaseModel):
    value: float = FieldInfo(alias="Value")
    """Amount of tax applied."""

    code: Optional[str] = FieldInfo(alias="Code", default=None)
    """Code corresponding to tax type."""


class ReservationOrderItemOriginalAmount(BaseModel):
    breakdown: ReservationOrderItemOriginalAmountBreakdown = FieldInfo(alias="Breakdown")
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

    tax_values: List[ReservationOrderItemOriginalAmountTaxValue] = FieldInfo(alias="TaxValues")
    """The tax values applied."""

    net: Optional[float] = FieldInfo(alias="Net", default=None)

    tax: Optional[float] = FieldInfo(alias="Tax", default=None)

    tax_rate: Optional[float] = FieldInfo(alias="TaxRate", default=None)

    value: Optional[float] = FieldInfo(alias="Value", default=None)


class ReservationOrderItemUnitAmountBreakdownItem(BaseModel):
    net_value: float = FieldInfo(alias="NetValue")
    """The net value that the tax is calculated from."""

    tax_value: float = FieldInfo(alias="TaxValue")
    """The value of the tax."""

    tax_rate_code: Optional[str] = FieldInfo(alias="TaxRateCode", default=None)
    """Tax rate code for the item. `null` for untaxed amounts."""


class ReservationOrderItemUnitAmountBreakdown(BaseModel):
    items: List[ReservationOrderItemUnitAmountBreakdownItem] = FieldInfo(alias="Items")
    """Tax breakdown items per each tax rate applied."""


class ReservationOrderItemUnitAmountTaxValue(BaseModel):
    value: float = FieldInfo(alias="Value")
    """Amount of tax applied."""

    code: Optional[str] = FieldInfo(alias="Code", default=None)
    """Code corresponding to tax type."""


class ReservationOrderItemUnitAmount(BaseModel):
    breakdown: ReservationOrderItemUnitAmountBreakdown = FieldInfo(alias="Breakdown")
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

    tax_values: List[ReservationOrderItemUnitAmountTaxValue] = FieldInfo(alias="TaxValues")
    """The tax values applied."""


class ReservationOrderItem(BaseModel):
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

    amount: Optional[ReservationOrderItemAmount] = FieldInfo(alias="Amount", default=None)

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

    data: Optional[ReservationOrderItemData] = FieldInfo(alias="Data", default=None)
    """Additional data specific to particular order item."""

    id: Optional[str] = FieldInfo(alias="Id", default=None)
    """Unique identifier of the item."""

    order_id: Optional[str] = FieldInfo(alias="OrderId", default=None)
    """
    Unique identifier of the order (or
    [Reservation](https://mews-systems.gitbook.io/connector-api/operations/reservations/#reservation-ver-2023-06-06)
    which is a special type of order) the item belongs to.
    """

    original_amount: Optional[ReservationOrderItemOriginalAmount] = FieldInfo(alias="OriginalAmount", default=None)

    revenue_type: Optional[str] = FieldInfo(alias="RevenueType", default=None)
    """Revenue type of the item."""

    start_utc: Optional[date] = FieldInfo(alias="StartUtc", default=None)

    unit_amount: Optional[ReservationOrderItemUnitAmount] = FieldInfo(alias="UnitAmount", default=None)

    unit_count: Optional[int] = FieldInfo(alias="UnitCount", default=None)
    """Unit count of item, i.e. the number of sub-items or units, if applicable."""

    updated_utc: Optional[date] = FieldInfo(alias="UpdatedUtc", default=None)

    updater_profile_id: Optional[str] = FieldInfo(alias="UpdaterProfileId", default=None)


class Reservation(BaseModel):
    items: List[ReservationItem] = FieldInfo(alias="Items")
    """Accounting items associated with the reservation."""

    order_items: List[ReservationOrderItem] = FieldInfo(alias="OrderItems")
    """Order items associated with the reservation."""

    reservation_id: Optional[str] = FieldInfo(alias="ReservationId", default=None)
    """Unique identifier of the reservation."""


class ReservationGetAllItemsResponse(BaseModel):
    reservations: List[Reservation] = FieldInfo(alias="Reservations")
    """The reservations with their items."""
