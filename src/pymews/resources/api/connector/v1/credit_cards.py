# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

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
    credit_card_list_params,
    credit_card_charge_params,
    credit_card_disable_params,
    credit_card_list_by_ids_params,
    credit_card_add_tokenized_params,
    credit_card_list_by_customers_params,
)
from .....types.api.connector.v1.credit_card_result import CreditCardResult
from .....types.api.connector.add_credit_card_result import AddCreditCardResult
from .....types.api.connector.v1.credit_card_charge_response import CreditCardChargeResponse

__all__ = ["CreditCardsResource", "AsyncCreditCardsResource"]


class CreditCardsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CreditCardsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return CreditCardsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CreditCardsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return CreditCardsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: credit_card_list_params.Limitation,
        credit_card_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        customer_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[credit_card_list_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreditCardResult:
        """
        Returns all credit cards, possibly filtered by identifiers,
        [Customers](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer)
        or other filters. Note this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          credit_card_ids: Unique identifiers of the
              [Credit cards](https://mews-systems.gitbook.io/connector-api/operations/#credit-card).
              Required if no other filter is provided.

          customer_ids: Unique identifiers of the
              [Customers](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer).

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/creditCards/getAll",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "credit_card_ids": credit_card_ids,
                    "customer_ids": customer_ids,
                    "enterprise_ids": enterprise_ids,
                    "updated_utc": updated_utc,
                },
                credit_card_list_params.CreditCardListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditCardResult,
        )

    def add_tokenized(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        credit_card_data: credit_card_add_tokenized_params.CreditCardData,
        customer_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AddCreditCardResult:
        """Adds a new tokenized credit card to the specified customer.

        To be able to use
        this operation special permission has to be granted during certification.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          credit_card_data: Credit card details provided by PCI provider.

          customer_id: Unique identifier of the
              [Customer](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/creditCards/addTokenized",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "credit_card_data": credit_card_data,
                    "customer_id": customer_id,
                },
                credit_card_add_tokenized_params.CreditCardAddTokenizedParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddCreditCardResult,
        )

    def charge(
        self,
        *,
        access_token: str,
        amount: credit_card_charge_params.Amount,
        client: str,
        client_token: str,
        accounting_category_id: Optional[str] | NotGiven = NOT_GIVEN,
        bill_id: Optional[str] | NotGiven = NOT_GIVEN,
        credit_card_id: str | NotGiven = NOT_GIVEN,
        notes: Optional[str] | NotGiven = NOT_GIVEN,
        receipt_identifier: Optional[str] | NotGiven = NOT_GIVEN,
        reservation_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreditCardChargeResponse:
        """
        Creates payment for specified customer credit card and charges the credit card
        via a gateway. Note that the kind of the card has to be `Gateway`.

        Args:
          access_token: Access token of the client application.

          amount

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          accounting_category_id: Unique identifier of the
              [Accounting category](https://mews-systems.gitbook.io/connector-api/operations/accountingcategories/#accounting-category).

          credit_card_id: Unique identifier of the
              [Credit card](https://mews-systems.gitbook.io/connector-api/operations/#credit-card).

          notes: Additional payment notes.

          receipt_identifier: Identifier of the payment receipt.

          reservation_id: Unique identifier of the reservation the payment belongs to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/creditCards/charge",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "amount": amount,
                    "client": client,
                    "client_token": client_token,
                    "accounting_category_id": accounting_category_id,
                    "bill_id": bill_id,
                    "credit_card_id": credit_card_id,
                    "notes": notes,
                    "receipt_identifier": receipt_identifier,
                    "reservation_id": reservation_id,
                },
                credit_card_charge_params.CreditCardChargeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditCardChargeResponse,
        )

    def disable(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        credit_card_id: str,
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Disable an existing credit card in the system.

        Only gateway credit card can be
        disabled. Note this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          credit_card_id: Unique identifier of the `CreditCard` to disable.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/creditCards/disable",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "credit_card_id": credit_card_id,
                    "enterprise_id": enterprise_id,
                },
                credit_card_disable_params.CreditCardDisableParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def list_by_customers(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        customer_ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreditCardResult:
        """
        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          customer_ids: Unique identifier of the
              [Customer](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/creditCards/getAllByCustomers",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "customer_ids": customer_ids,
                },
                credit_card_list_by_customers_params.CreditCardListByCustomersParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditCardResult,
        )

    def list_by_ids(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        credit_card_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreditCardResult:
        """
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
            "/api/connector/v1/creditCards/getAllByIds",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "credit_card_ids": credit_card_ids,
                },
                credit_card_list_by_ids_params.CreditCardListByIDsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditCardResult,
        )


class AsyncCreditCardsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCreditCardsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return AsyncCreditCardsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCreditCardsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return AsyncCreditCardsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: credit_card_list_params.Limitation,
        credit_card_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        customer_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[credit_card_list_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreditCardResult:
        """
        Returns all credit cards, possibly filtered by identifiers,
        [Customers](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer)
        or other filters. Note this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          credit_card_ids: Unique identifiers of the
              [Credit cards](https://mews-systems.gitbook.io/connector-api/operations/#credit-card).
              Required if no other filter is provided.

          customer_ids: Unique identifiers of the
              [Customers](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer).

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/creditCards/getAll",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "credit_card_ids": credit_card_ids,
                    "customer_ids": customer_ids,
                    "enterprise_ids": enterprise_ids,
                    "updated_utc": updated_utc,
                },
                credit_card_list_params.CreditCardListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditCardResult,
        )

    async def add_tokenized(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        credit_card_data: credit_card_add_tokenized_params.CreditCardData,
        customer_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AddCreditCardResult:
        """Adds a new tokenized credit card to the specified customer.

        To be able to use
        this operation special permission has to be granted during certification.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          credit_card_data: Credit card details provided by PCI provider.

          customer_id: Unique identifier of the
              [Customer](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/creditCards/addTokenized",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "credit_card_data": credit_card_data,
                    "customer_id": customer_id,
                },
                credit_card_add_tokenized_params.CreditCardAddTokenizedParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddCreditCardResult,
        )

    async def charge(
        self,
        *,
        access_token: str,
        amount: credit_card_charge_params.Amount,
        client: str,
        client_token: str,
        accounting_category_id: Optional[str] | NotGiven = NOT_GIVEN,
        bill_id: Optional[str] | NotGiven = NOT_GIVEN,
        credit_card_id: str | NotGiven = NOT_GIVEN,
        notes: Optional[str] | NotGiven = NOT_GIVEN,
        receipt_identifier: Optional[str] | NotGiven = NOT_GIVEN,
        reservation_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreditCardChargeResponse:
        """
        Creates payment for specified customer credit card and charges the credit card
        via a gateway. Note that the kind of the card has to be `Gateway`.

        Args:
          access_token: Access token of the client application.

          amount

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          accounting_category_id: Unique identifier of the
              [Accounting category](https://mews-systems.gitbook.io/connector-api/operations/accountingcategories/#accounting-category).

          credit_card_id: Unique identifier of the
              [Credit card](https://mews-systems.gitbook.io/connector-api/operations/#credit-card).

          notes: Additional payment notes.

          receipt_identifier: Identifier of the payment receipt.

          reservation_id: Unique identifier of the reservation the payment belongs to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/creditCards/charge",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "amount": amount,
                    "client": client,
                    "client_token": client_token,
                    "accounting_category_id": accounting_category_id,
                    "bill_id": bill_id,
                    "credit_card_id": credit_card_id,
                    "notes": notes,
                    "receipt_identifier": receipt_identifier,
                    "reservation_id": reservation_id,
                },
                credit_card_charge_params.CreditCardChargeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditCardChargeResponse,
        )

    async def disable(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        credit_card_id: str,
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Disable an existing credit card in the system.

        Only gateway credit card can be
        disabled. Note this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          credit_card_id: Unique identifier of the `CreditCard` to disable.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/creditCards/disable",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "credit_card_id": credit_card_id,
                    "enterprise_id": enterprise_id,
                },
                credit_card_disable_params.CreditCardDisableParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def list_by_customers(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        customer_ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreditCardResult:
        """
        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          customer_ids: Unique identifier of the
              [Customer](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/creditCards/getAllByCustomers",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "customer_ids": customer_ids,
                },
                credit_card_list_by_customers_params.CreditCardListByCustomersParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditCardResult,
        )

    async def list_by_ids(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        credit_card_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreditCardResult:
        """
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
            "/api/connector/v1/creditCards/getAllByIds",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "credit_card_ids": credit_card_ids,
                },
                credit_card_list_by_ids_params.CreditCardListByIDsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditCardResult,
        )


