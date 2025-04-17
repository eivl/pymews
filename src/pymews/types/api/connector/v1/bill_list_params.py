# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["BillListParams", "Limitation", "ClosedUtc", "CreatedUtc", "DueUtc", "Extent", "PaidUtc", "UpdatedUtc"]


class BillListParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    limitation: Required[Annotated[Limitation, PropertyInfo(alias="Limitation")]]
    """Limitation on the quantity of data returned."""

    bill_ids: Annotated[Optional[List[str]], PropertyInfo(alias="BillIds")]
    """Unique identifiers of the `Bills`. Required if no other filter is provided."""

    closed_utc: Annotated[Optional[ClosedUtc], PropertyInfo(alias="ClosedUtc")]
    """Interval in which the `Bill` was closed."""

    correction_state: Annotated[
        Optional[List[Literal["Bill", "CorrectiveBill"]]], PropertyInfo(alias="CorrectionState")
    ]
    """Whether to return regular bills, corrective bills, or both.

    If `BillIds` are specified, defaults to both, otherwise defaults to `Bill`.
    """

    created_utc: Annotated[Optional[CreatedUtc], PropertyInfo(alias="CreatedUtc")]
    """Interval in which the `Bill` was created."""

    customer_ids: Annotated[Optional[List[str]], PropertyInfo(alias="CustomerIds")]
    """Unique identifiers of the `Customers`."""

    due_utc: Annotated[Optional[DueUtc], PropertyInfo(alias="DueUtc")]
    """Interval in which the `Bill` is due to be paid."""

    enterprise_ids: Annotated[Optional[List[str]], PropertyInfo(alias="EnterpriseIds")]
    """Unique identifiers of the Enterprises.

    If not specified, the operation returns data for all enterprises within scope of
    the Access Token.
    """

    extent: Annotated[Optional[Extent], PropertyInfo(alias="Extent")]
    """Extent of data to be returned.

    E.g. it is possible to specify that together with the bills, payments and
    revenue items should be also returned. **Deprecated!**
    """

    paid_utc: Annotated[Optional[PaidUtc], PropertyInfo(alias="PaidUtc")]
    """Interval in which the `Bill` was paid."""

    state: Annotated[Optional[Literal["Open", "Closed"]], PropertyInfo(alias="State")]
    """Whether the bill is `Open` or `Closed`."""

    updated_utc: Annotated[Optional[UpdatedUtc], PropertyInfo(alias="UpdatedUtc")]
    """Interval in which the `Bill` was updated."""


class Limitation(TypedDict, total=False):
    count: Required[Annotated[int, PropertyInfo(alias="Count")]]

    cursor: Annotated[Optional[str], PropertyInfo(alias="Cursor")]


class ClosedUtc(TypedDict, total=False):
    end_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="EndUtc", format="iso8601")]

    start_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="StartUtc", format="iso8601")]


class CreatedUtc(TypedDict, total=False):
    end_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="EndUtc", format="iso8601")]

    start_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="StartUtc", format="iso8601")]


class DueUtc(TypedDict, total=False):
    end_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="EndUtc", format="iso8601")]

    start_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="StartUtc", format="iso8601")]


class Extent(TypedDict, total=False):
    items: Annotated[bool, PropertyInfo(alias="Items")]
    """Whether the response should contain payments and revenue items."""


class PaidUtc(TypedDict, total=False):
    end_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="EndUtc", format="iso8601")]

    start_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="StartUtc", format="iso8601")]


class UpdatedUtc(TypedDict, total=False):
    end_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="EndUtc", format="iso8601")]

    start_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="StartUtc", format="iso8601")]
