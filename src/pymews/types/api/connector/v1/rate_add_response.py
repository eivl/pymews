# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["RateAddResponse", "Rate"]


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


class RateAddResponse(BaseModel):
    rates: Optional[List[Rate]] = FieldInfo(alias="Rates", default=None)
    """Rates that have been added."""
