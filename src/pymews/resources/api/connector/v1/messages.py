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
from .....types.api.connector.v1 import message_add_params, message_list_params
from .....types.api.connector.v1.message_add_response import MessageAddResponse
from .....types.api.connector.v1.message_list_response import MessageListResponse

__all__ = ["MessagesResource", "AsyncMessagesResource"]


class MessagesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return MessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return MessagesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: message_list_params.Limitation,
        message_thread_ids: List[str],
        created_utc: Optional[message_list_params.CreatedUtc] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessageListResponse:
        """
        Get all messages belonging to the specified
        [Message threads](https://mews-systems.gitbook.io/connector-api/operations/messagethreads/#message-thread).
        Messages can only be returned for message threads you have created. Note this
        operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          message_thread_ids: Unique identifiers of
              [Message threads](https://mews-systems.gitbook.io/connector-api/operations/messagethreads/#message-thread)
              from where to return messages.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/messages/getAll",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "message_thread_ids": message_thread_ids,
                    "created_utc": created_utc,
                    "enterprise_ids": enterprise_ids,
                },
                message_list_params.MessageListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageListResponse,
        )

    def add(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        messages: Iterable[message_add_params.Message],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessageAddResponse:
        """
        Add the specified messages to the specified
        [Message threads](https://mews-systems.gitbook.io/connector-api/operations/messagethreads/#message-thread).
        You can only add messages to message threads that you have created.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          messages: Messages to be added.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/messages/add",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "messages": messages,
                },
                message_add_params.MessageAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageAddResponse,
        )


class AsyncMessagesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return AsyncMessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return AsyncMessagesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: message_list_params.Limitation,
        message_thread_ids: List[str],
        created_utc: Optional[message_list_params.CreatedUtc] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessageListResponse:
        """
        Get all messages belonging to the specified
        [Message threads](https://mews-systems.gitbook.io/connector-api/operations/messagethreads/#message-thread).
        Messages can only be returned for message threads you have created. Note this
        operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          message_thread_ids: Unique identifiers of
              [Message threads](https://mews-systems.gitbook.io/connector-api/operations/messagethreads/#message-thread)
              from where to return messages.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/messages/getAll",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "message_thread_ids": message_thread_ids,
                    "created_utc": created_utc,
                    "enterprise_ids": enterprise_ids,
                },
                message_list_params.MessageListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageListResponse,
        )

    async def add(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        messages: Iterable[message_add_params.Message],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessageAddResponse:
        """
        Add the specified messages to the specified
        [Message threads](https://mews-systems.gitbook.io/connector-api/operations/messagethreads/#message-thread).
        You can only add messages to message threads that you have created.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          messages: Messages to be added.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/messages/add",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "messages": messages,
                },
                message_add_params.MessageAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageAddResponse,
        )


class MessagesResourceWithRawResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.list = to_raw_response_wrapper(
            messages.list,
        )
        self.add = to_raw_response_wrapper(
            messages.add,
        )


class AsyncMessagesResourceWithRawResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.list = async_to_raw_response_wrapper(
            messages.list,
        )
        self.add = async_to_raw_response_wrapper(
            messages.add,
        )


class MessagesResourceWithStreamingResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.list = to_streamed_response_wrapper(
            messages.list,
        )
        self.add = to_streamed_response_wrapper(
            messages.add,
        )


class AsyncMessagesResourceWithStreamingResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.list = async_to_streamed_response_wrapper(
            messages.list,
        )
        self.add = async_to_streamed_response_wrapper(
            messages.add,
        )
