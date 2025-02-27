# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["CustomerListParams", "Extent", "Limitation", "CreatedUtc", "DeletedUtc", "UpdatedUtc"]


class CustomerListParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    extent: Required[Annotated[Extent, PropertyInfo(alias="Extent")]]

    limitation: Required[Annotated[Limitation, PropertyInfo(alias="Limitation")]]
    """Limitation on the quantity of data returned."""

    activity_states: Annotated[Optional[List[Literal["Deleted", "Active"]]], PropertyInfo(alias="ActivityStates")]
    """Whether to return only active, only deleted or both records."""

    chain_ids: Annotated[Optional[List[str]], PropertyInfo(alias="ChainIds")]
    """Unique identifiers of the chains.

    Required when using Portfolio Access Tokens, ignored otherwise.
    """

    company_ids: Annotated[Optional[List[str]], PropertyInfo(alias="CompanyIds")]
    """Unique identifier of the Company the customer is associated with."""

    created_utc: Annotated[Optional[CreatedUtc], PropertyInfo(alias="CreatedUtc")]
    """Interval in which Customer was created."""

    customer_ids: Annotated[Optional[List[str]], PropertyInfo(alias="CustomerIds")]
    """Unique identifiers of Customers. Required if no other filter is provided."""

    deleted_utc: Annotated[Optional[DeletedUtc], PropertyInfo(alias="DeletedUtc")]
    """Interval in which Customer was deleted.

    `ActivityStates` value `Deleted` should be provided with this filter to get
    expected results.
    """

    emails: Annotated[Optional[List[str]], PropertyInfo(alias="Emails")]
    """
    Emails of the
    [Customers](https://mews-systems.gitbook.io/connector-api/operations/#customer).
    """

    first_names: Annotated[Optional[List[str]], PropertyInfo(alias="FirstNames")]
    """
    First names of the
    [Customers](https://mews-systems.gitbook.io/connector-api/operations/#customer).
    """

    last_names: Annotated[Optional[List[str]], PropertyInfo(alias="LastNames")]
    """
    Last names of the
    [Customers](https://mews-systems.gitbook.io/connector-api/operations/#customer).
    """

    loyalty_codes: Annotated[Optional[List[str]], PropertyInfo(alias="LoyaltyCodes")]
    """
    Loyalty codes of the
    [Customers](https://mews-systems.gitbook.io/connector-api/operations/#customer).
    """

    updated_utc: Annotated[Optional[UpdatedUtc], PropertyInfo(alias="UpdatedUtc")]
    """Interval in which Customer was updated."""


class Extent(TypedDict, total=False):
    addresses: Annotated[Optional[bool], PropertyInfo(alias="Addresses")]
    """Whether the response should contain addresses of customers."""

    customers: Annotated[Optional[bool], PropertyInfo(alias="Customers")]
    """Whether the response should contain information about customers."""

    documents: Annotated[Optional[bool], PropertyInfo(alias="Documents")]
    """Whether the response should contain identity documents of customers."""


class Limitation(TypedDict, total=False):
    count: Required[Annotated[int, PropertyInfo(alias="Count")]]

    cursor: Annotated[Optional[str], PropertyInfo(alias="Cursor")]


class CreatedUtc(TypedDict, total=False):
    end_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="EndUtc", format="iso8601")]

    start_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="StartUtc", format="iso8601")]


class DeletedUtc(TypedDict, total=False):
    end_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="EndUtc", format="iso8601")]

    start_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="StartUtc", format="iso8601")]


class UpdatedUtc(TypedDict, total=False):
    end_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="EndUtc", format="iso8601")]

    start_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="StartUtc", format="iso8601")]
