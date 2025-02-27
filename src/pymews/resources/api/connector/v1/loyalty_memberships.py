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
    loyalty_membership_add_params,
    loyalty_membership_list_params,
    loyalty_membership_delete_params,
    loyalty_membership_update_params,
)
from .....types.api.connector.v1.loyalty_membership_result import LoyaltyMembershipResult

__all__ = ["LoyaltyMembershipsResource", "AsyncLoyaltyMembershipsResource"]


class LoyaltyMembershipsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LoyaltyMembershipsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return LoyaltyMembershipsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LoyaltyMembershipsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return LoyaltyMembershipsResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        loyalty_membership_updates: Iterable[loyalty_membership_update_params.LoyaltyMembershipUpdate],
        chain_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoyaltyMembershipResult:
        """Updates information about the specified loyalty memberships.

        Note this operation
        supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          loyalty_membership_updates: Loyalty memberships to be updated.

          chain_id: Unique identifier of the chain. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/loyaltyMemberships/update",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "loyalty_membership_updates": loyalty_membership_updates,
                    "chain_id": chain_id,
                },
                loyalty_membership_update_params.LoyaltyMembershipUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoyaltyMembershipResult,
        )

    def list(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: loyalty_membership_list_params.Limitation,
        account_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        activity_states: Optional[List[Literal["Deleted", "Active"]]] | NotGiven = NOT_GIVEN,
        chain_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        codes: Optional[List[str]] | NotGiven = NOT_GIVEN,
        created_utc: Optional[loyalty_membership_list_params.CreatedUtc] | NotGiven = NOT_GIVEN,
        loyalty_membership_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        loyalty_program_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        membership_states: Optional[List[Literal["New", "Pending", "Enrolled", "Canceled", "Declined"]]]
        | NotGiven = NOT_GIVEN,
        updated_utc: Optional[loyalty_membership_list_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoyaltyMembershipResult:
        """
        Returns all loyalty memberships of the enterprise (in the given activity
        states), optionally filtered by specific loyalty membership identifiers or other
        filter parameters. Note this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          account_ids: Unique identifiers of accounts (for example
              [Customers](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer)
              or
              [Companies](https://mews-systems.gitbook.io/connector-api/operations/companies/#company))
              the membership is associated with.

          activity_states: Whether to return only active, only deleted or both records.

          chain_ids: Unique identifiers of the chain. If not specified, the operation returns data
              for all chains within scope of the Access Token.

          loyalty_membership_ids: Unique identifiers of
              [Loyalty memberships](https://mews-systems.gitbook.io/connector-api/operations/#loyalty-membership).

          loyalty_program_ids: Unique identifiers of
              [Loyalty programs](https://mews-systems.gitbook.io/connector-api/operations/loyaltyprograms/#loyalty-program).

          membership_states: States of the loyalty memberships.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/loyaltyMemberships/getAll",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "account_ids": account_ids,
                    "activity_states": activity_states,
                    "chain_ids": chain_ids,
                    "codes": codes,
                    "created_utc": created_utc,
                    "loyalty_membership_ids": loyalty_membership_ids,
                    "loyalty_program_ids": loyalty_program_ids,
                    "membership_states": membership_states,
                    "updated_utc": updated_utc,
                },
                loyalty_membership_list_params.LoyaltyMembershipListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoyaltyMembershipResult,
        )

    def delete(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        loyalty_membership_ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Deletes loyalty memberships.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          loyalty_membership_ids: Unique identifier of the loyalty memberships to be deleted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/loyaltyMemberships/delete",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "loyalty_membership_ids": loyalty_membership_ids,
                },
                loyalty_membership_delete_params.LoyaltyMembershipDeleteParams,
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
        loyalty_memberships: Iterable[loyalty_membership_add_params.LoyaltyMembership],
        chain_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoyaltyMembershipResult:
        """Adds loyalty memberships to the enterprise.

        Note this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          loyalty_memberships: Loyalty memberships to be added.

          chain_id: Unique identifier of the chain. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/loyaltyMemberships/add",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "loyalty_memberships": loyalty_memberships,
                    "chain_id": chain_id,
                },
                loyalty_membership_add_params.LoyaltyMembershipAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoyaltyMembershipResult,
        )


class AsyncLoyaltyMembershipsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLoyaltyMembershipsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return AsyncLoyaltyMembershipsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLoyaltyMembershipsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return AsyncLoyaltyMembershipsResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        loyalty_membership_updates: Iterable[loyalty_membership_update_params.LoyaltyMembershipUpdate],
        chain_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoyaltyMembershipResult:
        """Updates information about the specified loyalty memberships.

        Note this operation
        supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          loyalty_membership_updates: Loyalty memberships to be updated.

          chain_id: Unique identifier of the chain. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/loyaltyMemberships/update",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "loyalty_membership_updates": loyalty_membership_updates,
                    "chain_id": chain_id,
                },
                loyalty_membership_update_params.LoyaltyMembershipUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoyaltyMembershipResult,
        )

    async def list(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: loyalty_membership_list_params.Limitation,
        account_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        activity_states: Optional[List[Literal["Deleted", "Active"]]] | NotGiven = NOT_GIVEN,
        chain_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        codes: Optional[List[str]] | NotGiven = NOT_GIVEN,
        created_utc: Optional[loyalty_membership_list_params.CreatedUtc] | NotGiven = NOT_GIVEN,
        loyalty_membership_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        loyalty_program_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        membership_states: Optional[List[Literal["New", "Pending", "Enrolled", "Canceled", "Declined"]]]
        | NotGiven = NOT_GIVEN,
        updated_utc: Optional[loyalty_membership_list_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoyaltyMembershipResult:
        """
        Returns all loyalty memberships of the enterprise (in the given activity
        states), optionally filtered by specific loyalty membership identifiers or other
        filter parameters. Note this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          account_ids: Unique identifiers of accounts (for example
              [Customers](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer)
              or
              [Companies](https://mews-systems.gitbook.io/connector-api/operations/companies/#company))
              the membership is associated with.

          activity_states: Whether to return only active, only deleted or both records.

          chain_ids: Unique identifiers of the chain. If not specified, the operation returns data
              for all chains within scope of the Access Token.

          loyalty_membership_ids: Unique identifiers of
              [Loyalty memberships](https://mews-systems.gitbook.io/connector-api/operations/#loyalty-membership).

          loyalty_program_ids: Unique identifiers of
              [Loyalty programs](https://mews-systems.gitbook.io/connector-api/operations/loyaltyprograms/#loyalty-program).

          membership_states: States of the loyalty memberships.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/loyaltyMemberships/getAll",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "account_ids": account_ids,
                    "activity_states": activity_states,
                    "chain_ids": chain_ids,
                    "codes": codes,
                    "created_utc": created_utc,
                    "loyalty_membership_ids": loyalty_membership_ids,
                    "loyalty_program_ids": loyalty_program_ids,
                    "membership_states": membership_states,
                    "updated_utc": updated_utc,
                },
                loyalty_membership_list_params.LoyaltyMembershipListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoyaltyMembershipResult,
        )

    async def delete(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        loyalty_membership_ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Deletes loyalty memberships.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          loyalty_membership_ids: Unique identifier of the loyalty memberships to be deleted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/loyaltyMemberships/delete",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "loyalty_membership_ids": loyalty_membership_ids,
                },
                loyalty_membership_delete_params.LoyaltyMembershipDeleteParams,
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
        loyalty_memberships: Iterable[loyalty_membership_add_params.LoyaltyMembership],
        chain_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoyaltyMembershipResult:
        """Adds loyalty memberships to the enterprise.

        Note this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          loyalty_memberships: Loyalty memberships to be added.

          chain_id: Unique identifier of the chain. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/loyaltyMemberships/add",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "loyalty_memberships": loyalty_memberships,
                    "chain_id": chain_id,
                },
                loyalty_membership_add_params.LoyaltyMembershipAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoyaltyMembershipResult,
        )


