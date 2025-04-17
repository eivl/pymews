# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["CreditCardChargeParams", "Amount"]


class CreditCardChargeParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    amount: Required[Annotated[Amount, PropertyInfo(alias="Amount")]]

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    accounting_category_id: Annotated[Optional[str], PropertyInfo(alias="AccountingCategoryId")]
    """
    Unique identifier of the
    [Accounting category](https://mews-systems.gitbook.io/connector-api/operations/accountingcategories/#accounting-category).
    """

    bill_id: Annotated[Optional[str], PropertyInfo(alias="BillId")]

    credit_card_id: Annotated[str, PropertyInfo(alias="CreditCardId")]
    """
    Unique identifier of the
    [Credit card](https://mews-systems.gitbook.io/connector-api/operations/#credit-card).
    """

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
