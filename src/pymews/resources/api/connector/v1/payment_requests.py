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
    payment_request_add_params,
    payment_request_list_params,
    payment_request_cancel_params,
)
from .....types.api.connector.v1.payment_request_result import PaymentRequestResult

__all__ = ["PaymentRequestsResource", "AsyncPaymentRequestsResource"]


class PaymentRequestsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PaymentRequestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return PaymentRequestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PaymentRequestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return PaymentRequestsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: payment_request_list_params.Limitation,
        account_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        payment_request_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        reservation_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        states: Optional[List[Literal["Pending", "Completed", "Canceled", "Expired"]]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[payment_request_list_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentRequestResult:
        """Get all payment requests belonging to the specified customer accounts.

        Note this
        operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          account_ids: Unique identifiers of
              [Customer](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer)
              accounts to which payment requests were issued.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          payment_request_ids: Unique identifiers of the requested
              [Payment requests](https://mews-systems.gitbook.io/connector-api/operations/#payment-request).

          states: A list of payment request states to filter by.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/paymentRequests/getAll",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "account_ids": account_ids,
                    "enterprise_ids": enterprise_ids,
                    "payment_request_ids": payment_request_ids,
                    "reservation_ids": reservation_ids,
                    "states": states,
                    "updated_utc": updated_utc,
                },
                payment_request_list_params.PaymentRequestListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentRequestResult,
        )

    def add(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        payment_requests: Iterable[payment_request_add_params.PaymentRequest],
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentRequestResult:
        """
        Creates a payment request to the specified
        [Customer](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer).
        Note this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          payment_requests: Payment requests to be added.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/paymentRequests/add",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "payment_requests": payment_requests,
                    "enterprise_id": enterprise_id,
                },
                payment_request_add_params.PaymentRequestAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentRequestResult,
        )

    def cancel(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        payment_request_ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentRequestResult:
        """Cancels specified payment requests.

        Only payment requests which are in `Pending`
        state can be canceled.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          payment_request_ids: Identifiers of payment requests to be canceled.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/paymentRequests/cancel",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "payment_request_ids": payment_request_ids,
                },
                payment_request_cancel_params.PaymentRequestCancelParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentRequestResult,
        )


class AsyncPaymentRequestsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPaymentRequestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return AsyncPaymentRequestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPaymentRequestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return AsyncPaymentRequestsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: payment_request_list_params.Limitation,
        account_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        payment_request_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        reservation_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        states: Optional[List[Literal["Pending", "Completed", "Canceled", "Expired"]]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[payment_request_list_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentRequestResult:
        """Get all payment requests belonging to the specified customer accounts.

        Note this
        operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          account_ids: Unique identifiers of
              [Customer](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer)
              accounts to which payment requests were issued.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          payment_request_ids: Unique identifiers of the requested
              [Payment requests](https://mews-systems.gitbook.io/connector-api/operations/#payment-request).

          states: A list of payment request states to filter by.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/paymentRequests/getAll",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "account_ids": account_ids,
                    "enterprise_ids": enterprise_ids,
                    "payment_request_ids": payment_request_ids,
                    "reservation_ids": reservation_ids,
                    "states": states,
                    "updated_utc": updated_utc,
                },
                payment_request_list_params.PaymentRequestListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentRequestResult,
        )

    async def add(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        payment_requests: Iterable[payment_request_add_params.PaymentRequest],
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentRequestResult:
        """
        Creates a payment request to the specified
        [Customer](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer).
        Note this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          payment_requests: Payment requests to be added.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/paymentRequests/add",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "payment_requests": payment_requests,
                    "enterprise_id": enterprise_id,
                },
                payment_request_add_params.PaymentRequestAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentRequestResult,
        )

    async def cancel(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        payment_request_ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentRequestResult:
        """Cancels specified payment requests.

        Only payment requests which are in `Pending`
        state can be canceled.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          payment_request_ids: Identifiers of payment requests to be canceled.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/paymentRequests/cancel",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "payment_request_ids": payment_request_ids,
                },
                payment_request_cancel_params.PaymentRequestCancelParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentRequestResult,
        )


class PaymentRequestsResourceWithRawResponse:
    def __init__(self, payment_requests: PaymentRequestsResource) -> None:
        self._payment_requests = payment_requests

        self.list = to_raw_response_wrapper(
            payment_requests.list,
        )
        self.add = to_raw_response_wrapper(
            payment_requests.add,
        )
        self.cancel = to_raw_response_wrapper(
            payment_requests.cancel,
        )


class AsyncPaymentRequestsResourceWithRawResponse:
    def __init__(self, payment_requests: AsyncPaymentRequestsResource) -> None:
        self._payment_requests = payment_requests

        self.list = async_to_raw_response_wrapper(
            payment_requests.list,
        )
        self.add = async_to_raw_response_wrapper(
            payment_requests.add,
        )
        self.cancel = async_to_raw_response_wrapper(
            payment_requests.cancel,
        )


class PaymentRequestsResourceWithStreamingResponse:
    def __init__(self, payment_requests: PaymentRequestsResource) -> None:
        self._payment_requests = payment_requests

        self.list = to_streamed_response_wrapper(
            payment_requests.list,
        )
        self.add = to_streamed_response_wrapper(
            payment_requests.add,
        )
        self.cancel = to_streamed_response_wrapper(
            payment_requests.cancel,
        )


class AsyncPaymentRequestsResourceWithStreamingResponse:
    def __init__(self, payment_requests: AsyncPaymentRequestsResource) -> None:
        self._payment_requests = payment_requests

        self.list = async_to_streamed_response_wrapper(
            payment_requests.list,
        )
        self.add = async_to_streamed_response_wrapper(
            payment_requests.add,
        )
        self.cancel = async_to_streamed_response_wrapper(
            payment_requests.cancel,
        )
