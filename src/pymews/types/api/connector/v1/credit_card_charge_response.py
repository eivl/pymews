# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["CreditCardChargeResponse"]


class CreditCardChargeResponse(BaseModel):
    payment_id: Optional[str] = FieldInfo(alias="PaymentId", default=None)
    """
    Unique identifier of the
    [Payment item](https://mews-systems.gitbook.io/connector-api/operations/accountingitems/#payment-item).
    """
