# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["CompanyAddParams", "Options", "Address", "CreditRating"]


class CompanyAddParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    name: Required[Annotated[str, PropertyInfo(alias="Name")]]
    """Name of the company."""

    options: Required[Annotated[Options, PropertyInfo(alias="Options")]]
    """Options of the company."""

    accounting_code: Annotated[Optional[str], PropertyInfo(alias="AccountingCode")]
    """Accounting code of the company."""

    additional_tax_identifier: Annotated[Optional[str], PropertyInfo(alias="AdditionalTaxIdentifier")]
    """Additional tax identifer of the company."""

    address: Annotated[Optional[Address], PropertyInfo(alias="Address")]
    """New address details."""

    billing_code: Annotated[Optional[str], PropertyInfo(alias="BillingCode")]
    """Billing code of the company."""

    chain_id: Annotated[Optional[str], PropertyInfo(alias="ChainId")]
    """Unique identifier of the chain.

    Required when using
    [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
    ignored otherwise.
    """

    contact: Annotated[Optional[str], PropertyInfo(alias="Contact")]
    """Other contact details, such as telephone, email or similar."""

    contact_person: Annotated[Optional[str], PropertyInfo(alias="ContactPerson")]
    """Contact person of the company."""

    credit_rating: Annotated[Optional[CreditRating], PropertyInfo(alias="CreditRating")]
    """Credit rating to define creditworthiness of the company."""

    department: Annotated[Optional[str], PropertyInfo(alias="Department")]
    """The internal segmentation of a company, e.g. sales department."""

    duns_number: Annotated[Optional[str], PropertyInfo(alias="DunsNumber")]
    """The Dun & Bradstreet unique 9-digit DUNS number."""

    external_identifier: Annotated[Optional[str], PropertyInfo(alias="ExternalIdentifier")]
    """Identifier of the company from external system."""

    iata: Annotated[Optional[str], PropertyInfo(alias="Iata")]
    """Iata of the company."""

    identifier: Annotated[Optional[str], PropertyInfo(alias="Identifier")]
    """Identifier of the company (e.g. legal identifier)."""

    invoice_due_interval: Annotated[Optional[str], PropertyInfo(alias="InvoiceDueInterval")]
    """
    The maximum time, when the invoice has to be be paid in ISO 8601 duration
    format.
    """

    invoicing_email: Annotated[Optional[str], PropertyInfo(alias="InvoicingEmail")]
    """Email for issuing invoices to the company."""

    mother_company_id: Annotated[Optional[str], PropertyInfo(alias="MotherCompanyId")]
    """Unique identifier of the mother company."""

    notes: Annotated[Optional[str], PropertyInfo(alias="Notes")]
    """Notes of the company."""

    reference_identifier: Annotated[Optional[str], PropertyInfo(alias="ReferenceIdentifier")]
    """
    External system identifier - custom identifier used by an external system such
    as an external database.
    """

    tax_identifier: Annotated[Optional[str], PropertyInfo(alias="TaxIdentifier")]
    """Tax identification number of the company."""

    telephone: Annotated[Optional[str], PropertyInfo(alias="Telephone")]
    """Contact telephone number."""

    website_url: Annotated[Optional[str], PropertyInfo(alias="WebsiteUrl")]
    """The website url of the company."""


class Options(TypedDict, total=False):
    add_fees_to_invoices: Annotated[bool, PropertyInfo(alias="AddFeesToInvoices")]
    """Whether the company has an additional fee applied for invoicing or not."""

    add_tax_deducted_payment_to_invoices: Annotated[bool, PropertyInfo(alias="AddTaxDeductedPaymentToInvoices")]
    """Whether tax-deducted payments should be automatically added to invoices."""

    invoiceable: Annotated[bool, PropertyInfo(alias="Invoiceable")]
    """Whether the company is invoiceable or not."""


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


class CreditRating(TypedDict, total=False):
    basic: Annotated[
        Optional[Literal["CreditOk", "PaymentRequiredUpfront", "LocalDecisionRequired"]], PropertyInfo(alias="Basic")
    ]
    """CreditOk (Company can book services.)

    PaymentRequiredUpfront (Company must pay upfront.)

    LocalDecisionRequired (Requires local approval.)

    - `CreditOk` - Company can book services.
    - `PaymentRequiredUpfront` - Company must pay upfront.
    - `LocalDecisionRequired` - Requires local approval.
    """
