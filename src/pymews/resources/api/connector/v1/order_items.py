# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
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
from .....types.api.connector.v1 import order_item_list_params, order_item_cancel_params
from .....types.api.connector.v1.order_item_list_response import OrderItemListResponse

__all__ = ["OrderItemsResource", "AsyncOrderItemsResource"]


class OrderItemsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OrderItemsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return OrderItemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrderItemsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return OrderItemsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: order_item_list_params.Limitation,
        accounting_states: Optional[List[Literal["Open", "Closed", "Inactive", "Canceled"]]] | NotGiven = NOT_GIVEN,
        bill_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        canceled_utc: Optional[order_item_list_params.CanceledUtc] | NotGiven = NOT_GIVEN,
        closed_utc: Optional[order_item_list_params.ClosedUtc] | NotGiven = NOT_GIVEN,
        consumed_utc: Optional[order_item_list_params.ConsumedUtc] | NotGiven = NOT_GIVEN,
        created_utc: Optional[order_item_list_params.CreatedUtc] | NotGiven = NOT_GIVEN,
        currency: Optional[str] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        order_item_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        service_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        service_order_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        types: Optional[
            List[
                Literal[
                    "CancellationFee",
                    "NightRebate",
                    "ProductOrderRebate",
                    "AdditionalExpenseRebate",
                    "Deposit",
                    "ExchangeRateDifference",
                    "CustomItem",
                    "ServiceCharge",
                    "CityTax",
                    "CityTaxDiscount",
                    "SpaceOrder",
                    "ProductOrder",
                    "Surcharge",
                    "TaxCorrection",
                    "ResourceUpgradeFee",
                    "InvoiceFee",
                    "MulticurrencyFee",
                    "AllowanceDiscount",
                ]
            ]
        ]
        | NotGiven = NOT_GIVEN,
        updated_utc: Optional[order_item_list_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrderItemListResponse:
        """Returns all order items.

        At least one of the `OrderItemIds`, `ServiceOrderIds`,
        `ServiceIds`, `BillIds`, `CreatedUtc`, `UpdatedUtc`, `ClosedUtc` filters must be
        specified in the request. Note this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          accounting_states: Accounting state of the item.

          bill_ids: Unique identifiers of the
              [Bills](https://mews-systems.gitbook.io/connector-api/operations/bills/#bill) to
              which order item is assigned. Required if no other filter is provided.

          canceled_utc: Interval in which the
              [Order item](https://mews-systems.gitbook.io/connector-api/operations/orderitems/#order-item)
              was canceled. Required if no other filter is provided.

          closed_utc: Interval in which the
              [Order item](https://mews-systems.gitbook.io/connector-api/operations/orderitems/#order-item)
              was closed. Required if no other filter is provided.

          consumed_utc: Interval in which the
              [Order item](https://mews-systems.gitbook.io/connector-api/operations/orderitems/#order-item)
              was consumed. Required if no other filter is provided.

          created_utc: Interval in which the
              [Order item](https://mews-systems.gitbook.io/connector-api/operations/orderitems/#order-item)
              was created. Required if no other filter is provided.

          currency: ISO-4217 code of the
              [Currency](https://mews-systems.gitbook.io/connector-api/operations/currencies/#currency)
              the item costs should be converted to.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          order_item_ids: Unique identifiers of the
              [Order items](https://mews-systems.gitbook.io/connector-api/operations/orderitems/#order-item).
              Required if no other filter is provided.

          service_ids: Unique identifiers of the
              [Services](https://mews-systems.gitbook.io/connector-api/operations/services/#service).
              Required if no other filter is provided.

          service_order_ids: Unique identifiers of the service orders
              ([product service orders](https://mews-systems.gitbook.io/connector-api/operations/productserviceorders/#product-service-order)
              or
              [reservations](https://mews-systems.gitbook.io/connector-api/operations/reservations/#reservation-ver-2023-06-06)).
              Required if no other filter is provided.

          types: Order item type, e.g. whether product order or space order.

          updated_utc: Interval in which the
              [Order item](https://mews-systems.gitbook.io/connector-api/operations/orderitems/#order-item)
              was updated. Required if no other filter is provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/orderItems/getAll",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "accounting_states": accounting_states,
                    "bill_ids": bill_ids,
                    "canceled_utc": canceled_utc,
                    "closed_utc": closed_utc,
                    "consumed_utc": consumed_utc,
                    "created_utc": created_utc,
                    "currency": currency,
                    "enterprise_ids": enterprise_ids,
                    "order_item_ids": order_item_ids,
                    "service_ids": service_ids,
                    "service_order_ids": service_order_ids,
                    "types": types,
                    "updated_utc": updated_utc,
                },
                order_item_list_params.OrderItemListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrderItemListResponse,
        )

    def cancel(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        order_item_ids: List[str],
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Cancels all order items with specified identifiers.

        Note this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          order_item_ids: Unique identifiers of the `OrderItems` to cancel.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/orderItems/cancel",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "order_item_ids": order_item_ids,
                    "enterprise_id": enterprise_id,
                },
                order_item_cancel_params.OrderItemCancelParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncOrderItemsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOrderItemsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return AsyncOrderItemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrderItemsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return AsyncOrderItemsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: order_item_list_params.Limitation,
        accounting_states: Optional[List[Literal["Open", "Closed", "Inactive", "Canceled"]]] | NotGiven = NOT_GIVEN,
        bill_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        canceled_utc: Optional[order_item_list_params.CanceledUtc] | NotGiven = NOT_GIVEN,
        closed_utc: Optional[order_item_list_params.ClosedUtc] | NotGiven = NOT_GIVEN,
        consumed_utc: Optional[order_item_list_params.ConsumedUtc] | NotGiven = NOT_GIVEN,
        created_utc: Optional[order_item_list_params.CreatedUtc] | NotGiven = NOT_GIVEN,
        currency: Optional[str] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        order_item_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        service_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        service_order_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        types: Optional[
            List[
                Literal[
                    "CancellationFee",
                    "NightRebate",
                    "ProductOrderRebate",
                    "AdditionalExpenseRebate",
                    "Deposit",
                    "ExchangeRateDifference",
                    "CustomItem",
                    "ServiceCharge",
                    "CityTax",
                    "CityTaxDiscount",
                    "SpaceOrder",
                    "ProductOrder",
                    "Surcharge",
                    "TaxCorrection",
                    "ResourceUpgradeFee",
                    "InvoiceFee",
                    "MulticurrencyFee",
                    "AllowanceDiscount",
                ]
            ]
        ]
        | NotGiven = NOT_GIVEN,
        updated_utc: Optional[order_item_list_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrderItemListResponse:
        """Returns all order items.

        At least one of the `OrderItemIds`, `ServiceOrderIds`,
        `ServiceIds`, `BillIds`, `CreatedUtc`, `UpdatedUtc`, `ClosedUtc` filters must be
        specified in the request. Note this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          accounting_states: Accounting state of the item.

          bill_ids: Unique identifiers of the
              [Bills](https://mews-systems.gitbook.io/connector-api/operations/bills/#bill) to
              which order item is assigned. Required if no other filter is provided.

          canceled_utc: Interval in which the
              [Order item](https://mews-systems.gitbook.io/connector-api/operations/orderitems/#order-item)
              was canceled. Required if no other filter is provided.

          closed_utc: Interval in which the
              [Order item](https://mews-systems.gitbook.io/connector-api/operations/orderitems/#order-item)
              was closed. Required if no other filter is provided.

          consumed_utc: Interval in which the
              [Order item](https://mews-systems.gitbook.io/connector-api/operations/orderitems/#order-item)
              was consumed. Required if no other filter is provided.

          created_utc: Interval in which the
              [Order item](https://mews-systems.gitbook.io/connector-api/operations/orderitems/#order-item)
              was created. Required if no other filter is provided.

          currency: ISO-4217 code of the
              [Currency](https://mews-systems.gitbook.io/connector-api/operations/currencies/#currency)
              the item costs should be converted to.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          order_item_ids: Unique identifiers of the
              [Order items](https://mews-systems.gitbook.io/connector-api/operations/orderitems/#order-item).
              Required if no other filter is provided.

          service_ids: Unique identifiers of the
              [Services](https://mews-systems.gitbook.io/connector-api/operations/services/#service).
              Required if no other filter is provided.

          service_order_ids: Unique identifiers of the service orders
              ([product service orders](https://mews-systems.gitbook.io/connector-api/operations/productserviceorders/#product-service-order)
              or
              [reservations](https://mews-systems.gitbook.io/connector-api/operations/reservations/#reservation-ver-2023-06-06)).
              Required if no other filter is provided.

          types: Order item type, e.g. whether product order or space order.

          updated_utc: Interval in which the
              [Order item](https://mews-systems.gitbook.io/connector-api/operations/orderitems/#order-item)
              was updated. Required if no other filter is provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/orderItems/getAll",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "accounting_states": accounting_states,
                    "bill_ids": bill_ids,
                    "canceled_utc": canceled_utc,
                    "closed_utc": closed_utc,
                    "consumed_utc": consumed_utc,
                    "created_utc": created_utc,
                    "currency": currency,
                    "enterprise_ids": enterprise_ids,
                    "order_item_ids": order_item_ids,
                    "service_ids": service_ids,
                    "service_order_ids": service_order_ids,
                    "types": types,
                    "updated_utc": updated_utc,
                },
                order_item_list_params.OrderItemListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrderItemListResponse,
        )

    async def cancel(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        order_item_ids: List[str],
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Cancels all order items with specified identifiers.

        Note this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          order_item_ids: Unique identifiers of the `OrderItems` to cancel.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/orderItems/cancel",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "order_item_ids": order_item_ids,
                    "enterprise_id": enterprise_id,
                },
                order_item_cancel_params.OrderItemCancelParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class OrderItemsResourceWithRawResponse:
    def __init__(self, order_items: OrderItemsResource) -> None:
        self._order_items = order_items

        self.list = to_raw_response_wrapper(
            order_items.list,
        )
        self.cancel = to_raw_response_wrapper(
            order_items.cancel,
        )


class AsyncOrderItemsResourceWithRawResponse:
    def __init__(self, order_items: AsyncOrderItemsResource) -> None:
        self._order_items = order_items

        self.list = async_to_raw_response_wrapper(
            order_items.list,
        )
        self.cancel = async_to_raw_response_wrapper(
            order_items.cancel,
        )


class OrderItemsResourceWithStreamingResponse:
    def __init__(self, order_items: OrderItemsResource) -> None:
        self._order_items = order_items

        self.list = to_streamed_response_wrapper(
            order_items.list,
        )
        self.cancel = to_streamed_response_wrapper(
            order_items.cancel,
        )


class AsyncOrderItemsResourceWithStreamingResponse:
    def __init__(self, order_items: AsyncOrderItemsResource) -> None:
        self._order_items = order_items

        self.list = async_to_streamed_response_wrapper(
            order_items.list,
        )
        self.cancel = async_to_streamed_response_wrapper(
            order_items.cancel,
        )
