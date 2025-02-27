# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "V1ListRulesResponse",
    "BusinessSegment",
    "RateGroup",
    "Rate",
    "ResourceCategory",
    "RuleAction",
    "RuleActionData",
    "RuleActionDataValue",
    "Rule",
    "RuleConditions",
    "RuleConditionsBusinessSegmentID",
    "RuleConditionsOrigin",
    "RuleConditionsRateGroupID",
    "RuleConditionsRateID",
    "RuleConditionsResourceCategoryID",
    "RuleConditionsResourceCategoryType",
    "RuleConditionsTravelAgencyID",
]


class BusinessSegment(BaseModel):
    created_utc: datetime = FieldInfo(alias="CreatedUtc")
    """
    Creation date and time of the business segment in UTC timezone in ISO 8601
    format.
    """

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the business segment."""

    is_active: bool = FieldInfo(alias="IsActive")
    """Whether the business segment is still active."""

    name: str = FieldInfo(alias="Name")
    """Name of the business segment."""

    service_id: str = FieldInfo(alias="ServiceId")
    """Unique identifier of the `Service`."""

    updated_utc: datetime = FieldInfo(alias="UpdatedUtc")
    """
    Last update date and time of the business segment in UTC timezone in ISO 8601
    format.
    """


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


class Rate(BaseModel):
    group_id: str = FieldInfo(alias="GroupId")
    """Unique identifier of `Rate Group` where the rate belongs."""

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the rate."""

    is_active: bool = FieldInfo(alias="IsActive")
    """Whether the rate is still active."""

    is_base_rate: bool = FieldInfo(alias="IsBaseRate")
    """Whether the rate is a base rate."""

    is_enabled: bool = FieldInfo(alias="IsEnabled")
    """Whether the rate is currently available to customers."""

    is_public: bool = FieldInfo(alias="IsPublic")
    """Whether the rate is publicly available."""

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


class RuleActionDataValue(BaseModel):
    action_type: Optional[str] = FieldInfo(alias="ActionType", default=None)

    product_id: Optional[str] = FieldInfo(alias="ProductId", default=None)


class RuleActionData(BaseModel):
    discriminator: Optional[Literal["Product"]] = None

    value: Optional[RuleActionDataValue] = None


class RuleAction(BaseModel):
    data: Optional[RuleActionData] = FieldInfo(alias="Data", default=None)
    """Additional information about action."""

    id: Optional[str] = FieldInfo(alias="Id", default=None)
    """Unique identifier of the rule action."""

    rule_id: Optional[str] = FieldInfo(alias="RuleId", default=None)
    """Unique identifier of the rule."""


class RuleConditionsBusinessSegmentID(BaseModel):
    condition_type: Optional[Literal["Equals", "NotEquals"]] = FieldInfo(alias="ConditionType", default=None)

    value: Optional[str] = FieldInfo(alias="Value", default=None)


class RuleConditionsOrigin(BaseModel):
    condition_type: Optional[Literal["Equals", "NotEquals"]] = FieldInfo(alias="ConditionType", default=None)

    value: Optional[str] = FieldInfo(alias="Value", default=None)


class RuleConditionsRateGroupID(BaseModel):
    condition_type: Optional[Literal["Equals", "NotEquals"]] = FieldInfo(alias="ConditionType", default=None)

    value: Optional[str] = FieldInfo(alias="Value", default=None)


class RuleConditionsRateID(BaseModel):
    condition_type: Optional[Literal["Equals", "NotEquals"]] = FieldInfo(alias="ConditionType", default=None)

    value: Optional[str] = FieldInfo(alias="Value", default=None)


class RuleConditionsResourceCategoryID(BaseModel):
    condition_type: Optional[Literal["Equals", "NotEquals"]] = FieldInfo(alias="ConditionType", default=None)

    value: Optional[str] = FieldInfo(alias="Value", default=None)


class RuleConditionsResourceCategoryType(BaseModel):
    condition_type: Optional[Literal["Equals", "NotEquals"]] = FieldInfo(alias="ConditionType", default=None)

    value: Optional[str] = FieldInfo(alias="Value", default=None)


class RuleConditionsTravelAgencyID(BaseModel):
    condition_type: Optional[Literal["Equals", "NotEquals"]] = FieldInfo(alias="ConditionType", default=None)

    value: Optional[str] = FieldInfo(alias="Value", default=None)


class RuleConditions(BaseModel):
    business_segment_id: Optional[RuleConditionsBusinessSegmentID] = FieldInfo(alias="BusinessSegmentId", default=None)

    maximum_time_unit_count: Optional[int] = FieldInfo(alias="MaximumTimeUnitCount", default=None)

    minimum_time_unit_count: Optional[int] = FieldInfo(alias="MinimumTimeUnitCount", default=None)

    origin: Optional[RuleConditionsOrigin] = FieldInfo(alias="Origin", default=None)

    rate_group_id: Optional[RuleConditionsRateGroupID] = FieldInfo(alias="RateGroupId", default=None)

    rate_id: Optional[RuleConditionsRateID] = FieldInfo(alias="RateId", default=None)

    resource_category_id: Optional[RuleConditionsResourceCategoryID] = FieldInfo(
        alias="ResourceCategoryId", default=None
    )

    resource_category_type: Optional[RuleConditionsResourceCategoryType] = FieldInfo(
        alias="ResourceCategoryType", default=None
    )

    travel_agency_id: Optional[RuleConditionsTravelAgencyID] = FieldInfo(alias="TravelAgencyId", default=None)


class Rule(BaseModel):
    created_utc: datetime = FieldInfo(alias="CreatedUtc")
    """Creation date and time of the rule in UTC timezone in ISO 8601 format."""

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the rule."""

    service_id: str = FieldInfo(alias="ServiceId")
    """
    Unique identifier of the
    [Service](https://mews-systems.gitbook.io/connector-api/operations/services/#service)
    the rule is assigned to.
    """

    updated_utc: datetime = FieldInfo(alias="UpdatedUtc")
    """Last update date and time of the rule in UTC timezone in ISO 8601 format."""

    conditions: Optional[RuleConditions] = FieldInfo(alias="Conditions", default=None)
    """Conditions of the rule."""


class V1ListRulesResponse(BaseModel):
    business_segments: Optional[List[BusinessSegment]] = FieldInfo(alias="BusinessSegments", default=None)
    """Business segments used in conditions."""

    cursor: Optional[str] = FieldInfo(alias="Cursor", default=None)
    """
    Unique identifier of the item one newer in time order than the items to be
    returned. If Cursor is not specified, i.e. null, then the latest or most recent
    items will be returned.
    """

    rate_groups: Optional[List[RateGroup]] = FieldInfo(alias="RateGroups", default=None)
    """Rate groups used in conditions."""

    rates: Optional[List[Rate]] = FieldInfo(alias="Rates", default=None)
    """Rates used in conditions."""

    resource_categories: Optional[List[ResourceCategory]] = FieldInfo(alias="ResourceCategories", default=None)
    """Resource categories used in conditions."""

    rule_actions: Optional[List[RuleAction]] = FieldInfo(alias="RuleActions", default=None)
    """Rule actions applied in rules."""

    rules: Optional[List[Rule]] = FieldInfo(alias="Rules", default=None)
    """Rules used with reservation creations and modifications."""
