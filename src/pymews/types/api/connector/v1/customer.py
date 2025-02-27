# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["Customer", "Address", "DriversLicense", "IdentityCard", "Passport", "Visa"]


class Address(BaseModel):
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


class DriversLicense(BaseModel):
    customer_id: Optional[str] = FieldInfo(alias="CustomerId", default=None)
    """Identifier of the `Customer`."""

    expiration: Optional[date] = FieldInfo(alias="Expiration", default=None)
    """Expiration date in ISO 8601 format."""

    id: Optional[str] = FieldInfo(alias="Id", default=None)
    """Unique identifier of the document."""

    identity_document_support_number: Optional[str] = FieldInfo(alias="IdentityDocumentSupportNumber", default=None)
    """Identity document support number.

    Only required for Spanish identity cards in Spanish hotels.
    """

    issuance: Optional[date] = FieldInfo(alias="Issuance", default=None)
    """Date of issuance in ISO 8601 format."""

    issuing_city: Optional[str] = FieldInfo(alias="IssuingCity", default=None)
    """City where the document was issued."""

    issuing_country_code: Optional[str] = FieldInfo(alias="IssuingCountryCode", default=None)
    """ISO 3166-1 code of the `Country`."""

    number: Optional[str] = FieldInfo(alias="Number", default=None)
    """Number of the document (e.g. passport number)."""

    type: Optional[Literal["IdentityCard", "Passport", "Visa", "DriversLicense"]] = FieldInfo(
        alias="Type", default=None
    )
    """IdentityCard

    Passport

    Visa

    DriversLicense
    """


class IdentityCard(BaseModel):
    customer_id: Optional[str] = FieldInfo(alias="CustomerId", default=None)
    """Identifier of the `Customer`."""

    expiration: Optional[date] = FieldInfo(alias="Expiration", default=None)
    """Expiration date in ISO 8601 format."""

    id: Optional[str] = FieldInfo(alias="Id", default=None)
    """Unique identifier of the document."""

    identity_document_support_number: Optional[str] = FieldInfo(alias="IdentityDocumentSupportNumber", default=None)
    """Identity document support number.

    Only required for Spanish identity cards in Spanish hotels.
    """

    issuance: Optional[date] = FieldInfo(alias="Issuance", default=None)
    """Date of issuance in ISO 8601 format."""

    issuing_city: Optional[str] = FieldInfo(alias="IssuingCity", default=None)
    """City where the document was issued."""

    issuing_country_code: Optional[str] = FieldInfo(alias="IssuingCountryCode", default=None)
    """ISO 3166-1 code of the `Country`."""

    number: Optional[str] = FieldInfo(alias="Number", default=None)
    """Number of the document (e.g. passport number)."""

    type: Optional[Literal["IdentityCard", "Passport", "Visa", "DriversLicense"]] = FieldInfo(
        alias="Type", default=None
    )
    """IdentityCard

    Passport

    Visa

    DriversLicense
    """


class Passport(BaseModel):
    customer_id: Optional[str] = FieldInfo(alias="CustomerId", default=None)
    """Identifier of the `Customer`."""

    expiration: Optional[date] = FieldInfo(alias="Expiration", default=None)
    """Expiration date in ISO 8601 format."""

    id: Optional[str] = FieldInfo(alias="Id", default=None)
    """Unique identifier of the document."""

    identity_document_support_number: Optional[str] = FieldInfo(alias="IdentityDocumentSupportNumber", default=None)
    """Identity document support number.

    Only required for Spanish identity cards in Spanish hotels.
    """

    issuance: Optional[date] = FieldInfo(alias="Issuance", default=None)
    """Date of issuance in ISO 8601 format."""

    issuing_city: Optional[str] = FieldInfo(alias="IssuingCity", default=None)
    """City where the document was issued."""

    issuing_country_code: Optional[str] = FieldInfo(alias="IssuingCountryCode", default=None)
    """ISO 3166-1 code of the `Country`."""

    number: Optional[str] = FieldInfo(alias="Number", default=None)
    """Number of the document (e.g. passport number)."""

    type: Optional[Literal["IdentityCard", "Passport", "Visa", "DriversLicense"]] = FieldInfo(
        alias="Type", default=None
    )
    """IdentityCard

    Passport

    Visa

    DriversLicense
    """


