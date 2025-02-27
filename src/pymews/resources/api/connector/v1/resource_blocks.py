# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.api.connector.v1 import (
    resource_block_add_params,
    resource_block_list_params,
    resource_block_delete_params,
)
from .....types.api.connector.v1.resource_block_result import ResourceBlockResult

__all__ = ["ResourceBlocksResource", "AsyncResourceBlocksResource"]


class ResourceBlocksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ResourceBlocksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return ResourceBlocksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResourceBlocksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return ResourceBlocksResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        extent: resource_block_list_params.Extent,
        limitation: resource_block_list_params.Limitation,
        assigned_resource_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        colliding_utc: Optional[resource_block_list_params.CollidingUtc] | NotGiven = NOT_GIVEN,
        created_utc: Optional[resource_block_list_params.CreatedUtc] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        resource_block_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[resource_block_list_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResourceBlockResult:
        """Returns all resource blocks (out of order blocks or internal use blocks).

        Note
        this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          extent: Extent of data to be returned.

          limitation: Limitation on the quantity of data returned.

          assigned_resource_ids: Unique identifiers of the requested Assigned
              [Resources](https://mews-systems.gitbook.io/connector-api/operations/resources/#resource).

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          resource_block_ids: Unique identifiers of the requested
              [Resource blocks](https://mews-systems.gitbook.io/connector-api/operations/#resource-block).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/resourceBlocks/getAll",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "extent": extent,
                    "limitation": limitation,
                    "assigned_resource_ids": assigned_resource_ids,
                    "colliding_utc": colliding_utc,
                    "created_utc": created_utc,
                    "enterprise_ids": enterprise_ids,
                    "resource_block_ids": resource_block_ids,
                    "updated_utc": updated_utc,
                },
                resource_block_list_params.ResourceBlockListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResourceBlockResult,
        )

    def delete(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        resource_block_ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Removes specified resource blocks from the resources.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          resource_block_ids: Unique identifier of
              [Resource blocks](https://mews-systems.gitbook.io/connector-api/operations/#resource-block)
              to be removed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/resourceBlocks/delete",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "resource_block_ids": resource_block_ids,
                },
                resource_block_delete_params.ResourceBlockDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def add(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        resource_blocks: Iterable[resource_block_add_params.ResourceBlock],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResourceBlockResult:
        """
        Adds a new resource block to the specified resource for a defined period of
        time.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          resource_blocks: Resource block parameters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/resourceBlocks/add",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "resource_blocks": resource_blocks,
                },
                resource_block_add_params.ResourceBlockAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResourceBlockResult,
        )


class AsyncResourceBlocksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncResourceBlocksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return AsyncResourceBlocksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResourceBlocksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return AsyncResourceBlocksResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        extent: resource_block_list_params.Extent,
        limitation: resource_block_list_params.Limitation,
        assigned_resource_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        colliding_utc: Optional[resource_block_list_params.CollidingUtc] | NotGiven = NOT_GIVEN,
        created_utc: Optional[resource_block_list_params.CreatedUtc] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        resource_block_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[resource_block_list_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResourceBlockResult:
        """Returns all resource blocks (out of order blocks or internal use blocks).

        Note
        this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          extent: Extent of data to be returned.

          limitation: Limitation on the quantity of data returned.

          assigned_resource_ids: Unique identifiers of the requested Assigned
              [Resources](https://mews-systems.gitbook.io/connector-api/operations/resources/#resource).

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          resource_block_ids: Unique identifiers of the requested
              [Resource blocks](https://mews-systems.gitbook.io/connector-api/operations/#resource-block).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/resourceBlocks/getAll",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "extent": extent,
                    "limitation": limitation,
                    "assigned_resource_ids": assigned_resource_ids,
                    "colliding_utc": colliding_utc,
                    "created_utc": created_utc,
                    "enterprise_ids": enterprise_ids,
                    "resource_block_ids": resource_block_ids,
                    "updated_utc": updated_utc,
                },
                resource_block_list_params.ResourceBlockListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResourceBlockResult,
        )

    async def delete(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        resource_block_ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Removes specified resource blocks from the resources.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          resource_block_ids: Unique identifier of
              [Resource blocks](https://mews-systems.gitbook.io/connector-api/operations/#resource-block)
              to be removed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/resourceBlocks/delete",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "resource_block_ids": resource_block_ids,
                },
                resource_block_delete_params.ResourceBlockDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def add(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        resource_blocks: Iterable[resource_block_add_params.ResourceBlock],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResourceBlockResult:
        """
        Adds a new resource block to the specified resource for a defined period of
        time.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          resource_blocks: Resource block parameters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/resourceBlocks/add",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "resource_blocks": resource_blocks,
                },
                resource_block_add_params.ResourceBlockAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResourceBlockResult,
        )


class ResourceBlocksResourceWithRawResponse:
    def __init__(self, resource_blocks: ResourceBlocksResource) -> None:
        self._resource_blocks = resource_blocks

        self.list = to_raw_response_wrapper(
            resource_blocks.list,
        )
        self.delete = to_raw_response_wrapper(
            resource_blocks.delete,
        )
        self.add = to_raw_response_wrapper(
            resource_blocks.add,
        )


class AsyncResourceBlocksResourceWithRawResponse:
    def __init__(self, resource_blocks: AsyncResourceBlocksResource) -> None:
        self._resource_blocks = resource_blocks

        self.list = async_to_raw_response_wrapper(
            resource_blocks.list,
        )
        self.delete = async_to_raw_response_wrapper(
            resource_blocks.delete,
        )
        self.add = async_to_raw_response_wrapper(
            resource_blocks.add,
        )


class ResourceBlocksResourceWithStreamingResponse:
    def __init__(self, resource_blocks: ResourceBlocksResource) -> None:
        self._resource_blocks = resource_blocks

        self.list = to_streamed_response_wrapper(
            resource_blocks.list,
        )
        self.delete = to_streamed_response_wrapper(
            resource_blocks.delete,
        )
        self.add = to_streamed_response_wrapper(
            resource_blocks.add,
        )


class AsyncResourceBlocksResourceWithStreamingResponse:
    def __init__(self, resource_blocks: AsyncResourceBlocksResource) -> None:
        self._resource_blocks = resource_blocks

        self.list = async_to_streamed_response_wrapper(
            resource_blocks.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            resource_blocks.delete,
        )
        self.add = async_to_streamed_response_wrapper(
            resource_blocks.add,
        )
