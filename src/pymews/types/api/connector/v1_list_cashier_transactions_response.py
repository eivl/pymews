# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["V1ListCashierTransactionsResponse", "CashierTransaction", "CashierTransactionAmount"]


class CashierTransactionAmount(BaseModel):
    currency: str = FieldInfo(alias="Currency")

    net: Optional[float] = FieldInfo(alias="Net", default=None)

    tax: Optional[float] = FieldInfo(alias="Tax", default=None)

    tax_rate: Optional[float] = FieldInfo(alias="TaxRate", default=None)

    value: Optional[float] = FieldInfo(alias="Value", default=None)


class CashierTransaction(BaseModel):
    amount: Optional[CashierTransactionAmount] = FieldInfo(alias="Amount", default=None)
    """Total price of the reservation."""

    cashier_id: Optional[str] = FieldInfo(alias="CashierId", default=None)
    """
    Unique identifier of the
    [Cashier](https://mews-systems.gitbook.io/connector-api/operations/cashiers/#cashier).
    """

    created_utc: Optional[str] = FieldInfo(alias="CreatedUtc", default=None)
    """Creation date and time of the transaction."""

    enterprise_id: Optional[str] = FieldInfo(alias="EnterpriseId", default=None)
    """
    Unique identifier of the
    [Enterprise](https://mews-systems.gitbook.io/connector-api/operations/enterprises/#enterprise).
    """

    id: Optional[str] = FieldInfo(alias="Id", default=None)
    """Unique identifier of the transaction."""

    notes: Optional[str] = FieldInfo(alias="Notes", default=None)
    """Additional notes of the transaction."""

    number: Optional[str] = FieldInfo(alias="Number", default=None)
    """Number of the transaction."""

    payment_id: Optional[str] = FieldInfo(alias="PaymentId", default=None)
    """
    Unique identifier of the corresponding payment
    [Payment item](https://mews-systems.gitbook.io/connector-api/operations/accountingitems/#payment-item).
    """


class V1ListCashierTransactionsResponse(BaseModel):
    cashier_transactions: Optional[List[CashierTransaction]] = FieldInfo(alias="CashierTransactions", default=None)
    """Cashier transactions created in the interval."""

    cursor: Optional[str] = FieldInfo(alias="Cursor", default=None)
    """
    Unique identifier of the item one newer in time order than the items to be
    returned. If Cursor is not specified, i.e. null, then the latest or most recent
    items will be returned.
    """
