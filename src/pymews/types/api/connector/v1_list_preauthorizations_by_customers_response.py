# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "V1ListPreauthorizationsByCustomersResponse",
    "Preauthorization",
    "PreauthorizationAmount",
    "PreauthorizationAmountBreakdown",
    "PreauthorizationAmountBreakdownItem",
    "PreauthorizationAmountTaxValue",
]


class PreauthorizationAmountBreakdownItem(BaseModel):
    net_value: float = FieldInfo(alias="NetValue")
    """The net value that the tax is calculated from."""

    tax_value: float = FieldInfo(alias="TaxValue")
    """The value of the tax."""

    tax_rate_code: Optional[str] = FieldInfo(alias="TaxRateCode", default=None)
    """Tax rate code for the item. `null` for untaxed amounts."""


class PreauthorizationAmountBreakdown(BaseModel):
    items: List[PreauthorizationAmountBreakdownItem] = FieldInfo(alias="Items")
    """Tax breakdown items per each tax rate applied."""


class PreauthorizationAmountTaxValue(BaseModel):
    value: float = FieldInfo(alias="Value")
    """Amount of tax applied."""

    code: Optional[str] = FieldInfo(alias="Code", default=None)
    """Code corresponding to tax type."""


class PreauthorizationAmount(BaseModel):
    breakdown: PreauthorizationAmountBreakdown = FieldInfo(alias="Breakdown")
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

    tax_values: List[PreauthorizationAmountTaxValue] = FieldInfo(alias="TaxValues")
    """The tax values applied."""


class Preauthorization(BaseModel):
    amount: Optional[PreauthorizationAmount] = FieldInfo(alias="Amount", default=None)

    code: Optional[str] = FieldInfo(alias="Code", default=None)
    """Code of the preauthorization."""

    credit_card_id: Optional[str] = FieldInfo(alias="CreditCardId", default=None)
    """Unique identifier of the credit card."""

    customer_id: Optional[str] = FieldInfo(alias="CustomerId", default=None)

    id: Optional[str] = FieldInfo(alias="Id", default=None)
    """Unique identifier of the preauthorization."""

    is_active: Optional[bool] = FieldInfo(alias="IsActive", default=None)

    state: Optional[str] = FieldInfo(alias="State", default=None)
    """State of the preauthorization."""


class V1ListPreauthorizationsByCustomersResponse(BaseModel):
    preauthorizations: Optional[List[Preauthorization]] = FieldInfo(alias="Preauthorizations", default=None)
    """
    Preauthorizations of the specified
    [Customers](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer).
    """
