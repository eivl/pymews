# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = [
    "ProductListResponse",
    "CustomerProduct",
    "CustomerProductClassifications",
    "CustomerProductOptions",
    "CustomerProductPrice",
    "CustomerProductPriceBreakdown",
    "CustomerProductPriceBreakdownItem",
    "CustomerProductPriceTaxValue",
    "CustomerProductPromotions",
    "CustomerProductPricing",
    "CustomerProductPricingValue",
    "CustomerProductPricingValueExtendedAmount",
    "CustomerProductPricingValueExtendedAmountBreakdown",
    "CustomerProductPricingValueExtendedAmountBreakdownItem",
    "CustomerProductPricingValueExtendedAmountTaxValue",
    "CustomerProductPricingValueRelativeProductPrice",
    "Product",
    "ProductClassifications",
    "ProductOptions",
    "ProductPrice",
    "ProductPriceBreakdown",
    "ProductPriceBreakdownItem",
    "ProductPriceTaxValue",
    "ProductPromotions",
    "ProductPricing",
    "ProductPricingValue",
    "ProductPricingValueExtendedAmount",
    "ProductPricingValueExtendedAmountBreakdown",
    "ProductPricingValueExtendedAmountBreakdownItem",
    "ProductPricingValueExtendedAmountTaxValue",
    "ProductPricingValueRelativeProductPrice",
]


class CustomerProductClassifications(BaseModel):
    beverage: Optional[bool] = FieldInfo(alias="Beverage", default=None)
    """Product is classified as beverage."""

    city_tax: Optional[bool] = FieldInfo(alias="CityTax", default=None)
    """Product is classified as city tax."""

    food: Optional[bool] = FieldInfo(alias="Food", default=None)
    """Product is classified as food."""

    wellness: Optional[bool] = FieldInfo(alias="Wellness", default=None)
    """Product is classified as wellness."""


class CustomerProductOptions(BaseModel):
    bill_as_package: bool = FieldInfo(alias="BillAsPackage")
    """Product should be displayed as part of a package."""


class CustomerProductPriceBreakdownItem(BaseModel):
    net_value: float = FieldInfo(alias="NetValue")
    """The net value that the tax is calculated from."""

    tax_value: float = FieldInfo(alias="TaxValue")
    """The value of the tax."""

    tax_rate_code: Optional[str] = FieldInfo(alias="TaxRateCode", default=None)
    """Tax rate code for the item. `null` for untaxed amounts."""


class CustomerProductPriceBreakdown(BaseModel):
    items: List[CustomerProductPriceBreakdownItem] = FieldInfo(alias="Items")
    """Tax breakdown items per each tax rate applied."""


class CustomerProductPriceTaxValue(BaseModel):
    value: float = FieldInfo(alias="Value")
    """Amount of tax applied."""

    code: Optional[str] = FieldInfo(alias="Code", default=None)
    """Code corresponding to tax type."""


class CustomerProductPrice(BaseModel):
    breakdown: CustomerProductPriceBreakdown = FieldInfo(alias="Breakdown")
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

    tax_values: List[CustomerProductPriceTaxValue] = FieldInfo(alias="TaxValues")
    """The tax values applied."""

    net: Optional[float] = FieldInfo(alias="Net", default=None)

    tax: Optional[float] = FieldInfo(alias="Tax", default=None)

    tax_rate: Optional[float] = FieldInfo(alias="TaxRate", default=None)

    value: Optional[float] = FieldInfo(alias="Value", default=None)


class CustomerProductPromotions(BaseModel):
    after_check_in: bool = FieldInfo(alias="AfterCheckIn")
    """Whether it can be promoted after check-in."""

    after_check_out: bool = FieldInfo(alias="AfterCheckOut")
    """Whether it can be promoted after check-out."""

    before_check_in: bool = FieldInfo(alias="BeforeCheckIn")
    """Whether it can be promoted before check-in."""

    before_check_out: bool = FieldInfo(alias="BeforeCheckOut")
    """Whether it can be promoted before check-out."""

    during_check_out: bool = FieldInfo(alias="DuringCheckOut")
    """Whether it can be promoted during check-out."""

    during_stay: bool = FieldInfo(alias="DuringStay")
    """Whether it can be promoted during stay."""


class CustomerProductPricingValueExtendedAmountBreakdownItem(BaseModel):
    net_value: float = FieldInfo(alias="NetValue")
    """The net value that the tax is calculated from."""

    tax_value: float = FieldInfo(alias="TaxValue")
    """The value of the tax."""

    tax_rate_code: Optional[str] = FieldInfo(alias="TaxRateCode", default=None)
    """Tax rate code for the item. `null` for untaxed amounts."""


