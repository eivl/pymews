# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["AccountNoteAddParams", "AccountNote"]


class AccountNoteAddParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    account_notes: Required[Annotated[Iterable[AccountNote], PropertyInfo(alias="AccountNotes")]]
    """Account notes to be added."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    chain_id: Annotated[Optional[str], PropertyInfo(alias="ChainId")]
    """Unique identifier of the chain.

    Required when using
    [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
    ignored otherwise.
    """


class AccountNote(TypedDict, total=False):
    account_id: Required[Annotated[str, PropertyInfo(alias="AccountId")]]

    classifications: Required[
        Annotated[
            List[
                Literal[
                    "General",
                    "FoodAndBeverage",
                    "FrontOffice",
                    "Reservations",
                    "Housekeeping",
                    "Maintenance",
                    "PreviousStay",
                    "FamilyRelations",
                    "Gifts",
                    "Accounting",
                    "Complaints",
                    "Other",
                ]
            ],
            PropertyInfo(alias="Classifications"),
        ]
    ]
    """Specifying the classifications of the note based on account type."""

    content: Required[Annotated[str, PropertyInfo(alias="Content")]]
    """The content of the account note."""
