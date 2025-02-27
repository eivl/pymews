# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["ReservationUpdateIntervalParams"]


class ReservationUpdateIntervalParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    charge_cancellation_fee: Required[Annotated[bool, PropertyInfo(alias="ChargeCancellationFee")]]
    """Whether cancellation fee should be charged for potentially canceled nights."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    reservation_id: Required[Annotated[str, PropertyInfo(alias="ReservationId")]]
    """Unique identifier of the reservation to be updated."""

    end_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="EndUtc", format="iso8601")]
    """New reservation end in UTC timezone in ISO 8601 format."""

    enterprise_id: Annotated[Optional[str], PropertyInfo(alias="EnterpriseId")]
    """Unique identifier of the enterprise.

    Required when using
    [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
    ignored otherwise.
    """

    start_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="StartUtc", format="iso8601")]
    """New reservation start in UTC timezone in ISO 8601 format."""
