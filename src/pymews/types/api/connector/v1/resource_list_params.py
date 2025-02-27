# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["ResourceListParams", "Limitation", "CreatedUtc", "Extent", "UpdatedUtc"]


class ResourceListParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    limitation: Required[Annotated[Limitation, PropertyInfo(alias="Limitation")]]
    """Limitation on the quantity of data returned."""

    created_utc: Annotated[Optional[CreatedUtc], PropertyInfo(alias="CreatedUtc")]

    enterprise_ids: Annotated[Optional[List[str]], PropertyInfo(alias="EnterpriseIds")]
    """Unique identifiers of the Enterprises.

    If not specified, the operation returns data for all enterprises within scope of
    the Access Token.
    """

    extent: Annotated[Optional[Extent], PropertyInfo(alias="Extent")]
    """Extent of data to be returned."""

    names: Annotated[Optional[List[str]], PropertyInfo(alias="Names")]

    resource_ids: Annotated[Optional[List[str]], PropertyInfo(alias="ResourceIds")]
    """
    Unique identifiers of the requested
    [Resources](https://mews-systems.gitbook.io/connector-api/operations/#resource).
    """

    updated_utc: Annotated[Optional[UpdatedUtc], PropertyInfo(alias="UpdatedUtc")]


class Limitation(TypedDict, total=False):
    count: Required[Annotated[int, PropertyInfo(alias="Count")]]

    cursor: Annotated[Optional[str], PropertyInfo(alias="Cursor")]


class CreatedUtc(TypedDict, total=False):
    end_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="EndUtc", format="iso8601")]

    start_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="StartUtc", format="iso8601")]


class Extent(TypedDict, total=False):
    inactive: Annotated[bool, PropertyInfo(alias="Inactive")]

    resource_categories: Annotated[bool, PropertyInfo(alias="ResourceCategories")]

    resource_category_assignments: Annotated[bool, PropertyInfo(alias="ResourceCategoryAssignments")]

    resource_category_image_assignments: Annotated[bool, PropertyInfo(alias="ResourceCategoryImageAssignments")]

    resource_feature_assignments: Annotated[bool, PropertyInfo(alias="ResourceFeatureAssignments")]

    resource_features: Annotated[bool, PropertyInfo(alias="ResourceFeatures")]

    resources: Annotated[bool, PropertyInfo(alias="Resources")]


class UpdatedUtc(TypedDict, total=False):
    end_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="EndUtc", format="iso8601")]

    start_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="StartUtc", format="iso8601")]
