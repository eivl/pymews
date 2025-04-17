# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["ProductGetPricingParams"]


class ProductGetPricingParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    first_time_unit_start_utc: Required[
        Annotated[Union[str, datetime], PropertyInfo(alias="FirstTimeUnitStartUtc", format="iso8601")]
    ]
    """
    Start of the time interval, expressed as the timestamp for the start of the
    first
    [time unit](https://mews-systems.gitbook.io/connector-api/concepts/time-units/),
    in UTC timezone ISO 8601 format.
    """

    last_time_unit_start_utc: Required[
        Annotated[Union[str, datetime], PropertyInfo(alias="LastTimeUnitStartUtc", format="iso8601")]
    ]
    """
    End of the time interval, expressed as the timestamp for the start of the last
    [time unit](https://mews-systems.gitbook.io/connector-api/concepts/time-units/),
    in UTC timezone ISO 8601 format. The maximum size of time interval depends on
    the service's
    [time unit](https://mews-systems.gitbook.io/connector-api/concepts/time-units/):
    100 hours if hours, 100 days if days, or 24 months if months.
    """

    product_id: Required[Annotated[str, PropertyInfo(alias="ProductId")]]
    """Unique identifier of the product."""

    enterprise_ids: Annotated[Optional[List[str]], PropertyInfo(alias="EnterpriseIds")]
    """Unique identifiers of the Enterprises.

    If not specified, the operation returns data for all enterprises within scope of
    the Access Token.
    """
