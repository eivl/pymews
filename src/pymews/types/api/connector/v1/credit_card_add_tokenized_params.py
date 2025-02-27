# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["CreditCardAddTokenizedParams", "CreditCardData"]


class CreditCardAddTokenizedParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    credit_card_data: Required[Annotated[CreditCardData, PropertyInfo(alias="CreditCardData")]]
    """Credit card details provided by PCI provider."""

    customer_id: Required[Annotated[str, PropertyInfo(alias="CustomerId")]]
    """
    Unique identifier of the
    [Customer](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer).
    """


class CreditCardData(TypedDict, total=False):
    expiration: Required[Annotated[str, PropertyInfo(alias="Expiration")]]

    storage_data: Required[Annotated[str, PropertyInfo(alias="StorageData")]]

    obfuscated_number: Annotated[Optional[str], PropertyInfo(alias="ObfuscatedNumber")]
