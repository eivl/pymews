# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = [
    "RoutingRuleUpdateParams",
    "RoutingRuleUpdate",
    "RoutingRuleUpdateApplicability",
    "RoutingRuleUpdateAssignmentTargetType",
    "RoutingRuleUpdateCompanyID",
    "RoutingRuleUpdateCompanyRelation",
    "RoutingRuleUpdateRouteType",
    "RoutingRuleUpdateSelectedStayItems",
    "RoutingRuleUpdateSelectedStayItemsCityTax",
    "RoutingRuleUpdateSelectedStayItemsNights",
    "RoutingRuleUpdateSelectedStayItemsProductCategoryIDs",
    "RoutingRuleUpdateServiceID",
]


class RoutingRuleUpdateParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    routing_rule_updates: Required[Annotated[Iterable[RoutingRuleUpdate], PropertyInfo(alias="RoutingRuleUpdates")]]
    """Collection of Routing rules to be updated."""


class RoutingRuleUpdateApplicability(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class RoutingRuleUpdateAssignmentTargetType(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class RoutingRuleUpdateCompanyID(TypedDict, total=False):
    value: Annotated[str, PropertyInfo(alias="Value")]


class RoutingRuleUpdateCompanyRelation(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class RoutingRuleUpdateRouteType(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class RoutingRuleUpdateSelectedStayItemsCityTax(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class RoutingRuleUpdateSelectedStayItemsNights(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class RoutingRuleUpdateSelectedStayItemsProductCategoryIDs(TypedDict, total=False):
    value: Annotated[Optional[List[str]], PropertyInfo(alias="Value")]


class RoutingRuleUpdateSelectedStayItems(TypedDict, total=False):
    city_tax: Annotated[Optional[RoutingRuleUpdateSelectedStayItemsCityTax], PropertyInfo(alias="CityTax")]

    nights: Annotated[Optional[RoutingRuleUpdateSelectedStayItemsNights], PropertyInfo(alias="Nights")]

    product_category_ids: Annotated[
        Optional[RoutingRuleUpdateSelectedStayItemsProductCategoryIDs], PropertyInfo(alias="ProductCategoryIds")
    ]


class RoutingRuleUpdateServiceID(TypedDict, total=False):
    value: Annotated[str, PropertyInfo(alias="Value")]


class RoutingRuleUpdate(TypedDict, total=False):
    routing_rule_id: Required[Annotated[str, PropertyInfo(alias="RoutingRuleId")]]

    applicability: Annotated[Optional[RoutingRuleUpdateApplicability], PropertyInfo(alias="Applicability")]

    assignment_target_type: Annotated[
        Optional[RoutingRuleUpdateAssignmentTargetType], PropertyInfo(alias="AssignmentTargetType")
    ]

    company_id: Annotated[Optional[RoutingRuleUpdateCompanyID], PropertyInfo(alias="CompanyId")]

    company_relation: Annotated[Optional[RoutingRuleUpdateCompanyRelation], PropertyInfo(alias="CompanyRelation")]

    route_type: Annotated[Optional[RoutingRuleUpdateRouteType], PropertyInfo(alias="RouteType")]

    selected_stay_items: Annotated[
        Optional[RoutingRuleUpdateSelectedStayItems], PropertyInfo(alias="SelectedStayItems")
    ]

    service_id: Annotated[Optional[RoutingRuleUpdateServiceID], PropertyInfo(alias="ServiceId")]
