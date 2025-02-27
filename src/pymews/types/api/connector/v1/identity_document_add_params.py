# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["IdentityDocumentAddParams", "IdentityDocument"]


class IdentityDocumentAddParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    identity_documents: Required[Annotated[Iterable[IdentityDocument], PropertyInfo(alias="IdentityDocuments")]]
    """Identity documents to be added."""

    chain_id: Annotated[Optional[str], PropertyInfo(alias="ChainId")]
    """Unique identifier of the chain.

    Required when using
    [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
    ignored otherwise.
    """


class IdentityDocument(TypedDict, total=False):
    customer_id: Required[Annotated[str, PropertyInfo(alias="CustomerId")]]
    """Identifier of the `Customer`."""

    number: Required[Annotated[str, PropertyInfo(alias="Number")]]
    """Number of the document (e.g. passport number)."""

    type: Required[Annotated[Literal["IdentityCard", "Passport", "Visa", "DriversLicense"], PropertyInfo(alias="Type")]]
    """IdentityCard

    Passport

    Visa

    DriversLicense
    """

    expiration_date: Annotated[Union[str, date, None], PropertyInfo(alias="ExpirationDate", format="iso8601")]
    """Expiration date in ISO 8601 format."""

    identity_document_support_number: Annotated[Optional[str], PropertyInfo(alias="IdentityDocumentSupportNumber")]
    """Identity document support number.

    Only required for Spanish identity cards in Spanish hotels.
    """

    issuance_date: Annotated[Union[str, date, None], PropertyInfo(alias="IssuanceDate", format="iso8601")]
    """Date of issuance in ISO 8601 format."""

    issuing_city: Annotated[Optional[str], PropertyInfo(alias="IssuingCity")]
    """City where the document was issued."""

    issuing_country_code: Annotated[Optional[str], PropertyInfo(alias="IssuingCountryCode")]
    """ISO 3166-1 code of the `Country`)."""
