# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["TaskAddResponse"]


class TaskAddResponse(BaseModel):
    task_id: Optional[str] = FieldInfo(alias="TaskId", default=None)
    """Unique identifier of added task."""
