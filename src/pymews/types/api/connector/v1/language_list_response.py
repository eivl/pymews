# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["LanguageListResponse", "Language"]


class Language(BaseModel):
    code: Optional[str] = FieldInfo(alias="Code", default=None)
    """Language-culture code of the language."""

    english_name: Optional[str] = FieldInfo(alias="EnglishName", default=None)
    """English name of the language."""

    fallback_language_code: Optional[str] = FieldInfo(alias="FallbackLanguageCode", default=None)
    """Language-culture code of the fallback language."""

    local_name: Optional[str] = FieldInfo(alias="LocalName", default=None)
    """Local name of the language."""


class LanguageListResponse(BaseModel):
    languages: Optional[List[Language]] = FieldInfo(alias="Languages", default=None)
    """The supported languages."""
