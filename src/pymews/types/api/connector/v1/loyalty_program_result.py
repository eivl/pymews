# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["LoyaltyProgramResult", "LoyaltyProgram"]


class LoyaltyProgram(BaseModel):
    chain_id: str = FieldInfo(alias="ChainId")
    """Unique identifier of the chain."""

    code: str = FieldInfo(alias="Code")
    """Code of the loyalty program."""

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the loyalty program."""

    name: str = FieldInfo(alias="Name")
    """Name of the loyalty program."""

    subscription: Optional[Literal["Free", "Paid"]] = FieldInfo(alias="Subscription", default=None)

    type: Optional[Literal["Hotel", "ExternalPartner", "SoftBrand", "Unknown"]] = FieldInfo(alias="Type", default=None)


class LoyaltyProgramResult(BaseModel):
    loyalty_programs: List[LoyaltyProgram] = FieldInfo(alias="LoyaltyPrograms")
    """Updated loyalty programs."""

    cursor: Optional[str] = FieldInfo(alias="Cursor", default=None)
    """
    Unique identifier of the item one newer in time order than the items to be
    returned. If Cursor is not specified, i.e. null, then the latest or most recent
    items will be returned.
    """
