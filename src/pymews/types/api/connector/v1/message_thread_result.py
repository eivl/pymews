# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["MessageThreadResult", "MessageThread"]


class MessageThread(BaseModel):
    created_utc: datetime = FieldInfo(alias="CreatedUtc")
    """
    Creation date and time of the message thread in UTC timezone in ISO 8601 format.
    """

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the message thread."""

    original_sender: str = FieldInfo(alias="OriginalSender")
    """The sender of the original message in the thread."""

    subject: str = FieldInfo(alias="Subject")
    """Subject of the message thread."""

    updated_utc: datetime = FieldInfo(alias="UpdatedUtc")
    """
    Last update date and time of the message thread in UTC timezone in ISO 8601
    format.
    """

    is_resolved: Optional[bool] = FieldInfo(alias="IsResolved", default=None)


class MessageThreadResult(BaseModel):
    message_threads: List[MessageThread] = FieldInfo(alias="MessageThreads")
    """The filtered message threads."""

    cursor: Optional[str] = FieldInfo(alias="Cursor", default=None)
    """Unique identifier of the last and hence oldest message thread returned.

    This can be used in
    [Limitation](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/#limitation)
    in a subsequent request to fetch the next batch of older message threads.
    """
