# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["PaymentRequestListParams", "Limitation", "UpdatedUtc"]


class PaymentRequestListParams(TypedDict, total=False):
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
    [Customer](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer)
    accounts to which payment requests were issued.
    """

    enterprise_ids: Annotated[Optional[List[str]], PropertyInfo(alias="EnterpriseIds")]
    """Unique identifiers of the Enterprises.

    If not specified, the operation returns data for all enterprises within scope of
    the Access Token.
    """

    payment_request_ids: Annotated[Optional[List[str]], PropertyInfo(alias="PaymentRequestIds")]
    """
    Unique identifiers of the requested
    [Payment requests](https://mews-systems.gitbook.io/connector-api/operations/#payment-request).
    """

    reservation_ids: Annotated[Optional[List[str]], PropertyInfo(alias="ReservationIds")]

    states: Annotated[
        Optional[List[Literal["Pending", "Completed", "Canceled", "Expired"]]], PropertyInfo(alias="States")
    ]
    """A list of payment request states to filter by."""

    updated_utc: Annotated[Optional[UpdatedUtc], PropertyInfo(alias="UpdatedUtc")]


class Limitation(TypedDict, total=False):
    count: Required[Annotated[int, PropertyInfo(alias="Count")]]

    cursor: Annotated[Optional[str], PropertyInfo(alias="Cursor")]


class UpdatedUtc(TypedDict, total=False):
    end_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="EndUtc", format="iso8601")]

    start_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="StartUtc", format="iso8601")]
