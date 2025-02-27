# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["PaymentRefundParams"]


class PaymentRefundParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    account_id: Required[Annotated[str, PropertyInfo(alias="AccountId")]]
    """
    Unique identifier of the account (for example
    [Customer](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer))
    the payment belongs to.
    """

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    payment_id: Required[Annotated[str, PropertyInfo(alias="PaymentId")]]
    """
    Unique identifier of specific
    [Payment](https://mews-systems.gitbook.io/connector-api/operations/payments/#payment).
    """

    reason: Required[Annotated[str, PropertyInfo(alias="Reason")]]
    """Refund reason."""

    enterprise_id: Annotated[Optional[str], PropertyInfo(alias="EnterpriseId")]
    """Unique identifier of the enterprise.

    Required when using
    [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
    ignored otherwise.
    """

    value_to_refund: Annotated[Optional[float], PropertyInfo(alias="ValueToRefund")]
    """Refund amount. If not provided, the whole payment will be refunded."""
