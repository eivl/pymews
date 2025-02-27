# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["V1ListResourceFeaturesResponse", "ResourceFeature"]


class ResourceFeature(BaseModel):
    classification: Literal[
        "SeaView",
        "RiverView",
        "OceanView",
        "TwinBeds",
        "DoubleBed",
        "RollawayBed",
        "UpperBed",
        "LowerBed",
        "Balcony",
        "AccessibleBathroom",
        "AccessibleRoom",
        "ElevatorAccess",
        "HighFloor",
        "Kitchenette",
        "AirConditioning",
        "PrivateJacuzzi",
        "PrivateSauna",
        "EnsuiteRoom",
        "PrivateBathroom",
        "SharedBathroom",
    ] = FieldInfo(alias="Classification")

    created_utc: datetime = FieldInfo(alias="CreatedUtc")

    descriptions: Dict[str, str] = FieldInfo(alias="Descriptions")
    """All translations of the description."""

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the feature."""

    is_active: bool = FieldInfo(alias="IsActive")
    """Whether the resource feature is still active."""

    names: Dict[str, str] = FieldInfo(alias="Names")
    """All translations of the name."""

    service_id: str = FieldInfo(alias="ServiceId")
    """
    Unique identifier of the
    [Service](https://mews-systems.gitbook.io/connector-api/operations/services/#service).
    """

    short_names: Dict[str, str] = FieldInfo(alias="ShortNames")
    """All translations of the short name."""

    updated_utc: datetime = FieldInfo(alias="UpdatedUtc")


class V1ListResourceFeaturesResponse(BaseModel):
    resource_features: List[ResourceFeature] = FieldInfo(alias="ResourceFeatures")
    """Resource features."""

    cursor: Optional[str] = FieldInfo(alias="Cursor", default=None)
    """Unique identifier of the last and hence oldest resource features returned.

    This can be used in
    [Limitation](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/#limitation)
    in a subsequent request to fetch the next batch of older resource feature.
    """
