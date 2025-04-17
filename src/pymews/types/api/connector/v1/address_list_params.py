# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["AddressListParams", "Limitation", "UpdatedUtc"]


class AddressListParams(TypedDict, total=False):
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
    Unique identifiers of
    [Companies](https://mews-systems.gitbook.io/connector-api/operations/companies/#company)
    or
    [Customers](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer)
    within the enterprise. Required if no other filter is provided.
    """

    activity_states: Annotated[Optional[List[Literal["Deleted", "Active"]]], PropertyInfo(alias="ActivityStates")]
    """Whether to return only active, only deleted or both records."""

    address_ids: Annotated[Optional[List[str]], PropertyInfo(alias="AddressIds")]
    """
    Unique identifiers of
    [Addresses](https://mews-systems.gitbook.io/connector-api/operations/#account-address)
    within the enterprise. Use this property if you want to fetch specific
    addresses. Required if no other filter is provided.
    """

    chain_ids: Annotated[Optional[List[str]], PropertyInfo(alias="ChainIds")]
    """Unique identifiers of `Chain`.

    If not specified, the operation returns data for all chains within scope of the
    Access Token.
    """

    updated_utc: Annotated[Optional[UpdatedUtc], PropertyInfo(alias="UpdatedUtc")]
    """Interval of Address last update date and time.

    Required if no other filter is provided.
    """


class Limitation(TypedDict, total=False):
    count: Required[Annotated[int, PropertyInfo(alias="Count")]]

    cursor: Annotated[Optional[str], PropertyInfo(alias="Cursor")]


class UpdatedUtc(TypedDict, total=False):
    end_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="EndUtc", format="iso8601")]

    start_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="StartUtc", format="iso8601")]
