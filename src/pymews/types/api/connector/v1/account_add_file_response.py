# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["AccountAddFileResponse"]


class AccountAddFileResponse(BaseModel):
    file_id: str = FieldInfo(alias="FileId")
    """Unique identifier of the uploaded file."""