class CustomerProductPricingValueExtendedAmountBreakdown(BaseModel):
    items: List[CustomerProductPricingValueExtendedAmountBreakdownItem] = FieldInfo(alias="Items")
    """Tax breakdown items per each tax rate applied."""


class CustomerProductPricingValueExtendedAmountTaxValue(BaseModel):
    value: float = FieldInfo(alias="Value")
    """Amount of tax applied."""

    code: Optional[str] = FieldInfo(alias="Code", default=None)
    """Code corresponding to tax type."""


class CustomerProductPricingValueExtendedAmount(BaseModel):
    breakdown: CustomerProductPricingValueExtendedAmountBreakdown = FieldInfo(alias="Breakdown")
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

    tax_values: List[CustomerProductPricingValueExtendedAmountTaxValue] = FieldInfo(alias="TaxValues")
    """The tax values applied."""

    net: Optional[float] = FieldInfo(alias="Net", default=None)

    tax: Optional[float] = FieldInfo(alias="Tax", default=None)

    tax_rate: Optional[float] = FieldInfo(alias="TaxRate", default=None)

    value: Optional[float] = FieldInfo(alias="Value", default=None)


class CustomerProductPricingValueRelativeProductPrice(BaseModel):
    multiplier: Optional[float] = FieldInfo(alias="Multiplier", default=None)

    product_ids: Optional[List[str]] = FieldInfo(alias="ProductIds", default=None)

    target: Optional[str] = FieldInfo(alias="Target", default=None)

    tax_rate_codes: Optional[List[str]] = FieldInfo(alias="TaxRateCodes", default=None)


CustomerProductPricingValue: TypeAlias = Union[
    CustomerProductPricingValueExtendedAmount, CustomerProductPricingValueRelativeProductPrice
]


class CustomerProductPricing(BaseModel):
    discriminator: Optional[Literal["Absolute", "Relative"]] = None

    value: Optional[CustomerProductPricingValue] = None


