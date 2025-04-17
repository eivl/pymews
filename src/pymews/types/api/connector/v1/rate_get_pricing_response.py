# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = [
    "RateGetPricingResponse",
    "AgeCategoryAdjustment",
    "BaseAmountPrice",
    "BaseAmountPriceBreakdown",
    "BaseAmountPriceBreakdownItem",
    "BaseAmountPriceTaxValue",
    "CategoryAdjustment",
    "CategoryPrice",
    "CategoryPriceAmountPrice",
    "CategoryPriceAmountPriceBreakdown",
    "CategoryPriceAmountPriceBreakdownItem",
    "CategoryPriceAmountPriceTaxValue",
]


class AgeCategoryAdjustment(BaseModel):
    absolute_value: float = FieldInfo(alias="AbsoluteValue")
    """Absolute value of the adjustment (e.g.

    `50` represents 50 EUR in case the rate currency is `EUR`).
    """

    age_category_id: str = FieldInfo(alias="AgeCategoryId")
    """Unique identifier of the age category."""

    type: Literal["ExtraOccupancyAdjustment", "NegativeOccupancyAdjustment", "StandardOccupancyAdjustment"] = FieldInfo(
        alias="Type"
    )
    """ExtraOccupancyAdjustment

    NegativeOccupancyAdjustment

    StandardOccupancyAdjustment
    """


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


class CategoryAdjustment(BaseModel):
    absolute_value: float = FieldInfo(alias="AbsoluteValue")
    """Absolute value of the adjustment (e.g.

    `50` represents 50 EUR in case the rate currency is `EUR`).
    """

    category_id: str = FieldInfo(alias="CategoryId")
    """Unique identifier of the adjustment category."""

    relative_value: float = FieldInfo(alias="RelativeValue")
    """Relative value of the adjustment (e.g. `0.5` represents 50% increase)."""

    parent_category_id: Optional[str] = FieldInfo(alias="ParentCategoryId", default=None)
    """
    Unique identifier of the parent category that serves as a base price for the
    current category.
    """


class CategoryPriceAmountPriceBreakdownItem(BaseModel):
    net_value: float = FieldInfo(alias="NetValue")
    """The net value that the tax is calculated from."""

    tax_value: float = FieldInfo(alias="TaxValue")
    """The value of the tax."""

    tax_rate_code: Optional[str] = FieldInfo(alias="TaxRateCode", default=None)
    """Tax rate code for the item. `null` for untaxed amounts."""


class CategoryPriceAmountPriceBreakdown(BaseModel):
    items: List[CategoryPriceAmountPriceBreakdownItem] = FieldInfo(alias="Items")
    """Tax breakdown items per each tax rate applied."""


class CategoryPriceAmountPriceTaxValue(BaseModel):
    value: float = FieldInfo(alias="Value")
    """Amount of tax applied."""

    code: Optional[str] = FieldInfo(alias="Code", default=None)
    """Code corresponding to tax type."""


class CategoryPriceAmountPrice(BaseModel):
    breakdown: CategoryPriceAmountPriceBreakdown = FieldInfo(alias="Breakdown")
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

    tax_values: List[CategoryPriceAmountPriceTaxValue] = FieldInfo(alias="TaxValues")
    """The tax values applied."""


class CategoryPrice(BaseModel):
    amount_prices: List[CategoryPriceAmountPrice] = FieldInfo(alias="AmountPrices")
    """Prices of the rate for the resource category in the covered dates."""

    category_id: str = FieldInfo(alias="CategoryId")
    """Unique identifier of the category."""

    prices: List[float] = FieldInfo(alias="Prices")
    """Prices of the rate for the resource category in the covered dates."""


class RateGetPricingResponse(BaseModel):
    age_category_adjustments: List[AgeCategoryAdjustment] = FieldInfo(alias="AgeCategoryAdjustments")
    """Assigns different pricing or occupancy based on the guest's age."""

    base_amount_prices: List[BaseAmountPrice] = FieldInfo(alias="BaseAmountPrices")
    """Base prices of the rates for each time unit covered by the time interval."""

    base_prices: List[float] = FieldInfo(alias="BasePrices")

    category_adjustments: List[CategoryAdjustment] = FieldInfo(alias="CategoryAdjustments")
    """Resource category adjustments."""

    category_prices: List[CategoryPrice] = FieldInfo(alias="CategoryPrices")
    """Resource category prices."""

    currency: str = FieldInfo(alias="Currency")
    """
    ISO-4217 code of the
    [Currency](https://mews-systems.gitbook.io/connector-api/operations/currencies/#currency).
    """

    time_unit_starts_utc: List[str] = FieldInfo(alias="TimeUnitStartsUtc")
    """
    Set of all time units covered by the time interval; expressed in UTC timezone
    ISO 8601 format.
    """

    absolute_adjustment: Optional[float] = FieldInfo(alias="AbsoluteAdjustment", default=None)
    """Relative amount which shows the difference between this rate and the base rate."""

    dates_utc: Optional[List[str]] = FieldInfo(alias="DatesUtc", default=None)

    empty_unit_adjustment: Optional[float] = FieldInfo(alias="EmptyUnitAdjustment", default=None)
    """
    Price adjustment for when the resource booked with this rate is not full to
    capacity.
    """

    extra_unit_adjustment: Optional[float] = FieldInfo(alias="ExtraUnitAdjustment", default=None)
    """Price adjustment for when the resource booked with this rate exceeds capacity."""

    relative_adjustment: Optional[float] = FieldInfo(alias="RelativeAdjustment", default=None)
    """Specific amount which shows the difference between this rate and the base rate."""
