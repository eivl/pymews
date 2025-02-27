# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["ServiceOrderNoteAddResponse", "ServiceOrderNote"]


class ServiceOrderNote(BaseModel):
    created_utc: Optional[datetime] = FieldInfo(alias="CreatedUtc", default=None)
    """
    Creation date and time of the service order note in UTC timezone in ISO 8601
    format.
    """

    id: Optional[str] = FieldInfo(alias="Id", default=None)
    """Unique identifier of the service order note."""

    order_id: Optional[str] = FieldInfo(alias="OrderId", default=None)
    """
    Unique identifier of the `Service order` to which the Service Order Note
    belongs.
    """

    text: Optional[str] = FieldInfo(alias="Text", default=None)
    """Content of the service order note."""

    type: Optional[Literal["General", "ChannelManager", "SpecialRequest"]] = FieldInfo(alias="Type", default=None)
    """General

    ChannelManager

    SpecialRequest
    """

    updated_utc: Optional[datetime] = FieldInfo(alias="UpdatedUtc", default=None)
    """
    Last update date and time of the service order note in UTC timezone in ISO 8601
    format.
    """


class ServiceOrderNoteAddResponse(BaseModel):
    service_order_notes: List[ServiceOrderNote] = FieldInfo(alias="ServiceOrderNotes")
    """Added service order notes."""
