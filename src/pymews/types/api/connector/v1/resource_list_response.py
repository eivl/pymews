# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = [
    "ResourceListResponse",
    "ResourceCategory",
    "ResourceCategoryAssignment",
    "ResourceCategoryImageAssignment",
    "ResourceFeatureAssignment",
    "ResourceFeature",
    "Resource",
    "ResourceData",
    "ResourceDataValue",
    "ResourceDataValueSpaceData",
]


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


class ResourceCategoryAssignment(BaseModel):
    category_id: str = FieldInfo(alias="CategoryId")
    """
    Unique identifier of the
    [Resource category](https://mews-systems.gitbook.io/connector-api/operations/#resource-category).
    """

    created_utc: datetime = FieldInfo(alias="CreatedUtc")
    """Creation date and time of the assignment in UTC timezone in ISO 8601 format."""

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the assignment."""

    is_active: bool = FieldInfo(alias="IsActive")
    """Whether the assignment is still active."""

    resource_id: str = FieldInfo(alias="ResourceId")
    """
    Unique identifier of the
    [Resource](https://mews-systems.gitbook.io/connector-api/operations/#resource)
    assigned to the Resource category.
    """

    updated_utc: datetime = FieldInfo(alias="UpdatedUtc")
    """Last update date and time of the assignment in UTC timezone in ISO 8601 format."""


class ResourceCategoryImageAssignment(BaseModel):
    category_id: str = FieldInfo(alias="CategoryId")
    """
    Unique identifier of the
    [Resource category](https://mews-systems.gitbook.io/connector-api/operations/#resource-category).
    """

    created_utc: datetime = FieldInfo(alias="CreatedUtc")
    """Creation date and time of the assignment in UTC timezone in ISO 8601 format."""

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the assignment."""

    image_id: str = FieldInfo(alias="ImageId")
    """Unique identifier of the image assigned to the Resource category."""

    is_active: bool = FieldInfo(alias="IsActive")
    """Whether the assignment is still active."""

    updated_utc: datetime = FieldInfo(alias="UpdatedUtc")
    """Last update date and time of the assignment in UTC timezone in ISO 8601 format."""


class ResourceFeatureAssignment(BaseModel):
    created_utc: datetime = FieldInfo(alias="CreatedUtc")
    """Creation date and time of the assignment in UTC timezone in ISO 8601 format."""

    feature_id: str = FieldInfo(alias="FeatureId")
    """
    Unique identifier of the
    [Resource feature](https://mews-systems.gitbook.io/connector-api/operations/#resource-feature)
    assigned to the Resource.
    """

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the assignment."""

    is_active: bool = FieldInfo(alias="IsActive")
    """Whether the assignment is still active."""

    resource_id: str = FieldInfo(alias="ResourceId")
    """
    Unique identifier of the
    [Resource](https://mews-systems.gitbook.io/connector-api/operations/resources/#resource).
    """

    updated_utc: datetime = FieldInfo(alias="UpdatedUtc")
    """Last update date and time of the assignment in UTC timezone in ISO 8601 format."""


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


class ResourceDataValueSpaceData(BaseModel):
    floor_number: str = FieldInfo(alias="FloorNumber")

    location_notes: Optional[str] = FieldInfo(alias="LocationNotes", default=None)


ResourceDataValue: TypeAlias = Union[ResourceDataValueSpaceData, object, object]


class ResourceData(BaseModel):
    discriminator: Optional[str] = None

    value: Optional[ResourceDataValue] = None


class Resource(BaseModel):
    created_utc: str = FieldInfo(alias="CreatedUtc")
    """Creation date and time of the resource in UTC timezone in ISO 8601 format."""

    data: ResourceData = FieldInfo(alias="Data")
    """Additional data of the resource."""

    descriptions: Dict[str, str] = FieldInfo(alias="Descriptions")
    """All translations of the description."""

    directions: Dict[str, str] = FieldInfo(alias="Directions")
    """All translations of direction."""

    enterprise_id: str = FieldInfo(alias="EnterpriseId")
    """
    Unique identifier of the
    [Enterprise](https://mews-systems.gitbook.io/connector-api/operations/enterprises/#enterprise).
    """

    external_names: Dict[str, str] = FieldInfo(alias="ExternalNames")
    """All translations of external name."""

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the resource."""

    is_active: bool = FieldInfo(alias="IsActive")
    """Whether the resource is still active."""

    name: str = FieldInfo(alias="Name")
    """Name of the resource (e.g. room number)."""

    state: str = FieldInfo(alias="State")
    """State of the resource."""

    updated_utc: str = FieldInfo(alias="UpdatedUtc")
    """Last update date and time of the resource in UTC timezone in ISO 8601 format."""

    parent_resource_id: Optional[str] = FieldInfo(alias="ParentResourceId", default=None)
    """
    Identifier of the parent
    [Resource](https://mews-systems.gitbook.io/connector-api/operations/#resource)
    (e.g. room of a bed).
    """


class ResourceListResponse(BaseModel):
    cursor: Optional[str] = FieldInfo(alias="Cursor", default=None)
    """
    Unique identifier of the item one newer in time order than the items to be
    returned. If Cursor is not specified, i.e. null, then the latest or most recent
    items will be returned.
    """

    resource_categories: Optional[List[ResourceCategory]] = FieldInfo(alias="ResourceCategories", default=None)
    """Categories of resources in the enterprise. **Deprecated!**"""

    resource_category_assignments: Optional[List[ResourceCategoryAssignment]] = FieldInfo(
        alias="ResourceCategoryAssignments", default=None
    )
    """Assignments of resources to categories. **Deprecated!**"""

    resource_category_image_assignments: Optional[List[ResourceCategoryImageAssignment]] = FieldInfo(
        alias="ResourceCategoryImageAssignments", default=None
    )
    """Assignments of images to categories. **Deprecated!**"""

    resource_feature_assignments: Optional[List[ResourceFeatureAssignment]] = FieldInfo(
        alias="ResourceFeatureAssignments", default=None
    )
    """Assignments of resource features to resources. **Deprecated!**"""

    resource_features: Optional[List[ResourceFeature]] = FieldInfo(alias="ResourceFeatures", default=None)
    """Features of resources in the enterprise. **Deprecated!**"""

    resources: Optional[List[Resource]] = FieldInfo(alias="Resources", default=None)
    """The resources of the enterprise."""
