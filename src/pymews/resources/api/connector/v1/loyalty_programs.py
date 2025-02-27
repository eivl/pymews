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
    loyalty_program_add_params,
    loyalty_program_list_params,
    loyalty_program_delete_params,
    loyalty_program_update_params,
)
from .....types.api.connector.v1.loyalty_program_result import LoyaltyProgramResult

__all__ = ["LoyaltyProgramsResource", "AsyncLoyaltyProgramsResource"]


class LoyaltyProgramsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LoyaltyProgramsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return LoyaltyProgramsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LoyaltyProgramsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return LoyaltyProgramsResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        loyalty_program_updates: Iterable[loyalty_program_update_params.LoyaltyProgramUpdate],
        chain_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoyaltyProgramResult:
        """Updates information about the specified loyalty programs.

        Note this operation
        supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          loyalty_program_updates: Loyalty programs to be updated.

          chain_id: Unique identifier of the chain. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/loyaltyPrograms/update",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "loyalty_program_updates": loyalty_program_updates,
                    "chain_id": chain_id,
                },
                loyalty_program_update_params.LoyaltyProgramUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoyaltyProgramResult,
        )

    def list(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: loyalty_program_list_params.Limitation,
        activity_states: Optional[List[Literal["Deleted", "Active"]]] | NotGiven = NOT_GIVEN,
        chain_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        codes: Optional[List[str]] | NotGiven = NOT_GIVEN,
        created_utc: Optional[loyalty_program_list_params.CreatedUtc] | NotGiven = NOT_GIVEN,
        loyalty_program_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[loyalty_program_list_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoyaltyProgramResult:
        """
        Returns all loyalty programs of the enterprise (in the given activity state),
        optionally filtered by specific loyalty program identifiers or other filter
        parameters. Note this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          activity_states: Whether to return only active, only deleted or both records.

          chain_ids: Unique identifiers of the chain. If not specified, the operation returns data
              for all chains within scope of the Access Token.

          loyalty_program_ids: Unique identifiers of
              [Loyalty programs](https://mews-systems.gitbook.io/connector-api/operations/#loyalty-program).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/loyaltyPrograms/getAll",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "activity_states": activity_states,
                    "chain_ids": chain_ids,
                    "codes": codes,
                    "created_utc": created_utc,
                    "loyalty_program_ids": loyalty_program_ids,
                    "updated_utc": updated_utc,
                },
                loyalty_program_list_params.LoyaltyProgramListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoyaltyProgramResult,
        )

    def delete(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        loyalty_program_ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Deletes loyalty programs.

        Note that a loyalty program containing active
        memberships cannot be deleted.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          loyalty_program_ids: Unique identifier of the loyalty programs to be deleted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/loyaltyPrograms/delete",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "loyalty_program_ids": loyalty_program_ids,
                },
                loyalty_program_delete_params.LoyaltyProgramDeleteParams,
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
        loyalty_programs: Iterable[loyalty_program_add_params.LoyaltyProgram],
        chain_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoyaltyProgramResult:
        """Adds loyalty programs to the enterprise.

        Note this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          loyalty_programs: Loyalty programs to be added.

          chain_id: Unique identifier of the chain. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/loyaltyPrograms/add",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "loyalty_programs": loyalty_programs,
                    "chain_id": chain_id,
                },
                loyalty_program_add_params.LoyaltyProgramAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoyaltyProgramResult,
        )


class AsyncLoyaltyProgramsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLoyaltyProgramsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return AsyncLoyaltyProgramsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLoyaltyProgramsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return AsyncLoyaltyProgramsResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        loyalty_program_updates: Iterable[loyalty_program_update_params.LoyaltyProgramUpdate],
        chain_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoyaltyProgramResult:
        """Updates information about the specified loyalty programs.

        Note this operation
        supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          loyalty_program_updates: Loyalty programs to be updated.

          chain_id: Unique identifier of the chain. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/loyaltyPrograms/update",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "loyalty_program_updates": loyalty_program_updates,
                    "chain_id": chain_id,
                },
                loyalty_program_update_params.LoyaltyProgramUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoyaltyProgramResult,
        )

    async def list(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: loyalty_program_list_params.Limitation,
        activity_states: Optional[List[Literal["Deleted", "Active"]]] | NotGiven = NOT_GIVEN,
        chain_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        codes: Optional[List[str]] | NotGiven = NOT_GIVEN,
        created_utc: Optional[loyalty_program_list_params.CreatedUtc] | NotGiven = NOT_GIVEN,
        loyalty_program_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[loyalty_program_list_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoyaltyProgramResult:
        """
        Returns all loyalty programs of the enterprise (in the given activity state),
        optionally filtered by specific loyalty program identifiers or other filter
        parameters. Note this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          activity_states: Whether to return only active, only deleted or both records.

          chain_ids: Unique identifiers of the chain. If not specified, the operation returns data
              for all chains within scope of the Access Token.

          loyalty_program_ids: Unique identifiers of
              [Loyalty programs](https://mews-systems.gitbook.io/connector-api/operations/#loyalty-program).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/loyaltyPrograms/getAll",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "activity_states": activity_states,
                    "chain_ids": chain_ids,
                    "codes": codes,
                    "created_utc": created_utc,
                    "loyalty_program_ids": loyalty_program_ids,
                    "updated_utc": updated_utc,
                },
                loyalty_program_list_params.LoyaltyProgramListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoyaltyProgramResult,
        )

    async def delete(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        loyalty_program_ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Deletes loyalty programs.

        Note that a loyalty program containing active
        memberships cannot be deleted.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          loyalty_program_ids: Unique identifier of the loyalty programs to be deleted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/loyaltyPrograms/delete",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "loyalty_program_ids": loyalty_program_ids,
                },
                loyalty_program_delete_params.LoyaltyProgramDeleteParams,
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
        loyalty_programs: Iterable[loyalty_program_add_params.LoyaltyProgram],
        chain_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoyaltyProgramResult:
        """Adds loyalty programs to the enterprise.

        Note this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          loyalty_programs: Loyalty programs to be added.

          chain_id: Unique identifier of the chain. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/loyaltyPrograms/add",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "loyalty_programs": loyalty_programs,
                    "chain_id": chain_id,
                },
                loyalty_program_add_params.LoyaltyProgramAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoyaltyProgramResult,
        )


