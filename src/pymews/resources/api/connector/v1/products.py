# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from datetime import datetime

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
    product_list_params,
    product_delete_params,
    product_get_pricing_params,
    product_update_price_params,
)
from .....types.api.connector.v1.product_list_response import ProductListResponse
from .....types.api.connector.v1.product_get_pricing_response import ProductGetPricingResponse

__all__ = ["ProductsResource", "AsyncProductsResource"]


class ProductsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProductsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return ProductsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProductsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return ProductsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: product_list_params.Limitation,
        service_ids: List[str],
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        include_default: Optional[bool] | NotGiven = NOT_GIVEN,
        product_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[product_list_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProductListResponse:
        """Returns all products offered together with the specified services.

        Note this
        operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          service_ids: Unique identifiers of the
              [Services](https://mews-systems.gitbook.io/connector-api/operations/services/#service).

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          include_default: Whether or not to include default products for the service, i.e. products which
              are standard includes and not true extras. For example, the night's stay would
              be the default product for a room reservation. These may be useful for
              accounting purposes but should not be displayed to customers for selection. If
              `ProductIds` are provided, `IncludeDefault` defaults to true, otherwise it
              defaults to false.

          product_ids: Unique identifiers of the product.

          updated_utc: Interval in which the products were updated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/products/getAll",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "service_ids": service_ids,
                    "enterprise_ids": enterprise_ids,
                    "include_default": include_default,
                    "product_ids": product_ids,
                    "updated_utc": updated_utc,
                },
                product_list_params.ProductListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProductListResponse,
        )

    def delete(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        product_ids: List[str],
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Deletes specified products.

        This operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          product_ids: Unique identifiers of the products to delete.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/products/delete",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "product_ids": product_ids,
                    "enterprise_id": enterprise_id,
                },
                product_delete_params.ProductDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def get_pricing(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        first_time_unit_start_utc: Union[str, datetime],
        last_time_unit_start_utc: Union[str, datetime],
        product_id: str,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProductGetPricingResponse:
        """Returns prices for a given product for a specified time interval.

        UTC timestamps
        must correspond to the start boundary of a time unit, e.g. 00:00 converted to
        UTC for a time unit of "Day". Other timestamps are not permitted. The **maximum
        size of time interval** depends on the service's time unit: 100 hours if hours,
        100 days if days, or 24 months if months. For more information about time units,
        see
        [Time unit](https://mews-systems.gitbook.io/connector-api/concepts/time-units).
        This operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

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
              100 hours if hours, 100 days if days, or 24 months if months.

          product_id: Unique identifier of the product.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/products/getPricing",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "first_time_unit_start_utc": first_time_unit_start_utc,
                    "last_time_unit_start_utc": last_time_unit_start_utc,
                    "product_id": product_id,
                    "enterprise_ids": enterprise_ids,
                },
                product_get_pricing_params.ProductGetPricingParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProductGetPricingResponse,
        )

    def update_price(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        price_updates: Iterable[product_update_price_params.PriceUpdate],
        product_id: str,
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Updates the prices for a given product.

        You can make multiple price updates with
        one API call, and for each one specify the price amount per
        [Time unit](https://mews-systems.gitbook.io/connector-api/concepts/time-units)
        and the time interval for which it applies. The price will be updated for all
        service time units that the specified time interval intersects. It is not
        permitted to update historical prices older than specified by
        `EditableHistoryInterval`. This operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          price_updates: Price adjustments for specific time intervals.

          product_id: Unique identifier of the `Product`.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/products/updatePrice",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "price_updates": price_updates,
                    "product_id": product_id,
                    "enterprise_id": enterprise_id,
                },
                product_update_price_params.ProductUpdatePriceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncProductsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProductsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return AsyncProductsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProductsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return AsyncProductsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: product_list_params.Limitation,
        service_ids: List[str],
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        include_default: Optional[bool] | NotGiven = NOT_GIVEN,
        product_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[product_list_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProductListResponse:
        """Returns all products offered together with the specified services.

        Note this
        operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          service_ids: Unique identifiers of the
              [Services](https://mews-systems.gitbook.io/connector-api/operations/services/#service).

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          include_default: Whether or not to include default products for the service, i.e. products which
              are standard includes and not true extras. For example, the night's stay would
              be the default product for a room reservation. These may be useful for
              accounting purposes but should not be displayed to customers for selection. If
              `ProductIds` are provided, `IncludeDefault` defaults to true, otherwise it
              defaults to false.

          product_ids: Unique identifiers of the product.

          updated_utc: Interval in which the products were updated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/products/getAll",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "service_ids": service_ids,
                    "enterprise_ids": enterprise_ids,
                    "include_default": include_default,
                    "product_ids": product_ids,
                    "updated_utc": updated_utc,
                },
                product_list_params.ProductListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProductListResponse,
        )

    async def delete(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        product_ids: List[str],
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Deletes specified products.

        This operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          product_ids: Unique identifiers of the products to delete.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/products/delete",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "product_ids": product_ids,
                    "enterprise_id": enterprise_id,
                },
                product_delete_params.ProductDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def get_pricing(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        first_time_unit_start_utc: Union[str, datetime],
        last_time_unit_start_utc: Union[str, datetime],
        product_id: str,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProductGetPricingResponse:
        """Returns prices for a given product for a specified time interval.

        UTC timestamps
        must correspond to the start boundary of a time unit, e.g. 00:00 converted to
        UTC for a time unit of "Day". Other timestamps are not permitted. The **maximum
        size of time interval** depends on the service's time unit: 100 hours if hours,
        100 days if days, or 24 months if months. For more information about time units,
        see
        [Time unit](https://mews-systems.gitbook.io/connector-api/concepts/time-units).
        This operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

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
              100 hours if hours, 100 days if days, or 24 months if months.

          product_id: Unique identifier of the product.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/products/getPricing",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "first_time_unit_start_utc": first_time_unit_start_utc,
                    "last_time_unit_start_utc": last_time_unit_start_utc,
                    "product_id": product_id,
                    "enterprise_ids": enterprise_ids,
                },
                product_get_pricing_params.ProductGetPricingParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProductGetPricingResponse,
        )

    async def update_price(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        price_updates: Iterable[product_update_price_params.PriceUpdate],
        product_id: str,
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Updates the prices for a given product.

        You can make multiple price updates with
        one API call, and for each one specify the price amount per
        [Time unit](https://mews-systems.gitbook.io/connector-api/concepts/time-units)
        and the time interval for which it applies. The price will be updated for all
        service time units that the specified time interval intersects. It is not
        permitted to update historical prices older than specified by
        `EditableHistoryInterval`. This operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          price_updates: Price adjustments for specific time intervals.

          product_id: Unique identifier of the `Product`.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/products/updatePrice",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "price_updates": price_updates,
                    "product_id": product_id,
                    "enterprise_id": enterprise_id,
                },
                product_update_price_params.ProductUpdatePriceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class ProductsResourceWithRawResponse:
    def __init__(self, products: ProductsResource) -> None:
        self._products = products

        self.list = to_raw_response_wrapper(
            products.list,
        )
        self.delete = to_raw_response_wrapper(
            products.delete,
        )
        self.get_pricing = to_raw_response_wrapper(
            products.get_pricing,
        )
        self.update_price = to_raw_response_wrapper(
            products.update_price,
        )


class AsyncProductsResourceWithRawResponse:
    def __init__(self, products: AsyncProductsResource) -> None:
        self._products = products

        self.list = async_to_raw_response_wrapper(
            products.list,
        )
        self.delete = async_to_raw_response_wrapper(
            products.delete,
        )
        self.get_pricing = async_to_raw_response_wrapper(
            products.get_pricing,
        )
        self.update_price = async_to_raw_response_wrapper(
            products.update_price,
        )


class ProductsResourceWithStreamingResponse:
    def __init__(self, products: ProductsResource) -> None:
        self._products = products

        self.list = to_streamed_response_wrapper(
            products.list,
        )
        self.delete = to_streamed_response_wrapper(
            products.delete,
        )
        self.get_pricing = to_streamed_response_wrapper(
            products.get_pricing,
        )
        self.update_price = to_streamed_response_wrapper(
            products.update_price,
        )


class AsyncProductsResourceWithStreamingResponse:
    def __init__(self, products: AsyncProductsResource) -> None:
        self._products = products

        self.list = async_to_streamed_response_wrapper(
            products.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            products.delete,
        )
        self.get_pricing = async_to_streamed_response_wrapper(
            products.get_pricing,
        )
        self.update_price = async_to_streamed_response_wrapper(
            products.update_price,
        )
