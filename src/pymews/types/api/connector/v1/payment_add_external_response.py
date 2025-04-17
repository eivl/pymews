# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["PaymentAddExternalResponse"]


class PaymentAddExternalResponse(BaseModel):
    external_payment_id: Optional[str] = FieldInfo(alias="ExternalPaymentId", default=None)
    """
    Unique identifier of the
    [Payment item](https://mews-systems.gitbook.io/connector-api/operations/accountingitems/#payment-item).
    """
