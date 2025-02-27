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
    voucher_add_params,
    voucher_list_params,
    voucher_delete_params,
    voucher_update_params,
)
from .....types.api.connector.v1.voucher_write_result import VoucherWriteResult
from .....types.api.connector.v1.voucher_list_response import VoucherListResponse

__all__ = ["VouchersResource", "AsyncVouchersResource"]


class VouchersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VouchersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return VouchersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VouchersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return VouchersResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        voucher_updates: Iterable[voucher_update_params.VoucherUpdate],
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VoucherWriteResult:
        """Updates information about the specified vouchers.

        Note this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          voucher_updates: Details of voucher updates.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/vouchers/update",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "voucher_updates": voucher_updates,
                    "enterprise_id": enterprise_id,
                },
                voucher_update_params.VoucherUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoucherWriteResult,
        )

    def list(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        extent: voucher_list_params.Extent,
        limitation: voucher_list_params.Limitation,
        service_ids: List[str],
        activity_states: Optional[List[Literal["Deleted", "Active"]]] | NotGiven = NOT_GIVEN,
        company_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        external_identifiers: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[voucher_list_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        voucher_code_values: Optional[List[str]] | NotGiven = NOT_GIVEN,
        voucher_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VoucherListResponse:
        """
        Returns all rate vouchers filtered by
        [Service](https://mews-systems.gitbook.io/connector-api/operations/services/#service),
        voucher code or voucher identifier. Note this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          extent: Extent of data to be returned. Whether only specific voucher info should be
              returned or related items as well.

          limitation: Limitation on the quantity of data returned.

          service_ids: Unique identifiers of
              [Services](https://mews-systems.gitbook.io/connector-api/operations/services/#service)
              where the vouchers belong to.

          activity_states: Whether to return only active, only deleted, or both types of record. If not
              specified, both active and deleted records will be returned.

          company_ids: Unique identifiers of the companies.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          external_identifiers: Identifiers of
              [Voucher](https://mews-systems.gitbook.io/connector-api/operations/#voucher)
              from external systems.

          voucher_code_values: Value of voucher codes used by customers.

          voucher_ids: Unique identifiers of vouchers.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/vouchers/getAll",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "extent": extent,
                    "limitation": limitation,
                    "service_ids": service_ids,
                    "activity_states": activity_states,
                    "company_ids": company_ids,
                    "enterprise_ids": enterprise_ids,
                    "external_identifiers": external_identifiers,
                    "updated_utc": updated_utc,
                    "voucher_code_values": voucher_code_values,
                    "voucher_ids": voucher_ids,
                },
                voucher_list_params.VoucherListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoucherListResponse,
        )

    def delete(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        voucher_ids: List[str],
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Delete specified vouchers.

        Note this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          voucher_ids: Unique identifiers of the vouchers to be deleted.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/vouchers/delete",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "voucher_ids": voucher_ids,
                    "enterprise_id": enterprise_id,
                },
                voucher_delete_params.VoucherDeleteParams,
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
        voucher_parameters: Iterable[voucher_add_params.VoucherParameter],
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VoucherWriteResult:
        """
        Adds the specified vouchers to the specified
        [Services](https://mews-systems.gitbook.io/connector-api/operations/services/#service).
        Note this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          voucher_parameters: Vouchers to be added.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/vouchers/add",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "voucher_parameters": voucher_parameters,
                    "enterprise_id": enterprise_id,
                },
                voucher_add_params.VoucherAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoucherWriteResult,
        )


class AsyncVouchersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVouchersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return AsyncVouchersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVouchersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return AsyncVouchersResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        voucher_updates: Iterable[voucher_update_params.VoucherUpdate],
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VoucherWriteResult:
        """Updates information about the specified vouchers.

        Note this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          voucher_updates: Details of voucher updates.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/vouchers/update",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "voucher_updates": voucher_updates,
                    "enterprise_id": enterprise_id,
                },
                voucher_update_params.VoucherUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoucherWriteResult,
        )

    async def list(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        extent: voucher_list_params.Extent,
        limitation: voucher_list_params.Limitation,
        service_ids: List[str],
        activity_states: Optional[List[Literal["Deleted", "Active"]]] | NotGiven = NOT_GIVEN,
        company_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        external_identifiers: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[voucher_list_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        voucher_code_values: Optional[List[str]] | NotGiven = NOT_GIVEN,
        voucher_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VoucherListResponse:
        """
        Returns all rate vouchers filtered by
        [Service](https://mews-systems.gitbook.io/connector-api/operations/services/#service),
        voucher code or voucher identifier. Note this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          extent: Extent of data to be returned. Whether only specific voucher info should be
              returned or related items as well.

          limitation: Limitation on the quantity of data returned.

          service_ids: Unique identifiers of
              [Services](https://mews-systems.gitbook.io/connector-api/operations/services/#service)
              where the vouchers belong to.

          activity_states: Whether to return only active, only deleted, or both types of record. If not
              specified, both active and deleted records will be returned.

          company_ids: Unique identifiers of the companies.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          external_identifiers: Identifiers of
              [Voucher](https://mews-systems.gitbook.io/connector-api/operations/#voucher)
              from external systems.

          voucher_code_values: Value of voucher codes used by customers.

          voucher_ids: Unique identifiers of vouchers.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/vouchers/getAll",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "extent": extent,
                    "limitation": limitation,
                    "service_ids": service_ids,
                    "activity_states": activity_states,
                    "company_ids": company_ids,
                    "enterprise_ids": enterprise_ids,
                    "external_identifiers": external_identifiers,
                    "updated_utc": updated_utc,
                    "voucher_code_values": voucher_code_values,
                    "voucher_ids": voucher_ids,
                },
                voucher_list_params.VoucherListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoucherListResponse,
        )

    async def delete(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        voucher_ids: List[str],
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Delete specified vouchers.

        Note this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          voucher_ids: Unique identifiers of the vouchers to be deleted.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/vouchers/delete",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "voucher_ids": voucher_ids,
                    "enterprise_id": enterprise_id,
                },
                voucher_delete_params.VoucherDeleteParams,
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
        voucher_parameters: Iterable[voucher_add_params.VoucherParameter],
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VoucherWriteResult:
        """
        Adds the specified vouchers to the specified
        [Services](https://mews-systems.gitbook.io/connector-api/operations/services/#service).
        Note this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          voucher_parameters: Vouchers to be added.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/vouchers/add",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "voucher_parameters": voucher_parameters,
                    "enterprise_id": enterprise_id,
                },
                voucher_add_params.VoucherAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoucherWriteResult,
        )


class VouchersResourceWithRawResponse:
    def __init__(self, vouchers: VouchersResource) -> None:
        self._vouchers = vouchers

        self.update = to_raw_response_wrapper(
            vouchers.update,
        )
        self.list = to_raw_response_wrapper(
            vouchers.list,
        )
        self.delete = to_raw_response_wrapper(
            vouchers.delete,
        )
        self.add = to_raw_response_wrapper(
            vouchers.add,
        )


class AsyncVouchersResourceWithRawResponse:
    def __init__(self, vouchers: AsyncVouchersResource) -> None:
        self._vouchers = vouchers

        self.update = async_to_raw_response_wrapper(
            vouchers.update,
        )
        self.list = async_to_raw_response_wrapper(
            vouchers.list,
        )
        self.delete = async_to_raw_response_wrapper(
            vouchers.delete,
        )
        self.add = async_to_raw_response_wrapper(
            vouchers.add,
        )


class VouchersResourceWithStreamingResponse:
    def __init__(self, vouchers: VouchersResource) -> None:
        self._vouchers = vouchers

        self.update = to_streamed_response_wrapper(
            vouchers.update,
        )
        self.list = to_streamed_response_wrapper(
            vouchers.list,
        )
        self.delete = to_streamed_response_wrapper(
            vouchers.delete,
        )
        self.add = to_streamed_response_wrapper(
            vouchers.add,
        )


class AsyncVouchersResourceWithStreamingResponse:
    def __init__(self, vouchers: AsyncVouchersResource) -> None:
        self._vouchers = vouchers

        self.update = async_to_streamed_response_wrapper(
            vouchers.update,
        )
        self.list = async_to_streamed_response_wrapper(
            vouchers.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            vouchers.delete,
        )
        self.add = async_to_streamed_response_wrapper(
            vouchers.add,
        )
