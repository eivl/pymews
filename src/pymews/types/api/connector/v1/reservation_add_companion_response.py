# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["ReservationAddCompanionResponse"]


class ReservationAddCompanionResponse(BaseModel):
    companionship_id: str = FieldInfo(alias="CompanionshipId")
    """Identifier of the created `Companionship` entity."""
