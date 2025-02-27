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
    loyalty_tier_add_params,
    loyalty_tier_list_params,
    loyalty_tier_delete_params,
    loyalty_tier_update_params,
)
from .....types.api.connector.v1.loyalty_tier_result import LoyaltyTierResult

__all__ = ["LoyaltyTiersResource", "AsyncLoyaltyTiersResource"]


class LoyaltyTiersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LoyaltyTiersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return LoyaltyTiersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LoyaltyTiersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return LoyaltyTiersResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        loyalty_tier_updates: Iterable[loyalty_tier_update_params.LoyaltyTierUpdate],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoyaltyTierResult:
        """
        Updates information about the specified loyalty tiers.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          loyalty_tier_updates: Loyalty tiers to be updated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/loyaltyTiers/update",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "loyalty_tier_updates": loyalty_tier_updates,
                },
                loyalty_tier_update_params.LoyaltyTierUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoyaltyTierResult,
        )

    def list(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        loyalty_program_ids: List[str],
        activity_states: Optional[List[Literal["Deleted", "Active"]]] | NotGiven = NOT_GIVEN,
        chain_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        limitation: Optional[loyalty_tier_list_params.Limitation] | NotGiven = NOT_GIVEN,
        loyalty_tier_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[loyalty_tier_list_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoyaltyTierResult:
        """
        Returns all loyalty tiers of the chain (in the given activity state), filtered
        by loyalty program identifiers and optionally filtered by specific loyalty tier
        identifiers or other filter parameters. Note this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          loyalty_program_ids: Unique identifiers of
              [Loyalty programs](https://mews-systems.gitbook.io/connector-api/operations/#loyalty-program).

          activity_states: Whether to return only active, only deleted or both records.

          chain_ids: Unique identifiers of the chain. If not specified, the operation returns data
              for all chains within scope of the Access Token.

          limitation: Limitation on the quantity of data returned.

          loyalty_tier_ids: Unique identifiers of
              [Loyalty tiers](https://mews-systems.gitbook.io/connector-api/operations/#loyalty-tier).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/loyaltyTiers/getAll",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "loyalty_program_ids": loyalty_program_ids,
                    "activity_states": activity_states,
                    "chain_ids": chain_ids,
                    "limitation": limitation,
                    "loyalty_tier_ids": loyalty_tier_ids,
                    "updated_utc": updated_utc,
                },
                loyalty_tier_list_params.LoyaltyTierListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoyaltyTierResult,
        )

    def delete(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        loyalty_tier_ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Deletes loyalty tiers.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          loyalty_tier_ids: Unique identifier of the loyalty tiers to be deleted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/loyaltyTiers/delete",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "loyalty_tier_ids": loyalty_tier_ids,
                },
                loyalty_tier_delete_params.LoyaltyTierDeleteParams,
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
        loyalty_tiers: Iterable[loyalty_tier_add_params.LoyaltyTier],
        chain_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoyaltyTierResult:
        """Adds loyalty tiers to a loyalty program of the enterprise chain.

        Note this
        operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          loyalty_tiers: Loyalty tiers to be added.

          chain_id: Unique identifier of the chain. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/loyaltyTiers/add",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "loyalty_tiers": loyalty_tiers,
                    "chain_id": chain_id,
                },
                loyalty_tier_add_params.LoyaltyTierAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoyaltyTierResult,
        )


class AsyncLoyaltyTiersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLoyaltyTiersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return AsyncLoyaltyTiersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLoyaltyTiersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return AsyncLoyaltyTiersResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        loyalty_tier_updates: Iterable[loyalty_tier_update_params.LoyaltyTierUpdate],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoyaltyTierResult:
        """
        Updates information about the specified loyalty tiers.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          loyalty_tier_updates: Loyalty tiers to be updated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/loyaltyTiers/update",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "loyalty_tier_updates": loyalty_tier_updates,
                },
                loyalty_tier_update_params.LoyaltyTierUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoyaltyTierResult,
        )

    async def list(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        loyalty_program_ids: List[str],
        activity_states: Optional[List[Literal["Deleted", "Active"]]] | NotGiven = NOT_GIVEN,
        chain_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        limitation: Optional[loyalty_tier_list_params.Limitation] | NotGiven = NOT_GIVEN,
        loyalty_tier_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[loyalty_tier_list_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoyaltyTierResult:
        """
        Returns all loyalty tiers of the chain (in the given activity state), filtered
        by loyalty program identifiers and optionally filtered by specific loyalty tier
        identifiers or other filter parameters. Note this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          loyalty_program_ids: Unique identifiers of
              [Loyalty programs](https://mews-systems.gitbook.io/connector-api/operations/#loyalty-program).

          activity_states: Whether to return only active, only deleted or both records.

          chain_ids: Unique identifiers of the chain. If not specified, the operation returns data
              for all chains within scope of the Access Token.

          limitation: Limitation on the quantity of data returned.

          loyalty_tier_ids: Unique identifiers of
              [Loyalty tiers](https://mews-systems.gitbook.io/connector-api/operations/#loyalty-tier).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/loyaltyTiers/getAll",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "loyalty_program_ids": loyalty_program_ids,
                    "activity_states": activity_states,
                    "chain_ids": chain_ids,
                    "limitation": limitation,
                    "loyalty_tier_ids": loyalty_tier_ids,
                    "updated_utc": updated_utc,
                },
                loyalty_tier_list_params.LoyaltyTierListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoyaltyTierResult,
        )

    async def delete(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        loyalty_tier_ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Deletes loyalty tiers.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          loyalty_tier_ids: Unique identifier of the loyalty tiers to be deleted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/loyaltyTiers/delete",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "loyalty_tier_ids": loyalty_tier_ids,
                },
                loyalty_tier_delete_params.LoyaltyTierDeleteParams,
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
        loyalty_tiers: Iterable[loyalty_tier_add_params.LoyaltyTier],
        chain_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoyaltyTierResult:
        """Adds loyalty tiers to a loyalty program of the enterprise chain.

        Note this
        operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          loyalty_tiers: Loyalty tiers to be added.

          chain_id: Unique identifier of the chain. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/loyaltyTiers/add",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "loyalty_tiers": loyalty_tiers,
                    "chain_id": chain_id,
                },
                loyalty_tier_add_params.LoyaltyTierAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoyaltyTierResult,
        )


