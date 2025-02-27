# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["V1ListCurrenciesResponse", "Currency"]


class Currency(BaseModel):
    code: str = FieldInfo(alias="Code")
    """ISO-4217 three-letter code, e.g. USD or GBP."""

    precision: int = FieldInfo(alias="Precision")
    """Precision of the currency (count of decimal places)."""


class V1ListCurrenciesResponse(BaseModel):
    currencies: List[Currency] = FieldInfo(alias="Currencies")
    """The supported currencies."""
