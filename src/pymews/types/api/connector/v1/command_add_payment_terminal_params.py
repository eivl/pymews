# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["CommandAddPaymentTerminalParams", "Amount"]


class CommandAddPaymentTerminalParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    customer_id: Required[Annotated[str, PropertyInfo(alias="CustomerId")]]
    """
    Unique identifier of the
    [Customer](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer).
    """

    terminal_id: Required[Annotated[str, PropertyInfo(alias="TerminalId")]]
    """Unique identifier of the payment terminal."""

    type: Required[Annotated[Literal["Payment", "Preauthorization"], PropertyInfo(alias="Type")]]

    amount: Annotated[Optional[Amount], PropertyInfo(alias="Amount")]
    """Total price of the reservation."""

    bill_id: Annotated[Optional[str], PropertyInfo(alias="BillId")]
    """
    Unique identifier of the
    [Bill](https://mews-systems.gitbook.io/connector-api/operations/bills/#bill).
    """

    payment_request_id: Annotated[Optional[str], PropertyInfo(alias="PaymentRequestId")]

    reservation_id: Annotated[Optional[str], PropertyInfo(alias="ReservationId")]


class Amount(TypedDict, total=False):
    currency: Required[Annotated[str, PropertyInfo(alias="Currency")]]

    net: Annotated[Optional[float], PropertyInfo(alias="Net")]

    tax: Annotated[Optional[float], PropertyInfo(alias="Tax")]

    tax_rate: Annotated[Optional[float], PropertyInfo(alias="TaxRate")]

    value: Annotated[Optional[float], PropertyInfo(alias="Value")]
