# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["ReservationCancelParams"]


class ReservationCancelParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    reservation_ids: Required[Annotated[List[str], PropertyInfo(alias="ReservationIds")]]
    """Unique identifiers of the reservation to cancel."""

    enterprise_id: Annotated[Optional[str], PropertyInfo(alias="EnterpriseId")]
    """Unique identifier of the enterprise.

    Required when using
    [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
    ignored otherwise.
    """

    notes: Annotated[str, PropertyInfo(alias="Notes")]
    """Additional notes describing the reason for the cancellation."""

    post_cancellation_fee: Annotated[Optional[bool], PropertyInfo(alias="PostCancellationFee")]
    """Whether the cancellation fees should be charged according to rate conditions.

    The default is `false`.
    """

    reservation_id: Annotated[str, PropertyInfo(alias="ReservationId")]

    send_email: Annotated[Optional[bool], PropertyInfo(alias="SendEmail")]
    """Whether the cancellation email should be sent. The default is `true`."""
