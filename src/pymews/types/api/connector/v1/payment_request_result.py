# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = [
    "PaymentRequestResult",
    "PaymentRequest",
    "PaymentRequestAmount",
    "PaymentRequestAmountBreakdown",
    "PaymentRequestAmountBreakdownItem",
    "PaymentRequestAmountTaxValue",
]


class PaymentRequestAmountBreakdownItem(BaseModel):
    net_value: float = FieldInfo(alias="NetValue")
    """The net value that the tax is calculated from."""

    tax_value: float = FieldInfo(alias="TaxValue")
    """The value of the tax."""

    tax_rate_code: Optional[str] = FieldInfo(alias="TaxRateCode", default=None)
    """Tax rate code for the item. `null` for untaxed amounts."""


class PaymentRequestAmountBreakdown(BaseModel):
    items: List[PaymentRequestAmountBreakdownItem] = FieldInfo(alias="Items")
    """Tax breakdown items per each tax rate applied."""


class PaymentRequestAmountTaxValue(BaseModel):
    value: float = FieldInfo(alias="Value")
    """Amount of tax applied."""

    code: Optional[str] = FieldInfo(alias="Code", default=None)
    """Code corresponding to tax type."""


class PaymentRequestAmount(BaseModel):
    breakdown: PaymentRequestAmountBreakdown = FieldInfo(alias="Breakdown")
    """Information about individual tax amounts."""

    currency: str = FieldInfo(alias="Currency")
    """
    ISO-4217 code of the
    [Currency](https://mews-systems.gitbook.io/connector-api/operations/currencies/#currency).
    """

    gross_value: float = FieldInfo(alias="GrossValue")
    """Gross value including all taxes."""

    net_value: float = FieldInfo(alias="NetValue")
    """Net value without taxes."""

    tax_values: List[PaymentRequestAmountTaxValue] = FieldInfo(alias="TaxValues")
    """The tax values applied."""


class PaymentRequest(BaseModel):
    account_id: str = FieldInfo(alias="AccountId")
    """
    Unique identifier of the
    [Customer](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer)
    to which the payment request was issued.
    """

    amount: PaymentRequestAmount = FieldInfo(alias="Amount")

    created_utc: datetime = FieldInfo(alias="CreatedUtc")
    """
    Creation date and time of the payment request in UTC timezone in ISO 8601
    format.
    """

    description: str = FieldInfo(alias="Description")
    """Description of the payment request."""

    enterprise_id: str = FieldInfo(alias="EnterpriseId")
    """
    Unique identifier of the
    [Enterprise](https://mews-systems.gitbook.io/connector-api/operations/enterprises/#enterprise).
    """

    expiration_utc: datetime = FieldInfo(alias="ExpirationUtc")
    """Date and time of the payment request's expiration in ISO 8601 format."""

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the payment request."""

    reason: Literal[
        "Other", "PaymentCardMissing", "PaymentCardDeclined", "Deposit", "Prepayment", "Fee", "RecurringPayment"
    ] = FieldInfo(alias="Reason")

    state: Literal["Pending", "Completed", "Canceled", "Expired"] = FieldInfo(alias="State")

    type: Literal["Payment", "Preauthorization"] = FieldInfo(alias="Type")

    updated_utc: datetime = FieldInfo(alias="UpdatedUtc")
    """
    Last update date and time of the payment request in UTC timezone in ISO 8601
    format.
    """

    customer_id: Optional[str] = FieldInfo(alias="CustomerId", default=None)

    notes: Optional[str] = FieldInfo(alias="Notes", default=None)
    """Payment request's notes."""

    reservation_group_id: Optional[str] = FieldInfo(alias="ReservationGroupId", default=None)
    """
    Unique identifier of the
    [Reservation group](https://mews-systems.gitbook.io/connector-api/operations/reservations#reservation-group).
    """

    reservation_id: Optional[str] = FieldInfo(alias="ReservationId", default=None)


class PaymentRequestResult(BaseModel):
    payment_requests: List[PaymentRequest] = FieldInfo(alias="PaymentRequests")
    """The filtered payment requests."""

    cursor: Optional[str] = FieldInfo(alias="Cursor", default=None)
    """Unique identifier of the last and hence oldest payment request returned.

    This can be used in
    [Limitation](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/#limitation)
    in a subsequent request to fetch the next batch of older payment requests.
    """
