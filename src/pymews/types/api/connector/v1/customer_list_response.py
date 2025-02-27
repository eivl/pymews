# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .customer import Customer
from ....._models import BaseModel

__all__ = ["CustomerListResponse", "Document"]


class Document(BaseModel):
    customer_id: Optional[str] = FieldInfo(alias="CustomerId", default=None)
    """Identifier of the `Customer`."""

    expiration: Optional[date] = FieldInfo(alias="Expiration", default=None)
    """Expiration date in ISO 8601 format."""

    id: Optional[str] = FieldInfo(alias="Id", default=None)
    """Unique identifier of the document."""

    identity_document_support_number: Optional[str] = FieldInfo(alias="IdentityDocumentSupportNumber", default=None)
    """Identity document support number.

    Only required for Spanish identity cards in Spanish hotels.
    """

    issuance: Optional[date] = FieldInfo(alias="Issuance", default=None)
    """Date of issuance in ISO 8601 format."""

    issuing_city: Optional[str] = FieldInfo(alias="IssuingCity", default=None)
    """City where the document was issued."""

    issuing_country_code: Optional[str] = FieldInfo(alias="IssuingCountryCode", default=None)
    """ISO 3166-1 code of the `Country`."""

    number: Optional[str] = FieldInfo(alias="Number", default=None)
    """Number of the document (e.g. passport number)."""

    type: Optional[Literal["IdentityCard", "Passport", "Visa", "DriversLicense"]] = FieldInfo(
        alias="Type", default=None
    )
    """IdentityCard

    Passport

    Visa

    DriversLicense
    """


class CustomerListResponse(BaseModel):
    customers: List[Customer] = FieldInfo(alias="Customers")
    """The customers."""

    cursor: Optional[str] = FieldInfo(alias="Cursor", default=None)
    """Unique identifier of the last and hence oldest customer item returned.

    This can be used in
    [Limitation](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/#limitation)
    in a subsequent request to fetch the next batch of older customers. If
    [Limitation](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/#limitation)
    is specified in the request message, then Cursor will always be included in the
    response message; this is true even when using Extents set to false so that no
    actual data is returned.
    """

    documents: Optional[List[Document]] = FieldInfo(alias="Documents", default=None)
    """The identity documents of customers."""
