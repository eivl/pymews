# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["V1ListAccountingCategoriesResponse", "AccountingCategory"]


class AccountingCategory(BaseModel):
    created_utc: datetime = FieldInfo(alias="CreatedUtc")
    """
    Creation date and time of the accounting category in UTC timezone in ISO 8601
    format.
    """

    enterprise_id: str = FieldInfo(alias="EnterpriseId")
    """
    Unique identifier of the
    [Enterprise](https://mews-systems.gitbook.io/connector-api/operations/enterprises/#enterprise).
    """

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the category."""

    is_active: bool = FieldInfo(alias="IsActive")
    """Whether the accounting category is still active."""

    name: str = FieldInfo(alias="Name")
    """Name of the category."""

    updated_utc: datetime = FieldInfo(alias="UpdatedUtc")
    """
    Last update date and time of the accounting category in UTC timezone in ISO 8601
    format.
    """

    classification: Optional[
        Literal[
            "Accommodation",
            "FoodAndBeverage",
            "Taxes",
            "Payments",
            "ExternalRevenue",
            "SundryIncome",
            "Wellness",
            "Sport",
            "Technology",
            "Facilities",
            "Events",
            "Tourism",
        ]
    ] = FieldInfo(alias="Classification", default=None)
    """Accommodation

    FoodAndBeverage

    Taxes

    Payments

    ExternalRevenue

    SundryIncome

    Wellness

    Sport

    Technology

    Facilities

    Events

    Tourism
    """

    code: Optional[str] = FieldInfo(alias="Code", default=None)
    """Code of the category within Mews."""

    cost_center_code: Optional[str] = FieldInfo(alias="CostCenterCode", default=None)
    """Code of cost center."""

    external_code: Optional[str] = FieldInfo(alias="ExternalCode", default=None)
    """Code of the category in external systems."""

    ledger_account_code: Optional[str] = FieldInfo(alias="LedgerAccountCode", default=None)
    """Code of the ledger account (double entry accounting)."""

    posting_account_code: Optional[str] = FieldInfo(alias="PostingAccountCode", default=None)
    """Code of the posting account (double entry accounting)."""


class V1ListAccountingCategoriesResponse(BaseModel):
    accounting_categories: List[AccountingCategory] = FieldInfo(alias="AccountingCategories")
    """Accounting categories of the enterprise."""

    cursor: Optional[str] = FieldInfo(alias="Cursor", default=None)
    """
    Unique identifier of the item one newer in time order than the items to be
    returned. If Cursor is not specified, i.e. null, then the latest or most recent
    items will be returned.
    """
