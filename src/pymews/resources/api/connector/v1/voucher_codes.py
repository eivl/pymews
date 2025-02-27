# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional

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
from .....types.api.connector.v1 import voucher_code_add_params, voucher_code_list_params, voucher_code_delete_params
from .....types.api.connector.v1.voucher_code_result import VoucherCodeResult

__all__ = ["VoucherCodesResource", "AsyncVoucherCodesResource"]


class VoucherCodesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VoucherCodesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return VoucherCodesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VoucherCodesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return VoucherCodesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: voucher_code_list_params.Limitation,
        voucher_ids: List[str],
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[voucher_code_list_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        voucher_code_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VoucherCodeResult:
        """
        Returns all voucher codes filtered by
        [Voucher](https://mews-systems.gitbook.io/connector-api/operations/vouchers/#voucher)
        or other filter parameters. Note this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          voucher_ids: Unique identifiers of vouchers.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          updated_utc: Interval of voucher code's last update date and time.

          voucher_code_ids: Unique identifiers of the voucher codes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/voucherCodes/getAll",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "voucher_ids": voucher_ids,
                    "enterprise_ids": enterprise_ids,
                    "updated_utc": updated_utc,
                    "voucher_code_ids": voucher_code_ids,
                },
                voucher_code_list_params.VoucherCodeListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoucherCodeResult,
        )

    def delete(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        voucher_code_ids: List[str],
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Delete specified voucher codes.

        Note this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          voucher_code_ids: Unique identifiers of the voucher codes to be deleted.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/voucherCodes/delete",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "voucher_code_ids": voucher_code_ids,
                    "enterprise_id": enterprise_id,
                },
                voucher_code_delete_params.VoucherCodeDeleteParams,
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
        voucher_code_parameters: Iterable[voucher_code_add_params.VoucherCodeParameter],
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VoucherCodeResult:
        """
        Adds voucher codes to the specified
        [Vouchers](https://mews-systems.gitbook.io/connector-api/operations/vouchers/#voucher).
        Note this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          voucher_code_parameters: Voucher codes to be added.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/voucherCodes/add",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "voucher_code_parameters": voucher_code_parameters,
                    "enterprise_id": enterprise_id,
                },
                voucher_code_add_params.VoucherCodeAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoucherCodeResult,
        )


class AsyncVoucherCodesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVoucherCodesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return AsyncVoucherCodesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVoucherCodesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return AsyncVoucherCodesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: voucher_code_list_params.Limitation,
        voucher_ids: List[str],
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[voucher_code_list_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        voucher_code_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VoucherCodeResult:
        """
        Returns all voucher codes filtered by
        [Voucher](https://mews-systems.gitbook.io/connector-api/operations/vouchers/#voucher)
        or other filter parameters. Note this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          voucher_ids: Unique identifiers of vouchers.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          updated_utc: Interval of voucher code's last update date and time.

          voucher_code_ids: Unique identifiers of the voucher codes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/voucherCodes/getAll",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "voucher_ids": voucher_ids,
                    "enterprise_ids": enterprise_ids,
                    "updated_utc": updated_utc,
                    "voucher_code_ids": voucher_code_ids,
                },
                voucher_code_list_params.VoucherCodeListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoucherCodeResult,
        )

    async def delete(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        voucher_code_ids: List[str],
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Delete specified voucher codes.

        Note this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          voucher_code_ids: Unique identifiers of the voucher codes to be deleted.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/voucherCodes/delete",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "voucher_code_ids": voucher_code_ids,
                    "enterprise_id": enterprise_id,
                },
                voucher_code_delete_params.VoucherCodeDeleteParams,
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
        voucher_code_parameters: Iterable[voucher_code_add_params.VoucherCodeParameter],
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VoucherCodeResult:
        """
        Adds voucher codes to the specified
        [Vouchers](https://mews-systems.gitbook.io/connector-api/operations/vouchers/#voucher).
        Note this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          voucher_code_parameters: Voucher codes to be added.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/voucherCodes/add",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "voucher_code_parameters": voucher_code_parameters,
                    "enterprise_id": enterprise_id,
                },
                voucher_code_add_params.VoucherCodeAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoucherCodeResult,
        )


class VoucherCodesResourceWithRawResponse:
    def __init__(self, voucher_codes: VoucherCodesResource) -> None:
        self._voucher_codes = voucher_codes

        self.list = to_raw_response_wrapper(
            voucher_codes.list,
        )
        self.delete = to_raw_response_wrapper(
            voucher_codes.delete,
        )
        self.add = to_raw_response_wrapper(
            voucher_codes.add,
        )


class AsyncVoucherCodesResourceWithRawResponse:
    def __init__(self, voucher_codes: AsyncVoucherCodesResource) -> None:
        self._voucher_codes = voucher_codes

        self.list = async_to_raw_response_wrapper(
            voucher_codes.list,
        )
        self.delete = async_to_raw_response_wrapper(
            voucher_codes.delete,
        )
        self.add = async_to_raw_response_wrapper(
            voucher_codes.add,
        )


class VoucherCodesResourceWithStreamingResponse:
    def __init__(self, voucher_codes: VoucherCodesResource) -> None:
        self._voucher_codes = voucher_codes

        self.list = to_streamed_response_wrapper(
            voucher_codes.list,
        )
        self.delete = to_streamed_response_wrapper(
            voucher_codes.delete,
        )
        self.add = to_streamed_response_wrapper(
            voucher_codes.add,
        )


class AsyncVoucherCodesResourceWithStreamingResponse:
    def __init__(self, voucher_codes: AsyncVoucherCodesResource) -> None:
        self._voucher_codes = voucher_codes

        self.list = async_to_streamed_response_wrapper(
            voucher_codes.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            voucher_codes.delete,
        )
        self.add = async_to_streamed_response_wrapper(
            voucher_codes.add,
        )
