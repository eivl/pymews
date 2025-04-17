# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["LoyaltyTierAddParams", "LoyaltyTier"]


class LoyaltyTierAddParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    loyalty_tiers: Required[Annotated[Iterable[LoyaltyTier], PropertyInfo(alias="LoyaltyTiers")]]
    """Loyalty tiers to be added."""

    chain_id: Annotated[Optional[str], PropertyInfo(alias="ChainId")]
    """Unique identifier of the chain.

    Required when using
    [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
    ignored otherwise.
    """


class LoyaltyTier(TypedDict, total=False):
    code: Required[Annotated[str, PropertyInfo(alias="Code")]]

    loyalty_program_id: Required[Annotated[str, PropertyInfo(alias="LoyaltyProgramId")]]

    name: Required[Annotated[str, PropertyInfo(alias="Name")]]

    ordering: Required[Annotated[int, PropertyInfo(alias="Ordering")]]
