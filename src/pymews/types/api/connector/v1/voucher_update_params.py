# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = [
    "VoucherUpdateParams",
    "VoucherUpdate",
    "VoucherUpdateAssignedRateIDs",
    "VoucherUpdateCompanyID",
    "VoucherUpdateExternalIdentifier",
    "VoucherUpdateName",
    "VoucherUpdateOccupiableIntervalEndUtc",
    "VoucherUpdateOccupiableIntervalStartUtc",
    "VoucherUpdateType",
]


class VoucherUpdateParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    voucher_updates: Required[Annotated[Iterable[VoucherUpdate], PropertyInfo(alias="VoucherUpdates")]]
    """Details of voucher updates."""

    enterprise_id: Annotated[Optional[str], PropertyInfo(alias="EnterpriseId")]
    """Unique identifier of the enterprise.

    Required when using
    [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
    ignored otherwise.
    """


class VoucherUpdateAssignedRateIDs(TypedDict, total=False):
    value: Annotated[Optional[List[str]], PropertyInfo(alias="Value")]
    """Unique identifiers of Rates (or `null` should it not be updated)."""


class VoucherUpdateCompanyID(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class VoucherUpdateExternalIdentifier(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class VoucherUpdateName(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class VoucherUpdateOccupiableIntervalEndUtc(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class VoucherUpdateOccupiableIntervalStartUtc(TypedDict, total=False):
    value: Annotated[Optional[str], PropertyInfo(alias="Value")]


class VoucherUpdateType(TypedDict, total=False):
    value: Annotated[Literal["Public", "PartnerCompany", "TravelAgency"], PropertyInfo(alias="Value")]
    """Public

    PartnerCompany

    TravelAgency
    """


class VoucherUpdate(TypedDict, total=False):
    voucher_id: Required[Annotated[str, PropertyInfo(alias="VoucherId")]]
    """Unique identifier of the Voucher."""

    assigned_rate_ids: Annotated[Optional[VoucherUpdateAssignedRateIDs], PropertyInfo(alias="AssignedRateIds")]
    """
    Has same structure as
    [Array of strings update value](https://mews-systems.gitbook.io/connector-api/operations/_objects#array-of-strings-update-value).
    """

    company_id: Annotated[Optional[VoucherUpdateCompanyID], PropertyInfo(alias="CompanyId")]
    """
    Unique identifier of Company (Company or Travel Agency) the voucher is related
    to. This is required for Type of `PartnerCompany` or `TravelAgency`. Use `null`
    if Company should not be updated.
    """

    external_identifier: Annotated[Optional[VoucherUpdateExternalIdentifier], PropertyInfo(alias="ExternalIdentifier")]
    """
    Identifier of the voucher from external system (or `null` if the identifier
    should not be updated).
    """

    name: Annotated[Optional[VoucherUpdateName], PropertyInfo(alias="Name")]
    """Internal name of the voucher (or `null` if the name should not be updated)."""

    occupiable_interval_end_utc: Annotated[
        Optional[VoucherUpdateOccupiableIntervalEndUtc], PropertyInfo(alias="OccupiableIntervalEndUtc")
    ]
    """
    End of the interval in which the voucher can be applied (or `null` if the end
    time should not be updated).
    """

    occupiable_interval_start_utc: Annotated[
        Optional[VoucherUpdateOccupiableIntervalStartUtc], PropertyInfo(alias="OccupiableIntervalStartUtc")
    ]
    """
    Start of the interval in which the voucher can be applied (or `null` if the
    start time should not be updated).
    """

    type: Annotated[Optional[VoucherUpdateType], PropertyInfo(alias="Type")]
    """Type of the voucher e.g.

    'Public', 'PartnerCompany' or 'TravelAgency' (or `null` if the type should not
    be updated).
    """
