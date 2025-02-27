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
    rate_add_params,
    rate_set_params,
    rate_list_params,
    rate_delete_params,
    rate_get_pricing_params,
    rate_update_price_params,
)
from .....types.api.connector.v1.rate_add_response import RateAddResponse
from .....types.api.connector.v1.rate_set_response import RateSetResponse
from .....types.api.connector.v1.rate_list_response import RateListResponse
from .....types.api.connector.v1.rate_get_pricing_response import RateGetPricingResponse

__all__ = ["RatesResource", "AsyncRatesResource"]


class RatesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return RatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return RatesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: rate_list_params.Limitation,
        service_ids: List[str],
        activity_states: Optional[List[Literal["Deleted", "Active"]]] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        extent: Optional[rate_list_params.Extent] | NotGiven = NOT_GIVEN,
        external_identifiers: Optional[List[str]] | NotGiven = NOT_GIVEN,
        rate_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[rate_list_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RateListResponse:
        """
        Returns all rates (pricing setups) of the default service provided by the
        enterprise. Note this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          service_ids: Unique identifiers of the
              [Services](https://mews-systems.gitbook.io/connector-api/operations/services/#service)
              from which the rates are requested.

          activity_states: Whether to return only active, only deleted, or both types of record. If not
              specified, both active and deleted will be returned.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          extent: Extent of data to be returned.

          external_identifiers: Identifiers of
              [Rate](https://mews-systems.gitbook.io/connector-api/operations/#rate) from
              external systems.

          rate_ids: Unique identifiers of the requested
              [Rates](https://mews-systems.gitbook.io/connector-api/operations/rates/#rate).

          updated_utc: Interval in which `Rate` was updated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/rates/getAll",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "service_ids": service_ids,
                    "activity_states": activity_states,
                    "enterprise_ids": enterprise_ids,
                    "extent": extent,
                    "external_identifiers": external_identifiers,
                    "rate_ids": rate_ids,
                    "updated_utc": updated_utc,
                },
                rate_list_params.RateListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RateListResponse,
        )

    def delete(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        rate_ids: List[str],
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Deletes specified rates.

        This operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          rate_ids: Unique identifiers of the rates to be deleted.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/rates/delete",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "rate_ids": rate_ids,
                    "enterprise_id": enterprise_id,
                },
                rate_delete_params.RateDeleteParams,
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
        rates: Iterable[rate_add_params.Rate],
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RateAddResponse:
        """Adds rates to the enterprise.

        Note this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).
        Rate type of `AvailabilityBlock` cannot be created via this operation.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          rates: Information about rates to be created.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/rates/add",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "rates": rates,
                    "enterprise_id": enterprise_id,
                },
                rate_add_params.RateAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RateAddResponse,
        )

    def get_pricing(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        first_time_unit_start_utc: Union[str, datetime],
        last_time_unit_start_utc: Union[str, datetime],
        rate_id: str,
        product_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RateGetPricingResponse:
        """Returns prices for a given rate for a specified time interval.

        Prices will be
        returned for all service time units that the specified time interval intersects.
        So, for example, an interval `1st Jan 23:00 UTC - 1st Jan 23:00 UTC` will result
        in one price for `2nd Jan`, while Interval
        `1st Jan 23:00 UTC - 2nd Jan 23:00 UTC` will result in two prices for `2nd Jan`
        and `3rd Jan` (assuming a time unit period of "Day"). UTC timestamps must
        correspond to the start boundary of a time unit, e.g. 00:00 converted to UTC for
        a time unit of "Day". Other timestamps are not permitted. The **maximum size of
        time interval** depends on the service's time unit: 367 hours if hours, 367 days
        if days, or 60 months if months. For more information about time units, see
        [Time units](https://mews-systems.gitbook.io/connector-api/concepts/time-units).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          first_time_unit_start_utc: Start of the time interval, expressed as the timestamp for the start of the
              first
              [time unit](https://mews-systems.gitbook.io/connector-api/concepts/time-units),
              in UTC timezone ISO 8601 format.

          last_time_unit_start_utc: End of the time interval, expressed as the timestamp for the start of the last
              [time unit](https://mews-systems.gitbook.io/connector-api/concepts/time-units),
              in UTC timezone ISO 8601 format. The maximum size of time interval depends on
              the service's time unit: 367 hours if hours, 367 days if days, or 24 months if
              months.

          rate_id: Unique identifier of the `Rate`.

          product_id: Unique identifier of the `Product`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/rates/getPricing",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "first_time_unit_start_utc": first_time_unit_start_utc,
                    "last_time_unit_start_utc": last_time_unit_start_utc,
                    "rate_id": rate_id,
                    "product_id": product_id,
                },
                rate_get_pricing_params.RateGetPricingParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RateGetPricingResponse,
        )

    def set(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        rates: Iterable[rate_set_params.Rate],
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RateSetResponse:
        """
        Adds new Rates or updates existing ones if they are matched by `Id` or
        `ExternalIdentifier` property. This operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          rates: Rates to be added or updated.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/rates/set",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "rates": rates,
                    "enterprise_id": enterprise_id,
                },
                rate_set_params.RateSetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RateSetResponse,
        )

    def update_price(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        price_updates: Iterable[rate_update_price_params.PriceUpdate],
        rate_id: str,
        product_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Updates the prices for a given rate.

        You can make multiple price updates with
        one API call, and for each one specify the time interval for which the update
        applies, the price value and the applicable
        [resource category](https://mews-systems.gitbook.io/connector-api/operations/resources/#resource-category).
        The price will be updated for all service
        [time units](https://mews-systems.gitbook.io/connector-api/operations/services/#time-unit)
        that the specified time interval intersects. The price is per time unit, e.g.
        per day or per month. If the resource category `CategoryId` is not specified,
        the updated price will apply to the base price for all resource categories. Note
        that prices are defined daily, so when the server receives the UTC interval, it
        first converts it to the enterprise timezone and updates the price on all dates
        that the interval intersects. Only root rates can be updated (the rates that
        have no base rate, that have `BaseRateId` set to `null`). It is not permitted to
        update historical prices older than specified by `EditableHistoryInterval`.
        Future prices may be updated up to 5 years in the future. The **maximum size of
        time interval** is 100 time units or 2 years, whichever is the shorter amount of
        time.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          price_updates: Price adjustments for specific time intervals.

          rate_id: Unique identifier of the `Rate`.

          product_id: Unique identifier of the `Product`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/rates/updatePrice",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "price_updates": price_updates,
                    "rate_id": rate_id,
                    "product_id": product_id,
                },
                rate_update_price_params.RateUpdatePriceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncRatesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return AsyncRatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return AsyncRatesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: rate_list_params.Limitation,
        service_ids: List[str],
        activity_states: Optional[List[Literal["Deleted", "Active"]]] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        extent: Optional[rate_list_params.Extent] | NotGiven = NOT_GIVEN,
        external_identifiers: Optional[List[str]] | NotGiven = NOT_GIVEN,
        rate_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[rate_list_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RateListResponse:
        """
        Returns all rates (pricing setups) of the default service provided by the
        enterprise. Note this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          service_ids: Unique identifiers of the
              [Services](https://mews-systems.gitbook.io/connector-api/operations/services/#service)
              from which the rates are requested.

          activity_states: Whether to return only active, only deleted, or both types of record. If not
              specified, both active and deleted will be returned.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          extent: Extent of data to be returned.

          external_identifiers: Identifiers of
              [Rate](https://mews-systems.gitbook.io/connector-api/operations/#rate) from
              external systems.

          rate_ids: Unique identifiers of the requested
              [Rates](https://mews-systems.gitbook.io/connector-api/operations/rates/#rate).

          updated_utc: Interval in which `Rate` was updated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/rates/getAll",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "service_ids": service_ids,
                    "activity_states": activity_states,
                    "enterprise_ids": enterprise_ids,
                    "extent": extent,
                    "external_identifiers": external_identifiers,
                    "rate_ids": rate_ids,
                    "updated_utc": updated_utc,
                },
                rate_list_params.RateListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RateListResponse,
        )

    async def delete(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        rate_ids: List[str],
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Deletes specified rates.

        This operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          rate_ids: Unique identifiers of the rates to be deleted.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/rates/delete",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "rate_ids": rate_ids,
                    "enterprise_id": enterprise_id,
                },
                rate_delete_params.RateDeleteParams,
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
        rates: Iterable[rate_add_params.Rate],
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RateAddResponse:
        """Adds rates to the enterprise.

        Note this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).
        Rate type of `AvailabilityBlock` cannot be created via this operation.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          rates: Information about rates to be created.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/rates/add",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "rates": rates,
                    "enterprise_id": enterprise_id,
                },
                rate_add_params.RateAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RateAddResponse,
        )

    async def get_pricing(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        first_time_unit_start_utc: Union[str, datetime],
        last_time_unit_start_utc: Union[str, datetime],
        rate_id: str,
        product_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RateGetPricingResponse:
        """Returns prices for a given rate for a specified time interval.

        Prices will be
        returned for all service time units that the specified time interval intersects.
        So, for example, an interval `1st Jan 23:00 UTC - 1st Jan 23:00 UTC` will result
        in one price for `2nd Jan`, while Interval
        `1st Jan 23:00 UTC - 2nd Jan 23:00 UTC` will result in two prices for `2nd Jan`
        and `3rd Jan` (assuming a time unit period of "Day"). UTC timestamps must
        correspond to the start boundary of a time unit, e.g. 00:00 converted to UTC for
        a time unit of "Day". Other timestamps are not permitted. The **maximum size of
        time interval** depends on the service's time unit: 367 hours if hours, 367 days
        if days, or 60 months if months. For more information about time units, see
        [Time units](https://mews-systems.gitbook.io/connector-api/concepts/time-units).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          first_time_unit_start_utc: Start of the time interval, expressed as the timestamp for the start of the
              first
              [time unit](https://mews-systems.gitbook.io/connector-api/concepts/time-units),
              in UTC timezone ISO 8601 format.

          last_time_unit_start_utc: End of the time interval, expressed as the timestamp for the start of the last
              [time unit](https://mews-systems.gitbook.io/connector-api/concepts/time-units),
              in UTC timezone ISO 8601 format. The maximum size of time interval depends on
              the service's time unit: 367 hours if hours, 367 days if days, or 24 months if
              months.

          rate_id: Unique identifier of the `Rate`.

          product_id: Unique identifier of the `Product`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/rates/getPricing",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "first_time_unit_start_utc": first_time_unit_start_utc,
                    "last_time_unit_start_utc": last_time_unit_start_utc,
                    "rate_id": rate_id,
                    "product_id": product_id,
                },
                rate_get_pricing_params.RateGetPricingParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RateGetPricingResponse,
        )

    async def set(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        rates: Iterable[rate_set_params.Rate],
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RateSetResponse:
        """
        Adds new Rates or updates existing ones if they are matched by `Id` or
        `ExternalIdentifier` property. This operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          rates: Rates to be added or updated.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/rates/set",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "rates": rates,
                    "enterprise_id": enterprise_id,
                },
                rate_set_params.RateSetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RateSetResponse,
        )

    async def update_price(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        price_updates: Iterable[rate_update_price_params.PriceUpdate],
        rate_id: str,
        product_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Updates the prices for a given rate.

        You can make multiple price updates with
        one API call, and for each one specify the time interval for which the update
        applies, the price value and the applicable
        [resource category](https://mews-systems.gitbook.io/connector-api/operations/resources/#resource-category).
        The price will be updated for all service
        [time units](https://mews-systems.gitbook.io/connector-api/operations/services/#time-unit)
        that the specified time interval intersects. The price is per time unit, e.g.
        per day or per month. If the resource category `CategoryId` is not specified,
        the updated price will apply to the base price for all resource categories. Note
        that prices are defined daily, so when the server receives the UTC interval, it
        first converts it to the enterprise timezone and updates the price on all dates
        that the interval intersects. Only root rates can be updated (the rates that
        have no base rate, that have `BaseRateId` set to `null`). It is not permitted to
        update historical prices older than specified by `EditableHistoryInterval`.
        Future prices may be updated up to 5 years in the future. The **maximum size of
        time interval** is 100 time units or 2 years, whichever is the shorter amount of
        time.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          price_updates: Price adjustments for specific time intervals.

          rate_id: Unique identifier of the `Rate`.

          product_id: Unique identifier of the `Product`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/rates/updatePrice",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "price_updates": price_updates,
                    "rate_id": rate_id,
                    "product_id": product_id,
                },
                rate_update_price_params.RateUpdatePriceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class RatesResourceWithRawResponse:
    def __init__(self, rates: RatesResource) -> None:
        self._rates = rates

        self.list = to_raw_response_wrapper(
            rates.list,
        )
        self.delete = to_raw_response_wrapper(
            rates.delete,
        )
        self.add = to_raw_response_wrapper(
            rates.add,
        )
        self.get_pricing = to_raw_response_wrapper(
            rates.get_pricing,
        )
        self.set = to_raw_response_wrapper(
            rates.set,
        )
        self.update_price = to_raw_response_wrapper(
            rates.update_price,
        )


class AsyncRatesResourceWithRawResponse:
    def __init__(self, rates: AsyncRatesResource) -> None:
        self._rates = rates

        self.list = async_to_raw_response_wrapper(
            rates.list,
        )
        self.delete = async_to_raw_response_wrapper(
            rates.delete,
        )
        self.add = async_to_raw_response_wrapper(
            rates.add,
        )
        self.get_pricing = async_to_raw_response_wrapper(
            rates.get_pricing,
        )
        self.set = async_to_raw_response_wrapper(
            rates.set,
        )
        self.update_price = async_to_raw_response_wrapper(
            rates.update_price,
        )


class RatesResourceWithStreamingResponse:
    def __init__(self, rates: RatesResource) -> None:
        self._rates = rates

        self.list = to_streamed_response_wrapper(
            rates.list,
        )
        self.delete = to_streamed_response_wrapper(
            rates.delete,
        )
        self.add = to_streamed_response_wrapper(
            rates.add,
        )
        self.get_pricing = to_streamed_response_wrapper(
            rates.get_pricing,
        )
        self.set = to_streamed_response_wrapper(
            rates.set,
        )
        self.update_price = to_streamed_response_wrapper(
            rates.update_price,
        )


class AsyncRatesResourceWithStreamingResponse:
    def __init__(self, rates: AsyncRatesResource) -> None:
        self._rates = rates

        self.list = async_to_streamed_response_wrapper(
            rates.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            rates.delete,
        )
        self.add = async_to_streamed_response_wrapper(
            rates.add,
        )
        self.get_pricing = async_to_streamed_response_wrapper(
            rates.get_pricing,
        )
        self.set = async_to_streamed_response_wrapper(
            rates.set,
        )
        self.update_price = async_to_streamed_response_wrapper(
            rates.update_price,
        )
