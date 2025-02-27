# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["V1GetImageURLsParams", "Image"]


class V1GetImageURLsParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    images: Required[Annotated[Iterable[Image], PropertyInfo(alias="Images")]]
    """Parameters of images whose URLs should be returned."""


class Image(TypedDict, total=False):
    image_id: Required[Annotated[str, PropertyInfo(alias="ImageId")]]
    """Unique identifier of the image."""

    height: Annotated[Optional[int], PropertyInfo(alias="Height")]
    """Desired height of the image."""

    resize_mode: Annotated[
        Optional[Literal["Cover", "CoverExact", "Fit", "FitExact"]], PropertyInfo(alias="ResizeMode")
    ]
    """
    Cover (Resize to fit within the specified size, so the result might be smaller
    than requested.)

    CoverExact (Resize and pad to exactly fit within the specified size.)

    Fit (Resize to fit within the specified size, so the result might be smaller
    than requested.)

    FitExact (Resize and pad to exactly fit within the specified size.)

    - `Cover` - Resize to fit within the specified size, so the result might be
      smaller than requested.
    - `CoverExact` - Resize and pad to exactly fit within the specified size.
    - `Fit` - Resize to fit within the specified size, so the result might be
      smaller than requested.
    - `FitExact` - Resize and pad to exactly fit within the specified size.
    """

    width: Annotated[Optional[int], PropertyInfo(alias="Width")]
    """Desired width of the image."""
