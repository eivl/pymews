# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["MessageAddResponse", "Message", "MessageMessage"]


class MessageMessage(BaseModel):
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


class Message(BaseModel):
    identifier: Optional[str] = FieldInfo(alias="Identifier", default=None)

    message: Optional[MessageMessage] = FieldInfo(alias="Message", default=None)


class MessageAddResponse(BaseModel):
    messages: List[Message] = FieldInfo(alias="Messages")
