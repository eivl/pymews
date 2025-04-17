# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = [
    "BillCloseParams",
    "AccountAddress",
    "AccountTaxIdentifier",
    "Address",
    "AssociatedAccountData",
    "AssociatedAccountDataAddress",
    "AssociatedAccountDataTaxIdentifier",
    "CompanyTaxIdentifier",
    "DueDate",
    "Notes",
    "Options",
    "OptionsDisplayCustomer",
    "OptionsDisplayTaxation",
    "PurchaseOrderNumber",
    "TaxedDate",
    "TaxIdentifier",
    "VariableSymbol",
]


class BillCloseParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    bill_id: Required[Annotated[str, PropertyInfo(alias="BillId")]]
    """
    Unique identifier of the
    [Bill](https://mews-systems.gitbook.io/connector-api/operations/#bill) to be
    closed.
    """

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    type: Required[Annotated[Literal["Receipt", "Invoice"], PropertyInfo(alias="Type")]]
    """After a bill is closed, the Bill Type is set to `Receipt` or `Invoice`.

    `Receipt` indicates that the bill has been fully paid and the balance is zero.
    `Invoice` indicates that the bill has not yet been fully paid but an invoice has
    been issued. Prior to closing, Bill Type should not be used.

    - `Receipt` - Default; the bill has been paid in full; only applicable after the
      bill is closed.
    - `Invoice` - Bill has not been paid in full but an invoice has been issued to
      request payment.
    """

    account_address: Annotated[Optional[AccountAddress], PropertyInfo(alias="AccountAddress")]
    """New address details."""

    account_tax_identifier: Annotated[Optional[AccountTaxIdentifier], PropertyInfo(alias="AccountTaxIdentifier")]
    """Tax identifier of account to be put on a bill."""

    address: Annotated[Optional[Address], PropertyInfo(alias="Address")]
    """New address details."""

    associated_account_data: Annotated[
        Optional[Iterable[AssociatedAccountData]], PropertyInfo(alias="AssociatedAccountData")
    ]
    """Account data of the associated account on a bill.

    Currently one object is supported and only populated when the bill is closed.
    """

    bill_counter_id: Annotated[Optional[str], PropertyInfo(alias="BillCounterId")]
    """
    Unique identifier of the
    [Counter](https://mews-systems.gitbook.io/connector-api/operations/counters/#counter)
    to be used for closing. Default one is used when no value is provided.
    """

    company_tax_identifier: Annotated[Optional[CompanyTaxIdentifier], PropertyInfo(alias="CompanyTaxIdentifier")]
    """Tax identifier of company to be put on a bill."""

    due_date: Annotated[Optional[DueDate], PropertyInfo(alias="DueDate")]
    """Deadline when bill is due to be paid.

    Can be used only with `Type` of `Invoice`.
    """

    enterprise_id: Annotated[Optional[str], PropertyInfo(alias="EnterpriseId")]
    """Unique identifier of the enterprise.

    Required when using
    [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
    ignored otherwise.
    """

    fiscal_machine_id: Annotated[Optional[str], PropertyInfo(alias="FiscalMachineId")]
    """
    Unique identifier of the
    [Fiscal Machine](https://mews-systems.gitbook.io/connector-api/operations/devices/#device)
    to be used for closing. Default one is used when no value is provided.
    """

    notes: Annotated[Optional[Notes], PropertyInfo(alias="Notes")]
    """Notes to be attached to bill."""

    options: Annotated[Optional[Options], PropertyInfo(alias="Options")]

    purchase_order_number: Annotated[Optional[PurchaseOrderNumber], PropertyInfo(alias="PurchaseOrderNumber")]
    """Unique number of the purchase order from the buyer."""

    taxed_date: Annotated[Optional[TaxedDate], PropertyInfo(alias="TaxedDate")]
    """Date of consumption for tax purposes.

    Can be used only with `Type` of `Invoice`.
    """

    tax_identifier: Annotated[Optional[TaxIdentifier], PropertyInfo(alias="TaxIdentifier")]
    """Tax identifier of account to be put on a bill."""

    variable_symbol: Annotated[Optional[VariableSymbol], PropertyInfo(alias="VariableSymbol")]
    """Optional unique identifier of requested payment.

    Can be used only with `Type` of `Invoice`.
    """


