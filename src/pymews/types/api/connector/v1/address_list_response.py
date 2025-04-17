# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["AddressListResponse", "Address"]


class Address(BaseModel):
    account_id: Optional[str] = FieldInfo(alias="AccountId", default=None)
    """
    Unique identifier of a
    [Company](https://mews-systems.gitbook.io/connector-api/operations/companies/#company)
    or a
    [Customer](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer)
    within the enterprise.
    """

    account_type: Optional[Literal["Company", "Customer"]] = FieldInfo(alias="AccountType", default=None)
    """
    A discriminator specifying the
    [type of account](https://mews-systems.gitbook.io/connector-api/operations/accounts/#account-type),
    e.g. customer or company.
    """

    chain_id: Optional[str] = FieldInfo(alias="ChainId", default=None)
    """Unique identifier of the chain."""

    city: Optional[str] = FieldInfo(alias="City", default=None)
    """The city."""

    country_code: Optional[str] = FieldInfo(alias="CountryCode", default=None)
    """ISO 3166-1 alpha-2 code of the Country."""

    country_subdivision_code: Optional[str] = FieldInfo(alias="CountrySubdivisionCode", default=None)
    """ISO 3166-2 code of the administrative division, e.g. DE-BW."""

    id: Optional[str] = FieldInfo(alias="Id", default=None)
    """Unique identifier of the address."""

    is_active: Optional[bool] = FieldInfo(alias="IsActive", default=None)
    """Whether the address is still active."""

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

    updated_utc: Optional[datetime] = FieldInfo(alias="UpdatedUtc", default=None)
    """Last update date and time of the address in UTC timezone in ISO 8601 format."""


class AddressListResponse(BaseModel):
    addresses: List[Address] = FieldInfo(alias="Addresses")
    """
    The collection of Account addresses, containing address and account information.
    """

    cursor: Optional[str] = FieldInfo(alias="Cursor", default=None)
    """Unique identifier of the last and hence oldest address item returned.

    This can be used in Limitation in a subsequent request to fetch the next batch
    of older Account address.
    """
