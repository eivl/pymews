# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = [
    "ReservationPriceResponse",
    "ReservationPrice",
    "ReservationPriceTotalAmount",
    "ReservationPriceTotalAmountBreakdown",
    "ReservationPriceTotalAmountBreakdownItem",
    "ReservationPriceTotalAmountTaxValue",
    "ReservationPriceTotal",
]


class ReservationPriceTotalAmountBreakdownItem(BaseModel):
    net_value: float = FieldInfo(alias="NetValue")
    """The net value that the tax is calculated from."""

    tax_value: float = FieldInfo(alias="TaxValue")
    """The value of the tax."""

    tax_rate_code: Optional[str] = FieldInfo(alias="TaxRateCode", default=None)
    """Tax rate code for the item. `null` for untaxed amounts."""


class ReservationPriceTotalAmountBreakdown(BaseModel):
    items: List[ReservationPriceTotalAmountBreakdownItem] = FieldInfo(alias="Items")
    """Tax breakdown items per each tax rate applied."""


class ReservationPriceTotalAmountTaxValue(BaseModel):
    value: float = FieldInfo(alias="Value")
    """Amount of tax applied."""

    code: Optional[str] = FieldInfo(alias="Code", default=None)
    """Code corresponding to tax type."""


class ReservationPriceTotalAmount(BaseModel):
    breakdown: ReservationPriceTotalAmountBreakdown = FieldInfo(alias="Breakdown")
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

    tax_values: List[ReservationPriceTotalAmountTaxValue] = FieldInfo(alias="TaxValues")
    """The tax values applied."""


class ReservationPriceTotal(BaseModel):
    currency: str = FieldInfo(alias="Currency")

    net: Optional[float] = FieldInfo(alias="Net", default=None)

    tax: Optional[float] = FieldInfo(alias="Tax", default=None)

    tax_rate: Optional[float] = FieldInfo(alias="TaxRate", default=None)

    value: Optional[float] = FieldInfo(alias="Value", default=None)


class ReservationPrice(BaseModel):
    total_amount: ReservationPriceTotalAmount = FieldInfo(alias="TotalAmount")

    identifier: Optional[str] = FieldInfo(alias="Identifier", default=None)
    """Identifier of the reservation within the transaction."""

    total: Optional[ReservationPriceTotal] = FieldInfo(alias="Total", default=None)
    """Total price of the reservation."""


class ReservationPriceResponse(BaseModel):
    reservation_prices: List[ReservationPrice] = FieldInfo(alias="ReservationPrices")
    """The reservation prices."""