class Visa(BaseModel):
    customer_id: Optional[str] = FieldInfo(alias="CustomerId", default=None)
    """Identifier of the `Customer`."""

    expiration: Optional[date] = FieldInfo(alias="Expiration", default=None)
    """Expiration date in ISO 8601 format."""

    id: Optional[str] = FieldInfo(alias="Id", default=None)
    """Unique identifier of the document."""

    identity_document_support_number: Optional[str] = FieldInfo(alias="IdentityDocumentSupportNumber", default=None)
    """Identity document support number.

    Only required for Spanish identity cards in Spanish hotels.
    """

    issuance: Optional[date] = FieldInfo(alias="Issuance", default=None)
    """Date of issuance in ISO 8601 format."""

    issuing_city: Optional[str] = FieldInfo(alias="IssuingCity", default=None)
    """City where the document was issued."""

    issuing_country_code: Optional[str] = FieldInfo(alias="IssuingCountryCode", default=None)
    """ISO 3166-1 code of the `Country`."""

    number: Optional[str] = FieldInfo(alias="Number", default=None)
    """Number of the document (e.g. passport number)."""

    type: Optional[Literal["IdentityCard", "Passport", "Visa", "DriversLicense"]] = FieldInfo(
        alias="Type", default=None
    )
    """IdentityCard

    Passport

    Visa

    DriversLicense
    """


