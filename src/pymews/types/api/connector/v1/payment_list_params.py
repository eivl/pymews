# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["PaymentListParams", "Limitation", "ChargedUtc", "ClosedUtc", "CreatedUtc", "SettlementUtc", "UpdatedUtc"]


class PaymentListParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    limitation: Required[Annotated[Limitation, PropertyInfo(alias="Limitation")]]
    """Limitation on the quantity of data returned."""

    account_ids: Annotated[Optional[List[str]], PropertyInfo(alias="AccountIds")]
    """Unique identifiers of specific `Accounts` to which payments are belongs to.

    Required if no other filter is provided.
    """

    accounting_states: Annotated[
        Optional[List[Literal["Open", "Closed", "Inactive", "Canceled"]]], PropertyInfo(alias="AccountingStates")
    ]
    """Accounting state of the item."""

    bill_ids: Annotated[Optional[List[str]], PropertyInfo(alias="BillIds")]
    """Unique identifiers of specific `Bill` items to which payments are assigned.

    Required if no other filter is provided.
    """

    charged_utc: Annotated[Optional[ChargedUtc], PropertyInfo(alias="ChargedUtc")]
    """Time interval during which the `Payment` was charged.

    Required if no other filter is provided.
    """

    closed_utc: Annotated[Optional[ClosedUtc], PropertyInfo(alias="ClosedUtc")]
    """Time interval during which the `Payment` was closed.

    Required if no other filter is provided.
    """

    created_utc: Annotated[Optional[CreatedUtc], PropertyInfo(alias="CreatedUtc")]
    """Time interval during which the `Payment` was created.

    Required if no other filter is provided.
    """

    currency: Annotated[Optional[str], PropertyInfo(alias="Currency")]
    """ISO-4217 code of the `Currency` the item costs should be converted to."""

    enterprise_ids: Annotated[Optional[List[str]], PropertyInfo(alias="EnterpriseIds")]
    """Unique identifiers of the Enterprises.

    If not specified, the operation returns data for all enterprises within scope of
    the Access Token.
    """

    payment_ids: Annotated[Optional[List[str]], PropertyInfo(alias="PaymentIds")]
    """Unique identifiers of specific `Payment` items.

    Required if no other filter is provided.
    """

    reservation_ids: Annotated[Optional[List[str]], PropertyInfo(alias="ReservationIds")]
    """Unique identifiers of specific `Reservations` to which payments belong.

    Required if no other filter is provided.
    """

    settlement_utc: Annotated[Optional[SettlementUtc], PropertyInfo(alias="SettlementUtc")]
    """Interval in which the `Payments` were settled."""

    states: Annotated[
        Optional[List[Literal["Charged", "Canceled", "Pending", "Failed", "Verifying"]]], PropertyInfo(alias="States")
    ]
    """Payment state of the item."""

    type: Annotated[
        Optional[
            Literal[
                "Payment",
                "CreditCardPayment",
                "AlternativePayment",
                "CashPayment",
                "InvoicePayment",
                "ExternalPayment",
                "GhostPayment",
                "TaxDeductedPayment",
            ]
        ],
        PropertyInfo(alias="Type"),
    ]
    """Payment

    CreditCardPayment

    AlternativePayment

    CashPayment

    InvoicePayment

    ExternalPayment

    GhostPayment

    TaxDeductedPayment
    """

    updated_utc: Annotated[Optional[UpdatedUtc], PropertyInfo(alias="UpdatedUtc")]
    """Time interval during which the `Payment` was updated.

    Required if no other filter is provided.
    """


class Limitation(TypedDict, total=False):
    count: Required[Annotated[int, PropertyInfo(alias="Count")]]

    cursor: Annotated[Optional[str], PropertyInfo(alias="Cursor")]


class ChargedUtc(TypedDict, total=False):
    end_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="EndUtc", format="iso8601")]

    start_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="StartUtc", format="iso8601")]


class ClosedUtc(TypedDict, total=False):
    end_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="EndUtc", format="iso8601")]

    start_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="StartUtc", format="iso8601")]


class CreatedUtc(TypedDict, total=False):
    end_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="EndUtc", format="iso8601")]

    start_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="StartUtc", format="iso8601")]


class SettlementUtc(TypedDict, total=False):
    end_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="EndUtc", format="iso8601")]

    start_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="StartUtc", format="iso8601")]


class UpdatedUtc(TypedDict, total=False):
    end_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="EndUtc", format="iso8601")]

    start_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="StartUtc", format="iso8601")]
