# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["ResourceAccessTokenResult", "ResourceAccessToken", "ResourceAccessTokenPermissions"]


class ResourceAccessTokenPermissions(BaseModel):
    bed: Optional[bool] = FieldInfo(alias="Bed", default=None)

    building: Optional[bool] = FieldInfo(alias="Building", default=None)

    floor: Optional[bool] = FieldInfo(alias="Floor", default=None)

    room: Optional[bool] = FieldInfo(alias="Room", default=None)


class ResourceAccessToken(BaseModel):
    created_utc: datetime = FieldInfo(alias="CreatedUtc")
    """
    Creation date and time of the resource access token in UTC timezone in ISO 8601
    format.
    """

    enterprise_id: str = FieldInfo(alias="EnterpriseId")
    """
    Unique identifier of the
    [Enterprise](https://mews-systems.gitbook.io/connector-api/operations/enterprises/#enterprise).
    """

    id: str = FieldInfo(alias="Id")
    """
    Unique identifier of
    [Resource access token](https://mews-systems.gitbook.io/connector-api/operations/#resource-access-token).
    """

    is_active: bool = FieldInfo(alias="IsActive")
    """Whether the resource access token is still active."""

    service_order_id: str = FieldInfo(alias="ServiceOrderId")
    """Unique identifier of a reservation."""

    type: Literal["PinCode", "RfidTag"] = FieldInfo(alias="Type")

    updated_utc: datetime = FieldInfo(alias="UpdatedUtc")
    """
    Last update date and time of the resource access token in UTC timezone in ISO
    8601 format.
    """

    validity_end_utc: datetime = FieldInfo(alias="ValidityEndUtc")
    """Marks the end of interval in which the resource access token can be used."""

    validity_start_utc: datetime = FieldInfo(alias="ValidityStartUtc")
    """Marks the start of interval in which the resource access token can be used."""

    companionship_id: Optional[str] = FieldInfo(alias="CompanionshipId", default=None)
    """
    Unique identifier of
    [Companionship](https://mews-systems.gitbook.io/connector-api/operations/companionships/#companionship).
    """

    permissions: Optional[ResourceAccessTokenPermissions] = FieldInfo(alias="Permissions", default=None)
    """
    Specify permissions of
    [Resource access token](https://mews-systems.gitbook.io/connector-api/operations/#resource-access-token).
    """

    resource_id: Optional[str] = FieldInfo(alias="ResourceId", default=None)
    """
    Unique identifier of
    [Resource](https://mews-systems.gitbook.io/connector-api/operations/resources/#resource).
    """

    serial_number: Optional[str] = FieldInfo(alias="SerialNumber", default=None)
    """
    Serial number of
    [Resource access token type](https://mews-systems.gitbook.io/connector-api/operations/#resource-access-token-type).
    """

    value: Optional[str] = FieldInfo(alias="Value", default=None)
    """Value of resource access token"""


class ResourceAccessTokenResult(BaseModel):
    cursor: Optional[str] = FieldInfo(alias="Cursor", default=None)
    """Unique identifier of the last and hence oldest item returned.

    This can be used in
    [Limitation](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/#limitation)
    in a subsequent request to fetch the next batch of older tokens. If
    [Limitation](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/#limitation)
    is specified in the request message, then Cursor will always be included in the
    response message.
    """

    resource_access_tokens: Optional[List[ResourceAccessToken]] = FieldInfo(alias="ResourceAccessTokens", default=None)
    """Resource access tokens."""
