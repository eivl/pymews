# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["CancellationPolicyListResponse", "CancellationPolicy", "CancellationPolicyAbsoluteFee"]


class CancellationPolicyAbsoluteFee(BaseModel):
    currency: str = FieldInfo(alias="Currency")

    value: float = FieldInfo(alias="Value")


class CancellationPolicy(BaseModel):
    absolute_fee: CancellationPolicyAbsoluteFee = FieldInfo(alias="AbsoluteFee")
    """Absolute value of the fee."""

    applicability: Literal["Creation", "Start", "StartDate"] = FieldInfo(alias="Applicability")
    """Applicability mode of the cancellation policy."""

    applicability_offset: str = FieldInfo(alias="ApplicabilityOffset")
    """
    Offset for order start (assuming Applicability is set to Start) from which the
    fee is applied.
    """

    created_utc: datetime = FieldInfo(alias="CreatedUtc")
    """
    Date and time of the cancellation policy creation in UTC timezone in ISO 8601
    format.
    """

    fee_extent: List[Literal["TimeUnits", "Products"]] = FieldInfo(alias="FeeExtent")
    """Extent for the cancellation fee, i.e.

    what should be in scope for the automatic payment.
    """

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the cancellation policy."""

    is_active: bool = FieldInfo(alias="IsActive")
    """Whether the cancellation policy is still active."""

    rate_group_id: str = FieldInfo(alias="RateGroupId")
    """Unique identifier of the rate group the cancellation policy belongs to."""

    relative_fee: float = FieldInfo(alias="RelativeFee")
    """Relative value of the fee, as a percentage of the reservation price."""

    updated_utc: datetime = FieldInfo(alias="UpdatedUtc")
    """
    Date and time of the cancellation policy update in UTC timezone in ISO 8601
    format.
    """

    fee_maximum_time_units: Optional[int] = FieldInfo(alias="FeeMaximumTimeUnits", default=None)
    """Maximum number of time units the cancellation fee is applicable to."""


class CancellationPolicyListResponse(BaseModel):
    cancellation_policies: List[CancellationPolicy] = FieldInfo(alias="CancellationPolicies")
    """The filtered cancellation policies."""

    cursor: Optional[str] = FieldInfo(alias="Cursor", default=None)
    """Unique identifier of the last and hence oldest cancellation policy returned.

    This can be used in
    [Limitation](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/#limitation)
    in a subsequent request to fetch the next batch of older cancellation policies.
    """
