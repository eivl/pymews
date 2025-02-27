# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["CompanyListParams", "CreatedUtc", "Limitation", "UpdatedUtc"]


class CompanyListParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    activity_states: Annotated[Optional[List[Literal["Deleted", "Active"]]], PropertyInfo(alias="ActivityStates")]
    """Whether to return only active, only deleted, or both types of record.

    If not specified, both active and deleted records will be returned.
    """

    chain_ids: Annotated[Optional[List[str]], PropertyInfo(alias="ChainIds")]
    """Unique identifiers of the chain.

    If not specified, the operation returns data for all chains within scope of the
    Access Token.
    """

    created_utc: Annotated[Optional[CreatedUtc], PropertyInfo(alias="CreatedUtc")]

    end_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="EndUtc", format="iso8601")]

    external_identifiers: Annotated[Optional[List[str]], PropertyInfo(alias="ExternalIdentifiers")]
    """
    Identifiers of
    [Company](https://mews-systems.gitbook.io/connector-api/operations/#company)
    from external system.
    """

    ids: Annotated[Optional[List[str]], PropertyInfo(alias="Ids")]
    """
    Unique identifiers of
    [Companies](https://mews-systems.gitbook.io/connector-api/operations/#company).
    """

    limitation: Annotated[Optional[Limitation], PropertyInfo(alias="Limitation")]
    """Limitation on the quantity of data returned."""

    mother_company_ids: Annotated[Optional[List[str]], PropertyInfo(alias="MotherCompanyIds")]
    """Unique identifiers of mother `Company`."""

    names: Annotated[Optional[List[str]], PropertyInfo(alias="Names")]
    """
    Names of
    [Companies](https://mews-systems.gitbook.io/connector-api/operations/#company).
    """

    start_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="StartUtc", format="iso8601")]

    time_filter: Annotated[Optional[Literal["Created", "Updated"]], PropertyInfo(alias="TimeFilter")]

    updated_utc: Annotated[Optional[UpdatedUtc], PropertyInfo(alias="UpdatedUtc")]


class CreatedUtc(TypedDict, total=False):
    end_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="EndUtc", format="iso8601")]

    start_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="StartUtc", format="iso8601")]


class Limitation(TypedDict, total=False):
    count: Required[Annotated[int, PropertyInfo(alias="Count")]]

    cursor: Annotated[Optional[str], PropertyInfo(alias="Cursor")]


class UpdatedUtc(TypedDict, total=False):
    end_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="EndUtc", format="iso8601")]

    start_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="StartUtc", format="iso8601")]
