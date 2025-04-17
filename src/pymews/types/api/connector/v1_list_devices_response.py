# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["V1ListDevicesResponse", "Device"]


class Device(BaseModel):
    id: str = FieldInfo(alias="Id")
    """Unique identifier of the device."""

    name: str = FieldInfo(alias="Name")
    """Name of the device."""

    type: Literal["Printer", "PaymentTerminal", "KeyCutter", "FiscalMachine", "PassportScanner"] = FieldInfo(
        alias="Type"
    )
    """Type of the device.

    Printer
    ([Printer command data](https://mews-systems.gitbook.io/connector-api/operations/commands#printer-command-data))

    PaymentTerminal
    ([Payment terminal command data](https://mews-systems.gitbook.io/connector-api/operations/commands#payment-terminal-command-data))

    KeyCutter
    ([Key cutter command data](https://mews-systems.gitbook.io/connector-api/operations/commands#key-cutter-command-data))

    FiscalMachine
    ([Fiscal machine command data](https://mews-systems.gitbook.io/connector-api/operations/commands#fiscal-machine-command-data))

    PassportScanner
    ([Passport scanner command data](https://mews-systems.gitbook.io/connector-api/operations/commands#passport-scanner-command-data))

    - `Printer` -
      [Printer command data](https://mews-systems.gitbook.io/connector-api/operations/commands#printer-command-data)
    - `PaymentTerminal` -
      [Payment terminal command data](https://mews-systems.gitbook.io/connector-api/operations/commands#payment-terminal-command-data)
    - `KeyCutter` -
      [Key cutter command data](https://mews-systems.gitbook.io/connector-api/operations/commands#key-cutter-command-data)
    - `FiscalMachine` -
      [Fiscal machine command data](https://mews-systems.gitbook.io/connector-api/operations/commands#fiscal-machine-command-data)
    - `PassportScanner` -
      [Passport scanner command data](https://mews-systems.gitbook.io/connector-api/operations/commands#passport-scanner-command-data)
    """

    identifier: Optional[str] = FieldInfo(alias="Identifier", default=None)
    """Device identifier (for internal purposes)."""


class V1ListDevicesResponse(BaseModel):
    devices: List[Device] = FieldInfo(alias="Devices")
    """The devices."""
