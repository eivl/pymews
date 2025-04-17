# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["LoyaltyProgramAddParams", "LoyaltyProgram"]


class LoyaltyProgramAddParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    loyalty_programs: Required[Annotated[Iterable[LoyaltyProgram], PropertyInfo(alias="LoyaltyPrograms")]]
    """Loyalty programs to be added."""

    chain_id: Annotated[Optional[str], PropertyInfo(alias="ChainId")]
    """Unique identifier of the chain.

    Required when using
    [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
    ignored otherwise.
    """


class LoyaltyProgram(TypedDict, total=False):
    code: Required[Annotated[str, PropertyInfo(alias="Code")]]

    name: Required[Annotated[str, PropertyInfo(alias="Name")]]

    subscription: Annotated[Optional[Literal["Free", "Paid"]], PropertyInfo(alias="Subscription")]

    type: Annotated[Optional[Literal["Hotel", "ExternalPartner", "SoftBrand", "Unknown"]], PropertyInfo(alias="Type")]
