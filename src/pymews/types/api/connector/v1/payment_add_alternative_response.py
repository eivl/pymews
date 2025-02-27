# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["PaymentAddAlternativeResponse", "NextAction"]


class NextAction(BaseModel):
    discriminator: Literal["RedirectToUrl"] = FieldInfo(alias="Discriminator")
    """
    RedirectToUrl (Redirect customer to a URL where they can complete their
    payment.)

    - `RedirectToUrl` - Redirect customer to a URL where they can complete their
      payment.
    """

    value: str = FieldInfo(alias="Value")
    """String value depending on `Type`."""


class PaymentAddAlternativeResponse(BaseModel):
    payment_id: str = FieldInfo(alias="PaymentId")
    """Unique identifier of the created payment."""

    next_action: Optional[NextAction] = FieldInfo(alias="NextAction", default=None)
    """Next action to take in order to complete the payment."""
