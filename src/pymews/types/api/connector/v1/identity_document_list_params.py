# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["IdentityDocumentListParams", "Limitation"]


class IdentityDocumentListParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    customer_ids: Required[Annotated[List[str], PropertyInfo(alias="CustomerIds")]]
    """Unique identifiers of `Customer`."""

    limitation: Required[Annotated[Limitation, PropertyInfo(alias="Limitation")]]
    """Limitation on the quantity of data returned."""

    chain_ids: Annotated[Optional[List[str]], PropertyInfo(alias="ChainIds")]
    """Unique identifiers of `Chain`.

    If not specified, the operation returns data for all chains within scope of the
    Access Token.
    """

    identity_document_ids: Annotated[Optional[List[str]], PropertyInfo(alias="IdentityDocumentIds")]
    """Unique identifiers of `Identity document`."""

    types: Annotated[
        Optional[List[Literal["IdentityCard", "Passport", "Visa", "DriversLicense"]]], PropertyInfo(alias="Types")
    ]
    """Type of the identity document."""


class Limitation(TypedDict, total=False):
    count: Required[Annotated[int, PropertyInfo(alias="Count")]]

    cursor: Annotated[Optional[str], PropertyInfo(alias="Cursor")]
