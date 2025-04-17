# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = [
    "IdentityDocumentUpdateParams",
    "IdentityDocument",
    "IdentityDocumentExpirationDate",
    "IdentityDocumentIdentityDocumentSupportNumber",
    "IdentityDocumentIssuanceDate",
    "IdentityDocumentIssuingCity",
    "IdentityDocumentIssuingCountryCode",
    "IdentityDocumentNumber",
    "IdentityDocumentType",
]


class IdentityDocumentUpdateParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    identity_documents: Required[Annotated[Iterable[IdentityDocument], PropertyInfo(alias="IdentityDocuments")]]
    """Identity documents to be updated."""

    chain_id: Annotated[Optional[str], PropertyInfo(alias="ChainId")]
    """Unique identifier of the chain.

    Required when using
    [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
    ignored otherwise.
    """


class IdentityDocumentExpirationDate(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class IdentityDocumentIdentityDocumentSupportNumber(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class IdentityDocumentIssuanceDate(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class IdentityDocumentIssuingCity(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class IdentityDocumentIssuingCountryCode(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class IdentityDocumentNumber(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class IdentityDocumentType(TypedDict, total=False):
    value: Annotated[Literal["IdentityCard", "Passport", "Visa", "DriversLicense"], PropertyInfo(alias="Value")]
    """IdentityCard

    Passport

    Visa

    DriversLicense
    """


class IdentityDocument(TypedDict, total=False):
    id: Required[Annotated[str, PropertyInfo(alias="Id")]]
    """Unique identifier of the document."""

    expiration_date: Annotated[Optional[IdentityDocumentExpirationDate], PropertyInfo(alias="ExpirationDate")]
    """
    Expiration date in ISO 8601 format (or `null` if the expiration date should not
    be updated).
    """

    identity_document_support_number: Annotated[
        Optional[IdentityDocumentIdentityDocumentSupportNumber], PropertyInfo(alias="IdentityDocumentSupportNumber")
    ]
    """Identity document support number.

    Only required for Spanish identity cards in Spanish hotels.
    """

    issuance_date: Annotated[Optional[IdentityDocumentIssuanceDate], PropertyInfo(alias="IssuanceDate")]
    """
    Date of issuance in ISO 8601 format (or `null` if the issuance date should not
    be updated).
    """

    issuing_city: Annotated[Optional[IdentityDocumentIssuingCity], PropertyInfo(alias="IssuingCity")]
    """
    City where the document was issued (or `null` if the issuing city should not be
    updated).
    """

    issuing_country_code: Annotated[
        Optional[IdentityDocumentIssuingCountryCode], PropertyInfo(alias="IssuingCountryCode")
    ]
    """
    ISO 3166-1 code of the `Country` (or `null` if the issuing country code should
    not be updated).
    """

    number: Annotated[Optional[IdentityDocumentNumber], PropertyInfo(alias="Number")]
    """Number of the document (e.g.

    passport number or `null` if the number should not be updated).
    """

    type: Annotated[Optional[IdentityDocumentType], PropertyInfo(alias="Type")]
    """
    Has same structure as
    [String update value](https://mews-systems.gitbook.io/connector-api/operations/_objects#string-update-value).
    """
