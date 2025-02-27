# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["ResourceAccessTokenDeleteParams"]


class ResourceAccessTokenDeleteParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    ids: Annotated[Optional[List[str]], PropertyInfo(alias="Ids")]
    """
    Unique identifiers of
    [Resource access token](https://mews-systems.gitbook.io/connector-api/operations/#resource-access-token).
    """
