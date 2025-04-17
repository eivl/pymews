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
    bill_add_params,
    bill_list_params,
    bill_close_params,
    bill_delete_params,
    bill_update_params,
    bill_get_pdf_params,
)
from .....types.api.connector.v1.bill_add_response import BillAddResponse
from .....types.api.connector.v1.bill_list_response import BillListResponse
from .....types.api.connector.v1.bill_close_response import BillCloseResponse
from .....types.api.connector.v1.bill_update_response import BillUpdateResponse
from .....types.api.connector.v1.bill_get_pdf_response import BillGetPdfResponse

__all__ = ["BillsResource", "AsyncBillsResource"]


class BillsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BillsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return BillsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BillsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return BillsResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        access_token: str,
        bills_updates: Iterable[bill_update_params.BillsUpdate],
        client: str,
        client_token: str,
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BillUpdateResponse:
        """Updates one or more existing bills in the system.

        Closed bills cannot be
        updated. Note this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        Args:
          access_token: Access token of the client application.

          bills_updates: Information about bills to be updated.

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
            "/api/connector/v1/bills/update",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "bills_updates": bills_updates,
                    "client": client,
                    "client_token": client_token,
                    "enterprise_id": enterprise_id,
                },
                bill_update_params.BillUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillUpdateResponse,
        )

    def list(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: bill_list_params.Limitation,
        bill_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        closed_utc: Optional[bill_list_params.ClosedUtc] | NotGiven = NOT_GIVEN,
        correction_state: Optional[List[Literal["Bill", "CorrectiveBill"]]] | NotGiven = NOT_GIVEN,
        created_utc: Optional[bill_list_params.CreatedUtc] | NotGiven = NOT_GIVEN,
        customer_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        due_utc: Optional[bill_list_params.DueUtc] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        extent: Optional[bill_list_params.Extent] | NotGiven = NOT_GIVEN,
        paid_utc: Optional[bill_list_params.PaidUtc] | NotGiven = NOT_GIVEN,
        state: Optional[Literal["Open", "Closed"]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[bill_list_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BillListResponse:
        """
        Returns all bills, optionally filtered by customers, identifiers and other
        filters. Note this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          bill_ids: Unique identifiers of the `Bills`. Required if no other filter is provided.

          closed_utc: Interval in which the `Bill` was closed.

          correction_state: Whether to return regular bills, corrective bills, or both. If `BillIds` are
              specified, defaults to both, otherwise defaults to `Bill`.

          created_utc: Interval in which the `Bill` was created.

          customer_ids: Unique identifiers of the `Customers`.

          due_utc: Interval in which the `Bill` is due to be paid.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          extent: Extent of data to be returned. E.g. it is possible to specify that together with
              the bills, payments and revenue items should be also returned. **Deprecated!**

          paid_utc: Interval in which the `Bill` was paid.

          state: Whether the bill is `Open` or `Closed`.

          updated_utc: Interval in which the `Bill` was updated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/bills/getAll",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "bill_ids": bill_ids,
                    "closed_utc": closed_utc,
                    "correction_state": correction_state,
                    "created_utc": created_utc,
                    "customer_ids": customer_ids,
                    "due_utc": due_utc,
                    "enterprise_ids": enterprise_ids,
                    "extent": extent,
                    "paid_utc": paid_utc,
                    "state": state,
                    "updated_utc": updated_utc,
                },
                bill_list_params.BillListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillListResponse,
        )

    def delete(
        self,
        *,
        access_token: str,
        bill_ids: List[str],
        client: str,
        client_token: str,
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Removes selected bills.

        Bill must be empty, otherwise it's not possible to
        delete it. Note this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          bill_ids: Unique identifiers of the
              [Bill](https://mews-systems.gitbook.io/connector-api/operations/#bill)s to be
              deleted.

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
            "/api/connector/v1/bills/delete",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "bill_ids": bill_ids,
                    "client": client,
                    "client_token": client_token,
                    "enterprise_id": enterprise_id,
                },
                bill_delete_params.BillDeleteParams,
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
        bills: Iterable[bill_add_params.Bill],
        client: str,
        client_token: str,
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BillAddResponse:
        """Creates new empty bill assigned to specified account.

        Note this operation
        supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          bills: Information about bills to be created.

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
            "/api/connector/v1/bills/add",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "bills": bills,
                    "client": client,
                    "client_token": client_token,
                    "enterprise_id": enterprise_id,
                },
                bill_add_params.BillAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillAddResponse,
        )

    def close(
        self,
        *,
        access_token: str,
        bill_id: str,
        client: str,
        client_token: str,
        type: Literal["Receipt", "Invoice"],
        account_address: Optional[bill_close_params.AccountAddress] | NotGiven = NOT_GIVEN,
        account_tax_identifier: Optional[bill_close_params.AccountTaxIdentifier] | NotGiven = NOT_GIVEN,
        address: Optional[bill_close_params.Address] | NotGiven = NOT_GIVEN,
        associated_account_data: Optional[Iterable[bill_close_params.AssociatedAccountData]] | NotGiven = NOT_GIVEN,
        bill_counter_id: Optional[str] | NotGiven = NOT_GIVEN,
        company_tax_identifier: Optional[bill_close_params.CompanyTaxIdentifier] | NotGiven = NOT_GIVEN,
        due_date: Optional[bill_close_params.DueDate] | NotGiven = NOT_GIVEN,
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        fiscal_machine_id: Optional[str] | NotGiven = NOT_GIVEN,
        notes: Optional[bill_close_params.Notes] | NotGiven = NOT_GIVEN,
        options: Optional[bill_close_params.Options] | NotGiven = NOT_GIVEN,
        purchase_order_number: Optional[bill_close_params.PurchaseOrderNumber] | NotGiven = NOT_GIVEN,
        taxed_date: Optional[bill_close_params.TaxedDate] | NotGiven = NOT_GIVEN,
        tax_identifier: Optional[bill_close_params.TaxIdentifier] | NotGiven = NOT_GIVEN,
        variable_symbol: Optional[bill_close_params.VariableSymbol] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BillCloseResponse:
        """Closes a bill so no further modification to it is possible.

        Note this operation
        supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          bill_id: Unique identifier of the
              [Bill](https://mews-systems.gitbook.io/connector-api/operations/#bill) to be
              closed.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          type: After a bill is closed, the Bill Type is set to `Receipt` or `Invoice`.
              `Receipt` indicates that the bill has been fully paid and the balance is zero.
              `Invoice` indicates that the bill has not yet been fully paid but an invoice has
              been issued. Prior to closing, Bill Type should not be used.

              - `Receipt` - Default; the bill has been paid in full; only applicable after the
                bill is closed.
              - `Invoice` - Bill has not been paid in full but an invoice has been issued to
                request payment.

          account_address: New address details.

          account_tax_identifier: Tax identifier of account to be put on a bill.

          address: New address details.

          associated_account_data: Account data of the associated account on a bill. Currently one object is
              supported and only populated when the bill is closed.

          bill_counter_id: Unique identifier of the
              [Counter](https://mews-systems.gitbook.io/connector-api/operations/counters/#counter)
              to be used for closing. Default one is used when no value is provided.

          company_tax_identifier: Tax identifier of company to be put on a bill.

          due_date: Deadline when bill is due to be paid. Can be used only with `Type` of `Invoice`.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          fiscal_machine_id: Unique identifier of the
              [Fiscal Machine](https://mews-systems.gitbook.io/connector-api/operations/devices/#device)
              to be used for closing. Default one is used when no value is provided.

          notes: Notes to be attached to bill.

          options

          purchase_order_number: Unique number of the purchase order from the buyer.

          taxed_date: Date of consumption for tax purposes. Can be used only with `Type` of `Invoice`.

          tax_identifier: Tax identifier of account to be put on a bill.

          variable_symbol: Optional unique identifier of requested payment. Can be used only with `Type` of
              `Invoice`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/bills/close",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "bill_id": bill_id,
                    "client": client,
                    "client_token": client_token,
                    "type": type,
                    "account_address": account_address,
                    "account_tax_identifier": account_tax_identifier,
                    "address": address,
                    "associated_account_data": associated_account_data,
                    "bill_counter_id": bill_counter_id,
                    "company_tax_identifier": company_tax_identifier,
                    "due_date": due_date,
                    "enterprise_id": enterprise_id,
                    "fiscal_machine_id": fiscal_machine_id,
                    "notes": notes,
                    "options": options,
                    "purchase_order_number": purchase_order_number,
                    "taxed_date": taxed_date,
                    "tax_identifier": tax_identifier,
                    "variable_symbol": variable_symbol,
                },
                bill_close_params.BillCloseParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillCloseResponse,
        )

    def get_pdf(
        self,
        *,
        access_token: str,
        bill_id: str,
        client: str,
        client_token: str,
        bill_print_event_id: Optional[str] | NotGiven = NOT_GIVEN,
        pdf_template: Optional[Literal["Detailed", "Consumption", "Reservation", "OrderItem", "Guest"]]
        | NotGiven = NOT_GIVEN,
        print_reason: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BillGetPdfResponse:
        """Creates a PDF version of the specified bill.

        In case it's not possible to return
        PDF immediately, you must retry the call later while providing the unique event
        identifier that is returned from the first invocation.

        Args:
          access_token: Access token of the client application.

          bill_id: Unique identifier of the
              [Bill](https://mews-systems.gitbook.io/connector-api/operations/#bill) to be
              printed.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          bill_print_event_id: Unique identifier of the
              [Bill print event](https://mews-systems.gitbook.io/connector-api/operations/#bill-print-event)
              returned by previous invocation.

          pdf_template: Detailed (Detailed overview. Items are grouped by the reservation, item type and
              price, and consumption date.)

              Consumption (Overview by date (no reservation details). Items of the same type
              and price are grouped by consumption date.)

              Reservation (Overview by reservation (no date). Items of the same type and price
              are grouped by reservation.)

              OrderItem (Consumption overview (not fiscal document). Items are grouped by the
              item type and price without reservation details and consumption date.)

              Guest (Overview by guest. Items are grouped by guest, reservation, consumption
              date, and item type.)

              - `Detailed` - Detailed overview. Items are grouped by the reservation, item
                type and price, and consumption date.
              - `Consumption` - Overview by date (no reservation details). Items of the same
                type and price are grouped by consumption date.
              - `Reservation` - Overview by reservation (no date). Items of the same type and
                price are grouped by reservation.
              - `OrderItem` - Consumption overview (not fiscal document). Items are grouped by
                the item type and price without reservation details and consumption date.
              - `Guest` - Overview by guest. Items are grouped by guest, reservation,
                consumption date, and item type.

          print_reason: The reason for reprinting the bill with different template. Required for France
              LE.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/bills/getPdf",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "bill_id": bill_id,
                    "client": client,
                    "client_token": client_token,
                    "bill_print_event_id": bill_print_event_id,
                    "pdf_template": pdf_template,
                    "print_reason": print_reason,
                },
                bill_get_pdf_params.BillGetPdfParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillGetPdfResponse,
        )


class AsyncBillsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBillsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return AsyncBillsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBillsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return AsyncBillsResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        access_token: str,
        bills_updates: Iterable[bill_update_params.BillsUpdate],
        client: str,
        client_token: str,
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BillUpdateResponse:
        """Updates one or more existing bills in the system.

        Closed bills cannot be
        updated. Note this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        Args:
          access_token: Access token of the client application.

          bills_updates: Information about bills to be updated.

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
            "/api/connector/v1/bills/update",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "bills_updates": bills_updates,
                    "client": client,
                    "client_token": client_token,
                    "enterprise_id": enterprise_id,
                },
                bill_update_params.BillUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillUpdateResponse,
        )

    async def list(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: bill_list_params.Limitation,
        bill_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        closed_utc: Optional[bill_list_params.ClosedUtc] | NotGiven = NOT_GIVEN,
        correction_state: Optional[List[Literal["Bill", "CorrectiveBill"]]] | NotGiven = NOT_GIVEN,
        created_utc: Optional[bill_list_params.CreatedUtc] | NotGiven = NOT_GIVEN,
        customer_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        due_utc: Optional[bill_list_params.DueUtc] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        extent: Optional[bill_list_params.Extent] | NotGiven = NOT_GIVEN,
        paid_utc: Optional[bill_list_params.PaidUtc] | NotGiven = NOT_GIVEN,
        state: Optional[Literal["Open", "Closed"]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[bill_list_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BillListResponse:
        """
        Returns all bills, optionally filtered by customers, identifiers and other
        filters. Note this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          bill_ids: Unique identifiers of the `Bills`. Required if no other filter is provided.

          closed_utc: Interval in which the `Bill` was closed.

          correction_state: Whether to return regular bills, corrective bills, or both. If `BillIds` are
              specified, defaults to both, otherwise defaults to `Bill`.

          created_utc: Interval in which the `Bill` was created.

          customer_ids: Unique identifiers of the `Customers`.

          due_utc: Interval in which the `Bill` is due to be paid.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          extent: Extent of data to be returned. E.g. it is possible to specify that together with
              the bills, payments and revenue items should be also returned. **Deprecated!**

          paid_utc: Interval in which the `Bill` was paid.

          state: Whether the bill is `Open` or `Closed`.

          updated_utc: Interval in which the `Bill` was updated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/bills/getAll",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "bill_ids": bill_ids,
                    "closed_utc": closed_utc,
                    "correction_state": correction_state,
                    "created_utc": created_utc,
                    "customer_ids": customer_ids,
                    "due_utc": due_utc,
                    "enterprise_ids": enterprise_ids,
                    "extent": extent,
                    "paid_utc": paid_utc,
                    "state": state,
                    "updated_utc": updated_utc,
                },
                bill_list_params.BillListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillListResponse,
        )

    async def delete(
        self,
        *,
        access_token: str,
        bill_ids: List[str],
        client: str,
        client_token: str,
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Removes selected bills.

        Bill must be empty, otherwise it's not possible to
        delete it. Note this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          bill_ids: Unique identifiers of the
              [Bill](https://mews-systems.gitbook.io/connector-api/operations/#bill)s to be
              deleted.

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
            "/api/connector/v1/bills/delete",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "bill_ids": bill_ids,
                    "client": client,
                    "client_token": client_token,
                    "enterprise_id": enterprise_id,
                },
                bill_delete_params.BillDeleteParams,
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
        bills: Iterable[bill_add_params.Bill],
        client: str,
        client_token: str,
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BillAddResponse:
        """Creates new empty bill assigned to specified account.

        Note this operation
        supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          bills: Information about bills to be created.

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
            "/api/connector/v1/bills/add",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "bills": bills,
                    "client": client,
                    "client_token": client_token,
                    "enterprise_id": enterprise_id,
                },
                bill_add_params.BillAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillAddResponse,
        )

    async def close(
        self,
        *,
        access_token: str,
        bill_id: str,
        client: str,
        client_token: str,
        type: Literal["Receipt", "Invoice"],
        account_address: Optional[bill_close_params.AccountAddress] | NotGiven = NOT_GIVEN,
        account_tax_identifier: Optional[bill_close_params.AccountTaxIdentifier] | NotGiven = NOT_GIVEN,
        address: Optional[bill_close_params.Address] | NotGiven = NOT_GIVEN,
        associated_account_data: Optional[Iterable[bill_close_params.AssociatedAccountData]] | NotGiven = NOT_GIVEN,
        bill_counter_id: Optional[str] | NotGiven = NOT_GIVEN,
        company_tax_identifier: Optional[bill_close_params.CompanyTaxIdentifier] | NotGiven = NOT_GIVEN,
        due_date: Optional[bill_close_params.DueDate] | NotGiven = NOT_GIVEN,
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        fiscal_machine_id: Optional[str] | NotGiven = NOT_GIVEN,
        notes: Optional[bill_close_params.Notes] | NotGiven = NOT_GIVEN,
        options: Optional[bill_close_params.Options] | NotGiven = NOT_GIVEN,
        purchase_order_number: Optional[bill_close_params.PurchaseOrderNumber] | NotGiven = NOT_GIVEN,
        taxed_date: Optional[bill_close_params.TaxedDate] | NotGiven = NOT_GIVEN,
        tax_identifier: Optional[bill_close_params.TaxIdentifier] | NotGiven = NOT_GIVEN,
        variable_symbol: Optional[bill_close_params.VariableSymbol] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BillCloseResponse:
        """Closes a bill so no further modification to it is possible.

        Note this operation
        supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          bill_id: Unique identifier of the
              [Bill](https://mews-systems.gitbook.io/connector-api/operations/#bill) to be
              closed.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          type: After a bill is closed, the Bill Type is set to `Receipt` or `Invoice`.
              `Receipt` indicates that the bill has been fully paid and the balance is zero.
              `Invoice` indicates that the bill has not yet been fully paid but an invoice has
              been issued. Prior to closing, Bill Type should not be used.

              - `Receipt` - Default; the bill has been paid in full; only applicable after the
                bill is closed.
              - `Invoice` - Bill has not been paid in full but an invoice has been issued to
                request payment.

          account_address: New address details.

          account_tax_identifier: Tax identifier of account to be put on a bill.

          address: New address details.

          associated_account_data: Account data of the associated account on a bill. Currently one object is
              supported and only populated when the bill is closed.

          bill_counter_id: Unique identifier of the
              [Counter](https://mews-systems.gitbook.io/connector-api/operations/counters/#counter)
              to be used for closing. Default one is used when no value is provided.

          company_tax_identifier: Tax identifier of company to be put on a bill.

          due_date: Deadline when bill is due to be paid. Can be used only with `Type` of `Invoice`.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          fiscal_machine_id: Unique identifier of the
              [Fiscal Machine](https://mews-systems.gitbook.io/connector-api/operations/devices/#device)
              to be used for closing. Default one is used when no value is provided.

          notes: Notes to be attached to bill.

          options

          purchase_order_number: Unique number of the purchase order from the buyer.

          taxed_date: Date of consumption for tax purposes. Can be used only with `Type` of `Invoice`.

          tax_identifier: Tax identifier of account to be put on a bill.

          variable_symbol: Optional unique identifier of requested payment. Can be used only with `Type` of
              `Invoice`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/bills/close",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "bill_id": bill_id,
                    "client": client,
                    "client_token": client_token,
                    "type": type,
                    "account_address": account_address,
                    "account_tax_identifier": account_tax_identifier,
                    "address": address,
                    "associated_account_data": associated_account_data,
                    "bill_counter_id": bill_counter_id,
                    "company_tax_identifier": company_tax_identifier,
                    "due_date": due_date,
                    "enterprise_id": enterprise_id,
                    "fiscal_machine_id": fiscal_machine_id,
                    "notes": notes,
                    "options": options,
                    "purchase_order_number": purchase_order_number,
                    "taxed_date": taxed_date,
                    "tax_identifier": tax_identifier,
                    "variable_symbol": variable_symbol,
                },
                bill_close_params.BillCloseParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillCloseResponse,
        )

    async def get_pdf(
        self,
        *,
        access_token: str,
        bill_id: str,
        client: str,
        client_token: str,
        bill_print_event_id: Optional[str] | NotGiven = NOT_GIVEN,
        pdf_template: Optional[Literal["Detailed", "Consumption", "Reservation", "OrderItem", "Guest"]]
        | NotGiven = NOT_GIVEN,
        print_reason: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BillGetPdfResponse:
        """Creates a PDF version of the specified bill.

        In case it's not possible to return
        PDF immediately, you must retry the call later while providing the unique event
        identifier that is returned from the first invocation.

        Args:
          access_token: Access token of the client application.

          bill_id: Unique identifier of the
              [Bill](https://mews-systems.gitbook.io/connector-api/operations/#bill) to be
              printed.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          bill_print_event_id: Unique identifier of the
              [Bill print event](https://mews-systems.gitbook.io/connector-api/operations/#bill-print-event)
              returned by previous invocation.

          pdf_template: Detailed (Detailed overview. Items are grouped by the reservation, item type and
              price, and consumption date.)

              Consumption (Overview by date (no reservation details). Items of the same type
              and price are grouped by consumption date.)

              Reservation (Overview by reservation (no date). Items of the same type and price
              are grouped by reservation.)

              OrderItem (Consumption overview (not fiscal document). Items are grouped by the
              item type and price without reservation details and consumption date.)

              Guest (Overview by guest. Items are grouped by guest, reservation, consumption
              date, and item type.)

              - `Detailed` - Detailed overview. Items are grouped by the reservation, item
                type and price, and consumption date.
              - `Consumption` - Overview by date (no reservation details). Items of the same
                type and price are grouped by consumption date.
              - `Reservation` - Overview by reservation (no date). Items of the same type and
                price are grouped by reservation.
              - `OrderItem` - Consumption overview (not fiscal document). Items are grouped by
                the item type and price without reservation details and consumption date.
              - `Guest` - Overview by guest. Items are grouped by guest, reservation,
                consumption date, and item type.

          print_reason: The reason for reprinting the bill with different template. Required for France
              LE.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/bills/getPdf",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "bill_id": bill_id,
                    "client": client,
                    "client_token": client_token,
                    "bill_print_event_id": bill_print_event_id,
                    "pdf_template": pdf_template,
                    "print_reason": print_reason,
                },
                bill_get_pdf_params.BillGetPdfParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillGetPdfResponse,
        )


class BillsResourceWithRawResponse:
    def __init__(self, bills: BillsResource) -> None:
        self._bills = bills

        self.update = to_raw_response_wrapper(
            bills.update,
        )
        self.list = to_raw_response_wrapper(
            bills.list,
        )
        self.delete = to_raw_response_wrapper(
            bills.delete,
        )
        self.add = to_raw_response_wrapper(
            bills.add,
        )
        self.close = to_raw_response_wrapper(
            bills.close,
        )
        self.get_pdf = to_raw_response_wrapper(
            bills.get_pdf,
        )


class AsyncBillsResourceWithRawResponse:
    def __init__(self, bills: AsyncBillsResource) -> None:
        self._bills = bills

        self.update = async_to_raw_response_wrapper(
            bills.update,
        )
        self.list = async_to_raw_response_wrapper(
            bills.list,
        )
        self.delete = async_to_raw_response_wrapper(
            bills.delete,
        )
        self.add = async_to_raw_response_wrapper(
            bills.add,
        )
        self.close = async_to_raw_response_wrapper(
            bills.close,
        )
        self.get_pdf = async_to_raw_response_wrapper(
            bills.get_pdf,
        )


class BillsResourceWithStreamingResponse:
    def __init__(self, bills: BillsResource) -> None:
        self._bills = bills

        self.update = to_streamed_response_wrapper(
            bills.update,
        )
        self.list = to_streamed_response_wrapper(
            bills.list,
        )
        self.delete = to_streamed_response_wrapper(
            bills.delete,
        )
        self.add = to_streamed_response_wrapper(
            bills.add,
        )
        self.close = to_streamed_response_wrapper(
            bills.close,
        )
        self.get_pdf = to_streamed_response_wrapper(
            bills.get_pdf,
        )


class AsyncBillsResourceWithStreamingResponse:
    def __init__(self, bills: AsyncBillsResource) -> None:
        self._bills = bills

        self.update = async_to_streamed_response_wrapper(
            bills.update,
        )
        self.list = async_to_streamed_response_wrapper(
            bills.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            bills.delete,
        )
        self.add = async_to_streamed_response_wrapper(
            bills.add,
        )
        self.close = async_to_streamed_response_wrapper(
            bills.close,
        )
        self.get_pdf = async_to_streamed_response_wrapper(
            bills.get_pdf,
        )
