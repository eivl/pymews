# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "V1ListCountersResponse",
    "BillCounter",
    "BillPreviewCounter",
    "Counter",
    "ProformaCounter",
    "RegistrationCardCounter",
    "ServiceOrderCounter",
]


class BillCounter(BaseModel):
    created_utc: datetime = FieldInfo(alias="CreatedUtc")
    """Creation date and time of the counter in UTC timezone in ISO 8601 format."""

    enterprise_id: str = FieldInfo(alias="EnterpriseId")

    format: str = FieldInfo(alias="Format")
    """Format the counter is displayed in."""

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the counter."""

    is_default: bool = FieldInfo(alias="IsDefault")
    """Whether the counter is used by default."""

    name: str = FieldInfo(alias="Name")
    """Name of the counter."""

    type: Literal[
        "Counter",
        "AccountingCounter",
        "AvailabilityBlockCounter",
        "BillCounter",
        "BillPreviewCounter",
        "FiscalCounter",
        "ProformaCounter",
        "RegistrationCardCounter",
        "ServiceOrderCounter",
        "CorrectionBillCounter",
        "PaymentConfirmationBillCounter",
        "CreditNoteBillCounter",
    ] = FieldInfo(alias="Type")

    updated_utc: datetime = FieldInfo(alias="UpdatedUtc")
    """Last update date and time of the counter in UTC timezone in ISO 8601 format."""

    value: int = FieldInfo(alias="Value")
    """Current value the counter."""


class BillPreviewCounter(BaseModel):
    created_utc: datetime = FieldInfo(alias="CreatedUtc")
    """Creation date and time of the counter in UTC timezone in ISO 8601 format."""

    enterprise_id: str = FieldInfo(alias="EnterpriseId")

    format: str = FieldInfo(alias="Format")
    """Format the counter is displayed in."""

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the counter."""

    is_default: bool = FieldInfo(alias="IsDefault")
    """Whether the counter is used by default."""

    name: str = FieldInfo(alias="Name")
    """Name of the counter."""

    type: Literal[
        "Counter",
        "AccountingCounter",
        "AvailabilityBlockCounter",
        "BillCounter",
        "BillPreviewCounter",
        "FiscalCounter",
        "ProformaCounter",
        "RegistrationCardCounter",
        "ServiceOrderCounter",
        "CorrectionBillCounter",
        "PaymentConfirmationBillCounter",
        "CreditNoteBillCounter",
    ] = FieldInfo(alias="Type")

    updated_utc: datetime = FieldInfo(alias="UpdatedUtc")
    """Last update date and time of the counter in UTC timezone in ISO 8601 format."""

    value: int = FieldInfo(alias="Value")
    """Current value the counter."""


class Counter(BaseModel):
    created_utc: datetime = FieldInfo(alias="CreatedUtc")
    """Creation date and time of the counter in UTC timezone in ISO 8601 format."""

    enterprise_id: str = FieldInfo(alias="EnterpriseId")

    format: str = FieldInfo(alias="Format")
    """Format the counter is displayed in."""

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the counter."""

    is_default: bool = FieldInfo(alias="IsDefault")
    """Whether the counter is used by default."""

    name: str = FieldInfo(alias="Name")
    """Name of the counter."""

    type: Literal[
        "Counter",
        "AccountingCounter",
        "AvailabilityBlockCounter",
        "BillCounter",
        "BillPreviewCounter",
        "FiscalCounter",
        "ProformaCounter",
        "RegistrationCardCounter",
        "ServiceOrderCounter",
        "CorrectionBillCounter",
        "PaymentConfirmationBillCounter",
        "CreditNoteBillCounter",
    ] = FieldInfo(alias="Type")

    updated_utc: datetime = FieldInfo(alias="UpdatedUtc")
    """Last update date and time of the counter in UTC timezone in ISO 8601 format."""

    value: int = FieldInfo(alias="Value")
    """Current value the counter."""


class ProformaCounter(BaseModel):
    created_utc: datetime = FieldInfo(alias="CreatedUtc")
    """Creation date and time of the counter in UTC timezone in ISO 8601 format."""

    enterprise_id: str = FieldInfo(alias="EnterpriseId")

    format: str = FieldInfo(alias="Format")
    """Format the counter is displayed in."""

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the counter."""

    is_default: bool = FieldInfo(alias="IsDefault")
    """Whether the counter is used by default."""

    name: str = FieldInfo(alias="Name")
    """Name of the counter."""

    type: Literal[
        "Counter",
        "AccountingCounter",
        "AvailabilityBlockCounter",
        "BillCounter",
        "BillPreviewCounter",
        "FiscalCounter",
        "ProformaCounter",
        "RegistrationCardCounter",
        "ServiceOrderCounter",
        "CorrectionBillCounter",
        "PaymentConfirmationBillCounter",
        "CreditNoteBillCounter",
    ] = FieldInfo(alias="Type")

    updated_utc: datetime = FieldInfo(alias="UpdatedUtc")
    """Last update date and time of the counter in UTC timezone in ISO 8601 format."""

    value: int = FieldInfo(alias="Value")
    """Current value the counter."""


