# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["V1ListCountriesResponse", "Country", "CountryGroup", "CountryRule", "CountrySubdivision"]


class Country(BaseModel):
    code: str = FieldInfo(alias="Code")
    """ISO 3166-1 alpha-2 code, e.g. `CZ` or `SK`."""

    english_name: str = FieldInfo(alias="EnglishName")
    """English name of the country."""

    sovereign_country_code: str = FieldInfo(alias="SovereignCountryCode")
    """ISO 3166-1 alpha-2 code of the sovereign country.

    May differ from `Code` for dependent territories.
    """


class CountryGroup(BaseModel):
    code: str = FieldInfo(alias="Code")
    """Group code, e.g. `EU`, `SCHENGEN`, `NORDIC`..."""

    country_codes: List[str] = FieldInfo(alias="CountryCodes")
    """Codes of countries included in the group, in ISO 3166-1 alpha-2 format."""

    english_name: str = FieldInfo(alias="EnglishName")
    """English name of the country group."""


class CountryRule(BaseModel):
    country_code: str = FieldInfo(alias="CountryCode")
    """ISO 3166-1 alpha-2 code, e.g. US or GB."""

    driver_licence_expiration_date_not_required: bool = FieldInfo(alias="DriverLicenceExpirationDateNotRequired")
    """Whether the country requires expiration date for driver's license."""

    identity_card_expiration_date_not_required: bool = FieldInfo(alias="IdentityCardExpirationDateNotRequired")
    """Whether the country requires expiration date for identity card."""


class CountrySubdivision(BaseModel):
    code: str = FieldInfo(alias="Code")
    """ISO 3166-2 code of the administrative division, e.g AU-QLD."""

    country_code: str = FieldInfo(alias="CountryCode")
    """
    ISO 3166-1 code of the
    [Country](https://mews-systems.gitbook.io/connector-api/operations/countries#country).
    """

    english_name: str = FieldInfo(alias="EnglishName")
    """English name of the country subdivision."""


class V1ListCountriesResponse(BaseModel):
    countries: List[Country] = FieldInfo(alias="Countries")
    """The supported countries."""

    country_groups: List[CountryGroup] = FieldInfo(alias="CountryGroups")
    """The supported country groups."""

    country_rules: List[CountryRule] = FieldInfo(alias="CountryRules")
    """Country-specific rules"""

    country_subdivisions: List[CountrySubdivision] = FieldInfo(alias="CountrySubdivisions")
    """The supported country subdivisions."""