class AccountAddress(TypedDict, total=False):
    city: Annotated[Optional[str], PropertyInfo(alias="City")]
    """The city."""

    country_code: Annotated[Optional[str], PropertyInfo(alias="CountryCode")]
    """ISO 3166-1 code of the Country."""

    country_subdivision_code: Annotated[Optional[str], PropertyInfo(alias="CountrySubdivisionCode")]
    """ISO 3166-2 code of the administrative division, e.g. DE-BW"""

    line1: Annotated[Optional[str], PropertyInfo(alias="Line1")]
    """First line of the address."""

    line2: Annotated[Optional[str], PropertyInfo(alias="Line2")]
    """Second line of the address."""

    postal_code: Annotated[Optional[str], PropertyInfo(alias="PostalCode")]
    """Postal code."""


class AccountTaxIdentifier(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class Address(TypedDict, total=False):
    city: Annotated[Optional[str], PropertyInfo(alias="City")]
    """The city."""

    country_code: Annotated[Optional[str], PropertyInfo(alias="CountryCode")]
    """ISO 3166-1 code of the Country."""

    country_subdivision_code: Annotated[Optional[str], PropertyInfo(alias="CountrySubdivisionCode")]
    """ISO 3166-2 code of the administrative division, e.g. DE-BW"""

    line1: Annotated[Optional[str], PropertyInfo(alias="Line1")]
    """First line of the address."""

    line2: Annotated[Optional[str], PropertyInfo(alias="Line2")]
    """Second line of the address."""

    postal_code: Annotated[Optional[str], PropertyInfo(alias="PostalCode")]
    """Postal code."""


class AssociatedAccountDataAddress(TypedDict, total=False):
    city: Annotated[Optional[str], PropertyInfo(alias="City")]
    """The city."""

    country_code: Annotated[Optional[str], PropertyInfo(alias="CountryCode")]
    """ISO 3166-1 code of the Country."""

    country_subdivision_code: Annotated[Optional[str], PropertyInfo(alias="CountrySubdivisionCode")]
    """ISO 3166-2 code of the administrative division, e.g. DE-BW"""

    line1: Annotated[Optional[str], PropertyInfo(alias="Line1")]
    """First line of the address."""

    line2: Annotated[Optional[str], PropertyInfo(alias="Line2")]
    """Second line of the address."""

    postal_code: Annotated[Optional[str], PropertyInfo(alias="PostalCode")]
    """Postal code."""


class AssociatedAccountDataTaxIdentifier(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AssociatedAccountData(TypedDict, total=False):
    id: Required[Annotated[str, PropertyInfo(alias="Id")]]
    """
    Unique identifier of the associated account (`Customer` or `Company`) the bill
    is associated to.
    """

    address: Annotated[Optional[AssociatedAccountDataAddress], PropertyInfo(alias="Address")]
    """New address details."""

    tax_identifier: Annotated[Optional[AssociatedAccountDataTaxIdentifier], PropertyInfo(alias="TaxIdentifier")]
    """Tax identifier of the associated account to be put on a bill."""


class CompanyTaxIdentifier(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class DueDate(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class Notes(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class OptionsDisplayCustomer(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class OptionsDisplayTaxation(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class Options(TypedDict, total=False):
    display_customer: Required[Annotated[OptionsDisplayCustomer, PropertyInfo(alias="DisplayCustomer")]]
    """Display customer information on a bill."""

    display_taxation: Required[Annotated[OptionsDisplayTaxation, PropertyInfo(alias="DisplayTaxation")]]
    """Display taxation detail on a bill."""


class PurchaseOrderNumber(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class TaxedDate(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class TaxIdentifier(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class VariableSymbol(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]
