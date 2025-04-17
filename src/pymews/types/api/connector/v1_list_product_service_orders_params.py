# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["V1ListProductServiceOrdersParams", "Limitation", "UpdatedUtc"]


class V1ListProductServiceOrdersParams(TypedDict, total=False):
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

    account_ids: Annotated[Optional[List[str]], PropertyInfo(alias="AccountIds")]

    enterprise_ids: Annotated[Optional[List[str]], PropertyInfo(alias="EnterpriseIds")]
    """Unique identifiers of the Enterprises.

    If not specified, the operation returns data for all enterprises within scope of
    the Access Token.
    """

    linked_reservation_ids: Annotated[Optional[List[str]], PropertyInfo(alias="LinkedReservationIds")]

    product_service_order_ids: Annotated[Optional[List[str]], PropertyInfo(alias="ProductServiceOrderIds")]
    """
    Unique identifiers of the
    [Product service order](https://mews-systems.gitbook.io/connector-api/operations/#product-service-order).
    """

    states: Annotated[
        Optional[List[Literal["Inquired", "Confirmed", "Started", "Processed", "Canceled", "Optional", "Requested"]]],
        PropertyInfo(alias="States"),
    ]
    """A list of product service order states to filter by."""

    updated_utc: Annotated[Optional[UpdatedUtc], PropertyInfo(alias="UpdatedUtc")]


class Limitation(TypedDict, total=False):
    count: Required[Annotated[int, PropertyInfo(alias="Count")]]

    cursor: Annotated[Optional[str], PropertyInfo(alias="Cursor")]


class UpdatedUtc(TypedDict, total=False):
    end_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="EndUtc", format="iso8601")]

    start_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="StartUtc", format="iso8601")]
