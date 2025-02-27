# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["V1ListResourceCategoriesResponse", "ResourceCategory"]


class ResourceCategory(BaseModel):
    capacity: int = FieldInfo(alias="Capacity")

    classification: Literal[
        "StandardSingle",
        "StandardDouble",
        "SuperiorTwin",
        "SuperiorDouble",
        "JuniorSuite",
        "SharedOrDorm",
        "Other",
        "SuperiorSingle",
        "Triple",
        "Family",
        "StandardTwin",
        "Studio",
        "SuperiorTripleRoom",
        "OneBedroomApartment",
        "ThreeBedroomsApartment",
        "TwoBedroomsApartment",
    ] = FieldInfo(alias="Classification")

    descriptions: Dict[str, str] = FieldInfo(alias="Descriptions")
    """All translations of the description."""

    enterprise_id: str = FieldInfo(alias="EnterpriseId")
    """
    Unique identifier of the
    [Enterprise](https://mews-systems.gitbook.io/connector-api/operations/enterprises/#enterprise).
    """

    extra_capacity: int = FieldInfo(alias="ExtraCapacity")
    """Extra capacity that can be served (e.g. extra bed count)."""

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the category."""

    is_active: bool = FieldInfo(alias="IsActive")
    """Whether the category is still active."""

    names: Dict[str, str] = FieldInfo(alias="Names")
    """All translations of the name."""

    ordering: int = FieldInfo(alias="Ordering")

    service_id: str = FieldInfo(alias="ServiceId")
    """
    Unique identifier of the
    [Service](https://mews-systems.gitbook.io/connector-api/operations/services/#service)
    of the resource category.
    """

    short_names: Dict[str, str] = FieldInfo(alias="ShortNames")
    """All translations of the short name."""

    type: Literal[
        "Room",
        "Bed",
        "Dorm",
        "Apartment",
        "Suite",
        "Villa",
        "Site",
        "Office",
        "MeetingRoom",
        "ParkingSpot",
        "Desk",
        "TeamArea",
        "Membership",
        "Tent",
        "CaravanOrRV",
        "UnequippedCampsite",
        "Bike",
        "ExtraBed",
        "Cot",
        "Crib",
        "ConferenceRoom",
        "Rooftop",
        "Garden",
        "Restaurant",
        "Amphitheater",
        "PrivateSpaces",
    ] = FieldInfo(alias="Type")

    accounting_category_id: Optional[str] = FieldInfo(alias="AccountingCategoryId", default=None)

    external_identifier: Optional[str] = FieldInfo(alias="ExternalIdentifier", default=None)
    """Identifier of the resource category from external system."""


class V1ListResourceCategoriesResponse(BaseModel):
    resource_categories: List[ResourceCategory] = FieldInfo(alias="ResourceCategories")
    """Resource categories of the resources."""

    cursor: Optional[str] = FieldInfo(alias="Cursor", default=None)
    """Unique identifier of the last and hence oldest resource category returned.

    This can be used in
    [Limitation](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/#limitation)
    in a subsequent request to fetch the next batch of older resource categories.
    """
