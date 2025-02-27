# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["VoucherAddParams", "VoucherParameter"]


class VoucherAddParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    voucher_parameters: Required[Annotated[Iterable[VoucherParameter], PropertyInfo(alias="VoucherParameters")]]
    """Vouchers to be added."""

    enterprise_id: Annotated[Optional[str], PropertyInfo(alias="EnterpriseId")]
    """Unique identifier of the enterprise.

    Required when using
    [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
    ignored otherwise.
    """


class VoucherParameter(TypedDict, total=False):
    name: Required[Annotated[str, PropertyInfo(alias="Name")]]
    """Internal name of the voucher."""

    service_id: Required[Annotated[str, PropertyInfo(alias="ServiceId")]]
    """Unique identifier of Service."""

    type: Required[Annotated[Literal["Public", "PartnerCompany", "TravelAgency"], PropertyInfo(alias="Type")]]
    """Public

    PartnerCompany

    TravelAgency
    """

    assigned_rate_ids: Annotated[Optional[List[str]], PropertyInfo(alias="AssignedRateIds")]
    """Unique identifiers of Rates."""

    company_id: Annotated[Optional[str], PropertyInfo(alias="CompanyId")]
    """Unique identifier of Company."""

    external_identifier: Annotated[Optional[str], PropertyInfo(alias="ExternalIdentifier")]
    """Identifier of the voucher from external system."""

    occupiable_interval_end_utc: Annotated[
        Union[str, datetime, None], PropertyInfo(alias="OccupiableIntervalEndUtc", format="iso8601")
    ]
    """End of the interval in which the voucher can be applied."""

    occupiable_interval_start_utc: Annotated[
        Union[str, datetime, None], PropertyInfo(alias="OccupiableIntervalStartUtc", format="iso8601")
    ]
    """Start of the interval in which the voucher can be applied."""
