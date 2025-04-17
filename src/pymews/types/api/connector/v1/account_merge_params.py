# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["AccountMergeParams", "AccountMergeParameter"]


class AccountMergeParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    account_merge_parameters: Required[
        Annotated[Iterable[AccountMergeParameter], PropertyInfo(alias="AccountMergeParameters")]
    ]
    """Accounts to be merged."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""


class AccountMergeParameter(TypedDict, total=False):
    account_type: Required[Annotated[Literal["Customer", "Company"], PropertyInfo(alias="AccountType")]]
    """Customer

    Company
    """

    source_account_ids: Required[Annotated[List[str], PropertyInfo(alias="SourceAccountIds")]]
    """Unique identifiers of the source accounts (`Customer` or `Company`)."""

    target_account_id: Required[Annotated[str, PropertyInfo(alias="TargetAccountId")]]
    """Unique identifier of the target account (`Customer` or `Company`)."""
