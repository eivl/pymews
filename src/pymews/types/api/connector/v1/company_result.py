# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["CompanyResult", "Company", "CompanyCreditRating", "CompanyOptions", "CompanyAddress"]


class CompanyCreditRating(BaseModel):
    basic: Optional[Literal["CreditOk", "PaymentRequiredUpfront", "LocalDecisionRequired"]] = FieldInfo(
        alias="Basic", default=None
    )
    """CreditOk (Company can book services.)

    PaymentRequiredUpfront (Company must pay upfront.)

    LocalDecisionRequired (Requires local approval.)

    - `CreditOk` - Company can book services.
    - `PaymentRequiredUpfront` - Company must pay upfront.
    - `LocalDecisionRequired` - Requires local approval.
    """


class CompanyOptions(BaseModel):
    add_fees_to_invoices: Optional[bool] = FieldInfo(alias="AddFeesToInvoices", default=None)
    """Whether the company has an additional fee applied for invoicing or not."""

    add_tax_deducted_payment_to_invoices: Optional[bool] = FieldInfo(
        alias="AddTaxDeductedPaymentToInvoices", default=None
    )
    """Whether tax-deducted payments should be automatically added to invoices."""

    invoiceable: Optional[bool] = FieldInfo(alias="Invoiceable", default=None)
    """Whether the company is invoiceable or not."""


class CompanyAddress(BaseModel):
    city: Optional[str] = FieldInfo(alias="City", default=None)
    """The city."""

    country_code: Optional[str] = FieldInfo(alias="CountryCode", default=None)
    """ISO 3166-1 code of the `Country`."""

    country_subdivision_code: Optional[str] = FieldInfo(alias="CountrySubdivisionCode", default=None)
    """ISO 3166-2 code of the administrative division, e.g. `DE-BW`."""

    id: Optional[str] = FieldInfo(alias="Id", default=None)
    """Unique identifier of the address."""

    latitude: Optional[float] = FieldInfo(alias="Latitude", default=None)
    """The latitude."""

    line1: Optional[str] = FieldInfo(alias="Line1", default=None)
    """First line of the address."""

    line2: Optional[str] = FieldInfo(alias="Line2", default=None)
    """Second line of the address."""

    longitude: Optional[float] = FieldInfo(alias="Longitude", default=None)
    """The longitude."""

    postal_code: Optional[str] = FieldInfo(alias="PostalCode", default=None)
    """Postal code."""


class Company(BaseModel):
    chain_id: str = FieldInfo(alias="ChainId")
    """Unique identifier of the chain."""

    credit_rating: CompanyCreditRating = FieldInfo(alias="CreditRating")
    """Credit rating to define creditworthiness of the company."""

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the company."""

    is_active: bool = FieldInfo(alias="IsActive")
    """Whether the company is still active."""

    name: str = FieldInfo(alias="Name")
    """Name of the company."""

    number: int = FieldInfo(alias="Number")
    """Unique number of the company."""

    options: CompanyOptions = FieldInfo(alias="Options")
    """Options of the company."""

    accounting_code: Optional[str] = FieldInfo(alias="AccountingCode", default=None)
    """Accounting code of the company."""

    additional_tax_identifier: Optional[str] = FieldInfo(alias="AdditionalTaxIdentifier", default=None)
    """Additional tax identifier of the company."""

    address: Optional[CompanyAddress] = FieldInfo(alias="Address", default=None)

    address_id: Optional[str] = FieldInfo(alias="AddressId", default=None)
    """
    Unique identifier of the company
    [Address](https://mews-systems.gitbook.io/connector-api/operations/addresses/#account-address).
    """

    billing_code: Optional[str] = FieldInfo(alias="BillingCode", default=None)
    """Billing code of the company."""

    contact: Optional[str] = FieldInfo(alias="Contact", default=None)
    """Other contact details, such as telephone, email or similar."""

    contact_person: Optional[str] = FieldInfo(alias="ContactPerson", default=None)
    """Contact person of the company."""

    created_utc: Optional[datetime] = FieldInfo(alias="CreatedUtc", default=None)
    """
    Date of
    [Company](https://mews-systems.gitbook.io/connector-api/operations/#company)
    creation date and time.
    """

    department: Optional[str] = FieldInfo(alias="Department", default=None)
    """The internal segmentation of a company, e.g. sales department."""

    duns_number: Optional[str] = FieldInfo(alias="DunsNumber", default=None)
    """The Dun & Bradstreet unique 9-digit DUNS number."""

    electronic_invoice_identifier: Optional[str] = FieldInfo(alias="ElectronicInvoiceIdentifier", default=None)
    """Electronic invoice identifier of the company."""

    external_identifier: Optional[str] = FieldInfo(alias="ExternalIdentifier", default=None)
    """Identifier of company from external system."""

    iata: Optional[str] = FieldInfo(alias="Iata", default=None)
    """Iata of the company."""

    identifier: Optional[str] = FieldInfo(alias="Identifier", default=None)
    """Other identifier of the company, e.g. legal identifier."""

    invoice_due_interval: Optional[str] = FieldInfo(alias="InvoiceDueInterval", default=None)
    """
    The maximum time, when the invoice has to be be paid in ISO 8601 duration
    format.
    """

    invoicing_email: Optional[str] = FieldInfo(alias="InvoicingEmail", default=None)
    """Email for issuing invoices to the company."""

    merge_target_id: Optional[str] = FieldInfo(alias="MergeTargetId", default=None)
    """Unique identifier of the account (Customer) to which this company is linked."""

    mother_company_id: Optional[str] = FieldInfo(alias="MotherCompanyId", default=None)
    """Unique identifier of mother company."""

    notes: Optional[str] = FieldInfo(alias="Notes", default=None)
    """Additional notes."""

    reference_identifier: Optional[str] = FieldInfo(alias="ReferenceIdentifier", default=None)
    """
    External system identifier - custom identifier used by an external system such
    as an external database.
    """

    tax_identification_number: Optional[str] = FieldInfo(alias="TaxIdentificationNumber", default=None)

    tax_identifier: Optional[str] = FieldInfo(alias="TaxIdentifier", default=None)
    """Tax identification number of the company."""

    telephone: Optional[str] = FieldInfo(alias="Telephone", default=None)
    """Contact telephone number."""

    updated_utc: Optional[datetime] = FieldInfo(alias="UpdatedUtc", default=None)
    """
    Date of
    [Company](https://mews-systems.gitbook.io/connector-api/operations/#company)
    last update date and time.
    """

    website_url: Optional[str] = FieldInfo(alias="WebsiteUrl", default=None)
    """The website url of the company."""


class CompanyResult(BaseModel):
    companies: List[Company] = FieldInfo(alias="Companies")
    """The company profiles of the enterprise."""

    cursor: Optional[str] = FieldInfo(alias="Cursor", default=None)
    """Unique identifier of the last and hence oldest company item returned.

    This can be used in
    [Limitation](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/#limitation)
    in a subsequent request to fetch the next batch of older companies. If
    [Limitation](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/#limitation)
    is specified in the request message, then Cursor will always be included in the
    response message; this is true even when using Extents set to false so that no
    actual data is returned.
    """
