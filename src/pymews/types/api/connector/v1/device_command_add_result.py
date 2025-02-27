# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["DeviceCommandAddResult"]


class DeviceCommandAddResult(BaseModel):
    command_id: Optional[str] = FieldInfo(alias="CommandId", default=None)
    """
    Unique identifier of the created
    [Command](https://mews-systems.gitbook.io/connector-api/operations/#command).
    """
