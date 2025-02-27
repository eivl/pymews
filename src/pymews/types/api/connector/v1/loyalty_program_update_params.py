# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = [
    "LoyaltyProgramUpdateParams",
    "LoyaltyProgramUpdate",
    "LoyaltyProgramUpdateName",
    "LoyaltyProgramUpdateSubscription",
    "LoyaltyProgramUpdateType",
]


class LoyaltyProgramUpdateParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    loyalty_program_updates: Required[
        Annotated[Iterable[LoyaltyProgramUpdate], PropertyInfo(alias="LoyaltyProgramUpdates")]
    ]
    """Loyalty programs to be updated."""

    chain_id: Annotated[Optional[str], PropertyInfo(alias="ChainId")]
    """Unique identifier of the chain.

    Required when using
    [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
    ignored otherwise.
    """


class LoyaltyProgramUpdateName(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class LoyaltyProgramUpdateSubscription(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class LoyaltyProgramUpdateType(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class LoyaltyProgramUpdate(TypedDict, total=False):
    loyalty_program_id: Required[Annotated[str, PropertyInfo(alias="LoyaltyProgramId")]]

    name: Annotated[Optional[LoyaltyProgramUpdateName], PropertyInfo(alias="Name")]

    subscription: Annotated[Optional[LoyaltyProgramUpdateSubscription], PropertyInfo(alias="Subscription")]

    type: Annotated[Optional[LoyaltyProgramUpdateType], PropertyInfo(alias="Type")]