class CustomerProduct(BaseModel):
    charging_mode: Literal["Once", "PerTimeUnit", "PerPersonPerTimeUnit", "PerPerson"] = FieldInfo(alias="ChargingMode")
    """Once

    PerTimeUnit

    PerPersonPerTimeUnit

    PerPerson
    """

    classifications: CustomerProductClassifications = FieldInfo(alias="Classifications")

    consumption_moment: Literal["ServiceOrderEnd", "ServiceOrderStart", "PostingTimeUnit", "NextTimeUnit"] = FieldInfo(
        alias="ConsumptionMoment"
    )
    """ServiceOrderEnd

    ServiceOrderStart

    PostingTimeUnit

    NextTimeUnit
    """

    created_utc: datetime = FieldInfo(alias="CreatedUtc")
    """Creation date and time of the product in UTC timezone in ISO 8601 format."""

    external_names: Dict[str, str] = FieldInfo(alias="ExternalNames")
    """All translations of external name."""

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the product."""

    is_active: bool = FieldInfo(alias="IsActive")
    """Whether the product is still active."""

    names: Dict[str, str] = FieldInfo(alias="Names")
    """All translations of the name."""

    options: CustomerProductOptions = FieldInfo(alias="Options")

    ordering: int = FieldInfo(alias="Ordering")
    """Order value for presentation purposes."""

    posting_mode: Literal["Once", "PerTimeUnit"] = FieldInfo(alias="PostingMode")
    """Once

    PerTimeUnit
    """

    price: CustomerProductPrice = FieldInfo(alias="Price")

    promotions: CustomerProductPromotions = FieldInfo(alias="Promotions")

    service_id: str = FieldInfo(alias="ServiceId")
    """
    Unique identifier of the
    [Service](https://mews-systems.gitbook.io/connector-api/operations/services/#service).
    """

    short_names: Dict[str, str] = FieldInfo(alias="ShortNames")
    """All translations of short name."""

    updated_utc: datetime = FieldInfo(alias="UpdatedUtc")
    """Last update date and time of the product in UTC timezone in ISO 8601 format."""

    accounting_category_id: Optional[str] = FieldInfo(alias="AccountingCategoryId", default=None)
    """
    Unique identifier of
    [Accounting Category](https://mews-systems.gitbook.io/connector-api/operations/accountingcategories/#accounting-category).
    """

    category_id: Optional[str] = FieldInfo(alias="CategoryId", default=None)
    """Unique identifier of the Product category."""

    charging: Optional[Literal["Once", "PerTimeUnit", "PerPersonPerTimeUnit", "PerPerson"]] = FieldInfo(
        alias="Charging", default=None
    )
    """Once

    PerTimeUnit

    PerPersonPerTimeUnit

    PerPerson
    """

    description: Optional[str] = FieldInfo(alias="Description", default=None)
    """Description of the product. **Deprecated!** Please use Descriptions"""

    descriptions: Optional[Dict[str, str]] = FieldInfo(alias="Descriptions", default=None)
    """All translations of descriptions."""

    external_identifier: Optional[str] = FieldInfo(alias="ExternalIdentifier", default=None)
    """Identifier of the product from external system."""

    external_name: Optional[str] = FieldInfo(alias="ExternalName", default=None)
    """Name of the product meant to be displayed to customer.

    **Deprecated!** Please use ExternalNames
    """

    image_ids: Optional[List[str]] = FieldInfo(alias="ImageIds", default=None)
    """Unique identifier of the product image."""

    is_default: Optional[bool] = FieldInfo(alias="IsDefault", default=None)

    name: Optional[str] = FieldInfo(alias="Name", default=None)
    """Name of the product. **Deprecated!** Please use Names"""

    posting: Optional[Literal["Once", "Daily"]] = FieldInfo(alias="Posting", default=None)
    """Once

    Daily
    """

    pricing: Optional[CustomerProductPricing] = FieldInfo(alias="Pricing", default=None)

    short_name: Optional[str] = FieldInfo(alias="ShortName", default=None)
    """Short name of the product. **Deprecated!** Please use ShortNames"""

    tax_exemption_legal_reference: Optional[str] = FieldInfo(alias="TaxExemptionLegalReference", default=None)
    """Legal reference that states why this product is exempt from tax."""

    tax_exemption_reason: Optional[Literal["IT_N1", "IT_N2_2", "IT_N3_5", "IT_N4", "IT_N5"]] = FieldInfo(
        alias="TaxExemptionReason", default=None
    )
    """IT_N1 (N1 - Escluse ex art.15)

    IT_N2_2 (N2.2 - Non soggette – altri casi)

    IT_N3_5 (N3.5 - Non imponibili – a seguito di dichiarazioni d’intento)

    IT_N4 (N4 - Esenti)

    IT_N5 (N5 - Regime del margine / IVA non esposta in fattura)

    - `IT_N1` - N1 - Escluse ex art.15
    - `IT_N2_2` - N2.2 - Non soggette – altri casi
    - `IT_N3_5` - N3.5 - Non imponibili – a seguito di dichiarazioni d’intento
    - `IT_N4` - N4 - Esenti
    - `IT_N5` - N5 - Regime del margine / IVA non esposta in fattura
    """


class ProductClassifications(BaseModel):
    beverage: Optional[bool] = FieldInfo(alias="Beverage", default=None)
    """Product is classified as beverage."""

    city_tax: Optional[bool] = FieldInfo(alias="CityTax", default=None)
    """Product is classified as city tax."""

    food: Optional[bool] = FieldInfo(alias="Food", default=None)
    """Product is classified as food."""

    wellness: Optional[bool] = FieldInfo(alias="Wellness", default=None)
    """Product is classified as wellness."""


class ProductOptions(BaseModel):
    bill_as_package: bool = FieldInfo(alias="BillAsPackage")
    """Product should be displayed as part of a package."""


class ProductPriceBreakdownItem(BaseModel):
    net_value: float = FieldInfo(alias="NetValue")
    """The net value that the tax is calculated from."""

    tax_value: float = FieldInfo(alias="TaxValue")
    """The value of the tax."""

    tax_rate_code: Optional[str] = FieldInfo(alias="TaxRateCode", default=None)
    """Tax rate code for the item. `null` for untaxed amounts."""


class ProductPriceBreakdown(BaseModel):
    items: List[ProductPriceBreakdownItem] = FieldInfo(alias="Items")
    """Tax breakdown items per each tax rate applied."""


class ProductPriceTaxValue(BaseModel):
    value: float = FieldInfo(alias="Value")
    """Amount of tax applied."""

    code: Optional[str] = FieldInfo(alias="Code", default=None)
    """Code corresponding to tax type."""


class ProductPrice(BaseModel):
    breakdown: ProductPriceBreakdown = FieldInfo(alias="Breakdown")
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

    tax_values: List[ProductPriceTaxValue] = FieldInfo(alias="TaxValues")
    """The tax values applied."""

    net: Optional[float] = FieldInfo(alias="Net", default=None)

    tax: Optional[float] = FieldInfo(alias="Tax", default=None)

    tax_rate: Optional[float] = FieldInfo(alias="TaxRate", default=None)

    value: Optional[float] = FieldInfo(alias="Value", default=None)


class ProductPromotions(BaseModel):
    after_check_in: bool = FieldInfo(alias="AfterCheckIn")
    """Whether it can be promoted after check-in."""

    after_check_out: bool = FieldInfo(alias="AfterCheckOut")
    """Whether it can be promoted after check-out."""

    before_check_in: bool = FieldInfo(alias="BeforeCheckIn")
    """Whether it can be promoted before check-in."""

    before_check_out: bool = FieldInfo(alias="BeforeCheckOut")
    """Whether it can be promoted before check-out."""

    during_check_out: bool = FieldInfo(alias="DuringCheckOut")
    """Whether it can be promoted during check-out."""

    during_stay: bool = FieldInfo(alias="DuringStay")
    """Whether it can be promoted during stay."""


class ProductPricingValueExtendedAmountBreakdownItem(BaseModel):
    net_value: float = FieldInfo(alias="NetValue")
    """The net value that the tax is calculated from."""

    tax_value: float = FieldInfo(alias="TaxValue")
    """The value of the tax."""

    tax_rate_code: Optional[str] = FieldInfo(alias="TaxRateCode", default=None)
    """Tax rate code for the item. `null` for untaxed amounts."""


class ProductPricingValueExtendedAmountBreakdown(BaseModel):
    items: List[ProductPricingValueExtendedAmountBreakdownItem] = FieldInfo(alias="Items")
    """Tax breakdown items per each tax rate applied."""


class ProductPricingValueExtendedAmountTaxValue(BaseModel):
    value: float = FieldInfo(alias="Value")
    """Amount of tax applied."""

    code: Optional[str] = FieldInfo(alias="Code", default=None)
    """Code corresponding to tax type."""


class ProductPricingValueExtendedAmount(BaseModel):
    breakdown: ProductPricingValueExtendedAmountBreakdown = FieldInfo(alias="Breakdown")
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

    tax_values: List[ProductPricingValueExtendedAmountTaxValue] = FieldInfo(alias="TaxValues")
    """The tax values applied."""

    net: Optional[float] = FieldInfo(alias="Net", default=None)

    tax: Optional[float] = FieldInfo(alias="Tax", default=None)

    tax_rate: Optional[float] = FieldInfo(alias="TaxRate", default=None)

    value: Optional[float] = FieldInfo(alias="Value", default=None)


class ProductPricingValueRelativeProductPrice(BaseModel):
    multiplier: Optional[float] = FieldInfo(alias="Multiplier", default=None)

    product_ids: Optional[List[str]] = FieldInfo(alias="ProductIds", default=None)

    target: Optional[str] = FieldInfo(alias="Target", default=None)

    tax_rate_codes: Optional[List[str]] = FieldInfo(alias="TaxRateCodes", default=None)


ProductPricingValue: TypeAlias = Union[ProductPricingValueExtendedAmount, ProductPricingValueRelativeProductPrice]


class ProductPricing(BaseModel):
    discriminator: Optional[Literal["Absolute", "Relative"]] = None

    value: Optional[ProductPricingValue] = None


class Product(BaseModel):
    charging_mode: Literal["Once", "PerTimeUnit", "PerPersonPerTimeUnit", "PerPerson"] = FieldInfo(alias="ChargingMode")
    """Once

    PerTimeUnit

    PerPersonPerTimeUnit

    PerPerson
    """

    classifications: ProductClassifications = FieldInfo(alias="Classifications")

    consumption_moment: Literal["ServiceOrderEnd", "ServiceOrderStart", "PostingTimeUnit", "NextTimeUnit"] = FieldInfo(
        alias="ConsumptionMoment"
    )
    """ServiceOrderEnd

    ServiceOrderStart

    PostingTimeUnit

    NextTimeUnit
    """

    created_utc: datetime = FieldInfo(alias="CreatedUtc")
    """Creation date and time of the product in UTC timezone in ISO 8601 format."""

    external_names: Dict[str, str] = FieldInfo(alias="ExternalNames")
    """All translations of external name."""

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the product."""

    is_active: bool = FieldInfo(alias="IsActive")
    """Whether the product is still active."""

    names: Dict[str, str] = FieldInfo(alias="Names")
    """All translations of the name."""

    options: ProductOptions = FieldInfo(alias="Options")

    ordering: int = FieldInfo(alias="Ordering")
    """Order value for presentation purposes."""

    posting_mode: Literal["Once", "PerTimeUnit"] = FieldInfo(alias="PostingMode")
    """Once

    PerTimeUnit
    """

    price: ProductPrice = FieldInfo(alias="Price")

    promotions: ProductPromotions = FieldInfo(alias="Promotions")

    service_id: str = FieldInfo(alias="ServiceId")
    """
    Unique identifier of the
    [Service](https://mews-systems.gitbook.io/connector-api/operations/services/#service).
    """

    short_names: Dict[str, str] = FieldInfo(alias="ShortNames")
    """All translations of short name."""

    updated_utc: datetime = FieldInfo(alias="UpdatedUtc")
    """Last update date and time of the product in UTC timezone in ISO 8601 format."""

    accounting_category_id: Optional[str] = FieldInfo(alias="AccountingCategoryId", default=None)
    """
    Unique identifier of
    [Accounting Category](https://mews-systems.gitbook.io/connector-api/operations/accountingcategories/#accounting-category).
    """

    category_id: Optional[str] = FieldInfo(alias="CategoryId", default=None)
    """Unique identifier of the Product category."""

    charging: Optional[Literal["Once", "PerTimeUnit", "PerPersonPerTimeUnit", "PerPerson"]] = FieldInfo(
        alias="Charging", default=None
    )
    """Once

    PerTimeUnit

    PerPersonPerTimeUnit

    PerPerson
    """

    description: Optional[str] = FieldInfo(alias="Description", default=None)
    """Description of the product. **Deprecated!** Please use Descriptions"""

    descriptions: Optional[Dict[str, str]] = FieldInfo(alias="Descriptions", default=None)
    """All translations of descriptions."""

    external_identifier: Optional[str] = FieldInfo(alias="ExternalIdentifier", default=None)
    """Identifier of the product from external system."""

    external_name: Optional[str] = FieldInfo(alias="ExternalName", default=None)
    """Name of the product meant to be displayed to customer.

    **Deprecated!** Please use ExternalNames
    """

    image_ids: Optional[List[str]] = FieldInfo(alias="ImageIds", default=None)
    """Unique identifier of the product image."""

    is_default: Optional[bool] = FieldInfo(alias="IsDefault", default=None)

    name: Optional[str] = FieldInfo(alias="Name", default=None)
    """Name of the product. **Deprecated!** Please use Names"""

    posting: Optional[Literal["Once", "Daily"]] = FieldInfo(alias="Posting", default=None)
    """Once

    Daily
    """

    pricing: Optional[ProductPricing] = FieldInfo(alias="Pricing", default=None)

    short_name: Optional[str] = FieldInfo(alias="ShortName", default=None)
    """Short name of the product. **Deprecated!** Please use ShortNames"""

    tax_exemption_legal_reference: Optional[str] = FieldInfo(alias="TaxExemptionLegalReference", default=None)
    """Legal reference that states why this product is exempt from tax."""

    tax_exemption_reason: Optional[Literal["IT_N1", "IT_N2_2", "IT_N3_5", "IT_N4", "IT_N5"]] = FieldInfo(
        alias="TaxExemptionReason", default=None
    )
    """IT_N1 (N1 - Escluse ex art.15)

    IT_N2_2 (N2.2 - Non soggette – altri casi)

    IT_N3_5 (N3.5 - Non imponibili – a seguito di dichiarazioni d’intento)

    IT_N4 (N4 - Esenti)

    IT_N5 (N5 - Regime del margine / IVA non esposta in fattura)

    - `IT_N1` - N1 - Escluse ex art.15
    - `IT_N2_2` - N2.2 - Non soggette – altri casi
    - `IT_N3_5` - N3.5 - Non imponibili – a seguito di dichiarazioni d’intento
    - `IT_N4` - N4 - Esenti
    - `IT_N5` - N5 - Regime del margine / IVA non esposta in fattura
    """


class ProductListResponse(BaseModel):
    customer_products: List[CustomerProduct] = FieldInfo(alias="CustomerProducts")
    """Products offered specifically to customers."""

    products: List[Product] = FieldInfo(alias="Products")
    """Products offered with the service."""

    cursor: Optional[str] = FieldInfo(alias="Cursor", default=None)
    """Unique identifier of the last and hence oldest product returned.

    This can be used in `Limitation` in a subsequent request to fetch the next batch
    of older products.
    """
