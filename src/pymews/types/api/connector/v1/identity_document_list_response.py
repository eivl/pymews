# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["IdentityDocumentListResponse", "IdentityDocument"]


class IdentityDocument(BaseModel):
    customer_id: str = FieldInfo(alias="CustomerId")
    """Identifier of the `Customer`."""

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the document."""

    number: str = FieldInfo(alias="Number")
    """Number of the document (e.g. passport number)."""

    type: Literal["IdentityCard", "Passport", "Visa", "DriversLicense"] = FieldInfo(alias="Type")
    """IdentityCard

    Passport

    Visa

    DriversLicense
    """

    expiration_date: Optional[date] = FieldInfo(alias="ExpirationDate", default=None)
    """Expiration date in ISO 8601 format."""

    identity_document_support_number: Optional[str] = FieldInfo(alias="IdentityDocumentSupportNumber", default=None)
    """Identity document support number.

    Only required for Spanish identity cards in Spanish hotels.
    """

    issuance_date: Optional[date] = FieldInfo(alias="IssuanceDate", default=None)
    """Date of issuance in ISO 8601 format."""

    issuing_city: Optional[str] = FieldInfo(alias="IssuingCity", default=None)
    """City where the document was issued."""

    issuing_country_code: Optional[str] = FieldInfo(alias="IssuingCountryCode", default=None)
    """ISO 3166-1 code of the `Country`."""


class IdentityDocumentListResponse(BaseModel):
    identity_documents: List[IdentityDocument] = FieldInfo(alias="IdentityDocuments")
    """The identity documents of customers."""

    cursor: Optional[str] = FieldInfo(alias="Cursor", default=None)
    """
    Unique identifier of the item one newer in time order than the items to be
    returned. If Cursor is not specified, i.e. null, then the latest or most recent
    items will be returned.
    """
