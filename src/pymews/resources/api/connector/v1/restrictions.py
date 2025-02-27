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
    restriction_add_params,
    restriction_set_params,
    restriction_list_params,
    restriction_clear_params,
    restriction_delete_params,
)
from .....types.api.connector.v1.restriction_add_response import RestrictionAddResponse
from .....types.api.connector.v1.restriction_list_response import RestrictionListResponse

__all__ = ["RestrictionsResource", "AsyncRestrictionsResource"]


class RestrictionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RestrictionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return RestrictionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RestrictionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return RestrictionsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: restriction_list_params.Limitation,
        service_ids: List[str],
        base_rate_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        colliding_utc: Optional[restriction_list_params.CollidingUtc] | NotGiven = NOT_GIVEN,
        created_utc: Optional[restriction_list_params.CreatedUtc] | NotGiven = NOT_GIVEN,
        end_utc: Optional[str] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        exact_rate_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        origin: Optional[Literal["User", "Integration"]] | NotGiven = NOT_GIVEN,
        rate_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        resource_category_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        restriction_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        start_utc: Optional[str] | NotGiven = NOT_GIVEN,
        time_filter: Optional[str] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[restriction_list_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RestrictionListResponse:
        """Returns all restrictions of the default service provided by the enterprise.

        Note
        this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          service_ids: Unique identifiers of the `Service` from which the restrictions are requested.

          base_rate_ids: Unique identifiers of `Rate`. Returns only those restrictions which have
              matching `BaseRateId` set in `Restriction Condition`.

          colliding_utc: Interval in which the `Restriction` is active.

          created_utc: Interval in which the `Restriction` was created.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          exact_rate_ids: Unique identifiers of `Rate`. Returns only those restrictions which have
              matching `ExactRateId` set in `Restriction Condition`.

          origin: Restriction origin. Returns only those restrictions which have matching Origin
              or all if not specified.

              - `User` - Restriction was created by a user in Mews.
              - `Integration` - Restriction was created by a 3rd-party integration.

          rate_ids: Unique identifiers of `Rate`. Returns all restrictions that affect the given
              rates, i.e. ones without any `Restriction Conditions`, ones assigned directly to
              specified rates, ones assigned to `Rate group` of specified rates, or ones
              inherited from base rates.`.

          resource_category_ids: Unique identifiers of `Resource category`.

          restriction_ids: Unique identifiers of the `Restriction`.

          updated_utc: Interval in which the `Restriction` was updated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/restrictions/getAll",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "service_ids": service_ids,
                    "base_rate_ids": base_rate_ids,
                    "colliding_utc": colliding_utc,
                    "created_utc": created_utc,
                    "end_utc": end_utc,
                    "enterprise_ids": enterprise_ids,
                    "exact_rate_ids": exact_rate_ids,
                    "origin": origin,
                    "rate_ids": rate_ids,
                    "resource_category_ids": resource_category_ids,
                    "restriction_ids": restriction_ids,
                    "start_utc": start_utc,
                    "time_filter": time_filter,
                    "updated_utc": updated_utc,
                },
                restriction_list_params.RestrictionListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RestrictionListResponse,
        )

    def delete(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        restriction_ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Removes restrictions from the service.

        This operation is intended to be used
        alongside
        [Add restrictions](https://mews-systems.gitbook.io/connector-api/operations/restrictions#set-restrictions).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          restriction_ids: Unique identifiers of the `Restriction`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/restrictions/delete",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "restriction_ids": restriction_ids,
                },
                restriction_delete_params.RestrictionDeleteParams,
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
        restrictions: Iterable[restriction_add_params.Restriction],
        service_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RestrictionAddResponse:
        """Adds new restrictions with the specified conditions.

        Care is needed to specify
        `StartUtc` and `EndUtc` in the correct format - see
        [Datetimes](https://mews-systems.gitbook.io/connector-api/guidelines/serialization#datetimes).
        **Important:** If consecutive restrictions are sent with the exact same
        conditions and exceptions, no attempt at merging them into a single restriction
        is made. This means that there can be a large number of restrictions per
        service, leading to sub-optimal performance. A quota limit of 150,000 has been
        introduced for this reason. To mitigate the issue, the preferred way to add
        restrictions is operation
        [Set restriction](https://mews-systems.gitbook.io/connector-api/operations/restrictions#set-restrictions).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          restrictions: Parameters of restrictions.

          service_id: Unique identifier of the
              [Service](https://mews-systems.gitbook.io/connector-api/operations/services/#service)
              restrictions will be added in.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/restrictions/add",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "restrictions": restrictions,
                    "service_id": service_id,
                },
                restriction_add_params.RestrictionAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RestrictionAddResponse,
        )

    def clear(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        data: Iterable[restriction_clear_params.Data],
        service_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Deletes restrictions that exactly match the specified conditions, using a
        splicing algorithm. This operation is intended to be used alongside
        [Set restrictions](https://mews-systems.gitbook.io/connector-api/operations/restrictions#set-restrictions).
        The specified conditions must be met exactly. The time interval, however, does
        not need to correspond to an existing restriction in the system, instead the API
        uses a splicing algorithm to work out how to divide up any existing restrictions
        to meet the specified time interval. For details about matching conditions and
        the splicing algorithm, see
        [Concepts > Restrictions](https://mews-systems.gitbook.io/connector-api/concepts/restrictions).

        Only restrictions created through the API are affected by this operation, _not_
        restrictions created by the user within **Mews Operations**. Similarly, if a
        user creates a restriction in **Mews Operations**, this will _not_ affect
        restrictions created through the API.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          data: Details of the matching conditions and time intervals for clearing restrictions.

          service_id: Unique identifier of the
              [Service](https://mews-systems.gitbook.io/connector-api/operations/services#service)
              to which the restrictions apply.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/restrictions/clear",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "data": data,
                    "service_id": service_id,
                },
                restriction_clear_params.RestrictionClearParams,
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
        data: Iterable[restriction_set_params.Data],
        service_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Adds new restrictions with the specified conditions.

        For improved efficiency,
        multiple similar restrictions will be merged into a single restriction. A quota
        of 150,000 restrictions per service applies, although it is unlikely to be
        exceeded because of the merging algorithm. For more information about the
        merging algorithm, see
        [Concepts > Restrictions](https://mews-systems.gitbook.io/connector-api/concepts/restrictions).

        Care is needed to specify `StartUtc` and `EndUtc` in the correct format - see
        [Datetimes](https://mews-systems.gitbook.io/connector-api/guidelines/serialization#datetimes).
        If migrating from deprecated operation
        [Add restrictions](https://mews-systems.gitbook.io/connector-api/operations/restrictions#add-restrictions),
        note that the validation of these properties is stronger in this operation.

        Only restrictions created through the API are affected by this operation, _not_
        restrictions created by the user within **Mews Operations**. Similarly, if a
        user creates a restriction in **Mews Operations**, this will _not_ affect
        restrictions created through the API.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          data: Parameters of restrictions.

          service_id: Unique identifier of the
              [Service](https://mews-systems.gitbook.io/connector-api/operations/services#service)
              restrictions will be set in.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/restrictions/set",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "data": data,
                    "service_id": service_id,
                },
                restriction_set_params.RestrictionSetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncRestrictionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRestrictionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return AsyncRestrictionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRestrictionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return AsyncRestrictionsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: restriction_list_params.Limitation,
        service_ids: List[str],
        base_rate_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        colliding_utc: Optional[restriction_list_params.CollidingUtc] | NotGiven = NOT_GIVEN,
        created_utc: Optional[restriction_list_params.CreatedUtc] | NotGiven = NOT_GIVEN,
        end_utc: Optional[str] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        exact_rate_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        origin: Optional[Literal["User", "Integration"]] | NotGiven = NOT_GIVEN,
        rate_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        resource_category_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        restriction_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        start_utc: Optional[str] | NotGiven = NOT_GIVEN,
        time_filter: Optional[str] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[restriction_list_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RestrictionListResponse:
        """Returns all restrictions of the default service provided by the enterprise.

        Note
        this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          service_ids: Unique identifiers of the `Service` from which the restrictions are requested.

          base_rate_ids: Unique identifiers of `Rate`. Returns only those restrictions which have
              matching `BaseRateId` set in `Restriction Condition`.

          colliding_utc: Interval in which the `Restriction` is active.

          created_utc: Interval in which the `Restriction` was created.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          exact_rate_ids: Unique identifiers of `Rate`. Returns only those restrictions which have
              matching `ExactRateId` set in `Restriction Condition`.

          origin: Restriction origin. Returns only those restrictions which have matching Origin
              or all if not specified.

              - `User` - Restriction was created by a user in Mews.
              - `Integration` - Restriction was created by a 3rd-party integration.

          rate_ids: Unique identifiers of `Rate`. Returns all restrictions that affect the given
              rates, i.e. ones without any `Restriction Conditions`, ones assigned directly to
              specified rates, ones assigned to `Rate group` of specified rates, or ones
              inherited from base rates.`.

          resource_category_ids: Unique identifiers of `Resource category`.

          restriction_ids: Unique identifiers of the `Restriction`.

          updated_utc: Interval in which the `Restriction` was updated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/restrictions/getAll",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "service_ids": service_ids,
                    "base_rate_ids": base_rate_ids,
                    "colliding_utc": colliding_utc,
                    "created_utc": created_utc,
                    "end_utc": end_utc,
                    "enterprise_ids": enterprise_ids,
                    "exact_rate_ids": exact_rate_ids,
                    "origin": origin,
                    "rate_ids": rate_ids,
                    "resource_category_ids": resource_category_ids,
                    "restriction_ids": restriction_ids,
                    "start_utc": start_utc,
                    "time_filter": time_filter,
                    "updated_utc": updated_utc,
                },
                restriction_list_params.RestrictionListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RestrictionListResponse,
        )

    async def delete(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        restriction_ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Removes restrictions from the service.

        This operation is intended to be used
        alongside
        [Add restrictions](https://mews-systems.gitbook.io/connector-api/operations/restrictions#set-restrictions).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          restriction_ids: Unique identifiers of the `Restriction`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/restrictions/delete",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "restriction_ids": restriction_ids,
                },
                restriction_delete_params.RestrictionDeleteParams,
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
        restrictions: Iterable[restriction_add_params.Restriction],
        service_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RestrictionAddResponse:
        """Adds new restrictions with the specified conditions.

        Care is needed to specify
        `StartUtc` and `EndUtc` in the correct format - see
        [Datetimes](https://mews-systems.gitbook.io/connector-api/guidelines/serialization#datetimes).
        **Important:** If consecutive restrictions are sent with the exact same
        conditions and exceptions, no attempt at merging them into a single restriction
        is made. This means that there can be a large number of restrictions per
        service, leading to sub-optimal performance. A quota limit of 150,000 has been
        introduced for this reason. To mitigate the issue, the preferred way to add
        restrictions is operation
        [Set restriction](https://mews-systems.gitbook.io/connector-api/operations/restrictions#set-restrictions).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          restrictions: Parameters of restrictions.

          service_id: Unique identifier of the
              [Service](https://mews-systems.gitbook.io/connector-api/operations/services/#service)
              restrictions will be added in.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/restrictions/add",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "restrictions": restrictions,
                    "service_id": service_id,
                },
                restriction_add_params.RestrictionAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RestrictionAddResponse,
        )

    async def clear(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        data: Iterable[restriction_clear_params.Data],
        service_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Deletes restrictions that exactly match the specified conditions, using a
        splicing algorithm. This operation is intended to be used alongside
        [Set restrictions](https://mews-systems.gitbook.io/connector-api/operations/restrictions#set-restrictions).
        The specified conditions must be met exactly. The time interval, however, does
        not need to correspond to an existing restriction in the system, instead the API
        uses a splicing algorithm to work out how to divide up any existing restrictions
        to meet the specified time interval. For details about matching conditions and
        the splicing algorithm, see
        [Concepts > Restrictions](https://mews-systems.gitbook.io/connector-api/concepts/restrictions).

        Only restrictions created through the API are affected by this operation, _not_
        restrictions created by the user within **Mews Operations**. Similarly, if a
        user creates a restriction in **Mews Operations**, this will _not_ affect
        restrictions created through the API.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          data: Details of the matching conditions and time intervals for clearing restrictions.

          service_id: Unique identifier of the
              [Service](https://mews-systems.gitbook.io/connector-api/operations/services#service)
              to which the restrictions apply.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/restrictions/clear",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "data": data,
                    "service_id": service_id,
                },
                restriction_clear_params.RestrictionClearParams,
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
        data: Iterable[restriction_set_params.Data],
        service_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Adds new restrictions with the specified conditions.

        For improved efficiency,
        multiple similar restrictions will be merged into a single restriction. A quota
        of 150,000 restrictions per service applies, although it is unlikely to be
        exceeded because of the merging algorithm. For more information about the
        merging algorithm, see
        [Concepts > Restrictions](https://mews-systems.gitbook.io/connector-api/concepts/restrictions).

        Care is needed to specify `StartUtc` and `EndUtc` in the correct format - see
        [Datetimes](https://mews-systems.gitbook.io/connector-api/guidelines/serialization#datetimes).
        If migrating from deprecated operation
        [Add restrictions](https://mews-systems.gitbook.io/connector-api/operations/restrictions#add-restrictions),
        note that the validation of these properties is stronger in this operation.

        Only restrictions created through the API are affected by this operation, _not_
        restrictions created by the user within **Mews Operations**. Similarly, if a
        user creates a restriction in **Mews Operations**, this will _not_ affect
        restrictions created through the API.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          data: Parameters of restrictions.

          service_id: Unique identifier of the
              [Service](https://mews-systems.gitbook.io/connector-api/operations/services#service)
              restrictions will be set in.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/restrictions/set",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "data": data,
                    "service_id": service_id,
                },
                restriction_set_params.RestrictionSetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class RestrictionsResourceWithRawResponse:
    def __init__(self, restrictions: RestrictionsResource) -> None:
        self._restrictions = restrictions

        self.list = to_raw_response_wrapper(
            restrictions.list,
        )
        self.delete = to_raw_response_wrapper(
            restrictions.delete,
        )
        self.add = to_raw_response_wrapper(
            restrictions.add,
        )
        self.clear = to_raw_response_wrapper(
            restrictions.clear,
        )
        self.set = to_raw_response_wrapper(
            restrictions.set,
        )


class AsyncRestrictionsResourceWithRawResponse:
    def __init__(self, restrictions: AsyncRestrictionsResource) -> None:
        self._restrictions = restrictions

        self.list = async_to_raw_response_wrapper(
            restrictions.list,
        )
        self.delete = async_to_raw_response_wrapper(
            restrictions.delete,
        )
        self.add = async_to_raw_response_wrapper(
            restrictions.add,
        )
        self.clear = async_to_raw_response_wrapper(
            restrictions.clear,
        )
        self.set = async_to_raw_response_wrapper(
            restrictions.set,
        )


class RestrictionsResourceWithStreamingResponse:
    def __init__(self, restrictions: RestrictionsResource) -> None:
        self._restrictions = restrictions

        self.list = to_streamed_response_wrapper(
            restrictions.list,
        )
        self.delete = to_streamed_response_wrapper(
            restrictions.delete,
        )
        self.add = to_streamed_response_wrapper(
            restrictions.add,
        )
        self.clear = to_streamed_response_wrapper(
            restrictions.clear,
        )
        self.set = to_streamed_response_wrapper(
            restrictions.set,
        )


class AsyncRestrictionsResourceWithStreamingResponse:
    def __init__(self, restrictions: AsyncRestrictionsResource) -> None:
        self._restrictions = restrictions

        self.list = async_to_streamed_response_wrapper(
            restrictions.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            restrictions.delete,
        )
        self.add = async_to_streamed_response_wrapper(
            restrictions.add,
        )
        self.clear = async_to_streamed_response_wrapper(
            restrictions.clear,
        )
        self.set = async_to_streamed_response_wrapper(
            restrictions.set,
        )
