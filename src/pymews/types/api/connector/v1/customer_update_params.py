# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = [
    "CustomerUpdateParams",
    "Address",
    "DriversLicense",
    "IdentityCard",
    "ItalianDestinationCode",
    "ItalianFiscalCode",
    "Passport",
    "Visa",
]


class CustomerUpdateParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    customer_id: Required[Annotated[str, PropertyInfo(alias="CustomerId")]]
    """Unique identifier of the `Customer` to be updated."""

    address: Annotated[Optional[Address], PropertyInfo(alias="Address")]
    """New address details."""

    birth_date: Annotated[Union[str, date, None], PropertyInfo(alias="BirthDate", format="iso8601")]
    """New birth date in ISO 8601 format."""

    birth_place: Annotated[Optional[str], PropertyInfo(alias="BirthPlace")]
    """New birth place."""

    car_registration_number: Annotated[Optional[str], PropertyInfo(alias="CarRegistrationNumber")]
    """New registration number of the customer's car."""

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
    """New classifications of the customer."""

    company_id: Annotated[Optional[str], PropertyInfo(alias="CompanyId")]
    """Unique identifier of `Company` the customer is associated with."""

    dietary_requirements: Annotated[Optional[str], PropertyInfo(alias="DietaryRequirements")]
    """Customer's dietary requirements, e.g. Vegan, Halal."""

    drivers_license: Annotated[Optional[DriversLicense], PropertyInfo(alias="DriversLicense")]

    email: Annotated[Optional[str], PropertyInfo(alias="Email")]
    """New email address."""

    first_name: Annotated[Optional[str], PropertyInfo(alias="FirstName")]
    """New first name."""

    identity_card: Annotated[Optional[IdentityCard], PropertyInfo(alias="IdentityCard")]

    italian_destination_code: Annotated[Optional[ItalianDestinationCode], PropertyInfo(alias="ItalianDestinationCode")]
    """New Italian destination code of customer."""

    italian_fiscal_code: Annotated[Optional[ItalianFiscalCode], PropertyInfo(alias="ItalianFiscalCode")]
    """New Italian fiscal code of customer."""

    last_name: Annotated[Optional[str], PropertyInfo(alias="LastName")]
    """New last name."""

    loyalty_code: Annotated[Optional[str], PropertyInfo(alias="LoyaltyCode")]
    """Loyalty code of the customer."""

    nationality_code: Annotated[Optional[str], PropertyInfo(alias="NationalityCode")]
    """New nationality code as ISO 3166-1 code of the `Country`."""

    notes: Annotated[Optional[str], PropertyInfo(alias="Notes")]
    """Internal notes about the customer. Old value will be overwritten."""

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
    """New phone number."""

    second_last_name: Annotated[Optional[str], PropertyInfo(alias="SecondLastName")]
    """New second last name."""

    sex: Annotated[Optional[Literal["Male", "Female"]], PropertyInfo(alias="Sex")]
    """Sex of the customer."""

    tax_identification_number: Annotated[Optional[str], PropertyInfo(alias="TaxIdentificationNumber")]
    """New tax identification number of the customer."""

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


class ItalianDestinationCode(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class ItalianFiscalCode(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


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
