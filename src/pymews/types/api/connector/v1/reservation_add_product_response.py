# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["ReservationAddProductResponse"]


class ReservationAddProductResponse(BaseModel):
    item_ids: Optional[List[str]] = FieldInfo(alias="ItemIds", default=None)
