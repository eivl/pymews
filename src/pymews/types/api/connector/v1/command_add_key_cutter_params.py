# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["CommandAddKeyCutterParams"]


class CommandAddKeyCutterParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    key_count: Required[Annotated[int, PropertyInfo(alias="KeyCount")]]
    """Count of keys to encode."""

    key_cutter_id: Required[Annotated[str, PropertyInfo(alias="KeyCutterId")]]
    """
    Unique identifier of the KeyCutter
    [Device](https://mews-systems.gitbook.io/connector-api/operations/devices/#device)
    where to encode the key.
    """

    reservation_id: Required[Annotated[str, PropertyInfo(alias="ReservationId")]]
    """Unique identifier of the reservation to encode the key for."""

    enterprise_id: Annotated[Optional[str], PropertyInfo(alias="EnterpriseId")]
    """Unique identifier of the enterprise.

    Required when using
    [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
    ignored otherwise.
    """
