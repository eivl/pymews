# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = [
    "ProductGetPricingResponse",
    "AgeCategoryPrice",
    "AgeCategoryPricePrice",
    "AgeCategoryPricePriceBreakdown",
    "AgeCategoryPricePriceBreakdownItem",
    "AgeCategoryPricePriceTaxValue",
    "BaseAmountPrice",
    "BaseAmountPriceBreakdown",
    "BaseAmountPriceBreakdownItem",
    "BaseAmountPriceTaxValue",
]


class AgeCategoryPricePriceBreakdownItem(BaseModel):
    net_value: float = FieldInfo(alias="NetValue")
    """The net value that the tax is calculated from."""

    tax_value: float = FieldInfo(alias="TaxValue")
    """The value of the tax."""

    tax_rate_code: Optional[str] = FieldInfo(alias="TaxRateCode", default=None)
    """Tax rate code for the item. `null` for untaxed amounts."""


class AgeCategoryPricePriceBreakdown(BaseModel):
    items: List[AgeCategoryPricePriceBreakdownItem] = FieldInfo(alias="Items")
    """Tax breakdown items per each tax rate applied."""


class AgeCategoryPricePriceTaxValue(BaseModel):
    value: float = FieldInfo(alias="Value")
    """Amount of tax applied."""

    code: Optional[str] = FieldInfo(alias="Code", default=None)
    """Code corresponding to tax type."""


class AgeCategoryPricePrice(BaseModel):
    breakdown: AgeCategoryPricePriceBreakdown = FieldInfo(alias="Breakdown")
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

    tax_values: List[AgeCategoryPricePriceTaxValue] = FieldInfo(alias="TaxValues")
    """The tax values applied."""


class AgeCategoryPrice(BaseModel):
    age_category_id: str = FieldInfo(alias="AgeCategoryId")
    """Unique identifier of the age category."""

    prices: List[AgeCategoryPricePrice] = FieldInfo(alias="Prices")
    """Prices of the product for the resource category in the covered dates."""


class BaseAmountPriceBreakdownItem(BaseModel):
    net_value: float = FieldInfo(alias="NetValue")
    """The net value that the tax is calculated from."""

    tax_value: float = FieldInfo(alias="TaxValue")
    """The value of the tax."""

    tax_rate_code: Optional[str] = FieldInfo(alias="TaxRateCode", default=None)
    """Tax rate code for the item. `null` for untaxed amounts."""


class BaseAmountPriceBreakdown(BaseModel):
    items: List[BaseAmountPriceBreakdownItem] = FieldInfo(alias="Items")
    """Tax breakdown items per each tax rate applied."""


class BaseAmountPriceTaxValue(BaseModel):
    value: float = FieldInfo(alias="Value")
    """Amount of tax applied."""

    code: Optional[str] = FieldInfo(alias="Code", default=None)
    """Code corresponding to tax type."""


class BaseAmountPrice(BaseModel):
    breakdown: BaseAmountPriceBreakdown = FieldInfo(alias="Breakdown")
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

    tax_values: List[BaseAmountPriceTaxValue] = FieldInfo(alias="TaxValues")
    """The tax values applied."""


class ProductGetPricingResponse(BaseModel):
    age_category_prices: List[AgeCategoryPrice] = FieldInfo(alias="AgeCategoryPrices")
    """Age category prices."""

    base_amount_prices: List[BaseAmountPrice] = FieldInfo(alias="BaseAmountPrices")
    """Base prices of the product for each time unit covered by the time interval."""

    product_id: str = FieldInfo(alias="ProductId")
    """Unique identifier of the product."""

    time_unit_starts_utc: List[str] = FieldInfo(alias="TimeUnitStartsUtc")
    """
    Set of all time units covered by the time interval; expressed in UTC timezone
    ISO 8601 format.
    """
