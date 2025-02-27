# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["V1ListEnterprisesResponse", "Enterprise", "EnterpriseAddress", "EnterpriseSubscription"]


class EnterpriseAddress(BaseModel):
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


class EnterpriseSubscription(BaseModel):
    tax_identifier: Optional[str] = FieldInfo(alias="TaxIdentifier", default=None)
    """Tax identifier of the `Enterprise`."""


class Enterprise(BaseModel):
    accommodation_environment_code: str = FieldInfo(alias="AccommodationEnvironmentCode")
    """Unique code of the accommodation environment where the enterprise resides."""

    accounting_editable_history_interval: str = FieldInfo(alias="AccountingEditableHistoryInterval")
    """Editable history interval for accounting data in ISO 8601 duration format."""

    accounting_environment_code: str = FieldInfo(alias="AccountingEnvironmentCode")
    """Unique code of the accounting environment where the enterprise resides."""

    address: EnterpriseAddress = FieldInfo(alias="Address")

    address_id: str = FieldInfo(alias="AddressId")
    """Unique identifier of the `Address` of the enterprise."""

    chain_id: str = FieldInfo(alias="ChainId")
    """Unique identifier of the chain to which the enterprise belongs."""

    created_utc: datetime = FieldInfo(alias="CreatedUtc")
    """Creation date and time of the enterprise in UTC timezone in ISO 8601 format."""

    default_language_code: str = FieldInfo(alias="DefaultLanguageCode")
    """Language-culture codes of the enterprise default `Language`."""

    editable_history_interval: str = FieldInfo(alias="EditableHistoryInterval")

    group_names: List[str] = FieldInfo(alias="GroupNames")
    """A list of the group names of the enterprise."""

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the enterprise."""

    legal_environment_code: str = FieldInfo(alias="LegalEnvironmentCode")
    """Unique identifier of the legal environment where the enterprise resides."""

    linked_utc: datetime = FieldInfo(alias="LinkedUtc")
    """
    Date and time when enterprise was added to the portfolio in UTC timezone in ISO
    8601 format.
    """

    name: str = FieldInfo(alias="Name")
    """Name of the enterprise."""

    operational_editable_history_interval: str = FieldInfo(alias="OperationalEditableHistoryInterval")
    """Editable history interval for operational data in ISO 8601 duration format."""

    pricing: Literal["Gross", "Net"] = FieldInfo(alias="Pricing")
    """Gross (The enterprise shows amount with gross prices.)

    Net (The enterprise shows amount with net prices.)

    - `Gross` - The enterprise shows amount with gross prices.
    - `Net` - The enterprise shows amount with net prices.
    """

    subscription: EnterpriseSubscription = FieldInfo(alias="Subscription")

    tax_environment_code: str = FieldInfo(alias="TaxEnvironmentCode")
    """Unique code of the tax environment where the enterprise resides."""

    time_zone_identifier: str = FieldInfo(alias="TimeZoneIdentifier")
    """IANA timezone identifier of the enterprise."""

    updated_utc: datetime = FieldInfo(alias="UpdatedUtc")
    """Creation date and time of the enterprise in UTC timezone in ISO 8601 format."""

    cover_image_id: Optional[str] = FieldInfo(alias="CoverImageId", default=None)
    """Unique identifier of the `Image` of the enterprise cover."""

    email: Optional[str] = FieldInfo(alias="Email", default=None)
    """Email address of the enterprise."""

    external_identifier: Optional[str] = FieldInfo(alias="ExternalIdentifier", default=None)
    """Identifier of the enterprise from external system."""

    logo_image_id: Optional[str] = FieldInfo(alias="LogoImageId", default=None)
    """Unique identifier of the `Image` of the enterprise logo."""

    phone: Optional[str] = FieldInfo(alias="Phone", default=None)
    """Phone number of the enterprise."""

    tax_precision: Optional[int] = FieldInfo(alias="TaxPrecision", default=None)
    """Tax precision used for financial calculations in the enterprise.

    If `null`, `Currency` precision is used.
    """

    website_url: Optional[str] = FieldInfo(alias="WebsiteUrl", default=None)
    """URL of the enterprise website."""


class V1ListEnterprisesResponse(BaseModel):
    enterprises: List[Enterprise] = FieldInfo(alias="Enterprises")
    """The filtered enterprises."""

    cursor: Optional[str] = FieldInfo(alias="Cursor", default=None)
    """Unique identifier of the last and hence oldest enterprise returned.

    This can be used in
    [Limitation](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/#limitation)
    in a subsequent request to fetch the next batch of older enterprises.
    """
