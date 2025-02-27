# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = [
    "AccountUpdateResponse",
    "Account",
    "AccountCompany",
    "AccountCompanyClassifications",
    "AccountCompanyOptions",
    "AccountCustomer",
    "AccountCustomerClassifications",
    "AccountCustomerLegalEntityIdentifiers",
    "AccountCustomerOptions",
]


class AccountCompanyClassifications(BaseModel):
    corporate: Optional[bool] = FieldInfo(alias="Corporate", default=None)
    """Corporate."""

    global_distribution_system: Optional[bool] = FieldInfo(alias="GlobalDistributionSystem", default=None)
    """Global distribution system."""

    government_entity: Optional[bool] = FieldInfo(alias="GovernmentEntity", default=None)
    """Government Entity"""

    inactive: Optional[bool] = FieldInfo(alias="Inactive", default=None)
    """Inactive."""

    internal: Optional[bool] = FieldInfo(alias="Internal", default=None)
    """Internal."""

    marketing: Optional[bool] = FieldInfo(alias="Marketing", default=None)
    """Marketing."""

    online_travel_agency: Optional[bool] = FieldInfo(alias="OnlineTravelAgency", default=None)
    """Online travel agency."""

    private: Optional[bool] = FieldInfo(alias="Private", default=None)
    """Private."""


class AccountCompanyOptions(BaseModel):
    add_fees_to_invoices: Optional[bool] = FieldInfo(alias="AddFeesToInvoices", default=None)
    """Whether the company has an additional fee applied for invoicing or not."""

    add_tax_deducted_payment_to_invoices: Optional[bool] = FieldInfo(
        alias="AddTaxDeductedPaymentToInvoices", default=None
    )
    """Whether tax-deducted payments should be automatically added to invoices."""

    invoiceable: Optional[bool] = FieldInfo(alias="Invoiceable", default=None)
    """Whether the company is invoiceable or not."""


class AccountCompany(BaseModel):
    chain_id: str = FieldInfo(alias="ChainId")
    """Unique identifier of the chain."""

    classifications: AccountCompanyClassifications = FieldInfo(alias="Classifications")
    """Classifications of the company."""

    created_utc: datetime = FieldInfo(alias="CreatedUtc")
    """Creation date and time of the `Company` in UTC timezone in ISO 8601 format."""

    name: str = FieldInfo(alias="Name")
    """Name of the company."""

    options: AccountCompanyOptions = FieldInfo(alias="Options")
    """Options of the company."""

    updated_utc: datetime = FieldInfo(alias="UpdatedUtc")
    """Last update date and time of the `Company` in UTC timezone in ISO 8601 format."""

    updater_profile_id: str = FieldInfo(alias="UpdaterProfileId")
    """Unique identifier of the user who updated the company."""

    accounting_code: Optional[str] = FieldInfo(alias="AccountingCode", default=None)
    """Accounting code of the company."""

    additional_tax_identifier: Optional[str] = FieldInfo(alias="AdditionalTaxIdentifier", default=None)
    """Additional tax identifier of the company."""

    billing_code: Optional[str] = FieldInfo(alias="BillingCode", default=None)
    """Billing code of the company."""

    contact: Optional[str] = FieldInfo(alias="Contact", default=None)
    """Other contact details, such as telephone, email or similar."""

    contact_person: Optional[str] = FieldInfo(alias="ContactPerson", default=None)
    """Contact person of the company."""

    credit_rating_basic: Optional[Literal["CreditOk", "PaymentRequiredUpfront", "LocalDecisionRequired"]] = FieldInfo(
        alias="CreditRatingBasic", default=None
    )
    """CreditOk (Company can book services.)

    PaymentRequiredUpfront (Company must pay upfront.)

    LocalDecisionRequired (Requires local approval.)

    - `CreditOk` - Company can book services.
    - `PaymentRequiredUpfront` - Company must pay upfront.
    - `LocalDecisionRequired` - Requires local approval.
    """

    department: Optional[str] = FieldInfo(alias="Department", default=None)
    """The internal segmentation of a company, e.g. sales department."""

    duns_number: Optional[str] = FieldInfo(alias="DunsNumber", default=None)
    """The Dun & Bradstreet unique 9-digit DUNS number."""

    email: Optional[str] = FieldInfo(alias="Email", default=None)
    """Email address of the company."""

    external_identifier: Optional[str] = FieldInfo(alias="ExternalIdentifier", default=None)
    """Identifier of company from external system."""

    fiscal_identifier: Optional[str] = FieldInfo(alias="FiscalIdentifier", default=None)
    """Fiscal identifier of the company."""

    iata: Optional[str] = FieldInfo(alias="Iata", default=None)
    """Iata of the company."""

    invoice_due_interval: Optional[str] = FieldInfo(alias="InvoiceDueInterval", default=None)
    """
    The maximum time (in ISO 8601 duration format), when the invoice has to be be
    paid.
    """

    mother_company_id: Optional[str] = FieldInfo(alias="MotherCompanyId", default=None)
    """Unique identifier of mother company."""

    notes: Optional[str] = FieldInfo(alias="Notes", default=None)
    """Additional notes."""

    reference_id: Optional[str] = FieldInfo(alias="ReferenceId", default=None)
    """
    External system identifier - custom identifier used by an external system such
    as an external database.
    """

    source_id: Optional[str] = FieldInfo(alias="SourceId", default=None)
    """Unique identifier of the `Source`."""

    tax_identifier: Optional[str] = FieldInfo(alias="TaxIdentifier", default=None)
    """Tax identification number of the company."""

    telephone: Optional[str] = FieldInfo(alias="Telephone", default=None)
    """Contact telephone number."""

    website_url: Optional[str] = FieldInfo(alias="WebsiteUrl", default=None)
    """The website url of the company."""


