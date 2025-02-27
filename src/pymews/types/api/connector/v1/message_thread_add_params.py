# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["MessageThreadAddParams"]


class MessageThreadAddParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    original_sender: Required[Annotated[str, PropertyInfo(alias="OriginalSender")]]
    """The sender of the original message in the thread."""

    subject: Required[Annotated[str, PropertyInfo(alias="Subject")]]
    """Subject of the message thread."""
