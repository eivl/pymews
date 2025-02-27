# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

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
from .....types.api.connector.v1 import account_merge_params, account_update_params, account_add_file_params
from .....types.api.connector.v1.account_update_response import AccountUpdateResponse
from .....types.api.connector.v1.account_add_file_response import AccountAddFileResponse

__all__ = ["AccountsResource", "AsyncAccountsResource"]


class AccountsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return AccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return AccountsResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        access_token: str,
        account_updates: Iterable[account_update_params.AccountUpdate],
        client: str,
        client_token: str,
        chain_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountUpdateResponse:
        """Updates one or more existing accounts in the system.

        Note this operation
        supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          account_updates: Accounts to be updated.

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
            "/api/connector/v1/accounts/update",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "account_updates": account_updates,
                    "client": client,
                    "client_token": client_token,
                    "chain_id": chain_id,
                },
                account_update_params.AccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountUpdateResponse,
        )

    def add_file(
        self,
        *,
        access_token: str,
        account_id: str,
        client: str,
        client_token: str,
        data: str,
        name: str,
        type: str,
        chain_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountAddFileResponse:
        """
        Attaches the specified file to the account.

        Allowed MIME types: `application/pdf`, `image/bmp`, `image/gif`, `image/jpeg`,
        `image/png`, `image/tiff`.

        Note this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/guidelines/multi-property).

        Args:
          access_token: Access token of the client application.

          account_id: Unique identifier of the account to which the file will be uploaded to.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          data: Uploaded file data serialized in base64 format.

          name: Uploaded file name.

          type: Content type of the uploaded file following defined by its MIME type.

          chain_id: Unique identifier of the chain. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/accounts/addFile",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "account_id": account_id,
                    "client": client,
                    "client_token": client_token,
                    "data": data,
                    "name": name,
                    "type": type,
                    "chain_id": chain_id,
                },
                account_add_file_params.AccountAddFileParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountAddFileResponse,
        )

    def merge(
        self,
        *,
        access_token: str,
        account_merge_parameters: Iterable[account_merge_params.AccountMergeParameter],
        client: str,
        client_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Merges two or more accounts of the same account type together.

        The given source
        accounts will be merged into the given target account and the merged account
        will keep the target account ID.

        Args:
          access_token: Access token of the client application.

          account_merge_parameters: Accounts to be merged.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/accounts/merge",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "account_merge_parameters": account_merge_parameters,
                    "client": client,
                    "client_token": client_token,
                },
                account_merge_params.AccountMergeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncAccountsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return AsyncAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return AsyncAccountsResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        access_token: str,
        account_updates: Iterable[account_update_params.AccountUpdate],
        client: str,
        client_token: str,
        chain_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountUpdateResponse:
        """Updates one or more existing accounts in the system.

        Note this operation
        supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          account_updates: Accounts to be updated.

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
            "/api/connector/v1/accounts/update",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "account_updates": account_updates,
                    "client": client,
                    "client_token": client_token,
                    "chain_id": chain_id,
                },
                account_update_params.AccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountUpdateResponse,
        )

    async def add_file(
        self,
        *,
        access_token: str,
        account_id: str,
        client: str,
        client_token: str,
        data: str,
        name: str,
        type: str,
        chain_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountAddFileResponse:
        """
        Attaches the specified file to the account.

        Allowed MIME types: `application/pdf`, `image/bmp`, `image/gif`, `image/jpeg`,
        `image/png`, `image/tiff`.

        Note this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/guidelines/multi-property).

        Args:
          access_token: Access token of the client application.

          account_id: Unique identifier of the account to which the file will be uploaded to.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          data: Uploaded file data serialized in base64 format.

          name: Uploaded file name.

          type: Content type of the uploaded file following defined by its MIME type.

          chain_id: Unique identifier of the chain. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/accounts/addFile",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "account_id": account_id,
                    "client": client,
                    "client_token": client_token,
                    "data": data,
                    "name": name,
                    "type": type,
                    "chain_id": chain_id,
                },
                account_add_file_params.AccountAddFileParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountAddFileResponse,
        )

    async def merge(
        self,
        *,
        access_token: str,
        account_merge_parameters: Iterable[account_merge_params.AccountMergeParameter],
        client: str,
        client_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Merges two or more accounts of the same account type together.

        The given source
        accounts will be merged into the given target account and the merged account
        will keep the target account ID.

        Args:
          access_token: Access token of the client application.

          account_merge_parameters: Accounts to be merged.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/accounts/merge",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "account_merge_parameters": account_merge_parameters,
                    "client": client,
                    "client_token": client_token,
                },
                account_merge_params.AccountMergeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AccountsResourceWithRawResponse:
    def __init__(self, accounts: AccountsResource) -> None:
        self._accounts = accounts

        self.update = to_raw_response_wrapper(
            accounts.update,
        )
        self.add_file = to_raw_response_wrapper(
            accounts.add_file,
        )
        self.merge = to_raw_response_wrapper(
            accounts.merge,
        )


class AsyncAccountsResourceWithRawResponse:
    def __init__(self, accounts: AsyncAccountsResource) -> None:
        self._accounts = accounts

        self.update = async_to_raw_response_wrapper(
            accounts.update,
        )
        self.add_file = async_to_raw_response_wrapper(
            accounts.add_file,
        )
        self.merge = async_to_raw_response_wrapper(
            accounts.merge,
        )


class AccountsResourceWithStreamingResponse:
    def __init__(self, accounts: AccountsResource) -> None:
        self._accounts = accounts

        self.update = to_streamed_response_wrapper(
            accounts.update,
        )
        self.add_file = to_streamed_response_wrapper(
            accounts.add_file,
        )
        self.merge = to_streamed_response_wrapper(
            accounts.merge,
        )


class AsyncAccountsResourceWithStreamingResponse:
    def __init__(self, accounts: AsyncAccountsResource) -> None:
        self._accounts = accounts

        self.update = async_to_streamed_response_wrapper(
            accounts.update,
        )
        self.add_file = async_to_streamed_response_wrapper(
            accounts.add_file,
        )
        self.merge = async_to_streamed_response_wrapper(
            accounts.merge,
        )
