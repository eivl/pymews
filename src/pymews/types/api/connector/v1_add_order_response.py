# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["V1AddOrderResponse"]


class V1AddOrderResponse(BaseModel):
    charge_id: Optional[str] = FieldInfo(alias="ChargeId", default=None)

    order_id: Optional[str] = FieldInfo(alias="OrderId", default=None)
    """Unique identifier of the created order."""
