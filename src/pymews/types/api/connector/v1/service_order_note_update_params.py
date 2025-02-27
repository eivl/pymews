# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["ServiceOrderNoteUpdateParams", "ServiceOrderNoteUpdate", "ServiceOrderNoteUpdateText"]


class ServiceOrderNoteUpdateParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    service_order_note_updates: Required[
        Annotated[Iterable[ServiceOrderNoteUpdate], PropertyInfo(alias="ServiceOrderNoteUpdates")]
    ]
    """Notes to be updated."""


class ServiceOrderNoteUpdateText(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class ServiceOrderNoteUpdate(TypedDict, total=False):
    service_order_note_id: Required[Annotated[str, PropertyInfo(alias="ServiceOrderNoteId")]]
    """Unique identifier of the `Service order note`."""

    text: Annotated[Optional[ServiceOrderNoteUpdateText], PropertyInfo(alias="Text")]
    """
    Content of the service order note (or `null` if the content should not be
    updated).
    """