class Customer(BaseModel):
    chain_id: str = FieldInfo(alias="ChainId")
    """Unique identifier of the chain."""

    classifications: List[
        Literal[
            "None",
            "PaymasterAccount",
            "Blacklist",
            "Media",
            "LoyaltyProgram",
            "PreviousComplaint",
            "Returning",
            "Staff",
            "FriendOrFamily",
            "TopManagement",
            "Important",
            "VeryImportant",
            "Problematic",
            "Cashlist",
            "DisabledPerson",
            "Military",
            "Airline",
            "HealthCompliant",
            "InRoom",
            "WaitingForRoom",
            "Student",
        ]
    ] = FieldInfo(alias="Classifications")
    """Classifications of the customer."""

    created_utc: datetime = FieldInfo(alias="CreatedUtc")
    """Creation date and time of the customer in UTC timezone in ISO 8601 format."""

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the customer."""

    is_active: bool = FieldInfo(alias="IsActive")
    """Whether the customer record is still active."""

    last_name: str = FieldInfo(alias="LastName")
    """Last name of the customer."""

    number: str = FieldInfo(alias="Number")
    """Number of the customer."""

    options: List[
        Literal[
            "None",
            "SendMarketingEmails",
            "Invoiceable",
            "BillAddressObjection",
            "SendMarketingPostalMail",
            "SendPartnerMarketingEmails",
            "SendPartnerMarketingPostalMail",
            "WithdrawCardConsent",
        ]
    ] = FieldInfo(alias="Options")
    """Options of the customer."""

    preferred_space_features: List[
        Literal[
            "SeaView",
            "RiverView",
            "OceanView",
            "TwinBeds",
            "DoubleBed",
            "RollawayBed",
            "UpperBed",
            "LowerBed",
            "Balcony",
            "AccessibleBathroom",
            "AccessibleRoom",
            "ElevatorAccess",
            "HighFloor",
            "Kitchenette",
            "AirConditioning",
            "PrivateJacuzzi",
            "PrivateSauna",
            "EnsuiteRoom",
            "PrivateBathroom",
            "SharedBathroom",
        ]
    ] = FieldInfo(alias="PreferredSpaceFeatures")
    """A list of room preferences, such as view type, bed type, and amenities."""

    updated_utc: datetime = FieldInfo(alias="UpdatedUtc")
    """Last update date and time of the customer in UTC timezone in ISO 8601 format."""

    accounting_code: Optional[str] = FieldInfo(alias="AccountingCode", default=None)
    """Accounting code of the customer."""

    activity_state: Optional[str] = FieldInfo(alias="ActivityState", default=None)
    """
    [Activity State](https://mews-systems.gitbook.io/connector-api/operations/#activity-state)
    of customer record, i.e. whether active or deleted.
    """

    address: Optional[Address] = FieldInfo(alias="Address", default=None)

    address_id: Optional[str] = FieldInfo(alias="AddressId", default=None)
    """Unique identifier of the `Address` of the customer."""

    billing_code: Optional[str] = FieldInfo(alias="BillingCode", default=None)
    """Billing code of the customer."""

    birth_date: Optional[str] = FieldInfo(alias="BirthDate", default=None)
    """Date of birth in ISO 8601 format."""

    birth_place: Optional[str] = FieldInfo(alias="BirthPlace", default=None)
    """Place of birth."""

    car_registration_number: Optional[str] = FieldInfo(alias="CarRegistrationNumber", default=None)
    """Registration number of the customer's car."""

    company_id: Optional[str] = FieldInfo(alias="CompanyId", default=None)
    """
    Unique identifier of
    [Company](https://mews-systems.gitbook.io/connector-api/operations/companies/#company)
    the customer is associated with.
    """

    dietary_requirements: Optional[str] = FieldInfo(alias="DietaryRequirements", default=None)
    """Customer's dietary requirements, e.g. Vegan, Halal."""

    drivers_license: Optional[DriversLicense] = FieldInfo(alias="DriversLicense", default=None)

    email: Optional[str] = FieldInfo(alias="Email", default=None)
    """Email address of the customer."""

    first_name: Optional[str] = FieldInfo(alias="FirstName", default=None)
    """First name of the customer."""

    has_ota_email: Optional[bool] = FieldInfo(alias="HasOtaEmail", default=None)
    """Whether the customer's email address is a temporary email address from an OTA.

    For more details, see the
    [product documentation](https://help.mews.com/s/article/how-to-maintain-ota-guest-profiles-with-verified-email-addresses-obtained-from-the-guest-portal).
    """

    identity_card: Optional[IdentityCard] = FieldInfo(alias="IdentityCard", default=None)

    italian_destination_code: Optional[str] = FieldInfo(alias="ItalianDestinationCode", default=None)
    """Value of Italian destination code."""

    italian_fiscal_code: Optional[str] = FieldInfo(alias="ItalianFiscalCode", default=None)
    """Value of Italian fiscal code."""

    language_code: Optional[str] = FieldInfo(alias="LanguageCode", default=None)
    """Language and culture code of the customer's language, based on multiple sources.

    These sources include the preferred language specified in internal data based on
    previous bookings, and the preferred language of the customer specified in their
    profile. If neither of these sources are present, we use the native language
    based on the customer's nationality. The format is, for example, `en-US` or
    `fr-FR`.
    """

    loyalty_code: Optional[str] = FieldInfo(alias="LoyaltyCode", default=None)
    """Loyalty code of the customer."""

    merge_target_id: Optional[str] = FieldInfo(alias="MergeTargetId", default=None)
    """
    Unique identifier of the account
    ([Customer](https://mews-systems.gitbook.io/connector-api/operations/#customer))
    to which this customer is linked.
    """

    nationality_code: Optional[str] = FieldInfo(alias="NationalityCode", default=None)
    """
    ISO 3166-1 code of the
    [Country](https://mews-systems.gitbook.io/connector-api/operations/countries/#country).
    """

    notes: Optional[str] = FieldInfo(alias="Notes", default=None)
    """Internal notes about the customer."""

    occupation: Optional[str] = FieldInfo(alias="Occupation", default=None)
    """Occupation of the customer."""

    passport: Optional[Passport] = FieldInfo(alias="Passport", default=None)

    phone: Optional[str] = FieldInfo(alias="Phone", default=None)
    """Phone number of the customer (possibly mobile)."""

    preferred_language_code: Optional[str] = FieldInfo(alias="PreferredLanguageCode", default=None)
    """
    Language and culture code of the customer's preferred language, according to
    their profile. For example: `en-GB`, `fr-CA`.
    """

    second_last_name: Optional[str] = FieldInfo(alias="SecondLastName", default=None)
    """Second last name of the customer."""

    sex: Optional[Literal["Male", "Female"]] = FieldInfo(alias="Sex", default=None)
    """Male

    Female
    """

    tax_identification_number: Optional[str] = FieldInfo(alias="TaxIdentificationNumber", default=None)
    """Tax identification number of the customer."""

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

    visa: Optional[Visa] = FieldInfo(alias="Visa", default=None)
