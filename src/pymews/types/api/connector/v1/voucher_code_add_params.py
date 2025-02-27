# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["VoucherCodeAddParams", "VoucherCodeParameter"]


class VoucherCodeAddParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    voucher_code_parameters: Required[
        Annotated[Iterable[VoucherCodeParameter], PropertyInfo(alias="VoucherCodeParameters")]
    ]
    """Voucher codes to be added."""

    enterprise_id: Annotated[Optional[str], PropertyInfo(alias="EnterpriseId")]
    """Unique identifier of the enterprise.

    Required when using
    [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
    ignored otherwise.
    """


class VoucherCodeParameter(TypedDict, total=False):
    value: Required[Annotated[str, PropertyInfo(alias="Value")]]
    """Value of voucher code used by customers."""

    voucher_id: Required[Annotated[str, PropertyInfo(alias="VoucherId")]]
    """Unique identifier of [Voucher](#voucher) the code belongs to."""

    validity_end_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="ValidityEndUtc", format="iso8601")]
    """If specified, marks the end of interval in which the code can be used."""

    validity_start_utc: Annotated[Union[str, datetime, None], PropertyInfo(alias="ValidityStartUtc", format="iso8601")]
    """If specified, marks the beginning of interval in which the code can be used."""
