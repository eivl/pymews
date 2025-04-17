# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["ProductListParams", "Limitation", "UpdatedUtc"]


class ProductListParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    limitation: Required[Annotated[Limitation, PropertyInfo(alias="Limitation")]]
    """Limitation on the quantity of data returned."""

    service_ids: Required[Annotated[List[str], PropertyInfo(alias="ServiceIds")]]
    """
    Unique identifiers of the
    [Services](https://mews-systems.gitbook.io/connector-api/operations/services/#service).
    """

    enterprise_ids: Annotated[Optional[List[str]], PropertyInfo(alias="EnterpriseIds")]
    """Unique identifiers of the Enterprises.

    If not specified, the operation returns data for all enterprises within scope of
    the Access Token.
    """

    include_default: Annotated[Optional[bool], PropertyInfo(alias="IncludeDefault")]
    """Whether or not to include default products for the service, i.e.

    products which are standard includes and not true extras. For example, the
    night's stay would be the default product for a room reservation. These may be
    useful for accounting purposes but should not be displayed to customers for
    selection. If `ProductIds` are provided, `IncludeDefault` defaults to true,
    otherwise it defaults to false.
    """

    product_ids: Annotated[Optional[List[str]], PropertyInfo(alias="ProductIds")]
    """Unique identifiers of the product."""

    updated_utc: Annotated[Optional[UpdatedUtc], PropertyInfo(alias="UpdatedUtc")]
    """Interval in which the products were updated."""


class Limitation(TypedDict, total=False):
    count: Required[Annotated[int, PropertyInfo(alias="Count")]]

    cursor: Annotated[Optional[str], PropertyInfo(alias="Cursor")]


class UpdatedUtc(TypedDict, total=False):
    end_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="EndUtc", format="iso8601")]

    start_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="StartUtc", format="iso8601")]
