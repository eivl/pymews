# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = [
    "CancellationPolicyGetByRatesResponse",
    "CancellationPolicy",
    "CancellationPolicyPolicy",
    "CancellationPolicyPolicyAbsoluteFee",
]


class CancellationPolicyPolicyAbsoluteFee(BaseModel):
    currency: str = FieldInfo(alias="Currency")

    value: float = FieldInfo(alias="Value")


class CancellationPolicyPolicy(BaseModel):
    absolute_fee: CancellationPolicyPolicyAbsoluteFee = FieldInfo(alias="AbsoluteFee")
    """Absolute value of the fee."""

    applicability: Literal["Creation", "Start", "StartDate"] = FieldInfo(alias="Applicability")
    """Applicability mode of the cancellation policy.

    Creation

    Start

    StartDate
    """

    applicability_offset: str = FieldInfo(alias="ApplicabilityOffset")
    """
    Offset for order start (assuming Applicability is set to Start) from which the
    fee is applied in ISO 8601 duration format.
    """

    fee_extents: List[Literal["Nothing", "TimeUnits", "Products", "Everything"]] = FieldInfo(alias="FeeExtents")
    """Extent for the cancellation fee, i.e.

    what should be in scope for the automatic payment.
    """

    relative_fee: float = FieldInfo(alias="RelativeFee")
    """Relative value of the fee, as a percentage of the reservation price."""

    fee_maximum_time_units: Optional[int] = FieldInfo(alias="FeeMaximumTimeUnits", default=None)
    """Maximum number of time units the cancellation fee is applicable to."""


class CancellationPolicy(BaseModel):
    policies: List[CancellationPolicyPolicy] = FieldInfo(alias="Policies")
    """Collection of cancellation policy data."""

    rate_id: str = FieldInfo(alias="RateId")
    """Unique identifier of the `Rate`."""


class CancellationPolicyGetByRatesResponse(BaseModel):
    cancellation_policies: List[CancellationPolicy] = FieldInfo(alias="CancellationPolicies")
    """List of cancellation policies data grouped by rate."""
