# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = [
    "AccountUpdateParams",
    "AccountUpdate",
    "AccountUpdateCompany",
    "AccountUpdateCompanyAccountingCode",
    "AccountUpdateCompanyAdditionalTaxIdentifier",
    "AccountUpdateCompanyBillingCode",
    "AccountUpdateCompanyClassifications",
    "AccountUpdateCompanyClassificationsCorporate",
    "AccountUpdateCompanyClassificationsGlobalDistributionSystem",
    "AccountUpdateCompanyClassificationsGovernmentEntity",
    "AccountUpdateCompanyClassificationsInactive",
    "AccountUpdateCompanyClassificationsInternal",
    "AccountUpdateCompanyClassificationsMarketing",
    "AccountUpdateCompanyClassificationsOnlineTravelAgency",
    "AccountUpdateCompanyClassificationsPrivate",
    "AccountUpdateCompanyContact",
    "AccountUpdateCompanyContactPerson",
    "AccountUpdateCompanyCreditRatingBasic",
    "AccountUpdateCompanyDepartment",
    "AccountUpdateCompanyDunsNumber",
    "AccountUpdateCompanyEmail",
    "AccountUpdateCompanyExternalIdentifier",
    "AccountUpdateCompanyFiscalIdentifier",
    "AccountUpdateCompanyIata",
    "AccountUpdateCompanyInvoiceDueInterval",
    "AccountUpdateCompanyMotherCompanyID",
    "AccountUpdateCompanyName",
    "AccountUpdateCompanyNotes",
    "AccountUpdateCompanyOptions",
    "AccountUpdateCompanyOptionsAddFeesToInvoices",
    "AccountUpdateCompanyOptionsAddTaxDeductedPaymentToInvoices",
    "AccountUpdateCompanyOptionsInvoiceable",
    "AccountUpdateCompanyReferenceID",
    "AccountUpdateCompanySourceID",
    "AccountUpdateCompanyTaxIdentifier",
    "AccountUpdateCompanyTelephone",
    "AccountUpdateCompanyWebsiteURL",
    "AccountUpdateCustomer",
    "AccountUpdateCustomerAccountingCode",
    "AccountUpdateCustomerBillingCode",
    "AccountUpdateCustomerBirthDate",
    "AccountUpdateCustomerBirthPlace",
    "AccountUpdateCustomerCarRegistrationNumber",
    "AccountUpdateCustomerClassifications",
    "AccountUpdateCustomerClassificationsAirline",
    "AccountUpdateCustomerClassificationsBlacklist",
    "AccountUpdateCustomerClassificationsCashlist",
    "AccountUpdateCustomerClassificationsDisabledPerson",
    "AccountUpdateCustomerClassificationsFriendOrFamily",
    "AccountUpdateCustomerClassificationsHealthCompliant",
    "AccountUpdateCustomerClassificationsImportant",
    "AccountUpdateCustomerClassificationsInRoom",
    "AccountUpdateCustomerClassificationsLoyaltyProgram",
    "AccountUpdateCustomerClassificationsMedia",
    "AccountUpdateCustomerClassificationsMilitary",
    "AccountUpdateCustomerClassificationsPaymasterAccount",
    "AccountUpdateCustomerClassificationsPreviousComplaint",
    "AccountUpdateCustomerClassificationsProblematic",
    "AccountUpdateCustomerClassificationsReturning",
    "AccountUpdateCustomerClassificationsStaff",
    "AccountUpdateCustomerClassificationsStudent",
    "AccountUpdateCustomerClassificationsTopManagement",
    "AccountUpdateCustomerClassificationsVeryImportant",
    "AccountUpdateCustomerClassificationsWaitingForRoom",
    "AccountUpdateCustomerCompanyID",
    "AccountUpdateCustomerDietaryRequirements",
    "AccountUpdateCustomerEmail",
    "AccountUpdateCustomerFirstName",
    "AccountUpdateCustomerLastName",
    "AccountUpdateCustomerLegalEntityIdentifiers",
    "AccountUpdateCustomerLegalEntityIdentifiersItDestinationCode",
    "AccountUpdateCustomerLegalEntityIdentifiersItFiscalCode",
    "AccountUpdateCustomerLoyaltyCode",
    "AccountUpdateCustomerNationalityCode",
    "AccountUpdateCustomerNotes",
    "AccountUpdateCustomerOccupation",
    "AccountUpdateCustomerOptions",
    "AccountUpdateCustomerOptionsBillAddressObjection",
    "AccountUpdateCustomerOptionsInvoiceable",
    "AccountUpdateCustomerOptionsSendMarketingEmails",
    "AccountUpdateCustomerPreferredLanguageCode",
    "AccountUpdateCustomerSecondLastName",
    "AccountUpdateCustomerSex",
    "AccountUpdateCustomerTaxIdentifier",
    "AccountUpdateCustomerTelephone",
    "AccountUpdateCustomerTitle",
]


class AccountUpdateParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    account_updates: Required[Annotated[Iterable[AccountUpdate], PropertyInfo(alias="AccountUpdates")]]
    """Accounts to be updated."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    chain_id: Annotated[Optional[str], PropertyInfo(alias="ChainId")]
    """Unique identifier of the chain.

    Required when using
    [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
    ignored otherwise.
    """


class AccountUpdateCompanyAccountingCode(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AccountUpdateCompanyAdditionalTaxIdentifier(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AccountUpdateCompanyBillingCode(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AccountUpdateCompanyClassificationsCorporate(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class AccountUpdateCompanyClassificationsGlobalDistributionSystem(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class AccountUpdateCompanyClassificationsGovernmentEntity(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class AccountUpdateCompanyClassificationsInactive(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class AccountUpdateCompanyClassificationsInternal(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class AccountUpdateCompanyClassificationsMarketing(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class AccountUpdateCompanyClassificationsOnlineTravelAgency(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class AccountUpdateCompanyClassificationsPrivate(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class AccountUpdateCompanyClassifications(TypedDict, total=False):
    corporate: Annotated[Optional[AccountUpdateCompanyClassificationsCorporate], PropertyInfo(alias="Corporate")]
    """Corporate (or `null` if the value should not be updated)."""

    global_distribution_system: Annotated[
        Optional[AccountUpdateCompanyClassificationsGlobalDistributionSystem],
        PropertyInfo(alias="GlobalDistributionSystem"),
    ]
    """Global distribution system (or `null` if the value should not be updated)."""

    government_entity: Annotated[
        Optional[AccountUpdateCompanyClassificationsGovernmentEntity], PropertyInfo(alias="GovernmentEntity")
    ]
    """Government Entity (or `null` if the value should not be updated)."""

    inactive: Annotated[Optional[AccountUpdateCompanyClassificationsInactive], PropertyInfo(alias="Inactive")]
    """Inactive (or `null` if the value should not be updated)."""

    internal: Annotated[Optional[AccountUpdateCompanyClassificationsInternal], PropertyInfo(alias="Internal")]
    """Internal (or `null` if the value should not be updated)."""

    marketing: Annotated[Optional[AccountUpdateCompanyClassificationsMarketing], PropertyInfo(alias="Marketing")]
    """Marketing (or `null` if the value should not be updated)."""

    online_travel_agency: Annotated[
        Optional[AccountUpdateCompanyClassificationsOnlineTravelAgency], PropertyInfo(alias="OnlineTravelAgency")
    ]
    """Online travel agency (or `null` if the value should not be updated)."""

    private: Annotated[Optional[AccountUpdateCompanyClassificationsPrivate], PropertyInfo(alias="Private")]
    """Private (or `null` if the value should not be updated)."""


class AccountUpdateCompanyContact(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AccountUpdateCompanyContactPerson(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AccountUpdateCompanyCreditRatingBasic(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AccountUpdateCompanyDepartment(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AccountUpdateCompanyDunsNumber(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AccountUpdateCompanyEmail(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AccountUpdateCompanyExternalIdentifier(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AccountUpdateCompanyFiscalIdentifier(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AccountUpdateCompanyIata(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AccountUpdateCompanyInvoiceDueInterval(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AccountUpdateCompanyMotherCompanyID(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AccountUpdateCompanyName(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AccountUpdateCompanyNotes(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AccountUpdateCompanyOptionsAddFeesToInvoices(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class AccountUpdateCompanyOptionsAddTaxDeductedPaymentToInvoices(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class AccountUpdateCompanyOptionsInvoiceable(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class AccountUpdateCompanyOptions(TypedDict, total=False):
    add_fees_to_invoices: Annotated[
        Optional[AccountUpdateCompanyOptionsAddFeesToInvoices], PropertyInfo(alias="AddFeesToInvoices")
    ]
    """
    Whether the company has an additional fee applied for invoicing or not (or
    `null` if the `AddFeesToInvoices` field should not be updated).
    """

    add_tax_deducted_payment_to_invoices: Annotated[
        Optional[AccountUpdateCompanyOptionsAddTaxDeductedPaymentToInvoices],
        PropertyInfo(alias="AddTaxDeductedPaymentToInvoices"),
    ]
    """
    Whether tax-deducted payments should be automatically added to invoices (or
    `null` if the `AddTaxDeductedPaymentToInvoices` field should not be updated).
    """

    invoiceable: Annotated[Optional[AccountUpdateCompanyOptionsInvoiceable], PropertyInfo(alias="Invoiceable")]
    """
    Whether the company is invoiceable or not (or `null` if the `Invoiceable` field
    should not be updated).
    """


class AccountUpdateCompanyReferenceID(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AccountUpdateCompanySourceID(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AccountUpdateCompanyTaxIdentifier(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AccountUpdateCompanyTelephone(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AccountUpdateCompanyWebsiteURL(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AccountUpdateCompany(TypedDict, total=False):
    accounting_code: Annotated[Optional[AccountUpdateCompanyAccountingCode], PropertyInfo(alias="AccountingCode")]
    """Accounting code (or `null` if the accounting code should not be updated)."""

    additional_tax_identifier: Annotated[
        Optional[AccountUpdateCompanyAdditionalTaxIdentifier], PropertyInfo(alias="AdditionalTaxIdentifier")
    ]
    """
    Additional tax identifier (or `null` if the additional tax identifier should not
    be updated).
    """

    billing_code: Annotated[Optional[AccountUpdateCompanyBillingCode], PropertyInfo(alias="BillingCode")]
    """Billing code (or `null` if the billing code should not be updated)."""

    classifications: Annotated[Optional[AccountUpdateCompanyClassifications], PropertyInfo(alias="Classifications")]
    """Classifications of the company."""

    contact: Annotated[Optional[AccountUpdateCompanyContact], PropertyInfo(alias="Contact")]
    """Contact (or `null` if the contact should not be updated)."""

    contact_person: Annotated[Optional[AccountUpdateCompanyContactPerson], PropertyInfo(alias="ContactPerson")]
    """Contact person (or `null` if the contact person should not be updated)."""

    credit_rating_basic: Annotated[
        Optional[AccountUpdateCompanyCreditRatingBasic], PropertyInfo(alias="CreditRatingBasic")
    ]
    """
    Basic credit rating (or `null` if the basic credit rating should not be
    updated).
    """

    department: Annotated[Optional[AccountUpdateCompanyDepartment], PropertyInfo(alias="Department")]
    """Department (or `null` if the department should not be updated)."""

    duns_number: Annotated[Optional[AccountUpdateCompanyDunsNumber], PropertyInfo(alias="DunsNumber")]
    """Duns number (or `null` if the duns number should not be updated)."""

    email: Annotated[Optional[AccountUpdateCompanyEmail], PropertyInfo(alias="Email")]
    """Email address (or `null` if the email should not be updated)."""

    external_identifier: Annotated[
        Optional[AccountUpdateCompanyExternalIdentifier], PropertyInfo(alias="ExternalIdentifier")
    ]
    """
    External identifier (or `null` if the external identifier should not be
    updated).
    """

    fiscal_identifier: Annotated[Optional[AccountUpdateCompanyFiscalIdentifier], PropertyInfo(alias="FiscalIdentifier")]
    """Fiscal identifier (or `null` if the fiscal identifier should not be updated)."""

    iata: Annotated[Optional[AccountUpdateCompanyIata], PropertyInfo(alias="Iata")]
    """IATA of the company (or `null` if the iata should not be updated)."""

    invoice_due_interval: Annotated[
        Optional[AccountUpdateCompanyInvoiceDueInterval], PropertyInfo(alias="InvoiceDueInterval")
    ]
    """
    Invoice due interval (or `null` if the invoice due interval should not be
    updated).
    """

    mother_company_id: Annotated[Optional[AccountUpdateCompanyMotherCompanyID], PropertyInfo(alias="MotherCompanyId")]
    """
    Mother company identifier (or `null` if the mother company identifier should not
    be updated).
    """

    name: Annotated[Optional[AccountUpdateCompanyName], PropertyInfo(alias="Name")]
    """Name (or `null` if the name should not be updated)."""

    notes: Annotated[Optional[AccountUpdateCompanyNotes], PropertyInfo(alias="Notes")]
    """Notes (or `null` if the notes should not be updated)."""

    options: Annotated[Optional[AccountUpdateCompanyOptions], PropertyInfo(alias="Options")]
    """Options of the company."""

    reference_id: Annotated[Optional[AccountUpdateCompanyReferenceID], PropertyInfo(alias="ReferenceId")]
    """
    Reference identifier (or `null` if the reference identifier should not be
    updated).
    """

    source_id: Annotated[Optional[AccountUpdateCompanySourceID], PropertyInfo(alias="SourceId")]
    """Source identifier (or `null` if the source identifier should not be updated)."""

    tax_identifier: Annotated[Optional[AccountUpdateCompanyTaxIdentifier], PropertyInfo(alias="TaxIdentifier")]
    """
    Tax identification number (or `null` if the tax identification number should not
    be updated).
    """

    telephone: Annotated[Optional[AccountUpdateCompanyTelephone], PropertyInfo(alias="Telephone")]
    """Telephone number (or `null` if the telephone number should not be updated)."""

    website_url: Annotated[Optional[AccountUpdateCompanyWebsiteURL], PropertyInfo(alias="WebsiteUrl")]
    """Website url (or `null` if the website url should not be updated)."""


class AccountUpdateCustomerAccountingCode(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AccountUpdateCustomerBillingCode(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AccountUpdateCustomerBirthDate(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AccountUpdateCustomerBirthPlace(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AccountUpdateCustomerCarRegistrationNumber(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AccountUpdateCustomerClassificationsAirline(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class AccountUpdateCustomerClassificationsBlacklist(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class AccountUpdateCustomerClassificationsCashlist(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class AccountUpdateCustomerClassificationsDisabledPerson(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class AccountUpdateCustomerClassificationsFriendOrFamily(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class AccountUpdateCustomerClassificationsHealthCompliant(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class AccountUpdateCustomerClassificationsImportant(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class AccountUpdateCustomerClassificationsInRoom(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class AccountUpdateCustomerClassificationsLoyaltyProgram(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class AccountUpdateCustomerClassificationsMedia(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class AccountUpdateCustomerClassificationsMilitary(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class AccountUpdateCustomerClassificationsPaymasterAccount(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class AccountUpdateCustomerClassificationsPreviousComplaint(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class AccountUpdateCustomerClassificationsProblematic(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class AccountUpdateCustomerClassificationsReturning(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class AccountUpdateCustomerClassificationsStaff(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class AccountUpdateCustomerClassificationsStudent(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class AccountUpdateCustomerClassificationsTopManagement(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class AccountUpdateCustomerClassificationsVeryImportant(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class AccountUpdateCustomerClassificationsWaitingForRoom(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class AccountUpdateCustomerClassifications(TypedDict, total=False):
    airline: Annotated[Optional[AccountUpdateCustomerClassificationsAirline], PropertyInfo(alias="Airline")]
    """Airline (or `null` if the value should not be updated)."""

    blacklist: Annotated[Optional[AccountUpdateCustomerClassificationsBlacklist], PropertyInfo(alias="Blacklist")]
    """Blacklist (or `null` if the value should not be updated)."""

    cashlist: Annotated[Optional[AccountUpdateCustomerClassificationsCashlist], PropertyInfo(alias="Cashlist")]
    """Cashlist (or `null` if the value should not be updated)."""

    disabled_person: Annotated[
        Optional[AccountUpdateCustomerClassificationsDisabledPerson], PropertyInfo(alias="DisabledPerson")
    ]
    """Disabled person (or `null` if the value should not be updated)."""

    friend_or_family: Annotated[
        Optional[AccountUpdateCustomerClassificationsFriendOrFamily], PropertyInfo(alias="FriendOrFamily")
    ]
    """Friend or family (or `null` if the value should not be updated)."""

    health_compliant: Annotated[
        Optional[AccountUpdateCustomerClassificationsHealthCompliant], PropertyInfo(alias="HealthCompliant")
    ]
    """Health compliant (or `null` if the value should not be updated)."""

    important: Annotated[Optional[AccountUpdateCustomerClassificationsImportant], PropertyInfo(alias="Important")]
    """Important (or `null` if the value should not be updated)."""

    in_room: Annotated[Optional[AccountUpdateCustomerClassificationsInRoom], PropertyInfo(alias="InRoom")]
    """In room (or `null` if the value should not be updated)."""

    loyalty_program: Annotated[
        Optional[AccountUpdateCustomerClassificationsLoyaltyProgram], PropertyInfo(alias="LoyaltyProgram")
    ]
    """Loyalty program (or `null` if the value should not be updated)."""

    media: Annotated[Optional[AccountUpdateCustomerClassificationsMedia], PropertyInfo(alias="Media")]
    """Media (or `null` if the value should not be updated)."""

    military: Annotated[Optional[AccountUpdateCustomerClassificationsMilitary], PropertyInfo(alias="Military")]
    """Military (or `null` if the value should not be updated)."""

    paymaster_account: Annotated[
        Optional[AccountUpdateCustomerClassificationsPaymasterAccount], PropertyInfo(alias="PaymasterAccount")
    ]
    """Paymaster account (or `null` if the value should not be updated)."""

    previous_complaint: Annotated[
        Optional[AccountUpdateCustomerClassificationsPreviousComplaint], PropertyInfo(alias="PreviousComplaint")
    ]
    """Previous complaint (or `null` if the value should not be updated)."""

    problematic: Annotated[Optional[AccountUpdateCustomerClassificationsProblematic], PropertyInfo(alias="Problematic")]
    """Problematic (or `null` if the value should not be updated)."""

    returning: Annotated[Optional[AccountUpdateCustomerClassificationsReturning], PropertyInfo(alias="Returning")]
    """Returning (or `null` if the value should not be updated)."""

    staff: Annotated[Optional[AccountUpdateCustomerClassificationsStaff], PropertyInfo(alias="Staff")]
    """Staff (or `null` if the value should not be updated)."""

    student: Annotated[Optional[AccountUpdateCustomerClassificationsStudent], PropertyInfo(alias="Student")]
    """Student (or `null` if the value should not be updated)."""

    top_management: Annotated[
        Optional[AccountUpdateCustomerClassificationsTopManagement], PropertyInfo(alias="TopManagement")
    ]
    """Top management (or `null` if the value should not be updated)."""

    very_important: Annotated[
        Optional[AccountUpdateCustomerClassificationsVeryImportant], PropertyInfo(alias="VeryImportant")
    ]
    """Very important (or `null` if the value should not be updated)."""

    waiting_for_room: Annotated[
        Optional[AccountUpdateCustomerClassificationsWaitingForRoom], PropertyInfo(alias="WaitingForRoom")
    ]
    """Waiting for room (or `null` if the value should not be updated)."""


class AccountUpdateCustomerCompanyID(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AccountUpdateCustomerDietaryRequirements(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AccountUpdateCustomerEmail(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AccountUpdateCustomerFirstName(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AccountUpdateCustomerLastName(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AccountUpdateCustomerLegalEntityIdentifiersItDestinationCode(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AccountUpdateCustomerLegalEntityIdentifiersItFiscalCode(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AccountUpdateCustomerLegalEntityIdentifiers(TypedDict, total=False):
    it_destination_code: Annotated[
        Optional[AccountUpdateCustomerLegalEntityIdentifiersItDestinationCode], PropertyInfo(alias="ItDestinationCode")
    ]
    """
    Italian destination code (or `null` if the Italian destination code should not
    be updated).
    """

    it_fiscal_code: Annotated[
        Optional[AccountUpdateCustomerLegalEntityIdentifiersItFiscalCode], PropertyInfo(alias="ItFiscalCode")
    ]
    """
    Italian fiscal code (or `null` if the Italian fiscal code should not be
    updated).
    """


class AccountUpdateCustomerLoyaltyCode(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AccountUpdateCustomerNationalityCode(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AccountUpdateCustomerNotes(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AccountUpdateCustomerOccupation(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AccountUpdateCustomerOptionsBillAddressObjection(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class AccountUpdateCustomerOptionsInvoiceable(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class AccountUpdateCustomerOptionsSendMarketingEmails(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class AccountUpdateCustomerOptions(TypedDict, total=False):
    bill_address_objection: Annotated[
        Optional[AccountUpdateCustomerOptionsBillAddressObjection], PropertyInfo(alias="BillAddressObjection")
    ]
    """Bill address objection (or `null` if the value should not be updated)."""

    invoiceable: Annotated[Optional[AccountUpdateCustomerOptionsInvoiceable], PropertyInfo(alias="Invoiceable")]
    """Invoiceable (or `null` if the value should not be updated)."""

    send_marketing_emails: Annotated[
        Optional[AccountUpdateCustomerOptionsSendMarketingEmails], PropertyInfo(alias="SendMarketingEmails")
    ]
    """Send marketing email (or `null` if the value should not be updated)."""


class AccountUpdateCustomerPreferredLanguageCode(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AccountUpdateCustomerSecondLastName(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AccountUpdateCustomerSex(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AccountUpdateCustomerTaxIdentifier(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AccountUpdateCustomerTelephone(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AccountUpdateCustomerTitle(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AccountUpdateCustomer(TypedDict, total=False):
    accounting_code: Annotated[Optional[AccountUpdateCustomerAccountingCode], PropertyInfo(alias="AccountingCode")]
    """Accounting code (or `null` if the accounting code should not be updated)."""

    billing_code: Annotated[Optional[AccountUpdateCustomerBillingCode], PropertyInfo(alias="BillingCode")]
    """Billing code (or `null` if the billing code should not be updated)."""

    birth_date: Annotated[Optional[AccountUpdateCustomerBirthDate], PropertyInfo(alias="BirthDate")]
    """Birth date (or `null` if the birth date should not be updated)."""

    birth_place: Annotated[Optional[AccountUpdateCustomerBirthPlace], PropertyInfo(alias="BirthPlace")]
    """Birth place (or `null` if the birth place should not be updated)."""

    car_registration_number: Annotated[
        Optional[AccountUpdateCustomerCarRegistrationNumber], PropertyInfo(alias="CarRegistrationNumber")
    ]
    """
    Car registration number (or `null` if the car registration number should not be
    updated).
    """

    classifications: Annotated[Optional[AccountUpdateCustomerClassifications], PropertyInfo(alias="Classifications")]
    """Classifications of the customer."""

    company_id: Annotated[Optional[AccountUpdateCustomerCompanyID], PropertyInfo(alias="CompanyId")]
    """
    Unique identifier of the company (or `null` if the company should not be
    updated).
    """

    dietary_requirements: Annotated[
        Optional[AccountUpdateCustomerDietaryRequirements], PropertyInfo(alias="DietaryRequirements")
    ]
    """
    Dietary requirements (or `null` if the dietary requirements should not be
    updated).
    """

    email: Annotated[Optional[AccountUpdateCustomerEmail], PropertyInfo(alias="Email")]
    """Email address (or `null` if the email should not be updated)."""

    first_name: Annotated[Optional[AccountUpdateCustomerFirstName], PropertyInfo(alias="FirstName")]
    """First name (or `null` if the first name should not be updated)."""

    last_name: Annotated[Optional[AccountUpdateCustomerLastName], PropertyInfo(alias="LastName")]
    """Last name (or `null` if the last name should not be updated)."""

    legal_entity_identifiers: Annotated[
        Optional[AccountUpdateCustomerLegalEntityIdentifiers], PropertyInfo(alias="LegalEntityIdentifiers")
    ]
    """Legal entity identifiers of the customer."""

    loyalty_code: Annotated[Optional[AccountUpdateCustomerLoyaltyCode], PropertyInfo(alias="LoyaltyCode")]
    """Loyalty code (or `null` if the loyalty code should not be updated)."""

    nationality_code: Annotated[Optional[AccountUpdateCustomerNationalityCode], PropertyInfo(alias="NationalityCode")]
    """Nationality code (or `null` if the nationality code should not be updated)."""

    notes: Annotated[Optional[AccountUpdateCustomerNotes], PropertyInfo(alias="Notes")]
    """Notes (or `null` if the notes should not be updated)."""

    occupation: Annotated[Optional[AccountUpdateCustomerOccupation], PropertyInfo(alias="Occupation")]
    """Occupation (or `null` if the occupation should not be updated)."""

    options: Annotated[Optional[AccountUpdateCustomerOptions], PropertyInfo(alias="Options")]
    """Options of the customer."""

    preferred_language_code: Annotated[
        Optional[AccountUpdateCustomerPreferredLanguageCode], PropertyInfo(alias="PreferredLanguageCode")
    ]
    """
    Preferred language code (or `null` if the preferred language code should not be
    updated).
    """

    second_last_name: Annotated[Optional[AccountUpdateCustomerSecondLastName], PropertyInfo(alias="SecondLastName")]
    """Second last name (or `null` if the second last name should not be updated)."""

    sex: Annotated[Optional[AccountUpdateCustomerSex], PropertyInfo(alias="Sex")]
    """Sex (or `null` if the sex should not be updated)."""

    tax_identifier: Annotated[Optional[AccountUpdateCustomerTaxIdentifier], PropertyInfo(alias="TaxIdentifier")]
    """
    Tax identification number (or `null` if the tax identification number should not
    be updated).
    """

    telephone: Annotated[Optional[AccountUpdateCustomerTelephone], PropertyInfo(alias="Telephone")]
    """Telephone number (or `null` if the telephone should not be updated)."""

    title: Annotated[Optional[AccountUpdateCustomerTitle], PropertyInfo(alias="Title")]
    """Title (or `null` if the title should not be updated)."""


class AccountUpdate(TypedDict, total=False):
    discriminator: Required[Annotated[Literal["Customer", "Company"], PropertyInfo(alias="Discriminator")]]
    """Customer

    Company
    """

    id: Required[Annotated[str, PropertyInfo(alias="Id")]]
    """Unique identifier of the account."""

    company: Annotated[Optional[AccountUpdateCompany], PropertyInfo(alias="Company")]
    """Company data to be updated. Required when `Discriminator` is `Company`."""

    customer: Annotated[Optional[AccountUpdateCustomer], PropertyInfo(alias="Customer")]
    """Customer data to be updated. Required when `Discriminator` is `Customer`."""