class RegistrationCardCounter(BaseModel):
    created_utc: datetime = FieldInfo(alias="CreatedUtc")
    """Creation date and time of the counter in UTC timezone in ISO 8601 format."""

    enterprise_id: str = FieldInfo(alias="EnterpriseId")

    format: str = FieldInfo(alias="Format")
    """Format the counter is displayed in."""

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the counter."""

    is_default: bool = FieldInfo(alias="IsDefault")
    """Whether the counter is used by default."""

    name: str = FieldInfo(alias="Name")
    """Name of the counter."""

    type: Literal[
        "Counter",
        "AccountingCounter",
        "AvailabilityBlockCounter",
        "BillCounter",
        "BillPreviewCounter",
        "FiscalCounter",
        "ProformaCounter",
        "RegistrationCardCounter",
        "ServiceOrderCounter",
        "CorrectionBillCounter",
        "PaymentConfirmationBillCounter",
        "CreditNoteBillCounter",
    ] = FieldInfo(alias="Type")

    updated_utc: datetime = FieldInfo(alias="UpdatedUtc")
    """Last update date and time of the counter in UTC timezone in ISO 8601 format."""

    value: int = FieldInfo(alias="Value")
    """Current value the counter."""


class ServiceOrderCounter(BaseModel):
    created_utc: datetime = FieldInfo(alias="CreatedUtc")
    """Creation date and time of the counter in UTC timezone in ISO 8601 format."""

    enterprise_id: str = FieldInfo(alias="EnterpriseId")

    format: str = FieldInfo(alias="Format")
    """Format the counter is displayed in."""

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the counter."""

    is_default: bool = FieldInfo(alias="IsDefault")
    """Whether the counter is used by default."""

    name: str = FieldInfo(alias="Name")
    """Name of the counter."""

    type: Literal[
        "Counter",
        "AccountingCounter",
        "AvailabilityBlockCounter",
        "BillCounter",
        "BillPreviewCounter",
        "FiscalCounter",
        "ProformaCounter",
        "RegistrationCardCounter",
        "ServiceOrderCounter",
        "CorrectionBillCounter",
        "PaymentConfirmationBillCounter",
        "CreditNoteBillCounter",
    ] = FieldInfo(alias="Type")

    updated_utc: datetime = FieldInfo(alias="UpdatedUtc")
    """Last update date and time of the counter in UTC timezone in ISO 8601 format."""

    value: int = FieldInfo(alias="Value")
    """Current value the counter."""


class V1ListCountersResponse(BaseModel):
    bill_counters: List[BillCounter] = FieldInfo(alias="BillCounters")
    """
    The counters used to count closed
    [Bills](https://mews-systems.gitbook.io/connector-api/operations/bills/#bill).
    **Deprecated!**
    """

    bill_preview_counters: List[BillPreviewCounter] = FieldInfo(alias="BillPreviewCounters")
    """
    The counters used to count bill previews for
    [Bills](https://mews-systems.gitbook.io/connector-api/operations/bills/#bill).
    **Deprecated!**
    """

    counters: List[Counter] = FieldInfo(alias="Counters")
    """All types of counters."""

    proforma_counters: List[ProformaCounter] = FieldInfo(alias="ProformaCounters")
    """
    The counters used to count Pro Forma invoices for
    [Bills](https://mews-systems.gitbook.io/connector-api/operations/bills/#bill).
    **Deprecated!**
    """

    registration_card_counters: List[RegistrationCardCounter] = FieldInfo(alias="RegistrationCardCounters")
    """The counters used to count registration cards. **Deprecated!**"""

    service_order_counters: List[ServiceOrderCounter] = FieldInfo(alias="ServiceOrderCounters")
    """The counters used to count service orders (for example reservations).

    **Deprecated!**
    """

    cursor: Optional[str] = FieldInfo(alias="Cursor", default=None)
