# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = [
    "CompanyUpdateParams",
    "AccountingCode",
    "AdditionalTaxIdentifier",
    "BillingCode",
    "Contact",
    "ContactPerson",
    "CreditRating",
    "CreditRatingBasic",
    "Department",
    "DunsNumber",
    "ExternalIdentifier",
    "Iata",
    "Identifier",
    "InvoiceDueInterval",
    "InvoicingEmail",
    "MotherCompanyID",
    "Name",
    "Notes",
    "Options",
    "OptionsAddFeesToInvoices",
    "OptionsAddTaxDeductedPaymentToInvoices",
    "OptionsInvoiceable",
    "ReferenceIdentifier",
    "TaxIdentifier",
    "Telephone",
    "WebsiteURL",
]


class CompanyUpdateParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    company_id: Required[Annotated[str, PropertyInfo(alias="CompanyId")]]
    """
    Unique identifier of the
    [Company](https://mews-systems.gitbook.io/connector-api/operations/#company).
    """

    accounting_code: Annotated[Optional[AccountingCode], PropertyInfo(alias="AccountingCode")]
    """
    Accounting code of the company (or `null` if the accounting code should not be
    updated).
    """

    additional_tax_identifier: Annotated[
        Optional[AdditionalTaxIdentifier], PropertyInfo(alias="AdditionalTaxIdentifier")
    ]
    """
    Additional tax identifier of the company (or `null` if the additional tax
    identifier should not be updated).
    """

    billing_code: Annotated[Optional[BillingCode], PropertyInfo(alias="BillingCode")]
    """
    Billing code of the company (or `null` if the billing code should not be
    updated).
    """

    chain_id: Annotated[Optional[str], PropertyInfo(alias="ChainId")]
    """Unique identifier of the chain.

    Required when using
    [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
    ignored otherwise.
    """

    contact: Annotated[Optional[Contact], PropertyInfo(alias="Contact")]
    """
    Other contact details, such as telephone, email or similar (or `null` if the
    contact should not be updated).
    """

    contact_person: Annotated[Optional[ContactPerson], PropertyInfo(alias="ContactPerson")]
    """
    Contact person of the company (or `null` if the contact person should not be
    updated).
    """

    credit_rating: Annotated[Optional[CreditRating], PropertyInfo(alias="CreditRating")]
    """Credit rating to define creditworthiness of the company."""

    department: Annotated[Optional[Department], PropertyInfo(alias="Department")]
    """The internal segmentation of a company, e.g.

    sales department (or `null` if the department should not be updated).
    """

    duns_number: Annotated[Optional[DunsNumber], PropertyInfo(alias="DunsNumber")]
    """
    The Dun & Bradstreet unique 9-digit DUNS number (or `null` if the Duns number
    should not be updated).
    """

    external_identifier: Annotated[Optional[ExternalIdentifier], PropertyInfo(alias="ExternalIdentifier")]
    """
    Identifier of the company from external system (or `null` if the External
    Identifier should not be updated).
    """

    iata: Annotated[Optional[Iata], PropertyInfo(alias="Iata")]
    """Iata of the company (or `null` if the Iata should not be updated)."""

    identifier: Annotated[Optional[Identifier], PropertyInfo(alias="Identifier")]
    """Identifier of the company, e.g.

    legal identifier (or `null` if the identifier should not be updated).
    """

    invoice_due_interval: Annotated[Optional[InvoiceDueInterval], PropertyInfo(alias="InvoiceDueInterval")]
    """
    The maximum time, when the invoice has to be be paid in ISO 8601 duration format
    (or `null` if the interval should not be updated).
    """

    invoicing_email: Annotated[Optional[InvoicingEmail], PropertyInfo(alias="InvoicingEmail")]
    """
    Email for issuing invoices to the company (or `null` if the email for issuing
    invoices should not be updated).
    """

    mother_company_id: Annotated[Optional[MotherCompanyID], PropertyInfo(alias="MotherCompanyId")]
    """
    Unique identifier of the mother company (or `null` if the mother company should
    not be updated).
    """

    name: Annotated[Optional[Name], PropertyInfo(alias="Name")]
    """Name of the company (or `null` if the name should not be updated)."""

    notes: Annotated[Optional[Notes], PropertyInfo(alias="Notes")]
    """Notes of the company (or `null` if the notes should not be updated)."""

    options: Annotated[Optional[Options], PropertyInfo(alias="Options")]
    """Options of the company."""

    reference_identifier: Annotated[Optional[ReferenceIdentifier], PropertyInfo(alias="ReferenceIdentifier")]
    """
    External system identifier - custom identifier used by an external system such
    as an external database (or `null` if the identifier should not be updated).
    """

    tax_identifier: Annotated[Optional[TaxIdentifier], PropertyInfo(alias="TaxIdentifier")]
    """
    Tax identification number of the company (or `null` if the tax identifier should
    not be updated).
    """

    telephone: Annotated[Optional[Telephone], PropertyInfo(alias="Telephone")]
    """
    Contact telephone number (or `null` if the telephone number should not be
    updated).
    """

    website_url: Annotated[Optional[WebsiteURL], PropertyInfo(alias="WebsiteUrl")]
    """
    The website url of the company (or `null` if the website url should not be
    updated).
    """


class AccountingCode(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AdditionalTaxIdentifier(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class BillingCode(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class Contact(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class ContactPerson(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class CreditRatingBasic(TypedDict, total=False):
    value: Annotated[
        Literal["CreditOk", "PaymentRequiredUpfront", "LocalDecisionRequired"], PropertyInfo(alias="Value")
    ]
    """CreditOk (Company can book services.)

    PaymentRequiredUpfront (Company must pay upfront.)

    LocalDecisionRequired (Requires local approval.)

    - `CreditOk` - Company can book services.
    - `PaymentRequiredUpfront` - Company must pay upfront.
    - `LocalDecisionRequired` - Requires local approval.
    """


class CreditRating(TypedDict, total=False):
    basic: Annotated[Optional[CreditRatingBasic], PropertyInfo(alias="Basic")]
    """
    Credit status of a company (or `null` if the credit status should not be
    updated).
    """


class Department(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class DunsNumber(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class ExternalIdentifier(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class Iata(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class Identifier(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class InvoiceDueInterval(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class InvoicingEmail(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class MotherCompanyID(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class Name(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class Notes(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class OptionsAddFeesToInvoices(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class OptionsAddTaxDeductedPaymentToInvoices(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class OptionsInvoiceable(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class Options(TypedDict, total=False):
    add_fees_to_invoices: Annotated[Optional[OptionsAddFeesToInvoices], PropertyInfo(alias="AddFeesToInvoices")]
    """
    Whether the company has an additional fee applied for invoicing or not (or
    `null` if the `AddFeesToInvoices` field should not be updated).
    """

    add_tax_deducted_payment_to_invoices: Annotated[
        Optional[OptionsAddTaxDeductedPaymentToInvoices], PropertyInfo(alias="AddTaxDeductedPaymentToInvoices")
    ]
    """
    Whether tax-deducted payments should be automatically added to invoices (or
    `null` if the `AddTaxDeductedPaymentToInvoices` field should not be updated).
    """

    invoiceable: Annotated[Optional[OptionsInvoiceable], PropertyInfo(alias="Invoiceable")]
    """
    Whether the company is invoiceable or not (or `null` if the `Invoiceable` field
    should not be updated).
    """


class ReferenceIdentifier(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class TaxIdentifier(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class Telephone(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class WebsiteURL(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]
