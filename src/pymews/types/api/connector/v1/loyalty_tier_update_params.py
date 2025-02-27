# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = [
    "LoyaltyTierUpdateParams",
    "LoyaltyTierUpdate",
    "LoyaltyTierUpdateCode",
    "LoyaltyTierUpdateName",
    "LoyaltyTierUpdateOrdering",
]


class LoyaltyTierUpdateParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    loyalty_tier_updates: Required[Annotated[Iterable[LoyaltyTierUpdate], PropertyInfo(alias="LoyaltyTierUpdates")]]
    """Loyalty tiers to be updated."""


class LoyaltyTierUpdateCode(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class LoyaltyTierUpdateName(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class LoyaltyTierUpdateOrdering(TypedDict, total=False):
    value: Annotated[int, PropertyInfo(alias="Value")]


class LoyaltyTierUpdate(TypedDict, total=False):
    loyalty_tier_id: Required[Annotated[str, PropertyInfo(alias="LoyaltyTierId")]]

    code: Annotated[Optional[LoyaltyTierUpdateCode], PropertyInfo(alias="Code")]

    name: Annotated[Optional[LoyaltyTierUpdateName], PropertyInfo(alias="Name")]

    ordering: Annotated[Optional[LoyaltyTierUpdateOrdering], PropertyInfo(alias="Ordering")]
