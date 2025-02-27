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
    payment_list_params,
    payment_refund_params,
    payment_add_external_params,
    payment_add_alternative_params,
    payment_add_credit_card_params,
)
from .....types.api.connector.add_credit_card_result import AddCreditCardResult
from .....types.api.connector.v1.payment_list_response import PaymentListResponse
from .....types.api.connector.v1.payment_refund_response import PaymentRefundResponse
from .....types.api.connector.v1.payment_add_external_response import PaymentAddExternalResponse
from .....types.api.connector.v1.payment_add_alternative_response import PaymentAddAlternativeResponse

__all__ = ["PaymentsResource", "AsyncPaymentsResource"]


class PaymentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PaymentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return PaymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PaymentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return PaymentsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: payment_list_params.Limitation,
        account_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        accounting_states: Optional[List[Literal["Open", "Closed", "Inactive", "Canceled"]]] | NotGiven = NOT_GIVEN,
        bill_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        charged_utc: Optional[payment_list_params.ChargedUtc] | NotGiven = NOT_GIVEN,
        closed_utc: Optional[payment_list_params.ClosedUtc] | NotGiven = NOT_GIVEN,
        created_utc: Optional[payment_list_params.CreatedUtc] | NotGiven = NOT_GIVEN,
        currency: Optional[str] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        payment_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        reservation_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        settlement_utc: Optional[payment_list_params.SettlementUtc] | NotGiven = NOT_GIVEN,
        states: Optional[List[Literal["Charged", "Canceled", "Pending", "Failed", "Verifying"]]] | NotGiven = NOT_GIVEN,
        type: Optional[
            Literal[
                "Payment",
                "CreditCardPayment",
                "AlternativePayment",
                "CashPayment",
                "InvoicePayment",
                "ExternalPayment",
                "GhostPayment",
                "TaxDeductedPayment",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        updated_utc: Optional[payment_list_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentListResponse:
        """Returns all payments in the system, filtered by various parameters.

        At least one
        filter parameter must be specified. Note this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          account_ids: Unique identifiers of specific `Accounts` to which payments are belongs to.
              Required if no other filter is provided.

          accounting_states: Accounting state of the item.

          bill_ids: Unique identifiers of specific `Bill` items to which payments are assigned.
              Required if no other filter is provided.

          charged_utc: Time interval during which the `Payment` was charged. Required if no other
              filter is provided.

          closed_utc: Time interval during which the `Payment` was closed. Required if no other filter
              is provided.

          created_utc: Time interval during which the `Payment` was created. Required if no other
              filter is provided.

          currency: ISO-4217 code of the `Currency` the item costs should be converted to.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          payment_ids: Unique identifiers of specific `Payment` items. Required if no other filter is
              provided.

          reservation_ids: Unique identifiers of specific `Reservations` to which payments belong. Required
              if no other filter is provided.

          settlement_utc: Interval in which the `Payments` were settled.

          states: Payment state of the item.

          type: Payment

              CreditCardPayment

              AlternativePayment

              CashPayment

              InvoicePayment

              ExternalPayment

              GhostPayment

              TaxDeductedPayment

          updated_utc: Time interval during which the `Payment` was updated. Required if no other
              filter is provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/payments/getAll",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "account_ids": account_ids,
                    "accounting_states": accounting_states,
                    "bill_ids": bill_ids,
                    "charged_utc": charged_utc,
                    "closed_utc": closed_utc,
                    "created_utc": created_utc,
                    "currency": currency,
                    "enterprise_ids": enterprise_ids,
                    "payment_ids": payment_ids,
                    "reservation_ids": reservation_ids,
                    "settlement_utc": settlement_utc,
                    "states": states,
                    "type": type,
                    "updated_utc": updated_utc,
                },
                payment_list_params.PaymentListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentListResponse,
        )

    def add_alternative(
        self,
        *,
        access_token: str,
        amount: payment_add_alternative_params.Amount,
        client: str,
        client_token: str,
        customer_id: str,
        data: payment_add_alternative_params.Data,
        method: Optional[Literal["Ideal", "ApplePay", "GooglePay"]] | NotGiven = NOT_GIVEN,
        redirect_url: Optional[str] | NotGiven = NOT_GIVEN,
        reservation_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentAddAlternativeResponse:
        """Adds a new alternative payment to a specified customer.

        **Pre-requisites:** The
        property must have the relevant type of alternative payment method enabled in
        their Mews subscriptions in order to accept such payments in their Mews
        environment. Please ask the property to confirm.

        Args:
          access_token: Access token of the client application.

          amount: Price of the product that overrides the price defined in Mews.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          customer_id: Unique identifier of the
              [Customer](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer).

          data: Data specific to particular alternative payment method.

          method: Payment method to use for the alternative payment.

          redirect_url: URL where the customer will be redirected after completing their payment.

          reservation_id: Unique identifier of the reservation the payment belongs to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/payments/addAlternative",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "amount": amount,
                    "client": client,
                    "client_token": client_token,
                    "customer_id": customer_id,
                    "data": data,
                    "method": method,
                    "redirect_url": redirect_url,
                    "reservation_id": reservation_id,
                },
                payment_add_alternative_params.PaymentAddAlternativeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentAddAlternativeResponse,
        )

    def add_credit_card(
        self,
        *,
        access_token: str,
        amount: payment_add_credit_card_params.Amount,
        client: str,
        client_token: str,
        credit_card: payment_add_credit_card_params.CreditCard,
        customer_id: str,
        accounting_category_id: Optional[str] | NotGiven = NOT_GIVEN,
        bill_id: Optional[str] | NotGiven = NOT_GIVEN,
        notes: Optional[str] | NotGiven = NOT_GIVEN,
        receipt_identifier: Optional[str] | NotGiven = NOT_GIVEN,
        reservation_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AddCreditCardResult:
        """Adds a new credit card payment to a bill of the specified customer.

        Note that
        the payment is added to open bill of the customer, either to the specified one
        or the default one. This operation only serves to record a credit card payment
        that has already been taken outside of Mews or Mews' payment terminal, and does
        not actually charge the customer's credit card. The bill can then be closed
        manually by a Mews user, or automatically via API with the
        [Close bill](https://mews-systems.gitbook.io/connector-api/operations/bills/#close-bill)
        operation.

        Args:
          access_token: Access token of the client application.

          amount

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          credit_card

          customer_id: Unique identifier of the
              [Customer](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer).

          accounting_category_id: Unique identifier of an
              [Accounting category](https://mews-systems.gitbook.io/connector-api/operations/accountingcategories/#accounting-category)
              to be assigned to the credit card payment.

          bill_id: Unique identifier of an open bill of the customer where to assign the payment.

          notes: Additional payment notes.

          receipt_identifier: Identifier of the payment receipt.

          reservation_id: Unique identifier of the reservation the payment belongs to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/payments/addCreditCard",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "amount": amount,
                    "client": client,
                    "client_token": client_token,
                    "credit_card": credit_card,
                    "customer_id": customer_id,
                    "accounting_category_id": accounting_category_id,
                    "bill_id": bill_id,
                    "notes": notes,
                    "receipt_identifier": receipt_identifier,
                    "reservation_id": reservation_id,
                },
                payment_add_credit_card_params.PaymentAddCreditCardParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddCreditCardResult,
        )

    def add_external(
        self,
        *,
        access_token: str,
        account_id: str,
        amount: payment_add_external_params.Amount,
        client: str,
        client_token: str,
        accounting_category_id: Optional[str] | NotGiven = NOT_GIVEN,
        bill_id: Optional[str] | NotGiven = NOT_GIVEN,
        customer_id: Optional[str] | NotGiven = NOT_GIVEN,
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        external_identifier: Optional[str] | NotGiven = NOT_GIVEN,
        notes: Optional[str] | NotGiven = NOT_GIVEN,
        reservation_id: Optional[str] | NotGiven = NOT_GIVEN,
        type: Optional[
            Literal[
                "Unspecified",
                "BadDebts",
                "Bacs",
                "WireTransfer",
                "Invoice",
                "ExchangeRateDifference",
                "Complimentary",
                "Reseller",
                "ExchangeRoundingDifference",
                "Barter",
                "Commission",
                "BankCharges",
                "CrossSettlement",
                "Cash",
                "CreditCard",
                "Prepayment",
                "Cheque",
                "Bancontact",
                "IDeal",
                "PayPal",
                "GiftCard",
                "LoyaltyPoints",
                "ChequeVacances",
                "OnlinePayment",
                "CardCheck",
                "PaymentHubRedirection",
                "Voucher",
                "MasterCard",
                "Visa",
                "Amex",
                "Discover",
                "DinersClub",
                "Jcb",
                "UnionPay",
                "Twint",
                "Reka",
                "LoyaltyCard",
                "PosDiningAndSpaReward",
                "DirectDebit",
                "DepositCheck",
                "DepositCash",
                "DepositCreditCard",
                "DepositWireTransfer",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentAddExternalResponse:
        """Adds a new external payment to a bill of the specified customer.

        An external
        payment represents a payment that is tracked outside of the system. Note this
        operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        **Prerequisites:** The external payment type must be enabled by the property in
        order to accept such payments in their Mews environment. Use
        [Get configuration](https://mews-systems.gitbook.io/connector-api/operations/configuration#get-configuration)
        to check which external payment types are supported.

        Args:
          access_token: Access token of the client application.

          account_id: Unique identifier of the
              [Customer](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer)
              or
              [Company](https://mews-systems.gitbook.io/connector-api/operations/companies/#company).
              Company billing may not be enabled for your integration.

          amount

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          accounting_category_id: Unique identifier of an
              [Accounting category](https://mews-systems.gitbook.io/connector-api/operations/accountingcategories/#accounting-category)
              to be assigned to the external payment.

          bill_id: Unique identifier of an open bill of the customer where to assign the payment.

          customer_id: Unique identifier of the
              [Customer](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer).
              **Deprecated!**

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          external_identifier: Identifier of the payment from external system.

          notes: Additional payment notes.

          reservation_id: Unique identifier of the reservation the payment belongs to.

          type: Unspecified (Unspecified (unavailable in French Legal Environment))

              BadDebts (Bad debts)

              Bacs (Bacs payment)

              WireTransfer (Wire transfer)

              Invoice (Invoice)

              ExchangeRateDifference (Exchange rate difference)

              Complimentary (Complimentary)

              Reseller (Reseller)

              ExchangeRoundingDifference (Exchange rounding difference)

              Barter (Barter)

              Commission (Commission)

              BankCharges (Bank charges)

              CrossSettlement (Cross settlement)

              Cash (Cash)

              CreditCard (Credit card)

              Prepayment (Prepayment)

              Cheque (Cheque)

              Bancontact (Bancontact)

              IDeal (iDeal)

              PayPal (PayPal)

              GiftCard (Gift card)

              LoyaltyPoints (Loyalty points)

              ChequeVacances (Chèque-Vacances)

              OnlinePayment (Online payment)

              CardCheck (Card check)

              PaymentHubRedirection (Payment hub redirection)

              Voucher (Voucher)

              MasterCard (MasterCard)

              Visa (Visa)

              Amex (American Express)

              Discover (Discover)

              DinersClub (Diners Club)

              Jcb (JCB)

              UnionPay (UnionPay)

              Twint (TWINT)

              Reka (Reka)

              LoyaltyCard (Loyalty card)

              PosDiningAndSpaReward (POS Dining & Spa Reward)

              DirectDebit (Direct debit)

              DepositCheck (Deposit - check)

              DepositCash (Deposit - cash)

              DepositCreditCard (Deposit - credit card)

              DepositWireTransfer (Deposit - wire transfer)

              - `Unspecified` - Unspecified (unavailable in French Legal Environment)
              - `BadDebts` - Bad debts
              - `Bacs` - Bacs payment
              - `WireTransfer` - Wire transfer
              - `Invoice` - Invoice
              - `ExchangeRateDifference` - Exchange rate difference
              - `Complimentary` - Complimentary
              - `Reseller` - Reseller
              - `ExchangeRoundingDifference` - Exchange rounding difference
              - `Barter` - Barter
              - `Commission` - Commission
              - `BankCharges` - Bank charges
              - `CrossSettlement` - Cross settlement
              - `Cash` - Cash
              - `CreditCard` - Credit card
              - `Prepayment` - Prepayment
              - `Cheque` - Cheque
              - `Bancontact` - Bancontact
              - `IDeal` - iDeal
              - `PayPal` - PayPal
              - `GiftCard` - Gift card
              - `LoyaltyPoints` - Loyalty points
              - `ChequeVacances` - Chèque-Vacances
              - `OnlinePayment` - Online payment
              - `CardCheck` - Card check
              - `PaymentHubRedirection` - Payment hub redirection
              - `Voucher` - Voucher
              - `MasterCard` - MasterCard
              - `Visa` - Visa
              - `Amex` - American Express
              - `Discover` - Discover
              - `DinersClub` - Diners Club
              - `Jcb` - JCB
              - `UnionPay` - UnionPay
              - `Twint` - TWINT
              - `Reka` - Reka
              - `LoyaltyCard` - Loyalty card
              - `PosDiningAndSpaReward` - POS Dining & Spa Reward
              - `DirectDebit` - Direct debit
              - `DepositCheck` - Deposit - check
              - `DepositCash` - Deposit - cash
              - `DepositCreditCard` - Deposit - credit card
              - `DepositWireTransfer` - Deposit - wire transfer

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/payments/addExternal",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "account_id": account_id,
                    "amount": amount,
                    "client": client,
                    "client_token": client_token,
                    "accounting_category_id": accounting_category_id,
                    "bill_id": bill_id,
                    "customer_id": customer_id,
                    "enterprise_id": enterprise_id,
                    "external_identifier": external_identifier,
                    "notes": notes,
                    "reservation_id": reservation_id,
                    "type": type,
                },
                payment_add_external_params.PaymentAddExternalParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentAddExternalResponse,
        )

    def refund(
        self,
        *,
        access_token: str,
        account_id: str,
        client: str,
        client_token: str,
        payment_id: str,
        reason: str,
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        value_to_refund: Optional[float] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentRefundResponse:
        """Refunds a specified payment on a specified account.

        A reason must be provided.
        Optionally, specify an amount for a partial refund. This operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        - **Payment types**: Only `CreditCardPayment` and `AlternativePayment` can be
          refunded. Other payment types will fail.
        - **Refund information**: The refund is a payment itself. To get more
          information, use
          [Get all payments](https://mews-systems.gitbook.io/connector-api/operations/payments#get-all-payments)
          with the `RefundId` as the `PaymentId`.
        - **Potential failures**: This operation initiates the refund process, but
          refunds can fail if the payment is in a `Pending` state and fails processing.
          To check the status of a pending payment, including refunds, use
          [Get all payments](https://mews-systems.gitbook.io/connector-api/operations/payments#get-all-payments).

        Args:
          access_token: Access token of the client application.

          account_id: Unique identifier of the account (for example
              [Customer](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer))
              the payment belongs to.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          payment_id: Unique identifier of specific
              [Payment](https://mews-systems.gitbook.io/connector-api/operations/payments/#payment).

          reason: Refund reason.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          value_to_refund: Refund amount. If not provided, the whole payment will be refunded.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/payments/refund",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "account_id": account_id,
                    "client": client,
                    "client_token": client_token,
                    "payment_id": payment_id,
                    "reason": reason,
                    "enterprise_id": enterprise_id,
                    "value_to_refund": value_to_refund,
                },
                payment_refund_params.PaymentRefundParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentRefundResponse,
        )


class AsyncPaymentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPaymentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return AsyncPaymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPaymentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return AsyncPaymentsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: payment_list_params.Limitation,
        account_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        accounting_states: Optional[List[Literal["Open", "Closed", "Inactive", "Canceled"]]] | NotGiven = NOT_GIVEN,
        bill_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        charged_utc: Optional[payment_list_params.ChargedUtc] | NotGiven = NOT_GIVEN,
        closed_utc: Optional[payment_list_params.ClosedUtc] | NotGiven = NOT_GIVEN,
        created_utc: Optional[payment_list_params.CreatedUtc] | NotGiven = NOT_GIVEN,
        currency: Optional[str] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        payment_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        reservation_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        settlement_utc: Optional[payment_list_params.SettlementUtc] | NotGiven = NOT_GIVEN,
        states: Optional[List[Literal["Charged", "Canceled", "Pending", "Failed", "Verifying"]]] | NotGiven = NOT_GIVEN,
        type: Optional[
            Literal[
                "Payment",
                "CreditCardPayment",
                "AlternativePayment",
                "CashPayment",
                "InvoicePayment",
                "ExternalPayment",
                "GhostPayment",
                "TaxDeductedPayment",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        updated_utc: Optional[payment_list_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentListResponse:
        """Returns all payments in the system, filtered by various parameters.

        At least one
        filter parameter must be specified. Note this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          account_ids: Unique identifiers of specific `Accounts` to which payments are belongs to.
              Required if no other filter is provided.

          accounting_states: Accounting state of the item.

          bill_ids: Unique identifiers of specific `Bill` items to which payments are assigned.
              Required if no other filter is provided.

          charged_utc: Time interval during which the `Payment` was charged. Required if no other
              filter is provided.

          closed_utc: Time interval during which the `Payment` was closed. Required if no other filter
              is provided.

          created_utc: Time interval during which the `Payment` was created. Required if no other
              filter is provided.

          currency: ISO-4217 code of the `Currency` the item costs should be converted to.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          payment_ids: Unique identifiers of specific `Payment` items. Required if no other filter is
              provided.

          reservation_ids: Unique identifiers of specific `Reservations` to which payments belong. Required
              if no other filter is provided.

          settlement_utc: Interval in which the `Payments` were settled.

          states: Payment state of the item.

          type: Payment

              CreditCardPayment

              AlternativePayment

              CashPayment

              InvoicePayment

              ExternalPayment

              GhostPayment

              TaxDeductedPayment

          updated_utc: Time interval during which the `Payment` was updated. Required if no other
              filter is provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/payments/getAll",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "account_ids": account_ids,
                    "accounting_states": accounting_states,
                    "bill_ids": bill_ids,
                    "charged_utc": charged_utc,
                    "closed_utc": closed_utc,
                    "created_utc": created_utc,
                    "currency": currency,
                    "enterprise_ids": enterprise_ids,
                    "payment_ids": payment_ids,
                    "reservation_ids": reservation_ids,
                    "settlement_utc": settlement_utc,
                    "states": states,
                    "type": type,
                    "updated_utc": updated_utc,
                },
                payment_list_params.PaymentListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentListResponse,
        )

    async def add_alternative(
        self,
        *,
        access_token: str,
        amount: payment_add_alternative_params.Amount,
        client: str,
        client_token: str,
        customer_id: str,
        data: payment_add_alternative_params.Data,
        method: Optional[Literal["Ideal", "ApplePay", "GooglePay"]] | NotGiven = NOT_GIVEN,
        redirect_url: Optional[str] | NotGiven = NOT_GIVEN,
        reservation_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentAddAlternativeResponse:
        """Adds a new alternative payment to a specified customer.

        **Pre-requisites:** The
        property must have the relevant type of alternative payment method enabled in
        their Mews subscriptions in order to accept such payments in their Mews
        environment. Please ask the property to confirm.

        Args:
          access_token: Access token of the client application.

          amount: Price of the product that overrides the price defined in Mews.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          customer_id: Unique identifier of the
              [Customer](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer).

          data: Data specific to particular alternative payment method.

          method: Payment method to use for the alternative payment.

          redirect_url: URL where the customer will be redirected after completing their payment.

          reservation_id: Unique identifier of the reservation the payment belongs to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/payments/addAlternative",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "amount": amount,
                    "client": client,
                    "client_token": client_token,
                    "customer_id": customer_id,
                    "data": data,
                    "method": method,
                    "redirect_url": redirect_url,
                    "reservation_id": reservation_id,
                },
                payment_add_alternative_params.PaymentAddAlternativeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentAddAlternativeResponse,
        )

    async def add_credit_card(
        self,
        *,
        access_token: str,
        amount: payment_add_credit_card_params.Amount,
        client: str,
        client_token: str,
        credit_card: payment_add_credit_card_params.CreditCard,
        customer_id: str,
        accounting_category_id: Optional[str] | NotGiven = NOT_GIVEN,
        bill_id: Optional[str] | NotGiven = NOT_GIVEN,
        notes: Optional[str] | NotGiven = NOT_GIVEN,
        receipt_identifier: Optional[str] | NotGiven = NOT_GIVEN,
        reservation_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AddCreditCardResult:
        """Adds a new credit card payment to a bill of the specified customer.

        Note that
        the payment is added to open bill of the customer, either to the specified one
        or the default one. This operation only serves to record a credit card payment
        that has already been taken outside of Mews or Mews' payment terminal, and does
        not actually charge the customer's credit card. The bill can then be closed
        manually by a Mews user, or automatically via API with the
        [Close bill](https://mews-systems.gitbook.io/connector-api/operations/bills/#close-bill)
        operation.

        Args:
          access_token: Access token of the client application.

          amount

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          credit_card

          customer_id: Unique identifier of the
              [Customer](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer).

          accounting_category_id: Unique identifier of an
              [Accounting category](https://mews-systems.gitbook.io/connector-api/operations/accountingcategories/#accounting-category)
              to be assigned to the credit card payment.

          bill_id: Unique identifier of an open bill of the customer where to assign the payment.

          notes: Additional payment notes.

          receipt_identifier: Identifier of the payment receipt.

          reservation_id: Unique identifier of the reservation the payment belongs to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/payments/addCreditCard",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "amount": amount,
                    "client": client,
                    "client_token": client_token,
                    "credit_card": credit_card,
                    "customer_id": customer_id,
                    "accounting_category_id": accounting_category_id,
                    "bill_id": bill_id,
                    "notes": notes,
                    "receipt_identifier": receipt_identifier,
                    "reservation_id": reservation_id,
                },
                payment_add_credit_card_params.PaymentAddCreditCardParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddCreditCardResult,
        )

    async def add_external(
        self,
        *,
        access_token: str,
        account_id: str,
        amount: payment_add_external_params.Amount,
        client: str,
        client_token: str,
        accounting_category_id: Optional[str] | NotGiven = NOT_GIVEN,
        bill_id: Optional[str] | NotGiven = NOT_GIVEN,
        customer_id: Optional[str] | NotGiven = NOT_GIVEN,
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        external_identifier: Optional[str] | NotGiven = NOT_GIVEN,
        notes: Optional[str] | NotGiven = NOT_GIVEN,
        reservation_id: Optional[str] | NotGiven = NOT_GIVEN,
        type: Optional[
            Literal[
                "Unspecified",
                "BadDebts",
                "Bacs",
                "WireTransfer",
                "Invoice",
                "ExchangeRateDifference",
                "Complimentary",
                "Reseller",
                "ExchangeRoundingDifference",
                "Barter",
                "Commission",
                "BankCharges",
                "CrossSettlement",
                "Cash",
                "CreditCard",
                "Prepayment",
                "Cheque",
                "Bancontact",
                "IDeal",
                "PayPal",
                "GiftCard",
                "LoyaltyPoints",
                "ChequeVacances",
                "OnlinePayment",
                "CardCheck",
                "PaymentHubRedirection",
                "Voucher",
                "MasterCard",
                "Visa",
                "Amex",
                "Discover",
                "DinersClub",
                "Jcb",
                "UnionPay",
                "Twint",
                "Reka",
                "LoyaltyCard",
                "PosDiningAndSpaReward",
                "DirectDebit",
                "DepositCheck",
                "DepositCash",
                "DepositCreditCard",
                "DepositWireTransfer",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentAddExternalResponse:
        """Adds a new external payment to a bill of the specified customer.

        An external
        payment represents a payment that is tracked outside of the system. Note this
        operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        **Prerequisites:** The external payment type must be enabled by the property in
        order to accept such payments in their Mews environment. Use
        [Get configuration](https://mews-systems.gitbook.io/connector-api/operations/configuration#get-configuration)
        to check which external payment types are supported.

        Args:
          access_token: Access token of the client application.

          account_id: Unique identifier of the
              [Customer](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer)
              or
              [Company](https://mews-systems.gitbook.io/connector-api/operations/companies/#company).
              Company billing may not be enabled for your integration.

          amount

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          accounting_category_id: Unique identifier of an
              [Accounting category](https://mews-systems.gitbook.io/connector-api/operations/accountingcategories/#accounting-category)
              to be assigned to the external payment.

          bill_id: Unique identifier of an open bill of the customer where to assign the payment.

          customer_id: Unique identifier of the
              [Customer](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer).
              **Deprecated!**

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          external_identifier: Identifier of the payment from external system.

          notes: Additional payment notes.

          reservation_id: Unique identifier of the reservation the payment belongs to.

          type: Unspecified (Unspecified (unavailable in French Legal Environment))

              BadDebts (Bad debts)

              Bacs (Bacs payment)

              WireTransfer (Wire transfer)

              Invoice (Invoice)

              ExchangeRateDifference (Exchange rate difference)

              Complimentary (Complimentary)

              Reseller (Reseller)

              ExchangeRoundingDifference (Exchange rounding difference)

              Barter (Barter)

              Commission (Commission)

              BankCharges (Bank charges)

              CrossSettlement (Cross settlement)

              Cash (Cash)

              CreditCard (Credit card)

              Prepayment (Prepayment)

              Cheque (Cheque)

              Bancontact (Bancontact)

              IDeal (iDeal)

              PayPal (PayPal)

              GiftCard (Gift card)

              LoyaltyPoints (Loyalty points)

              ChequeVacances (Chèque-Vacances)

              OnlinePayment (Online payment)

              CardCheck (Card check)

              PaymentHubRedirection (Payment hub redirection)

              Voucher (Voucher)

              MasterCard (MasterCard)

              Visa (Visa)

              Amex (American Express)

              Discover (Discover)

              DinersClub (Diners Club)

              Jcb (JCB)

              UnionPay (UnionPay)

              Twint (TWINT)

              Reka (Reka)

              LoyaltyCard (Loyalty card)

              PosDiningAndSpaReward (POS Dining & Spa Reward)

              DirectDebit (Direct debit)

              DepositCheck (Deposit - check)

              DepositCash (Deposit - cash)

              DepositCreditCard (Deposit - credit card)

              DepositWireTransfer (Deposit - wire transfer)

              - `Unspecified` - Unspecified (unavailable in French Legal Environment)
              - `BadDebts` - Bad debts
              - `Bacs` - Bacs payment
              - `WireTransfer` - Wire transfer
              - `Invoice` - Invoice
              - `ExchangeRateDifference` - Exchange rate difference
              - `Complimentary` - Complimentary
              - `Reseller` - Reseller
              - `ExchangeRoundingDifference` - Exchange rounding difference
              - `Barter` - Barter
              - `Commission` - Commission
              - `BankCharges` - Bank charges
              - `CrossSettlement` - Cross settlement
              - `Cash` - Cash
              - `CreditCard` - Credit card
              - `Prepayment` - Prepayment
              - `Cheque` - Cheque
              - `Bancontact` - Bancontact
              - `IDeal` - iDeal
              - `PayPal` - PayPal
              - `GiftCard` - Gift card
              - `LoyaltyPoints` - Loyalty points
              - `ChequeVacances` - Chèque-Vacances
              - `OnlinePayment` - Online payment
              - `CardCheck` - Card check
              - `PaymentHubRedirection` - Payment hub redirection
              - `Voucher` - Voucher
              - `MasterCard` - MasterCard
              - `Visa` - Visa
              - `Amex` - American Express
              - `Discover` - Discover
              - `DinersClub` - Diners Club
              - `Jcb` - JCB
              - `UnionPay` - UnionPay
              - `Twint` - TWINT
              - `Reka` - Reka
              - `LoyaltyCard` - Loyalty card
              - `PosDiningAndSpaReward` - POS Dining & Spa Reward
              - `DirectDebit` - Direct debit
              - `DepositCheck` - Deposit - check
              - `DepositCash` - Deposit - cash
              - `DepositCreditCard` - Deposit - credit card
              - `DepositWireTransfer` - Deposit - wire transfer

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/payments/addExternal",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "account_id": account_id,
                    "amount": amount,
                    "client": client,
                    "client_token": client_token,
                    "accounting_category_id": accounting_category_id,
                    "bill_id": bill_id,
                    "customer_id": customer_id,
                    "enterprise_id": enterprise_id,
                    "external_identifier": external_identifier,
                    "notes": notes,
                    "reservation_id": reservation_id,
                    "type": type,
                },
                payment_add_external_params.PaymentAddExternalParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentAddExternalResponse,
        )

    async def refund(
        self,
        *,
        access_token: str,
        account_id: str,
        client: str,
        client_token: str,
        payment_id: str,
        reason: str,
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        value_to_refund: Optional[float] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentRefundResponse:
        """Refunds a specified payment on a specified account.

        A reason must be provided.
        Optionally, specify an amount for a partial refund. This operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        - **Payment types**: Only `CreditCardPayment` and `AlternativePayment` can be
          refunded. Other payment types will fail.
        - **Refund information**: The refund is a payment itself. To get more
          information, use
          [Get all payments](https://mews-systems.gitbook.io/connector-api/operations/payments#get-all-payments)
          with the `RefundId` as the `PaymentId`.
        - **Potential failures**: This operation initiates the refund process, but
          refunds can fail if the payment is in a `Pending` state and fails processing.
          To check the status of a pending payment, including refunds, use
          [Get all payments](https://mews-systems.gitbook.io/connector-api/operations/payments#get-all-payments).

        Args:
          access_token: Access token of the client application.

          account_id: Unique identifier of the account (for example
              [Customer](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer))
              the payment belongs to.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          payment_id: Unique identifier of specific
              [Payment](https://mews-systems.gitbook.io/connector-api/operations/payments/#payment).

          reason: Refund reason.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          value_to_refund: Refund amount. If not provided, the whole payment will be refunded.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/payments/refund",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "account_id": account_id,
                    "client": client,
                    "client_token": client_token,
                    "payment_id": payment_id,
                    "reason": reason,
                    "enterprise_id": enterprise_id,
                    "value_to_refund": value_to_refund,
                },
                payment_refund_params.PaymentRefundParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentRefundResponse,
        )


class PaymentsResourceWithRawResponse:
    def __init__(self, payments: PaymentsResource) -> None:
        self._payments = payments

        self.list = to_raw_response_wrapper(
            payments.list,
        )
        self.add_alternative = to_raw_response_wrapper(
            payments.add_alternative,
        )
        self.add_credit_card = to_raw_response_wrapper(
            payments.add_credit_card,
        )
        self.add_external = to_raw_response_wrapper(
            payments.add_external,
        )
        self.refund = to_raw_response_wrapper(
            payments.refund,
        )


class AsyncPaymentsResourceWithRawResponse:
    def __init__(self, payments: AsyncPaymentsResource) -> None:
        self._payments = payments

        self.list = async_to_raw_response_wrapper(
            payments.list,
        )
        self.add_alternative = async_to_raw_response_wrapper(
            payments.add_alternative,
        )
        self.add_credit_card = async_to_raw_response_wrapper(
            payments.add_credit_card,
        )
        self.add_external = async_to_raw_response_wrapper(
            payments.add_external,
        )
        self.refund = async_to_raw_response_wrapper(
            payments.refund,
        )


class PaymentsResourceWithStreamingResponse:
    def __init__(self, payments: PaymentsResource) -> None:
        self._payments = payments

        self.list = to_streamed_response_wrapper(
            payments.list,
        )
        self.add_alternative = to_streamed_response_wrapper(
            payments.add_alternative,
        )
        self.add_credit_card = to_streamed_response_wrapper(
            payments.add_credit_card,
        )
        self.add_external = to_streamed_response_wrapper(
            payments.add_external,
        )
        self.refund = to_streamed_response_wrapper(
            payments.refund,
        )


class AsyncPaymentsResourceWithStreamingResponse:
    def __init__(self, payments: AsyncPaymentsResource) -> None:
        self._payments = payments

        self.list = async_to_streamed_response_wrapper(
            payments.list,
        )
        self.add_alternative = async_to_streamed_response_wrapper(
            payments.add_alternative,
        )
        self.add_credit_card = async_to_streamed_response_wrapper(
            payments.add_credit_card,
        )
        self.add_external = async_to_streamed_response_wrapper(
            payments.add_external,
        )
        self.refund = async_to_streamed_response_wrapper(
            payments.refund,
        )
