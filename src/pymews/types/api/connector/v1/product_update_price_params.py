# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["ProductUpdatePriceParams", "PriceUpdate"]


class ProductUpdatePriceParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    price_updates: Required[Annotated[Iterable[PriceUpdate], PropertyInfo(alias="PriceUpdates")]]
    """Price adjustments for specific time intervals."""

    product_id: Required[Annotated[str, PropertyInfo(alias="ProductId")]]
    """Unique identifier of the `Product`."""

    enterprise_id: Annotated[Optional[str], PropertyInfo(alias="EnterpriseId")]
    """Unique identifier of the enterprise.

    Required when using
    [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
    ignored otherwise.
    """


class PriceUpdate(TypedDict, total=False):
    first_time_unit_start_utc: Annotated[
        Union[str, datetime, None], PropertyInfo(alias="FirstTimeUnitStartUtc", format="iso8601")
    ]
    """
    Start of the time interval, expressed as the timestamp for the start of the
    first
    [time unit](https://mews-systems.gitbook.io/connector-api/concepts/time-units),
    in UTC timezone ISO 8601 format.
    """

    last_time_unit_start_utc: Annotated[
        Union[str, datetime, None], PropertyInfo(alias="LastTimeUnitStartUtc", format="iso8601")
    ]
    """
    End of the time interval, expressed as the timestamp for the start of the last
    [time unit](https://mews-systems.gitbook.io/connector-api/concepts/time-units),
    in UTC timezone ISO 8601 format. The maximum size of time interval depends on
    the service's time unit: 367 hours if hours, 367 days if days, or 24 months if
    months.
    """

    value: Annotated[Optional[float], PropertyInfo(alias="Value")]
    """New value of the product on the interval.

    If not specified, removes all price adjustments within the interval.
    """
