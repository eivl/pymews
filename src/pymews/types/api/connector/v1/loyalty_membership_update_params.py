# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = [
    "LoyaltyMembershipUpdateParams",
    "LoyaltyMembershipUpdate",
    "LoyaltyMembershipUpdateCode",
    "LoyaltyMembershipUpdateExpirationDate",
    "LoyaltyMembershipUpdateIsPrimary",
    "LoyaltyMembershipUpdateLoyaltyProgramID",
    "LoyaltyMembershipUpdateLoyaltyTierID",
    "LoyaltyMembershipUpdatePoints",
    "LoyaltyMembershipUpdateState",
    "LoyaltyMembershipUpdateURL",
]


class LoyaltyMembershipUpdateParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    loyalty_membership_updates: Required[
        Annotated[Iterable[LoyaltyMembershipUpdate], PropertyInfo(alias="LoyaltyMembershipUpdates")]
    ]
    """Loyalty memberships to be updated."""

    chain_id: Annotated[Optional[str], PropertyInfo(alias="ChainId")]
    """Unique identifier of the chain.

    Required when using
    [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
    ignored otherwise.
    """


class LoyaltyMembershipUpdateCode(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class LoyaltyMembershipUpdateExpirationDate(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class LoyaltyMembershipUpdateIsPrimary(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class LoyaltyMembershipUpdateLoyaltyProgramID(TypedDict, total=False):
    value: Annotated[str, PropertyInfo(alias="Value")]


class LoyaltyMembershipUpdateLoyaltyTierID(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class LoyaltyMembershipUpdatePoints(TypedDict, total=False):
    value: Annotated[Optional[int], PropertyInfo(alias="Value")]


class LoyaltyMembershipUpdateState(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class LoyaltyMembershipUpdateURL(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class LoyaltyMembershipUpdate(TypedDict, total=False):
    loyalty_membership_id: Required[Annotated[str, PropertyInfo(alias="LoyaltyMembershipId")]]

    code: Annotated[Optional[LoyaltyMembershipUpdateCode], PropertyInfo(alias="Code")]

    expiration_date: Annotated[Optional[LoyaltyMembershipUpdateExpirationDate], PropertyInfo(alias="ExpirationDate")]

    is_primary: Annotated[Optional[LoyaltyMembershipUpdateIsPrimary], PropertyInfo(alias="IsPrimary")]

    loyalty_program_id: Annotated[
        Optional[LoyaltyMembershipUpdateLoyaltyProgramID], PropertyInfo(alias="LoyaltyProgramId")
    ]

    loyalty_tier_id: Annotated[Optional[LoyaltyMembershipUpdateLoyaltyTierID], PropertyInfo(alias="LoyaltyTierId")]

    points: Annotated[Optional[LoyaltyMembershipUpdatePoints], PropertyInfo(alias="Points")]

    state: Annotated[Optional[LoyaltyMembershipUpdateState], PropertyInfo(alias="State")]

    url: Annotated[Optional[LoyaltyMembershipUpdateURL], PropertyInfo(alias="Url")]
