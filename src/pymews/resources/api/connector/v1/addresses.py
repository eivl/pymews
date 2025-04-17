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
    address_add_params,
    address_list_params,
    address_delete_params,
    address_update_params,
)
from .....types.api.connector.v1.address_result import AddressResult
from .....types.api.connector.v1.address_list_response import AddressListResponse

__all__ = ["AddressesResource", "AsyncAddressesResource"]


class AddressesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AddressesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return AddressesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AddressesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return AddressesResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        access_token: str,
        address_updates: Iterable[address_update_params.AddressUpdate],
        client: str,
        client_token: str,
        chain_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AddressResult:
        """
        Updates one or more existing addresses in the system, assigned to specified
        accounts. Note this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          address_updates: Collection of addresses to be updated.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          chain_id: Unique identifier of the chain. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/addresses/update",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "address_updates": address_updates,
                    "client": client,
                    "client_token": client_token,
                    "chain_id": chain_id,
                },
                address_update_params.AddressUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddressResult,
        )

    def list(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: address_list_params.Limitation,
        account_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        activity_states: Optional[List[Literal["Deleted", "Active"]]] | NotGiven = NOT_GIVEN,
        address_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        chain_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[address_list_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AddressListResponse:
        """
        Returns all addresses associated with the specified accounts within the
        enterprise. Note this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          account_ids: Unique identifiers of
              [Companies](https://mews-systems.gitbook.io/connector-api/operations/companies/#company)
              or
              [Customers](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer)
              within the enterprise. Required if no other filter is provided.

          activity_states: Whether to return only active, only deleted or both records.

          address_ids: Unique identifiers of
              [Addresses](https://mews-systems.gitbook.io/connector-api/operations/#account-address)
              within the enterprise. Use this property if you want to fetch specific
              addresses. Required if no other filter is provided.

          chain_ids: Unique identifiers of `Chain`. If not specified, the operation returns data for
              all chains within scope of the Access Token.

          updated_utc: Interval of Address last update date and time. Required if no other filter is
              provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/addresses/getAll",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "account_ids": account_ids,
                    "activity_states": activity_states,
                    "address_ids": address_ids,
                    "chain_ids": chain_ids,
                    "updated_utc": updated_utc,
                },
                address_list_params.AddressListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddressListResponse,
        )

    def delete(
        self,
        *,
        access_token: str,
        address_ids: List[str],
        client: str,
        client_token: str,
        chain_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Deletes one or more addresses in the system.

        Note this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          address_ids: Unique identifiers of
              [Addresses](https://mews-systems.gitbook.io/connector-api/operations/#account-address)
              within the enterprise to be deleted.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          chain_id: Unique identifier of the chain. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/addresses/delete",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "address_ids": address_ids,
                    "client": client,
                    "client_token": client_token,
                    "chain_id": chain_id,
                },
                address_delete_params.AddressDeleteParams,
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
        addresses: Iterable[address_add_params.Address],
        client: str,
        client_token: str,
        chain_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AddressResult:
        """
        Adds one or more new addresses to the system and assigns them to specified
        accounts. Note this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          addresses: Collection of addresses to be created.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          chain_id: Unique identifier of the chain. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/addresses/add",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "addresses": addresses,
                    "client": client,
                    "client_token": client_token,
                    "chain_id": chain_id,
                },
                address_add_params.AddressAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddressResult,
        )


class AsyncAddressesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAddressesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return AsyncAddressesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAddressesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return AsyncAddressesResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        access_token: str,
        address_updates: Iterable[address_update_params.AddressUpdate],
        client: str,
        client_token: str,
        chain_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AddressResult:
        """
        Updates one or more existing addresses in the system, assigned to specified
        accounts. Note this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          address_updates: Collection of addresses to be updated.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          chain_id: Unique identifier of the chain. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/addresses/update",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "address_updates": address_updates,
                    "client": client,
                    "client_token": client_token,
                    "chain_id": chain_id,
                },
                address_update_params.AddressUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddressResult,
        )

    async def list(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: address_list_params.Limitation,
        account_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        activity_states: Optional[List[Literal["Deleted", "Active"]]] | NotGiven = NOT_GIVEN,
        address_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        chain_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[address_list_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AddressListResponse:
        """
        Returns all addresses associated with the specified accounts within the
        enterprise. Note this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          account_ids: Unique identifiers of
              [Companies](https://mews-systems.gitbook.io/connector-api/operations/companies/#company)
              or
              [Customers](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer)
              within the enterprise. Required if no other filter is provided.

          activity_states: Whether to return only active, only deleted or both records.

          address_ids: Unique identifiers of
              [Addresses](https://mews-systems.gitbook.io/connector-api/operations/#account-address)
              within the enterprise. Use this property if you want to fetch specific
              addresses. Required if no other filter is provided.

          chain_ids: Unique identifiers of `Chain`. If not specified, the operation returns data for
              all chains within scope of the Access Token.

          updated_utc: Interval of Address last update date and time. Required if no other filter is
              provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/addresses/getAll",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "account_ids": account_ids,
                    "activity_states": activity_states,
                    "address_ids": address_ids,
                    "chain_ids": chain_ids,
                    "updated_utc": updated_utc,
                },
                address_list_params.AddressListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddressListResponse,
        )

    async def delete(
        self,
        *,
        access_token: str,
        address_ids: List[str],
        client: str,
        client_token: str,
        chain_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Deletes one or more addresses in the system.

        Note this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          address_ids: Unique identifiers of
              [Addresses](https://mews-systems.gitbook.io/connector-api/operations/#account-address)
              within the enterprise to be deleted.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          chain_id: Unique identifier of the chain. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/addresses/delete",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "address_ids": address_ids,
                    "client": client,
                    "client_token": client_token,
                    "chain_id": chain_id,
                },
                address_delete_params.AddressDeleteParams,
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
        addresses: Iterable[address_add_params.Address],
        client: str,
        client_token: str,
        chain_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AddressResult:
        """
        Adds one or more new addresses to the system and assigns them to specified
        accounts. Note this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          addresses: Collection of addresses to be created.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          chain_id: Unique identifier of the chain. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/addresses/add",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "addresses": addresses,
                    "client": client,
                    "client_token": client_token,
                    "chain_id": chain_id,
                },
                address_add_params.AddressAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddressResult,
        )


