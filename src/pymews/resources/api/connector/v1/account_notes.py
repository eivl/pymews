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
    account_note_add_params,
    account_note_list_params,
    account_note_delete_params,
    account_note_update_params,
)
from .....types.api.connector.v1.account_note_add_response import AccountNoteAddResponse
from .....types.api.connector.v1.account_note_list_response import AccountNoteListResponse
from .....types.api.connector.v1.account_note_update_response import AccountNoteUpdateResponse

__all__ = ["AccountNotesResource", "AsyncAccountNotesResource"]


class AccountNotesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccountNotesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return AccountNotesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountNotesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return AccountNotesResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        access_token: str,
        account_note_updates: Iterable[account_note_update_params.AccountNoteUpdate],
        client: str,
        client_token: str,
        chain_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountNoteUpdateResponse:
        """
        Updates information about the specified account notes.

        Args:
          access_token: Access token of the client application.

          account_note_updates: Account notes to be updated.

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
            "/api/connector/v1/accountNotes/update",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "account_note_updates": account_note_updates,
                    "client": client,
                    "client_token": client_token,
                    "chain_id": chain_id,
                },
                account_note_update_params.AccountNoteUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountNoteUpdateResponse,
        )

    def list(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: account_note_list_params.Limitation,
        account_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        account_note_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        activity_states: Optional[List[Literal["Deleted", "Active"]]] | NotGiven = NOT_GIVEN,
        chain_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[account_note_list_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountNoteListResponse:
        """
        Returns all account notes of an account, optionally filtered by activity state,
        account identifiers, specific account note identifiers or other filter
        parameters. Note this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          account_ids: Unique identifiers of the accounts
              ([Customer](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer)
              or
              [Company](https://mews-systems.gitbook.io/connector-api/operations/companies/#company)).

          account_note_ids: Unique identifiers of
              [Account note](https://mews-systems.gitbook.io/connector-api/operations/#account-note).

          activity_states: Whether to return only active, only deleted or both records.

          chain_ids: Unique identifiers of `Chain`. If not specified, the operation returns data for
              all chains within scope of the Access Token.

          updated_utc: Interval of Account note's last update date and time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/accountNotes/getAll",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "account_ids": account_ids,
                    "account_note_ids": account_note_ids,
                    "activity_states": activity_states,
                    "chain_ids": chain_ids,
                    "updated_utc": updated_utc,
                },
                account_note_list_params.AccountNoteListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountNoteListResponse,
        )

    def delete(
        self,
        *,
        access_token: str,
        account_note_ids: List[str],
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
        """
        Deletes specified account notes.

        Args:
          access_token: Access token of the client application.

          account_note_ids: Unique identifiers of the account notes to be deleted.

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
            "/api/connector/v1/accountNotes/delete",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "account_note_ids": account_note_ids,
                    "client": client,
                    "client_token": client_token,
                    "chain_id": chain_id,
                },
                account_note_delete_params.AccountNoteDeleteParams,
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
        account_notes: Iterable[account_note_add_params.AccountNote],
        client: str,
        client_token: str,
        chain_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountNoteAddResponse:
        """Adds account notes to an account of the enterprise chain.

        Note this operation
        supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          account_notes: Account notes to be added.

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
            "/api/connector/v1/accountNotes/add",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "account_notes": account_notes,
                    "client": client,
                    "client_token": client_token,
                    "chain_id": chain_id,
                },
                account_note_add_params.AccountNoteAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountNoteAddResponse,
        )


class AsyncAccountNotesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccountNotesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return AsyncAccountNotesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountNotesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return AsyncAccountNotesResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        access_token: str,
        account_note_updates: Iterable[account_note_update_params.AccountNoteUpdate],
        client: str,
        client_token: str,
        chain_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountNoteUpdateResponse:
        """
        Updates information about the specified account notes.

        Args:
          access_token: Access token of the client application.

          account_note_updates: Account notes to be updated.

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
            "/api/connector/v1/accountNotes/update",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "account_note_updates": account_note_updates,
                    "client": client,
                    "client_token": client_token,
                    "chain_id": chain_id,
                },
                account_note_update_params.AccountNoteUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountNoteUpdateResponse,
        )

    async def list(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: account_note_list_params.Limitation,
        account_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        account_note_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        activity_states: Optional[List[Literal["Deleted", "Active"]]] | NotGiven = NOT_GIVEN,
        chain_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[account_note_list_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountNoteListResponse:
        """
        Returns all account notes of an account, optionally filtered by activity state,
        account identifiers, specific account note identifiers or other filter
        parameters. Note this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          account_ids: Unique identifiers of the accounts
              ([Customer](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer)
              or
              [Company](https://mews-systems.gitbook.io/connector-api/operations/companies/#company)).

          account_note_ids: Unique identifiers of
              [Account note](https://mews-systems.gitbook.io/connector-api/operations/#account-note).

          activity_states: Whether to return only active, only deleted or both records.

          chain_ids: Unique identifiers of `Chain`. If not specified, the operation returns data for
              all chains within scope of the Access Token.

          updated_utc: Interval of Account note's last update date and time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/accountNotes/getAll",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "account_ids": account_ids,
                    "account_note_ids": account_note_ids,
                    "activity_states": activity_states,
                    "chain_ids": chain_ids,
                    "updated_utc": updated_utc,
                },
                account_note_list_params.AccountNoteListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountNoteListResponse,
        )

    async def delete(
        self,
        *,
        access_token: str,
        account_note_ids: List[str],
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
        """
        Deletes specified account notes.

        Args:
          access_token: Access token of the client application.

          account_note_ids: Unique identifiers of the account notes to be deleted.

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
            "/api/connector/v1/accountNotes/delete",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "account_note_ids": account_note_ids,
                    "client": client,
                    "client_token": client_token,
                    "chain_id": chain_id,
                },
                account_note_delete_params.AccountNoteDeleteParams,
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
        account_notes: Iterable[account_note_add_params.AccountNote],
        client: str,
        client_token: str,
        chain_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountNoteAddResponse:
        """Adds account notes to an account of the enterprise chain.

        Note this operation
        supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          account_notes: Account notes to be added.

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
            "/api/connector/v1/accountNotes/add",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "account_notes": account_notes,
                    "client": client,
                    "client_token": client_token,
                    "chain_id": chain_id,
                },
                account_note_add_params.AccountNoteAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountNoteAddResponse,
        )


class AccountNotesResourceWithRawResponse:
    def __init__(self, account_notes: AccountNotesResource) -> None:
        self._account_notes = account_notes

        self.update = to_raw_response_wrapper(
            account_notes.update,
        )
        self.list = to_raw_response_wrapper(
            account_notes.list,
        )
        self.delete = to_raw_response_wrapper(
            account_notes.delete,
        )
        self.add = to_raw_response_wrapper(
            account_notes.add,
        )


class AsyncAccountNotesResourceWithRawResponse:
    def __init__(self, account_notes: AsyncAccountNotesResource) -> None:
        self._account_notes = account_notes

        self.update = async_to_raw_response_wrapper(
            account_notes.update,
        )
        self.list = async_to_raw_response_wrapper(
            account_notes.list,
        )
        self.delete = async_to_raw_response_wrapper(
            account_notes.delete,
        )
        self.add = async_to_raw_response_wrapper(
            account_notes.add,
        )


class AccountNotesResourceWithStreamingResponse:
    def __init__(self, account_notes: AccountNotesResource) -> None:
        self._account_notes = account_notes

        self.update = to_streamed_response_wrapper(
            account_notes.update,
        )
        self.list = to_streamed_response_wrapper(
            account_notes.list,
        )
        self.delete = to_streamed_response_wrapper(
            account_notes.delete,
        )
        self.add = to_streamed_response_wrapper(
            account_notes.add,
        )


class AsyncAccountNotesResourceWithStreamingResponse:
    def __init__(self, account_notes: AsyncAccountNotesResource) -> None:
        self._account_notes = account_notes

        self.update = async_to_streamed_response_wrapper(
            account_notes.update,
        )
        self.list = async_to_streamed_response_wrapper(
            account_notes.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            account_notes.delete,
        )
        self.add = async_to_streamed_response_wrapper(
            account_notes.add,
        )
