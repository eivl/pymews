# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = [
    "ResourceAccessTokenAddParams",
    "ResourceAccessTokenParameter",
    "ResourceAccessTokenParameterPermissions",
    "ResourceAccessTokenParameterPermissionsBed",
    "ResourceAccessTokenParameterPermissionsBuilding",
    "ResourceAccessTokenParameterPermissionsFloor",
    "ResourceAccessTokenParameterPermissionsRoom",
]


class ResourceAccessTokenAddParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    resource_access_token_parameters: Required[
        Annotated[Iterable[ResourceAccessTokenParameter], PropertyInfo(alias="ResourceAccessTokenParameters")]
    ]
    """
    Parameters of
    [Resource access token](https://mews-systems.gitbook.io/connector-api/operations/#resource-access-token).
    """


class ResourceAccessTokenParameterPermissionsBed(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class ResourceAccessTokenParameterPermissionsBuilding(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class ResourceAccessTokenParameterPermissionsFloor(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class ResourceAccessTokenParameterPermissionsRoom(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class ResourceAccessTokenParameterPermissions(TypedDict, total=False):
    bed: Annotated[Optional[ResourceAccessTokenParameterPermissionsBed], PropertyInfo(alias="Bed")]

    building: Annotated[Optional[ResourceAccessTokenParameterPermissionsBuilding], PropertyInfo(alias="Building")]

    floor: Annotated[Optional[ResourceAccessTokenParameterPermissionsFloor], PropertyInfo(alias="Floor")]

    room: Annotated[Optional[ResourceAccessTokenParameterPermissionsRoom], PropertyInfo(alias="Room")]


class ResourceAccessTokenParameter(TypedDict, total=False):
    companionship_id: Annotated[Optional[str], PropertyInfo(alias="CompanionshipId")]

    permissions: Annotated[Optional[ResourceAccessTokenParameterPermissions], PropertyInfo(alias="Permissions")]

    resource_id: Annotated[Optional[str], PropertyInfo(alias="ResourceId")]

    serial_number: Annotated[Optional[str], PropertyInfo(alias="SerialNumber")]

    service_order_id: Annotated[str, PropertyInfo(alias="ServiceOrderId")]

    type: Annotated[Optional[str], PropertyInfo(alias="Type")]

    validity_end_utc: Annotated[Optional[str], PropertyInfo(alias="ValidityEndUtc")]

    validity_start_utc: Annotated[Optional[str], PropertyInfo(alias="ValidityStartUtc")]

    value: Annotated[Optional[str], PropertyInfo(alias="Value")]
