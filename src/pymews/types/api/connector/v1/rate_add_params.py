# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = [
    "RateAddParams",
    "Rate",
    "RatePricing",
    "RatePricingBaseRatePricing",
    "RatePricingBaseRatePricingAmount",
    "RatePricingDependentRatePricing",
]


class RateAddParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    rates: Required[Annotated[Iterable[Rate], PropertyInfo(alias="Rates")]]
    """Information about rates to be created."""

    enterprise_id: Annotated[Optional[str], PropertyInfo(alias="EnterpriseId")]
    """Unique identifier of the enterprise.

    Required when using
    [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
    ignored otherwise.
    """


class RatePricingBaseRatePricingAmount(TypedDict, total=False):
    currency: Required[Annotated[str, PropertyInfo(alias="Currency")]]

    tax_codes: Required[Annotated[List[str], PropertyInfo(alias="TaxCodes")]]

    gross_value: Annotated[Optional[float], PropertyInfo(alias="GrossValue")]

    net_value: Annotated[Optional[float], PropertyInfo(alias="NetValue")]


class RatePricingBaseRatePricing(TypedDict, total=False):
    amount: Required[Annotated[RatePricingBaseRatePricingAmount, PropertyInfo(alias="Amount")]]
    """Price of the product that overrides the price defined in Mews."""

    extra_occupancy_adjustment: Annotated[float, PropertyInfo(alias="ExtraOccupancyAdjustment")]
    """
    This is the amount added to the price when the Space Category Capacity is
    exceeded.
    """

    negative_occupancy_adjustment: Annotated[float, PropertyInfo(alias="NegativeOccupancyAdjustment")]
    """
    This is the amount added to the price when occupancy of the space is less than
    the Space Category Capacity. To provide a discount price for under-occupancy,
    simply use a negative value.
    """


class RatePricingDependentRatePricing(TypedDict, total=False):
    base_rate_id: Required[Annotated[str, PropertyInfo(alias="BaseRateId")]]
    """Unique identifier of the base rate."""

    absolute_adjustment: Annotated[float, PropertyInfo(alias="AbsoluteAdjustment")]
    """Specific amount which shows the difference between this rate and the base rate."""

    relative_adjustment: Annotated[float, PropertyInfo(alias="RelativeAdjustment")]
    """Relative amount which shows the difference between this rate and the base rate."""


class RatePricing(TypedDict, total=False):
    base_rate_pricing: Annotated[Optional[RatePricingBaseRatePricing], PropertyInfo(alias="BaseRatePricing")]
    """Additional data for rates with base rate pricing.

    Used when `PricingType` is `BaseRatePricing`. Defaults are applied if not
    specified: amount is set to 10000 in default Enterprise's currency and with its
    default accommodation tax rate code.
    """

    dependent_rate_pricing: Annotated[
        Optional[RatePricingDependentRatePricing], PropertyInfo(alias="DependentRatePricing")
    ]
    """Additional data for rate with dependent rate pricing.

    Required when `PricingType` is `DependentRatePricing`.
    """


class Rate(TypedDict, total=False):
    names: Required[Annotated[Dict[str, str], PropertyInfo(alias="Names")]]
    """All translations of the name of the rate."""

    pricing_type: Required[
        Annotated[Literal["BaseRatePricing", "DependentRatePricing"], PropertyInfo(alias="PricingType")]
    ]
    """BaseRatePricing

    DependentRatePricing
    """

    rate_group_id: Required[Annotated[str, PropertyInfo(alias="RateGroupId")]]
    """Unique identifier of the rate group under which rate is assigned."""

    service_id: Required[Annotated[str, PropertyInfo(alias="ServiceId")]]
    """Unique identifier of the service."""

    accounting_category_id: Annotated[Optional[str], PropertyInfo(alias="AccountingCategoryId")]
    """Unique identifier of the accounting category the rate belongs to."""

    business_segment_id: Annotated[Optional[str], PropertyInfo(alias="BusinessSegmentId")]
    """Unique identifier of the business segment."""

    descriptions: Annotated[Optional[Dict[str, str]], PropertyInfo(alias="Descriptions")]
    """All translations of the description."""

    external_identifier: Annotated[Optional[str], PropertyInfo(alias="ExternalIdentifier")]
    """Identifier of the rate from external system."""

    external_names: Annotated[Optional[Dict[str, str]], PropertyInfo(alias="ExternalNames")]
    """All translations of the external name of the rate."""

    is_enabled: Annotated[Optional[bool], PropertyInfo(alias="IsEnabled")]
    """Whether the rate is available to customers.

    `false` will be used as a default when not provided.
    """

    pricing: Annotated[Optional[RatePricing], PropertyInfo(alias="Pricing")]
    """Contains additional data about pricing of the rate."""

    short_names: Annotated[Optional[Dict[str, str]], PropertyInfo(alias="ShortNames")]
    """All translations of the short name of the rate."""

    type: Annotated[Literal["Public", "Private"], PropertyInfo(alias="Type")]
    """Public

    Private
    """
