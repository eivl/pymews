# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "V1ListOutletItemsResponse",
    "OutletBill",
    "OutletItem",
    "OutletItemUnitAmount",
    "OutletItemUnitAmountBreakdown",
    "OutletItemUnitAmountBreakdownItem",
    "OutletItemUnitAmountTaxValue",
    "OutletItemUnitCost",
]


class OutletBill(BaseModel):
    closed_utc: datetime = FieldInfo(alias="ClosedUtc")
    """Date and time of the bill closure in UTC timezone in ISO 8601 format."""

    enterprise_id: str = FieldInfo(alias="EnterpriseId")
    """Unique identifier of the Enterprise."""

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the bill."""

    outlet_id: str = FieldInfo(alias="OutletId")
    """
    Unique identifier of the
    [Outlet](https://mews-systems.gitbook.io/connector-api/operations/outlets/#outlet)
    where the bill was issued.
    """

    updated_utc: datetime = FieldInfo(alias="UpdatedUtc")
    """Last update date and time of the bill in UTC timezone in ISO 8601 format."""

    notes: Optional[str] = FieldInfo(alias="Notes", default=None)
    """Additional notes on the bill."""

    number: Optional[str] = FieldInfo(alias="Number", default=None)
    """Number of the bill."""


class OutletItemUnitAmountBreakdownItem(BaseModel):
    net_value: float = FieldInfo(alias="NetValue")
    """The net value that the tax is calculated from."""

    tax_value: float = FieldInfo(alias="TaxValue")
    """The value of the tax."""

    tax_rate_code: Optional[str] = FieldInfo(alias="TaxRateCode", default=None)
    """Tax rate code for the item. `null` for untaxed amounts."""


class OutletItemUnitAmountBreakdown(BaseModel):
    items: List[OutletItemUnitAmountBreakdownItem] = FieldInfo(alias="Items")
    """Tax breakdown items per each tax rate applied."""


class OutletItemUnitAmountTaxValue(BaseModel):
    value: float = FieldInfo(alias="Value")
    """Amount of tax applied."""

    code: Optional[str] = FieldInfo(alias="Code", default=None)
    """Code corresponding to tax type."""


class OutletItemUnitAmount(BaseModel):
    breakdown: OutletItemUnitAmountBreakdown = FieldInfo(alias="Breakdown")
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

    tax_values: List[OutletItemUnitAmountTaxValue] = FieldInfo(alias="TaxValues")
    """The tax values applied."""


class OutletItemUnitCost(BaseModel):
    currency: str = FieldInfo(alias="Currency")

    net: Optional[float] = FieldInfo(alias="Net", default=None)

    tax: Optional[float] = FieldInfo(alias="Tax", default=None)

    tax_rate: Optional[float] = FieldInfo(alias="TaxRate", default=None)

    value: Optional[float] = FieldInfo(alias="Value", default=None)


class OutletItem(BaseModel):
    bill_id: str = FieldInfo(alias="BillId")
    """
    Unique identifier of the
    [Outlet bill](https://mews-systems.gitbook.io/connector-api/operations/#outlet-bill)
    the item belongs to.
    """

    consumed_utc: datetime = FieldInfo(alias="ConsumedUtc")
    """Date and time of the item consumption in UTC timezone in ISO 8601 format."""

    created_utc: datetime = FieldInfo(alias="CreatedUtc")
    """Date and time of the item creation in UTC timezone in ISO 8601 format."""

    enterprise_id: str = FieldInfo(alias="EnterpriseId")
    """
    Unique identifier of the
    [Enterprise](https://mews-systems.gitbook.io/connector-api/operations/enterprises/#enterprise).
    """

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the item."""

    type: Literal["Revenue", "NonRevenue", "Payment"] = FieldInfo(alias="Type")
    """Type of the outlet item."""

    unit_amount: OutletItemUnitAmount = FieldInfo(alias="UnitAmount")

    unit_count: int = FieldInfo(alias="UnitCount")
    """Unit count of the item."""

    updated_utc: datetime = FieldInfo(alias="UpdatedUtc")
    """Last update date and time of the item in UTC timezone in ISO 8601 format."""

    accounting_category_id: Optional[str] = FieldInfo(alias="AccountingCategoryId", default=None)
    """
    Unique identifier of the
    [Accounting category](https://mews-systems.gitbook.io/connector-api/operations/accountingcategories/#accounting-category)
    the item belongs to.
    """

    external_identifier: Optional[str] = FieldInfo(alias="ExternalIdentifier", default=None)
    """An identifier of this item from another system."""

    name: Optional[str] = FieldInfo(alias="Name", default=None)
    """Name of the item."""

    notes: Optional[str] = FieldInfo(alias="Notes", default=None)
    """Additional notes."""

    payment_card_payment_id: Optional[str] = FieldInfo(alias="PaymentCardPaymentId", default=None)
    """Unique identifier of the payment card `Payment` this item is linked to.

    This is only applicable to items where `Type` is `Payment`.
    """

    unit_cost: Optional[OutletItemUnitCost] = FieldInfo(alias="UnitCost", default=None)
    """Total price of the reservation."""


class V1ListOutletItemsResponse(BaseModel):
    outlet_bills: List[OutletBill] = FieldInfo(alias="OutletBills")
    """The outlet bills of the items."""

    outlet_items: List[OutletItem] = FieldInfo(alias="OutletItems")
    """The outlet items."""

    cursor: Optional[str] = FieldInfo(alias="Cursor", default=None)
    """Unique identifier of the last and hence oldest outlet item returned.

    This can be used in
    [Limitation](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/#limitation)
    in a subsequent request to fetch the next batch of older outlet items.
    """