class LoyaltyMembershipsResourceWithRawResponse:
    def __init__(self, loyalty_memberships: LoyaltyMembershipsResource) -> None:
        self._loyalty_memberships = loyalty_memberships

        self.update = to_raw_response_wrapper(
            loyalty_memberships.update,
        )
        self.list = to_raw_response_wrapper(
            loyalty_memberships.list,
        )
        self.delete = to_raw_response_wrapper(
            loyalty_memberships.delete,
        )
        self.add = to_raw_response_wrapper(
            loyalty_memberships.add,
        )


class AsyncLoyaltyMembershipsResourceWithRawResponse:
    def __init__(self, loyalty_memberships: AsyncLoyaltyMembershipsResource) -> None:
        self._loyalty_memberships = loyalty_memberships

        self.update = async_to_raw_response_wrapper(
            loyalty_memberships.update,
        )
        self.list = async_to_raw_response_wrapper(
            loyalty_memberships.list,
        )
        self.delete = async_to_raw_response_wrapper(
            loyalty_memberships.delete,
        )
        self.add = async_to_raw_response_wrapper(
            loyalty_memberships.add,
        )


class LoyaltyMembershipsResourceWithStreamingResponse:
    def __init__(self, loyalty_memberships: LoyaltyMembershipsResource) -> None:
        self._loyalty_memberships = loyalty_memberships

        self.update = to_streamed_response_wrapper(
            loyalty_memberships.update,
        )
        self.list = to_streamed_response_wrapper(
            loyalty_memberships.list,
        )
        self.delete = to_streamed_response_wrapper(
            loyalty_memberships.delete,
        )
        self.add = to_streamed_response_wrapper(
            loyalty_memberships.add,
        )


class AsyncLoyaltyMembershipsResourceWithStreamingResponse:
    def __init__(self, loyalty_memberships: AsyncLoyaltyMembershipsResource) -> None:
        self._loyalty_memberships = loyalty_memberships

        self.update = async_to_streamed_response_wrapper(
            loyalty_memberships.update,
        )
        self.list = async_to_streamed_response_wrapper(
            loyalty_memberships.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            loyalty_memberships.delete,
        )
        self.add = async_to_streamed_response_wrapper(
            loyalty_memberships.add,
        )
