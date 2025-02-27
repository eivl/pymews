# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["AccountNoteListParams", "Limitation", "UpdatedUtc"]


class AccountNoteListParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    limitation: Required[Annotated[Limitation, PropertyInfo(alias="Limitation")]]
    """Limitation on the quantity of data returned."""

    account_ids: Annotated[Optional[List[str]], PropertyInfo(alias="AccountIds")]
    """
    Unique identifiers of the accounts
    ([Customer](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer)
    or
    [Company](https://mews-systems.gitbook.io/connector-api/operations/companies/#company)).
    """

    account_note_ids: Annotated[Optional[List[str]], PropertyInfo(alias="AccountNoteIds")]
    """
    Unique identifiers of
    [Account note](https://mews-systems.gitbook.io/connector-api/operations/#account-note).
    """

    activity_states: Annotated[Optional[List[Literal["Deleted", "Active"]]], PropertyInfo(alias="ActivityStates")]
    """Whether to return only active, only deleted or both records."""

    chain_ids: Annotated[Optional[List[str]], PropertyInfo(alias="ChainIds")]
    """Unique identifiers of `Chain`.

    If not specified, the operation returns data for all chains within scope of the
    Access Token.
    """

    updated_utc: Annotated[Optional[UpdatedUtc], PropertyInfo(alias="UpdatedUtc")]
    """Interval of Account note's last update date and time."""


class Limitation(TypedDict, total=False):
    count: Required[Annotated[int, PropertyInfo(alias="Count")]]

    cursor: Annotated[Optional[str], PropertyInfo(alias="Cursor")]


class UpdatedUtc(TypedDict, total=False):
    end_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="EndUtc", format="iso8601")]

    start_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="StartUtc", format="iso8601")]
