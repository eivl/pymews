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
    service_order_note_add_params,
    service_order_note_list_params,
    service_order_note_delete_params,
    service_order_note_update_params,
)
from .....types.api.connector.v1.service_order_note_add_response import ServiceOrderNoteAddResponse
from .....types.api.connector.v1.service_order_note_list_response import ServiceOrderNoteListResponse
from .....types.api.connector.v1.service_order_note_update_response import ServiceOrderNoteUpdateResponse

__all__ = ["ServiceOrderNotesResource", "AsyncServiceOrderNotesResource"]


class ServiceOrderNotesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ServiceOrderNotesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return ServiceOrderNotesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ServiceOrderNotesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return ServiceOrderNotesResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        service_order_note_updates: Iterable[service_order_note_update_params.ServiceOrderNoteUpdate],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ServiceOrderNoteUpdateResponse:
        """
        Updates one or more given service order notes with new text.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          service_order_note_updates: Notes to be updated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/serviceOrderNotes/update",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "service_order_note_updates": service_order_note_updates,
                },
                service_order_note_update_params.ServiceOrderNoteUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServiceOrderNoteUpdateResponse,
        )

    def list(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: service_order_note_list_params.Limitation,
        service_order_ids: List[str],
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        service_order_note_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        types: Optional[List[Literal["General", "ChannelManager", "SpecialRequest"]]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[service_order_note_list_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ServiceOrderNoteListResponse:
        """Returns all notes associated with the given service orders.

        Service orders can
        be reservations or product orders. Note this operation uses
        [Pagination](../guidelines/pagination.md) and supports
        [Portfolio Access Tokens](../guidelines/multi-property.md).

        > **Service order:** This is the general name for an order made against a
        > service, which includes both 'stay' service orders, called
        > [Reservations](reservations.md#reservation), and 'product' service orders,
        > which we simply call [Orders](orders.md). Operations such as
        > [Get all service order notes](#get-all-service-order-notes) will accept
        > Reservation IDs or Order IDs as service order identifiers.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          service_order_ids: Unique identifiers of `Service order`. Reservation IDs or Order IDs can be used
              as service order identifiers.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          service_order_note_ids: Unique identifiers of `Service order note`. Use this property if you want to
              fetch specific service order notes.

          types: Type of the service order note. Defaults to `["General", "ChannelManage"]`.

          updated_utc: Timestamp in UTC timezone ISO 8601 format when the service order note was
              updated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/serviceOrderNotes/getAll",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "service_order_ids": service_order_ids,
                    "enterprise_ids": enterprise_ids,
                    "service_order_note_ids": service_order_note_ids,
                    "types": types,
                    "updated_utc": updated_utc,
                },
                service_order_note_list_params.ServiceOrderNoteListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServiceOrderNoteListResponse,
        )

    def delete(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        service_order_note_ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Deletes service order notes.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          service_order_note_ids: Unique identifiers of the service order notes to be deleted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/serviceOrderNotes/delete",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "service_order_note_ids": service_order_note_ids,
                },
                service_order_note_delete_params.ServiceOrderNoteDeleteParams,
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
        service_order_notes: Iterable[service_order_note_add_params.ServiceOrderNote],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ServiceOrderNoteAddResponse:
        """Adds one or more notes with a provided text to a specific service order.

        Service
        orders can be reservations or product orders.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          service_order_notes: Notes to be added.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/serviceOrderNotes/add",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "service_order_notes": service_order_notes,
                },
                service_order_note_add_params.ServiceOrderNoteAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServiceOrderNoteAddResponse,
        )


class AsyncServiceOrderNotesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncServiceOrderNotesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return AsyncServiceOrderNotesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncServiceOrderNotesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return AsyncServiceOrderNotesResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        service_order_note_updates: Iterable[service_order_note_update_params.ServiceOrderNoteUpdate],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ServiceOrderNoteUpdateResponse:
        """
        Updates one or more given service order notes with new text.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          service_order_note_updates: Notes to be updated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/serviceOrderNotes/update",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "service_order_note_updates": service_order_note_updates,
                },
                service_order_note_update_params.ServiceOrderNoteUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServiceOrderNoteUpdateResponse,
        )

    async def list(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: service_order_note_list_params.Limitation,
        service_order_ids: List[str],
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        service_order_note_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        types: Optional[List[Literal["General", "ChannelManager", "SpecialRequest"]]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[service_order_note_list_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ServiceOrderNoteListResponse:
        """Returns all notes associated with the given service orders.

        Service orders can
        be reservations or product orders. Note this operation uses
        [Pagination](../guidelines/pagination.md) and supports
        [Portfolio Access Tokens](../guidelines/multi-property.md).

        > **Service order:** This is the general name for an order made against a
        > service, which includes both 'stay' service orders, called
        > [Reservations](reservations.md#reservation), and 'product' service orders,
        > which we simply call [Orders](orders.md). Operations such as
        > [Get all service order notes](#get-all-service-order-notes) will accept
        > Reservation IDs or Order IDs as service order identifiers.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          service_order_ids: Unique identifiers of `Service order`. Reservation IDs or Order IDs can be used
              as service order identifiers.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          service_order_note_ids: Unique identifiers of `Service order note`. Use this property if you want to
              fetch specific service order notes.

          types: Type of the service order note. Defaults to `["General", "ChannelManage"]`.

          updated_utc: Timestamp in UTC timezone ISO 8601 format when the service order note was
              updated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/serviceOrderNotes/getAll",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "service_order_ids": service_order_ids,
                    "enterprise_ids": enterprise_ids,
                    "service_order_note_ids": service_order_note_ids,
                    "types": types,
                    "updated_utc": updated_utc,
                },
                service_order_note_list_params.ServiceOrderNoteListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServiceOrderNoteListResponse,
        )

    async def delete(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        service_order_note_ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Deletes service order notes.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          service_order_note_ids: Unique identifiers of the service order notes to be deleted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/serviceOrderNotes/delete",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "service_order_note_ids": service_order_note_ids,
                },
                service_order_note_delete_params.ServiceOrderNoteDeleteParams,
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
        service_order_notes: Iterable[service_order_note_add_params.ServiceOrderNote],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ServiceOrderNoteAddResponse:
        """Adds one or more notes with a provided text to a specific service order.

        Service
        orders can be reservations or product orders.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          service_order_notes: Notes to be added.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/serviceOrderNotes/add",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "service_order_notes": service_order_notes,
                },
                service_order_note_add_params.ServiceOrderNoteAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServiceOrderNoteAddResponse,
        )


class ServiceOrderNotesResourceWithRawResponse:
    def __init__(self, service_order_notes: ServiceOrderNotesResource) -> None:
        self._service_order_notes = service_order_notes

        self.update = to_raw_response_wrapper(
            service_order_notes.update,
        )
        self.list = to_raw_response_wrapper(
            service_order_notes.list,
        )
        self.delete = to_raw_response_wrapper(
            service_order_notes.delete,
        )
        self.add = to_raw_response_wrapper(
            service_order_notes.add,
        )


class AsyncServiceOrderNotesResourceWithRawResponse:
    def __init__(self, service_order_notes: AsyncServiceOrderNotesResource) -> None:
        self._service_order_notes = service_order_notes

        self.update = async_to_raw_response_wrapper(
            service_order_notes.update,
        )
        self.list = async_to_raw_response_wrapper(
            service_order_notes.list,
        )
        self.delete = async_to_raw_response_wrapper(
            service_order_notes.delete,
        )
        self.add = async_to_raw_response_wrapper(
            service_order_notes.add,
        )


class ServiceOrderNotesResourceWithStreamingResponse:
    def __init__(self, service_order_notes: ServiceOrderNotesResource) -> None:
        self._service_order_notes = service_order_notes

        self.update = to_streamed_response_wrapper(
            service_order_notes.update,
        )
        self.list = to_streamed_response_wrapper(
            service_order_notes.list,
        )
        self.delete = to_streamed_response_wrapper(
            service_order_notes.delete,
        )
        self.add = to_streamed_response_wrapper(
            service_order_notes.add,
        )


class AsyncServiceOrderNotesResourceWithStreamingResponse:
    def __init__(self, service_order_notes: AsyncServiceOrderNotesResource) -> None:
        self._service_order_notes = service_order_notes

        self.update = async_to_streamed_response_wrapper(
            service_order_notes.update,
        )
        self.list = async_to_streamed_response_wrapper(
            service_order_notes.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            service_order_notes.delete,
        )
        self.add = async_to_streamed_response_wrapper(
            service_order_notes.add,
        )
