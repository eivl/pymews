# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["PaymentAddCreditCardParams", "Amount", "CreditCard"]


class PaymentAddCreditCardParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    amount: Required[Annotated[Amount, PropertyInfo(alias="Amount")]]

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    credit_card: Required[Annotated[CreditCard, PropertyInfo(alias="CreditCard")]]

    customer_id: Required[Annotated[str, PropertyInfo(alias="CustomerId")]]
    """
    Unique identifier of the
    [Customer](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer).
    """

    accounting_category_id: Annotated[Optional[str], PropertyInfo(alias="AccountingCategoryId")]
    """
    Unique identifier of an
    [Accounting category](https://mews-systems.gitbook.io/connector-api/operations/accountingcategories/#accounting-category)
    to be assigned to the credit card payment.
    """

    bill_id: Annotated[Optional[str], PropertyInfo(alias="BillId")]
    """Unique identifier of an open bill of the customer where to assign the payment."""

    notes: Annotated[Optional[str], PropertyInfo(alias="Notes")]
    """Additional payment notes."""

    receipt_identifier: Annotated[Optional[str], PropertyInfo(alias="ReceiptIdentifier")]
    """Identifier of the payment receipt."""

    reservation_id: Annotated[Optional[str], PropertyInfo(alias="ReservationId")]
    """Unique identifier of the reservation the payment belongs to."""


class Amount(TypedDict, total=False):
    currency: Required[Annotated[str, PropertyInfo(alias="Currency")]]
    """ISO-4217 code of the `Currency`."""

    gross_value: Annotated[Optional[float], PropertyInfo(alias="GrossValue")]
    """Gross value including all taxes."""

    net_value: Annotated[Optional[float], PropertyInfo(alias="NetValue")]
    """Net value in case the item is taxed."""

    tax_codes: Annotated[Optional[List[str]], PropertyInfo(alias="TaxCodes")]
    """The tax values applied."""


class CreditCard(TypedDict, total=False):
    name: Required[Annotated[str, PropertyInfo(alias="Name")]]
    """Name of the card holder."""

    number: Required[Annotated[str, PropertyInfo(alias="Number")]]
    """Obfuscated credit card number.

    At most first six digits and last four digits can be specified, the digits in
    between should be replaced with `*`. It is possible to provide even more
    obfuscated number or just last four digits. **Never provide full credit card
    number**. For example `411111******1111`.
    """

    type: Required[Annotated[str, PropertyInfo(alias="Type")]]
    """
    Type of the credit card, one of: `Visa`, `MasterCard`, `Amex`, `Discover`,
    `DinersClub`, `Jcb`, `EnRoute`, `Maestro`, `UnionPay`.
    """

    expiration: Annotated[Optional[str], PropertyInfo(alias="Expiration")]
    """Expiration of the credit card in format `MM/YYYY`, e.g. `12/2016` or `04/2017`."""
