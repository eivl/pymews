# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal

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
    availability_block_add_params,
    availability_block_list_params,
    availability_block_delete_params,
    availability_block_update_params,
)
from .....types.api.connector.v1.availability_block_add_result import AvailabilityBlockAddResult
from .....types.api.connector.v1.availability_block_list_response import AvailabilityBlockListResponse

__all__ = ["AvailabilityBlocksResource", "AsyncAvailabilityBlocksResource"]


class AvailabilityBlocksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AvailabilityBlocksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return AvailabilityBlocksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AvailabilityBlocksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return AvailabilityBlocksResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        access_token: str,
        availability_blocks: Iterable[availability_block_update_params.AvailabilityBlock],
        client: str,
        client_token: str,
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AvailabilityBlockAddResult:
        """Updates information about the specified `Availability block`.

        Note this
        operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        Args:
          access_token: Access token of the client application.

          availability_blocks: Availability blocks to be updated.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/availabilityBlocks/update",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "availability_blocks": availability_blocks,
                    "client": client,
                    "client_token": client_token,
                    "enterprise_id": enterprise_id,
                },
                availability_block_update_params.AvailabilityBlockUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AvailabilityBlockAddResult,
        )

    def list(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        extent: availability_block_list_params.Extent,
        limitation: availability_block_list_params.Limitation,
        activity_states: Optional[List[str]] | NotGiven = NOT_GIVEN,
        availability_block_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        colliding_utc: Optional[availability_block_list_params.CollidingUtc] | NotGiven = NOT_GIVEN,
        created_utc: Optional[availability_block_list_params.CreatedUtc] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        external_identifiers: Optional[List[str]] | NotGiven = NOT_GIVEN,
        released_utc: Optional[availability_block_list_params.ReleasedUtc] | NotGiven = NOT_GIVEN,
        service_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        states: Optional[List[Literal["Confirmed", "Optional", "Inquired", "Canceled"]]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[availability_block_list_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AvailabilityBlockListResponse:
        """
        Returns all availability blocks filtered by services, unique identifiers and
        other filters. Note this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          extent

          limitation: Limitation on the quantity of data returned.

          activity_states: Whether to return only active, only deleted or both records.

          availability_block_ids: Unique identifiers of the requested `Availability blocks`.

          colliding_utc: Interval in which the `Availability blocks` are active.

          created_utc: Interval in which the availability blocks were created.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          external_identifiers: Identifiers of `Availability blocks` from external systems.

          released_utc: Interval in which the `Availability blocks`are released.

          service_ids: Unique identifiers of the `Services` to which `Availability blocks` are
              assigned.

          states: States the availability blocks should be in.

          updated_utc: Interval in which the `Availability blocks` were updated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/availabilityBlocks/getAll",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "extent": extent,
                    "limitation": limitation,
                    "activity_states": activity_states,
                    "availability_block_ids": availability_block_ids,
                    "colliding_utc": colliding_utc,
                    "created_utc": created_utc,
                    "enterprise_ids": enterprise_ids,
                    "external_identifiers": external_identifiers,
                    "released_utc": released_utc,
                    "service_ids": service_ids,
                    "states": states,
                    "updated_utc": updated_utc,
                },
                availability_block_list_params.AvailabilityBlockListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AvailabilityBlockListResponse,
        )

    def delete(
        self,
        *,
        access_token: str,
        availability_block_ids: List[str],
        client: str,
        client_token: str,
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Delete availability blocks.

        Note that an availability block containing active
        reservations (reservations which are not Canceled) cannot be deleted. Note this
        operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        Args:
          access_token: Access token of the client application.

          availability_block_ids: Unique identifier of the Availability block to delete.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/availabilityBlocks/delete",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "availability_block_ids": availability_block_ids,
                    "client": client,
                    "client_token": client_token,
                    "enterprise_id": enterprise_id,
                },
                availability_block_delete_params.AvailabilityBlockDeleteParams,
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
        availability_blocks: Iterable[availability_block_add_params.AvailabilityBlock],
        client: str,
        client_token: str,
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AvailabilityBlockAddResult:
        """
        Adds availability blocks which are used to group related `Availability updates`.
        This makes limiting public availability easier and more organized. Note this
        operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        Args:
          access_token: Access token of the client application.

          availability_blocks: Availability blocks to be added.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/availabilityBlocks/add",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "availability_blocks": availability_blocks,
                    "client": client,
                    "client_token": client_token,
                    "enterprise_id": enterprise_id,
                },
                availability_block_add_params.AvailabilityBlockAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AvailabilityBlockAddResult,
        )


class AsyncAvailabilityBlocksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAvailabilityBlocksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return AsyncAvailabilityBlocksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAvailabilityBlocksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return AsyncAvailabilityBlocksResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        access_token: str,
        availability_blocks: Iterable[availability_block_update_params.AvailabilityBlock],
        client: str,
        client_token: str,
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AvailabilityBlockAddResult:
        """Updates information about the specified `Availability block`.

        Note this
        operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        Args:
          access_token: Access token of the client application.

          availability_blocks: Availability blocks to be updated.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/availabilityBlocks/update",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "availability_blocks": availability_blocks,
                    "client": client,
                    "client_token": client_token,
                    "enterprise_id": enterprise_id,
                },
                availability_block_update_params.AvailabilityBlockUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AvailabilityBlockAddResult,
        )

    async def list(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        extent: availability_block_list_params.Extent,
        limitation: availability_block_list_params.Limitation,
        activity_states: Optional[List[str]] | NotGiven = NOT_GIVEN,
        availability_block_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        colliding_utc: Optional[availability_block_list_params.CollidingUtc] | NotGiven = NOT_GIVEN,
        created_utc: Optional[availability_block_list_params.CreatedUtc] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        external_identifiers: Optional[List[str]] | NotGiven = NOT_GIVEN,
        released_utc: Optional[availability_block_list_params.ReleasedUtc] | NotGiven = NOT_GIVEN,
        service_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        states: Optional[List[Literal["Confirmed", "Optional", "Inquired", "Canceled"]]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[availability_block_list_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AvailabilityBlockListResponse:
        """
        Returns all availability blocks filtered by services, unique identifiers and
        other filters. Note this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          extent

          limitation: Limitation on the quantity of data returned.

          activity_states: Whether to return only active, only deleted or both records.

          availability_block_ids: Unique identifiers of the requested `Availability blocks`.

          colliding_utc: Interval in which the `Availability blocks` are active.

          created_utc: Interval in which the availability blocks were created.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          external_identifiers: Identifiers of `Availability blocks` from external systems.

          released_utc: Interval in which the `Availability blocks`are released.

          service_ids: Unique identifiers of the `Services` to which `Availability blocks` are
              assigned.

          states: States the availability blocks should be in.

          updated_utc: Interval in which the `Availability blocks` were updated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/availabilityBlocks/getAll",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "extent": extent,
                    "limitation": limitation,
                    "activity_states": activity_states,
                    "availability_block_ids": availability_block_ids,
                    "colliding_utc": colliding_utc,
                    "created_utc": created_utc,
                    "enterprise_ids": enterprise_ids,
                    "external_identifiers": external_identifiers,
                    "released_utc": released_utc,
                    "service_ids": service_ids,
                    "states": states,
                    "updated_utc": updated_utc,
                },
                availability_block_list_params.AvailabilityBlockListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AvailabilityBlockListResponse,
        )

    async def delete(
        self,
        *,
        access_token: str,
        availability_block_ids: List[str],
        client: str,
        client_token: str,
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Delete availability blocks.

        Note that an availability block containing active
        reservations (reservations which are not Canceled) cannot be deleted. Note this
        operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        Args:
          access_token: Access token of the client application.

          availability_block_ids: Unique identifier of the Availability block to delete.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/availabilityBlocks/delete",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "availability_block_ids": availability_block_ids,
                    "client": client,
                    "client_token": client_token,
                    "enterprise_id": enterprise_id,
                },
                availability_block_delete_params.AvailabilityBlockDeleteParams,
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
        availability_blocks: Iterable[availability_block_add_params.AvailabilityBlock],
        client: str,
        client_token: str,
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AvailabilityBlockAddResult:
        """
        Adds availability blocks which are used to group related `Availability updates`.
        This makes limiting public availability easier and more organized. Note this
        operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        Args:
          access_token: Access token of the client application.

          availability_blocks: Availability blocks to be added.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/availabilityBlocks/add",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "availability_blocks": availability_blocks,
                    "client": client,
                    "client_token": client_token,
                    "enterprise_id": enterprise_id,
                },
                availability_block_add_params.AvailabilityBlockAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AvailabilityBlockAddResult,
        )


class AvailabilityBlocksResourceWithRawResponse:
    def __init__(self, availability_blocks: AvailabilityBlocksResource) -> None:
        self._availability_blocks = availability_blocks

        self.update = to_raw_response_wrapper(
            availability_blocks.update,
        )
        self.list = to_raw_response_wrapper(
            availability_blocks.list,
        )
        self.delete = to_raw_response_wrapper(
            availability_blocks.delete,
        )
        self.add = to_raw_response_wrapper(
            availability_blocks.add,
        )


class AsyncAvailabilityBlocksResourceWithRawResponse:
    def __init__(self, availability_blocks: AsyncAvailabilityBlocksResource) -> None:
        self._availability_blocks = availability_blocks

        self.update = async_to_raw_response_wrapper(
            availability_blocks.update,
        )
        self.list = async_to_raw_response_wrapper(
            availability_blocks.list,
        )
        self.delete = async_to_raw_response_wrapper(
            availability_blocks.delete,
        )
        self.add = async_to_raw_response_wrapper(
            availability_blocks.add,
        )


class AvailabilityBlocksResourceWithStreamingResponse:
    def __init__(self, availability_blocks: AvailabilityBlocksResource) -> None:
        self._availability_blocks = availability_blocks

        self.update = to_streamed_response_wrapper(
            availability_blocks.update,
        )
        self.list = to_streamed_response_wrapper(
            availability_blocks.list,
        )
        self.delete = to_streamed_response_wrapper(
            availability_blocks.delete,
        )
        self.add = to_streamed_response_wrapper(
            availability_blocks.add,
        )


class AsyncAvailabilityBlocksResourceWithStreamingResponse:
    def __init__(self, availability_blocks: AsyncAvailabilityBlocksResource) -> None:
        self._availability_blocks = availability_blocks

        self.update = async_to_streamed_response_wrapper(
            availability_blocks.update,
        )
        self.list = async_to_streamed_response_wrapper(
            availability_blocks.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            availability_blocks.delete,
        )
        self.add = async_to_streamed_response_wrapper(
            availability_blocks.add,
        )
