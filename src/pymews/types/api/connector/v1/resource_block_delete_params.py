# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["ResourceBlockDeleteParams"]


class ResourceBlockDeleteParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    resource_block_ids: Required[Annotated[List[str], PropertyInfo(alias="ResourceBlockIds")]]
    """
    Unique identifier of
    [Resource blocks](https://mews-systems.gitbook.io/connector-api/operations/#resource-block)
    to be removed.
    """
