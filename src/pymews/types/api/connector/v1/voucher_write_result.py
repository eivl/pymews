# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["VoucherWriteResult", "Voucher"]


class Voucher(BaseModel):
    created_utc: datetime = FieldInfo(alias="CreatedUtc")
    """Creation date and time of the voucher in UTC timezone in ISO 8601 format."""

    id: str = FieldInfo(alias="Id")
    """Unique identifier of voucher."""

    is_active: bool = FieldInfo(alias="IsActive")
    """Whether the voucher is still active."""

    name: str = FieldInfo(alias="Name")
    """Internal name of the voucher."""

    service_id: str = FieldInfo(alias="ServiceId")
    """
    Unique identifier of
    [Service](https://mews-systems.gitbook.io/connector-api/operations/services/#service)
    the voucher belongs to.
    """

    type: Literal["Public", "PartnerCompany", "TravelAgency"] = FieldInfo(alias="Type")
    """Public

    PartnerCompany

    TravelAgency
    """

    updated_utc: datetime = FieldInfo(alias="UpdatedUtc")
    """Last update date and time of the voucher in UTC timezone in ISO 8601 format."""

    activity_state: Optional[Literal["Deleted", "Active"]] = FieldInfo(alias="ActivityState", default=None)
    """Whether voucher is active or deleted."""

    company_id: Optional[str] = FieldInfo(alias="CompanyId", default=None)
    """
    Unique identifier of
    [Company](https://mews-systems.gitbook.io/connector-api/operations/companies/#company)
    the voucher is related to.
    """

    external_identifier: Optional[str] = FieldInfo(alias="ExternalIdentifier", default=None)
    """Identifier of the voucher from external system."""

    occupiable_interval_end_utc: Optional[datetime] = FieldInfo(alias="OccupiableIntervalEndUtc", default=None)
    """
    End of the time interval, expressed as the timestamp for the start of the last
    time unit, in UTC timezone ISO 8601 format (or null if the end time should not
    be updated).
    """

    occupiable_interval_start_utc: Optional[datetime] = FieldInfo(alias="OccupiableIntervalStartUtc", default=None)
    """
    Start of the time interval, expressed as the timestamp for the start of the
    first time unit, in UTC timezone ISO 8601 format (or null if the start time
    should not be updated).
    """

    travel_agency_id: Optional[str] = FieldInfo(alias="TravelAgencyId", default=None)
    """
    Unique identifier of
    [Company](https://mews-systems.gitbook.io/connector-api/operations/companies/#company)
    with
    [Travel agency contract](https://mews-systems.gitbook.io/connector-api/operations/companycontracts/#travel-agency-contract)
    the voucher is related to.
    """


class VoucherWriteResult(BaseModel):
    vouchers: Optional[List[Voucher]] = FieldInfo(alias="Vouchers", default=None)
    """Details about vouchers added to the system."""
