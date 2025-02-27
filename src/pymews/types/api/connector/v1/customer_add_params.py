# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["CustomerAddParams", "Address", "DriversLicense", "IdentityCard", "Passport", "Visa"]


class CustomerAddParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    last_name: Required[Annotated[str, PropertyInfo(alias="LastName")]]
    """Last name of the customer."""

    overwrite_existing: Required[Annotated[bool, PropertyInfo(alias="OverwriteExisting")]]
    """Whether an existing customer should be overwritten in case of duplicity.

    This applies only to basic personal information (`Title`, `FirstName`,
    `LastName`, ...).
    """

    address: Annotated[Optional[Address], PropertyInfo(alias="Address")]
    """New address details."""

    birth_date: Annotated[Union[str, date, None], PropertyInfo(alias="BirthDate", format="iso8601")]
    """Date of birth in ISO 8601 format."""

    birth_place: Annotated[Optional[str], PropertyInfo(alias="BirthPlace")]
    """Place of birth."""

    car_registration_number: Annotated[Optional[str], PropertyInfo(alias="CarRegistrationNumber")]
    """Registration number of the customer's car."""

    chain_id: Annotated[Optional[str], PropertyInfo(alias="ChainId")]
    """Unique identifier of the chain.

    Required when using `PortfolioAccessTokens`, ignored otherwise.
    """

    classifications: Annotated[
        Optional[
            List[
                Literal[
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
            ]
        ],
        PropertyInfo(alias="Classifications"),
    ]
    """Classifications of the customer."""

    company_id: Annotated[Optional[str], PropertyInfo(alias="CompanyId")]
    """Unique identifier of `Company` the customer is associated with."""

    dietary_requirements: Annotated[Optional[str], PropertyInfo(alias="DietaryRequirements")]
    """Customer's dietary requirements, e.g. Vegan, Halal."""

    drivers_license: Annotated[Optional[DriversLicense], PropertyInfo(alias="DriversLicense")]

    email: Annotated[Optional[str], PropertyInfo(alias="Email")]
    """Email address of the customer."""

    first_name: Annotated[Optional[str], PropertyInfo(alias="FirstName")]
    """First name of the customer."""

    identity_card: Annotated[Optional[IdentityCard], PropertyInfo(alias="IdentityCard")]

    italian_destination_code: Annotated[Optional[str], PropertyInfo(alias="ItalianDestinationCode")]
    """Value of Italian destination code."""

    italian_fiscal_code: Annotated[Optional[str], PropertyInfo(alias="ItalianFiscalCode")]
    """Value of Italian fiscal code."""

    loyalty_code: Annotated[Optional[str], PropertyInfo(alias="LoyaltyCode")]
    """Loyalty code of the customer."""

    nationality_code: Annotated[Optional[str], PropertyInfo(alias="NationalityCode")]
    """ISO 3166-1 code of the `Country`."""

    notes: Annotated[Optional[str], PropertyInfo(alias="Notes")]
    """Internal notes about the customer."""

    occupation: Annotated[Optional[str], PropertyInfo(alias="Occupation")]
    """Occupation of the customer."""

    options: Annotated[
        Optional[
            List[
                Literal[
                    "SendMarketingEmails",
                    "Invoiceable",
                    "BillAddressObjection",
                    "SendMarketingPostalMail",
                    "SendPartnerMarketingEmails",
                    "SendPartnerMarketingPostalMail",
                    "WithdrawCardConsent",
                ]
            ]
        ],
        PropertyInfo(alias="Options"),
    ]
    """Options of the customer."""

    passport: Annotated[Optional[Passport], PropertyInfo(alias="Passport")]

    phone: Annotated[Optional[str], PropertyInfo(alias="Phone")]
    """Phone number of the customer (possibly mobile)."""

    second_last_name: Annotated[Optional[str], PropertyInfo(alias="SecondLastName")]
    """Second last name of the customer."""

    sex: Annotated[Optional[Literal["Male", "Female"]], PropertyInfo(alias="Sex")]
    """Sex of the customer."""

    tax_identification_number: Annotated[Optional[str], PropertyInfo(alias="TaxIdentificationNumber")]
    """Tax identification number of the customer."""

    title: Annotated[Optional[Literal["Mister", "Miss", "Misses"]], PropertyInfo(alias="Title")]
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

    visa: Annotated[Optional[Visa], PropertyInfo(alias="Visa")]


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


class DriversLicense(TypedDict, total=False):
    expiration: Annotated[Union[str, date, None], PropertyInfo(alias="Expiration", format="iso8601")]
    """Expiration date in ISO 8601 format."""

    issuance: Annotated[Union[str, date, None], PropertyInfo(alias="Issuance", format="iso8601")]
    """Date of issuance in ISO 8601 format."""

    issuing_city: Annotated[Optional[str], PropertyInfo(alias="IssuingCity")]
    """City from which document issued"""

    issuing_country_code: Annotated[Optional[str], PropertyInfo(alias="IssuingCountryCode")]
    """ISO 3166-1 code of the `Country`."""

    number: Annotated[Optional[str], PropertyInfo(alias="Number")]
    """Number of the document (e.g. passport number)."""


class IdentityCard(TypedDict, total=False):
    expiration: Annotated[Union[str, date, None], PropertyInfo(alias="Expiration", format="iso8601")]
    """Expiration date in ISO 8601 format."""

    issuance: Annotated[Union[str, date, None], PropertyInfo(alias="Issuance", format="iso8601")]
    """Date of issuance in ISO 8601 format."""

    issuing_city: Annotated[Optional[str], PropertyInfo(alias="IssuingCity")]
    """City from which document issued"""

    issuing_country_code: Annotated[Optional[str], PropertyInfo(alias="IssuingCountryCode")]
    """ISO 3166-1 code of the `Country`."""

    number: Annotated[Optional[str], PropertyInfo(alias="Number")]
    """Number of the document (e.g. passport number)."""


class Passport(TypedDict, total=False):
    expiration: Annotated[Union[str, date, None], PropertyInfo(alias="Expiration", format="iso8601")]
    """Expiration date in ISO 8601 format."""

    issuance: Annotated[Union[str, date, None], PropertyInfo(alias="Issuance", format="iso8601")]
    """Date of issuance in ISO 8601 format."""

    issuing_city: Annotated[Optional[str], PropertyInfo(alias="IssuingCity")]
    """City from which document issued"""

    issuing_country_code: Annotated[Optional[str], PropertyInfo(alias="IssuingCountryCode")]
    """ISO 3166-1 code of the `Country`."""

    number: Annotated[Optional[str], PropertyInfo(alias="Number")]
    """Number of the document (e.g. passport number)."""


class Visa(TypedDict, total=False):
    expiration: Annotated[Union[str, date, None], PropertyInfo(alias="Expiration", format="iso8601")]
    """Expiration date in ISO 8601 format."""

    issuance: Annotated[Union[str, date, None], PropertyInfo(alias="Issuance", format="iso8601")]
    """Date of issuance in ISO 8601 format."""

    issuing_city: Annotated[Optional[str], PropertyInfo(alias="IssuingCity")]
    """City from which document issued"""

    issuing_country_code: Annotated[Optional[str], PropertyInfo(alias="IssuingCountryCode")]
    """ISO 3166-1 code of the `Country`."""

    number: Annotated[Optional[str], PropertyInfo(alias="Number")]
    """Number of the document (e.g. passport number)."""