class AccountCustomerClassifications(BaseModel):
    airline: Optional[bool] = FieldInfo(alias="Airline", default=None)
    """Airline."""

    blacklist: Optional[bool] = FieldInfo(alias="Blacklist", default=None)
    """Blacklist."""

    cashlist: Optional[bool] = FieldInfo(alias="Cashlist", default=None)
    """Cash list."""

    disabled_person: Optional[bool] = FieldInfo(alias="DisabledPerson", default=None)
    """Disabled person."""

    friend_or_family: Optional[bool] = FieldInfo(alias="FriendOrFamily", default=None)
    """Friend or family."""

    health_compliant: Optional[bool] = FieldInfo(alias="HealthCompliant", default=None)
    """Health compliant."""

    important: Optional[bool] = FieldInfo(alias="Important", default=None)
    """Important."""

    in_room: Optional[bool] = FieldInfo(alias="InRoom", default=None)
    """In room."""

    loyalty_program: Optional[bool] = FieldInfo(alias="LoyaltyProgram", default=None)
    """Loyalty program."""

    media: Optional[bool] = FieldInfo(alias="Media", default=None)
    """Media."""

    military: Optional[bool] = FieldInfo(alias="Military", default=None)
    """Military."""

    paymaster_account: Optional[bool] = FieldInfo(alias="PaymasterAccount", default=None)
    """Paymaster account."""

    previous_complaint: Optional[bool] = FieldInfo(alias="PreviousComplaint", default=None)
    """Previous complaint."""

    problematic: Optional[bool] = FieldInfo(alias="Problematic", default=None)
    """Problematic."""

    returning: Optional[bool] = FieldInfo(alias="Returning", default=None)
    """Returning."""

    staff: Optional[bool] = FieldInfo(alias="Staff", default=None)
    """Staff."""

    student: Optional[bool] = FieldInfo(alias="Student", default=None)
    """Student."""

    top_management: Optional[bool] = FieldInfo(alias="TopManagement", default=None)
    """Top management."""

    very_important: Optional[bool] = FieldInfo(alias="VeryImportant", default=None)
    """Very important."""

    waiting_for_room: Optional[bool] = FieldInfo(alias="WaitingForRoom", default=None)
    """Waiting for room."""


class AccountCustomerLegalEntityIdentifiers(BaseModel):
    it_destination_code: Optional[str] = FieldInfo(alias="ItDestinationCode", default=None)
    """Italian destination code."""

    it_fiscal_code: Optional[str] = FieldInfo(alias="ItFiscalCode", default=None)
    """Italian fiscal code."""


class AccountCustomerOptions(BaseModel):
    bill_address_objection: Optional[bool] = FieldInfo(alias="BillAddressObjection", default=None)
    """Bill address objection."""

    invoiceable: Optional[bool] = FieldInfo(alias="Invoiceable", default=None)
    """Invoiceable."""

    send_marketing_emails: Optional[bool] = FieldInfo(alias="SendMarketingEmails", default=None)
    """Send marketing emails."""


