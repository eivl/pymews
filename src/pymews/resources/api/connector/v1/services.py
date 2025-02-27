# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
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
    service_list_params,
    service_get_availability_params,
    service_update_availability_params,
    service_get_availability_2024_01_22_params,
)
from .....types.api.connector.v1.service_list_response import ServiceListResponse
from .....types.api.connector.v1.service_get_availability_response import ServiceGetAvailabilityResponse
from .....types.api.connector.v1.service_get_availability_2024_01_22_response import (
    ServiceGetAvailability2024_01_22Response,
)

__all__ = ["ServicesResource", "AsyncServicesResource"]


class ServicesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ServicesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return ServicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ServicesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return ServicesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: service_list_params.Limitation,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        service_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[service_list_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ServiceListResponse:
        """Returns all services offered by the enterprise.

        Note this operation uses
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

          service_ids: Unique identifiers of
              [Services](https://mews-systems.gitbook.io/connector-api/operations/services/#service).

          updated_utc: Interval in which `Services` were updated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/services/getAll",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "enterprise_ids": enterprise_ids,
                    "service_ids": service_ids,
                    "updated_utc": updated_utc,
                },
                service_list_params.ServiceListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServiceListResponse,
        )

    def get_availability(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        first_time_unit_start_utc: Union[str, datetime],
        last_time_unit_start_utc: Union[str, datetime],
        service_id: str,
        end_utc: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        start_utc: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ServiceGetAvailabilityResponse:
        """
        Returns availability of a bookable service for a specified time interval
        including applied availability adjustments. Availability will be returned for
        all service time units that the specified time interval intersects. So, for
        example, an interval `1st Jan 23:00 UTC - 1st Jan 23:00 UTC` will result in one
        price for `2nd Jan`, while Interval `1st Jan 23:00 UTC - 2nd Jan 23:00 UTC` will
        result in two prices for `2nd Jan` and `3rd Jan` (assuming a time unit period of
        "Day"). UTC timestamps must correspond to the start boundary of a time unit,
        e.g. 00:00 converted to UTC for a time unit of "Day". Other timestamps are not
        permitted. The **maximum size of time interval** depends on the service's time
        unit: 367 hours if hours, 367 days if days, or 60 months if months. For more
        information about time units, see
        [Time unit](https://mews-systems.gitbook.io/connector-api/concepts/time-units).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          first_time_unit_start_utc: Start of the time interval, expressed as the timestamp for the start of the
              first
              [time unit](https://mews-systems.gitbook.io/connector-api/concepts/time-units/),
              in UTC timezone ISO 8601 format.

          last_time_unit_start_utc: End of the time interval, expressed as the timestamp for the start of the last
              [time unit](https://mews-systems.gitbook.io/connector-api/concepts/time-units/),
              in UTC timezone ISO 8601 format. The maximum size of time interval depends on
              the service's
              [time unit](https://mews-systems.gitbook.io/connector-api/concepts/time-units/):
              367 hours if hours, 367 days if days, or 60 months if months.

          service_id: Unique identifier of the
              [Service](https://mews-systems.gitbook.io/connector-api/operations/#service)
              whose availability should be returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/services/getAvailability",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "first_time_unit_start_utc": first_time_unit_start_utc,
                    "last_time_unit_start_utc": last_time_unit_start_utc,
                    "service_id": service_id,
                    "end_utc": end_utc,
                    "start_utc": start_utc,
                },
                service_get_availability_params.ServiceGetAvailabilityParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServiceGetAvailabilityResponse,
        )

    def get_availability_2024_01_22(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        first_time_unit_start_utc: Union[str, datetime],
        last_time_unit_start_utc: Union[str, datetime],
        metrics: List[
            Literal[
                "OutOfOrderBlocks",
                "PublicAvailabilityAdjustment",
                "OtherServiceReservationCount",
                "Occupied",
                "ConfirmedReservations",
                "OptionalReservations",
                "BlockAvailability",
                "AllocatedBlockAvailability",
                "UsableResources",
                "ActiveResources",
            ]
        ],
        service_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ServiceGetAvailability2024_01_22Response:
        """
        Returns selected availability and occupancy metrics of a bookable service for a
        specified time interval, similar to
        [the availability & occupancy report](https://help.mews.com/s/article/Availability-Occupancy-report).
        Availability will be returned for all service time units that the specified time
        interval intersects. So, for example, an interval
        `1st Jan 23:00 UTC - 1st Jan 23:00 UTC` will result in one time unit for
        `2nd Jan`, while Interval `1st Jan 23:00 UTC - 2nd Jan 23:00 UTC` will result in
        two time units for `2nd Jan` and `3rd Jan` (assuming a time unit period of
        "Day"). UTC timestamps must correspond to the start boundary of a time unit,
        e.g. 00:00 converted to UTC for a time unit of "Day". Other timestamps are not
        permitted. The **maximum size of time interval** depends on the service's time
        unit: 367 hours if hours, 367 days if days, or 60 months if months. For more
        information about time units, see
        [Time unit](https://mews-systems.gitbook.io/connector-api/concepts/time-units).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          first_time_unit_start_utc: Start of the time interval, expressed as the timestamp for the start of the
              first
              [time unit](https://mews-systems.gitbook.io/connector-api/concepts/time-units/),
              in UTC timezone ISO 8601 format.

          last_time_unit_start_utc: End of the time interval, expressed as the timestamp for the start of the last
              [time unit](https://mews-systems.gitbook.io/connector-api/concepts/time-units/),
              in UTC timezone ISO 8601 format. The maximum size of time interval depends on
              the service's
              [time unit](https://mews-systems.gitbook.io/connector-api/concepts/time-units/):
              367 hours if hours, 367 days if days, or 60 months if months.

          metrics: Set of
              [Service availability metrics](https://mews-systems.gitbook.io/connector-api/operations/services/#service-availability-metrics)
              to be returned.

          service_id: Unique identifier of the
              [Service](https://mews-systems.gitbook.io/connector-api/operations/services/#service)
              whose availability should be returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/services/getAvailability/2024-01-22",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "first_time_unit_start_utc": first_time_unit_start_utc,
                    "last_time_unit_start_utc": last_time_unit_start_utc,
                    "metrics": metrics,
                    "service_id": service_id,
                },
                service_get_availability_2024_01_22_params.ServiceGetAvailability2024_01_22Params,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServiceGetAvailability2024_01_22Response,
        )

    def update_availability(
        self,
        *,
        access_token: str,
        availability_updates: Iterable[service_update_availability_params.AvailabilityUpdate],
        client: str,
        client_token: str,
        service_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Updates the number of available resources in
        [Resource category](https://mews-systems.gitbook.io/connector-api/operations/resources/#resource-category)
        by a certain amount (relative adjustment). Note that availabilities are defined
        per time unit, so when the server receives the UTC interval, it first converts
        it to enterprise timezone and updates the availability on all time units that
        the interval intersects. It's not allowed to update past availabilities outside
        of `EditableHistoryInterval`, future updates are allowed for up to 5 years.

        Args:
          access_token: Access token of the client application.

          availability_updates: Availability updates.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          service_id: Unique identifier of the
              [Service](https://mews-systems.gitbook.io/connector-api/operations/#service) to
              update.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/services/updateAvailability",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "availability_updates": availability_updates,
                    "client": client,
                    "client_token": client_token,
                    "service_id": service_id,
                },
                service_update_availability_params.ServiceUpdateAvailabilityParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncServicesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncServicesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return AsyncServicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncServicesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return AsyncServicesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: service_list_params.Limitation,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        service_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[service_list_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ServiceListResponse:
        """Returns all services offered by the enterprise.

        Note this operation uses
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

          service_ids: Unique identifiers of
              [Services](https://mews-systems.gitbook.io/connector-api/operations/services/#service).

          updated_utc: Interval in which `Services` were updated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/services/getAll",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "enterprise_ids": enterprise_ids,
                    "service_ids": service_ids,
                    "updated_utc": updated_utc,
                },
                service_list_params.ServiceListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServiceListResponse,
        )

    async def get_availability(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        first_time_unit_start_utc: Union[str, datetime],
        last_time_unit_start_utc: Union[str, datetime],
        service_id: str,
        end_utc: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        start_utc: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ServiceGetAvailabilityResponse:
        """
        Returns availability of a bookable service for a specified time interval
        including applied availability adjustments. Availability will be returned for
        all service time units that the specified time interval intersects. So, for
        example, an interval `1st Jan 23:00 UTC - 1st Jan 23:00 UTC` will result in one
        price for `2nd Jan`, while Interval `1st Jan 23:00 UTC - 2nd Jan 23:00 UTC` will
        result in two prices for `2nd Jan` and `3rd Jan` (assuming a time unit period of
        "Day"). UTC timestamps must correspond to the start boundary of a time unit,
        e.g. 00:00 converted to UTC for a time unit of "Day". Other timestamps are not
        permitted. The **maximum size of time interval** depends on the service's time
        unit: 367 hours if hours, 367 days if days, or 60 months if months. For more
        information about time units, see
        [Time unit](https://mews-systems.gitbook.io/connector-api/concepts/time-units).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          first_time_unit_start_utc: Start of the time interval, expressed as the timestamp for the start of the
              first
              [time unit](https://mews-systems.gitbook.io/connector-api/concepts/time-units/),
              in UTC timezone ISO 8601 format.

          last_time_unit_start_utc: End of the time interval, expressed as the timestamp for the start of the last
              [time unit](https://mews-systems.gitbook.io/connector-api/concepts/time-units/),
              in UTC timezone ISO 8601 format. The maximum size of time interval depends on
              the service's
              [time unit](https://mews-systems.gitbook.io/connector-api/concepts/time-units/):
              367 hours if hours, 367 days if days, or 60 months if months.

          service_id: Unique identifier of the
              [Service](https://mews-systems.gitbook.io/connector-api/operations/#service)
              whose availability should be returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/services/getAvailability",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "first_time_unit_start_utc": first_time_unit_start_utc,
                    "last_time_unit_start_utc": last_time_unit_start_utc,
                    "service_id": service_id,
                    "end_utc": end_utc,
                    "start_utc": start_utc,
                },
                service_get_availability_params.ServiceGetAvailabilityParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServiceGetAvailabilityResponse,
        )

    async def get_availability_2024_01_22(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        first_time_unit_start_utc: Union[str, datetime],
        last_time_unit_start_utc: Union[str, datetime],
        metrics: List[
            Literal[
                "OutOfOrderBlocks",
                "PublicAvailabilityAdjustment",
                "OtherServiceReservationCount",
                "Occupied",
                "ConfirmedReservations",
                "OptionalReservations",
                "BlockAvailability",
                "AllocatedBlockAvailability",
                "UsableResources",
                "ActiveResources",
            ]
        ],
        service_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ServiceGetAvailability2024_01_22Response:
        """
        Returns selected availability and occupancy metrics of a bookable service for a
        specified time interval, similar to
        [the availability & occupancy report](https://help.mews.com/s/article/Availability-Occupancy-report).
        Availability will be returned for all service time units that the specified time
        interval intersects. So, for example, an interval
        `1st Jan 23:00 UTC - 1st Jan 23:00 UTC` will result in one time unit for
        `2nd Jan`, while Interval `1st Jan 23:00 UTC - 2nd Jan 23:00 UTC` will result in
        two time units for `2nd Jan` and `3rd Jan` (assuming a time unit period of
        "Day"). UTC timestamps must correspond to the start boundary of a time unit,
        e.g. 00:00 converted to UTC for a time unit of "Day". Other timestamps are not
        permitted. The **maximum size of time interval** depends on the service's time
        unit: 367 hours if hours, 367 days if days, or 60 months if months. For more
        information about time units, see
        [Time unit](https://mews-systems.gitbook.io/connector-api/concepts/time-units).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          first_time_unit_start_utc: Start of the time interval, expressed as the timestamp for the start of the
              first
              [time unit](https://mews-systems.gitbook.io/connector-api/concepts/time-units/),
              in UTC timezone ISO 8601 format.

          last_time_unit_start_utc: End of the time interval, expressed as the timestamp for the start of the last
              [time unit](https://mews-systems.gitbook.io/connector-api/concepts/time-units/),
              in UTC timezone ISO 8601 format. The maximum size of time interval depends on
              the service's
              [time unit](https://mews-systems.gitbook.io/connector-api/concepts/time-units/):
              367 hours if hours, 367 days if days, or 60 months if months.

          metrics: Set of
              [Service availability metrics](https://mews-systems.gitbook.io/connector-api/operations/services/#service-availability-metrics)
              to be returned.

          service_id: Unique identifier of the
              [Service](https://mews-systems.gitbook.io/connector-api/operations/services/#service)
              whose availability should be returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/services/getAvailability/2024-01-22",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "first_time_unit_start_utc": first_time_unit_start_utc,
                    "last_time_unit_start_utc": last_time_unit_start_utc,
                    "metrics": metrics,
                    "service_id": service_id,
                },
                service_get_availability_2024_01_22_params.ServiceGetAvailability2024_01_22Params,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServiceGetAvailability2024_01_22Response,
        )

    async def update_availability(
        self,
        *,
        access_token: str,
        availability_updates: Iterable[service_update_availability_params.AvailabilityUpdate],
        client: str,
        client_token: str,
        service_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Updates the number of available resources in
        [Resource category](https://mews-systems.gitbook.io/connector-api/operations/resources/#resource-category)
        by a certain amount (relative adjustment). Note that availabilities are defined
        per time unit, so when the server receives the UTC interval, it first converts
        it to enterprise timezone and updates the availability on all time units that
        the interval intersects. It's not allowed to update past availabilities outside
        of `EditableHistoryInterval`, future updates are allowed for up to 5 years.

        Args:
          access_token: Access token of the client application.

          availability_updates: Availability updates.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          service_id: Unique identifier of the
              [Service](https://mews-systems.gitbook.io/connector-api/operations/#service) to
              update.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/services/updateAvailability",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "availability_updates": availability_updates,
                    "client": client,
                    "client_token": client_token,
                    "service_id": service_id,
                },
                service_update_availability_params.ServiceUpdateAvailabilityParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class ServicesResourceWithRawResponse:
    def __init__(self, services: ServicesResource) -> None:
        self._services = services

        self.list = to_raw_response_wrapper(
            services.list,
        )
        self.get_availability = to_raw_response_wrapper(
            services.get_availability,
        )
        self.get_availability_2024_01_22 = to_raw_response_wrapper(
            services.get_availability_2024_01_22,
        )
        self.update_availability = to_raw_response_wrapper(
            services.update_availability,
        )


class AsyncServicesResourceWithRawResponse:
    def __init__(self, services: AsyncServicesResource) -> None:
        self._services = services

        self.list = async_to_raw_response_wrapper(
            services.list,
        )
        self.get_availability = async_to_raw_response_wrapper(
            services.get_availability,
        )
        self.get_availability_2024_01_22 = async_to_raw_response_wrapper(
            services.get_availability_2024_01_22,
        )
        self.update_availability = async_to_raw_response_wrapper(
            services.update_availability,
        )


class ServicesResourceWithStreamingResponse:
    def __init__(self, services: ServicesResource) -> None:
        self._services = services

        self.list = to_streamed_response_wrapper(
            services.list,
        )
        self.get_availability = to_streamed_response_wrapper(
            services.get_availability,
        )
        self.get_availability_2024_01_22 = to_streamed_response_wrapper(
            services.get_availability_2024_01_22,
        )
        self.update_availability = to_streamed_response_wrapper(
            services.update_availability,
        )


class AsyncServicesResourceWithStreamingResponse:
    def __init__(self, services: AsyncServicesResource) -> None:
        self._services = services

        self.list = async_to_streamed_response_wrapper(
            services.list,
        )
        self.get_availability = async_to_streamed_response_wrapper(
            services.get_availability,
        )
        self.get_availability_2024_01_22 = async_to_streamed_response_wrapper(
            services.get_availability_2024_01_22,
        )
        self.update_availability = async_to_streamed_response_wrapper(
            services.update_availability,
        )
