# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["V1GetImageURLsResponse", "ImageURL"]


class ImageURL(BaseModel):
    image_id: str = FieldInfo(alias="ImageId")
    """Unique identifier of the image."""

    url: str = FieldInfo(alias="Url")
    """URL of the image."""


class V1GetImageURLsResponse(BaseModel):
    image_urls: List[ImageURL] = FieldInfo(alias="ImageUrls")
    """URLs of the images."""