class LoyaltyTiersResourceWithRawResponse:
    def __init__(self, loyalty_tiers: LoyaltyTiersResource) -> None:
        self._loyalty_tiers = loyalty_tiers

        self.update = to_raw_response_wrapper(
            loyalty_tiers.update,
        )
        self.list = to_raw_response_wrapper(
            loyalty_tiers.list,
        )
        self.delete = to_raw_response_wrapper(
            loyalty_tiers.delete,
        )
        self.add = to_raw_response_wrapper(
            loyalty_tiers.add,
        )


class AsyncLoyaltyTiersResourceWithRawResponse:
    def __init__(self, loyalty_tiers: AsyncLoyaltyTiersResource) -> None:
        self._loyalty_tiers = loyalty_tiers

        self.update = async_to_raw_response_wrapper(
            loyalty_tiers.update,
        )
        self.list = async_to_raw_response_wrapper(
            loyalty_tiers.list,
        )
        self.delete = async_to_raw_response_wrapper(
            loyalty_tiers.delete,
        )
        self.add = async_to_raw_response_wrapper(
            loyalty_tiers.add,
        )


class LoyaltyTiersResourceWithStreamingResponse:
    def __init__(self, loyalty_tiers: LoyaltyTiersResource) -> None:
        self._loyalty_tiers = loyalty_tiers

        self.update = to_streamed_response_wrapper(
            loyalty_tiers.update,
        )
        self.list = to_streamed_response_wrapper(
            loyalty_tiers.list,
        )
        self.delete = to_streamed_response_wrapper(
            loyalty_tiers.delete,
        )
        self.add = to_streamed_response_wrapper(
            loyalty_tiers.add,
        )


class AsyncLoyaltyTiersResourceWithStreamingResponse:
    def __init__(self, loyalty_tiers: AsyncLoyaltyTiersResource) -> None:
        self._loyalty_tiers = loyalty_tiers

        self.update = async_to_streamed_response_wrapper(
            loyalty_tiers.update,
        )
        self.list = async_to_streamed_response_wrapper(
            loyalty_tiers.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            loyalty_tiers.delete,
        )
        self.add = async_to_streamed_response_wrapper(
            loyalty_tiers.add,
        )
