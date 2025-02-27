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
from .....types.api.connector.v1 import accounting_item_list_params, accounting_item_update_params
from .....types.api.connector.v1.accounting_item_result import AccountingItemResult

__all__ = ["AccountingItemsResource", "AsyncAccountingItemsResource"]


class AccountingItemsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccountingItemsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return AccountingItemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountingItemsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return AccountingItemsResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        access_token: str,
        accounting_item_updates: Iterable[accounting_item_update_params.AccountingItemUpdate],
        client: str,
        client_token: str,
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountingItemResult:
        """Updates specified accounting items.

        You can use this operation to assign an
        accounting item to a different account or bill. Note this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          accounting_item_updates: List of requested updates.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/accountingItems/update",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "accounting_item_updates": accounting_item_updates,
                    "client": client,
                    "client_token": client_token,
                    "enterprise_id": enterprise_id,
                },
                accounting_item_update_params.AccountingItemUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountingItemResult,
        )

    def list(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        end_utc: Union[str, datetime],
        extent: accounting_item_list_params.Extent,
        start_utc: Union[str, datetime],
        closed_utc: Optional[accounting_item_list_params.ClosedUtc] | NotGiven = NOT_GIVEN,
        consumed_utc: Optional[accounting_item_list_params.ConsumedUtc] | NotGiven = NOT_GIVEN,
        currency: Optional[str] | NotGiven = NOT_GIVEN,
        item_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        rebated_item_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        states: Optional[List[str]] | NotGiven = NOT_GIVEN,
        time_filter: Optional[str] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[accounting_item_list_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountingItemResult:
        """
        Use `payments/getAll` or `orderItems/getAll`.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          extent: Extent of data to be returned. E.g. it is possible to specify that together with
              the accounting items, credit card transactions should be also returned.

          currency: ISO-4217 code of the
              [Currency](https://mews-systems.gitbook.io/connector-api/operations/currencies/#currency)
              the item costs should be converted to.

          item_ids: Unique identifiers of the Accounting items. Required if no other filter is
              provided.

          rebated_item_ids: Unique identifiers of the Accounting items we are finding rebates for. Required
              if no other filter is provided.

          states: States the accounting items should be in. If not specified, accounting items in
              Open or Closed states are returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/accountingItems/getAll",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "end_utc": end_utc,
                    "extent": extent,
                    "start_utc": start_utc,
                    "closed_utc": closed_utc,
                    "consumed_utc": consumed_utc,
                    "currency": currency,
                    "item_ids": item_ids,
                    "rebated_item_ids": rebated_item_ids,
                    "states": states,
                    "time_filter": time_filter,
                    "updated_utc": updated_utc,
                },
                accounting_item_list_params.AccountingItemListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountingItemResult,
        )


class AsyncAccountingItemsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccountingItemsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return AsyncAccountingItemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountingItemsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return AsyncAccountingItemsResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        access_token: str,
        accounting_item_updates: Iterable[accounting_item_update_params.AccountingItemUpdate],
        client: str,
        client_token: str,
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountingItemResult:
        """Updates specified accounting items.

        You can use this operation to assign an
        accounting item to a different account or bill. Note this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          accounting_item_updates: List of requested updates.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/accountingItems/update",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "accounting_item_updates": accounting_item_updates,
                    "client": client,
                    "client_token": client_token,
                    "enterprise_id": enterprise_id,
                },
                accounting_item_update_params.AccountingItemUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountingItemResult,
        )

    async def list(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        end_utc: Union[str, datetime],
        extent: accounting_item_list_params.Extent,
        start_utc: Union[str, datetime],
        closed_utc: Optional[accounting_item_list_params.ClosedUtc] | NotGiven = NOT_GIVEN,
        consumed_utc: Optional[accounting_item_list_params.ConsumedUtc] | NotGiven = NOT_GIVEN,
        currency: Optional[str] | NotGiven = NOT_GIVEN,
        item_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        rebated_item_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        states: Optional[List[str]] | NotGiven = NOT_GIVEN,
        time_filter: Optional[str] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[accounting_item_list_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountingItemResult:
        """
        Use `payments/getAll` or `orderItems/getAll`.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          extent: Extent of data to be returned. E.g. it is possible to specify that together with
              the accounting items, credit card transactions should be also returned.

          currency: ISO-4217 code of the
              [Currency](https://mews-systems.gitbook.io/connector-api/operations/currencies/#currency)
              the item costs should be converted to.

          item_ids: Unique identifiers of the Accounting items. Required if no other filter is
              provided.

          rebated_item_ids: Unique identifiers of the Accounting items we are finding rebates for. Required
              if no other filter is provided.

          states: States the accounting items should be in. If not specified, accounting items in
              Open or Closed states are returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/accountingItems/getAll",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "end_utc": end_utc,
                    "extent": extent,
                    "start_utc": start_utc,
                    "closed_utc": closed_utc,
                    "consumed_utc": consumed_utc,
                    "currency": currency,
                    "item_ids": item_ids,
                    "rebated_item_ids": rebated_item_ids,
                    "states": states,
                    "time_filter": time_filter,
                    "updated_utc": updated_utc,
                },
                accounting_item_list_params.AccountingItemListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountingItemResult,
        )


class AccountingItemsResourceWithRawResponse:
    def __init__(self, accounting_items: AccountingItemsResource) -> None:
        self._accounting_items = accounting_items

        self.update = to_raw_response_wrapper(
            accounting_items.update,
        )
        self.list = to_raw_response_wrapper(
            accounting_items.list,
        )


class AsyncAccountingItemsResourceWithRawResponse:
    def __init__(self, accounting_items: AsyncAccountingItemsResource) -> None:
        self._accounting_items = accounting_items

        self.update = async_to_raw_response_wrapper(
            accounting_items.update,
        )
        self.list = async_to_raw_response_wrapper(
            accounting_items.list,
        )


class AccountingItemsResourceWithStreamingResponse:
    def __init__(self, accounting_items: AccountingItemsResource) -> None:
        self._accounting_items = accounting_items

        self.update = to_streamed_response_wrapper(
            accounting_items.update,
        )
        self.list = to_streamed_response_wrapper(
            accounting_items.list,
        )


class AsyncAccountingItemsResourceWithStreamingResponse:
    def __init__(self, accounting_items: AsyncAccountingItemsResource) -> None:
        self._accounting_items = accounting_items

        self.update = async_to_streamed_response_wrapper(
            accounting_items.update,
        )
        self.list = async_to_streamed_response_wrapper(
            accounting_items.list,
        )
