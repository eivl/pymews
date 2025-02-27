# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["ReservationGetAllItemsParams"]


class ReservationGetAllItemsParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    reservation_ids: Required[Annotated[List[str], PropertyInfo(alias="ReservationIds")]]
    """Unique identifiers of the reservation."""

    accounting_states: Annotated[Optional[List[str]], PropertyInfo(alias="AccountingStates")]
    """States the items should be in.

    If not specified, items in Open or Closed states are returned.
    """

    currency: Annotated[Optional[str], PropertyInfo(alias="Currency")]
    """
    ISO-4217 code of the
    [Currency](https://mews-systems.gitbook.io/connector-api/operations/currencies/#currency)
    the item costs should be converted to.
    """
