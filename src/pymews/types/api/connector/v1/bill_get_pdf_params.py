# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["BillGetPdfParams"]


class BillGetPdfParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    bill_id: Required[Annotated[str, PropertyInfo(alias="BillId")]]
    """
    Unique identifier of the
    [Bill](https://mews-systems.gitbook.io/connector-api/operations/#bill) to be
    printed.
    """

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    bill_print_event_id: Annotated[Optional[str], PropertyInfo(alias="BillPrintEventId")]
    """
    Unique identifier of the
    [Bill print event](https://mews-systems.gitbook.io/connector-api/operations/#bill-print-event)
    returned by previous invocation.
    """

    pdf_template: Annotated[
        Optional[Literal["Detailed", "Consumption", "Reservation", "OrderItem", "Guest"]],
        PropertyInfo(alias="PdfTemplate"),
    ]
    """Detailed (Detailed overview.

    Items are grouped by the reservation, item type and price, and consumption
    date.)

    Consumption (Overview by date (no reservation details). Items of the same type
    and price are grouped by consumption date.)

    Reservation (Overview by reservation (no date). Items of the same type and price
    are grouped by reservation.)

    OrderItem (Consumption overview (not fiscal document). Items are grouped by the
    item type and price without reservation details and consumption date.)

    Guest (Overview by guest. Items are grouped by guest, reservation, consumption
    date, and item type.)

    - `Detailed` - Detailed overview. Items are grouped by the reservation, item
      type and price, and consumption date.
    - `Consumption` - Overview by date (no reservation details). Items of the same
      type and price are grouped by consumption date.
    - `Reservation` - Overview by reservation (no date). Items of the same type and
      price are grouped by reservation.
    - `OrderItem` - Consumption overview (not fiscal document). Items are grouped by
      the item type and price without reservation details and consumption date.
    - `Guest` - Overview by guest. Items are grouped by guest, reservation,
      consumption date, and item type.
    """

    print_reason: Annotated[Optional[str], PropertyInfo(alias="PrintReason")]
    """The reason for reprinting the bill with different template.

    Required for France LE.
    """