class AddressesResourceWithRawResponse:
    def __init__(self, addresses: AddressesResource) -> None:
        self._addresses = addresses

        self.update = to_raw_response_wrapper(
            addresses.update,
        )
        self.list = to_raw_response_wrapper(
            addresses.list,
        )
        self.delete = to_raw_response_wrapper(
            addresses.delete,
        )
        self.add = to_raw_response_wrapper(
            addresses.add,
        )


class AsyncAddressesResourceWithRawResponse:
    def __init__(self, addresses: AsyncAddressesResource) -> None:
        self._addresses = addresses

        self.update = async_to_raw_response_wrapper(
            addresses.update,
        )
        self.list = async_to_raw_response_wrapper(
            addresses.list,
        )
        self.delete = async_to_raw_response_wrapper(
            addresses.delete,
        )
        self.add = async_to_raw_response_wrapper(
            addresses.add,
        )


class AddressesResourceWithStreamingResponse:
    def __init__(self, addresses: AddressesResource) -> None:
        self._addresses = addresses

        self.update = to_streamed_response_wrapper(
            addresses.update,
        )
        self.list = to_streamed_response_wrapper(
            addresses.list,
        )
        self.delete = to_streamed_response_wrapper(
            addresses.delete,
        )
        self.add = to_streamed_response_wrapper(
            addresses.add,
        )


class AsyncAddressesResourceWithStreamingResponse:
    def __init__(self, addresses: AsyncAddressesResource) -> None:
        self._addresses = addresses

        self.update = async_to_streamed_response_wrapper(
            addresses.update,
        )
        self.list = async_to_streamed_response_wrapper(
            addresses.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            addresses.delete,
        )
        self.add = async_to_streamed_response_wrapper(
            addresses.add,
        )
