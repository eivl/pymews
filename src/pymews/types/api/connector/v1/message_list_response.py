# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["MessageListResponse", "Message"]


class Message(BaseModel):
    created_utc: datetime = FieldInfo(alias="CreatedUtc")
    """Creation date and time of the message in UTC timezone in ISO 8601 format."""

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the message."""

    message_thread_id: str = FieldInfo(alias="MessageThreadId")
    """
    Unique identifier of the
    [Message thread](https://mews-systems.gitbook.io/connector-api/operations/messagethreads/#message-thread)
    which the message belongs to.
    """

    sender: Literal["Application", "Enterprise"] = FieldInfo(alias="Sender")

    text: str = FieldInfo(alias="Text")
    """Text of the message."""


class MessageListResponse(BaseModel):
    messages: List[Message] = FieldInfo(alias="Messages")
    """The filtered messages."""

    cursor: Optional[str] = FieldInfo(alias="Cursor", default=None)
    """Unique identifier of the last and hence oldest message returned.

    This can be used in
    [Limitation](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/#limitation)
    in a subsequent request to fetch the next batch of older messages.
    """
