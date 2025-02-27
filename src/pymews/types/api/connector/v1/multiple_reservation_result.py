# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["MultipleReservationResult"]


class MultipleReservationResult(BaseModel):
    reservation_ids: List[str] = FieldInfo(alias="ReservationIds")
    """Identifiers of the affected `Reservation` entities."""