class AccountCustomer(BaseModel):
    chain_id: str = FieldInfo(alias="ChainId")
    """Unique identifier of the chain."""

    classifications: AccountCustomerClassifications = FieldInfo(alias="Classifications")
    """Classifications of the customer."""

    created_utc: datetime = FieldInfo(alias="CreatedUtc")
    """Creation date and time of the customer in UTC timezone in ISO 8601 format."""

    last_name: str = FieldInfo(alias="LastName")
    """Last name of the customer."""

    legal_entity_identifiers: AccountCustomerLegalEntityIdentifiers = FieldInfo(alias="LegalEntityIdentifiers")
    """Legal entity identifiers of the customer."""

    options: AccountCustomerOptions = FieldInfo(alias="Options")
    """Options of the customer."""

    updated_utc: datetime = FieldInfo(alias="UpdatedUtc")
    """Last update date and time of the customer in UTC timezone in ISO 8601 format."""

    updater_profile_id: str = FieldInfo(alias="UpdaterProfileId")
    """Unique identifier of the user who updated the customer."""

    accounting_code: Optional[str] = FieldInfo(alias="AccountingCode", default=None)
    """Accounting code of the customer."""

    billing_code: Optional[str] = FieldInfo(alias="BillingCode", default=None)
    """Billing code of the customer."""

    birth_date: Optional[datetime] = FieldInfo(alias="BirthDate", default=None)
    """Date of birth in ISO 8601 format."""

    birth_place: Optional[str] = FieldInfo(alias="BirthPlace", default=None)
    """Place of birth."""

    car_registration_number: Optional[str] = FieldInfo(alias="CarRegistrationNumber", default=None)
    """Registration number of the customer's car."""

    company_id: Optional[str] = FieldInfo(alias="CompanyId", default=None)
    """Unique identifier of `Company` the customer is associated with."""

    dietary_requirements: Optional[str] = FieldInfo(alias="DietaryRequirements", default=None)
    """Dietary requirements of the customer."""

    email: Optional[str] = FieldInfo(alias="Email", default=None)
    """Email address of the customer."""

    first_name: Optional[str] = FieldInfo(alias="FirstName", default=None)
    """First name of the customer."""

    loyalty_code: Optional[str] = FieldInfo(alias="LoyaltyCode", default=None)
    """Loyalty code of the customer."""

    nationality_code: Optional[str] = FieldInfo(alias="NationalityCode", default=None)
    """ISO 3166-1 code of the `Country`."""

    notes: Optional[str] = FieldInfo(alias="Notes", default=None)
    """Internal notes about the customer."""

    occupation: Optional[str] = FieldInfo(alias="Occupation", default=None)
    """Occupation of the customer."""

    preferred_language_code: Optional[str] = FieldInfo(alias="PreferredLanguageCode", default=None)
    """Language and culture code of the customer's preferred language.

    E.g. `en-US` or `fr-FR`.
    """

    second_last_name: Optional[str] = FieldInfo(alias="SecondLastName", default=None)
    """Second last name of the customer."""

    sex: Optional[str] = FieldInfo(alias="Sex", default=None)
    """Sex of the customer."""

    tax_identifier: Optional[str] = FieldInfo(alias="TaxIdentifier", default=None)
    """Tax identification number of the customer."""

    telephone: Optional[str] = FieldInfo(alias="Telephone", default=None)
    """Telephone number of the customer (possibly mobile)."""

    title: Optional[Literal["Mister", "Miss", "Misses"]] = FieldInfo(alias="Title", default=None)
    """Type of the title prefix of the customer.

    Note that the value should not be used as-is, but localized. For example, the
    value `Misses` should be displayed as `Mrs.` in English and `Fr.` in German.

    Mister (Mr.)

    Miss (Ms.)

    Misses (Mrs.)

    - `Mister` - Mr.
    - `Miss` - Ms.
    - `Misses` - Mrs.
    """


class Account(BaseModel):
    discriminator: Literal["Company", "Customer"] = FieldInfo(alias="Discriminator")
    """Company

    Customer
    """

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the account."""

    company: Optional[AccountCompany] = FieldInfo(alias="Company", default=None)

    customer: Optional[AccountCustomer] = FieldInfo(alias="Customer", default=None)
    """Updated customer data."""


class AccountUpdateResponse(BaseModel):
    accounts: List[Account] = FieldInfo(alias="Accounts")
    """Updated accounts."""
