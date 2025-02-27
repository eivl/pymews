# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = [
    "ResourceAccessTokenUpdateParams",
    "ResourceAccessTokenUpdate",
    "ResourceAccessTokenUpdatePermissions",
    "ResourceAccessTokenUpdatePermissionsBed",
    "ResourceAccessTokenUpdatePermissionsBuilding",
    "ResourceAccessTokenUpdatePermissionsFloor",
    "ResourceAccessTokenUpdatePermissionsRoom",
    "ResourceAccessTokenUpdateValidityEndUtc",
    "ResourceAccessTokenUpdateValidityStartUtc",
    "ResourceAccessTokenUpdateValue",
]


class ResourceAccessTokenUpdateParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    enterprise_id: Annotated[Optional[str], PropertyInfo(alias="EnterpriseId")]
    """Unique identifier of the enterprise.

    Required when using
    [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
    ignored otherwise.
    """

    resource_access_token_updates: Annotated[
        Optional[Iterable[ResourceAccessTokenUpdate]], PropertyInfo(alias="ResourceAccessTokenUpdates")
    ]
    """
    Parameters of
    [Resource access token](https://mews-systems.gitbook.io/connector-api/operations/#resource-access-token).
    """


class ResourceAccessTokenUpdatePermissionsBed(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class ResourceAccessTokenUpdatePermissionsBuilding(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class ResourceAccessTokenUpdatePermissionsFloor(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class ResourceAccessTokenUpdatePermissionsRoom(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class ResourceAccessTokenUpdatePermissions(TypedDict, total=False):
    bed: Annotated[Optional[ResourceAccessTokenUpdatePermissionsBed], PropertyInfo(alias="Bed")]

    building: Annotated[Optional[ResourceAccessTokenUpdatePermissionsBuilding], PropertyInfo(alias="Building")]

    floor: Annotated[Optional[ResourceAccessTokenUpdatePermissionsFloor], PropertyInfo(alias="Floor")]

    room: Annotated[Optional[ResourceAccessTokenUpdatePermissionsRoom], PropertyInfo(alias="Room")]


class ResourceAccessTokenUpdateValidityEndUtc(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class ResourceAccessTokenUpdateValidityStartUtc(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class ResourceAccessTokenUpdateValue(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class ResourceAccessTokenUpdate(TypedDict, total=False):
    permissions: Annotated[Optional[ResourceAccessTokenUpdatePermissions], PropertyInfo(alias="Permissions")]

    resource_access_token_id: Annotated[str, PropertyInfo(alias="ResourceAccessTokenId")]

    validity_end_utc: Annotated[Optional[ResourceAccessTokenUpdateValidityEndUtc], PropertyInfo(alias="ValidityEndUtc")]

    validity_start_utc: Annotated[
        Optional[ResourceAccessTokenUpdateValidityStartUtc], PropertyInfo(alias="ValidityStartUtc")
    ]

    value: Annotated[Optional[ResourceAccessTokenUpdateValue], PropertyInfo(alias="Value")]
    """Value of resource access token (or null if the value should not be updated)."""
