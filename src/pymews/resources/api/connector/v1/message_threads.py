# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

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
from .....types.api.connector.v1 import message_thread_add_params, message_thread_list_params
from .....types.api.connector.v1.message_thread_result import MessageThreadResult

__all__ = ["MessageThreadsResource", "AsyncMessageThreadsResource"]


class MessageThreadsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MessageThreadsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return MessageThreadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MessageThreadsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return MessageThreadsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: message_thread_list_params.Limitation,
        created_utc: Optional[message_thread_list_params.CreatedUtc] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        message_thread_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[message_thread_list_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessageThreadResult:
        """
        Get all message threads that you have created, filtered by time interval and/or
        specific message thread IDs. Note this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          message_thread_ids: Unique identifiers of
              [Message threads](https://mews-systems.gitbook.io/connector-api/operations/#message-thread).
              Required if no other filter is provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/messageThreads/getAll",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "created_utc": created_utc,
                    "enterprise_ids": enterprise_ids,
                    "message_thread_ids": message_thread_ids,
                    "updated_utc": updated_utc,
                },
                message_thread_list_params.MessageThreadListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageThreadResult,
        )

    def add(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        original_sender: str,
        subject: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessageThreadResult:
        """
        Creates a new
        [Message thread](https://mews-systems.gitbook.io/connector-api/operations/#message-thread)
        on behalf of the specified customer, i.e. the sender of the original message in
        the message thread.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          original_sender: The sender of the original message in the thread.

          subject: Subject of the message thread.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/messageThreads/add",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "original_sender": original_sender,
                    "subject": subject,
                },
                message_thread_add_params.MessageThreadAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageThreadResult,
        )


class AsyncMessageThreadsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMessageThreadsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return AsyncMessageThreadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMessageThreadsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return AsyncMessageThreadsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: message_thread_list_params.Limitation,
        created_utc: Optional[message_thread_list_params.CreatedUtc] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        message_thread_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[message_thread_list_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessageThreadResult:
        """
        Get all message threads that you have created, filtered by time interval and/or
        specific message thread IDs. Note this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          message_thread_ids: Unique identifiers of
              [Message threads](https://mews-systems.gitbook.io/connector-api/operations/#message-thread).
              Required if no other filter is provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/messageThreads/getAll",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "created_utc": created_utc,
                    "enterprise_ids": enterprise_ids,
                    "message_thread_ids": message_thread_ids,
                    "updated_utc": updated_utc,
                },
                message_thread_list_params.MessageThreadListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageThreadResult,
        )

    async def add(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        original_sender: str,
        subject: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessageThreadResult:
        """
        Creates a new
        [Message thread](https://mews-systems.gitbook.io/connector-api/operations/#message-thread)
        on behalf of the specified customer, i.e. the sender of the original message in
        the message thread.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          original_sender: The sender of the original message in the thread.

          subject: Subject of the message thread.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/messageThreads/add",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "original_sender": original_sender,
                    "subject": subject,
                },
                message_thread_add_params.MessageThreadAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageThreadResult,
        )


class MessageThreadsResourceWithRawResponse:
    def __init__(self, message_threads: MessageThreadsResource) -> None:
        self._message_threads = message_threads

        self.list = to_raw_response_wrapper(
            message_threads.list,
        )
        self.add = to_raw_response_wrapper(
            message_threads.add,
        )


class AsyncMessageThreadsResourceWithRawResponse:
    def __init__(self, message_threads: AsyncMessageThreadsResource) -> None:
        self._message_threads = message_threads

        self.list = async_to_raw_response_wrapper(
            message_threads.list,
        )
        self.add = async_to_raw_response_wrapper(
            message_threads.add,
        )


class MessageThreadsResourceWithStreamingResponse:
    def __init__(self, message_threads: MessageThreadsResource) -> None:
        self._message_threads = message_threads

        self.list = to_streamed_response_wrapper(
            message_threads.list,
        )
        self.add = to_streamed_response_wrapper(
            message_threads.add,
        )


class AsyncMessageThreadsResourceWithStreamingResponse:
    def __init__(self, message_threads: AsyncMessageThreadsResource) -> None:
        self._message_threads = message_threads

        self.list = async_to_streamed_response_wrapper(
            message_threads.list,
        )
        self.add = async_to_streamed_response_wrapper(
            message_threads.add,
        )