class CreditCardsResourceWithRawResponse:
    def __init__(self, credit_cards: CreditCardsResource) -> None:
        self._credit_cards = credit_cards

        self.list = to_raw_response_wrapper(
            credit_cards.list,
        )
        self.add_tokenized = to_raw_response_wrapper(
            credit_cards.add_tokenized,
        )
        self.charge = to_raw_response_wrapper(
            credit_cards.charge,
        )
        self.disable = to_raw_response_wrapper(
            credit_cards.disable,
        )
        self.list_by_customers = to_raw_response_wrapper(
            credit_cards.list_by_customers,
        )
        self.list_by_ids = to_raw_response_wrapper(
            credit_cards.list_by_ids,
        )


class AsyncCreditCardsResourceWithRawResponse:
    def __init__(self, credit_cards: AsyncCreditCardsResource) -> None:
        self._credit_cards = credit_cards

        self.list = async_to_raw_response_wrapper(
            credit_cards.list,
        )
        self.add_tokenized = async_to_raw_response_wrapper(
            credit_cards.add_tokenized,
        )
        self.charge = async_to_raw_response_wrapper(
            credit_cards.charge,
        )
        self.disable = async_to_raw_response_wrapper(
            credit_cards.disable,
        )
        self.list_by_customers = async_to_raw_response_wrapper(
            credit_cards.list_by_customers,
        )
        self.list_by_ids = async_to_raw_response_wrapper(
            credit_cards.list_by_ids,
        )


