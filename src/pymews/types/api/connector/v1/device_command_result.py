# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["DeviceCommandResult", "Command", "CommandCreator", "CommandData", "CommandDevice"]


class CommandCreator(BaseModel):
    email: Optional[str] = FieldInfo(alias="Email", default=None)

    first_name: Optional[str] = FieldInfo(alias="FirstName", default=None)

    id: Optional[str] = FieldInfo(alias="Id", default=None)

    image_url: Optional[str] = FieldInfo(alias="ImageUrl", default=None)

    last_name: Optional[str] = FieldInfo(alias="LastName", default=None)

    last_successful_sign_in_utc: Optional[datetime] = FieldInfo(alias="LastSuccessfulSignInUtc", default=None)


class CommandData:
    pass


class CommandDevice(BaseModel):
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


class Command(BaseModel):
    created_utc: Optional[str] = FieldInfo(alias="CreatedUtc", default=None)

    creator: Optional[CommandCreator] = FieldInfo(alias="Creator", default=None)

    data: Optional[CommandData] = FieldInfo(alias="Data", default=None)

    device: Optional[CommandDevice] = FieldInfo(alias="Device", default=None)

    id: Optional[str] = FieldInfo(alias="Id", default=None)

    state: Optional[str] = FieldInfo(alias="State", default=None)


class DeviceCommandResult(BaseModel):
    commands: Optional[List[Command]] = FieldInfo(alias="Commands", default=None)

    cursor: Optional[str] = FieldInfo(alias="Cursor", default=None)
