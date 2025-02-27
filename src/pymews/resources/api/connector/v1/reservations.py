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
    reservation_add_params,
    reservation_price_params,
    reservation_start_params,
    reservation_cancel_params,
    reservation_update_params,
    reservation_confirm_params,
    reservation_get_all_params,
    reservation_process_params,
    reservation_add_product_params,
    reservation_add_companion_params,
    reservation_get_all_items_params,
    reservation_update_customer_params,
    reservation_update_interval_params,
    reservation_delete_companion_params,
    reservation_get_all_2023_06_06_params,
)
from .....types.api.connector.v1.reservation_result import ReservationResult
from .....types.api.connector.v1.reservation_add_response import ReservationAddResponse
from .....types.api.connector.v1.reservation_price_response import ReservationPriceResponse
from .....types.api.connector.v1.multiple_reservation_result import MultipleReservationResult
from .....types.api.connector.v1.reservation_add_product_response import ReservationAddProductResponse
from .....types.api.connector.v1.reservation_add_companion_response import ReservationAddCompanionResponse
from .....types.api.connector.v1.reservation_get_all_items_response import ReservationGetAllItemsResponse
from .....types.api.connector.v1.reservation_get_all_2023_06_06_response import ReservationGetAll2023_06_06Response

__all__ = ["ReservationsResource", "AsyncReservationsResource"]


class ReservationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ReservationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return ReservationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReservationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return ReservationsResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        reservation_id: str,
        reservation_updates: Iterable[reservation_update_params.ReservationUpdate],
        apply_cancellation_fee: Optional[bool] | NotGiven = NOT_GIVEN,
        assigned_resource_id: Optional[reservation_update_params.AssignedResourceID] | NotGiven = NOT_GIVEN,
        assigned_resource_locked: Optional[reservation_update_params.AssignedResourceLocked] | NotGiven = NOT_GIVEN,
        availability_block_id: Optional[reservation_update_params.AvailabilityBlockID] | NotGiven = NOT_GIVEN,
        booker_id: Optional[reservation_update_params.BookerID] | NotGiven = NOT_GIVEN,
        business_segment_id: Optional[reservation_update_params.BusinessSegmentID] | NotGiven = NOT_GIVEN,
        channel_number: Optional[reservation_update_params.ChannelNumber] | NotGiven = NOT_GIVEN,
        check_overbooking: Optional[bool] | NotGiven = NOT_GIVEN,
        check_rate_applicability: Optional[bool] | NotGiven = NOT_GIVEN,
        company_id: Optional[reservation_update_params.CompanyID] | NotGiven = NOT_GIVEN,
        credit_card_id: Optional[reservation_update_params.CreditCardID] | NotGiven = NOT_GIVEN,
        end_utc: Optional[reservation_update_params.EndUtc] | NotGiven = NOT_GIVEN,
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        options: Optional[reservation_update_params.Options] | NotGiven = NOT_GIVEN,
        person_counts: Optional[reservation_update_params.PersonCounts] | NotGiven = NOT_GIVEN,
        purpose: Optional[reservation_update_params.Purpose] | NotGiven = NOT_GIVEN,
        rate_id: Optional[reservation_update_params.RateID] | NotGiven = NOT_GIVEN,
        reason: Optional[str] | NotGiven = NOT_GIVEN,
        released_utc: Optional[reservation_update_params.ReleasedUtc] | NotGiven = NOT_GIVEN,
        reprice: Optional[bool] | NotGiven = NOT_GIVEN,
        requested_category_id: Optional[reservation_update_params.RequestedCategoryID] | NotGiven = NOT_GIVEN,
        start_utc: Optional[reservation_update_params.StartUtc] | NotGiven = NOT_GIVEN,
        time_unit_prices: Optional[reservation_update_params.TimeUnitPrices] | NotGiven = NOT_GIVEN,
        travel_agency_id: Optional[reservation_update_params.TravelAgencyID] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReservationResult:
        """Updates information about the specified reservations.

        Note that if any of the
        fields are sent as `null`, it won't clear the field in Mews. If the `Value`
        within the object is sent as `null`, the field will be cleared in Mews. Note
        this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          reservation_id: Unique identifier of the reservation.

          reservation_updates: Array of properties to be updated in each reservation specified.

          apply_cancellation_fee: Whether the cancellation fees should be applied according to rate cancellation
              policies. If not specified, the cancellation fees are applied.

          assigned_resource_id: Identifier of the assigned `Resource`.

          assigned_resource_locked: Whether the reservation should be locked to the assigned `Resource`. Unlocking
              and assigning reservation to new `Resource` can be done in one call.

          availability_block_id: Unique identifier of the `AvailabilityBlock` the reservation is assigned to.

          booker_id: Identifier of the `Customer` on whose behalf the reservation was made. (or
              `null` if the booker should not be updated).

          business_segment_id: Identifier of the reservation `BusinessSegment` (or `null` if the business
              segment should not be updated).

          channel_number: Number of the reservation within the Channel (i.e. OTA, GDS, CRS, etc) in case
              the reservation group originates there (e.g. Booking.com confirmation number)
              (or `null` if the channel number should not be updated).

          check_overbooking: Indicates whether the system will check and prevent a booking being made in the
              case of an overbooking, i.e. where there is an insufficient number of resources
              available to meet the request.

          check_rate_applicability: Indicates whether the system will check and prevent a booking being made using a
              restricted rate, e.g. a private rate. The default is true, i.e. the system will
              normally check for this unless the property is set to false.

          company_id: Identifier of the `Company` on behalf of which the reservation was made (or
              `null` if company should not be updated).

          credit_card_id: Identifier of `CreditCard` belonging to `Customer` who owns the reservation. (or
              `null` if the credit card should not be updated).

          end_utc: Reservation end in UTC timezone in ISO 8601 format. (or `null` if the end time
              should not be updated).

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          options: Options of the reservations.

          person_counts: Number of people per age category the reservation is for. If supplied, the
              person counts will be replaced. (or `null` if the person counts should not be
              updated).

          purpose: `Purpose` of the reservation (or `null` if the purpose should not be updated).

          rate_id: Identifier of the reservation `Rate` (or `null` if the rate should not be
              updated).

          reason: Reason for updating the reservation. Required when updating the price of the
              reservation.

          released_utc: Date when the optional reservation is released in UTC timezone in ISO 8601
              format. (or `null` if the release time should not be updated).

          reprice: Whether the price should be updated to latest value for date/rate/category
              combination set in Mews. If not specified, the reservation price is updated.

          requested_category_id: Identifier of the requested `ResourceCategory` (or `null` if resource category
              should not be updated).

          start_utc: Reservation start in UTC timezone in ISO 8601 format. (or `null` if the start
              time should not be updated).

          time_unit_prices: Prices for time units of the reservation. E.g. prices for the first or second
              night. (or `null` if the unit amounts should not be updated).

          travel_agency_id: Identifier of the `Company` that mediated the reservation (or `null` if travel
              agency should not be updated).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/reservations/update",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "reservation_id": reservation_id,
                    "reservation_updates": reservation_updates,
                    "apply_cancellation_fee": apply_cancellation_fee,
                    "assigned_resource_id": assigned_resource_id,
                    "assigned_resource_locked": assigned_resource_locked,
                    "availability_block_id": availability_block_id,
                    "booker_id": booker_id,
                    "business_segment_id": business_segment_id,
                    "channel_number": channel_number,
                    "check_overbooking": check_overbooking,
                    "check_rate_applicability": check_rate_applicability,
                    "company_id": company_id,
                    "credit_card_id": credit_card_id,
                    "end_utc": end_utc,
                    "enterprise_id": enterprise_id,
                    "options": options,
                    "person_counts": person_counts,
                    "purpose": purpose,
                    "rate_id": rate_id,
                    "reason": reason,
                    "released_utc": released_utc,
                    "reprice": reprice,
                    "requested_category_id": requested_category_id,
                    "start_utc": start_utc,
                    "time_unit_prices": time_unit_prices,
                    "travel_agency_id": travel_agency_id,
                },
                reservation_update_params.ReservationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReservationResult,
        )

    def add(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        reservations: Iterable[reservation_add_params.Reservation],
        service_id: str,
        check_overbooking: Optional[bool] | NotGiven = NOT_GIVEN,
        check_rate_applicability: Optional[bool] | NotGiven = NOT_GIVEN,
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        group_id: Optional[str] | NotGiven = NOT_GIVEN,
        group_name: Optional[str] | NotGiven = NOT_GIVEN,
        send_confirmation_email: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReservationAddResponse:
        """Adds the specified reservations as a single group.

        If `GroupId` is specified,
        adds the reservations to an already existing group. Note that all reservations
        linked to an availability block must belong to the same reservation group.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          reservations: Parameters of the new reservations.

          service_id: Unique identifier of the `Service` to be reserved.

          check_overbooking: Indicates whether the system will check and prevent a booking being made in the
              case of an overbooking, i.e. where there is an insufficient number of resources
              available to meet the request. The default is `true`, i.e. the system will
              normally check for this unless the property is set to `false`.

          check_rate_applicability: Indicates whether the system will check and prevent a booking being made using a
              restricted rate, e.g. a private rate. The default is `true`, i.e. the system
              will normally check for this unless the property is set to `false`.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          group_id: Unique identifier of the `ReservationGroup` where the reservations are added. If
              not specified, a new group is created.

          group_name: Name of the `ReservationGroup` where the reservations are added to. If `GroupId`
              is specified, this field is ignored. If not specified, the group name is
              automatically created.

          send_confirmation_email: Whether the confirmation email is sent. Default value is `true`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/reservations/add",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "reservations": reservations,
                    "service_id": service_id,
                    "check_overbooking": check_overbooking,
                    "check_rate_applicability": check_rate_applicability,
                    "enterprise_id": enterprise_id,
                    "group_id": group_id,
                    "group_name": group_name,
                    "send_confirmation_email": send_confirmation_email,
                },
                reservation_add_params.ReservationAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReservationAddResponse,
        )

    def add_companion(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        customer_id: str,
        reservation_id: str,
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReservationAddCompanionResponse:
        """Adds a customer as a companion to the reservation.

        Succeeds only if there is
        space for the new companion (count of current companions is less than
        `AdultCount + ChildCount`). Note this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          customer_id: Unique identifier of the `Customer`.

          reservation_id: Unique identifier of the `Reservation`.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/reservations/addCompanion",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "customer_id": customer_id,
                    "reservation_id": reservation_id,
                    "enterprise_id": enterprise_id,
                },
                reservation_add_companion_params.ReservationAddCompanionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReservationAddCompanionResponse,
        )

    def add_product(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        count: int,
        product_id: str,
        reservation_id: str,
        end_utc: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        start_utc: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        unit_amount: Optional[reservation_add_product_params.UnitAmount] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReservationAddProductResponse:
        """
        Adds a new product order of the specified product to the reservation.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          count: The amount of the products to be added. Note that if the product is charged e.g.
              per night, count 1 means a single product every night. Count 2 means two
              products every night.

          product_id: Unique identifier of the
              [Product](https://mews-systems.gitbook.io/connector-api/operations/products/#product).

          reservation_id: Unique identifier of the reservation.

          end_utc: Product end in UTC timezone in ISO 8601 format. For products with charging Once
              and PerPerson must be set to same value as StartUtc.

          start_utc: Product start in UTC timezone in ISO 8601 format. For products with charging
              Once and PerPerson must be set to same value as EndUtc.

          unit_amount: Price of the product that overrides the price defined in Mews.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/reservations/addProduct",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "count": count,
                    "product_id": product_id,
                    "reservation_id": reservation_id,
                    "end_utc": end_utc,
                    "start_utc": start_utc,
                    "unit_amount": unit_amount,
                },
                reservation_add_product_params.ReservationAddProductParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReservationAddProductResponse,
        )

    def cancel(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        reservation_ids: List[str],
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        post_cancellation_fee: Optional[bool] | NotGiven = NOT_GIVEN,
        reservation_id: str | NotGiven = NOT_GIVEN,
        send_email: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MultipleReservationResult:
        """Cancels all reservation with specified identifiers.

        Succeeds only if the
        reservations are cancellable. Note this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          reservation_ids: Unique identifiers of the reservation to cancel.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          notes: Additional notes describing the reason for the cancellation.

          post_cancellation_fee: Whether the cancellation fees should be charged according to rate conditions.
              The default is `false`.

          send_email: Whether the cancellation email should be sent. The default is `true`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/reservations/cancel",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "reservation_ids": reservation_ids,
                    "enterprise_id": enterprise_id,
                    "notes": notes,
                    "post_cancellation_fee": post_cancellation_fee,
                    "reservation_id": reservation_id,
                    "send_email": send_email,
                },
                reservation_cancel_params.ReservationCancelParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MultipleReservationResult,
        )

    def confirm(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        reservation_ids: List[str],
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        send_confirmation_email: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MultipleReservationResult:
        """Marks all specified reservations as `Confirmed`.

        Succeeds only if all
        confirmation conditions are met (the reservations have the `Optional` state).
        Note this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          reservation_ids: Unique identifier of the reservations to confirm.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          send_confirmation_email: Wheter the confirmation email is sent. Default value is true.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/reservations/confirm",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "reservation_ids": reservation_ids,
                    "enterprise_id": enterprise_id,
                    "send_confirmation_email": send_confirmation_email,
                },
                reservation_confirm_params.ReservationConfirmParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MultipleReservationResult,
        )

    def delete_companion(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        customer_id: str,
        reservation_id: str,
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Removes customer companionship from the reservation.

        Note that the customer
        profile stays untouched, only the relation between the customer and reservation
        is deleted. Note this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          customer_id: Unique identifier of the `Customer`.

          reservation_id: Unique identifier of the `Reservation`.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/reservations/deleteCompanion",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "customer_id": customer_id,
                    "reservation_id": reservation_id,
                    "enterprise_id": enterprise_id,
                },
                reservation_delete_companion_params.ReservationDeleteCompanionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def get_all(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        extent: reservation_get_all_params.Extent,
        limitation: reservation_get_all_params.Limitation,
        service_ids: List[str],
        assigned_resource_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        business_segment_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        channel_numbers: Optional[List[str]] | NotGiven = NOT_GIVEN,
        currency: Optional[str] | NotGiven = NOT_GIVEN,
        customer_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        end_utc: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        group_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        numbers: Optional[List[str]] | NotGiven = NOT_GIVEN,
        rate_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        reservation_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        service_id: Optional[str] | NotGiven = NOT_GIVEN,
        start_utc: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        states: Optional[
            List[Literal["Enquired", "Confirmed", "Started", "Processed", "Canceled", "Optional", "Requested"]]
        ]
        | NotGiven = NOT_GIVEN,
        time_filter: Optional[Literal["Colliding", "Created", "Updated", "Start", "End", "Overlapping", "Canceled"]]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReservationResult:
        """
        Use
        [Get all reservations (ver 2023-06-06)](https://mews-systems.gitbook.io/connector-api/operations/reservations#get-all-reservations-ver-2023-06-06).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          extent: Extent of data to be returned. E.g. it is possible to specify that together with
              the reservations, customers, groups and rates should be also returned.

          limitation: Limitation on the quantity of data returned.

          service_ids: Unique identifiers of the
              [Services](https://mews-systems.gitbook.io/connector-api/operations/services/#service)
              from which the reservations are requested.

          assigned_resource_ids: Unique identifiers of
              [Resources](https://mews-systems.gitbook.io/connector-api/operations/resources/#resource)
              assigned to the reservations.

          business_segment_ids: Unique identifiers of
              [Business segments](https://mews-systems.gitbook.io/connector-api/operations/businesssegments/#business-segment)
              assigned to the reservations.

          channel_numbers: Set of numbers or references used by the Channel (i.e. OTA, GDS, CRS, etc.) in
              case the reservation group originates there, e.g. Booking.com confirmation
              numbers.

          currency: ISO-4217 code of the
              [Currency](https://mews-systems.gitbook.io/connector-api/operations/currencies/#currency)
              the item costs should be converted to.

          customer_ids: Unique identifiers of the
              [Customers](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer)
              which own the reservations.

          end_utc: End of the interval in UTC timezone in ISO 8601 format. Required when used in
              conjunction with the TimeFilter or States search parameter.

          group_ids: Unique identifiers of the requested
              [Reservation groups](https://mews-systems.gitbook.io/connector-api/operations/#reservation-group).

          numbers: Confirmation numbers of
              [Reservations](https://mews-systems.gitbook.io/connector-api/operations/#reservation-ver-2017-04-12).

          rate_ids: Unique identifiers of
              [Rates](https://mews-systems.gitbook.io/connector-api/operations/rates/#rate)
              assigned to the reservations.

          reservation_ids: Unique identifiers of the requested
              [Reservations](https://mews-systems.gitbook.io/connector-api/operations/#reservation-ver-2017-04-12).

          start_utc: Start of the interval in UTC timezone in ISO 8601 format. Required when used in
              conjunction with the TimeFilter or States search parameter.

          states: States the reservations should be in. If not specified, reservations in
              Confirmed, Started or Processed states or reservations specified by
              ReservationIds regardless of state are returned.

          time_filter: Time filter of the interval. If not specified, reservations Colliding with the
              interval are returned.

              - `Colliding` - Reservations whose intervals collide with the specified
                interval.
              - `Created` - Reservations created within the specified interval.
              - `Updated` - Reservations updated within the specified interval.
              - `Start` - Reservations starting (arriving) within the specified interval.
              - `End` - Reservations ending (departing) within the specified interval.
              - `Overlapping` - Reservations whose intervals contain the specified interval.
              - `Canceled` - Reservations canceled within the specified interval.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/reservations/getAll",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "extent": extent,
                    "limitation": limitation,
                    "service_ids": service_ids,
                    "assigned_resource_ids": assigned_resource_ids,
                    "business_segment_ids": business_segment_ids,
                    "channel_numbers": channel_numbers,
                    "currency": currency,
                    "customer_ids": customer_ids,
                    "end_utc": end_utc,
                    "group_ids": group_ids,
                    "numbers": numbers,
                    "rate_ids": rate_ids,
                    "reservation_ids": reservation_ids,
                    "service_id": service_id,
                    "start_utc": start_utc,
                    "states": states,
                    "time_filter": time_filter,
                },
                reservation_get_all_params.ReservationGetAllParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReservationResult,
        )

    def get_all_2023_06_06(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: reservation_get_all_2023_06_06_params.Limitation,
        account_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        actual_start_utc: Optional[reservation_get_all_2023_06_06_params.ActualStartUtc] | NotGiven = NOT_GIVEN,
        assigned_resource_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        availability_block_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        colliding_utc: Optional[reservation_get_all_2023_06_06_params.CollidingUtc] | NotGiven = NOT_GIVEN,
        created_utc: Optional[reservation_get_all_2023_06_06_params.CreatedUtc] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        numbers: Optional[List[str]] | NotGiven = NOT_GIVEN,
        reservation_group_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        reservation_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        scheduled_end_utc: Optional[reservation_get_all_2023_06_06_params.ScheduledEndUtc] | NotGiven = NOT_GIVEN,
        scheduled_start_utc: Optional[reservation_get_all_2023_06_06_params.ScheduledStartUtc] | NotGiven = NOT_GIVEN,
        service_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        states: Optional[
            List[Literal["Inquired", "Confirmed", "Started", "Processed", "Canceled", "Optional", "Requested"]]
        ]
        | NotGiven = NOT_GIVEN,
        updated_utc: Optional[reservation_get_all_2023_06_06_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReservationGetAll2023_06_06Response:
        """
        Returns all reservations within scope of the Access Token, filtered according to
        the specified parameters. This operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          account_ids: Unique identifiers of accounts (currently only
              [Customers](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer),
              in the future also
              [Companies](https://mews-systems.gitbook.io/connector-api/operations/companies/#company))
              the reservation is associated with.

          actual_start_utc: Interval filtering Reservations by their actual start (check-in) time. Cannot be
              used with `ScheduledStartUtc`. Note that the filter applies only to started or
              processed reservations.

          assigned_resource_ids: Unique identifiers of the
              [Resources](https://mews-systems.gitbook.io/connector-api/operations/resources#resource)
              assigned to the reservations.

          availability_block_ids: Unique identifiers of the `Availability blocks` assigned to the reservations.

          colliding_utc: Interval in which the reservations are active. This is defined for a
              `Reservation` as the period between the reservation's scheduled start time
              `ScheduledStartUtc` and its scheduled end time `EndUtc`. Reservation is selected
              if any part of its interval intersects with the interval specified in
              `CollidingUtc

          created_utc: Interval in which the
              [Reservation](https://mews-systems.gitbook.io/connector-api/operations/reservations/#reservation-ver-2023-06-06)
              was created.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          numbers: A list of reservation numbers. Each number uniquely identifies a reservation
              within the system

          reservation_group_ids: Unique identifiers of
              [Reservation groups](https://mews-systems.gitbook.io/connector-api/operations/#reservation-group).

          reservation_ids: Unique identifiers of the
              [Reservations](https://mews-systems.gitbook.io/connector-api/operations/#reservation-ver-2023-06-06).

          scheduled_end_utc: Interval filtering Reservations by their scheduled end time.

          scheduled_start_utc: Interval filtering Reservations by their scheduled start time. Cannot be used
              with `ActualStartUtc`.

          service_ids: Unique identifiers of the
              [Services](https://mews-systems.gitbook.io/connector-api/operations/services/#service).
              If not provided, all bookable services are used.

          states: A list of service order states to filter by.

          updated_utc: Interval in which the `Reservations` were updated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/reservations/getAll/2023-06-06",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "account_ids": account_ids,
                    "actual_start_utc": actual_start_utc,
                    "assigned_resource_ids": assigned_resource_ids,
                    "availability_block_ids": availability_block_ids,
                    "colliding_utc": colliding_utc,
                    "created_utc": created_utc,
                    "enterprise_ids": enterprise_ids,
                    "numbers": numbers,
                    "reservation_group_ids": reservation_group_ids,
                    "reservation_ids": reservation_ids,
                    "scheduled_end_utc": scheduled_end_utc,
                    "scheduled_start_utc": scheduled_start_utc,
                    "service_ids": service_ids,
                    "states": states,
                    "updated_utc": updated_utc,
                },
                reservation_get_all_2023_06_06_params.ReservationGetAll2023_06_06Params,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReservationGetAll2023_06_06Response,
        )

    def get_all_items(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        reservation_ids: List[str],
        accounting_states: Optional[List[str]] | NotGiven = NOT_GIVEN,
        currency: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReservationGetAllItemsResponse:
        """
        Use orderItems/getAll.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          reservation_ids: Unique identifiers of the reservation.

          accounting_states: States the items should be in. If not specified, items in Open or Closed states
              are returned.

          currency: ISO-4217 code of the
              [Currency](https://mews-systems.gitbook.io/connector-api/operations/currencies/#currency)
              the item costs should be converted to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/reservations/getAllItems",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "reservation_ids": reservation_ids,
                    "accounting_states": accounting_states,
                    "currency": currency,
                },
                reservation_get_all_items_params.ReservationGetAllItemsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReservationGetAllItemsResponse,
        )

    def price(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        reservations: Iterable[reservation_price_params.Reservation],
        service_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReservationPriceResponse:
        """Returns prices of reservations with the specified parameters.

        Note that the
        operation doesn't check the maximum capacity of requested resource category.
        Requesting person counts above the capacity will return prices for the maximum
        available capacity.

        This operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          reservations: Parameters of the reservations to price. Note that `CustomerId` is not required
              when pricing reservations.

          service_id: Unique identifier of the `Service` to be priced.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/reservations/price",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "reservations": reservations,
                    "service_id": service_id,
                },
                reservation_price_params.ReservationPriceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReservationPriceResponse,
        )

    def process(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        reservation_id: str,
        allow_open_balance: Optional[bool] | NotGiven = NOT_GIVEN,
        close_bills: Optional[bool] | NotGiven = NOT_GIVEN,
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        notes: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Marks a reservation as `Processed` (= checked out).

        Succeeds only if all
        processing conditions are met (the reservation has the `Started` state, balance
        of all reservation members is zero etc). Note this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        ### Conditions

        - Reservation has already been checked in.
        - Reservation isn't alredy in `Processed` state.
        - Reservation can't be checked out sooner than last day of planned stay.
        - The companion profiles of reservation are complete (details can be found in
          error message).
        - If `AllowOpenBalance` set to `false`, all bills have to be closable (items on
          bills are either paid by current customer, or set to be paid by other
          customer). With `CloseBills` option set to `true` they can be automatically
          closed, when set to `false` they must be closed manually.
        - If `AllowOpenBalance` set to `true`, `Notes` must be filled in.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          reservation_id: Unique identifier of the reservation to process.

          allow_open_balance: Whether non-zero consumed balance of all reservation members is allowed.

          close_bills: Whether closable bills of the reservation members should be automatically
              closed.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          notes: Required if AllowOpenBalance set to true. Used to provide reason for closing
              with unbalanced bill.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/reservations/process",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "reservation_id": reservation_id,
                    "allow_open_balance": allow_open_balance,
                    "close_bills": close_bills,
                    "enterprise_id": enterprise_id,
                    "notes": notes,
                },
                reservation_process_params.ReservationProcessParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def start(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        reservation_id: str,
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Marks a reservation as `Started` (= checked in).

        Succeeds only if all starting
        conditions are met (the reservation has the `Confirmed` state, does not have
        start set to future, has an inspected room assigned etc). Note this operation
        supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          reservation_id: Unique identifier of the reservation to start.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/reservations/start",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "reservation_id": reservation_id,
                    "enterprise_id": enterprise_id,
                },
                reservation_start_params.ReservationStartParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def update_customer(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        customer_id: str,
        reservation_id: str,
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Updates customer of a reservation.

        Note this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          customer_id: Unique identifier of the
              [Customer](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer).

          reservation_id: Unique identifier of the reservation to be updated.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/reservations/updateCustomer",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "customer_id": customer_id,
                    "reservation_id": reservation_id,
                    "enterprise_id": enterprise_id,
                },
                reservation_update_customer_params.ReservationUpdateCustomerParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def update_interval(
        self,
        *,
        access_token: str,
        charge_cancellation_fee: bool,
        client: str,
        client_token: str,
        reservation_id: str,
        end_utc: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        start_utc: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Updates reservation interval (start, end or both).

        Note this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          charge_cancellation_fee: Whether cancellation fee should be charged for potentially canceled nights.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          reservation_id: Unique identifier of the reservation to be updated.

          end_utc: New reservation end in UTC timezone in ISO 8601 format.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          start_utc: New reservation start in UTC timezone in ISO 8601 format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/reservations/updateInterval",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "charge_cancellation_fee": charge_cancellation_fee,
                    "client": client,
                    "client_token": client_token,
                    "reservation_id": reservation_id,
                    "end_utc": end_utc,
                    "enterprise_id": enterprise_id,
                    "start_utc": start_utc,
                },
                reservation_update_interval_params.ReservationUpdateIntervalParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncReservationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncReservationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return AsyncReservationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReservationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return AsyncReservationsResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        reservation_id: str,
        reservation_updates: Iterable[reservation_update_params.ReservationUpdate],
        apply_cancellation_fee: Optional[bool] | NotGiven = NOT_GIVEN,
        assigned_resource_id: Optional[reservation_update_params.AssignedResourceID] | NotGiven = NOT_GIVEN,
        assigned_resource_locked: Optional[reservation_update_params.AssignedResourceLocked] | NotGiven = NOT_GIVEN,
        availability_block_id: Optional[reservation_update_params.AvailabilityBlockID] | NotGiven = NOT_GIVEN,
        booker_id: Optional[reservation_update_params.BookerID] | NotGiven = NOT_GIVEN,
        business_segment_id: Optional[reservation_update_params.BusinessSegmentID] | NotGiven = NOT_GIVEN,
        channel_number: Optional[reservation_update_params.ChannelNumber] | NotGiven = NOT_GIVEN,
        check_overbooking: Optional[bool] | NotGiven = NOT_GIVEN,
        check_rate_applicability: Optional[bool] | NotGiven = NOT_GIVEN,
        company_id: Optional[reservation_update_params.CompanyID] | NotGiven = NOT_GIVEN,
        credit_card_id: Optional[reservation_update_params.CreditCardID] | NotGiven = NOT_GIVEN,
        end_utc: Optional[reservation_update_params.EndUtc] | NotGiven = NOT_GIVEN,
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        options: Optional[reservation_update_params.Options] | NotGiven = NOT_GIVEN,
        person_counts: Optional[reservation_update_params.PersonCounts] | NotGiven = NOT_GIVEN,
        purpose: Optional[reservation_update_params.Purpose] | NotGiven = NOT_GIVEN,
        rate_id: Optional[reservation_update_params.RateID] | NotGiven = NOT_GIVEN,
        reason: Optional[str] | NotGiven = NOT_GIVEN,
        released_utc: Optional[reservation_update_params.ReleasedUtc] | NotGiven = NOT_GIVEN,
        reprice: Optional[bool] | NotGiven = NOT_GIVEN,
        requested_category_id: Optional[reservation_update_params.RequestedCategoryID] | NotGiven = NOT_GIVEN,
        start_utc: Optional[reservation_update_params.StartUtc] | NotGiven = NOT_GIVEN,
        time_unit_prices: Optional[reservation_update_params.TimeUnitPrices] | NotGiven = NOT_GIVEN,
        travel_agency_id: Optional[reservation_update_params.TravelAgencyID] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReservationResult:
        """Updates information about the specified reservations.

        Note that if any of the
        fields are sent as `null`, it won't clear the field in Mews. If the `Value`
        within the object is sent as `null`, the field will be cleared in Mews. Note
        this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          reservation_id: Unique identifier of the reservation.

          reservation_updates: Array of properties to be updated in each reservation specified.

          apply_cancellation_fee: Whether the cancellation fees should be applied according to rate cancellation
              policies. If not specified, the cancellation fees are applied.

          assigned_resource_id: Identifier of the assigned `Resource`.

          assigned_resource_locked: Whether the reservation should be locked to the assigned `Resource`. Unlocking
              and assigning reservation to new `Resource` can be done in one call.

          availability_block_id: Unique identifier of the `AvailabilityBlock` the reservation is assigned to.

          booker_id: Identifier of the `Customer` on whose behalf the reservation was made. (or
              `null` if the booker should not be updated).

          business_segment_id: Identifier of the reservation `BusinessSegment` (or `null` if the business
              segment should not be updated).

          channel_number: Number of the reservation within the Channel (i.e. OTA, GDS, CRS, etc) in case
              the reservation group originates there (e.g. Booking.com confirmation number)
              (or `null` if the channel number should not be updated).

          check_overbooking: Indicates whether the system will check and prevent a booking being made in the
              case of an overbooking, i.e. where there is an insufficient number of resources
              available to meet the request.

          check_rate_applicability: Indicates whether the system will check and prevent a booking being made using a
              restricted rate, e.g. a private rate. The default is true, i.e. the system will
              normally check for this unless the property is set to false.

          company_id: Identifier of the `Company` on behalf of which the reservation was made (or
              `null` if company should not be updated).

          credit_card_id: Identifier of `CreditCard` belonging to `Customer` who owns the reservation. (or
              `null` if the credit card should not be updated).

          end_utc: Reservation end in UTC timezone in ISO 8601 format. (or `null` if the end time
              should not be updated).

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          options: Options of the reservations.

          person_counts: Number of people per age category the reservation is for. If supplied, the
              person counts will be replaced. (or `null` if the person counts should not be
              updated).

          purpose: `Purpose` of the reservation (or `null` if the purpose should not be updated).

          rate_id: Identifier of the reservation `Rate` (or `null` if the rate should not be
              updated).

          reason: Reason for updating the reservation. Required when updating the price of the
              reservation.

          released_utc: Date when the optional reservation is released in UTC timezone in ISO 8601
              format. (or `null` if the release time should not be updated).

          reprice: Whether the price should be updated to latest value for date/rate/category
              combination set in Mews. If not specified, the reservation price is updated.

          requested_category_id: Identifier of the requested `ResourceCategory` (or `null` if resource category
              should not be updated).

          start_utc: Reservation start in UTC timezone in ISO 8601 format. (or `null` if the start
              time should not be updated).

          time_unit_prices: Prices for time units of the reservation. E.g. prices for the first or second
              night. (or `null` if the unit amounts should not be updated).

          travel_agency_id: Identifier of the `Company` that mediated the reservation (or `null` if travel
              agency should not be updated).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/reservations/update",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "reservation_id": reservation_id,
                    "reservation_updates": reservation_updates,
                    "apply_cancellation_fee": apply_cancellation_fee,
                    "assigned_resource_id": assigned_resource_id,
                    "assigned_resource_locked": assigned_resource_locked,
                    "availability_block_id": availability_block_id,
                    "booker_id": booker_id,
                    "business_segment_id": business_segment_id,
                    "channel_number": channel_number,
                    "check_overbooking": check_overbooking,
                    "check_rate_applicability": check_rate_applicability,
                    "company_id": company_id,
                    "credit_card_id": credit_card_id,
                    "end_utc": end_utc,
                    "enterprise_id": enterprise_id,
                    "options": options,
                    "person_counts": person_counts,
                    "purpose": purpose,
                    "rate_id": rate_id,
                    "reason": reason,
                    "released_utc": released_utc,
                    "reprice": reprice,
                    "requested_category_id": requested_category_id,
                    "start_utc": start_utc,
                    "time_unit_prices": time_unit_prices,
                    "travel_agency_id": travel_agency_id,
                },
                reservation_update_params.ReservationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReservationResult,
        )

    async def add(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        reservations: Iterable[reservation_add_params.Reservation],
        service_id: str,
        check_overbooking: Optional[bool] | NotGiven = NOT_GIVEN,
        check_rate_applicability: Optional[bool] | NotGiven = NOT_GIVEN,
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        group_id: Optional[str] | NotGiven = NOT_GIVEN,
        group_name: Optional[str] | NotGiven = NOT_GIVEN,
        send_confirmation_email: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReservationAddResponse:
        """Adds the specified reservations as a single group.

        If `GroupId` is specified,
        adds the reservations to an already existing group. Note that all reservations
        linked to an availability block must belong to the same reservation group.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          reservations: Parameters of the new reservations.

          service_id: Unique identifier of the `Service` to be reserved.

          check_overbooking: Indicates whether the system will check and prevent a booking being made in the
              case of an overbooking, i.e. where there is an insufficient number of resources
              available to meet the request. The default is `true`, i.e. the system will
              normally check for this unless the property is set to `false`.

          check_rate_applicability: Indicates whether the system will check and prevent a booking being made using a
              restricted rate, e.g. a private rate. The default is `true`, i.e. the system
              will normally check for this unless the property is set to `false`.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          group_id: Unique identifier of the `ReservationGroup` where the reservations are added. If
              not specified, a new group is created.

          group_name: Name of the `ReservationGroup` where the reservations are added to. If `GroupId`
              is specified, this field is ignored. If not specified, the group name is
              automatically created.

          send_confirmation_email: Whether the confirmation email is sent. Default value is `true`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/reservations/add",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "reservations": reservations,
                    "service_id": service_id,
                    "check_overbooking": check_overbooking,
                    "check_rate_applicability": check_rate_applicability,
                    "enterprise_id": enterprise_id,
                    "group_id": group_id,
                    "group_name": group_name,
                    "send_confirmation_email": send_confirmation_email,
                },
                reservation_add_params.ReservationAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReservationAddResponse,
        )

    async def add_companion(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        customer_id: str,
        reservation_id: str,
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReservationAddCompanionResponse:
        """Adds a customer as a companion to the reservation.

        Succeeds only if there is
        space for the new companion (count of current companions is less than
        `AdultCount + ChildCount`). Note this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          customer_id: Unique identifier of the `Customer`.

          reservation_id: Unique identifier of the `Reservation`.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/reservations/addCompanion",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "customer_id": customer_id,
                    "reservation_id": reservation_id,
                    "enterprise_id": enterprise_id,
                },
                reservation_add_companion_params.ReservationAddCompanionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReservationAddCompanionResponse,
        )

    async def add_product(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        count: int,
        product_id: str,
        reservation_id: str,
        end_utc: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        start_utc: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        unit_amount: Optional[reservation_add_product_params.UnitAmount] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReservationAddProductResponse:
        """
        Adds a new product order of the specified product to the reservation.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          count: The amount of the products to be added. Note that if the product is charged e.g.
              per night, count 1 means a single product every night. Count 2 means two
              products every night.

          product_id: Unique identifier of the
              [Product](https://mews-systems.gitbook.io/connector-api/operations/products/#product).

          reservation_id: Unique identifier of the reservation.

          end_utc: Product end in UTC timezone in ISO 8601 format. For products with charging Once
              and PerPerson must be set to same value as StartUtc.

          start_utc: Product start in UTC timezone in ISO 8601 format. For products with charging
              Once and PerPerson must be set to same value as EndUtc.

          unit_amount: Price of the product that overrides the price defined in Mews.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/reservations/addProduct",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "count": count,
                    "product_id": product_id,
                    "reservation_id": reservation_id,
                    "end_utc": end_utc,
                    "start_utc": start_utc,
                    "unit_amount": unit_amount,
                },
                reservation_add_product_params.ReservationAddProductParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReservationAddProductResponse,
        )

    async def cancel(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        reservation_ids: List[str],
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        post_cancellation_fee: Optional[bool] | NotGiven = NOT_GIVEN,
        reservation_id: str | NotGiven = NOT_GIVEN,
        send_email: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MultipleReservationResult:
        """Cancels all reservation with specified identifiers.

        Succeeds only if the
        reservations are cancellable. Note this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          reservation_ids: Unique identifiers of the reservation to cancel.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          notes: Additional notes describing the reason for the cancellation.

          post_cancellation_fee: Whether the cancellation fees should be charged according to rate conditions.
              The default is `false`.

          send_email: Whether the cancellation email should be sent. The default is `true`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/reservations/cancel",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "reservation_ids": reservation_ids,
                    "enterprise_id": enterprise_id,
                    "notes": notes,
                    "post_cancellation_fee": post_cancellation_fee,
                    "reservation_id": reservation_id,
                    "send_email": send_email,
                },
                reservation_cancel_params.ReservationCancelParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MultipleReservationResult,
        )

    async def confirm(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        reservation_ids: List[str],
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        send_confirmation_email: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MultipleReservationResult:
        """Marks all specified reservations as `Confirmed`.

        Succeeds only if all
        confirmation conditions are met (the reservations have the `Optional` state).
        Note this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          reservation_ids: Unique identifier of the reservations to confirm.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          send_confirmation_email: Wheter the confirmation email is sent. Default value is true.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/reservations/confirm",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "reservation_ids": reservation_ids,
                    "enterprise_id": enterprise_id,
                    "send_confirmation_email": send_confirmation_email,
                },
                reservation_confirm_params.ReservationConfirmParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MultipleReservationResult,
        )

    async def delete_companion(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        customer_id: str,
        reservation_id: str,
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Removes customer companionship from the reservation.

        Note that the customer
        profile stays untouched, only the relation between the customer and reservation
        is deleted. Note this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          customer_id: Unique identifier of the `Customer`.

          reservation_id: Unique identifier of the `Reservation`.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/reservations/deleteCompanion",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "customer_id": customer_id,
                    "reservation_id": reservation_id,
                    "enterprise_id": enterprise_id,
                },
                reservation_delete_companion_params.ReservationDeleteCompanionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def get_all(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        extent: reservation_get_all_params.Extent,
        limitation: reservation_get_all_params.Limitation,
        service_ids: List[str],
        assigned_resource_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        business_segment_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        channel_numbers: Optional[List[str]] | NotGiven = NOT_GIVEN,
        currency: Optional[str] | NotGiven = NOT_GIVEN,
        customer_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        end_utc: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        group_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        numbers: Optional[List[str]] | NotGiven = NOT_GIVEN,
        rate_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        reservation_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        service_id: Optional[str] | NotGiven = NOT_GIVEN,
        start_utc: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        states: Optional[
            List[Literal["Enquired", "Confirmed", "Started", "Processed", "Canceled", "Optional", "Requested"]]
        ]
        | NotGiven = NOT_GIVEN,
        time_filter: Optional[Literal["Colliding", "Created", "Updated", "Start", "End", "Overlapping", "Canceled"]]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReservationResult:
        """
        Use
        [Get all reservations (ver 2023-06-06)](https://mews-systems.gitbook.io/connector-api/operations/reservations#get-all-reservations-ver-2023-06-06).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          extent: Extent of data to be returned. E.g. it is possible to specify that together with
              the reservations, customers, groups and rates should be also returned.

          limitation: Limitation on the quantity of data returned.

          service_ids: Unique identifiers of the
              [Services](https://mews-systems.gitbook.io/connector-api/operations/services/#service)
              from which the reservations are requested.

          assigned_resource_ids: Unique identifiers of
              [Resources](https://mews-systems.gitbook.io/connector-api/operations/resources/#resource)
              assigned to the reservations.

          business_segment_ids: Unique identifiers of
              [Business segments](https://mews-systems.gitbook.io/connector-api/operations/businesssegments/#business-segment)
              assigned to the reservations.

          channel_numbers: Set of numbers or references used by the Channel (i.e. OTA, GDS, CRS, etc.) in
              case the reservation group originates there, e.g. Booking.com confirmation
              numbers.

          currency: ISO-4217 code of the
              [Currency](https://mews-systems.gitbook.io/connector-api/operations/currencies/#currency)
              the item costs should be converted to.

          customer_ids: Unique identifiers of the
              [Customers](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer)
              which own the reservations.

          end_utc: End of the interval in UTC timezone in ISO 8601 format. Required when used in
              conjunction with the TimeFilter or States search parameter.

          group_ids: Unique identifiers of the requested
              [Reservation groups](https://mews-systems.gitbook.io/connector-api/operations/#reservation-group).

          numbers: Confirmation numbers of
              [Reservations](https://mews-systems.gitbook.io/connector-api/operations/#reservation-ver-2017-04-12).

          rate_ids: Unique identifiers of
              [Rates](https://mews-systems.gitbook.io/connector-api/operations/rates/#rate)
              assigned to the reservations.

          reservation_ids: Unique identifiers of the requested
              [Reservations](https://mews-systems.gitbook.io/connector-api/operations/#reservation-ver-2017-04-12).

          start_utc: Start of the interval in UTC timezone in ISO 8601 format. Required when used in
              conjunction with the TimeFilter or States search parameter.

          states: States the reservations should be in. If not specified, reservations in
              Confirmed, Started or Processed states or reservations specified by
              ReservationIds regardless of state are returned.

          time_filter: Time filter of the interval. If not specified, reservations Colliding with the
              interval are returned.

              - `Colliding` - Reservations whose intervals collide with the specified
                interval.
              - `Created` - Reservations created within the specified interval.
              - `Updated` - Reservations updated within the specified interval.
              - `Start` - Reservations starting (arriving) within the specified interval.
              - `End` - Reservations ending (departing) within the specified interval.
              - `Overlapping` - Reservations whose intervals contain the specified interval.
              - `Canceled` - Reservations canceled within the specified interval.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/reservations/getAll",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "extent": extent,
                    "limitation": limitation,
                    "service_ids": service_ids,
                    "assigned_resource_ids": assigned_resource_ids,
                    "business_segment_ids": business_segment_ids,
                    "channel_numbers": channel_numbers,
                    "currency": currency,
                    "customer_ids": customer_ids,
                    "end_utc": end_utc,
                    "group_ids": group_ids,
                    "numbers": numbers,
                    "rate_ids": rate_ids,
                    "reservation_ids": reservation_ids,
                    "service_id": service_id,
                    "start_utc": start_utc,
                    "states": states,
                    "time_filter": time_filter,
                },
                reservation_get_all_params.ReservationGetAllParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReservationResult,
        )

    async def get_all_2023_06_06(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: reservation_get_all_2023_06_06_params.Limitation,
        account_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        actual_start_utc: Optional[reservation_get_all_2023_06_06_params.ActualStartUtc] | NotGiven = NOT_GIVEN,
        assigned_resource_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        availability_block_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        colliding_utc: Optional[reservation_get_all_2023_06_06_params.CollidingUtc] | NotGiven = NOT_GIVEN,
        created_utc: Optional[reservation_get_all_2023_06_06_params.CreatedUtc] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        numbers: Optional[List[str]] | NotGiven = NOT_GIVEN,
        reservation_group_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        reservation_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        scheduled_end_utc: Optional[reservation_get_all_2023_06_06_params.ScheduledEndUtc] | NotGiven = NOT_GIVEN,
        scheduled_start_utc: Optional[reservation_get_all_2023_06_06_params.ScheduledStartUtc] | NotGiven = NOT_GIVEN,
        service_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        states: Optional[
            List[Literal["Inquired", "Confirmed", "Started", "Processed", "Canceled", "Optional", "Requested"]]
        ]
        | NotGiven = NOT_GIVEN,
        updated_utc: Optional[reservation_get_all_2023_06_06_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReservationGetAll2023_06_06Response:
        """
        Returns all reservations within scope of the Access Token, filtered according to
        the specified parameters. This operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          account_ids: Unique identifiers of accounts (currently only
              [Customers](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer),
              in the future also
              [Companies](https://mews-systems.gitbook.io/connector-api/operations/companies/#company))
              the reservation is associated with.

          actual_start_utc: Interval filtering Reservations by their actual start (check-in) time. Cannot be
              used with `ScheduledStartUtc`. Note that the filter applies only to started or
              processed reservations.

          assigned_resource_ids: Unique identifiers of the
              [Resources](https://mews-systems.gitbook.io/connector-api/operations/resources#resource)
              assigned to the reservations.

          availability_block_ids: Unique identifiers of the `Availability blocks` assigned to the reservations.

          colliding_utc: Interval in which the reservations are active. This is defined for a
              `Reservation` as the period between the reservation's scheduled start time
              `ScheduledStartUtc` and its scheduled end time `EndUtc`. Reservation is selected
              if any part of its interval intersects with the interval specified in
              `CollidingUtc

          created_utc: Interval in which the
              [Reservation](https://mews-systems.gitbook.io/connector-api/operations/reservations/#reservation-ver-2023-06-06)
              was created.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          numbers: A list of reservation numbers. Each number uniquely identifies a reservation
              within the system

          reservation_group_ids: Unique identifiers of
              [Reservation groups](https://mews-systems.gitbook.io/connector-api/operations/#reservation-group).

          reservation_ids: Unique identifiers of the
              [Reservations](https://mews-systems.gitbook.io/connector-api/operations/#reservation-ver-2023-06-06).

          scheduled_end_utc: Interval filtering Reservations by their scheduled end time.

          scheduled_start_utc: Interval filtering Reservations by their scheduled start time. Cannot be used
              with `ActualStartUtc`.

          service_ids: Unique identifiers of the
              [Services](https://mews-systems.gitbook.io/connector-api/operations/services/#service).
              If not provided, all bookable services are used.

          states: A list of service order states to filter by.

          updated_utc: Interval in which the `Reservations` were updated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/reservations/getAll/2023-06-06",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "account_ids": account_ids,
                    "actual_start_utc": actual_start_utc,
                    "assigned_resource_ids": assigned_resource_ids,
                    "availability_block_ids": availability_block_ids,
                    "colliding_utc": colliding_utc,
                    "created_utc": created_utc,
                    "enterprise_ids": enterprise_ids,
                    "numbers": numbers,
                    "reservation_group_ids": reservation_group_ids,
                    "reservation_ids": reservation_ids,
                    "scheduled_end_utc": scheduled_end_utc,
                    "scheduled_start_utc": scheduled_start_utc,
                    "service_ids": service_ids,
                    "states": states,
                    "updated_utc": updated_utc,
                },
                reservation_get_all_2023_06_06_params.ReservationGetAll2023_06_06Params,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReservationGetAll2023_06_06Response,
        )

    async def get_all_items(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        reservation_ids: List[str],
        accounting_states: Optional[List[str]] | NotGiven = NOT_GIVEN,
        currency: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReservationGetAllItemsResponse:
        """
        Use orderItems/getAll.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          reservation_ids: Unique identifiers of the reservation.

          accounting_states: States the items should be in. If not specified, items in Open or Closed states
              are returned.

          currency: ISO-4217 code of the
              [Currency](https://mews-systems.gitbook.io/connector-api/operations/currencies/#currency)
              the item costs should be converted to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/reservations/getAllItems",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "reservation_ids": reservation_ids,
                    "accounting_states": accounting_states,
                    "currency": currency,
                },
                reservation_get_all_items_params.ReservationGetAllItemsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReservationGetAllItemsResponse,
        )

    async def price(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        reservations: Iterable[reservation_price_params.Reservation],
        service_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReservationPriceResponse:
        """Returns prices of reservations with the specified parameters.

        Note that the
        operation doesn't check the maximum capacity of requested resource category.
        Requesting person counts above the capacity will return prices for the maximum
        available capacity.

        This operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          reservations: Parameters of the reservations to price. Note that `CustomerId` is not required
              when pricing reservations.

          service_id: Unique identifier of the `Service` to be priced.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/reservations/price",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "reservations": reservations,
                    "service_id": service_id,
                },
                reservation_price_params.ReservationPriceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReservationPriceResponse,
        )

    async def process(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        reservation_id: str,
        allow_open_balance: Optional[bool] | NotGiven = NOT_GIVEN,
        close_bills: Optional[bool] | NotGiven = NOT_GIVEN,
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        notes: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Marks a reservation as `Processed` (= checked out).

        Succeeds only if all
        processing conditions are met (the reservation has the `Started` state, balance
        of all reservation members is zero etc). Note this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        ### Conditions

        - Reservation has already been checked in.
        - Reservation isn't alredy in `Processed` state.
        - Reservation can't be checked out sooner than last day of planned stay.
        - The companion profiles of reservation are complete (details can be found in
          error message).
        - If `AllowOpenBalance` set to `false`, all bills have to be closable (items on
          bills are either paid by current customer, or set to be paid by other
          customer). With `CloseBills` option set to `true` they can be automatically
          closed, when set to `false` they must be closed manually.
        - If `AllowOpenBalance` set to `true`, `Notes` must be filled in.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          reservation_id: Unique identifier of the reservation to process.

          allow_open_balance: Whether non-zero consumed balance of all reservation members is allowed.

          close_bills: Whether closable bills of the reservation members should be automatically
              closed.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          notes: Required if AllowOpenBalance set to true. Used to provide reason for closing
              with unbalanced bill.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/reservations/process",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "reservation_id": reservation_id,
                    "allow_open_balance": allow_open_balance,
                    "close_bills": close_bills,
                    "enterprise_id": enterprise_id,
                    "notes": notes,
                },
                reservation_process_params.ReservationProcessParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def start(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        reservation_id: str,
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Marks a reservation as `Started` (= checked in).

        Succeeds only if all starting
        conditions are met (the reservation has the `Confirmed` state, does not have
        start set to future, has an inspected room assigned etc). Note this operation
        supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          reservation_id: Unique identifier of the reservation to start.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/reservations/start",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "reservation_id": reservation_id,
                    "enterprise_id": enterprise_id,
                },
                reservation_start_params.ReservationStartParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def update_customer(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        customer_id: str,
        reservation_id: str,
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Updates customer of a reservation.

        Note this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          customer_id: Unique identifier of the
              [Customer](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer).

          reservation_id: Unique identifier of the reservation to be updated.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/reservations/updateCustomer",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "customer_id": customer_id,
                    "reservation_id": reservation_id,
                    "enterprise_id": enterprise_id,
                },
                reservation_update_customer_params.ReservationUpdateCustomerParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def update_interval(
        self,
        *,
        access_token: str,
        charge_cancellation_fee: bool,
        client: str,
        client_token: str,
        reservation_id: str,
        end_utc: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        start_utc: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Updates reservation interval (start, end or both).

        Note this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          charge_cancellation_fee: Whether cancellation fee should be charged for potentially canceled nights.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          reservation_id: Unique identifier of the reservation to be updated.

          end_utc: New reservation end in UTC timezone in ISO 8601 format.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          start_utc: New reservation start in UTC timezone in ISO 8601 format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/reservations/updateInterval",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "charge_cancellation_fee": charge_cancellation_fee,
                    "client": client,
                    "client_token": client_token,
                    "reservation_id": reservation_id,
                    "end_utc": end_utc,
                    "enterprise_id": enterprise_id,
                    "start_utc": start_utc,
                },
                reservation_update_interval_params.ReservationUpdateIntervalParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class ReservationsResourceWithRawResponse:
    def __init__(self, reservations: ReservationsResource) -> None:
        self._reservations = reservations

        self.update = to_raw_response_wrapper(
            reservations.update,
        )
        self.add = to_raw_response_wrapper(
            reservations.add,
        )
        self.add_companion = to_raw_response_wrapper(
            reservations.add_companion,
        )
        self.add_product = to_raw_response_wrapper(
            reservations.add_product,
        )
        self.cancel = to_raw_response_wrapper(
            reservations.cancel,
        )
        self.confirm = to_raw_response_wrapper(
            reservations.confirm,
        )
        self.delete_companion = to_raw_response_wrapper(
            reservations.delete_companion,
        )
        self.get_all = to_raw_response_wrapper(
            reservations.get_all,
        )
        self.get_all_2023_06_06 = to_raw_response_wrapper(
            reservations.get_all_2023_06_06,
        )
        self.get_all_items = to_raw_response_wrapper(
            reservations.get_all_items,
        )
        self.price = to_raw_response_wrapper(
            reservations.price,
        )
        self.process = to_raw_response_wrapper(
            reservations.process,
        )
        self.start = to_raw_response_wrapper(
            reservations.start,
        )
        self.update_customer = to_raw_response_wrapper(
            reservations.update_customer,
        )
        self.update_interval = to_raw_response_wrapper(
            reservations.update_interval,
        )


class AsyncReservationsResourceWithRawResponse:
    def __init__(self, reservations: AsyncReservationsResource) -> None:
        self._reservations = reservations

        self.update = async_to_raw_response_wrapper(
            reservations.update,
        )
        self.add = async_to_raw_response_wrapper(
            reservations.add,
        )
        self.add_companion = async_to_raw_response_wrapper(
            reservations.add_companion,
        )
        self.add_product = async_to_raw_response_wrapper(
            reservations.add_product,
        )
        self.cancel = async_to_raw_response_wrapper(
            reservations.cancel,
        )
        self.confirm = async_to_raw_response_wrapper(
            reservations.confirm,
        )
        self.delete_companion = async_to_raw_response_wrapper(
            reservations.delete_companion,
        )
        self.get_all = async_to_raw_response_wrapper(
            reservations.get_all,
        )
        self.get_all_2023_06_06 = async_to_raw_response_wrapper(
            reservations.get_all_2023_06_06,
        )
        self.get_all_items = async_to_raw_response_wrapper(
            reservations.get_all_items,
        )
        self.price = async_to_raw_response_wrapper(
            reservations.price,
        )
        self.process = async_to_raw_response_wrapper(
            reservations.process,
        )
        self.start = async_to_raw_response_wrapper(
            reservations.start,
        )
        self.update_customer = async_to_raw_response_wrapper(
            reservations.update_customer,
        )
        self.update_interval = async_to_raw_response_wrapper(
            reservations.update_interval,
        )


class ReservationsResourceWithStreamingResponse:
    def __init__(self, reservations: ReservationsResource) -> None:
        self._reservations = reservations

        self.update = to_streamed_response_wrapper(
            reservations.update,
        )
        self.add = to_streamed_response_wrapper(
            reservations.add,
        )
        self.add_companion = to_streamed_response_wrapper(
            reservations.add_companion,
        )
        self.add_product = to_streamed_response_wrapper(
            reservations.add_product,
        )
        self.cancel = to_streamed_response_wrapper(
            reservations.cancel,
        )
        self.confirm = to_streamed_response_wrapper(
            reservations.confirm,
        )
        self.delete_companion = to_streamed_response_wrapper(
            reservations.delete_companion,
        )
        self.get_all = to_streamed_response_wrapper(
            reservations.get_all,
        )
        self.get_all_2023_06_06 = to_streamed_response_wrapper(
            reservations.get_all_2023_06_06,
        )
        self.get_all_items = to_streamed_response_wrapper(
            reservations.get_all_items,
        )
        self.price = to_streamed_response_wrapper(
            reservations.price,
        )
        self.process = to_streamed_response_wrapper(
            reservations.process,
        )
        self.start = to_streamed_response_wrapper(
            reservations.start,
        )
        self.update_customer = to_streamed_response_wrapper(
            reservations.update_customer,
        )
        self.update_interval = to_streamed_response_wrapper(
            reservations.update_interval,
        )


class AsyncReservationsResourceWithStreamingResponse:
    def __init__(self, reservations: AsyncReservationsResource) -> None:
        self._reservations = reservations

        self.update = async_to_streamed_response_wrapper(
            reservations.update,
        )
        self.add = async_to_streamed_response_wrapper(
            reservations.add,
        )
        self.add_companion = async_to_streamed_response_wrapper(
            reservations.add_companion,
        )
        self.add_product = async_to_streamed_response_wrapper(
            reservations.add_product,
        )
        self.cancel = async_to_streamed_response_wrapper(
            reservations.cancel,
        )
        self.confirm = async_to_streamed_response_wrapper(
            reservations.confirm,
        )
        self.delete_companion = async_to_streamed_response_wrapper(
            reservations.delete_companion,
        )
        self.get_all = async_to_streamed_response_wrapper(
            reservations.get_all,
        )
        self.get_all_2023_06_06 = async_to_streamed_response_wrapper(
            reservations.get_all_2023_06_06,
        )
        self.get_all_items = async_to_streamed_response_wrapper(
            reservations.get_all_items,
        )
        self.price = async_to_streamed_response_wrapper(
            reservations.price,
        )
        self.process = async_to_streamed_response_wrapper(
            reservations.process,
        )
        self.start = async_to_streamed_response_wrapper(
            reservations.start,
        )
        self.update_customer = async_to_streamed_response_wrapper(
            reservations.update_customer,
        )
        self.update_interval = async_to_streamed_response_wrapper(
            reservations.update_interval,
        )
