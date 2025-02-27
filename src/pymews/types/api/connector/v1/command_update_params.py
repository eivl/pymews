# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["CommandUpdateParams", "ExternalRequestIdentifier"]


class CommandUpdateParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    command_id: Required[Annotated[str, PropertyInfo(alias="CommandId")]]
    """
    Identifier of the
    [Command](https://mews-systems.gitbook.io/connector-api/operations/#command) to
    be updated.
    """

    state: Required[
        Annotated[
            Literal["Pending", "Received", "Processing", "Processed", "Cancelled", "Error"], PropertyInfo(alias="State")
        ]
    ]

    external_request_identifier: Annotated[
        Optional[ExternalRequestIdentifier], PropertyInfo(alias="ExternalRequestIdentifier")
    ]

    notes: Annotated[Optional[str], PropertyInfo(alias="Notes")]
    """Notes about command execution.

    Only used if the State is Processed, Cancelled or Error, otherwise ignored.
    """

    progress: Annotated[Optional[float], PropertyInfo(alias="Progress")]
    """Progress of the command processing.

    Only used if the State is Processing, otherwise ignored.
    """


class ExternalRequestIdentifier(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]
