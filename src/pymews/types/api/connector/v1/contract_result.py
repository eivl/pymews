# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["ContractResult", "TravelAgencyContract", "TravelAgencyContractOptions"]


class TravelAgencyContractOptions(BaseModel):
    include_cancellation_fee_in_commission_estimate: Optional[bool] = FieldInfo(
        alias="IncludeCancellationFeeInCommissionEstimate", default=None
    )

    skip_automatic_settlement: Optional[bool] = FieldInfo(alias="SkipAutomaticSettlement", default=None)


class TravelAgencyContract(BaseModel):
    company_id: str = FieldInfo(alias="CompanyId")
    """
    Unique identifier of the contracted
    [Company](https://mews-systems.gitbook.io/connector-api/operations/companies/#company).
    """

    created_utc: datetime = FieldInfo(alias="CreatedUtc")
    """
    Creation date and time of the travel agency contract in UTC timezone in ISO 8601
    format.
    """

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the contract."""

    is_active: bool = FieldInfo(alias="IsActive")
    """Whether the contract is still active."""

    service_id: str = FieldInfo(alias="ServiceId")
    """
    Unique identifier of the
    [Service](https://mews-systems.gitbook.io/connector-api/operations/services/#service)
    the contract is related to.
    """

    updated_utc: datetime = FieldInfo(alias="UpdatedUtc")
    """
    Last update date and time of the travel agency contract in UTC timezone in ISO
    8601 format.
    """

    accounting_code: Optional[str] = FieldInfo(alias="AccountingCode", default=None)
    """Accounting code of the travel agency contract."""

    additional_contact_info: Optional[str] = FieldInfo(alias="AdditionalContactInfo", default=None)
    """Additional contact info of the travel agency."""

    channel_manager_absolute_adjustment: Optional[float] = FieldInfo(
        alias="ChannelManagerAbsoluteAdjustment", default=None
    )
    """
    Flat fee added to (or subtracted from) the reservation price when coming from
    Channel Managers.
    """

    channel_manager_business_segment_id: Optional[str] = FieldInfo(
        alias="ChannelManagerBusinessSegmentId", default=None
    )

    channel_manager_relative_adjustment: Optional[float] = FieldInfo(
        alias="ChannelManagerRelativeAdjustment", default=None
    )
    """
    Percentage of the reservation price added to (or subtracted from) price when
    coming from Channel Managers.
    """

    commission: Optional[float] = FieldInfo(alias="Commission", default=None)
    """Commission of the travel agency."""

    commission_included: Optional[bool] = FieldInfo(alias="CommissionIncluded", default=None)
    """Whether commission of the travel agency is included in the rate.

    When CommissionIncluded is not provided in the response, that means commission
    is unspecified, when set to true it means the the commission is included in the
    rate and false means the commission in not included in the rate.
    """

    contact_email: Optional[str] = FieldInfo(alias="ContactEmail", default=None)
    """Contact email of the travel agency."""

    contact_person: Optional[str] = FieldInfo(alias="ContactPerson", default=None)
    """Contact person of the travel agency."""

    invoice_due_interval: Optional[str] = FieldInfo(alias="InvoiceDueInterval", default=None)
    """
    The maximum time, when the invoice has to be be paid in ISO 8601 duration
    format.
    """

    notes: Optional[str] = FieldInfo(alias="Notes", default=None)
    """Additional notes of the travel agency contract."""

    options: Optional[TravelAgencyContractOptions] = FieldInfo(alias="Options", default=None)
    """Options of the travel agency contract."""


class ContractResult(BaseModel):
    travel_agency_contracts: List[TravelAgencyContract] = FieldInfo(alias="TravelAgencyContracts")
    """The updated travel agency contracts."""

    cursor: Optional[str] = FieldInfo(alias="Cursor", default=None)
    """Unique identifier of the last and hence oldest contract returned.

    This can be used in
    [Limitation](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/#limitation)
    in a subsequent request to fetch the next batch of older messages.
    """
