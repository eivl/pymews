# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["AddCreditCardResult"]


class AddCreditCardResult(BaseModel):
    credit_card_id: Optional[str] = FieldInfo(alias="CreditCardId", default=None)
    """
    Unique identifier of the
    [Credit card](https://mews-systems.gitbook.io/connector-api/operations/creditcards/#credit-card).
    """
