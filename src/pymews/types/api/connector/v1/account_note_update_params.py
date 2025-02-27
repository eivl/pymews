# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = [
    "AccountNoteUpdateParams",
    "AccountNoteUpdate",
    "AccountNoteUpdateClassifications",
    "AccountNoteUpdateClassificationsAccounting",
    "AccountNoteUpdateClassificationsComplaints",
    "AccountNoteUpdateClassificationsFamilyRelations",
    "AccountNoteUpdateClassificationsFoodAndBeverage",
    "AccountNoteUpdateClassificationsFrontOffice",
    "AccountNoteUpdateClassificationsGeneral",
    "AccountNoteUpdateClassificationsGifts",
    "AccountNoteUpdateClassificationsHousekeeping",
    "AccountNoteUpdateClassificationsMaintenance",
    "AccountNoteUpdateClassificationsOther",
    "AccountNoteUpdateClassificationsPreviousStay",
    "AccountNoteUpdateClassificationsReservations",
    "AccountNoteUpdateContent",
]


class AccountNoteUpdateParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    account_note_updates: Required[Annotated[Iterable[AccountNoteUpdate], PropertyInfo(alias="AccountNoteUpdates")]]
    """Account notes to be updated."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    chain_id: Annotated[Optional[str], PropertyInfo(alias="ChainId")]
    """Unique identifier of the chain.

    Required when using
    [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
    ignored otherwise.
    """


class AccountNoteUpdateClassificationsAccounting(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class AccountNoteUpdateClassificationsComplaints(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class AccountNoteUpdateClassificationsFamilyRelations(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class AccountNoteUpdateClassificationsFoodAndBeverage(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class AccountNoteUpdateClassificationsFrontOffice(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class AccountNoteUpdateClassificationsGeneral(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class AccountNoteUpdateClassificationsGifts(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class AccountNoteUpdateClassificationsHousekeeping(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class AccountNoteUpdateClassificationsMaintenance(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class AccountNoteUpdateClassificationsOther(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class AccountNoteUpdateClassificationsPreviousStay(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class AccountNoteUpdateClassificationsReservations(TypedDict, total=False):
    value: Annotated[bool, PropertyInfo(alias="Value")]


class AccountNoteUpdateClassifications(TypedDict, total=False):
    accounting: Annotated[Optional[AccountNoteUpdateClassificationsAccounting], PropertyInfo(alias="Accounting")]
    """
    Customer only: Boolean value defining the accounting classification for the
    account note (or `null` if the value should not be updated).
    """

    complaints: Annotated[Optional[AccountNoteUpdateClassificationsComplaints], PropertyInfo(alias="Complaints")]
    """
    Customer only: Boolean value defining the complaints classification for the
    account note (or `null` if the value should not be updated).
    """

    family_relations: Annotated[
        Optional[AccountNoteUpdateClassificationsFamilyRelations], PropertyInfo(alias="FamilyRelations")
    ]
    """
    Customer only: Boolean value defining the family relations classification for
    the account note (or `null` if the value should not be updated).
    """

    food_and_beverage: Annotated[
        Optional[AccountNoteUpdateClassificationsFoodAndBeverage], PropertyInfo(alias="FoodAndBeverage")
    ]
    """
    Customer only: Boolean value defining the food and beverage classification for
    the account note (or `null` if the value should not be updated).
    """

    front_office: Annotated[Optional[AccountNoteUpdateClassificationsFrontOffice], PropertyInfo(alias="FrontOffice")]
    """
    Customer only: Boolean value defining the front office classification for the
    account note (or `null` if the value should not be updated).
    """

    general: Annotated[Optional[AccountNoteUpdateClassificationsGeneral], PropertyInfo(alias="General")]
    """
    Company and Customer: Boolean value defining the general classification for the
    account note (or `null` if the value should not be updated).
    """

    gifts: Annotated[Optional[AccountNoteUpdateClassificationsGifts], PropertyInfo(alias="Gifts")]
    """
    Customer only: Boolean value defining the gifts classification for the account
    note (or `null` if the value should not be updated).
    """

    housekeeping: Annotated[Optional[AccountNoteUpdateClassificationsHousekeeping], PropertyInfo(alias="Housekeeping")]
    """
    Customer only: Boolean value defining the housekeeping classification for the
    account note (or `null` if the value should not be updated).
    """

    maintenance: Annotated[Optional[AccountNoteUpdateClassificationsMaintenance], PropertyInfo(alias="Maintenance")]
    """
    Customer only: Boolean value defining the maintenance classification for the
    account note (or `null` if the value should not be updated).
    """

    other: Annotated[Optional[AccountNoteUpdateClassificationsOther], PropertyInfo(alias="Other")]
    """
    Customer only: Boolean value defining the other classification for the account
    note (or `null` if the value should not be updated).
    """

    previous_stay: Annotated[Optional[AccountNoteUpdateClassificationsPreviousStay], PropertyInfo(alias="PreviousStay")]
    """
    Customer only: Boolean value defining the previous stay classification for the
    account note (or `null` if the value should not be updated).
    """

    reservations: Annotated[Optional[AccountNoteUpdateClassificationsReservations], PropertyInfo(alias="Reservations")]
    """
    Customer only: Boolean value defining the reservations classification for the
    account note (or `null` if the value should not be updated).
    """


class AccountNoteUpdateContent(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class AccountNoteUpdate(TypedDict, total=False):
    account_note_id: Required[Annotated[str, PropertyInfo(alias="AccountNoteId")]]
    """Unique identifier of the account note."""

    classifications: Required[Annotated[AccountNoteUpdateClassifications, PropertyInfo(alias="Classifications")]]
    """Classification of the account note."""

    content: Annotated[Optional[AccountNoteUpdateContent], PropertyInfo(alias="Content")]
    """Content of the account note (or `null` if the content should not be updated)."""
