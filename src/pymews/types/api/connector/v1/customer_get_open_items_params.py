# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["CustomerGetOpenItemsParams"]


class CustomerGetOpenItemsParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    customer_ids: Required[Annotated[List[str], PropertyInfo(alias="CustomerIds")]]
    """
    Unique identifiers of the
    [Customers](https://mews-systems.gitbook.io/connector-api/operations/#customer).
    """

    currency: Annotated[Union[str, datetime, None], PropertyInfo(alias="Currency", format="iso8601")]
    """
    ISO-4217 code of the
    [Currency](https://mews-systems.gitbook.io/connector-api/operations/currencies/#currency)
    the item costs should be converted to.
    """
