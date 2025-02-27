# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["ReservationProcessParams"]


class ReservationProcessParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    reservation_id: Required[Annotated[str, PropertyInfo(alias="ReservationId")]]
    """Unique identifier of the reservation to process."""

    allow_open_balance: Annotated[Optional[bool], PropertyInfo(alias="AllowOpenBalance")]
    """Whether non-zero consumed balance of all reservation members is allowed."""

    close_bills: Annotated[Optional[bool], PropertyInfo(alias="CloseBills")]
    """
    Whether closable bills of the reservation members should be automatically
    closed.
    """

    enterprise_id: Annotated[Optional[str], PropertyInfo(alias="EnterpriseId")]
    """Unique identifier of the enterprise.

    Required when using
    [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
    ignored otherwise.
    """

    notes: Annotated[Optional[str], PropertyInfo(alias="Notes")]
    """Required if AllowOpenBalance set to true.

    Used to provide reason for closing with unbalanced bill.
    """
