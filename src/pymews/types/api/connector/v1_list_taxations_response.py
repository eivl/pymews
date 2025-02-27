# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "V1ListTaxationsResponse",
    "Taxation",
    "TaxRate",
    "TaxRateStrategy",
    "TaxRateStrategyValue",
    "TaxRateStrategyValueRelativeTaxRateStrategy",
    "TaxRateStrategyValueFlatTaxRateStrategy",
    "TaxRateStrategyValueDependentTaxRateStrategy",
    "TaxRateValidityInvervalsUtc",
]


class Taxation(BaseModel):
    code: Optional[str] = FieldInfo(alias="Code", default=None)
    """Code of the taxation."""

    local_name: Optional[str] = FieldInfo(alias="LocalName", default=None)
    """Local name of the taxation."""

    name: Optional[str] = FieldInfo(alias="Name", default=None)
    """Name of the taxation."""


class TaxRateStrategyValueRelativeTaxRateStrategy(BaseModel):
    value: Optional[float] = FieldInfo(alias="Value", default=None)


class TaxRateStrategyValueFlatTaxRateStrategy(BaseModel):
    currency_code: Optional[str] = FieldInfo(alias="CurrencyCode", default=None)

    value: Optional[float] = FieldInfo(alias="Value", default=None)


class TaxRateStrategyValueDependentTaxRateStrategy(BaseModel):
    base_taxation_codes: Optional[List[str]] = FieldInfo(alias="BaseTaxationCodes", default=None)

    value: Optional[float] = FieldInfo(alias="Value", default=None)


TaxRateStrategyValue: TypeAlias = Union[
    TaxRateStrategyValueRelativeTaxRateStrategy,
    TaxRateStrategyValueFlatTaxRateStrategy,
    TaxRateStrategyValueDependentTaxRateStrategy,
]


class TaxRateStrategy(BaseModel):
    discriminator: Optional[Literal["Relative", "Flat", "Dependent"]] = None

    value: Optional[TaxRateStrategyValue] = None


class TaxRateValidityInvervalsUtc(BaseModel):
    end_utc: Optional[str] = FieldInfo(alias="EndUtc", default=None)

    start_utc: Optional[str] = FieldInfo(alias="StartUtc", default=None)


class TaxRate(BaseModel):
    code: Optional[str] = FieldInfo(alias="Code", default=None)
    """Code of the tax rate.

    To be used when posting revenue items which should be accompanied by the tax
    rate(s) applicable to the nature of the item and the tax environment.
    """

    strategy: Optional[TaxRateStrategy] = FieldInfo(alias="Strategy", default=None)
    """Tax strategy type, e.g. relative, flat or dependent."""

    taxation_code: Optional[str] = FieldInfo(alias="TaxationCode", default=None)
    """
    Code of the
    [Taxation](https://mews-systems.gitbook.io/connector-api/operations/#taxation)
    the rate is part of.
    """

    validity_invervals_utc: Optional[List[TaxRateValidityInvervalsUtc]] = FieldInfo(
        alias="ValidityInvervalsUtc", default=None
    )

    value: Optional[float] = FieldInfo(alias="Value", default=None)


class V1ListTaxationsResponse(BaseModel):
    taxations: Optional[List[Taxation]] = FieldInfo(alias="Taxations", default=None)
    """The supported taxations."""

    tax_rates: Optional[List[TaxRate]] = FieldInfo(alias="TaxRates", default=None)
    """The supported tax rates."""
