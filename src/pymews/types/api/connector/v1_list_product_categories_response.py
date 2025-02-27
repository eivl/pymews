# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["V1ListProductCategoriesResponse", "ProductCategory", "ProductCategoryParentProductCategory"]


class ProductCategoryParentProductCategory(BaseModel):
    id: str = FieldInfo(alias="Id")

    names: Dict[str, str] = FieldInfo(alias="Names")


class ProductCategory(BaseModel):
    created_utc: datetime = FieldInfo(alias="CreatedUtc")
    """
    Date and time of the product category creation in UTC timezone in ISO 8601
    format.
    """

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the category."""

    names: Dict[str, str] = FieldInfo(alias="Names")
    """All translations of the name."""

    ordering: int = FieldInfo(alias="Ordering")
    """
    Ordering of the category, lower number corresponds to lower category (note that
    neither uniqueness nor continuous sequence is guaranteed).
    """

    service_id: str = FieldInfo(alias="ServiceId")
    """
    Unique identifier of the
    [Service](https://mews-systems.gitbook.io/connector-api/operations/services/#service)
    of the resource category.
    """

    updated_utc: datetime = FieldInfo(alias="UpdatedUtc")
    """
    Date and time of the product category update in UTC timezone in ISO 8601 format.
    """

    descriptions: Optional[Dict[str, str]] = FieldInfo(alias="Descriptions", default=None)
    """All translations of the description."""

    parent_product_category: Optional[ProductCategoryParentProductCategory] = FieldInfo(
        alias="ParentProductCategory", default=None
    )
    """
    [Parent product category](https://mews-systems.gitbook.io/connector-api/operations/#parent-product-category).
    """

    short_names: Optional[Dict[str, str]] = FieldInfo(alias="ShortNames", default=None)
    """All translations of the short name."""


class V1ListProductCategoriesResponse(BaseModel):
    product_categories: List[ProductCategory] = FieldInfo(alias="ProductCategories")
    """Product categories."""

    cursor: Optional[str] = FieldInfo(alias="Cursor", default=None)
    """
    Unique identifier of the item one newer in time order than the items to be
    returned. If Cursor is not specified, i.e. null, then the latest or most recent
    items will be returned.
    """