class LoyaltyProgramsResourceWithRawResponse:
    def __init__(self, loyalty_programs: LoyaltyProgramsResource) -> None:
        self._loyalty_programs = loyalty_programs

        self.update = to_raw_response_wrapper(
            loyalty_programs.update,
        )
        self.list = to_raw_response_wrapper(
            loyalty_programs.list,
        )
        self.delete = to_raw_response_wrapper(
            loyalty_programs.delete,
        )
        self.add = to_raw_response_wrapper(
            loyalty_programs.add,
        )


class AsyncLoyaltyProgramsResourceWithRawResponse:
    def __init__(self, loyalty_programs: AsyncLoyaltyProgramsResource) -> None:
        self._loyalty_programs = loyalty_programs

        self.update = async_to_raw_response_wrapper(
            loyalty_programs.update,
        )
        self.list = async_to_raw_response_wrapper(
            loyalty_programs.list,
        )
        self.delete = async_to_raw_response_wrapper(
            loyalty_programs.delete,
        )
        self.add = async_to_raw_response_wrapper(
            loyalty_programs.add,
        )


class LoyaltyProgramsResourceWithStreamingResponse:
    def __init__(self, loyalty_programs: LoyaltyProgramsResource) -> None:
        self._loyalty_programs = loyalty_programs

        self.update = to_streamed_response_wrapper(
            loyalty_programs.update,
        )
        self.list = to_streamed_response_wrapper(
            loyalty_programs.list,
        )
        self.delete = to_streamed_response_wrapper(
            loyalty_programs.delete,
        )
        self.add = to_streamed_response_wrapper(
            loyalty_programs.add,
        )


class AsyncLoyaltyProgramsResourceWithStreamingResponse:
    def __init__(self, loyalty_programs: AsyncLoyaltyProgramsResource) -> None:
        self._loyalty_programs = loyalty_programs

        self.update = async_to_streamed_response_wrapper(
            loyalty_programs.update,
        )
        self.list = async_to_streamed_response_wrapper(
            loyalty_programs.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            loyalty_programs.delete,
        )
        self.add = async_to_streamed_response_wrapper(
            loyalty_programs.add,
        )
