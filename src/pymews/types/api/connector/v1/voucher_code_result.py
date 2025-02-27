# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["VoucherCodeResult", "VoucherCode"]


class VoucherCode(BaseModel):
    activity_state: Optional[str] = FieldInfo(alias="ActivityState", default=None)
    """Whether voucher code is active or deleted."""

    created_utc: Optional[str] = FieldInfo(alias="CreatedUtc", default=None)
    """Creation date and time of the voucher in UTC timezone in ISO 8601 format."""

    id: Optional[str] = FieldInfo(alias="Id", default=None)
    """Unique identifier of the voucher code."""

    is_active: Optional[bool] = FieldInfo(alias="IsActive", default=None)
    """Whether the voucher code is still active."""

    updated_utc: Optional[str] = FieldInfo(alias="UpdatedUtc", default=None)
    """Last update date and time of the voucher in UTC timezone in ISO 8601 format."""

    validity_end_utc: Optional[str] = FieldInfo(alias="ValidityEndUtc", default=None)
    """If specified, marks the end of interval in which the code can be used."""

    validity_start_utc: Optional[str] = FieldInfo(alias="ValidityStartUtc", default=None)
    """If specified, marks the beginning of interval in which the code can be used."""

    value: Optional[str] = FieldInfo(alias="Value", default=None)
    """Value of voucher code used by customers."""

    voucher_id: Optional[str] = FieldInfo(alias="VoucherId", default=None)
    """
    Unique identifier of
    [Voucher](https://mews-systems.gitbook.io/connector-api/operations/#voucher) the
    code belongs to.
    """


class VoucherCodeResult(BaseModel):
    voucher_codes: List[VoucherCode] = FieldInfo(alias="VoucherCodes")
    """Information about voucher codes used by customers."""

    cursor: Optional[str] = FieldInfo(alias="Cursor", default=None)
    """
    Unique identifier of the item one newer in time order than the items to be
    returned. If Cursor is not specified, i.e. null, then the latest or most recent
    items will be returned.
    """
