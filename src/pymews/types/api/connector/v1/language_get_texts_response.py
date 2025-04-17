# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["LanguageGetTextsResponse", "LanguageText"]


class LanguageText(BaseModel):
    language_code: Optional[str] = FieldInfo(alias="LanguageCode", default=None)
    """
    Language-culture code of the
    [Language](https://mews-systems.gitbook.io/connector-api/operations/#language).
    """

    texts: Optional[Dict[str, Optional[str]]] = FieldInfo(alias="Texts", default=None)
    """Texts in the specified language by their keys."""


class LanguageGetTextsResponse(BaseModel):
    language_texts: Optional[List[LanguageText]] = FieldInfo(alias="LanguageTexts", default=None)
    """Texts in the specified languages."""
