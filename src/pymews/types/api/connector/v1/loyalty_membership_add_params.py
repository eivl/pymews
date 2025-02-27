# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["LoyaltyMembershipAddParams", "LoyaltyMembership"]


class LoyaltyMembershipAddParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    loyalty_memberships: Required[Annotated[Iterable[LoyaltyMembership], PropertyInfo(alias="LoyaltyMemberships")]]
    """Loyalty memberships to be added."""

    chain_id: Annotated[Optional[str], PropertyInfo(alias="ChainId")]
    """Unique identifier of the chain.

    Required when using
    [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
    ignored otherwise.
    """


class LoyaltyMembership(TypedDict, total=False):
    account_id: Required[Annotated[str, PropertyInfo(alias="AccountId")]]

    is_primary: Required[Annotated[bool, PropertyInfo(alias="IsPrimary")]]

    loyalty_program_id: Required[Annotated[str, PropertyInfo(alias="LoyaltyProgramId")]]

    code: Annotated[Optional[str], PropertyInfo(alias="Code")]

    expiration_date: Annotated[Union[str, date, None], PropertyInfo(alias="ExpirationDate", format="iso8601")]

    loyalty_tier_id: Annotated[Optional[str], PropertyInfo(alias="LoyaltyTierId")]

    points: Annotated[Optional[int], PropertyInfo(alias="Points")]

    state: Annotated[
        Optional[Literal["New", "Pending", "Enrolled", "Canceled", "Declined"]], PropertyInfo(alias="State")
    ]

    url: Annotated[Optional[str], PropertyInfo(alias="Url")]
