# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["V1ListReservationGroupsResponse", "ReservationGroup"]


class ReservationGroup(BaseModel):
    enterprise_id: str = FieldInfo(alias="EnterpriseId")
    """
    Unique identifier of the
    [Enterprise](https://mews-systems.gitbook.io/connector-api/operations/enterprises/#enterprise)
    the reservation group belongs to.
    """

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the reservation group."""

    name: str = FieldInfo(alias="Name")
    """Name of the reservation group, might be empty or same for multiple groups."""

    channel_manager: Optional[str] = FieldInfo(alias="ChannelManager", default=None)
    """Name of the corresponding channel manager."""

    channel_manager_group_number: Optional[str] = FieldInfo(alias="ChannelManagerGroupNumber", default=None)
    """Identifier of the channel manager."""


class V1ListReservationGroupsResponse(BaseModel):
    reservation_groups: List[ReservationGroup] = FieldInfo(alias="ReservationGroups")
    """The filtered reservation groups."""

    cursor: Optional[str] = FieldInfo(alias="Cursor", default=None)
    """Unique identifier of the last and hence oldest reservation group returned.

    This can be used in
    [Limitation](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/#limitation)
    in a subsequent request to fetch the next batch of older reservation groups.
    """
