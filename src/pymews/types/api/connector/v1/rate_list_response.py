# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = [
    "RateListResponse",
    "RateGroup",
    "RateRestrictions",
    "RateRestrictionsDateRestriction",
    "RateRestrictionsEarlinessRestriction",
    "RateRestrictionsLengthRestriction",
    "Rate",
]


class RateGroup(BaseModel):
    external_identifier: Optional[str] = FieldInfo(alias="ExternalIdentifier", default=None)
    """External identifier of the rate group."""

    id: Optional[str] = FieldInfo(alias="Id", default=None)
    """Unique identifier of the rate group."""

    is_active: Optional[bool] = FieldInfo(alias="IsActive", default=None)
    """Whether the rate group is still active."""

    name: Optional[str] = FieldInfo(alias="Name", default=None)
    """Name of the rate group."""

    service_id: Optional[str] = FieldInfo(alias="ServiceId", default=None)
    """Unique identifier of the Service that the rate group belongs to."""


class RateRestrictionsDateRestriction(BaseModel):
    days: Optional[List[str]] = FieldInfo(alias="Days", default=None)
    """The restricted days of week."""

    end_utc: Optional[str] = FieldInfo(alias="EndUtc", default=None)
    """End of the rate restriction in UTC timezone in ISO 8601 format."""

    external_identifier: Optional[str] = FieldInfo(alias="ExternalIdentifier", default=None)
    """Identifiers of from external systems."""

    id: Optional[str] = FieldInfo(alias="Id", default=None)
    """Unique identifier of the rate restriction."""

    is_inherited: Optional[bool] = FieldInfo(alias="IsInherited", default=None)
    """Whether the rate restriction is inherited from the parent rate."""

    rate_id: Optional[str] = FieldInfo(alias="RateId", default=None)
    """Unique identifier of the rate."""

    start_utc: Optional[str] = FieldInfo(alias="StartUtc", default=None)
    """Start of the rate restriction in UTC timezone in ISO 8601 format."""


class RateRestrictionsEarlinessRestriction(BaseModel):
    days: Optional[List[str]] = FieldInfo(alias="Days", default=None)
    """The restricted days of week."""

    end_utc: Optional[str] = FieldInfo(alias="EndUtc", default=None)
    """End of the rate restriction in UTC timezone in ISO 8601 format."""

    external_identifier: Optional[str] = FieldInfo(alias="ExternalIdentifier", default=None)
    """Identifiers of from external systems."""

    id: Optional[str] = FieldInfo(alias="Id", default=None)
    """Unique identifier of the rate restriction."""

    is_inherited: Optional[bool] = FieldInfo(alias="IsInherited", default=None)
    """Whether the rate restriction is inherited from the parent rate."""

    max_advance: Optional[str] = FieldInfo(alias="MaxAdvance", default=None)
    """
    The maximum time before the reservation starts, you can reserve in ISO 8601
    duration format.
    """

    min_advance: Optional[str] = FieldInfo(alias="MinAdvance", default=None)
    """
    The minimum time before the reservation starts, you can reserve in ISO 8601
    duration format.
    """

    rate_id: Optional[str] = FieldInfo(alias="RateId", default=None)
    """Unique identifier of the rate."""

    start_utc: Optional[str] = FieldInfo(alias="StartUtc", default=None)
    """Start of the rate restriction in UTC timezone in ISO 8601 format."""


