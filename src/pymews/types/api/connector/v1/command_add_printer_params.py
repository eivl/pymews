# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["CommandAddPrinterParams"]


class CommandAddPrinterParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    copy_count: Required[Annotated[int, PropertyInfo(alias="CopyCount")]]
    """Count of copies to be printed."""

    data: Required[Annotated[str, PropertyInfo(alias="Data")]]
    """Base64 encoded data of PDF document to print."""

    printer_id: Required[Annotated[str, PropertyInfo(alias="PrinterId")]]
    """
    Uniqque identifier of the Printer
    [Device](https://mews-systems.gitbook.io/connector-api/operations/devices/#device)
    where to print the document.
    """

    enterprise_id: Annotated[Optional[str], PropertyInfo(alias="EnterpriseId")]
    """Unique identifier of the enterprise.

    Required when using
    [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
    ignored otherwise.
    """
