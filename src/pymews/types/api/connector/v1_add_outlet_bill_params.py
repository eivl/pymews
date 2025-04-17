# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = [
    "V1AddOutletBillParams",
    "Bill",
    "BillItem",
    "BillItemUnitAmount",
    "BillItemAccountingCategory",
    "BillItemUnitCost",
]


class V1AddOutletBillParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    bills: Required[Annotated[Iterable[Bill], PropertyInfo(alias="Bills")]]
    """The new outlet bills."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""


class BillItemUnitAmount(TypedDict, total=False):
    currency: Required[Annotated[str, PropertyInfo(alias="Currency")]]

    tax_codes: Required[Annotated[List[str], PropertyInfo(alias="TaxCodes")]]

    gross_value: Annotated[Optional[float], PropertyInfo(alias="GrossValue")]

    net_value: Annotated[Optional[float], PropertyInfo(alias="NetValue")]


class BillItemAccountingCategory(TypedDict, total=False):
    code: Annotated[Optional[str], PropertyInfo(alias="Code")]

    name: Annotated[Optional[str], PropertyInfo(alias="Name")]


class BillItemUnitCost(TypedDict, total=False):
    amount: Required[Annotated[float, PropertyInfo(alias="Amount")]]

    currency: Required[Annotated[str, PropertyInfo(alias="Currency")]]

    tax: Required[Annotated[float, PropertyInfo(alias="Tax")]]


class BillItem(TypedDict, total=False):
    consumed_utc: Required[Annotated[Union[str, datetime], PropertyInfo(alias="ConsumedUtc", format="iso8601")]]

    name: Required[Annotated[str, PropertyInfo(alias="Name")]]

    unit_amount: Required[Annotated[BillItemUnitAmount, PropertyInfo(alias="UnitAmount")]]
    """Price of the product that overrides the price defined in Mews."""

    unit_count: Required[Annotated[int, PropertyInfo(alias="UnitCount")]]

    accounting_category: Annotated[Optional[BillItemAccountingCategory], PropertyInfo(alias="AccountingCategory")]

    accounting_category_id: Annotated[Optional[str], PropertyInfo(alias="AccountingCategoryId")]

    external_identifier: Annotated[Optional[str], PropertyInfo(alias="ExternalIdentifier")]

    notes: Annotated[Optional[str], PropertyInfo(alias="Notes")]

    type: Annotated[Optional[str], PropertyInfo(alias="Type")]

    unit_cost: Annotated[Optional[BillItemUnitCost], PropertyInfo(alias="UnitCost")]


class Bill(TypedDict, total=False):
    closed_utc: Required[Annotated[str, PropertyInfo(alias="ClosedUtc")]]

    items: Required[Annotated[Iterable[BillItem], PropertyInfo(alias="Items")]]

    number: Required[Annotated[str, PropertyInfo(alias="Number")]]

    outlet_id: Required[Annotated[str, PropertyInfo(alias="OutletId")]]

    account_id: Annotated[Optional[str], PropertyInfo(alias="AccountId")]

    notes: Annotated[Optional[str], PropertyInfo(alias="Notes")]
