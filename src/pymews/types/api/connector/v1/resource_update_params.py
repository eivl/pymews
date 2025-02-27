# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ....._utils import PropertyInfo

__all__ = [
    "ResourceUpdateParams",
    "ResourceUpdate",
    "ResourceUpdateData",
    "ResourceUpdateDataValue",
    "ResourceUpdateDataValueSpaceData",
    "ResourceUpdateName",
    "ResourceUpdateParentResourceID",
    "ResourceUpdateState",
    "ResourceUpdateStateReason",
]


class ResourceUpdateParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    resource_updates: Required[Annotated[Iterable[ResourceUpdate], PropertyInfo(alias="ResourceUpdates")]]
    """Resource updates."""


class ResourceUpdateDataValueSpaceData(TypedDict, total=False):
    floor_number: Required[Annotated[str, PropertyInfo(alias="FloorNumber")]]

    location_notes: Annotated[Optional[str], PropertyInfo(alias="LocationNotes")]


ResourceUpdateDataValue: TypeAlias = Union[ResourceUpdateDataValueSpaceData, object, object]


class ResourceUpdateData(TypedDict, total=False):
    discriminator: Literal["Space", "Object", "Person"]

    value: ResourceUpdateDataValue


class ResourceUpdateName(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class ResourceUpdateParentResourceID(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class ResourceUpdateState(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class ResourceUpdateStateReason(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class ResourceUpdate(TypedDict, total=False):
    resource_id: Required[Annotated[str, PropertyInfo(alias="ResourceId")]]

    data: Annotated[ResourceUpdateData, PropertyInfo(alias="Data")]

    name: Annotated[Optional[ResourceUpdateName], PropertyInfo(alias="Name")]

    parent_resource_id: Annotated[Optional[ResourceUpdateParentResourceID], PropertyInfo(alias="ParentResourceId")]

    state: Annotated[Optional[ResourceUpdateState], PropertyInfo(alias="State")]

    state_reason: Annotated[Optional[ResourceUpdateStateReason], PropertyInfo(alias="StateReason")]
