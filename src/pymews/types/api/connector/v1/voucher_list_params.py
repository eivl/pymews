# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["VoucherListParams", "Extent", "Limitation", "UpdatedUtc"]


class VoucherListParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    extent: Required[Annotated[Extent, PropertyInfo(alias="Extent")]]
    """Extent of data to be returned.

    Whether only specific voucher info should be returned or related items as well.
    """

    limitation: Required[Annotated[Limitation, PropertyInfo(alias="Limitation")]]
    """Limitation on the quantity of data returned."""

    service_ids: Required[Annotated[List[str], PropertyInfo(alias="ServiceIds")]]
    """
    Unique identifiers of
    [Services](https://mews-systems.gitbook.io/connector-api/operations/services/#service)
    where the vouchers belong to.
    """

    activity_states: Annotated[Optional[List[Literal["Deleted", "Active"]]], PropertyInfo(alias="ActivityStates")]
    """Whether to return only active, only deleted, or both types of record.

    If not specified, both active and deleted records will be returned.
    """

    company_ids: Annotated[Optional[List[str]], PropertyInfo(alias="CompanyIds")]
    """Unique identifiers of the companies."""

    enterprise_ids: Annotated[Optional[List[str]], PropertyInfo(alias="EnterpriseIds")]
    """Unique identifiers of the Enterprises.

    If not specified, the operation returns data for all enterprises within scope of
    the Access Token.
    """

    external_identifiers: Annotated[Optional[List[str]], PropertyInfo(alias="ExternalIdentifiers")]
    """
    Identifiers of
    [Voucher](https://mews-systems.gitbook.io/connector-api/operations/#voucher)
    from external systems.
    """

    updated_utc: Annotated[Optional[UpdatedUtc], PropertyInfo(alias="UpdatedUtc")]

    voucher_code_values: Annotated[Optional[List[str]], PropertyInfo(alias="VoucherCodeValues")]
    """Value of voucher codes used by customers."""

    voucher_ids: Annotated[Optional[List[str]], PropertyInfo(alias="VoucherIds")]
    """Unique identifiers of vouchers."""


class Extent(TypedDict, total=False):
    companies: Annotated[Optional[bool], PropertyInfo(alias="Companies")]
    """Whether the response should contain detail of related companies."""

    rates: Annotated[Optional[bool], PropertyInfo(alias="Rates")]
    """Whether the response should contain detail of assigned rates."""

    voucher_assignments: Annotated[Optional[bool], PropertyInfo(alias="VoucherAssignments")]
    """Whether the response should contain assignments between vouchers and Rates."""

    voucher_codes: Annotated[Optional[bool], PropertyInfo(alias="VoucherCodes")]
    """Whether the response should contain voucher codes used by customers."""

    vouchers: Annotated[Optional[bool], PropertyInfo(alias="Vouchers")]
    """Whether the response should contain main information about vouchers."""


class Limitation(TypedDict, total=False):
    count: Required[Annotated[int, PropertyInfo(alias="Count")]]

    cursor: Annotated[Optional[str], PropertyInfo(alias="Cursor")]


class UpdatedUtc(TypedDict, total=False):
    end_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="EndUtc", format="iso8601")]

    start_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="StartUtc", format="iso8601")]
