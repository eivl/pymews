# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .connector.connector import (
    ConnectorResource,
    AsyncConnectorResource,
    ConnectorResourceWithRawResponse,
    AsyncConnectorResourceWithRawResponse,
    ConnectorResourceWithStreamingResponse,
    AsyncConnectorResourceWithStreamingResponse,
)

__all__ = ["APIResource", "AsyncAPIResource"]


class APIResource(SyncAPIResource):
    @cached_property
    def connector(self) -> ConnectorResource:
        return ConnectorResource(self._client)

    @cached_property
    def with_raw_response(self) -> APIResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return APIResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> APIResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return APIResourceWithStreamingResponse(self)


class AsyncAPIResource(AsyncAPIResource):
    @cached_property
    def connector(self) -> AsyncConnectorResource:
        return AsyncConnectorResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAPIResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return AsyncAPIResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAPIResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return AsyncAPIResourceWithStreamingResponse(self)


class APIResourceWithRawResponse:
    def __init__(self, api: APIResource) -> None:
        self._api = api

    @cached_property
    def connector(self) -> ConnectorResourceWithRawResponse:
        return ConnectorResourceWithRawResponse(self._api.connector)


class AsyncAPIResourceWithRawResponse:
    def __init__(self, api: AsyncAPIResource) -> None:
        self._api = api

    @cached_property
    def connector(self) -> AsyncConnectorResourceWithRawResponse:
        return AsyncConnectorResourceWithRawResponse(self._api.connector)


class APIResourceWithStreamingResponse:
    def __init__(self, api: APIResource) -> None:
        self._api = api

    @cached_property
    def connector(self) -> ConnectorResourceWithStreamingResponse:
        return ConnectorResourceWithStreamingResponse(self._api.connector)


class AsyncAPIResourceWithStreamingResponse:
    def __init__(self, api: AsyncAPIResource) -> None:
        self._api = api

    @cached_property
    def connector(self) -> AsyncConnectorResourceWithStreamingResponse:
        return AsyncConnectorResourceWithStreamingResponse(self._api.connector)
