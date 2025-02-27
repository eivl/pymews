# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["V1ListPreauthorizationsByCustomersParams"]


class V1ListPreauthorizationsByCustomersParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    customer_ids: Required[Annotated[List[str], PropertyInfo(alias="CustomerIds")]]
    """
    Unique identifier of the
    [Customer](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer).
    """
