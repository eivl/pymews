# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["CancellationPolicyGetByRatesParams"]


class CancellationPolicyGetByRatesParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    rate_ids: Required[Annotated[List[str], PropertyInfo(alias="RateIds")]]
    """Unique identifiers of the `Rate`."""

    reservation_end_utc: Required[
        Annotated[Union[str, datetime], PropertyInfo(alias="ReservationEndUtc", format="iso8601")]
    ]
    """End of the reservation interval in UTC timezone in ISO 8601 format."""

    reservation_start_utc: Required[
        Annotated[Union[str, datetime], PropertyInfo(alias="ReservationStartUtc", format="iso8601")]
    ]
    """Start of the reservation interval in UTC timezone in ISO 8601 format."""
