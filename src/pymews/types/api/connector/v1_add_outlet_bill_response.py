# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["V1AddOutletBillResponse"]


class V1AddOutletBillResponse(BaseModel):
    outlet_bill_ids: Optional[List[str]] = FieldInfo(alias="OutletBillIds", default=None)
    """Array of unique identifiers of the added Outlet bills."""
