# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = [
    "LoyaltyMembershipResult",
    "LoyaltyMembership",
    "LoyaltyMembershipCreatorProfile",
    "LoyaltyMembershipCreatorProfileEnterpriseProfile",
    "LoyaltyMembershipUpdaterProfile",
    "LoyaltyMembershipUpdaterProfileEnterpriseProfile",
]


class LoyaltyMembershipCreatorProfileEnterpriseProfile(BaseModel):
    profile_id: str = FieldInfo(alias="ProfileId")
    """Unique identifier of the profile."""


class LoyaltyMembershipCreatorProfile(BaseModel):
    discriminator: Literal["Personal", "Enterprise", "Platform", "Static", "Integration"] = FieldInfo(
        alias="Discriminator"
    )

    enterprise_profile: Optional[LoyaltyMembershipCreatorProfileEnterpriseProfile] = FieldInfo(
        alias="EnterpriseProfile", default=None
    )
    """Enterprise profile data."""


class LoyaltyMembershipUpdaterProfileEnterpriseProfile(BaseModel):
    profile_id: str = FieldInfo(alias="ProfileId")
    """Unique identifier of the profile."""


class LoyaltyMembershipUpdaterProfile(BaseModel):
    discriminator: Literal["Personal", "Enterprise", "Platform", "Static", "Integration"] = FieldInfo(
        alias="Discriminator"
    )

    enterprise_profile: Optional[LoyaltyMembershipUpdaterProfileEnterpriseProfile] = FieldInfo(
        alias="EnterpriseProfile", default=None
    )
    """Enterprise profile data."""


class LoyaltyMembership(BaseModel):
    account_id: str = FieldInfo(alias="AccountId")
    """Unique identifier of the account."""

    chain_id: str = FieldInfo(alias="ChainId")
    """Unique identifier of the chain."""

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the loyalty membership."""

    is_primary: bool = FieldInfo(alias="IsPrimary")
    """Defines the primary loyalty membership."""

    loyalty_program_id: str = FieldInfo(alias="LoyaltyProgramId")
    """Unique identifier of the loyalty program."""

    state: Literal["New", "Pending", "Enrolled", "Canceled", "Declined"] = FieldInfo(alias="State")

    code: Optional[str] = FieldInfo(alias="Code", default=None)
    """Code of the loyalty membership."""

    creator_profile: Optional[LoyaltyMembershipCreatorProfile] = FieldInfo(alias="CreatorProfile", default=None)
    """The profile data of the user who created or last updated the record."""

    expiration_date: Optional[datetime] = FieldInfo(alias="ExpirationDate", default=None)
    """Expiration date of the loyalty membership in UTC timezone in ISO 8601 format."""

    loyalty_tier_id: Optional[str] = FieldInfo(alias="LoyaltyTierId", default=None)
    """Unique identifier of the loyalty tier."""

    points: Optional[int] = FieldInfo(alias="Points", default=None)
    """The loyalty points for the account in that membership."""

    updater_profile: Optional[LoyaltyMembershipUpdaterProfile] = FieldInfo(alias="UpdaterProfile", default=None)
    """The profile data of the user who created or last updated the record."""

    url: Optional[str] = FieldInfo(alias="Url", default=None)
    """Url of the loyalty membership."""


class LoyaltyMembershipResult(BaseModel):
    loyalty_memberships: List[LoyaltyMembership] = FieldInfo(alias="LoyaltyMemberships")
    """Added loyalty memberships."""

    cursor: Optional[str] = FieldInfo(alias="Cursor", default=None)
    """
    Unique identifier of the item one newer in time order than the items to be
    returned. If Cursor is not specified, i.e. null, then the latest or most recent
    items will be returned.
    """
