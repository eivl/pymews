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
from .....types.api.connector.v1 import (
    command_update_params,
    command_add_printer_params,
    command_list_active_params,
    command_list_by_ids_params,
    command_add_key_cutter_params,
    command_add_payment_terminal_params,
)
from .....types.api.connector.v1.device_command_result import DeviceCommandResult
from .....types.api.connector.v1.device_command_add_result import DeviceCommandAddResult

__all__ = ["CommandsResource", "AsyncCommandsResource"]


class CommandsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CommandsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return CommandsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CommandsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return CommandsResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        command_id: str,
        state: Literal["Pending", "Received", "Processing", "Processed", "Cancelled", "Error"],
        external_request_identifier: Optional[command_update_params.ExternalRequestIdentifier] | NotGiven = NOT_GIVEN,
        notes: Optional[str] | NotGiven = NOT_GIVEN,
        progress: Optional[float] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Updates state of a command.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          command_id: Identifier of the
              [Command](https://mews-systems.gitbook.io/connector-api/operations/#command) to
              be updated.

          notes: Notes about command execution. Only used if the State is Processed, Cancelled or
              Error, otherwise ignored.

          progress: Progress of the command processing. Only used if the State is Processing,
              otherwise ignored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/commands/update",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "command_id": command_id,
                    "state": state,
                    "external_request_identifier": external_request_identifier,
                    "notes": notes,
                    "progress": progress,
                },
                command_update_params.CommandUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def add_key_cutter(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        key_count: int,
        key_cutter_id: str,
        reservation_id: str,
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeviceCommandAddResult:
        """
        Adds a new key cutter command representing cutting of a key for the specified
        reservation. Note this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          key_count: Count of keys to encode.

          key_cutter_id: Unique identifier of the KeyCutter
              [Device](https://mews-systems.gitbook.io/connector-api/operations/devices/#device)
              where to encode the key.

          reservation_id: Unique identifier of the reservation to encode the key for.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/commands/addKeyCutter",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "key_count": key_count,
                    "key_cutter_id": key_cutter_id,
                    "reservation_id": reservation_id,
                    "enterprise_id": enterprise_id,
                },
                command_add_key_cutter_params.CommandAddKeyCutterParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeviceCommandAddResult,
        )

    def add_payment_terminal(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        customer_id: str,
        terminal_id: str,
        type: Literal["Payment", "Preauthorization"],
        amount: Optional[command_add_payment_terminal_params.Amount] | NotGiven = NOT_GIVEN,
        bill_id: Optional[str] | NotGiven = NOT_GIVEN,
        payment_request_id: Optional[str] | NotGiven = NOT_GIVEN,
        reservation_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeviceCommandAddResult:
        """
        > ### Restricted!
        >
        > This operation is part of a custom workflow for Mews partners such as POS
        > systems to access Mews Payment Terminals. See
        > [Mews Payment Terminals](https://mews-systems.gitbook.io/connector-api/use-cases/mews-terminals/).
        > Adds a new Mews Payment Terminal command for taking a customer payment. The
        > operation instructs a specified terminal device to take a payment from a
        > specified customer for a specified amount.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          customer_id: Unique identifier of the
              [Customer](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer).

          terminal_id: Unique identifier of the payment terminal.

          amount: Total price of the reservation.

          bill_id: Unique identifier of the
              [Bill](https://mews-systems.gitbook.io/connector-api/operations/bills/#bill).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/commands/addPaymentTerminal",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "customer_id": customer_id,
                    "terminal_id": terminal_id,
                    "type": type,
                    "amount": amount,
                    "bill_id": bill_id,
                    "payment_request_id": payment_request_id,
                    "reservation_id": reservation_id,
                },
                command_add_payment_terminal_params.CommandAddPaymentTerminalParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeviceCommandAddResult,
        )

    def add_printer(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        copy_count: int,
        data: str,
        printer_id: str,
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeviceCommandAddResult:
        """
        Adds a new printer command representing printing of the specified document on a
        printer. Note this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          copy_count: Count of copies to be printed.

          data: Base64 encoded data of PDF document to print.

          printer_id: Uniqque identifier of the Printer
              [Device](https://mews-systems.gitbook.io/connector-api/operations/devices/#device)
              where to print the document.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/commands/addPrinter",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "copy_count": copy_count,
                    "data": data,
                    "printer_id": printer_id,
                    "enterprise_id": enterprise_id,
                },
                command_add_printer_params.CommandAddPrinterParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeviceCommandAddResult,
        )

    def list_active(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeviceCommandResult:
        """
        Returns all commands the are still active from the client application point of
        view. That means commands that are in either `Pending` or `Received` state.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/commands/getAllActive",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                },
                command_list_active_params.CommandListActiveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeviceCommandResult,
        )

    def list_by_ids(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        command_ids: List[str],
        limitation: Optional[command_list_by_ids_params.Limitation] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeviceCommandResult:
        """
        Returns all commands by their identifiers.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          command_ids: Unique identifiers of
              [Commands](https://mews-systems.gitbook.io/connector-api/operations/#command) to
              be returned.

          limitation: Limitation on the quantity of data returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/commands/getAllByIds",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "command_ids": command_ids,
                    "limitation": limitation,
                },
                command_list_by_ids_params.CommandListByIDsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeviceCommandResult,
        )


class AsyncCommandsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCommandsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return AsyncCommandsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCommandsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return AsyncCommandsResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        command_id: str,
        state: Literal["Pending", "Received", "Processing", "Processed", "Cancelled", "Error"],
        external_request_identifier: Optional[command_update_params.ExternalRequestIdentifier] | NotGiven = NOT_GIVEN,
        notes: Optional[str] | NotGiven = NOT_GIVEN,
        progress: Optional[float] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Updates state of a command.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          command_id: Identifier of the
              [Command](https://mews-systems.gitbook.io/connector-api/operations/#command) to
              be updated.

          notes: Notes about command execution. Only used if the State is Processed, Cancelled or
              Error, otherwise ignored.

          progress: Progress of the command processing. Only used if the State is Processing,
              otherwise ignored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/commands/update",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "command_id": command_id,
                    "state": state,
                    "external_request_identifier": external_request_identifier,
                    "notes": notes,
                    "progress": progress,
                },
                command_update_params.CommandUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def add_key_cutter(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        key_count: int,
        key_cutter_id: str,
        reservation_id: str,
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeviceCommandAddResult:
        """
        Adds a new key cutter command representing cutting of a key for the specified
        reservation. Note this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          key_count: Count of keys to encode.

          key_cutter_id: Unique identifier of the KeyCutter
              [Device](https://mews-systems.gitbook.io/connector-api/operations/devices/#device)
              where to encode the key.

          reservation_id: Unique identifier of the reservation to encode the key for.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/commands/addKeyCutter",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "key_count": key_count,
                    "key_cutter_id": key_cutter_id,
                    "reservation_id": reservation_id,
                    "enterprise_id": enterprise_id,
                },
                command_add_key_cutter_params.CommandAddKeyCutterParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeviceCommandAddResult,
        )

    async def add_payment_terminal(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        customer_id: str,
        terminal_id: str,
        type: Literal["Payment", "Preauthorization"],
        amount: Optional[command_add_payment_terminal_params.Amount] | NotGiven = NOT_GIVEN,
        bill_id: Optional[str] | NotGiven = NOT_GIVEN,
        payment_request_id: Optional[str] | NotGiven = NOT_GIVEN,
        reservation_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeviceCommandAddResult:
        """
        > ### Restricted!
        >
        > This operation is part of a custom workflow for Mews partners such as POS
        > systems to access Mews Payment Terminals. See
        > [Mews Payment Terminals](https://mews-systems.gitbook.io/connector-api/use-cases/mews-terminals/).
        > Adds a new Mews Payment Terminal command for taking a customer payment. The
        > operation instructs a specified terminal device to take a payment from a
        > specified customer for a specified amount.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          customer_id: Unique identifier of the
              [Customer](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer).

          terminal_id: Unique identifier of the payment terminal.

          amount: Total price of the reservation.

          bill_id: Unique identifier of the
              [Bill](https://mews-systems.gitbook.io/connector-api/operations/bills/#bill).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/commands/addPaymentTerminal",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "customer_id": customer_id,
                    "terminal_id": terminal_id,
                    "type": type,
                    "amount": amount,
                    "bill_id": bill_id,
                    "payment_request_id": payment_request_id,
                    "reservation_id": reservation_id,
                },
                command_add_payment_terminal_params.CommandAddPaymentTerminalParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeviceCommandAddResult,
        )

    async def add_printer(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        copy_count: int,
        data: str,
        printer_id: str,
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeviceCommandAddResult:
        """
        Adds a new printer command representing printing of the specified document on a
        printer. Note this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          copy_count: Count of copies to be printed.

          data: Base64 encoded data of PDF document to print.

          printer_id: Uniqque identifier of the Printer
              [Device](https://mews-systems.gitbook.io/connector-api/operations/devices/#device)
              where to print the document.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/commands/addPrinter",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "copy_count": copy_count,
                    "data": data,
                    "printer_id": printer_id,
                    "enterprise_id": enterprise_id,
                },
                command_add_printer_params.CommandAddPrinterParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeviceCommandAddResult,
        )

    async def list_active(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeviceCommandResult:
        """
        Returns all commands the are still active from the client application point of
        view. That means commands that are in either `Pending` or `Received` state.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/commands/getAllActive",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                },
                command_list_active_params.CommandListActiveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeviceCommandResult,
        )

    async def list_by_ids(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        command_ids: List[str],
        limitation: Optional[command_list_by_ids_params.Limitation] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeviceCommandResult:
        """
        Returns all commands by their identifiers.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          command_ids: Unique identifiers of
              [Commands](https://mews-systems.gitbook.io/connector-api/operations/#command) to
              be returned.

          limitation: Limitation on the quantity of data returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/commands/getAllByIds",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "command_ids": command_ids,
                    "limitation": limitation,
                },
                command_list_by_ids_params.CommandListByIDsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeviceCommandResult,
        )


class CommandsResourceWithRawResponse:
    def __init__(self, commands: CommandsResource) -> None:
        self._commands = commands

        self.update = to_raw_response_wrapper(
            commands.update,
        )
        self.add_key_cutter = to_raw_response_wrapper(
            commands.add_key_cutter,
        )
        self.add_payment_terminal = to_raw_response_wrapper(
            commands.add_payment_terminal,
        )
        self.add_printer = to_raw_response_wrapper(
            commands.add_printer,
        )
        self.list_active = to_raw_response_wrapper(
            commands.list_active,
        )
        self.list_by_ids = to_raw_response_wrapper(
            commands.list_by_ids,
        )


class AsyncCommandsResourceWithRawResponse:
    def __init__(self, commands: AsyncCommandsResource) -> None:
        self._commands = commands

        self.update = async_to_raw_response_wrapper(
            commands.update,
        )
        self.add_key_cutter = async_to_raw_response_wrapper(
            commands.add_key_cutter,
        )
        self.add_payment_terminal = async_to_raw_response_wrapper(
            commands.add_payment_terminal,
        )
        self.add_printer = async_to_raw_response_wrapper(
            commands.add_printer,
        )
        self.list_active = async_to_raw_response_wrapper(
            commands.list_active,
        )
        self.list_by_ids = async_to_raw_response_wrapper(
            commands.list_by_ids,
        )


class CommandsResourceWithStreamingResponse:
    def __init__(self, commands: CommandsResource) -> None:
        self._commands = commands

        self.update = to_streamed_response_wrapper(
            commands.update,
        )
        self.add_key_cutter = to_streamed_response_wrapper(
            commands.add_key_cutter,
        )
        self.add_payment_terminal = to_streamed_response_wrapper(
            commands.add_payment_terminal,
        )
        self.add_printer = to_streamed_response_wrapper(
            commands.add_printer,
        )
        self.list_active = to_streamed_response_wrapper(
            commands.list_active,
        )
        self.list_by_ids = to_streamed_response_wrapper(
            commands.list_by_ids,
        )


class AsyncCommandsResourceWithStreamingResponse:
    def __init__(self, commands: AsyncCommandsResource) -> None:
        self._commands = commands

        self.update = async_to_streamed_response_wrapper(
            commands.update,
        )
        self.add_key_cutter = async_to_streamed_response_wrapper(
            commands.add_key_cutter,
        )
        self.add_payment_terminal = async_to_streamed_response_wrapper(
            commands.add_payment_terminal,
        )
        self.add_printer = async_to_streamed_response_wrapper(
            commands.add_printer,
        )
        self.list_active = async_to_streamed_response_wrapper(
            commands.list_active,
        )
        self.list_by_ids = async_to_streamed_response_wrapper(
            commands.list_by_ids,
        )