class RateRestrictionsLengthRestriction(BaseModel):
    days: Optional[List[str]] = FieldInfo(alias="Days", default=None)
    """The restricted days of week."""

    end_utc: Optional[str] = FieldInfo(alias="EndUtc", default=None)
    """End of the rate restriction in UTC timezone in ISO 8601 format."""

    external_identifier: Optional[str] = FieldInfo(alias="ExternalIdentifier", default=None)
    """Identifiers of from external systems."""

    id: Optional[str] = FieldInfo(alias="Id", default=None)
    """Unique identifier of the rate restriction."""

    is_inherited: Optional[bool] = FieldInfo(alias="IsInherited", default=None)
    """Whether the rate restriction is inherited from the parent rate."""

    max_length: Optional[str] = FieldInfo(alias="MaxLength", default=None)
    """Maximal reservation length in ISO 8601 duration format."""

    min_length: Optional[str] = FieldInfo(alias="MinLength", default=None)
    """Minimal reservation length in ISO 8601 duration format."""

    rate_id: Optional[str] = FieldInfo(alias="RateId", default=None)
    """Unique identifier of the rate."""

    start_utc: Optional[str] = FieldInfo(alias="StartUtc", default=None)
    """Start of the rate restriction in UTC timezone in ISO 8601 format."""


class RateRestrictions(BaseModel):
    date_restrictions: List[RateRestrictionsDateRestriction] = FieldInfo(alias="DateRestrictions")
    """Date restrictions for the rate."""

    earliness_restrictions: List[RateRestrictionsEarlinessRestriction] = FieldInfo(alias="EarlinessRestrictions")
    """
    Earliness restrictions for the rates that are only available up to before
    arrival.
    """

    length_restrictions: List[RateRestrictionsLengthRestriction] = FieldInfo(alias="LengthRestrictions")
    """Length restrictions for the rate."""


class Rate(BaseModel):
    group_id: str = FieldInfo(alias="GroupId")
    """Unique identifier of `Rate Group` where the rate belongs."""

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the rate."""

    is_active: bool = FieldInfo(alias="IsActive")
    """Indicates if this rate is active."""

    is_base_rate: bool = FieldInfo(alias="IsBaseRate")
    """Indicates if this is a base rate."""

    is_enabled: bool = FieldInfo(alias="IsEnabled")
    """Indicates if this rate is currently available to customers."""

    is_public: bool = FieldInfo(alias="IsPublic")
    """Indicates if this rate is publicly available."""

    names: Dict[str, str] = FieldInfo(alias="Names")
    """All translations of the name."""

    service_id: str = FieldInfo(alias="ServiceId")
    """Unique identifier of the `Service`."""

    type: Literal["Public", "Private", "AvailabilityBlock"] = FieldInfo(alias="Type")
    """Public

    Private

    AvailabilityBlock
    """

    updated_utc: datetime = FieldInfo(alias="UpdatedUtc")
    """Interval in which the rates were updated."""

    base_rate_id: Optional[str] = FieldInfo(alias="BaseRateId", default=None)
    """Unique identifier of the base `Rate`."""

    business_segment_id: Optional[str] = FieldInfo(alias="BusinessSegmentId", default=None)
    """Unique identifier of the `Business Segment`."""

    description: Optional[Dict[str, str]] = FieldInfo(alias="Description", default=None)
    """All translations of the description of the rate."""

    external_identifier: Optional[str] = FieldInfo(alias="ExternalIdentifier", default=None)
    """Identifier of the rate from external system."""

    external_names: Optional[Dict[str, str]] = FieldInfo(alias="ExternalNames", default=None)
    """All translations of the external name of the rate."""

    name: Optional[str] = FieldInfo(alias="Name", default=None)
    """Name of the rate (in the default language)."""

    short_name: Optional[str] = FieldInfo(alias="ShortName", default=None)
    """Short name of the rate (in the default language)."""

    tax_exemption_legal_reference: Optional[str] = FieldInfo(alias="TaxExemptionLegalReference", default=None)
    """Legal reference that states why this rate is exempt from tax."""

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


class RateListResponse(BaseModel):
    rate_groups: List[RateGroup] = FieldInfo(alias="RateGroups")
    """Rate groups of the default service."""

    rate_restrictions: RateRestrictions = FieldInfo(alias="RateRestrictions")

    rates: List[Rate] = FieldInfo(alias="Rates")
    """Rates of the default service."""

    cursor: Optional[str] = FieldInfo(alias="Cursor", default=None)
    """
    Unique identifier of the item one newer in time order than the items to be
    returned. If Cursor is not specified, i.e. null, then the latest or most recent
    items will be returned.
    """
