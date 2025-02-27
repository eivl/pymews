# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["V1ListProductServiceOrdersResponse", "ProductServiceOrder", "ProductServiceOrderOptions"]


class ProductServiceOrderOptions(BaseModel):
    all_companions_checked_in: bool = FieldInfo(alias="AllCompanionsCheckedIn")
    """All companions of the reservation checked in."""

    any_companion_checked_in: bool = FieldInfo(alias="AnyCompanionCheckedIn")
    """Any of the companions of the reservation checked in."""

    connector_check_in: bool = FieldInfo(alias="ConnectorCheckIn")
    """Check in was done via Connector API."""

    owner_checked_in: bool = FieldInfo(alias="OwnerCheckedIn")
    """Owner of the reservation checked in."""


class ProductServiceOrder(BaseModel):
    account_id: str = FieldInfo(alias="AccountId")

    created_utc: datetime = FieldInfo(alias="CreatedUtc")

    creator_profile_id: str = FieldInfo(alias="CreatorProfileId")

    id: str = FieldInfo(alias="Id")

    options: ProductServiceOrderOptions = FieldInfo(alias="Options")

    origin: Literal["Distributor", "ChannelManager", "Commander", "Import", "Connector", "Navigator"] = FieldInfo(
        alias="Origin"
    )
    """
    - `Distributor` - From the Mews Booking Engine or Booking Engine API.
    - `ChannelManager` - From a channel manager.
    - `Commander` - From Mews Operations.
    - `Import` - From an import process.
    - `Connector` - From the Mews Connector API.
    - `Navigator` - From Mews Guest Services.
    """

    service_id: str = FieldInfo(alias="ServiceId")
    """
    Unique identifier of the
    [Service](https://mews-systems.gitbook.io/connector-api/operations/services#service)
    that service order is made against.
    """

    state: Literal["Inquired", "Confirmed", "Started", "Processed", "Canceled", "Optional", "Requested"] = FieldInfo(
        alias="State"
    )
    """
    - `Inquired` - Confirmed neither by the customer nor enterprise.
    - `Confirmed` - Confirmed by both parties, before check-in.
    - `Started` - Checked in.
    - `Processed` - Checked out.
    - `Canceled` - Canceled.
    - `Optional` - Confirmed by enterprise but not by the guest (the enterprise is
      holding resource for the guest).
    - `Requested` - Confirmed by the customer but not by the enterprise (waitlist).
    """

    updated_utc: datetime = FieldInfo(alias="UpdatedUtc")

    updater_profile_id: str = FieldInfo(alias="UpdaterProfileId")

    account_type: Optional[Literal["Company", "Customer"]] = FieldInfo(alias="AccountType", default=None)

    booker_id: Optional[str] = FieldInfo(alias="BookerId", default=None)

    business_segment_id: Optional[str] = FieldInfo(alias="BusinessSegmentId", default=None)

    cancelled_utc: Optional[datetime] = FieldInfo(alias="CancelledUtc", default=None)

    commander_origin: Optional[Literal["InPerson", "Channel", "Phone", "Email", "Website", "Message", "CallCenter"]] = (
        FieldInfo(alias="CommanderOrigin", default=None)
    )

    linked_reservation_id: Optional[str] = FieldInfo(alias="LinkedReservationId", default=None)

    number: Optional[str] = FieldInfo(alias="Number", default=None)

    origin_details: Optional[str] = FieldInfo(alias="OriginDetails", default=None)

    voucher_id: Optional[str] = FieldInfo(alias="VoucherId", default=None)


class V1ListProductServiceOrdersResponse(BaseModel):
    product_service_orders: List[ProductServiceOrder] = FieldInfo(alias="ProductServiceOrders")
    """The product service order of the enterprise."""

    cursor: Optional[str] = FieldInfo(alias="Cursor", default=None)
    """
    Unique identifier of the item one newer in time order than the items to be
    returned. If Cursor is not specified, i.e. null, then the latest or most recent
    items will be returned.
    """
