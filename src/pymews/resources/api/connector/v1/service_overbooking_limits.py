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
    service_overbooking_limit_set_params,
    service_overbooking_limit_list_params,
    service_overbooking_limit_clear_params,
)
from .....types.api.connector.v1.service_overbooking_limit_list_response import ServiceOverbookingLimitListResponse

__all__ = ["ServiceOverbookingLimitsResource", "AsyncServiceOverbookingLimitsResource"]


class ServiceOverbookingLimitsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ServiceOverbookingLimitsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return ServiceOverbookingLimitsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ServiceOverbookingLimitsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return ServiceOverbookingLimitsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: service_overbooking_limit_list_params.Limitation,
        service_ids: List[str],
        activity_states: Optional[List[Literal["Deleted", "Active"]]] | NotGiven = NOT_GIVEN,
        colliding_utc: Optional[service_overbooking_limit_list_params.CollidingUtc] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        service_overbooking_limit_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[service_overbooking_limit_list_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ServiceOverbookingLimitListResponse:
        """Returns all service overbooking limits.

        Note this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          service_ids: Unique identifiers of `Services` associated with the service overbooking limits.

          activity_states: Whether to return only active, only deleted, or both types of record. If not
              specified, only active records will be returned.

          colliding_utc: Interval in which the service overbooking limit is active.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          service_overbooking_limit_ids: Unique identifiers of the service overbooking limits.

          updated_utc: Interval in which the service overbooking limits were updated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/serviceOverbookingLimits/getAll",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "service_ids": service_ids,
                    "activity_states": activity_states,
                    "colliding_utc": colliding_utc,
                    "enterprise_ids": enterprise_ids,
                    "service_overbooking_limit_ids": service_overbooking_limit_ids,
                    "updated_utc": updated_utc,
                },
                service_overbooking_limit_list_params.ServiceOverbookingLimitListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServiceOverbookingLimitListResponse,
        )

    def clear(
        self,
        *,
        access_token: str,
        clear_service_overbooking_limits: Iterable[service_overbooking_limit_clear_params.ClearServiceOverbookingLimit],
        client: str,
        client_token: str,
        service_id: str,
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Deletes service overbooking limits that exactly match the specified conditions.
        This operation is intended to be used alongside `serviceOverbookingLimits/set`.
        The specified conditions must be met exactly. The time interval, however, does
        not need to correspond to an existing service overbooking limit in the system,
        instead the API uses a splicing algorithm to work out how to divide up any
        existing service overbooking limit to meet the specified time interval. Past
        overbooking limits cannot be cleared outside of
        `OperationalEditableHistoryInterval`. Care is needed to specify
        `FirstTimeUnitStartUtc` and `LastTimeUnitStartUtc` in the correct format - see
        [Datetimes](https://mews-systems.gitbook.io/connector-api/guidelines/serialization#datetimes).
        This operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        Args:
          access_token: Access token of the client application.

          clear_service_overbooking_limits: Collection of service overbooking limits to be cleared.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          service_id: Unique identifier of the
              [Service](https://mews-systems.gitbook.io/connector-api/operations/services#service)
              overbooking limits will be set in.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/serviceOverbookingLimits/clear",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "clear_service_overbooking_limits": clear_service_overbooking_limits,
                    "client": client,
                    "client_token": client_token,
                    "service_id": service_id,
                    "enterprise_id": enterprise_id,
                },
                service_overbooking_limit_clear_params.ServiceOverbookingLimitClearParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def set(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        service_id: str,
        set_service_overbooking_limits: Iterable[service_overbooking_limit_set_params.SetServiceOverbookingLimit],
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Adds new service overbooking limits with the specified conditions.

        Past
        overbooking limits cannot be updated outside of
        `OperationalEditableHistoryInterval`. Care is needed to specify
        `FirstTimeUnitStartUtc` and `LastTimeUnitStartUtc` in the correct format - see
        [Datetimes](https://mews-systems.gitbook.io/connector-api/guidelines/serialization#datetimes).
        This operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          service_id: Unique identifier of the
              [Service](https://mews-systems.gitbook.io/connector-api/operations/services#service)
              overbooking limits will be set in.

          set_service_overbooking_limits: Collection of service overbooking limits to be set.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/serviceOverbookingLimits/set",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "service_id": service_id,
                    "set_service_overbooking_limits": set_service_overbooking_limits,
                    "enterprise_id": enterprise_id,
                },
                service_overbooking_limit_set_params.ServiceOverbookingLimitSetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncServiceOverbookingLimitsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncServiceOverbookingLimitsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return AsyncServiceOverbookingLimitsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncServiceOverbookingLimitsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return AsyncServiceOverbookingLimitsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: service_overbooking_limit_list_params.Limitation,
        service_ids: List[str],
        activity_states: Optional[List[Literal["Deleted", "Active"]]] | NotGiven = NOT_GIVEN,
        colliding_utc: Optional[service_overbooking_limit_list_params.CollidingUtc] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        service_overbooking_limit_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[service_overbooking_limit_list_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ServiceOverbookingLimitListResponse:
        """Returns all service overbooking limits.

        Note this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          service_ids: Unique identifiers of `Services` associated with the service overbooking limits.

          activity_states: Whether to return only active, only deleted, or both types of record. If not
              specified, only active records will be returned.

          colliding_utc: Interval in which the service overbooking limit is active.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          service_overbooking_limit_ids: Unique identifiers of the service overbooking limits.

          updated_utc: Interval in which the service overbooking limits were updated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/serviceOverbookingLimits/getAll",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "service_ids": service_ids,
                    "activity_states": activity_states,
                    "colliding_utc": colliding_utc,
                    "enterprise_ids": enterprise_ids,
                    "service_overbooking_limit_ids": service_overbooking_limit_ids,
                    "updated_utc": updated_utc,
                },
                service_overbooking_limit_list_params.ServiceOverbookingLimitListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServiceOverbookingLimitListResponse,
        )

    async def clear(
        self,
        *,
        access_token: str,
        clear_service_overbooking_limits: Iterable[service_overbooking_limit_clear_params.ClearServiceOverbookingLimit],
        client: str,
        client_token: str,
        service_id: str,
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Deletes service overbooking limits that exactly match the specified conditions.
        This operation is intended to be used alongside `serviceOverbookingLimits/set`.
        The specified conditions must be met exactly. The time interval, however, does
        not need to correspond to an existing service overbooking limit in the system,
        instead the API uses a splicing algorithm to work out how to divide up any
        existing service overbooking limit to meet the specified time interval. Past
        overbooking limits cannot be cleared outside of
        `OperationalEditableHistoryInterval`. Care is needed to specify
        `FirstTimeUnitStartUtc` and `LastTimeUnitStartUtc` in the correct format - see
        [Datetimes](https://mews-systems.gitbook.io/connector-api/guidelines/serialization#datetimes).
        This operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        Args:
          access_token: Access token of the client application.

          clear_service_overbooking_limits: Collection of service overbooking limits to be cleared.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          service_id: Unique identifier of the
              [Service](https://mews-systems.gitbook.io/connector-api/operations/services#service)
              overbooking limits will be set in.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/serviceOverbookingLimits/clear",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "clear_service_overbooking_limits": clear_service_overbooking_limits,
                    "client": client,
                    "client_token": client_token,
                    "service_id": service_id,
                    "enterprise_id": enterprise_id,
                },
                service_overbooking_limit_clear_params.ServiceOverbookingLimitClearParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def set(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        service_id: str,
        set_service_overbooking_limits: Iterable[service_overbooking_limit_set_params.SetServiceOverbookingLimit],
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Adds new service overbooking limits with the specified conditions.

        Past
        overbooking limits cannot be updated outside of
        `OperationalEditableHistoryInterval`. Care is needed to specify
        `FirstTimeUnitStartUtc` and `LastTimeUnitStartUtc` in the correct format - see
        [Datetimes](https://mews-systems.gitbook.io/connector-api/guidelines/serialization#datetimes).
        This operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          service_id: Unique identifier of the
              [Service](https://mews-systems.gitbook.io/connector-api/operations/services#service)
              overbooking limits will be set in.

          set_service_overbooking_limits: Collection of service overbooking limits to be set.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/serviceOverbookingLimits/set",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "service_id": service_id,
                    "set_service_overbooking_limits": set_service_overbooking_limits,
                    "enterprise_id": enterprise_id,
                },
                service_overbooking_limit_set_params.ServiceOverbookingLimitSetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class ServiceOverbookingLimitsResourceWithRawResponse:
    def __init__(self, service_overbooking_limits: ServiceOverbookingLimitsResource) -> None:
        self._service_overbooking_limits = service_overbooking_limits

        self.list = to_raw_response_wrapper(
            service_overbooking_limits.list,
        )
        self.clear = to_raw_response_wrapper(
            service_overbooking_limits.clear,
        )
        self.set = to_raw_response_wrapper(
            service_overbooking_limits.set,
        )


class AsyncServiceOverbookingLimitsResourceWithRawResponse:
    def __init__(self, service_overbooking_limits: AsyncServiceOverbookingLimitsResource) -> None:
        self._service_overbooking_limits = service_overbooking_limits

        self.list = async_to_raw_response_wrapper(
            service_overbooking_limits.list,
        )
        self.clear = async_to_raw_response_wrapper(
            service_overbooking_limits.clear,
        )
        self.set = async_to_raw_response_wrapper(
            service_overbooking_limits.set,
        )


class ServiceOverbookingLimitsResourceWithStreamingResponse:
    def __init__(self, service_overbooking_limits: ServiceOverbookingLimitsResource) -> None:
        self._service_overbooking_limits = service_overbooking_limits

        self.list = to_streamed_response_wrapper(
            service_overbooking_limits.list,
        )
        self.clear = to_streamed_response_wrapper(
            service_overbooking_limits.clear,
        )
        self.set = to_streamed_response_wrapper(
            service_overbooking_limits.set,
        )


class AsyncServiceOverbookingLimitsResourceWithStreamingResponse:
    def __init__(self, service_overbooking_limits: AsyncServiceOverbookingLimitsResource) -> None:
        self._service_overbooking_limits = service_overbooking_limits

        self.list = async_to_streamed_response_wrapper(
            service_overbooking_limits.list,
        )
        self.clear = async_to_streamed_response_wrapper(
            service_overbooking_limits.clear,
        )
        self.set = async_to_streamed_response_wrapper(
            service_overbooking_limits.set,
        )