class CreditCardsResourceWithStreamingResponse:
    def __init__(self, credit_cards: CreditCardsResource) -> None:
        self._credit_cards = credit_cards

        self.list = to_streamed_response_wrapper(
            credit_cards.list,
        )
        self.add_tokenized = to_streamed_response_wrapper(
            credit_cards.add_tokenized,
        )
        self.charge = to_streamed_response_wrapper(
            credit_cards.charge,
        )
        self.disable = to_streamed_response_wrapper(
            credit_cards.disable,
        )
        self.list_by_customers = to_streamed_response_wrapper(
            credit_cards.list_by_customers,
        )
        self.list_by_ids = to_streamed_response_wrapper(
            credit_cards.list_by_ids,
        )


class AsyncCreditCardsResourceWithStreamingResponse:
    def __init__(self, credit_cards: AsyncCreditCardsResource) -> None:
        self._credit_cards = credit_cards

        self.list = async_to_streamed_response_wrapper(
            credit_cards.list,
        )
        self.add_tokenized = async_to_streamed_response_wrapper(
            credit_cards.add_tokenized,
        )
        self.charge = async_to_streamed_response_wrapper(
            credit_cards.charge,
        )
        self.disable = async_to_streamed_response_wrapper(
            credit_cards.disable,
        )
        self.list_by_customers = async_to_streamed_response_wrapper(
            credit_cards.list_by_customers,
        )
        self.list_by_ids = async_to_streamed_response_wrapper(
            credit_cards.list_by_ids,
        )
