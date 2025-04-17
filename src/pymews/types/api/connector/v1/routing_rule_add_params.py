# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["RoutingRuleAddParams", "RoutingRule", "RoutingRuleSelectedStayItems"]


class RoutingRuleAddParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    routing_rules: Required[Annotated[Iterable[RoutingRule], PropertyInfo(alias="RoutingRules")]]
    """Collection of Routing rules to be added."""


class RoutingRuleSelectedStayItems(TypedDict, total=False):
    city_tax: Annotated[bool, PropertyInfo(alias="CityTax")]

    nights: Annotated[bool, PropertyInfo(alias="Nights")]

    product_category_ids: Annotated[Optional[List[str]], PropertyInfo(alias="ProductCategoryIds")]


class RoutingRule(TypedDict, total=False):
    applicability: Required[Annotated[Literal["Always", "PrepaidOnly"], PropertyInfo(alias="Applicability")]]

    company_id: Required[Annotated[str, PropertyInfo(alias="CompanyId")]]

    company_relation: Required[
        Annotated[Literal["PartnerCompany", "TravelAgency"], PropertyInfo(alias="CompanyRelation")]
    ]

    route_type: Required[Annotated[Literal["AllStayItems", "SelectedStayItems"], PropertyInfo(alias="RouteType")]]

    service_id: Required[Annotated[str, PropertyInfo(alias="ServiceId")]]

    assignment_target_type: Annotated[
        Optional[Literal["AllStayItems", "SelectedStayItems"]], PropertyInfo(alias="AssignmentTargetType")
    ]

    selected_stay_items: Annotated[Optional[RoutingRuleSelectedStayItems], PropertyInfo(alias="SelectedStayItems")]
