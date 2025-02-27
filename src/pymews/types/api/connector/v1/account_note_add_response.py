# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = [
    "AccountNoteAddResponse",
    "AccountNote",
    "AccountNoteCreatorProfile",
    "AccountNoteCreatorProfileEnterpriseProfile",
    "AccountNoteUpdaterProfile",
    "AccountNoteUpdaterProfileEnterpriseProfile",
]


class AccountNoteCreatorProfileEnterpriseProfile(BaseModel):
    profile_id: str = FieldInfo(alias="ProfileId")
    """Unique identifier of the profile."""


class AccountNoteCreatorProfile(BaseModel):
    discriminator: Literal["Personal", "Enterprise", "Platform", "Static", "Integration"] = FieldInfo(
        alias="Discriminator"
    )

    enterprise_profile: Optional[AccountNoteCreatorProfileEnterpriseProfile] = FieldInfo(
        alias="EnterpriseProfile", default=None
    )
    """Enterprise profile data."""


class AccountNoteUpdaterProfileEnterpriseProfile(BaseModel):
    profile_id: str = FieldInfo(alias="ProfileId")
    """Unique identifier of the profile."""


class AccountNoteUpdaterProfile(BaseModel):
    discriminator: Literal["Personal", "Enterprise", "Platform", "Static", "Integration"] = FieldInfo(
        alias="Discriminator"
    )

    enterprise_profile: Optional[AccountNoteUpdaterProfileEnterpriseProfile] = FieldInfo(
        alias="EnterpriseProfile", default=None
    )
    """Enterprise profile data."""


class AccountNote(BaseModel):
    account_id: str = FieldInfo(alias="AccountId")
    """Unique identifier of the account."""

    account_type: Literal["Company", "Customer"] = FieldInfo(alias="AccountType")
    """Company

    Customer
    """

    classifications: List[
        Literal[
            "General",
            "FoodAndBeverage",
            "FrontOffice",
            "Reservations",
            "Housekeeping",
            "Maintenance",
            "PreviousStay",
            "FamilyRelations",
            "Gifts",
            "Accounting",
            "Complaints",
            "Other",
        ]
    ] = FieldInfo(alias="Classifications")
    """Specifying the classifications of the note based on account type."""

    content: str = FieldInfo(alias="Content")
    """The content of the account note."""

    creator_profile: AccountNoteCreatorProfile = FieldInfo(alias="CreatorProfile")
    """The profile data of the user who created or last updated the record."""

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the account note."""

    is_active: bool = FieldInfo(alias="IsActive")
    """Whether the account note is still active."""

    updater_profile: AccountNoteUpdaterProfile = FieldInfo(alias="UpdaterProfile")
    """The profile data of the user who created or last updated the record."""


class AccountNoteAddResponse(BaseModel):
    account_notes: List[AccountNote] = FieldInfo(alias="AccountNotes")
    """Added account notes."""
