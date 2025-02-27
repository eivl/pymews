# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["V1ListExchangeRatesResponse", "ExchangeRate"]


class ExchangeRate(BaseModel):
    enterprise_id: str = FieldInfo(alias="EnterpriseId")
    """
    Unique identifier of the
    [Enterprise](https://mews-systems.gitbook.io/connector-api/operations/configuration/#enterprise)
    to which the Exchange Rate belongs.
    """

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the Exchange Rate."""

    source_currency: str = FieldInfo(alias="SourceCurrency")
    """
    ISO-4217 code of the source
    [Currency](https://mews-systems.gitbook.io/connector-api/operations/currencies/#currency).
    """

    target_currency: str = FieldInfo(alias="TargetCurrency")
    """
    ISO-4217 code of the target
    [Currency](https://mews-systems.gitbook.io/connector-api/operations/currencies/#currency).
    """

    value: float = FieldInfo(alias="Value")
    """The exchange rate from the source currency to the target currency."""


class V1ListExchangeRatesResponse(BaseModel):
    exchange_rates: List[ExchangeRate] = FieldInfo(alias="ExchangeRates")
    """The available exchange rates."""
