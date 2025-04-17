# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["CreditCardResult", "CreditCard"]


class CreditCard(BaseModel):
    created_utc: datetime = FieldInfo(alias="CreatedUtc")
    """Creation date and time of the credit card in UTC timezone in ISO 8601 format."""

    customer_id: str = FieldInfo(alias="CustomerId")
    """
    Unique identifier of the credit card
    [owner](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer).
    """

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the credit card."""

    is_active: bool = FieldInfo(alias="IsActive")
    """Whether the credit card is still active."""

    updated_utc: datetime = FieldInfo(alias="UpdatedUtc")
    """
    Last update date and time of the credit card in UTC timezone in ISO 8601 format.
    """

    enterprise_id: Optional[str] = FieldInfo(alias="EnterpriseId", default=None)
    """
    Unique identifier of the
    [Enterprise](https://mews-systems.gitbook.io/connector-api/operations/enterprises/#enterprise).
    """

    expiration: Optional[str] = FieldInfo(alias="Expiration", default=None)
    """Expiration of the credit card in format MM/YYYY."""

    format: Optional[str] = FieldInfo(alias="Format", default=None)
    """Format of the credit card."""

    kind: Optional[str] = FieldInfo(alias="Kind", default=None)
    """Kind of the credit card."""

    obfuscated_number: Optional[str] = FieldInfo(alias="ObfuscatedNumber", default=None)
    """Obfuscated credit card number.

    At most first six digits and last four digits can be specified, otherwise the
    digits are replaced with \\**.
    """

    state: Optional[str] = FieldInfo(alias="State", default=None)
    """State of the credit card."""

    type: Optional[str] = FieldInfo(alias="Type", default=None)
    """Type of the credit card."""


class CreditCardResult(BaseModel):
    credit_cards: Optional[List[CreditCard]] = FieldInfo(alias="CreditCards", default=None)
    """The credit cards."""

    cursor: Optional[str] = FieldInfo(alias="Cursor", default=None)
    """
    Unique identifier of the item one newer in time order than the items to be
    returned. If Cursor is not specified, i.e. null, then the latest or most recent
    items will be returned.
    """
