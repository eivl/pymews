# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["LoyaltyTierResult", "LoyaltyTier"]


class LoyaltyTier(BaseModel):
    code: str = FieldInfo(alias="Code")
    """Code of the loyalty tier."""

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the loyalty tier."""

    loyalty_program_id: str = FieldInfo(alias="LoyaltyProgramId")
    """Unique identifier of the loyalty program of that loyalty tier."""

    name: str = FieldInfo(alias="Name")
    """Name of the loyalty tier."""

    ordering: int = FieldInfo(alias="Ordering")
    """Ordering of the loyalty tier."""


class LoyaltyTierResult(BaseModel):
    loyalty_tiers: List[LoyaltyTier] = FieldInfo(alias="LoyaltyTiers")
    """Updated loyalty tiers."""

    cursor: Optional[str] = FieldInfo(alias="Cursor", default=None)
    """
    Unique identifier of the item one newer in time order than the items to be
    returned. If Cursor is not specified, i.e. null, then the latest or most recent
    items will be returned.
    """
