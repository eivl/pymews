# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["ResourceBlockAddParams", "ResourceBlock"]


class ResourceBlockAddParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    resource_blocks: Required[Annotated[Iterable[ResourceBlock], PropertyInfo(alias="ResourceBlocks")]]
    """Resource block parameters."""


class ResourceBlock(TypedDict, total=False):
    end_utc: Required[Annotated[Union[str, datetime], PropertyInfo(alias="EndUtc", format="iso8601")]]

    name: Required[Annotated[str, PropertyInfo(alias="Name")]]

    resource_id: Required[Annotated[str, PropertyInfo(alias="ResourceId")]]

    start_utc: Required[Annotated[Union[str, datetime], PropertyInfo(alias="StartUtc", format="iso8601")]]

    type: Required[Annotated[Literal["OutOfOrder", "InternalUse"], PropertyInfo(alias="Type")]]

    notes: Annotated[Optional[str], PropertyInfo(alias="Notes")]
