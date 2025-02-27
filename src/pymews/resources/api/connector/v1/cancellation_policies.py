# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
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
    cancellation_policy_list_params,
    cancellation_policy_get_by_rates_params,
    cancellation_policy_get_by_reservations_params,
)
from .....types.api.connector.v1.cancellation_policy_list_response import CancellationPolicyListResponse
from .....types.api.connector.v1.cancellation_policy_get_by_rates_response import CancellationPolicyGetByRatesResponse
from .....types.api.connector.v1.cancellation_policy_get_by_reservations_response import (
    CancellationPolicyGetByReservationsResponse,
)

__all__ = ["CancellationPoliciesResource", "AsyncCancellationPoliciesResource"]


class CancellationPoliciesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CancellationPoliciesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return CancellationPoliciesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CancellationPoliciesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return CancellationPoliciesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: cancellation_policy_list_params.Limitation,
        service_ids: List[str],
        activity_states: Optional[List[Literal["Deleted", "Active"]]] | NotGiven = NOT_GIVEN,
        cancellation_policy_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        rate_group_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[cancellation_policy_list_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CancellationPolicyListResponse:
        """
        > ### Restricted!
        >
        > This operation is currently in beta-test and as such it is subject to change.
        > Returns all cancellation policies, filtered by services, rate groups and other
        > filters. Note this operation uses
        > [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        > and supports
        > [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          service_ids: Unique identifiers of the
              [Service](https://mews-systems.gitbook.io/connector-api/operations/services/#service).

          activity_states: Whether to return only active, only deleted, or both types of record. If not
              specified, only active records will be returned.

          cancellation_policy_ids: Unique identifiers of the
              [Cancellation Policy](https://mews-systems.gitbook.io/connector-api/operations/#cancellationpolicy).
              Required if no other filter is provided.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          rate_group_ids: Unique identifiers of the
              [Rate group](https://mews-systems.gitbook.io/connector-api/operations/rates/#rategroup).
              Required if no other filter is provided.

          updated_utc: Interval in which the Cancellation Policy was updated. Required if no other
              filter is provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/cancellationPolicies/getAll",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "service_ids": service_ids,
                    "activity_states": activity_states,
                    "cancellation_policy_ids": cancellation_policy_ids,
                    "enterprise_ids": enterprise_ids,
                    "rate_group_ids": rate_group_ids,
                    "updated_utc": updated_utc,
                },
                cancellation_policy_list_params.CancellationPolicyListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CancellationPolicyListResponse,
        )

    def get_by_rates(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        rate_ids: List[str],
        reservation_end_utc: Union[str, datetime],
        reservation_start_utc: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CancellationPolicyGetByRatesResponse:
        """
        Gets cancellation policies for enterprise grouped by rate for granular
        cancellation policies flow. This operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          rate_ids: Unique identifiers of the `Rate`.

          reservation_end_utc: End of the reservation interval in UTC timezone in ISO 8601 format.

          reservation_start_utc: Start of the reservation interval in UTC timezone in ISO 8601 format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/cancellationPolicies/getByRates",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "rate_ids": rate_ids,
                    "reservation_end_utc": reservation_end_utc,
                    "reservation_start_utc": reservation_start_utc,
                },
                cancellation_policy_get_by_rates_params.CancellationPolicyGetByRatesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CancellationPolicyGetByRatesResponse,
        )

    def get_by_reservations(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        reservation_ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CancellationPolicyGetByReservationsResponse:
        """
        Gets cancellation policies for enterprise grouped by reservation for granular
        cancellation policies flow. This operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          reservation_ids: Unique identifiers of the `Reservation`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/cancellationPolicies/getByReservations",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "reservation_ids": reservation_ids,
                },
                cancellation_policy_get_by_reservations_params.CancellationPolicyGetByReservationsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CancellationPolicyGetByReservationsResponse,
        )


class AsyncCancellationPoliciesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCancellationPoliciesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return AsyncCancellationPoliciesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCancellationPoliciesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return AsyncCancellationPoliciesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: cancellation_policy_list_params.Limitation,
        service_ids: List[str],
        activity_states: Optional[List[Literal["Deleted", "Active"]]] | NotGiven = NOT_GIVEN,
        cancellation_policy_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        rate_group_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[cancellation_policy_list_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CancellationPolicyListResponse:
        """
        > ### Restricted!
        >
        > This operation is currently in beta-test and as such it is subject to change.
        > Returns all cancellation policies, filtered by services, rate groups and other
        > filters. Note this operation uses
        > [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        > and supports
        > [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          service_ids: Unique identifiers of the
              [Service](https://mews-systems.gitbook.io/connector-api/operations/services/#service).

          activity_states: Whether to return only active, only deleted, or both types of record. If not
              specified, only active records will be returned.

          cancellation_policy_ids: Unique identifiers of the
              [Cancellation Policy](https://mews-systems.gitbook.io/connector-api/operations/#cancellationpolicy).
              Required if no other filter is provided.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          rate_group_ids: Unique identifiers of the
              [Rate group](https://mews-systems.gitbook.io/connector-api/operations/rates/#rategroup).
              Required if no other filter is provided.

          updated_utc: Interval in which the Cancellation Policy was updated. Required if no other
              filter is provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/cancellationPolicies/getAll",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "service_ids": service_ids,
                    "activity_states": activity_states,
                    "cancellation_policy_ids": cancellation_policy_ids,
                    "enterprise_ids": enterprise_ids,
                    "rate_group_ids": rate_group_ids,
                    "updated_utc": updated_utc,
                },
                cancellation_policy_list_params.CancellationPolicyListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CancellationPolicyListResponse,
        )

    async def get_by_rates(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        rate_ids: List[str],
        reservation_end_utc: Union[str, datetime],
        reservation_start_utc: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CancellationPolicyGetByRatesResponse:
        """
        Gets cancellation policies for enterprise grouped by rate for granular
        cancellation policies flow. This operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          rate_ids: Unique identifiers of the `Rate`.

          reservation_end_utc: End of the reservation interval in UTC timezone in ISO 8601 format.

          reservation_start_utc: Start of the reservation interval in UTC timezone in ISO 8601 format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/cancellationPolicies/getByRates",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "rate_ids": rate_ids,
                    "reservation_end_utc": reservation_end_utc,
                    "reservation_start_utc": reservation_start_utc,
                },
                cancellation_policy_get_by_rates_params.CancellationPolicyGetByRatesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CancellationPolicyGetByRatesResponse,
        )

    async def get_by_reservations(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        reservation_ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CancellationPolicyGetByReservationsResponse:
        """
        Gets cancellation policies for enterprise grouped by reservation for granular
        cancellation policies flow. This operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          reservation_ids: Unique identifiers of the `Reservation`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/cancellationPolicies/getByReservations",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "reservation_ids": reservation_ids,
                },
                cancellation_policy_get_by_reservations_params.CancellationPolicyGetByReservationsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CancellationPolicyGetByReservationsResponse,
        )


class CancellationPoliciesResourceWithRawResponse:
    def __init__(self, cancellation_policies: CancellationPoliciesResource) -> None:
        self._cancellation_policies = cancellation_policies

        self.list = to_raw_response_wrapper(
            cancellation_policies.list,
        )
        self.get_by_rates = to_raw_response_wrapper(
            cancellation_policies.get_by_rates,
        )
        self.get_by_reservations = to_raw_response_wrapper(
            cancellation_policies.get_by_reservations,
        )


class AsyncCancellationPoliciesResourceWithRawResponse:
    def __init__(self, cancellation_policies: AsyncCancellationPoliciesResource) -> None:
        self._cancellation_policies = cancellation_policies

        self.list = async_to_raw_response_wrapper(
            cancellation_policies.list,
        )
        self.get_by_rates = async_to_raw_response_wrapper(
            cancellation_policies.get_by_rates,
        )
        self.get_by_reservations = async_to_raw_response_wrapper(
            cancellation_policies.get_by_reservations,
        )


class CancellationPoliciesResourceWithStreamingResponse:
    def __init__(self, cancellation_policies: CancellationPoliciesResource) -> None:
        self._cancellation_policies = cancellation_policies

        self.list = to_streamed_response_wrapper(
            cancellation_policies.list,
        )
        self.get_by_rates = to_streamed_response_wrapper(
            cancellation_policies.get_by_rates,
        )
        self.get_by_reservations = to_streamed_response_wrapper(
            cancellation_policies.get_by_reservations,
        )


class AsyncCancellationPoliciesResourceWithStreamingResponse:
    def __init__(self, cancellation_policies: AsyncCancellationPoliciesResource) -> None:
        self._cancellation_policies = cancellation_policies

        self.list = async_to_streamed_response_wrapper(
            cancellation_policies.list,
        )
        self.get_by_rates = async_to_streamed_response_wrapper(
            cancellation_policies.get_by_rates,
        )
        self.get_by_reservations = async_to_streamed_response_wrapper(
            cancellation_policies.get_by_reservations,
        )
