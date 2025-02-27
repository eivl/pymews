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
    resource_access_token_add_params,
    resource_access_token_list_params,
    resource_access_token_delete_params,
    resource_access_token_update_params,
)
from .....types.api.connector.v1.resource_access_token_result import ResourceAccessTokenResult

__all__ = ["ResourceAccessTokensResource", "AsyncResourceAccessTokensResource"]


class ResourceAccessTokensResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ResourceAccessTokensResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return ResourceAccessTokensResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResourceAccessTokensResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return ResourceAccessTokensResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        resource_access_token_updates: Optional[Iterable[resource_access_token_update_params.ResourceAccessTokenUpdate]]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResourceAccessTokenResult:
        """
        Updates the
        [Resource access token](https://mews-systems.gitbook.io/connector-api/operations/#resource-access-token)
        validity interval and
        [permissions](https://mews-systems.gitbook.io/connector-api/operations/#resource-access-token-permission-parameter)
        that it grants.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          resource_access_token_updates: Parameters of
              [Resource access token](https://mews-systems.gitbook.io/connector-api/operations/#resource-access-token).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/resourceAccessTokens/update",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "enterprise_id": enterprise_id,
                    "resource_access_token_updates": resource_access_token_updates,
                },
                resource_access_token_update_params.ResourceAccessTokenUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResourceAccessTokenResult,
        )

    def list(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: resource_access_token_list_params.Limitation,
        activity_states: Optional[List[str]] | NotGiven = NOT_GIVEN,
        colliding_utc: Optional[resource_access_token_list_params.CollidingUtc] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        resource_access_token_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        service_order_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[resource_access_token_list_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResourceAccessTokenResult:
        """
        Returns all resource access tokens based on resource access token identifiers,
        reservations or interval. One of them must be specified in the request. Note
        this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          activity_states: Whether to return only active, only deleted or both records.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          resource_access_token_ids: Unique identifiers of
              [Resource access tokens](https://mews-systems.gitbook.io/connector-api/operations/#resource-access-token).
              Required if no other filter is provided.

          service_order_ids: Unique identifiers of reservations. Required if no other filter is provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/resourceAccessTokens/getAll",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "activity_states": activity_states,
                    "colliding_utc": colliding_utc,
                    "enterprise_ids": enterprise_ids,
                    "resource_access_token_ids": resource_access_token_ids,
                    "service_order_ids": service_order_ids,
                    "updated_utc": updated_utc,
                },
                resource_access_token_list_params.ResourceAccessTokenListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResourceAccessTokenResult,
        )

    def delete(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Delete specified resource access tokens.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          ids: Unique identifiers of
              [Resource access token](https://mews-systems.gitbook.io/connector-api/operations/#resource-access-token).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/resourceAccessTokens/delete",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "ids": ids,
                },
                resource_access_token_delete_params.ResourceAccessTokenDeleteParams,
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
        resource_access_token_parameters: Iterable[resource_access_token_add_params.ResourceAccessTokenParameter],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResourceAccessTokenResult:
        """
        Adds new resource access tokens with the specified data.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          resource_access_token_parameters: Parameters of
              [Resource access token](https://mews-systems.gitbook.io/connector-api/operations/#resource-access-token).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/resourceAccessTokens/add",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "resource_access_token_parameters": resource_access_token_parameters,
                },
                resource_access_token_add_params.ResourceAccessTokenAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResourceAccessTokenResult,
        )


class AsyncResourceAccessTokensResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncResourceAccessTokensResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return AsyncResourceAccessTokensResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResourceAccessTokensResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return AsyncResourceAccessTokensResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        resource_access_token_updates: Optional[Iterable[resource_access_token_update_params.ResourceAccessTokenUpdate]]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResourceAccessTokenResult:
        """
        Updates the
        [Resource access token](https://mews-systems.gitbook.io/connector-api/operations/#resource-access-token)
        validity interval and
        [permissions](https://mews-systems.gitbook.io/connector-api/operations/#resource-access-token-permission-parameter)
        that it grants.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          resource_access_token_updates: Parameters of
              [Resource access token](https://mews-systems.gitbook.io/connector-api/operations/#resource-access-token).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/resourceAccessTokens/update",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "enterprise_id": enterprise_id,
                    "resource_access_token_updates": resource_access_token_updates,
                },
                resource_access_token_update_params.ResourceAccessTokenUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResourceAccessTokenResult,
        )

    async def list(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: resource_access_token_list_params.Limitation,
        activity_states: Optional[List[str]] | NotGiven = NOT_GIVEN,
        colliding_utc: Optional[resource_access_token_list_params.CollidingUtc] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        resource_access_token_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        service_order_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[resource_access_token_list_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResourceAccessTokenResult:
        """
        Returns all resource access tokens based on resource access token identifiers,
        reservations or interval. One of them must be specified in the request. Note
        this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          activity_states: Whether to return only active, only deleted or both records.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          resource_access_token_ids: Unique identifiers of
              [Resource access tokens](https://mews-systems.gitbook.io/connector-api/operations/#resource-access-token).
              Required if no other filter is provided.

          service_order_ids: Unique identifiers of reservations. Required if no other filter is provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/resourceAccessTokens/getAll",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "activity_states": activity_states,
                    "colliding_utc": colliding_utc,
                    "enterprise_ids": enterprise_ids,
                    "resource_access_token_ids": resource_access_token_ids,
                    "service_order_ids": service_order_ids,
                    "updated_utc": updated_utc,
                },
                resource_access_token_list_params.ResourceAccessTokenListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResourceAccessTokenResult,
        )

    async def delete(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Delete specified resource access tokens.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          ids: Unique identifiers of
              [Resource access token](https://mews-systems.gitbook.io/connector-api/operations/#resource-access-token).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/resourceAccessTokens/delete",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "ids": ids,
                },
                resource_access_token_delete_params.ResourceAccessTokenDeleteParams,
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
        resource_access_token_parameters: Iterable[resource_access_token_add_params.ResourceAccessTokenParameter],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResourceAccessTokenResult:
        """
        Adds new resource access tokens with the specified data.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          resource_access_token_parameters: Parameters of
              [Resource access token](https://mews-systems.gitbook.io/connector-api/operations/#resource-access-token).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/resourceAccessTokens/add",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "resource_access_token_parameters": resource_access_token_parameters,
                },
                resource_access_token_add_params.ResourceAccessTokenAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResourceAccessTokenResult,
        )


class ResourceAccessTokensResourceWithRawResponse:
    def __init__(self, resource_access_tokens: ResourceAccessTokensResource) -> None:
        self._resource_access_tokens = resource_access_tokens

        self.update = to_raw_response_wrapper(
            resource_access_tokens.update,
        )
        self.list = to_raw_response_wrapper(
            resource_access_tokens.list,
        )
        self.delete = to_raw_response_wrapper(
            resource_access_tokens.delete,
        )
        self.add = to_raw_response_wrapper(
            resource_access_tokens.add,
        )


class AsyncResourceAccessTokensResourceWithRawResponse:
    def __init__(self, resource_access_tokens: AsyncResourceAccessTokensResource) -> None:
        self._resource_access_tokens = resource_access_tokens

        self.update = async_to_raw_response_wrapper(
            resource_access_tokens.update,
        )
        self.list = async_to_raw_response_wrapper(
            resource_access_tokens.list,
        )
        self.delete = async_to_raw_response_wrapper(
            resource_access_tokens.delete,
        )
        self.add = async_to_raw_response_wrapper(
            resource_access_tokens.add,
        )


class ResourceAccessTokensResourceWithStreamingResponse:
    def __init__(self, resource_access_tokens: ResourceAccessTokensResource) -> None:
        self._resource_access_tokens = resource_access_tokens

        self.update = to_streamed_response_wrapper(
            resource_access_tokens.update,
        )
        self.list = to_streamed_response_wrapper(
            resource_access_tokens.list,
        )
        self.delete = to_streamed_response_wrapper(
            resource_access_tokens.delete,
        )
        self.add = to_streamed_response_wrapper(
            resource_access_tokens.add,
        )


class AsyncResourceAccessTokensResourceWithStreamingResponse:
    def __init__(self, resource_access_tokens: AsyncResourceAccessTokensResource) -> None:
        self._resource_access_tokens = resource_access_tokens

        self.update = async_to_streamed_response_wrapper(
            resource_access_tokens.update,
        )
        self.list = async_to_streamed_response_wrapper(
            resource_access_tokens.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            resource_access_tokens.delete,
        )
        self.add = async_to_streamed_response_wrapper(
            resource_access_tokens.add,
        )
