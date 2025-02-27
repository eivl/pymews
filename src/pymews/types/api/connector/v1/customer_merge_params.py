# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["CustomerMergeParams"]


class CustomerMergeParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    source_customer_id: Required[Annotated[str, PropertyInfo(alias="SourceCustomerId")]]
    """
    Unique identifier of the source
    [Customer](https://mews-systems.gitbook.io/connector-api/operations/#customer).
    """

    target_customer_id: Required[Annotated[str, PropertyInfo(alias="TargetCustomerId")]]
    """
    Unique identifier of the target
    [Customer](https://mews-systems.gitbook.io/connector-api/operations/#customer).
    """
