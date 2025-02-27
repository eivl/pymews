# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["PaymentRequestAddParams", "PaymentRequest", "PaymentRequestAmount"]


class PaymentRequestAddParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    payment_requests: Required[Annotated[Iterable[PaymentRequest], PropertyInfo(alias="PaymentRequests")]]
    """Payment requests to be added."""

    enterprise_id: Annotated[Optional[str], PropertyInfo(alias="EnterpriseId")]
    """Unique identifier of the enterprise.

    Required when using
    [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
    ignored otherwise.
    """


class PaymentRequestAmount(TypedDict, total=False):
    currency: Required[Annotated[str, PropertyInfo(alias="Currency")]]

    value: Required[Annotated[float, PropertyInfo(alias="Value")]]


class PaymentRequest(TypedDict, total=False):
    account_id: Required[Annotated[str, PropertyInfo(alias="AccountId")]]

    amount: Required[Annotated[PaymentRequestAmount, PropertyInfo(alias="Amount")]]
    """Absolute value of the fee."""

    description: Required[Annotated[str, PropertyInfo(alias="Description")]]

    expiration_utc: Required[Annotated[Union[str, datetime], PropertyInfo(alias="ExpirationUtc", format="iso8601")]]

    reason: Required[
        Annotated[
            Literal[
                "Other", "PaymentCardMissing", "PaymentCardDeclined", "Deposit", "Prepayment", "Fee", "RecurringPayment"
            ],
            PropertyInfo(alias="Reason"),
        ]
    ]

    type: Required[Annotated[Literal["Payment", "Preauthorization"], PropertyInfo(alias="Type")]]

    notes: Annotated[Optional[str], PropertyInfo(alias="Notes")]

    reservation_id: Annotated[Optional[str], PropertyInfo(alias="ReservationId")]
