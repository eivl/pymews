# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "V1ListTaxEnvironmentsResponse",
    "Taxation",
    "TaxEnvironment",
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

    local_name: Optional[str] = FieldInfo(alias="LocalName", default=None)

    name: Optional[str] = FieldInfo(alias="Name", default=None)

    tax_environment_code: Optional[str] = FieldInfo(alias="TaxEnvironmentCode", default=None)


class TaxEnvironment(BaseModel):
    code: Optional[str] = FieldInfo(alias="Code", default=None)
    """Code of the tax environment."""

    country_code: Optional[str] = FieldInfo(alias="CountryCode", default=None)
    """ISO 3166-1 alpha-3 code of associated country, e.g. USA or GBR."""

    taxation_codes: Optional[List[str]] = FieldInfo(alias="TaxationCodes", default=None)
    """
    Codes of the
    [Taxations](https://mews-systems.gitbook.io/connector-api/operations/#taxation)
    that are used by this environment.
    """

    validity_end_utc: Optional[str] = FieldInfo(alias="ValidityEndUtc", default=None)
    """
    If specified, marks the end of the validity interval in UTC timezone in ISO 8601
    format.
    """

    validity_start_utc: Optional[str] = FieldInfo(alias="ValidityStartUtc", default=None)
    """
    If specified, marks the start of the validity interval in UTC timezone in ISO
    8601 format.
    """


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


class V1ListTaxEnvironmentsResponse(BaseModel):
    taxations: Optional[List[Taxation]] = FieldInfo(alias="Taxations", default=None)

    tax_environments: Optional[List[TaxEnvironment]] = FieldInfo(alias="TaxEnvironments", default=None)
    """The supported tax environments."""

    tax_rates: Optional[List[TaxRate]] = FieldInfo(alias="TaxRates", default=None)
