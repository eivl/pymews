# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "V1ListLedgerBalancesResponse",
    "LedgerBalance",
    "LedgerBalanceClosingBalance",
    "LedgerBalanceClosingBalanceBreakdown",
    "LedgerBalanceClosingBalanceBreakdownItem",
    "LedgerBalanceClosingBalanceTaxValue",
    "LedgerBalanceOpeningBalance",
    "LedgerBalanceOpeningBalanceBreakdown",
    "LedgerBalanceOpeningBalanceBreakdownItem",
    "LedgerBalanceOpeningBalanceTaxValue",
]


class LedgerBalanceClosingBalanceBreakdownItem(BaseModel):
    net_value: float = FieldInfo(alias="NetValue")
    """The net value that the tax is calculated from."""

    tax_value: float = FieldInfo(alias="TaxValue")
    """The value of the tax."""

    tax_rate_code: Optional[str] = FieldInfo(alias="TaxRateCode", default=None)
    """Tax rate code for the item. `null` for untaxed amounts."""


class LedgerBalanceClosingBalanceBreakdown(BaseModel):
    items: List[LedgerBalanceClosingBalanceBreakdownItem] = FieldInfo(alias="Items")
    """Tax breakdown items per each tax rate applied."""


class LedgerBalanceClosingBalanceTaxValue(BaseModel):
    value: float = FieldInfo(alias="Value")
    """Amount of tax applied."""

    code: Optional[str] = FieldInfo(alias="Code", default=None)
    """Code corresponding to tax type."""


class LedgerBalanceClosingBalance(BaseModel):
    breakdown: LedgerBalanceClosingBalanceBreakdown = FieldInfo(alias="Breakdown")
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

    tax_values: List[LedgerBalanceClosingBalanceTaxValue] = FieldInfo(alias="TaxValues")
    """The tax values applied."""


class LedgerBalanceOpeningBalanceBreakdownItem(BaseModel):
    net_value: float = FieldInfo(alias="NetValue")
    """The net value that the tax is calculated from."""

    tax_value: float = FieldInfo(alias="TaxValue")
    """The value of the tax."""

    tax_rate_code: Optional[str] = FieldInfo(alias="TaxRateCode", default=None)
    """Tax rate code for the item. `null` for untaxed amounts."""


class LedgerBalanceOpeningBalanceBreakdown(BaseModel):
    items: List[LedgerBalanceOpeningBalanceBreakdownItem] = FieldInfo(alias="Items")
    """Tax breakdown items per each tax rate applied."""


class LedgerBalanceOpeningBalanceTaxValue(BaseModel):
    value: float = FieldInfo(alias="Value")
    """Amount of tax applied."""

    code: Optional[str] = FieldInfo(alias="Code", default=None)
    """Code corresponding to tax type."""


class LedgerBalanceOpeningBalance(BaseModel):
    breakdown: LedgerBalanceOpeningBalanceBreakdown = FieldInfo(alias="Breakdown")
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

    tax_values: List[LedgerBalanceOpeningBalanceTaxValue] = FieldInfo(alias="TaxValues")
    """The tax values applied."""


class LedgerBalance(BaseModel):
    closing_balance: LedgerBalanceClosingBalance = FieldInfo(alias="ClosingBalance")

    date: datetime.date = FieldInfo(alias="Date")
    """Day for which ledger balance applies in ISO 8601 format."""

    enterprise_id: str = FieldInfo(alias="EnterpriseId")
    """Unique identifier of the Enterprise."""

    ledger_type: Literal["Revenue", "Tax", "Payment", "Deposit", "Guest", "City"] = FieldInfo(alias="LedgerType")
    """Revenue

    Tax

    Payment

    Deposit

    Guest

    City
    """

    opening_balance: LedgerBalanceOpeningBalance = FieldInfo(alias="OpeningBalance")


class V1ListLedgerBalancesResponse(BaseModel):
    ledger_balances: Optional[List[LedgerBalance]] = FieldInfo(alias="LedgerBalances", default=None)
    """The list of filtered ledger balances."""

    cursor: Optional[str] = FieldInfo(alias="Cursor", default=None)
    """Unique identifier of the last and hence oldest ledger balance returned.

    This can be used in Limitation in a subsequent request to fetch the next batch
    of ledger balances.
    """
