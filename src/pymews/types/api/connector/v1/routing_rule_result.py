# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["RoutingRuleResult", "RoutingRule", "RoutingRuleSelectedStayItems"]


class RoutingRuleSelectedStayItems(BaseModel):
    city_tax: Optional[bool] = FieldInfo(alias="CityTax", default=None)

    nights: Optional[bool] = FieldInfo(alias="Nights", default=None)

    product_category_ids: Optional[List[str]] = FieldInfo(alias="ProductCategoryIds", default=None)


class RoutingRule(BaseModel):
    applicability: Literal["Always", "PrepaidOnly"] = FieldInfo(alias="Applicability")

    company_id: str = FieldInfo(alias="CompanyId")
    """
    Unique identifier of the
    [Company](https://mews-systems.gitbook.io/connector-api/operations/companies/#company)
    routing rule is assigned to.
    """

    company_relation: Literal["PartnerCompany", "TravelAgency"] = FieldInfo(alias="CompanyRelation")

    created_utc: datetime = FieldInfo(alias="CreatedUtc")
    """Creation date and time of the routing rule in UTC timezone in ISO 8601 format."""

    enterprise_id: str = FieldInfo(alias="EnterpriseId")
    """
    Unique identifier of the
    [Enterprise](https://mews-systems.gitbook.io/connector-api/operations/enterprises/#enterprise).
    """

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the routing rule."""

    route_type: Literal["AllStayItems", "SelectedStayItems"] = FieldInfo(alias="RouteType")

    updated_utc: datetime = FieldInfo(alias="UpdatedUtc")
    """
    Last update date and time of the routing rule in UTC timezone in ISO 8601
    format.
    """

    selected_stay_items: Optional[RoutingRuleSelectedStayItems] = FieldInfo(alias="SelectedStayItems", default=None)
    """Specific items to which the routing rule applies.

    Returns only if RouteType value is SelectedStayItems.
    """

    service_id: Optional[str] = FieldInfo(alias="ServiceId", default=None)
    """
    Unique identifier of the
    [Service](https://mews-systems.gitbook.io/connector-api/operations/services/#service)
    routing rule is assigned to.
    """


class RoutingRuleResult(BaseModel):
    routing_rules: List[RoutingRule] = FieldInfo(alias="RoutingRules")
    """Collection of Routing rules."""

    cursor: Optional[str] = FieldInfo(alias="Cursor", default=None)
    """
    Unique identifier of the item one newer in time order than the items to be
    returned. If Cursor is not specified, i.e. null, then the latest or most recent
    items will be returned.
    """
