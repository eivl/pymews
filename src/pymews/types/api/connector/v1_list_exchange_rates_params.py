# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["V1ListExchangeRatesParams"]


class V1ListExchangeRatesParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    enterprise_ids: Annotated[Optional[List[str]], PropertyInfo(alias="EnterpriseIds")]
    """
    Unique identifiers of the
    [Enterprises](https://mews-systems.gitbook.io/connector-api/operations/configuration/#enterprise).
    If not specified, the operation returns the exchange rates for all enterprises
    within scope of the Access Token.
    """

    ids: Annotated[Optional[List[str]], PropertyInfo(alias="Ids")]
    """Unique identifiers of the Exchange Rates.

    If not specified, the operation returns all exchange rates.
    """
