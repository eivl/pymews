# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = [
    "VoucherListResponse",
    "Company",
    "CompanyCreditRating",
    "CompanyOptions",
    "CompanyAddress",
    "Rate",
    "VoucherAssignment",
    "VoucherCode",
    "Voucher",
]


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


class Rate(BaseModel):
    group_id: str = FieldInfo(alias="GroupId")
    """Unique identifier of `Rate Group` where the rate belongs."""

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the rate."""

    is_active: bool = FieldInfo(alias="IsActive")
    """Whether the rate is still active."""

    is_base_rate: bool = FieldInfo(alias="IsBaseRate")
    """Whether the rate is a base rate."""

    is_enabled: bool = FieldInfo(alias="IsEnabled")
    """Whether the rate is currently available to customers."""

    is_public: bool = FieldInfo(alias="IsPublic")
    """Whether the rate is publicly available."""

    names: Dict[str, str] = FieldInfo(alias="Names")
    """All translations of the name."""

    service_id: str = FieldInfo(alias="ServiceId")
    """Unique identifier of the `Service`."""

    type: Literal["Public", "Private", "AvailabilityBlock"] = FieldInfo(alias="Type")
    """Public

    Private

    AvailabilityBlock
    """

    updated_utc: datetime = FieldInfo(alias="UpdatedUtc")
    """Interval in which the rates were updated."""

    base_rate_id: Optional[str] = FieldInfo(alias="BaseRateId", default=None)
    """Unique identifier of the base `Rate`."""

    business_segment_id: Optional[str] = FieldInfo(alias="BusinessSegmentId", default=None)
    """Unique identifier of the `Business Segment`."""

    description: Optional[Dict[str, str]] = FieldInfo(alias="Description", default=None)
    """All translations of the description of the rate."""

    external_identifier: Optional[str] = FieldInfo(alias="ExternalIdentifier", default=None)
    """Identifier of the rate from external system."""

    external_names: Optional[Dict[str, str]] = FieldInfo(alias="ExternalNames", default=None)
    """All translations of the external name of the rate."""

    name: Optional[str] = FieldInfo(alias="Name", default=None)
    """Name of the rate (in the default language)."""

    short_name: Optional[str] = FieldInfo(alias="ShortName", default=None)
    """Short name of the rate (in the default language)."""


class VoucherAssignment(BaseModel):
    rate_id: Optional[str] = FieldInfo(alias="RateId", default=None)
    """
    Unique identifier of
    [Rate](https://mews-systems.gitbook.io/connector-api/operations/rates/#rate) the
    voucher is assigned with.
    """

    voucher_id: Optional[str] = FieldInfo(alias="VoucherId", default=None)
    """
    Unique identifier of
    [Voucher](https://mews-systems.gitbook.io/connector-api/operations/#voucher).
    """


class VoucherCode(BaseModel):
    activity_state: Optional[str] = FieldInfo(alias="ActivityState", default=None)
    """Whether voucher code is active or deleted."""

    created_utc: Optional[str] = FieldInfo(alias="CreatedUtc", default=None)
    """Creation date and time of the voucher in UTC timezone in ISO 8601 format."""

    id: Optional[str] = FieldInfo(alias="Id", default=None)
    """Unique identifier of the voucher code."""

    is_active: Optional[bool] = FieldInfo(alias="IsActive", default=None)
    """Whether the voucher code is still active."""

    updated_utc: Optional[str] = FieldInfo(alias="UpdatedUtc", default=None)
    """Last update date and time of the voucher in UTC timezone in ISO 8601 format."""

    validity_end_utc: Optional[str] = FieldInfo(alias="ValidityEndUtc", default=None)
    """If specified, marks the end of interval in which the code can be used."""

    validity_start_utc: Optional[str] = FieldInfo(alias="ValidityStartUtc", default=None)
    """If specified, marks the beginning of interval in which the code can be used."""

    value: Optional[str] = FieldInfo(alias="Value", default=None)
    """Value of voucher code used by customers."""

    voucher_id: Optional[str] = FieldInfo(alias="VoucherId", default=None)
    """
    Unique identifier of
    [Voucher](https://mews-systems.gitbook.io/connector-api/operations/#voucher) the
    code belongs to.
    """


class Voucher(BaseModel):
    created_utc: datetime = FieldInfo(alias="CreatedUtc")
    """Creation date and time of the voucher in UTC timezone in ISO 8601 format."""

    id: str = FieldInfo(alias="Id")
    """Unique identifier of voucher."""

    is_active: bool = FieldInfo(alias="IsActive")
    """Whether the voucher is still active."""

    name: str = FieldInfo(alias="Name")
    """Internal name of the voucher."""

    service_id: str = FieldInfo(alias="ServiceId")
    """
    Unique identifier of
    [Service](https://mews-systems.gitbook.io/connector-api/operations/services/#service)
    the voucher belongs to.
    """

    type: Literal["Public", "PartnerCompany", "TravelAgency"] = FieldInfo(alias="Type")
    """Public

    PartnerCompany

    TravelAgency
    """

    updated_utc: datetime = FieldInfo(alias="UpdatedUtc")
    """Last update date and time of the voucher in UTC timezone in ISO 8601 format."""

    activity_state: Optional[Literal["Deleted", "Active"]] = FieldInfo(alias="ActivityState", default=None)
    """Whether voucher is active or deleted."""

    company_id: Optional[str] = FieldInfo(alias="CompanyId", default=None)
    """
    Unique identifier of
    [Company](https://mews-systems.gitbook.io/connector-api/operations/companies/#company)
    the voucher is related to.
    """

    external_identifier: Optional[str] = FieldInfo(alias="ExternalIdentifier", default=None)
    """Identifier of the voucher from external system."""

    occupiable_interval_end_utc: Optional[datetime] = FieldInfo(alias="OccupiableIntervalEndUtc", default=None)
    """
    End of the time interval, expressed as the timestamp for the start of the last
    time unit, in UTC timezone ISO 8601 format (or null if the end time should not
    be updated).
    """

    occupiable_interval_start_utc: Optional[datetime] = FieldInfo(alias="OccupiableIntervalStartUtc", default=None)
    """
    Start of the time interval, expressed as the timestamp for the start of the
    first time unit, in UTC timezone ISO 8601 format (or null if the start time
    should not be updated).
    """

    travel_agency_id: Optional[str] = FieldInfo(alias="TravelAgencyId", default=None)
    """
    Unique identifier of
    [Company](https://mews-systems.gitbook.io/connector-api/operations/companies/#company)
    with
    [Travel agency contract](https://mews-systems.gitbook.io/connector-api/operations/companycontracts/#travel-agency-contract)
    the voucher is related to.
    """


class VoucherListResponse(BaseModel):
    companies: Optional[List[Company]] = FieldInfo(alias="Companies", default=None)
    """The related companies and travel agencies."""

    cursor: Optional[str] = FieldInfo(alias="Cursor", default=None)
    """
    Unique identifier of the item one newer in time order than the items to be
    returned. If Cursor is not specified, i.e. null, then the latest or most recent
    items will be returned.
    """

    rates: Optional[List[Rate]] = FieldInfo(alias="Rates", default=None)
    """The assigned rates."""

    voucher_assignments: Optional[List[VoucherAssignment]] = FieldInfo(alias="VoucherAssignments", default=None)
    """
    The assignments between vouchers and
    [Rates](https://mews-systems.gitbook.io/connector-api/operations/rates/#rate).
    """

    voucher_codes: Optional[List[VoucherCode]] = FieldInfo(alias="VoucherCodes", default=None)
    """Information about voucher codes used by customers."""

    vouchers: Optional[List[Voucher]] = FieldInfo(alias="Vouchers", default=None)
    """Details about vouchers added to the system."""
