# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["PaymentRefundResponse", "Amount"]


class Amount(BaseModel):
    currency: str = FieldInfo(alias="Currency")

    value: float = FieldInfo(alias="Value")


class PaymentRefundResponse(BaseModel):
    amount: Amount = FieldInfo(alias="Amount")
    """Absolute value of the fee."""

    payment_id: str = FieldInfo(alias="PaymentId")
    """
    Unique identifier of specific
    [Payment](https://mews-systems.gitbook.io/connector-api/operations/payments/#payment).
    """

    refund_id: str = FieldInfo(alias="RefundId")
    """Unique identifier of refund."""

    state: Literal["Charged", "Canceled", "Pending", "Failed", "Verifying"] = FieldInfo(alias="State")
    """Charged

    Canceled

    Pending

    Failed

    Verifying
    """

    type: Literal["CreditCardPayment", "AlternativePayment"] = FieldInfo(alias="Type")
    """CreditCardPayment

    AlternativePayment
    """
