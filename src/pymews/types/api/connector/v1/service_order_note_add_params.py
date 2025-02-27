# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["ServiceOrderNoteAddParams", "ServiceOrderNote"]


class ServiceOrderNoteAddParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    service_order_notes: Required[Annotated[Iterable[ServiceOrderNote], PropertyInfo(alias="ServiceOrderNotes")]]
    """Notes to be added."""


class ServiceOrderNote(TypedDict, total=False):
    service_order_id: Required[Annotated[str, PropertyInfo(alias="ServiceOrderId")]]
    """Unique identifier of the `Service order` to which note will be added."""

    text: Required[Annotated[str, PropertyInfo(alias="Text")]]
    """Content of the service order note."""
