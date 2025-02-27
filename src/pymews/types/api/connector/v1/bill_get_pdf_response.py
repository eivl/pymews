# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["BillGetPdfResponse", "Result", "ResultValue", "ResultValueBillPdfFile", "ResultValueBillPrintEvent"]


class ResultValueBillPdfFile(BaseModel):
    base64_data: str = FieldInfo(alias="Base64Data")
    """Base64 encoded PDF file."""


class ResultValueBillPrintEvent(BaseModel):
    bill_print_event_id: Optional[str] = FieldInfo(alias="BillPrintEventId", default=None)
    """Unique identifier of print event.

    Must be used in retry calls to retrieve the PDF.
    """


ResultValue: TypeAlias = Union[ResultValueBillPdfFile, ResultValueBillPrintEvent]


class Result(BaseModel):
    discriminator: Optional[Literal["BillPdfFile", "BillPrintEvent"]] = None
    """The result of operation.

    - `BillPdfFile` - PDF version of a `Bill` was successfully created, `Value` is
      `BillPdfFile`.
    - `BillPrintEvent` - PDF version of a `Bill` couldn't be created at this moment
      (for example bill haven't been reported to authorities yet), `Value` is
      `BillPrintEvent`
    """

    value: Optional[ResultValue] = None


class BillGetPdfResponse(BaseModel):
    bill_id: Optional[str] = FieldInfo(alias="BillId", default=None)
    """Unique identifier of the printed bill."""

    result: Optional[Result] = FieldInfo(alias="Result", default=None)
