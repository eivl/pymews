# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from .bills import (
    BillsResource,
    AsyncBillsResource,
    BillsResourceWithRawResponse,
    AsyncBillsResourceWithRawResponse,
    BillsResourceWithStreamingResponse,
    AsyncBillsResourceWithStreamingResponse,
)
from .rates import (
    RatesResource,
    AsyncRatesResource,
    RatesResourceWithRawResponse,
    AsyncRatesResourceWithRawResponse,
    RatesResourceWithStreamingResponse,
    AsyncRatesResourceWithStreamingResponse,
)
from .tasks import (
    TasksResource,
    AsyncTasksResource,
    TasksResourceWithRawResponse,
    AsyncTasksResourceWithRawResponse,
    TasksResourceWithStreamingResponse,
    AsyncTasksResourceWithStreamingResponse,
)
from .exports import (
    ExportsResource,
    AsyncExportsResource,
    ExportsResourceWithRawResponse,
    AsyncExportsResourceWithRawResponse,
    ExportsResourceWithStreamingResponse,
    AsyncExportsResourceWithStreamingResponse,
)
from .accounts import (
    AccountsResource,
    AsyncAccountsResource,
    AccountsResourceWithRawResponse,
    AsyncAccountsResourceWithRawResponse,
    AccountsResourceWithStreamingResponse,
    AsyncAccountsResourceWithStreamingResponse,
)
from .commands import (
    CommandsResource,
    AsyncCommandsResource,
    CommandsResourceWithRawResponse,
    AsyncCommandsResourceWithRawResponse,
    CommandsResourceWithStreamingResponse,
    AsyncCommandsResourceWithStreamingResponse,
)
from .messages import (
    MessagesResource,
    AsyncMessagesResource,
    MessagesResourceWithRawResponse,
    AsyncMessagesResourceWithRawResponse,
    MessagesResourceWithStreamingResponse,
    AsyncMessagesResourceWithStreamingResponse,
)
from .payments import (
    PaymentsResource,
    AsyncPaymentsResource,
    PaymentsResourceWithRawResponse,
    AsyncPaymentsResourceWithRawResponse,
    PaymentsResourceWithStreamingResponse,
    AsyncPaymentsResourceWithStreamingResponse,
)
from .products import (
    ProductsResource,
    AsyncProductsResource,
    ProductsResourceWithRawResponse,
    AsyncProductsResourceWithRawResponse,
    ProductsResourceWithStreamingResponse,
    AsyncProductsResourceWithStreamingResponse,
)
from .services import (
    ServicesResource,
    AsyncServicesResource,
    ServicesResourceWithRawResponse,
    AsyncServicesResourceWithRawResponse,
    ServicesResourceWithStreamingResponse,
    AsyncServicesResourceWithStreamingResponse,
)
from .vouchers import (
    VouchersResource,
    AsyncVouchersResource,
    VouchersResourceWithRawResponse,
    AsyncVouchersResourceWithRawResponse,
    VouchersResourceWithStreamingResponse,
    AsyncVouchersResourceWithStreamingResponse,
)
from .addresses import (
    AddressesResource,
    AsyncAddressesResource,
    AddressesResourceWithRawResponse,
    AsyncAddressesResourceWithRawResponse,
    AddressesResourceWithStreamingResponse,
    AsyncAddressesResourceWithStreamingResponse,
)
from .companies import (
    CompaniesResource,
    AsyncCompaniesResource,
    CompaniesResourceWithRawResponse,
    AsyncCompaniesResourceWithRawResponse,
    CompaniesResourceWithStreamingResponse,
    AsyncCompaniesResourceWithStreamingResponse,
)
from .customers import (
    CustomersResource,
    AsyncCustomersResource,
    CustomersResourceWithRawResponse,
    AsyncCustomersResourceWithRawResponse,
    CustomersResourceWithStreamingResponse,
    AsyncCustomersResourceWithStreamingResponse,
)
from .languages import (
    LanguagesResource,
    AsyncLanguagesResource,
    LanguagesResourceWithRawResponse,
    AsyncLanguagesResourceWithRawResponse,
    LanguagesResourceWithStreamingResponse,
    AsyncLanguagesResourceWithStreamingResponse,
)
from .resources import (
    ResourcesResource,
    AsyncResourcesResource,
    ResourcesResourceWithRawResponse,
    AsyncResourcesResourceWithRawResponse,
    ResourcesResourceWithStreamingResponse,
    AsyncResourcesResourceWithStreamingResponse,
)
from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ....._compat import cached_property
from .order_items import (
    OrderItemsResource,
    AsyncOrderItemsResource,
    OrderItemsResourceWithRawResponse,
    AsyncOrderItemsResourceWithRawResponse,
    OrderItemsResourceWithStreamingResponse,
    AsyncOrderItemsResourceWithStreamingResponse,
)
from .credit_cards import (
    CreditCardsResource,
    AsyncCreditCardsResource,
    CreditCardsResourceWithRawResponse,
    AsyncCreditCardsResourceWithRawResponse,
    CreditCardsResourceWithStreamingResponse,
    AsyncCreditCardsResourceWithStreamingResponse,
)
from .reservations import (
    ReservationsResource,
    AsyncReservationsResource,
    ReservationsResourceWithRawResponse,
    AsyncReservationsResourceWithRawResponse,
    ReservationsResourceWithStreamingResponse,
    AsyncReservationsResourceWithStreamingResponse,
)
from .restrictions import (
    RestrictionsResource,
    AsyncRestrictionsResource,
    RestrictionsResourceWithRawResponse,
    AsyncRestrictionsResourceWithRawResponse,
    RestrictionsResourceWithStreamingResponse,
    AsyncRestrictionsResourceWithStreamingResponse,
)
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .account_notes import (
    AccountNotesResource,
    AsyncAccountNotesResource,
    AccountNotesResourceWithRawResponse,
    AsyncAccountNotesResourceWithRawResponse,
    AccountNotesResourceWithStreamingResponse,
    AsyncAccountNotesResourceWithStreamingResponse,
)
from .loyalty_tiers import (
    LoyaltyTiersResource,
    AsyncLoyaltyTiersResource,
    LoyaltyTiersResourceWithRawResponse,
    AsyncLoyaltyTiersResourceWithRawResponse,
    LoyaltyTiersResourceWithStreamingResponse,
    AsyncLoyaltyTiersResourceWithStreamingResponse,
)
from .routing_rules import (
    RoutingRulesResource,
    AsyncRoutingRulesResource,
    RoutingRulesResourceWithRawResponse,
    AsyncRoutingRulesResourceWithRawResponse,
    RoutingRulesResourceWithStreamingResponse,
    AsyncRoutingRulesResourceWithStreamingResponse,
)
from .voucher_codes import (
    VoucherCodesResource,
    AsyncVoucherCodesResource,
    VoucherCodesResourceWithRawResponse,
    AsyncVoucherCodesResourceWithRawResponse,
    VoucherCodesResourceWithStreamingResponse,
    AsyncVoucherCodesResourceWithStreamingResponse,
)
from .message_threads import (
    MessageThreadsResource,
    AsyncMessageThreadsResource,
    MessageThreadsResourceWithRawResponse,
    AsyncMessageThreadsResourceWithRawResponse,
    MessageThreadsResourceWithStreamingResponse,
    AsyncMessageThreadsResourceWithStreamingResponse,
)
from .resource_blocks import (
    ResourceBlocksResource,
    AsyncResourceBlocksResource,
    ResourceBlocksResourceWithRawResponse,
    AsyncResourceBlocksResourceWithRawResponse,
    ResourceBlocksResourceWithStreamingResponse,
    AsyncResourceBlocksResourceWithStreamingResponse,
)
from ....._base_client import make_request_options
from .accounting_items import (
    AccountingItemsResource,
    AsyncAccountingItemsResource,
    AccountingItemsResourceWithRawResponse,
    AsyncAccountingItemsResourceWithRawResponse,
    AccountingItemsResourceWithStreamingResponse,
    AsyncAccountingItemsResourceWithStreamingResponse,
)
from .loyalty_programs import (
    LoyaltyProgramsResource,
    AsyncLoyaltyProgramsResource,
    LoyaltyProgramsResourceWithRawResponse,
    AsyncLoyaltyProgramsResourceWithRawResponse,
    LoyaltyProgramsResourceWithStreamingResponse,
    AsyncLoyaltyProgramsResourceWithStreamingResponse,
)
from .payment_requests import (
    PaymentRequestsResource,
    AsyncPaymentRequestsResource,
    PaymentRequestsResourceWithRawResponse,
    AsyncPaymentRequestsResourceWithRawResponse,
    PaymentRequestsResourceWithStreamingResponse,
    AsyncPaymentRequestsResourceWithStreamingResponse,
)
from .company_contracts import (
    CompanyContractsResource,
    AsyncCompanyContractsResource,
    CompanyContractsResourceWithRawResponse,
    AsyncCompanyContractsResourceWithRawResponse,
    CompanyContractsResourceWithStreamingResponse,
    AsyncCompanyContractsResourceWithStreamingResponse,
)
from .identity_documents import (
    IdentityDocumentsResource,
    AsyncIdentityDocumentsResource,
    IdentityDocumentsResourceWithRawResponse,
    AsyncIdentityDocumentsResourceWithRawResponse,
    IdentityDocumentsResourceWithStreamingResponse,
    AsyncIdentityDocumentsResourceWithStreamingResponse,
)
from .availability_blocks import (
    AvailabilityBlocksResource,
    AsyncAvailabilityBlocksResource,
    AvailabilityBlocksResourceWithRawResponse,
    AsyncAvailabilityBlocksResourceWithRawResponse,
    AvailabilityBlocksResourceWithStreamingResponse,
    AsyncAvailabilityBlocksResourceWithStreamingResponse,
)
from .loyalty_memberships import (
    LoyaltyMembershipsResource,
    AsyncLoyaltyMembershipsResource,
    LoyaltyMembershipsResourceWithRawResponse,
    AsyncLoyaltyMembershipsResourceWithRawResponse,
    LoyaltyMembershipsResourceWithStreamingResponse,
    AsyncLoyaltyMembershipsResourceWithStreamingResponse,
)
from .service_order_notes import (
    ServiceOrderNotesResource,
    AsyncServiceOrderNotesResource,
    ServiceOrderNotesResourceWithRawResponse,
    AsyncServiceOrderNotesResourceWithRawResponse,
    ServiceOrderNotesResourceWithStreamingResponse,
    AsyncServiceOrderNotesResourceWithStreamingResponse,
)
from .cancellation_policies import (
    CancellationPoliciesResource,
    AsyncCancellationPoliciesResource,
    CancellationPoliciesResourceWithRawResponse,
    AsyncCancellationPoliciesResourceWithRawResponse,
    CancellationPoliciesResourceWithStreamingResponse,
    AsyncCancellationPoliciesResourceWithStreamingResponse,
)
from .resource_access_tokens import (
    ResourceAccessTokensResource,
    AsyncResourceAccessTokensResource,
    ResourceAccessTokensResourceWithRawResponse,
    AsyncResourceAccessTokensResourceWithRawResponse,
    ResourceAccessTokensResourceWithStreamingResponse,
    AsyncResourceAccessTokensResourceWithStreamingResponse,
)
from .....types.api.connector import (
    v1_add_order_params,
    v1_list_rules_params,
    v1_list_devices_params,
    v1_list_outlets_params,
    v1_list_sources_params,
    v1_list_cashiers_params,
    v1_list_counters_params,
    v1_get_image_urls_params,
    v1_list_countries_params,
    v1_list_taxations_params,
    v1_add_outlet_bill_params,
    v1_list_currencies_params,
    v1_list_departments_params,
    v1_list_enterprises_params,
    v1_list_rate_groups_params,
    v1_get_configuration_params,
    v1_list_outlet_items_params,
    v1_list_age_categories_params,
    v1_list_companionships_params,
    v1_list_exchange_rates_params,
    v1_list_ledger_balances_params,
    v1_list_tax_environments_params,
    v1_list_business_segments_params,
    v1_list_resource_features_params,
    v1_list_product_categories_params,
    v1_list_reservation_groups_params,
    v1_list_resource_categories_params,
    v1_list_cashier_transactions_params,
    v1_get_all_source_assignments_params,
    v1_list_accounting_categories_params,
    v1_list_product_service_orders_params,
    v1_list_availability_adjustments_params,
    v1_list_resource_feature_assignments_params,
    v1_list_resource_category_assignments_params,
    v1_list_preauthorizations_by_customers_params,
    v1_get_all_source_assignments_2024_09_20_params,
    v1_list_resource_category_image_assignments_params,
)
from .service_overbooking_limits import (
    ServiceOverbookingLimitsResource,
    AsyncServiceOverbookingLimitsResource,
    ServiceOverbookingLimitsResourceWithRawResponse,
    AsyncServiceOverbookingLimitsResourceWithRawResponse,
    ServiceOverbookingLimitsResourceWithStreamingResponse,
    AsyncServiceOverbookingLimitsResourceWithStreamingResponse,
)
from .....types.api.connector.v1_add_order_response import V1AddOrderResponse
from .....types.api.connector.v1_list_rules_response import V1ListRulesResponse
from .....types.api.connector.v1_list_devices_response import V1ListDevicesResponse
from .....types.api.connector.v1_list_outlets_response import V1ListOutletsResponse
from .....types.api.connector.v1_list_sources_response import V1ListSourcesResponse
from .....types.api.connector.v1_list_cashiers_response import V1ListCashiersResponse
from .....types.api.connector.v1_list_counters_response import V1ListCountersResponse
from .....types.api.connector.v1_get_image_urls_response import V1GetImageURLsResponse
from .....types.api.connector.v1_list_countries_response import V1ListCountriesResponse
from .....types.api.connector.v1_list_taxations_response import V1ListTaxationsResponse
from .....types.api.connector.v1_add_outlet_bill_response import V1AddOutletBillResponse
from .....types.api.connector.v1_list_currencies_response import V1ListCurrenciesResponse
from .....types.api.connector.v1_list_departments_response import V1ListDepartmentsResponse
from .....types.api.connector.v1_list_enterprises_response import V1ListEnterprisesResponse
from .....types.api.connector.v1_list_rate_groups_response import V1ListRateGroupsResponse
from .....types.api.connector.v1_get_configuration_response import V1GetConfigurationResponse
from .....types.api.connector.v1_list_outlet_items_response import V1ListOutletItemsResponse
from .....types.api.connector.v1_list_age_categories_response import V1ListAgeCategoriesResponse
from .....types.api.connector.v1_list_companionships_response import V1ListCompanionshipsResponse
from .....types.api.connector.v1_list_exchange_rates_response import V1ListExchangeRatesResponse
from .....types.api.connector.v1_list_ledger_balances_response import V1ListLedgerBalancesResponse
from .....types.api.connector.v1_list_tax_environments_response import V1ListTaxEnvironmentsResponse
from .....types.api.connector.v1_list_business_segments_response import V1ListBusinessSegmentsResponse
from .....types.api.connector.v1_list_resource_features_response import V1ListResourceFeaturesResponse
from .....types.api.connector.v1_list_product_categories_response import V1ListProductCategoriesResponse
from .....types.api.connector.v1_list_reservation_groups_response import V1ListReservationGroupsResponse
from .....types.api.connector.v1_list_resource_categories_response import V1ListResourceCategoriesResponse
from .....types.api.connector.v1_list_cashier_transactions_response import V1ListCashierTransactionsResponse
from .....types.api.connector.v1_get_all_source_assignments_response import V1GetAllSourceAssignmentsResponse
from .....types.api.connector.v1_list_accounting_categories_response import V1ListAccountingCategoriesResponse
from .....types.api.connector.v1_list_product_service_orders_response import V1ListProductServiceOrdersResponse
from .....types.api.connector.v1_list_availability_adjustments_response import V1ListAvailabilityAdjustmentsResponse
from .....types.api.connector.v1_list_resource_feature_assignments_response import (
    V1ListResourceFeatureAssignmentsResponse,
)
from .....types.api.connector.v1_list_resource_category_assignments_response import (
    V1ListResourceCategoryAssignmentsResponse,
)
from .....types.api.connector.v1_list_preauthorizations_by_customers_response import (
    V1ListPreauthorizationsByCustomersResponse,
)
from .....types.api.connector.v1_get_all_source_assignments_2024_09_20_response import (
    V1GetAllSourceAssignments2024_09_20Response,
)
from .....types.api.connector.v1_list_resource_category_image_assignments_response import (
    V1ListResourceCategoryImageAssignmentsResponse,
)

__all__ = ["V1Resource", "AsyncV1Resource"]


class V1Resource(SyncAPIResource):
    @cached_property
    def account_notes(self) -> AccountNotesResource:
        return AccountNotesResource(self._client)

    @cached_property
    def accounting_items(self) -> AccountingItemsResource:
        return AccountingItemsResource(self._client)

    @cached_property
    def accounts(self) -> AccountsResource:
        return AccountsResource(self._client)

    @cached_property
    def addresses(self) -> AddressesResource:
        return AddressesResource(self._client)

    @cached_property
    def availability_blocks(self) -> AvailabilityBlocksResource:
        return AvailabilityBlocksResource(self._client)

    @cached_property
    def bills(self) -> BillsResource:
        return BillsResource(self._client)

    @cached_property
    def cancellation_policies(self) -> CancellationPoliciesResource:
        return CancellationPoliciesResource(self._client)

    @cached_property
    def commands(self) -> CommandsResource:
        return CommandsResource(self._client)

    @cached_property
    def companies(self) -> CompaniesResource:
        return CompaniesResource(self._client)

    @cached_property
    def company_contracts(self) -> CompanyContractsResource:
        return CompanyContractsResource(self._client)

    @cached_property
    def credit_cards(self) -> CreditCardsResource:
        return CreditCardsResource(self._client)

    @cached_property
    def customers(self) -> CustomersResource:
        return CustomersResource(self._client)

    @cached_property
    def exports(self) -> ExportsResource:
        return ExportsResource(self._client)

    @cached_property
    def identity_documents(self) -> IdentityDocumentsResource:
        return IdentityDocumentsResource(self._client)

    @cached_property
    def languages(self) -> LanguagesResource:
        return LanguagesResource(self._client)

    @cached_property
    def loyalty_memberships(self) -> LoyaltyMembershipsResource:
        return LoyaltyMembershipsResource(self._client)

    @cached_property
    def loyalty_programs(self) -> LoyaltyProgramsResource:
        return LoyaltyProgramsResource(self._client)

    @cached_property
    def loyalty_tiers(self) -> LoyaltyTiersResource:
        return LoyaltyTiersResource(self._client)

    @cached_property
    def message_threads(self) -> MessageThreadsResource:
        return MessageThreadsResource(self._client)

    @cached_property
    def messages(self) -> MessagesResource:
        return MessagesResource(self._client)

    @cached_property
    def order_items(self) -> OrderItemsResource:
        return OrderItemsResource(self._client)

    @cached_property
    def payment_requests(self) -> PaymentRequestsResource:
        return PaymentRequestsResource(self._client)

    @cached_property
    def payments(self) -> PaymentsResource:
        return PaymentsResource(self._client)

    @cached_property
    def products(self) -> ProductsResource:
        return ProductsResource(self._client)

    @cached_property
    def rates(self) -> RatesResource:
        return RatesResource(self._client)

    @cached_property
    def reservations(self) -> ReservationsResource:
        return ReservationsResource(self._client)

    @cached_property
    def resource_access_tokens(self) -> ResourceAccessTokensResource:
        return ResourceAccessTokensResource(self._client)

    @cached_property
    def resource_blocks(self) -> ResourceBlocksResource:
        return ResourceBlocksResource(self._client)

    @cached_property
    def resources(self) -> ResourcesResource:
        return ResourcesResource(self._client)

    @cached_property
    def restrictions(self) -> RestrictionsResource:
        return RestrictionsResource(self._client)

    @cached_property
    def routing_rules(self) -> RoutingRulesResource:
        return RoutingRulesResource(self._client)

    @cached_property
    def service_order_notes(self) -> ServiceOrderNotesResource:
        return ServiceOrderNotesResource(self._client)

    @cached_property
    def service_overbooking_limits(self) -> ServiceOverbookingLimitsResource:
        return ServiceOverbookingLimitsResource(self._client)

    @cached_property
    def services(self) -> ServicesResource:
        return ServicesResource(self._client)

    @cached_property
    def tasks(self) -> TasksResource:
        return TasksResource(self._client)

    @cached_property
    def voucher_codes(self) -> VoucherCodesResource:
        return VoucherCodesResource(self._client)

    @cached_property
    def vouchers(self) -> VouchersResource:
        return VouchersResource(self._client)

    @cached_property
    def with_raw_response(self) -> V1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return V1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return V1ResourceWithStreamingResponse(self)

    def add_order(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        service_id: str,
        account_id: Optional[str] | NotGiven = NOT_GIVEN,
        bill_id: Optional[str] | NotGiven = NOT_GIVEN,
        business_segment_id: Optional[str] | NotGiven = NOT_GIVEN,
        consumption_utc: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        customer_id: Optional[str] | NotGiven = NOT_GIVEN,
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        items: Optional[Iterable[v1_add_order_params.Item]] | NotGiven = NOT_GIVEN,
        linked_reservation_id: Optional[str] | NotGiven = NOT_GIVEN,
        notes: Optional[str] | NotGiven = NOT_GIVEN,
        options: Optional[v1_add_order_params.Options] | NotGiven = NOT_GIVEN,
        product_orders: Optional[Iterable[v1_add_order_params.ProductOrder]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1AddOrderResponse:
        """Creates a new order, with the specified products and items.

        If the time of
        consumption is specified, it must be either in the future or within the Editable
        History Interval for the enterprise. Compared to a stay service order (i.e. a
        reservation), which is consumed over certain span of time, a product service
        order is consumed at a single point in time. Note this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          service_id: Identifier of the
              [Service](https://mews-systems.gitbook.io/connector-api/operations/services/#service)
              to be ordered.

          account_id: Identifier of the
              [Customer](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer)
              or
              [Company](https://mews-systems.gitbook.io/connector-api/operations/companies/#company)
              to be charged. Company billing may not be enabled for your integration.

          bill_id: Identifier of the
              [Bill](https://mews-systems.gitbook.io/connector-api/operations/bills/#bill) to
              which the created order will be assigned. The bill needs to be issued to the
              same account as the order.

          consumption_utc: Date and time of the order consumption in UTC timezone in ISO 8601 format. If
              not specified, current date and time is used. Please note, as order consumption
              is one-time event, the optional parameters StartUtc and EndUtc in
              [Product order parameters](https://mews-systems.gitbook.io/connector-api/operations/#product-order-parameters)
              should not be used.

          customer_id: Identifier of the
              [Customer](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer)
              to be charged. **Deprecated!**

          enterprise_id: Unique identifier of the
              [Enterprise](https://mews-systems.gitbook.io/connector-api/operations/enterprises/#enterprise).
              Required when using a
              [Portfolio Access Token](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          items: Parameters of the ordered custom items.

          notes: Additional notes of the order.

          product_orders: Parameters of the ordered products.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/orders/add",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "service_id": service_id,
                    "account_id": account_id,
                    "bill_id": bill_id,
                    "business_segment_id": business_segment_id,
                    "consumption_utc": consumption_utc,
                    "customer_id": customer_id,
                    "enterprise_id": enterprise_id,
                    "items": items,
                    "linked_reservation_id": linked_reservation_id,
                    "notes": notes,
                    "options": options,
                    "product_orders": product_orders,
                },
                v1_add_order_params.V1AddOrderParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1AddOrderResponse,
        )

    def add_outlet_bill(
        self,
        *,
        access_token: str,
        bills: Iterable[v1_add_outlet_bill_params.Bill],
        client: str,
        client_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1AddOutletBillResponse:
        """
        Adds new outlet bills with their items.

        Args:
          access_token: Access token of the client application.

          bills: The new outlet bills.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/outletBills/add",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "bills": bills,
                    "client": client,
                    "client_token": client_token,
                },
                v1_add_outlet_bill_params.V1AddOutletBillParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1AddOutletBillResponse,
        )

    def get_all_source_assignments(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: v1_get_all_source_assignments_params.Limitation,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        reservation_group_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[v1_get_all_source_assignments_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1GetAllSourceAssignmentsResponse:
        """Returns all Sources assigned to a Reservation group.

        Each reservation group can
        have multiple sources. Note this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          reservation_group_ids: Unique identifiers of the `Reservation group`.

          updated_utc: Interval of `Reservation group` last update date and time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/sourceAssignments/getAll",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "enterprise_ids": enterprise_ids,
                    "reservation_group_ids": reservation_group_ids,
                    "updated_utc": updated_utc,
                },
                v1_get_all_source_assignments_params.V1GetAllSourceAssignmentsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1GetAllSourceAssignmentsResponse,
        )

    def get_all_source_assignments_2024_09_20(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: v1_get_all_source_assignments_2024_09_20_params.Limitation,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        reservation_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1GetAllSourceAssignments2024_09_20Response:
        """Returns all Sources assigned to Reservations.

        Each reservation can have multiple
        sources. Note this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          reservation_ids: Unique identifiers of `Reservation`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/sourceAssignments/getAll/2024-09-20",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "enterprise_ids": enterprise_ids,
                    "reservation_ids": reservation_ids,
                },
                v1_get_all_source_assignments_2024_09_20_params.V1GetAllSourceAssignments2024_09_20Params,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1GetAllSourceAssignments2024_09_20Response,
        )

    def get_configuration(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1GetConfigurationResponse:
        """Returns the enterprise configuration.

        For single-enterprise Access Tokens, this
        is the enterprise associated with the token. For
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
        use the `EnterpriseId` parameter to specify which enterprise you want the
        configuration for. In the case of service scoped integrations, the operation
        returns the configuration associated with both the enterprise and the bookable
        service linked to the token.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          enterprise_id: Unique identifier of the
              [Enterprise](https://mews-systems.gitbook.io/connector-api/operations/#enterprise),
              defaults to the enterprise associated with the given access token.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/configuration/get",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "enterprise_id": enterprise_id,
                },
                v1_get_configuration_params.V1GetConfigurationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1GetConfigurationResponse,
        )

    def get_image_urls(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        images: Iterable[v1_get_image_urls_params.Image],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1GetImageURLsResponse:
        """
        Returns URLs of the specified images.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          images: Parameters of images whose URLs should be returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/images/getUrls",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "images": images,
                },
                v1_get_image_urls_params.V1GetImageURLsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1GetImageURLsResponse,
        )

    def list_accounting_categories(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: v1_list_accounting_categories_params.Limitation,
        accounting_category_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        activity_states: Optional[List[Literal["Deleted", "Active"]]] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[v1_list_accounting_categories_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1ListAccountingCategoriesResponse:
        """
        Returns all accounting categories of the enterprise associated with the
        connector integration. Note this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          accounting_category_ids: Unique identifiers of the requested
              [Accounting categories](https://mews-systems.gitbook.io/connector-api/operations/#accounting-category).

          activity_states: Whether to return only active, only deleted or both records.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          updated_utc: Last update date and time of the accounting category in UTC timezone in ISO 8601
              format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/accountingCategories/getAll",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "accounting_category_ids": accounting_category_ids,
                    "activity_states": activity_states,
                    "enterprise_ids": enterprise_ids,
                    "updated_utc": updated_utc,
                },
                v1_list_accounting_categories_params.V1ListAccountingCategoriesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListAccountingCategoriesResponse,
        )

    def list_age_categories(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: v1_list_age_categories_params.Limitation,
        activity_states: Optional[List[Literal["Deleted", "Active"]]] | NotGiven = NOT_GIVEN,
        age_category_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        service_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[v1_list_age_categories_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1ListAgeCategoriesResponse:
        """
        Returns all age categories filtered by
        [Service](https://mews-systems.gitbook.io/connector-api/operations/services/#service).
        Note this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          activity_states: Whether to return only active, only deleted or both records.

          age_category_ids: Unique identifiers of
              [Age categories](https://mews-systems.gitbook.io/connector-api/operations/#age-category).

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          service_ids: Unique identifiers of `Services` associated with the age categories. If not
              provided, defaults to all bookable services.

          updated_utc: Interval in which the age category was updated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/ageCategories/getAll",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "activity_states": activity_states,
                    "age_category_ids": age_category_ids,
                    "enterprise_ids": enterprise_ids,
                    "service_ids": service_ids,
                    "updated_utc": updated_utc,
                },
                v1_list_age_categories_params.V1ListAgeCategoriesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListAgeCategoriesResponse,
        )

    def list_availability_adjustments(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: v1_list_availability_adjustments_params.Limitation,
        activity_states: Optional[List[Literal["Deleted", "Active"]]] | NotGiven = NOT_GIVEN,
        availability_adjustment_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[v1_list_availability_adjustments_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1ListAvailabilityAdjustmentsResponse:
        """Returns all availability adjustments.

        Note this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          activity_states: Whether to return only active, only deleted, or both types of record. If not
              specified, only active records will be returned.

          availability_adjustment_ids: Unique identifiers of the requested
              [Availability adjustments](https://mews-systems.gitbook.io/connector-api/operations/#availability-adjustment).

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          updated_utc: Interval in which the availability adjustments were updated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/availabilityAdjustments/getAll",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "activity_states": activity_states,
                    "availability_adjustment_ids": availability_adjustment_ids,
                    "enterprise_ids": enterprise_ids,
                    "updated_utc": updated_utc,
                },
                v1_list_availability_adjustments_params.V1ListAvailabilityAdjustmentsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListAvailabilityAdjustmentsResponse,
        )

    def list_business_segments(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: v1_list_business_segments_params.Limitation,
        activity_states: Optional[List[Literal["Deleted", "Active"]]] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        service_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[v1_list_business_segments_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1ListBusinessSegmentsResponse:
        """Returns all business segments.

        This operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          activity_states: Whether to return only active, only deleted or both records.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          ids: Unique identifiers of the requested `Business segment`.

          service_ids: Unique identifiers of the `Services` from which the business segments are
              requested.

          updated_utc: Interval of `Business segment` last update date and time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/businessSegments/getAll",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "activity_states": activity_states,
                    "enterprise_ids": enterprise_ids,
                    "ids": ids,
                    "service_ids": service_ids,
                    "updated_utc": updated_utc,
                },
                v1_list_business_segments_params.V1ListBusinessSegmentsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListBusinessSegmentsResponse,
        )

    def list_cashier_transactions(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: v1_list_cashier_transactions_params.Limitation,
        cashier_transaction_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        created_utc: Optional[v1_list_cashier_transactions_params.CreatedUtc] | NotGiven = NOT_GIVEN,
        end_utc: Optional[str] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        start_utc: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1ListCashierTransactionsResponse:
        """Returns all cashier transactions created within the specified interval.

        Note
        this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/cashierTransactions/getAll",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "cashier_transaction_ids": cashier_transaction_ids,
                    "created_utc": created_utc,
                    "end_utc": end_utc,
                    "enterprise_ids": enterprise_ids,
                    "start_utc": start_utc,
                },
                v1_list_cashier_transactions_params.V1ListCashierTransactionsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListCashierTransactionsResponse,
        )

    def list_cashiers(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: v1_list_cashiers_params.Limitation,
        activity_states: Optional[List[Literal["Deleted", "Active"]]] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[v1_list_cashiers_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1ListCashiersResponse:
        """Returns all cashiers.

        Note this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          activity_states: Whether to return only active, only deleted or both records.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          ids: Unique identifiers of the requested
              [Cashier](https://mews-systems.gitbook.io/connector-api/operations/#cashier).

          updated_utc: Interval in which `Cashier` was updated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/cashiers/getAll",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "activity_states": activity_states,
                    "enterprise_ids": enterprise_ids,
                    "ids": ids,
                    "updated_utc": updated_utc,
                },
                v1_list_cashiers_params.V1ListCashiersParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListCashiersResponse,
        )

    def list_companionships(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        extent: v1_list_companionships_params.Extent,
        limitation: v1_list_companionships_params.Limitation,
        companionship_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        customer_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        reservation_group_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        reservation_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[v1_list_companionships_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1ListCompanionshipsResponse:
        """
        Returns all companionships based on customers, reservations or reservation
        groups. One of them must be specified in the request. Note this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          extent: Extent of data to be returned. E.g. it is possible to specify that together with
              the companionships, customers, reservations, and reservation groups should be
              also returned.

          limitation: Limitation on the quantity of data returned.

          companionship_ids: Unique identifiers of
              [Companionship](https://mews-systems.gitbook.io/connector-api/operations/#companionship).

          customer_ids: Unique identifiers of
              [Customers](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer).

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          reservation_group_ids: Unique identifiers of
              [Reservation groups](https://mews-systems.gitbook.io/connector-api/operations/reservations/#reservation-group).

          reservation_ids: Unique identifiers of reservations.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/companionships/getAll",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "extent": extent,
                    "limitation": limitation,
                    "companionship_ids": companionship_ids,
                    "customer_ids": customer_ids,
                    "enterprise_ids": enterprise_ids,
                    "reservation_group_ids": reservation_group_ids,
                    "reservation_ids": reservation_ids,
                    "updated_utc": updated_utc,
                },
                v1_list_companionships_params.V1ListCompanionshipsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListCompanionshipsResponse,
        )

    def list_counters(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: v1_list_counters_params.Limitation,
        counter_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        type: Optional[
            Literal[
                "Counter",
                "AccountingCounter",
                "AvailabilityBlockCounter",
                "BillCounter",
                "BillPreviewCounter",
                "FiscalCounter",
                "ProformaCounter",
                "RegistrationCardCounter",
                "ServiceOrderCounter",
                "CorrectionBillCounter",
                "PaymentConfirmationBillCounter",
                "CreditNoteBillCounter",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        updated_utc: Optional[v1_list_counters_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1ListCountersResponse:
        """
        Returns all counters of an enterprise associated with the connector integration.
        Note this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          type: Type of the counter. If not specified, the operation returns all types.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/counters/getAll",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "counter_ids": counter_ids,
                    "enterprise_ids": enterprise_ids,
                    "type": type,
                    "updated_utc": updated_utc,
                },
                v1_list_counters_params.V1ListCountersParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListCountersResponse,
        )

    def list_countries(
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
    ) -> V1ListCountriesResponse:
        """
        Returns all countries supported by the API.

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
            "/api/connector/v1/countries/getAll",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                },
                v1_list_countries_params.V1ListCountriesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListCountriesResponse,
        )

    def list_currencies(
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
    ) -> V1ListCurrenciesResponse:
        """
        Returns all currencies supported by the API.

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
            "/api/connector/v1/currencies/getAll",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                },
                v1_list_currencies_params.V1ListCurrenciesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListCurrenciesResponse,
        )

    def list_departments(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: v1_list_departments_params.Limitation,
        department_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[v1_list_departments_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1ListDepartmentsResponse:
        """
        Returns all departments of an enterprise associated with the connector
        integration. Note this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          department_ids: Unique identifiers of
              [Department](https://mews-systems.gitbook.io/connector-api/operations/#department).

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/departments/getAll",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "department_ids": department_ids,
                    "enterprise_ids": enterprise_ids,
                    "updated_utc": updated_utc,
                },
                v1_list_departments_params.V1ListDepartmentsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListDepartmentsResponse,
        )

    def list_devices(
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
    ) -> V1ListDevicesResponse:
        """
        Returns all devices in the enterprise.

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
            "/api/connector/v1/devices/getAll",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                },
                v1_list_devices_params.V1ListDevicesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListDevicesResponse,
        )

    def list_enterprises(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: v1_list_enterprises_params.Limitation,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        external_identifiers: Optional[List[str]] | NotGiven = NOT_GIVEN,
        linked_utc: Optional[v1_list_enterprises_params.LinkedUtc] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[v1_list_enterprises_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1ListEnterprisesResponse:
        """
        Returns all enterprises within scope of the `Access Token`, optionally filtered
        by enterprise identifiers and external identifiers. Note this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          enterprise_ids: Unique identifiers of the
              [Enterprises](https://mews-systems.gitbook.io/connector-api/operations/#enterprise).
              If not specified, all enterprises within scope of the Access Token are returned.

          external_identifiers: Identifiers of the
              [Enterprise](https://mews-systems.gitbook.io/connector-api/operations/#enterprise)
              from external system.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/enterprises/getAll",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "enterprise_ids": enterprise_ids,
                    "external_identifiers": external_identifiers,
                    "linked_utc": linked_utc,
                    "updated_utc": updated_utc,
                },
                v1_list_enterprises_params.V1ListEnterprisesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListEnterprisesResponse,
        )

    def list_exchange_rates(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1ListExchangeRatesResponse:
        """
        Returns all available exchange rates among currencies of the
        [Enterprise](https://mews-systems.gitbook.io/connector-api/operations/configuration/#enterprise).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          enterprise_ids: Unique identifiers of the
              [Enterprises](https://mews-systems.gitbook.io/connector-api/operations/configuration/#enterprise).
              If not specified, the operation returns the exchange rates for all enterprises
              within scope of the Access Token.

          ids: Unique identifiers of the Exchange Rates. If not specified, the operation
              returns all exchange rates.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/exchangeRates/getAll",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "enterprise_ids": enterprise_ids,
                    "ids": ids,
                },
                v1_list_exchange_rates_params.V1ListExchangeRatesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListExchangeRatesResponse,
        )

    def list_ledger_balances(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        date: v1_list_ledger_balances_params.Date,
        ledger_types: List[Literal["Revenue", "Tax", "Payment", "Deposit", "Guest", "City"]],
        limitation: v1_list_ledger_balances_params.Limitation,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1ListLedgerBalancesResponse:
        """
        Returns opening & closing balances of all specified ledgers for each day in the
        specified interval.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          date: Date interval over which the ledger balances are created.

          ledger_types: Accounting ledger types to which ledger balances belong.

          limitation: Limitation on the quantity of data returned.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/ledgerBalances/getAll",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "date": date,
                    "ledger_types": ledger_types,
                    "limitation": limitation,
                    "enterprise_ids": enterprise_ids,
                },
                v1_list_ledger_balances_params.V1ListLedgerBalancesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListLedgerBalancesResponse,
        )

    def list_outlet_items(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: v1_list_outlet_items_params.Limitation,
        closed_utc: Optional[v1_list_outlet_items_params.ClosedUtc] | NotGiven = NOT_GIVEN,
        consumed_utc: Optional[v1_list_outlet_items_params.ConsumedUtc] | NotGiven = NOT_GIVEN,
        currency: Optional[str] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[v1_list_outlet_items_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1ListOutletItemsResponse:
        """
        Returns all outlet items of the enterprise that were consumed (posted) or will
        be consumed within the specified interval. If the `Currency` is specified, costs
        of the items are converted to that currency. Note this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          closed_utc: Interval in which the [Outlet bill](#outlet-bill) was closed.

          consumed_utc: Interval in which the [Outlet item](#outlet-item) was consumed. Required if no
              other filter is provided.

          currency: ISO-4217 code of the [Currency](#currency) the item costs should be converted
              to.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          ids: Unique identifiers of the [Outlet items](#outlet-item). If not specified, the
              operation returns data for all [Outlet items](#outlet-item) within scope of the
              Access Token.

          updated_utc: Interval in which the [Outlet bill](#outlet-bill) was updated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/outletItems/getAll",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "closed_utc": closed_utc,
                    "consumed_utc": consumed_utc,
                    "currency": currency,
                    "enterprise_ids": enterprise_ids,
                    "ids": ids,
                    "updated_utc": updated_utc,
                },
                v1_list_outlet_items_params.V1ListOutletItemsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListOutletItemsResponse,
        )

    def list_outlets(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: v1_list_outlets_params.Limitation,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        outlet_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[v1_list_outlets_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1ListOutletsResponse:
        """
        Returns all outlets of an enterprise associated with the connector integration.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          outlet_ids: Unique identifiers of the requested
              [Outlets](https://mews-systems.gitbook.io/connector-api/operations/#outlet).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/outlets/getAll",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "enterprise_ids": enterprise_ids,
                    "outlet_ids": outlet_ids,
                    "updated_utc": updated_utc,
                },
                v1_list_outlets_params.V1ListOutletsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListOutletsResponse,
        )

    def list_preauthorizations_by_customers(
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
    ) -> V1ListPreauthorizationsByCustomersResponse:
        """
        Returns all preauthorizations of specified customers.

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
            "/api/connector/v1/preauthorizations/getAllByCustomers",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "customer_ids": customer_ids,
                },
                v1_list_preauthorizations_by_customers_params.V1ListPreauthorizationsByCustomersParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListPreauthorizationsByCustomersResponse,
        )

    def list_product_categories(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: v1_list_product_categories_params.Limitation,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        product_category_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        service_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[v1_list_product_categories_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1ListProductCategoriesResponse:
        """Returns all categories of products.

        Note this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          product_category_ids: Unique identifiers of
              [Product category](https://mews-systems.gitbook.io/connector-api/operations/#product-category).

          service_ids: Unique identifiers of
              [Services](https://mews-systems.gitbook.io/connector-api/operations/services/#service)
              to which the resource categories belong.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/productCategories/getAll",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "enterprise_ids": enterprise_ids,
                    "product_category_ids": product_category_ids,
                    "service_ids": service_ids,
                    "updated_utc": updated_utc,
                },
                v1_list_product_categories_params.V1ListProductCategoriesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListProductCategoriesResponse,
        )

    def list_product_service_orders(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: v1_list_product_service_orders_params.Limitation,
        service_ids: List[str],
        account_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        linked_reservation_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        product_service_order_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        states: Optional[
            List[Literal["Inquired", "Confirmed", "Started", "Processed", "Canceled", "Optional", "Requested"]]
        ]
        | NotGiven = NOT_GIVEN,
        updated_utc: Optional[v1_list_product_service_orders_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1ListProductServiceOrdersResponse:
        """
        Returns all product service orders orders associated with the given enterprise.
        This operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property)..

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          service_ids: Unique identifiers of the
              [Services](https://mews-systems.gitbook.io/connector-api/operations/services/#service).

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          product_service_order_ids: Unique identifiers of the
              [Product service order](https://mews-systems.gitbook.io/connector-api/operations/#product-service-order).

          states: A list of product service order states to filter by.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/productServiceOrders/getAll",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "service_ids": service_ids,
                    "account_ids": account_ids,
                    "enterprise_ids": enterprise_ids,
                    "linked_reservation_ids": linked_reservation_ids,
                    "product_service_order_ids": product_service_order_ids,
                    "states": states,
                    "updated_utc": updated_utc,
                },
                v1_list_product_service_orders_params.V1ListProductServiceOrdersParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListProductServiceOrdersResponse,
        )

    def list_rate_groups(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: v1_list_rate_groups_params.Limitation,
        activity_states: Optional[List[Literal["Deleted", "Active"]]] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        external_identifiers: Optional[List[str]] | NotGiven = NOT_GIVEN,
        rate_group_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        service_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[v1_list_rate_groups_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1ListRateGroupsResponse:
        """Returns all rate groups, filtered by unique identifiers and other filters.

        Note
        this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          activity_states: Whether to return only active, only deleted or both records.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          external_identifiers: Identifiers of
              [Rate group](https://mews-systems.gitbook.io/connector-api/operations/#rate-group)
              from external systems.

          rate_group_ids: Unique identifiers of the
              [Rate group](https://mews-systems.gitbook.io/connector-api/operations/#rate-group).
              Required if ServiceIds filter is not provided.

          service_ids: Unique identifiers of the
              [Service](https://mews-systems.gitbook.io/connector-api/operations/services/#service).
              Required if RateGroupIds filter is not provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/rateGroups/getAll",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "activity_states": activity_states,
                    "enterprise_ids": enterprise_ids,
                    "external_identifiers": external_identifiers,
                    "rate_group_ids": rate_group_ids,
                    "service_ids": service_ids,
                    "updated_utc": updated_utc,
                },
                v1_list_rate_groups_params.V1ListRateGroupsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListRateGroupsResponse,
        )

    def list_reservation_groups(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: v1_list_reservation_groups_params.Limitation,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        reservation_group_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[v1_list_reservation_groups_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1ListReservationGroupsResponse:
        """Returns all reservation groups, filtered by unique identifiers and other
        filters.

        Note this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          reservation_group_ids: Unique identifiers of the
              [Reservation Group](https://mews-systems.gitbook.io/connector-api/operations/#reservation-group).
              Required if no other filter is provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/reservationGroups/getAll",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "enterprise_ids": enterprise_ids,
                    "reservation_group_ids": reservation_group_ids,
                    "updated_utc": updated_utc,
                },
                v1_list_reservation_groups_params.V1ListReservationGroupsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListReservationGroupsResponse,
        )

    def list_resource_categories(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: v1_list_resource_categories_params.Limitation,
        service_ids: List[str],
        activity_states: Optional[List[Literal["Deleted", "Active"]]] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        resource_category_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[v1_list_resource_categories_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1ListResourceCategoriesResponse:
        """Returns all categories of resources.

        This operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          service_ids: Unique identifiers of
              [Services](https://mews-systems.gitbook.io/connector-api/operations/services/#service)
              to which the resource categories belong.

          activity_states: Whether to return only active, only deleted or both records.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          resource_category_ids: Unique identifiers of
              [Resource categories](https://mews-systems.gitbook.io/connector-api/operations/#resource-category).

          updated_utc: Interval in which the resource categories were updated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/resourceCategories/getAll",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "service_ids": service_ids,
                    "activity_states": activity_states,
                    "enterprise_ids": enterprise_ids,
                    "resource_category_ids": resource_category_ids,
                    "updated_utc": updated_utc,
                },
                v1_list_resource_categories_params.V1ListResourceCategoriesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListResourceCategoriesResponse,
        )

    def list_resource_category_assignments(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: v1_list_resource_category_assignments_params.Limitation,
        resource_category_ids: List[str],
        activity_states: Optional[List[Literal["Deleted", "Active"]]] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        resource_category_assignment_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        resource_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[v1_list_resource_category_assignments_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1ListResourceCategoryAssignmentsResponse:
        """Returns all resource category assignments.

        This operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          resource_category_ids: Unique identifiers of
              [Resource categories](https://mews-systems.gitbook.io/connector-api/operations/#resource-category)
              to which the resource category assignment belong.

          activity_states: Whether to return only active, only deleted or both records.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          resource_category_assignment_ids: Unique identifiers of
              [Resource category assignment](https://mews-systems.gitbook.io/connector-api/operations/resourcecategories/#resource-category-assignment).

          resource_ids: Unique identifiers of resources to which the resource category assignments
              belong.

          updated_utc: Interval in which the resource category assignments were updated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/resourceCategoryAssignments/getAll",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "resource_category_ids": resource_category_ids,
                    "activity_states": activity_states,
                    "enterprise_ids": enterprise_ids,
                    "resource_category_assignment_ids": resource_category_assignment_ids,
                    "resource_ids": resource_ids,
                    "updated_utc": updated_utc,
                },
                v1_list_resource_category_assignments_params.V1ListResourceCategoryAssignmentsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListResourceCategoryAssignmentsResponse,
        )

    def list_resource_category_image_assignments(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: v1_list_resource_category_image_assignments_params.Limitation,
        resource_category_ids: List[str],
        activity_states: Optional[List[Literal["Deleted", "Active"]]] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        resource_category_image_assignment_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[v1_list_resource_category_image_assignments_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1ListResourceCategoryImageAssignmentsResponse:
        """Returns all resource category image assignments.

        This operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          resource_category_ids: Unique identifiers of
              [Resource categories](https://mews-systems.gitbook.io/connector-api/operations/resources/#resource-category)
              to which the resource category image assignments belong.

          activity_states: Whether to return only active, only deleted or both records.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          resource_category_image_assignment_ids: Unique identifiers of
              [Resource category image assignments](https://mews-systems.gitbook.io/connector-api/operations/resourcecategories/#resource-category-image-assignment).

          updated_utc: Interval in which the resource category image assignments were updated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/resourceCategoryImageAssignments/getAll",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "resource_category_ids": resource_category_ids,
                    "activity_states": activity_states,
                    "enterprise_ids": enterprise_ids,
                    "resource_category_image_assignment_ids": resource_category_image_assignment_ids,
                    "updated_utc": updated_utc,
                },
                v1_list_resource_category_image_assignments_params.V1ListResourceCategoryImageAssignmentsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListResourceCategoryImageAssignmentsResponse,
        )

    def list_resource_feature_assignments(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: v1_list_resource_feature_assignments_params.Limitation,
        resource_feature_ids: List[str],
        activity_states: Optional[List[Literal["Deleted", "Active"]]] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        resource_feature_assignment_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[v1_list_resource_feature_assignments_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1ListResourceFeatureAssignmentsResponse:
        """Returns all resource feature assignments.

        This operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          resource_feature_ids: Unique identifiers of
              [Resource features](https://mews-systems.gitbook.io/connector-api/operations/#resource-feature)
              to which the resource feature assignments belong.

          activity_states: Whether to return only active, only deleted or both records.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/resourceFeatureAssignments/getAll",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "resource_feature_ids": resource_feature_ids,
                    "activity_states": activity_states,
                    "enterprise_ids": enterprise_ids,
                    "resource_feature_assignment_ids": resource_feature_assignment_ids,
                    "updated_utc": updated_utc,
                },
                v1_list_resource_feature_assignments_params.V1ListResourceFeatureAssignmentsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListResourceFeatureAssignmentsResponse,
        )

    def list_resource_features(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: v1_list_resource_features_params.Limitation,
        service_ids: List[str],
        activity_states: Optional[List[Literal["Deleted", "Active"]]] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        resource_feature_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[v1_list_resource_features_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1ListResourceFeaturesResponse:
        """Returns all resource features.

        This operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          service_ids: Unique identifiers of
              [Services](https://mews-systems.gitbook.io/connector-api/operations/services/#service)
              to which the resource features belong.

          activity_states: Whether to return only active, only deleted or both records.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          resource_feature_ids: Unique identifiers of
              [Resource features](https://mews-systems.gitbook.io/connector-api/operations/#resource-feature).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/resourceFeatures/getAll",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "service_ids": service_ids,
                    "activity_states": activity_states,
                    "enterprise_ids": enterprise_ids,
                    "resource_feature_ids": resource_feature_ids,
                    "updated_utc": updated_utc,
                },
                v1_list_resource_features_params.V1ListResourceFeaturesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListResourceFeaturesResponse,
        )

    def list_rules(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        extent: v1_list_rules_params.Extent,
        limitation: v1_list_rules_params.Limitation,
        service_ids: List[str],
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[v1_list_rules_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1ListRulesResponse:
        """Returns all rules applied with the reservations.

        Note this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          extent: Extent of data to be returned.

          limitation: Limitation on the quantity of data returned.

          service_ids: Unique identifiers of the
              [Services](https://mews-systems.gitbook.io/connector-api/operations/services/#service).

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/rules/getAll",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "extent": extent,
                    "limitation": limitation,
                    "service_ids": service_ids,
                    "enterprise_ids": enterprise_ids,
                    "ids": ids,
                    "updated_utc": updated_utc,
                },
                v1_list_rules_params.V1ListRulesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListRulesResponse,
        )

    def list_sources(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: v1_list_sources_params.Limitation,
        source_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[v1_list_sources_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1ListSourcesResponse:
        """Returns all sources from which reservations can originate.

        Note this operation
        uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          source_ids: Unique identifiers of
              [Sources](https://mews-systems.gitbook.io/connector-api/operations/sources/#source).

          updated_utc: Interval in which the source was updated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/sources/getAll",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "source_ids": source_ids,
                    "updated_utc": updated_utc,
                },
                v1_list_sources_params.V1ListSourcesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListSourcesResponse,
        )

    def list_tax_environments(
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
    ) -> V1ListTaxEnvironmentsResponse:
        """
        Returns all tax environments supported by the API.

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
            "/api/connector/v1/taxEnvironments/getAll",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                },
                v1_list_tax_environments_params.V1ListTaxEnvironmentsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListTaxEnvironmentsResponse,
        )

    def list_taxations(
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
    ) -> V1ListTaxationsResponse:
        """
        Returns all taxations supported in tax environments.

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
            "/api/connector/v1/taxations/getAll",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                },
                v1_list_taxations_params.V1ListTaxationsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListTaxationsResponse,
        )


class AsyncV1Resource(AsyncAPIResource):
    @cached_property
    def account_notes(self) -> AsyncAccountNotesResource:
        return AsyncAccountNotesResource(self._client)

    @cached_property
    def accounting_items(self) -> AsyncAccountingItemsResource:
        return AsyncAccountingItemsResource(self._client)

    @cached_property
    def accounts(self) -> AsyncAccountsResource:
        return AsyncAccountsResource(self._client)

    @cached_property
    def addresses(self) -> AsyncAddressesResource:
        return AsyncAddressesResource(self._client)

    @cached_property
    def availability_blocks(self) -> AsyncAvailabilityBlocksResource:
        return AsyncAvailabilityBlocksResource(self._client)

    @cached_property
    def bills(self) -> AsyncBillsResource:
        return AsyncBillsResource(self._client)

    @cached_property
    def cancellation_policies(self) -> AsyncCancellationPoliciesResource:
        return AsyncCancellationPoliciesResource(self._client)

    @cached_property
    def commands(self) -> AsyncCommandsResource:
        return AsyncCommandsResource(self._client)

    @cached_property
    def companies(self) -> AsyncCompaniesResource:
        return AsyncCompaniesResource(self._client)

    @cached_property
    def company_contracts(self) -> AsyncCompanyContractsResource:
        return AsyncCompanyContractsResource(self._client)

    @cached_property
    def credit_cards(self) -> AsyncCreditCardsResource:
        return AsyncCreditCardsResource(self._client)

    @cached_property
    def customers(self) -> AsyncCustomersResource:
        return AsyncCustomersResource(self._client)

    @cached_property
    def exports(self) -> AsyncExportsResource:
        return AsyncExportsResource(self._client)

    @cached_property
    def identity_documents(self) -> AsyncIdentityDocumentsResource:
        return AsyncIdentityDocumentsResource(self._client)

    @cached_property
    def languages(self) -> AsyncLanguagesResource:
        return AsyncLanguagesResource(self._client)

    @cached_property
    def loyalty_memberships(self) -> AsyncLoyaltyMembershipsResource:
        return AsyncLoyaltyMembershipsResource(self._client)

    @cached_property
    def loyalty_programs(self) -> AsyncLoyaltyProgramsResource:
        return AsyncLoyaltyProgramsResource(self._client)

    @cached_property
    def loyalty_tiers(self) -> AsyncLoyaltyTiersResource:
        return AsyncLoyaltyTiersResource(self._client)

    @cached_property
    def message_threads(self) -> AsyncMessageThreadsResource:
        return AsyncMessageThreadsResource(self._client)

    @cached_property
    def messages(self) -> AsyncMessagesResource:
        return AsyncMessagesResource(self._client)

    @cached_property
    def order_items(self) -> AsyncOrderItemsResource:
        return AsyncOrderItemsResource(self._client)

    @cached_property
    def payment_requests(self) -> AsyncPaymentRequestsResource:
        return AsyncPaymentRequestsResource(self._client)

    @cached_property
    def payments(self) -> AsyncPaymentsResource:
        return AsyncPaymentsResource(self._client)

    @cached_property
    def products(self) -> AsyncProductsResource:
        return AsyncProductsResource(self._client)

    @cached_property
    def rates(self) -> AsyncRatesResource:
        return AsyncRatesResource(self._client)

    @cached_property
    def reservations(self) -> AsyncReservationsResource:
        return AsyncReservationsResource(self._client)

    @cached_property
    def resource_access_tokens(self) -> AsyncResourceAccessTokensResource:
        return AsyncResourceAccessTokensResource(self._client)

    @cached_property
    def resource_blocks(self) -> AsyncResourceBlocksResource:
        return AsyncResourceBlocksResource(self._client)

    @cached_property
    def resources(self) -> AsyncResourcesResource:
        return AsyncResourcesResource(self._client)

    @cached_property
    def restrictions(self) -> AsyncRestrictionsResource:
        return AsyncRestrictionsResource(self._client)

    @cached_property
    def routing_rules(self) -> AsyncRoutingRulesResource:
        return AsyncRoutingRulesResource(self._client)

    @cached_property
    def service_order_notes(self) -> AsyncServiceOrderNotesResource:
        return AsyncServiceOrderNotesResource(self._client)

    @cached_property
    def service_overbooking_limits(self) -> AsyncServiceOverbookingLimitsResource:
        return AsyncServiceOverbookingLimitsResource(self._client)

    @cached_property
    def services(self) -> AsyncServicesResource:
        return AsyncServicesResource(self._client)

    @cached_property
    def tasks(self) -> AsyncTasksResource:
        return AsyncTasksResource(self._client)

    @cached_property
    def voucher_codes(self) -> AsyncVoucherCodesResource:
        return AsyncVoucherCodesResource(self._client)

    @cached_property
    def vouchers(self) -> AsyncVouchersResource:
        return AsyncVouchersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return AsyncV1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return AsyncV1ResourceWithStreamingResponse(self)

    async def add_order(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        service_id: str,
        account_id: Optional[str] | NotGiven = NOT_GIVEN,
        bill_id: Optional[str] | NotGiven = NOT_GIVEN,
        business_segment_id: Optional[str] | NotGiven = NOT_GIVEN,
        consumption_utc: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        customer_id: Optional[str] | NotGiven = NOT_GIVEN,
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        items: Optional[Iterable[v1_add_order_params.Item]] | NotGiven = NOT_GIVEN,
        linked_reservation_id: Optional[str] | NotGiven = NOT_GIVEN,
        notes: Optional[str] | NotGiven = NOT_GIVEN,
        options: Optional[v1_add_order_params.Options] | NotGiven = NOT_GIVEN,
        product_orders: Optional[Iterable[v1_add_order_params.ProductOrder]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1AddOrderResponse:
        """Creates a new order, with the specified products and items.

        If the time of
        consumption is specified, it must be either in the future or within the Editable
        History Interval for the enterprise. Compared to a stay service order (i.e. a
        reservation), which is consumed over certain span of time, a product service
        order is consumed at a single point in time. Note this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          service_id: Identifier of the
              [Service](https://mews-systems.gitbook.io/connector-api/operations/services/#service)
              to be ordered.

          account_id: Identifier of the
              [Customer](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer)
              or
              [Company](https://mews-systems.gitbook.io/connector-api/operations/companies/#company)
              to be charged. Company billing may not be enabled for your integration.

          bill_id: Identifier of the
              [Bill](https://mews-systems.gitbook.io/connector-api/operations/bills/#bill) to
              which the created order will be assigned. The bill needs to be issued to the
              same account as the order.

          consumption_utc: Date and time of the order consumption in UTC timezone in ISO 8601 format. If
              not specified, current date and time is used. Please note, as order consumption
              is one-time event, the optional parameters StartUtc and EndUtc in
              [Product order parameters](https://mews-systems.gitbook.io/connector-api/operations/#product-order-parameters)
              should not be used.

          customer_id: Identifier of the
              [Customer](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer)
              to be charged. **Deprecated!**

          enterprise_id: Unique identifier of the
              [Enterprise](https://mews-systems.gitbook.io/connector-api/operations/enterprises/#enterprise).
              Required when using a
              [Portfolio Access Token](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          items: Parameters of the ordered custom items.

          notes: Additional notes of the order.

          product_orders: Parameters of the ordered products.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/orders/add",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "service_id": service_id,
                    "account_id": account_id,
                    "bill_id": bill_id,
                    "business_segment_id": business_segment_id,
                    "consumption_utc": consumption_utc,
                    "customer_id": customer_id,
                    "enterprise_id": enterprise_id,
                    "items": items,
                    "linked_reservation_id": linked_reservation_id,
                    "notes": notes,
                    "options": options,
                    "product_orders": product_orders,
                },
                v1_add_order_params.V1AddOrderParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1AddOrderResponse,
        )

    async def add_outlet_bill(
        self,
        *,
        access_token: str,
        bills: Iterable[v1_add_outlet_bill_params.Bill],
        client: str,
        client_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1AddOutletBillResponse:
        """
        Adds new outlet bills with their items.

        Args:
          access_token: Access token of the client application.

          bills: The new outlet bills.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/outletBills/add",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "bills": bills,
                    "client": client,
                    "client_token": client_token,
                },
                v1_add_outlet_bill_params.V1AddOutletBillParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1AddOutletBillResponse,
        )

    async def get_all_source_assignments(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: v1_get_all_source_assignments_params.Limitation,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        reservation_group_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[v1_get_all_source_assignments_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1GetAllSourceAssignmentsResponse:
        """Returns all Sources assigned to a Reservation group.

        Each reservation group can
        have multiple sources. Note this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          reservation_group_ids: Unique identifiers of the `Reservation group`.

          updated_utc: Interval of `Reservation group` last update date and time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/sourceAssignments/getAll",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "enterprise_ids": enterprise_ids,
                    "reservation_group_ids": reservation_group_ids,
                    "updated_utc": updated_utc,
                },
                v1_get_all_source_assignments_params.V1GetAllSourceAssignmentsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1GetAllSourceAssignmentsResponse,
        )

    async def get_all_source_assignments_2024_09_20(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: v1_get_all_source_assignments_2024_09_20_params.Limitation,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        reservation_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1GetAllSourceAssignments2024_09_20Response:
        """Returns all Sources assigned to Reservations.

        Each reservation can have multiple
        sources. Note this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          reservation_ids: Unique identifiers of `Reservation`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/sourceAssignments/getAll/2024-09-20",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "enterprise_ids": enterprise_ids,
                    "reservation_ids": reservation_ids,
                },
                v1_get_all_source_assignments_2024_09_20_params.V1GetAllSourceAssignments2024_09_20Params,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1GetAllSourceAssignments2024_09_20Response,
        )

    async def get_configuration(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1GetConfigurationResponse:
        """Returns the enterprise configuration.

        For single-enterprise Access Tokens, this
        is the enterprise associated with the token. For
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
        use the `EnterpriseId` parameter to specify which enterprise you want the
        configuration for. In the case of service scoped integrations, the operation
        returns the configuration associated with both the enterprise and the bookable
        service linked to the token.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          enterprise_id: Unique identifier of the
              [Enterprise](https://mews-systems.gitbook.io/connector-api/operations/#enterprise),
              defaults to the enterprise associated with the given access token.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/configuration/get",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "enterprise_id": enterprise_id,
                },
                v1_get_configuration_params.V1GetConfigurationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1GetConfigurationResponse,
        )

    async def get_image_urls(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        images: Iterable[v1_get_image_urls_params.Image],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1GetImageURLsResponse:
        """
        Returns URLs of the specified images.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          images: Parameters of images whose URLs should be returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/images/getUrls",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "images": images,
                },
                v1_get_image_urls_params.V1GetImageURLsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1GetImageURLsResponse,
        )

    async def list_accounting_categories(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: v1_list_accounting_categories_params.Limitation,
        accounting_category_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        activity_states: Optional[List[Literal["Deleted", "Active"]]] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[v1_list_accounting_categories_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1ListAccountingCategoriesResponse:
        """
        Returns all accounting categories of the enterprise associated with the
        connector integration. Note this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          accounting_category_ids: Unique identifiers of the requested
              [Accounting categories](https://mews-systems.gitbook.io/connector-api/operations/#accounting-category).

          activity_states: Whether to return only active, only deleted or both records.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          updated_utc: Last update date and time of the accounting category in UTC timezone in ISO 8601
              format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/accountingCategories/getAll",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "accounting_category_ids": accounting_category_ids,
                    "activity_states": activity_states,
                    "enterprise_ids": enterprise_ids,
                    "updated_utc": updated_utc,
                },
                v1_list_accounting_categories_params.V1ListAccountingCategoriesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListAccountingCategoriesResponse,
        )

    async def list_age_categories(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: v1_list_age_categories_params.Limitation,
        activity_states: Optional[List[Literal["Deleted", "Active"]]] | NotGiven = NOT_GIVEN,
        age_category_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        service_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[v1_list_age_categories_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1ListAgeCategoriesResponse:
        """
        Returns all age categories filtered by
        [Service](https://mews-systems.gitbook.io/connector-api/operations/services/#service).
        Note this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          activity_states: Whether to return only active, only deleted or both records.

          age_category_ids: Unique identifiers of
              [Age categories](https://mews-systems.gitbook.io/connector-api/operations/#age-category).

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          service_ids: Unique identifiers of `Services` associated with the age categories. If not
              provided, defaults to all bookable services.

          updated_utc: Interval in which the age category was updated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/ageCategories/getAll",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "activity_states": activity_states,
                    "age_category_ids": age_category_ids,
                    "enterprise_ids": enterprise_ids,
                    "service_ids": service_ids,
                    "updated_utc": updated_utc,
                },
                v1_list_age_categories_params.V1ListAgeCategoriesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListAgeCategoriesResponse,
        )

    async def list_availability_adjustments(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: v1_list_availability_adjustments_params.Limitation,
        activity_states: Optional[List[Literal["Deleted", "Active"]]] | NotGiven = NOT_GIVEN,
        availability_adjustment_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[v1_list_availability_adjustments_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1ListAvailabilityAdjustmentsResponse:
        """Returns all availability adjustments.

        Note this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          activity_states: Whether to return only active, only deleted, or both types of record. If not
              specified, only active records will be returned.

          availability_adjustment_ids: Unique identifiers of the requested
              [Availability adjustments](https://mews-systems.gitbook.io/connector-api/operations/#availability-adjustment).

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          updated_utc: Interval in which the availability adjustments were updated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/availabilityAdjustments/getAll",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "activity_states": activity_states,
                    "availability_adjustment_ids": availability_adjustment_ids,
                    "enterprise_ids": enterprise_ids,
                    "updated_utc": updated_utc,
                },
                v1_list_availability_adjustments_params.V1ListAvailabilityAdjustmentsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListAvailabilityAdjustmentsResponse,
        )

    async def list_business_segments(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: v1_list_business_segments_params.Limitation,
        activity_states: Optional[List[Literal["Deleted", "Active"]]] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        service_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[v1_list_business_segments_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1ListBusinessSegmentsResponse:
        """Returns all business segments.

        This operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          activity_states: Whether to return only active, only deleted or both records.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          ids: Unique identifiers of the requested `Business segment`.

          service_ids: Unique identifiers of the `Services` from which the business segments are
              requested.

          updated_utc: Interval of `Business segment` last update date and time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/businessSegments/getAll",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "activity_states": activity_states,
                    "enterprise_ids": enterprise_ids,
                    "ids": ids,
                    "service_ids": service_ids,
                    "updated_utc": updated_utc,
                },
                v1_list_business_segments_params.V1ListBusinessSegmentsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListBusinessSegmentsResponse,
        )

    async def list_cashier_transactions(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: v1_list_cashier_transactions_params.Limitation,
        cashier_transaction_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        created_utc: Optional[v1_list_cashier_transactions_params.CreatedUtc] | NotGiven = NOT_GIVEN,
        end_utc: Optional[str] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        start_utc: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1ListCashierTransactionsResponse:
        """Returns all cashier transactions created within the specified interval.

        Note
        this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/cashierTransactions/getAll",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "cashier_transaction_ids": cashier_transaction_ids,
                    "created_utc": created_utc,
                    "end_utc": end_utc,
                    "enterprise_ids": enterprise_ids,
                    "start_utc": start_utc,
                },
                v1_list_cashier_transactions_params.V1ListCashierTransactionsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListCashierTransactionsResponse,
        )

    async def list_cashiers(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: v1_list_cashiers_params.Limitation,
        activity_states: Optional[List[Literal["Deleted", "Active"]]] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[v1_list_cashiers_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1ListCashiersResponse:
        """Returns all cashiers.

        Note this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          activity_states: Whether to return only active, only deleted or both records.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          ids: Unique identifiers of the requested
              [Cashier](https://mews-systems.gitbook.io/connector-api/operations/#cashier).

          updated_utc: Interval in which `Cashier` was updated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/cashiers/getAll",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "activity_states": activity_states,
                    "enterprise_ids": enterprise_ids,
                    "ids": ids,
                    "updated_utc": updated_utc,
                },
                v1_list_cashiers_params.V1ListCashiersParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListCashiersResponse,
        )

    async def list_companionships(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        extent: v1_list_companionships_params.Extent,
        limitation: v1_list_companionships_params.Limitation,
        companionship_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        customer_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        reservation_group_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        reservation_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[v1_list_companionships_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1ListCompanionshipsResponse:
        """
        Returns all companionships based on customers, reservations or reservation
        groups. One of them must be specified in the request. Note this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          extent: Extent of data to be returned. E.g. it is possible to specify that together with
              the companionships, customers, reservations, and reservation groups should be
              also returned.

          limitation: Limitation on the quantity of data returned.

          companionship_ids: Unique identifiers of
              [Companionship](https://mews-systems.gitbook.io/connector-api/operations/#companionship).

          customer_ids: Unique identifiers of
              [Customers](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer).

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          reservation_group_ids: Unique identifiers of
              [Reservation groups](https://mews-systems.gitbook.io/connector-api/operations/reservations/#reservation-group).

          reservation_ids: Unique identifiers of reservations.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/companionships/getAll",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "extent": extent,
                    "limitation": limitation,
                    "companionship_ids": companionship_ids,
                    "customer_ids": customer_ids,
                    "enterprise_ids": enterprise_ids,
                    "reservation_group_ids": reservation_group_ids,
                    "reservation_ids": reservation_ids,
                    "updated_utc": updated_utc,
                },
                v1_list_companionships_params.V1ListCompanionshipsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListCompanionshipsResponse,
        )

    async def list_counters(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: v1_list_counters_params.Limitation,
        counter_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        type: Optional[
            Literal[
                "Counter",
                "AccountingCounter",
                "AvailabilityBlockCounter",
                "BillCounter",
                "BillPreviewCounter",
                "FiscalCounter",
                "ProformaCounter",
                "RegistrationCardCounter",
                "ServiceOrderCounter",
                "CorrectionBillCounter",
                "PaymentConfirmationBillCounter",
                "CreditNoteBillCounter",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        updated_utc: Optional[v1_list_counters_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1ListCountersResponse:
        """
        Returns all counters of an enterprise associated with the connector integration.
        Note this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          type: Type of the counter. If not specified, the operation returns all types.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/counters/getAll",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "counter_ids": counter_ids,
                    "enterprise_ids": enterprise_ids,
                    "type": type,
                    "updated_utc": updated_utc,
                },
                v1_list_counters_params.V1ListCountersParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListCountersResponse,
        )

    async def list_countries(
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
    ) -> V1ListCountriesResponse:
        """
        Returns all countries supported by the API.

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
            "/api/connector/v1/countries/getAll",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                },
                v1_list_countries_params.V1ListCountriesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListCountriesResponse,
        )

    async def list_currencies(
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
    ) -> V1ListCurrenciesResponse:
        """
        Returns all currencies supported by the API.

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
            "/api/connector/v1/currencies/getAll",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                },
                v1_list_currencies_params.V1ListCurrenciesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListCurrenciesResponse,
        )

    async def list_departments(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: v1_list_departments_params.Limitation,
        department_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[v1_list_departments_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1ListDepartmentsResponse:
        """
        Returns all departments of an enterprise associated with the connector
        integration. Note this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          department_ids: Unique identifiers of
              [Department](https://mews-systems.gitbook.io/connector-api/operations/#department).

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/departments/getAll",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "department_ids": department_ids,
                    "enterprise_ids": enterprise_ids,
                    "updated_utc": updated_utc,
                },
                v1_list_departments_params.V1ListDepartmentsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListDepartmentsResponse,
        )

    async def list_devices(
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
    ) -> V1ListDevicesResponse:
        """
        Returns all devices in the enterprise.

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
            "/api/connector/v1/devices/getAll",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                },
                v1_list_devices_params.V1ListDevicesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListDevicesResponse,
        )

    async def list_enterprises(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: v1_list_enterprises_params.Limitation,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        external_identifiers: Optional[List[str]] | NotGiven = NOT_GIVEN,
        linked_utc: Optional[v1_list_enterprises_params.LinkedUtc] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[v1_list_enterprises_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1ListEnterprisesResponse:
        """
        Returns all enterprises within scope of the `Access Token`, optionally filtered
        by enterprise identifiers and external identifiers. Note this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          enterprise_ids: Unique identifiers of the
              [Enterprises](https://mews-systems.gitbook.io/connector-api/operations/#enterprise).
              If not specified, all enterprises within scope of the Access Token are returned.

          external_identifiers: Identifiers of the
              [Enterprise](https://mews-systems.gitbook.io/connector-api/operations/#enterprise)
              from external system.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/enterprises/getAll",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "enterprise_ids": enterprise_ids,
                    "external_identifiers": external_identifiers,
                    "linked_utc": linked_utc,
                    "updated_utc": updated_utc,
                },
                v1_list_enterprises_params.V1ListEnterprisesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListEnterprisesResponse,
        )

    async def list_exchange_rates(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1ListExchangeRatesResponse:
        """
        Returns all available exchange rates among currencies of the
        [Enterprise](https://mews-systems.gitbook.io/connector-api/operations/configuration/#enterprise).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          enterprise_ids: Unique identifiers of the
              [Enterprises](https://mews-systems.gitbook.io/connector-api/operations/configuration/#enterprise).
              If not specified, the operation returns the exchange rates for all enterprises
              within scope of the Access Token.

          ids: Unique identifiers of the Exchange Rates. If not specified, the operation
              returns all exchange rates.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/exchangeRates/getAll",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "enterprise_ids": enterprise_ids,
                    "ids": ids,
                },
                v1_list_exchange_rates_params.V1ListExchangeRatesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListExchangeRatesResponse,
        )

    async def list_ledger_balances(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        date: v1_list_ledger_balances_params.Date,
        ledger_types: List[Literal["Revenue", "Tax", "Payment", "Deposit", "Guest", "City"]],
        limitation: v1_list_ledger_balances_params.Limitation,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1ListLedgerBalancesResponse:
        """
        Returns opening & closing balances of all specified ledgers for each day in the
        specified interval.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          date: Date interval over which the ledger balances are created.

          ledger_types: Accounting ledger types to which ledger balances belong.

          limitation: Limitation on the quantity of data returned.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/ledgerBalances/getAll",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "date": date,
                    "ledger_types": ledger_types,
                    "limitation": limitation,
                    "enterprise_ids": enterprise_ids,
                },
                v1_list_ledger_balances_params.V1ListLedgerBalancesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListLedgerBalancesResponse,
        )

    async def list_outlet_items(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: v1_list_outlet_items_params.Limitation,
        closed_utc: Optional[v1_list_outlet_items_params.ClosedUtc] | NotGiven = NOT_GIVEN,
        consumed_utc: Optional[v1_list_outlet_items_params.ConsumedUtc] | NotGiven = NOT_GIVEN,
        currency: Optional[str] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[v1_list_outlet_items_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1ListOutletItemsResponse:
        """
        Returns all outlet items of the enterprise that were consumed (posted) or will
        be consumed within the specified interval. If the `Currency` is specified, costs
        of the items are converted to that currency. Note this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          closed_utc: Interval in which the [Outlet bill](#outlet-bill) was closed.

          consumed_utc: Interval in which the [Outlet item](#outlet-item) was consumed. Required if no
              other filter is provided.

          currency: ISO-4217 code of the [Currency](#currency) the item costs should be converted
              to.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          ids: Unique identifiers of the [Outlet items](#outlet-item). If not specified, the
              operation returns data for all [Outlet items](#outlet-item) within scope of the
              Access Token.

          updated_utc: Interval in which the [Outlet bill](#outlet-bill) was updated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/outletItems/getAll",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "closed_utc": closed_utc,
                    "consumed_utc": consumed_utc,
                    "currency": currency,
                    "enterprise_ids": enterprise_ids,
                    "ids": ids,
                    "updated_utc": updated_utc,
                },
                v1_list_outlet_items_params.V1ListOutletItemsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListOutletItemsResponse,
        )

    async def list_outlets(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: v1_list_outlets_params.Limitation,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        outlet_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[v1_list_outlets_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1ListOutletsResponse:
        """
        Returns all outlets of an enterprise associated with the connector integration.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          outlet_ids: Unique identifiers of the requested
              [Outlets](https://mews-systems.gitbook.io/connector-api/operations/#outlet).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/outlets/getAll",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "enterprise_ids": enterprise_ids,
                    "outlet_ids": outlet_ids,
                    "updated_utc": updated_utc,
                },
                v1_list_outlets_params.V1ListOutletsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListOutletsResponse,
        )

    async def list_preauthorizations_by_customers(
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
    ) -> V1ListPreauthorizationsByCustomersResponse:
        """
        Returns all preauthorizations of specified customers.

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
            "/api/connector/v1/preauthorizations/getAllByCustomers",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "customer_ids": customer_ids,
                },
                v1_list_preauthorizations_by_customers_params.V1ListPreauthorizationsByCustomersParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListPreauthorizationsByCustomersResponse,
        )

    async def list_product_categories(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: v1_list_product_categories_params.Limitation,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        product_category_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        service_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[v1_list_product_categories_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1ListProductCategoriesResponse:
        """Returns all categories of products.

        Note this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          product_category_ids: Unique identifiers of
              [Product category](https://mews-systems.gitbook.io/connector-api/operations/#product-category).

          service_ids: Unique identifiers of
              [Services](https://mews-systems.gitbook.io/connector-api/operations/services/#service)
              to which the resource categories belong.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/productCategories/getAll",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "enterprise_ids": enterprise_ids,
                    "product_category_ids": product_category_ids,
                    "service_ids": service_ids,
                    "updated_utc": updated_utc,
                },
                v1_list_product_categories_params.V1ListProductCategoriesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListProductCategoriesResponse,
        )

    async def list_product_service_orders(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: v1_list_product_service_orders_params.Limitation,
        service_ids: List[str],
        account_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        linked_reservation_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        product_service_order_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        states: Optional[
            List[Literal["Inquired", "Confirmed", "Started", "Processed", "Canceled", "Optional", "Requested"]]
        ]
        | NotGiven = NOT_GIVEN,
        updated_utc: Optional[v1_list_product_service_orders_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1ListProductServiceOrdersResponse:
        """
        Returns all product service orders orders associated with the given enterprise.
        This operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property)..

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          service_ids: Unique identifiers of the
              [Services](https://mews-systems.gitbook.io/connector-api/operations/services/#service).

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          product_service_order_ids: Unique identifiers of the
              [Product service order](https://mews-systems.gitbook.io/connector-api/operations/#product-service-order).

          states: A list of product service order states to filter by.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/productServiceOrders/getAll",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "service_ids": service_ids,
                    "account_ids": account_ids,
                    "enterprise_ids": enterprise_ids,
                    "linked_reservation_ids": linked_reservation_ids,
                    "product_service_order_ids": product_service_order_ids,
                    "states": states,
                    "updated_utc": updated_utc,
                },
                v1_list_product_service_orders_params.V1ListProductServiceOrdersParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListProductServiceOrdersResponse,
        )

    async def list_rate_groups(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: v1_list_rate_groups_params.Limitation,
        activity_states: Optional[List[Literal["Deleted", "Active"]]] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        external_identifiers: Optional[List[str]] | NotGiven = NOT_GIVEN,
        rate_group_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        service_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[v1_list_rate_groups_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1ListRateGroupsResponse:
        """Returns all rate groups, filtered by unique identifiers and other filters.

        Note
        this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          activity_states: Whether to return only active, only deleted or both records.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          external_identifiers: Identifiers of
              [Rate group](https://mews-systems.gitbook.io/connector-api/operations/#rate-group)
              from external systems.

          rate_group_ids: Unique identifiers of the
              [Rate group](https://mews-systems.gitbook.io/connector-api/operations/#rate-group).
              Required if ServiceIds filter is not provided.

          service_ids: Unique identifiers of the
              [Service](https://mews-systems.gitbook.io/connector-api/operations/services/#service).
              Required if RateGroupIds filter is not provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/rateGroups/getAll",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "activity_states": activity_states,
                    "enterprise_ids": enterprise_ids,
                    "external_identifiers": external_identifiers,
                    "rate_group_ids": rate_group_ids,
                    "service_ids": service_ids,
                    "updated_utc": updated_utc,
                },
                v1_list_rate_groups_params.V1ListRateGroupsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListRateGroupsResponse,
        )

    async def list_reservation_groups(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: v1_list_reservation_groups_params.Limitation,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        reservation_group_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[v1_list_reservation_groups_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1ListReservationGroupsResponse:
        """Returns all reservation groups, filtered by unique identifiers and other
        filters.

        Note this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          reservation_group_ids: Unique identifiers of the
              [Reservation Group](https://mews-systems.gitbook.io/connector-api/operations/#reservation-group).
              Required if no other filter is provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/reservationGroups/getAll",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "enterprise_ids": enterprise_ids,
                    "reservation_group_ids": reservation_group_ids,
                    "updated_utc": updated_utc,
                },
                v1_list_reservation_groups_params.V1ListReservationGroupsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListReservationGroupsResponse,
        )

    async def list_resource_categories(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: v1_list_resource_categories_params.Limitation,
        service_ids: List[str],
        activity_states: Optional[List[Literal["Deleted", "Active"]]] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        resource_category_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[v1_list_resource_categories_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1ListResourceCategoriesResponse:
        """Returns all categories of resources.

        This operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          service_ids: Unique identifiers of
              [Services](https://mews-systems.gitbook.io/connector-api/operations/services/#service)
              to which the resource categories belong.

          activity_states: Whether to return only active, only deleted or both records.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          resource_category_ids: Unique identifiers of
              [Resource categories](https://mews-systems.gitbook.io/connector-api/operations/#resource-category).

          updated_utc: Interval in which the resource categories were updated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/resourceCategories/getAll",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "service_ids": service_ids,
                    "activity_states": activity_states,
                    "enterprise_ids": enterprise_ids,
                    "resource_category_ids": resource_category_ids,
                    "updated_utc": updated_utc,
                },
                v1_list_resource_categories_params.V1ListResourceCategoriesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListResourceCategoriesResponse,
        )

    async def list_resource_category_assignments(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: v1_list_resource_category_assignments_params.Limitation,
        resource_category_ids: List[str],
        activity_states: Optional[List[Literal["Deleted", "Active"]]] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        resource_category_assignment_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        resource_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[v1_list_resource_category_assignments_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1ListResourceCategoryAssignmentsResponse:
        """Returns all resource category assignments.

        This operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          resource_category_ids: Unique identifiers of
              [Resource categories](https://mews-systems.gitbook.io/connector-api/operations/#resource-category)
              to which the resource category assignment belong.

          activity_states: Whether to return only active, only deleted or both records.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          resource_category_assignment_ids: Unique identifiers of
              [Resource category assignment](https://mews-systems.gitbook.io/connector-api/operations/resourcecategories/#resource-category-assignment).

          resource_ids: Unique identifiers of resources to which the resource category assignments
              belong.

          updated_utc: Interval in which the resource category assignments were updated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/resourceCategoryAssignments/getAll",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "resource_category_ids": resource_category_ids,
                    "activity_states": activity_states,
                    "enterprise_ids": enterprise_ids,
                    "resource_category_assignment_ids": resource_category_assignment_ids,
                    "resource_ids": resource_ids,
                    "updated_utc": updated_utc,
                },
                v1_list_resource_category_assignments_params.V1ListResourceCategoryAssignmentsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListResourceCategoryAssignmentsResponse,
        )

    async def list_resource_category_image_assignments(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: v1_list_resource_category_image_assignments_params.Limitation,
        resource_category_ids: List[str],
        activity_states: Optional[List[Literal["Deleted", "Active"]]] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        resource_category_image_assignment_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[v1_list_resource_category_image_assignments_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1ListResourceCategoryImageAssignmentsResponse:
        """Returns all resource category image assignments.

        This operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          resource_category_ids: Unique identifiers of
              [Resource categories](https://mews-systems.gitbook.io/connector-api/operations/resources/#resource-category)
              to which the resource category image assignments belong.

          activity_states: Whether to return only active, only deleted or both records.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          resource_category_image_assignment_ids: Unique identifiers of
              [Resource category image assignments](https://mews-systems.gitbook.io/connector-api/operations/resourcecategories/#resource-category-image-assignment).

          updated_utc: Interval in which the resource category image assignments were updated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/resourceCategoryImageAssignments/getAll",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "resource_category_ids": resource_category_ids,
                    "activity_states": activity_states,
                    "enterprise_ids": enterprise_ids,
                    "resource_category_image_assignment_ids": resource_category_image_assignment_ids,
                    "updated_utc": updated_utc,
                },
                v1_list_resource_category_image_assignments_params.V1ListResourceCategoryImageAssignmentsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListResourceCategoryImageAssignmentsResponse,
        )

    async def list_resource_feature_assignments(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: v1_list_resource_feature_assignments_params.Limitation,
        resource_feature_ids: List[str],
        activity_states: Optional[List[Literal["Deleted", "Active"]]] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        resource_feature_assignment_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[v1_list_resource_feature_assignments_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1ListResourceFeatureAssignmentsResponse:
        """Returns all resource feature assignments.

        This operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          resource_feature_ids: Unique identifiers of
              [Resource features](https://mews-systems.gitbook.io/connector-api/operations/#resource-feature)
              to which the resource feature assignments belong.

          activity_states: Whether to return only active, only deleted or both records.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/resourceFeatureAssignments/getAll",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "resource_feature_ids": resource_feature_ids,
                    "activity_states": activity_states,
                    "enterprise_ids": enterprise_ids,
                    "resource_feature_assignment_ids": resource_feature_assignment_ids,
                    "updated_utc": updated_utc,
                },
                v1_list_resource_feature_assignments_params.V1ListResourceFeatureAssignmentsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListResourceFeatureAssignmentsResponse,
        )

    async def list_resource_features(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: v1_list_resource_features_params.Limitation,
        service_ids: List[str],
        activity_states: Optional[List[Literal["Deleted", "Active"]]] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        resource_feature_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[v1_list_resource_features_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1ListResourceFeaturesResponse:
        """Returns all resource features.

        This operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          service_ids: Unique identifiers of
              [Services](https://mews-systems.gitbook.io/connector-api/operations/services/#service)
              to which the resource features belong.

          activity_states: Whether to return only active, only deleted or both records.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          resource_feature_ids: Unique identifiers of
              [Resource features](https://mews-systems.gitbook.io/connector-api/operations/#resource-feature).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/resourceFeatures/getAll",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "service_ids": service_ids,
                    "activity_states": activity_states,
                    "enterprise_ids": enterprise_ids,
                    "resource_feature_ids": resource_feature_ids,
                    "updated_utc": updated_utc,
                },
                v1_list_resource_features_params.V1ListResourceFeaturesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListResourceFeaturesResponse,
        )

    async def list_rules(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        extent: v1_list_rules_params.Extent,
        limitation: v1_list_rules_params.Limitation,
        service_ids: List[str],
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[v1_list_rules_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1ListRulesResponse:
        """Returns all rules applied with the reservations.

        Note this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          extent: Extent of data to be returned.

          limitation: Limitation on the quantity of data returned.

          service_ids: Unique identifiers of the
              [Services](https://mews-systems.gitbook.io/connector-api/operations/services/#service).

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/rules/getAll",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "extent": extent,
                    "limitation": limitation,
                    "service_ids": service_ids,
                    "enterprise_ids": enterprise_ids,
                    "ids": ids,
                    "updated_utc": updated_utc,
                },
                v1_list_rules_params.V1ListRulesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListRulesResponse,
        )

    async def list_sources(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: v1_list_sources_params.Limitation,
        source_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[v1_list_sources_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1ListSourcesResponse:
        """Returns all sources from which reservations can originate.

        Note this operation
        uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          source_ids: Unique identifiers of
              [Sources](https://mews-systems.gitbook.io/connector-api/operations/sources/#source).

          updated_utc: Interval in which the source was updated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/sources/getAll",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "source_ids": source_ids,
                    "updated_utc": updated_utc,
                },
                v1_list_sources_params.V1ListSourcesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListSourcesResponse,
        )

    async def list_tax_environments(
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
    ) -> V1ListTaxEnvironmentsResponse:
        """
        Returns all tax environments supported by the API.

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
            "/api/connector/v1/taxEnvironments/getAll",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                },
                v1_list_tax_environments_params.V1ListTaxEnvironmentsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListTaxEnvironmentsResponse,
        )

    async def list_taxations(
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
    ) -> V1ListTaxationsResponse:
        """
        Returns all taxations supported in tax environments.

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
            "/api/connector/v1/taxations/getAll",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                },
                v1_list_taxations_params.V1ListTaxationsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListTaxationsResponse,
        )


class V1ResourceWithRawResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.add_order = to_raw_response_wrapper(
            v1.add_order,
        )
        self.add_outlet_bill = to_raw_response_wrapper(
            v1.add_outlet_bill,
        )
        self.get_all_source_assignments = to_raw_response_wrapper(
            v1.get_all_source_assignments,
        )
        self.get_all_source_assignments_2024_09_20 = to_raw_response_wrapper(
            v1.get_all_source_assignments_2024_09_20,
        )
        self.get_configuration = to_raw_response_wrapper(
            v1.get_configuration,
        )
        self.get_image_urls = to_raw_response_wrapper(
            v1.get_image_urls,
        )
        self.list_accounting_categories = to_raw_response_wrapper(
            v1.list_accounting_categories,
        )
        self.list_age_categories = to_raw_response_wrapper(
            v1.list_age_categories,
        )
        self.list_availability_adjustments = to_raw_response_wrapper(
            v1.list_availability_adjustments,
        )
        self.list_business_segments = to_raw_response_wrapper(
            v1.list_business_segments,
        )
        self.list_cashier_transactions = to_raw_response_wrapper(
            v1.list_cashier_transactions,
        )
        self.list_cashiers = to_raw_response_wrapper(
            v1.list_cashiers,
        )
        self.list_companionships = to_raw_response_wrapper(
            v1.list_companionships,
        )
        self.list_counters = to_raw_response_wrapper(
            v1.list_counters,
        )
        self.list_countries = to_raw_response_wrapper(
            v1.list_countries,
        )
        self.list_currencies = to_raw_response_wrapper(
            v1.list_currencies,
        )
        self.list_departments = to_raw_response_wrapper(
            v1.list_departments,
        )
        self.list_devices = to_raw_response_wrapper(
            v1.list_devices,
        )
        self.list_enterprises = to_raw_response_wrapper(
            v1.list_enterprises,
        )
        self.list_exchange_rates = to_raw_response_wrapper(
            v1.list_exchange_rates,
        )
        self.list_ledger_balances = to_raw_response_wrapper(
            v1.list_ledger_balances,
        )
        self.list_outlet_items = to_raw_response_wrapper(
            v1.list_outlet_items,
        )
        self.list_outlets = to_raw_response_wrapper(
            v1.list_outlets,
        )
        self.list_preauthorizations_by_customers = to_raw_response_wrapper(
            v1.list_preauthorizations_by_customers,
        )
        self.list_product_categories = to_raw_response_wrapper(
            v1.list_product_categories,
        )
        self.list_product_service_orders = to_raw_response_wrapper(
            v1.list_product_service_orders,
        )
        self.list_rate_groups = to_raw_response_wrapper(
            v1.list_rate_groups,
        )
        self.list_reservation_groups = to_raw_response_wrapper(
            v1.list_reservation_groups,
        )
        self.list_resource_categories = to_raw_response_wrapper(
            v1.list_resource_categories,
        )
        self.list_resource_category_assignments = to_raw_response_wrapper(
            v1.list_resource_category_assignments,
        )
        self.list_resource_category_image_assignments = to_raw_response_wrapper(
            v1.list_resource_category_image_assignments,
        )
        self.list_resource_feature_assignments = to_raw_response_wrapper(
            v1.list_resource_feature_assignments,
        )
        self.list_resource_features = to_raw_response_wrapper(
            v1.list_resource_features,
        )
        self.list_rules = to_raw_response_wrapper(
            v1.list_rules,
        )
        self.list_sources = to_raw_response_wrapper(
            v1.list_sources,
        )
        self.list_tax_environments = to_raw_response_wrapper(
            v1.list_tax_environments,
        )
        self.list_taxations = to_raw_response_wrapper(
            v1.list_taxations,
        )

    @cached_property
    def account_notes(self) -> AccountNotesResourceWithRawResponse:
        return AccountNotesResourceWithRawResponse(self._v1.account_notes)

    @cached_property
    def accounting_items(self) -> AccountingItemsResourceWithRawResponse:
        return AccountingItemsResourceWithRawResponse(self._v1.accounting_items)

    @cached_property
    def accounts(self) -> AccountsResourceWithRawResponse:
        return AccountsResourceWithRawResponse(self._v1.accounts)

    @cached_property
    def addresses(self) -> AddressesResourceWithRawResponse:
        return AddressesResourceWithRawResponse(self._v1.addresses)

    @cached_property
    def availability_blocks(self) -> AvailabilityBlocksResourceWithRawResponse:
        return AvailabilityBlocksResourceWithRawResponse(self._v1.availability_blocks)

    @cached_property
    def bills(self) -> BillsResourceWithRawResponse:
        return BillsResourceWithRawResponse(self._v1.bills)

    @cached_property
    def cancellation_policies(self) -> CancellationPoliciesResourceWithRawResponse:
        return CancellationPoliciesResourceWithRawResponse(self._v1.cancellation_policies)

    @cached_property
    def commands(self) -> CommandsResourceWithRawResponse:
        return CommandsResourceWithRawResponse(self._v1.commands)

    @cached_property
    def companies(self) -> CompaniesResourceWithRawResponse:
        return CompaniesResourceWithRawResponse(self._v1.companies)

    @cached_property
    def company_contracts(self) -> CompanyContractsResourceWithRawResponse:
        return CompanyContractsResourceWithRawResponse(self._v1.company_contracts)

    @cached_property
    def credit_cards(self) -> CreditCardsResourceWithRawResponse:
        return CreditCardsResourceWithRawResponse(self._v1.credit_cards)

    @cached_property
    def customers(self) -> CustomersResourceWithRawResponse:
        return CustomersResourceWithRawResponse(self._v1.customers)

    @cached_property
    def exports(self) -> ExportsResourceWithRawResponse:
        return ExportsResourceWithRawResponse(self._v1.exports)

    @cached_property
    def identity_documents(self) -> IdentityDocumentsResourceWithRawResponse:
        return IdentityDocumentsResourceWithRawResponse(self._v1.identity_documents)

    @cached_property
    def languages(self) -> LanguagesResourceWithRawResponse:
        return LanguagesResourceWithRawResponse(self._v1.languages)

    @cached_property
    def loyalty_memberships(self) -> LoyaltyMembershipsResourceWithRawResponse:
        return LoyaltyMembershipsResourceWithRawResponse(self._v1.loyalty_memberships)

    @cached_property
    def loyalty_programs(self) -> LoyaltyProgramsResourceWithRawResponse:
        return LoyaltyProgramsResourceWithRawResponse(self._v1.loyalty_programs)

    @cached_property
    def loyalty_tiers(self) -> LoyaltyTiersResourceWithRawResponse:
        return LoyaltyTiersResourceWithRawResponse(self._v1.loyalty_tiers)

    @cached_property
    def message_threads(self) -> MessageThreadsResourceWithRawResponse:
        return MessageThreadsResourceWithRawResponse(self._v1.message_threads)

    @cached_property
    def messages(self) -> MessagesResourceWithRawResponse:
        return MessagesResourceWithRawResponse(self._v1.messages)

    @cached_property
    def order_items(self) -> OrderItemsResourceWithRawResponse:
        return OrderItemsResourceWithRawResponse(self._v1.order_items)

    @cached_property
    def payment_requests(self) -> PaymentRequestsResourceWithRawResponse:
        return PaymentRequestsResourceWithRawResponse(self._v1.payment_requests)

    @cached_property
    def payments(self) -> PaymentsResourceWithRawResponse:
        return PaymentsResourceWithRawResponse(self._v1.payments)

    @cached_property
    def products(self) -> ProductsResourceWithRawResponse:
        return ProductsResourceWithRawResponse(self._v1.products)

    @cached_property
    def rates(self) -> RatesResourceWithRawResponse:
        return RatesResourceWithRawResponse(self._v1.rates)

    @cached_property
    def reservations(self) -> ReservationsResourceWithRawResponse:
        return ReservationsResourceWithRawResponse(self._v1.reservations)

    @cached_property
    def resource_access_tokens(self) -> ResourceAccessTokensResourceWithRawResponse:
        return ResourceAccessTokensResourceWithRawResponse(self._v1.resource_access_tokens)

    @cached_property
    def resource_blocks(self) -> ResourceBlocksResourceWithRawResponse:
        return ResourceBlocksResourceWithRawResponse(self._v1.resource_blocks)

    @cached_property
    def resources(self) -> ResourcesResourceWithRawResponse:
        return ResourcesResourceWithRawResponse(self._v1.resources)

    @cached_property
    def restrictions(self) -> RestrictionsResourceWithRawResponse:
        return RestrictionsResourceWithRawResponse(self._v1.restrictions)

    @cached_property
    def routing_rules(self) -> RoutingRulesResourceWithRawResponse:
        return RoutingRulesResourceWithRawResponse(self._v1.routing_rules)

    @cached_property
    def service_order_notes(self) -> ServiceOrderNotesResourceWithRawResponse:
        return ServiceOrderNotesResourceWithRawResponse(self._v1.service_order_notes)

    @cached_property
    def service_overbooking_limits(self) -> ServiceOverbookingLimitsResourceWithRawResponse:
        return ServiceOverbookingLimitsResourceWithRawResponse(self._v1.service_overbooking_limits)

    @cached_property
    def services(self) -> ServicesResourceWithRawResponse:
        return ServicesResourceWithRawResponse(self._v1.services)

    @cached_property
    def tasks(self) -> TasksResourceWithRawResponse:
        return TasksResourceWithRawResponse(self._v1.tasks)

    @cached_property
    def voucher_codes(self) -> VoucherCodesResourceWithRawResponse:
        return VoucherCodesResourceWithRawResponse(self._v1.voucher_codes)

    @cached_property
    def vouchers(self) -> VouchersResourceWithRawResponse:
        return VouchersResourceWithRawResponse(self._v1.vouchers)


class AsyncV1ResourceWithRawResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.add_order = async_to_raw_response_wrapper(
            v1.add_order,
        )
        self.add_outlet_bill = async_to_raw_response_wrapper(
            v1.add_outlet_bill,
        )
        self.get_all_source_assignments = async_to_raw_response_wrapper(
            v1.get_all_source_assignments,
        )
        self.get_all_source_assignments_2024_09_20 = async_to_raw_response_wrapper(
            v1.get_all_source_assignments_2024_09_20,
        )
        self.get_configuration = async_to_raw_response_wrapper(
            v1.get_configuration,
        )
        self.get_image_urls = async_to_raw_response_wrapper(
            v1.get_image_urls,
        )
        self.list_accounting_categories = async_to_raw_response_wrapper(
            v1.list_accounting_categories,
        )
        self.list_age_categories = async_to_raw_response_wrapper(
            v1.list_age_categories,
        )
        self.list_availability_adjustments = async_to_raw_response_wrapper(
            v1.list_availability_adjustments,
        )
        self.list_business_segments = async_to_raw_response_wrapper(
            v1.list_business_segments,
        )
        self.list_cashier_transactions = async_to_raw_response_wrapper(
            v1.list_cashier_transactions,
        )
        self.list_cashiers = async_to_raw_response_wrapper(
            v1.list_cashiers,
        )
        self.list_companionships = async_to_raw_response_wrapper(
            v1.list_companionships,
        )
        self.list_counters = async_to_raw_response_wrapper(
            v1.list_counters,
        )
        self.list_countries = async_to_raw_response_wrapper(
            v1.list_countries,
        )
        self.list_currencies = async_to_raw_response_wrapper(
            v1.list_currencies,
        )
        self.list_departments = async_to_raw_response_wrapper(
            v1.list_departments,
        )
        self.list_devices = async_to_raw_response_wrapper(
            v1.list_devices,
        )
        self.list_enterprises = async_to_raw_response_wrapper(
            v1.list_enterprises,
        )
        self.list_exchange_rates = async_to_raw_response_wrapper(
            v1.list_exchange_rates,
        )
        self.list_ledger_balances = async_to_raw_response_wrapper(
            v1.list_ledger_balances,
        )
        self.list_outlet_items = async_to_raw_response_wrapper(
            v1.list_outlet_items,
        )
        self.list_outlets = async_to_raw_response_wrapper(
            v1.list_outlets,
        )
        self.list_preauthorizations_by_customers = async_to_raw_response_wrapper(
            v1.list_preauthorizations_by_customers,
        )
        self.list_product_categories = async_to_raw_response_wrapper(
            v1.list_product_categories,
        )
        self.list_product_service_orders = async_to_raw_response_wrapper(
            v1.list_product_service_orders,
        )
        self.list_rate_groups = async_to_raw_response_wrapper(
            v1.list_rate_groups,
        )
        self.list_reservation_groups = async_to_raw_response_wrapper(
            v1.list_reservation_groups,
        )
        self.list_resource_categories = async_to_raw_response_wrapper(
            v1.list_resource_categories,
        )
        self.list_resource_category_assignments = async_to_raw_response_wrapper(
            v1.list_resource_category_assignments,
        )
        self.list_resource_category_image_assignments = async_to_raw_response_wrapper(
            v1.list_resource_category_image_assignments,
        )
        self.list_resource_feature_assignments = async_to_raw_response_wrapper(
            v1.list_resource_feature_assignments,
        )
        self.list_resource_features = async_to_raw_response_wrapper(
            v1.list_resource_features,
        )
        self.list_rules = async_to_raw_response_wrapper(
            v1.list_rules,
        )
        self.list_sources = async_to_raw_response_wrapper(
            v1.list_sources,
        )
        self.list_tax_environments = async_to_raw_response_wrapper(
            v1.list_tax_environments,
        )
        self.list_taxations = async_to_raw_response_wrapper(
            v1.list_taxations,
        )

    @cached_property
    def account_notes(self) -> AsyncAccountNotesResourceWithRawResponse:
        return AsyncAccountNotesResourceWithRawResponse(self._v1.account_notes)

    @cached_property
    def accounting_items(self) -> AsyncAccountingItemsResourceWithRawResponse:
        return AsyncAccountingItemsResourceWithRawResponse(self._v1.accounting_items)

    @cached_property
    def accounts(self) -> AsyncAccountsResourceWithRawResponse:
        return AsyncAccountsResourceWithRawResponse(self._v1.accounts)

    @cached_property
    def addresses(self) -> AsyncAddressesResourceWithRawResponse:
        return AsyncAddressesResourceWithRawResponse(self._v1.addresses)

    @cached_property
    def availability_blocks(self) -> AsyncAvailabilityBlocksResourceWithRawResponse:
        return AsyncAvailabilityBlocksResourceWithRawResponse(self._v1.availability_blocks)

    @cached_property
    def bills(self) -> AsyncBillsResourceWithRawResponse:
        return AsyncBillsResourceWithRawResponse(self._v1.bills)

    @cached_property
    def cancellation_policies(self) -> AsyncCancellationPoliciesResourceWithRawResponse:
        return AsyncCancellationPoliciesResourceWithRawResponse(self._v1.cancellation_policies)

    @cached_property
    def commands(self) -> AsyncCommandsResourceWithRawResponse:
        return AsyncCommandsResourceWithRawResponse(self._v1.commands)

    @cached_property
    def companies(self) -> AsyncCompaniesResourceWithRawResponse:
        return AsyncCompaniesResourceWithRawResponse(self._v1.companies)

    @cached_property
    def company_contracts(self) -> AsyncCompanyContractsResourceWithRawResponse:
        return AsyncCompanyContractsResourceWithRawResponse(self._v1.company_contracts)

    @cached_property
    def credit_cards(self) -> AsyncCreditCardsResourceWithRawResponse:
        return AsyncCreditCardsResourceWithRawResponse(self._v1.credit_cards)

    @cached_property
    def customers(self) -> AsyncCustomersResourceWithRawResponse:
        return AsyncCustomersResourceWithRawResponse(self._v1.customers)

    @cached_property
    def exports(self) -> AsyncExportsResourceWithRawResponse:
        return AsyncExportsResourceWithRawResponse(self._v1.exports)

    @cached_property
    def identity_documents(self) -> AsyncIdentityDocumentsResourceWithRawResponse:
        return AsyncIdentityDocumentsResourceWithRawResponse(self._v1.identity_documents)

    @cached_property
    def languages(self) -> AsyncLanguagesResourceWithRawResponse:
        return AsyncLanguagesResourceWithRawResponse(self._v1.languages)

    @cached_property
    def loyalty_memberships(self) -> AsyncLoyaltyMembershipsResourceWithRawResponse:
        return AsyncLoyaltyMembershipsResourceWithRawResponse(self._v1.loyalty_memberships)

    @cached_property
    def loyalty_programs(self) -> AsyncLoyaltyProgramsResourceWithRawResponse:
        return AsyncLoyaltyProgramsResourceWithRawResponse(self._v1.loyalty_programs)

    @cached_property
    def loyalty_tiers(self) -> AsyncLoyaltyTiersResourceWithRawResponse:
        return AsyncLoyaltyTiersResourceWithRawResponse(self._v1.loyalty_tiers)

    @cached_property
    def message_threads(self) -> AsyncMessageThreadsResourceWithRawResponse:
        return AsyncMessageThreadsResourceWithRawResponse(self._v1.message_threads)

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithRawResponse:
        return AsyncMessagesResourceWithRawResponse(self._v1.messages)

    @cached_property
    def order_items(self) -> AsyncOrderItemsResourceWithRawResponse:
        return AsyncOrderItemsResourceWithRawResponse(self._v1.order_items)

    @cached_property
    def payment_requests(self) -> AsyncPaymentRequestsResourceWithRawResponse:
        return AsyncPaymentRequestsResourceWithRawResponse(self._v1.payment_requests)

    @cached_property
    def payments(self) -> AsyncPaymentsResourceWithRawResponse:
        return AsyncPaymentsResourceWithRawResponse(self._v1.payments)

    @cached_property
    def products(self) -> AsyncProductsResourceWithRawResponse:
        return AsyncProductsResourceWithRawResponse(self._v1.products)

    @cached_property
    def rates(self) -> AsyncRatesResourceWithRawResponse:
        return AsyncRatesResourceWithRawResponse(self._v1.rates)

    @cached_property
    def reservations(self) -> AsyncReservationsResourceWithRawResponse:
        return AsyncReservationsResourceWithRawResponse(self._v1.reservations)

    @cached_property
    def resource_access_tokens(self) -> AsyncResourceAccessTokensResourceWithRawResponse:
        return AsyncResourceAccessTokensResourceWithRawResponse(self._v1.resource_access_tokens)

    @cached_property
    def resource_blocks(self) -> AsyncResourceBlocksResourceWithRawResponse:
        return AsyncResourceBlocksResourceWithRawResponse(self._v1.resource_blocks)

    @cached_property
    def resources(self) -> AsyncResourcesResourceWithRawResponse:
        return AsyncResourcesResourceWithRawResponse(self._v1.resources)

    @cached_property
    def restrictions(self) -> AsyncRestrictionsResourceWithRawResponse:
        return AsyncRestrictionsResourceWithRawResponse(self._v1.restrictions)

    @cached_property
    def routing_rules(self) -> AsyncRoutingRulesResourceWithRawResponse:
        return AsyncRoutingRulesResourceWithRawResponse(self._v1.routing_rules)

    @cached_property
    def service_order_notes(self) -> AsyncServiceOrderNotesResourceWithRawResponse:
        return AsyncServiceOrderNotesResourceWithRawResponse(self._v1.service_order_notes)

    @cached_property
    def service_overbooking_limits(self) -> AsyncServiceOverbookingLimitsResourceWithRawResponse:
        return AsyncServiceOverbookingLimitsResourceWithRawResponse(self._v1.service_overbooking_limits)

    @cached_property
    def services(self) -> AsyncServicesResourceWithRawResponse:
        return AsyncServicesResourceWithRawResponse(self._v1.services)

    @cached_property
    def tasks(self) -> AsyncTasksResourceWithRawResponse:
        return AsyncTasksResourceWithRawResponse(self._v1.tasks)

    @cached_property
    def voucher_codes(self) -> AsyncVoucherCodesResourceWithRawResponse:
        return AsyncVoucherCodesResourceWithRawResponse(self._v1.voucher_codes)

    @cached_property
    def vouchers(self) -> AsyncVouchersResourceWithRawResponse:
        return AsyncVouchersResourceWithRawResponse(self._v1.vouchers)


class V1ResourceWithStreamingResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.add_order = to_streamed_response_wrapper(
            v1.add_order,
        )
        self.add_outlet_bill = to_streamed_response_wrapper(
            v1.add_outlet_bill,
        )
        self.get_all_source_assignments = to_streamed_response_wrapper(
            v1.get_all_source_assignments,
        )
        self.get_all_source_assignments_2024_09_20 = to_streamed_response_wrapper(
            v1.get_all_source_assignments_2024_09_20,
        )
        self.get_configuration = to_streamed_response_wrapper(
            v1.get_configuration,
        )
        self.get_image_urls = to_streamed_response_wrapper(
            v1.get_image_urls,
        )
        self.list_accounting_categories = to_streamed_response_wrapper(
            v1.list_accounting_categories,
        )
        self.list_age_categories = to_streamed_response_wrapper(
            v1.list_age_categories,
        )
        self.list_availability_adjustments = to_streamed_response_wrapper(
            v1.list_availability_adjustments,
        )
        self.list_business_segments = to_streamed_response_wrapper(
            v1.list_business_segments,
        )
        self.list_cashier_transactions = to_streamed_response_wrapper(
            v1.list_cashier_transactions,
        )
        self.list_cashiers = to_streamed_response_wrapper(
            v1.list_cashiers,
        )
        self.list_companionships = to_streamed_response_wrapper(
            v1.list_companionships,
        )
        self.list_counters = to_streamed_response_wrapper(
            v1.list_counters,
        )
        self.list_countries = to_streamed_response_wrapper(
            v1.list_countries,
        )
        self.list_currencies = to_streamed_response_wrapper(
            v1.list_currencies,
        )
        self.list_departments = to_streamed_response_wrapper(
            v1.list_departments,
        )
        self.list_devices = to_streamed_response_wrapper(
            v1.list_devices,
        )
        self.list_enterprises = to_streamed_response_wrapper(
            v1.list_enterprises,
        )
        self.list_exchange_rates = to_streamed_response_wrapper(
            v1.list_exchange_rates,
        )
        self.list_ledger_balances = to_streamed_response_wrapper(
            v1.list_ledger_balances,
        )
        self.list_outlet_items = to_streamed_response_wrapper(
            v1.list_outlet_items,
        )
        self.list_outlets = to_streamed_response_wrapper(
            v1.list_outlets,
        )
        self.list_preauthorizations_by_customers = to_streamed_response_wrapper(
            v1.list_preauthorizations_by_customers,
        )
        self.list_product_categories = to_streamed_response_wrapper(
            v1.list_product_categories,
        )
        self.list_product_service_orders = to_streamed_response_wrapper(
            v1.list_product_service_orders,
        )
        self.list_rate_groups = to_streamed_response_wrapper(
            v1.list_rate_groups,
        )
        self.list_reservation_groups = to_streamed_response_wrapper(
            v1.list_reservation_groups,
        )
        self.list_resource_categories = to_streamed_response_wrapper(
            v1.list_resource_categories,
        )
        self.list_resource_category_assignments = to_streamed_response_wrapper(
            v1.list_resource_category_assignments,
        )
        self.list_resource_category_image_assignments = to_streamed_response_wrapper(
            v1.list_resource_category_image_assignments,
        )
        self.list_resource_feature_assignments = to_streamed_response_wrapper(
            v1.list_resource_feature_assignments,
        )
        self.list_resource_features = to_streamed_response_wrapper(
            v1.list_resource_features,
        )
        self.list_rules = to_streamed_response_wrapper(
            v1.list_rules,
        )
        self.list_sources = to_streamed_response_wrapper(
            v1.list_sources,
        )
        self.list_tax_environments = to_streamed_response_wrapper(
            v1.list_tax_environments,
        )
        self.list_taxations = to_streamed_response_wrapper(
            v1.list_taxations,
        )

    @cached_property
    def account_notes(self) -> AccountNotesResourceWithStreamingResponse:
        return AccountNotesResourceWithStreamingResponse(self._v1.account_notes)

    @cached_property
    def accounting_items(self) -> AccountingItemsResourceWithStreamingResponse:
        return AccountingItemsResourceWithStreamingResponse(self._v1.accounting_items)

    @cached_property
    def accounts(self) -> AccountsResourceWithStreamingResponse:
        return AccountsResourceWithStreamingResponse(self._v1.accounts)

    @cached_property
    def addresses(self) -> AddressesResourceWithStreamingResponse:
        return AddressesResourceWithStreamingResponse(self._v1.addresses)

    @cached_property
    def availability_blocks(self) -> AvailabilityBlocksResourceWithStreamingResponse:
        return AvailabilityBlocksResourceWithStreamingResponse(self._v1.availability_blocks)

    @cached_property
    def bills(self) -> BillsResourceWithStreamingResponse:
        return BillsResourceWithStreamingResponse(self._v1.bills)

    @cached_property
    def cancellation_policies(self) -> CancellationPoliciesResourceWithStreamingResponse:
        return CancellationPoliciesResourceWithStreamingResponse(self._v1.cancellation_policies)

    @cached_property
    def commands(self) -> CommandsResourceWithStreamingResponse:
        return CommandsResourceWithStreamingResponse(self._v1.commands)

    @cached_property
    def companies(self) -> CompaniesResourceWithStreamingResponse:
        return CompaniesResourceWithStreamingResponse(self._v1.companies)

    @cached_property
    def company_contracts(self) -> CompanyContractsResourceWithStreamingResponse:
        return CompanyContractsResourceWithStreamingResponse(self._v1.company_contracts)

    @cached_property
    def credit_cards(self) -> CreditCardsResourceWithStreamingResponse:
        return CreditCardsResourceWithStreamingResponse(self._v1.credit_cards)

    @cached_property
    def customers(self) -> CustomersResourceWithStreamingResponse:
        return CustomersResourceWithStreamingResponse(self._v1.customers)

    @cached_property
    def exports(self) -> ExportsResourceWithStreamingResponse:
        return ExportsResourceWithStreamingResponse(self._v1.exports)

    @cached_property
    def identity_documents(self) -> IdentityDocumentsResourceWithStreamingResponse:
        return IdentityDocumentsResourceWithStreamingResponse(self._v1.identity_documents)

    @cached_property
    def languages(self) -> LanguagesResourceWithStreamingResponse:
        return LanguagesResourceWithStreamingResponse(self._v1.languages)

    @cached_property
    def loyalty_memberships(self) -> LoyaltyMembershipsResourceWithStreamingResponse:
        return LoyaltyMembershipsResourceWithStreamingResponse(self._v1.loyalty_memberships)

    @cached_property
    def loyalty_programs(self) -> LoyaltyProgramsResourceWithStreamingResponse:
        return LoyaltyProgramsResourceWithStreamingResponse(self._v1.loyalty_programs)

    @cached_property
    def loyalty_tiers(self) -> LoyaltyTiersResourceWithStreamingResponse:
        return LoyaltyTiersResourceWithStreamingResponse(self._v1.loyalty_tiers)

    @cached_property
    def message_threads(self) -> MessageThreadsResourceWithStreamingResponse:
        return MessageThreadsResourceWithStreamingResponse(self._v1.message_threads)

    @cached_property
    def messages(self) -> MessagesResourceWithStreamingResponse:
        return MessagesResourceWithStreamingResponse(self._v1.messages)

    @cached_property
    def order_items(self) -> OrderItemsResourceWithStreamingResponse:
        return OrderItemsResourceWithStreamingResponse(self._v1.order_items)

    @cached_property
    def payment_requests(self) -> PaymentRequestsResourceWithStreamingResponse:
        return PaymentRequestsResourceWithStreamingResponse(self._v1.payment_requests)

    @cached_property
    def payments(self) -> PaymentsResourceWithStreamingResponse:
        return PaymentsResourceWithStreamingResponse(self._v1.payments)

    @cached_property
    def products(self) -> ProductsResourceWithStreamingResponse:
        return ProductsResourceWithStreamingResponse(self._v1.products)

    @cached_property
    def rates(self) -> RatesResourceWithStreamingResponse:
        return RatesResourceWithStreamingResponse(self._v1.rates)

    @cached_property
    def reservations(self) -> ReservationsResourceWithStreamingResponse:
        return ReservationsResourceWithStreamingResponse(self._v1.reservations)

    @cached_property
    def resource_access_tokens(self) -> ResourceAccessTokensResourceWithStreamingResponse:
        return ResourceAccessTokensResourceWithStreamingResponse(self._v1.resource_access_tokens)

    @cached_property
    def resource_blocks(self) -> ResourceBlocksResourceWithStreamingResponse:
        return ResourceBlocksResourceWithStreamingResponse(self._v1.resource_blocks)

    @cached_property
    def resources(self) -> ResourcesResourceWithStreamingResponse:
        return ResourcesResourceWithStreamingResponse(self._v1.resources)

    @cached_property
    def restrictions(self) -> RestrictionsResourceWithStreamingResponse:
        return RestrictionsResourceWithStreamingResponse(self._v1.restrictions)

    @cached_property
    def routing_rules(self) -> RoutingRulesResourceWithStreamingResponse:
        return RoutingRulesResourceWithStreamingResponse(self._v1.routing_rules)

    @cached_property
    def service_order_notes(self) -> ServiceOrderNotesResourceWithStreamingResponse:
        return ServiceOrderNotesResourceWithStreamingResponse(self._v1.service_order_notes)

    @cached_property
    def service_overbooking_limits(self) -> ServiceOverbookingLimitsResourceWithStreamingResponse:
        return ServiceOverbookingLimitsResourceWithStreamingResponse(self._v1.service_overbooking_limits)

    @cached_property
    def services(self) -> ServicesResourceWithStreamingResponse:
        return ServicesResourceWithStreamingResponse(self._v1.services)

    @cached_property
    def tasks(self) -> TasksResourceWithStreamingResponse:
        return TasksResourceWithStreamingResponse(self._v1.tasks)

    @cached_property
    def voucher_codes(self) -> VoucherCodesResourceWithStreamingResponse:
        return VoucherCodesResourceWithStreamingResponse(self._v1.voucher_codes)

    @cached_property
    def vouchers(self) -> VouchersResourceWithStreamingResponse:
        return VouchersResourceWithStreamingResponse(self._v1.vouchers)


class AsyncV1ResourceWithStreamingResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.add_order = async_to_streamed_response_wrapper(
            v1.add_order,
        )
        self.add_outlet_bill = async_to_streamed_response_wrapper(
            v1.add_outlet_bill,
        )
        self.get_all_source_assignments = async_to_streamed_response_wrapper(
            v1.get_all_source_assignments,
        )
        self.get_all_source_assignments_2024_09_20 = async_to_streamed_response_wrapper(
            v1.get_all_source_assignments_2024_09_20,
        )
        self.get_configuration = async_to_streamed_response_wrapper(
            v1.get_configuration,
        )
        self.get_image_urls = async_to_streamed_response_wrapper(
            v1.get_image_urls,
        )
        self.list_accounting_categories = async_to_streamed_response_wrapper(
            v1.list_accounting_categories,
        )
        self.list_age_categories = async_to_streamed_response_wrapper(
            v1.list_age_categories,
        )
        self.list_availability_adjustments = async_to_streamed_response_wrapper(
            v1.list_availability_adjustments,
        )
        self.list_business_segments = async_to_streamed_response_wrapper(
            v1.list_business_segments,
        )
        self.list_cashier_transactions = async_to_streamed_response_wrapper(
            v1.list_cashier_transactions,
        )
        self.list_cashiers = async_to_streamed_response_wrapper(
            v1.list_cashiers,
        )
        self.list_companionships = async_to_streamed_response_wrapper(
            v1.list_companionships,
        )
        self.list_counters = async_to_streamed_response_wrapper(
            v1.list_counters,
        )
        self.list_countries = async_to_streamed_response_wrapper(
            v1.list_countries,
        )
        self.list_currencies = async_to_streamed_response_wrapper(
            v1.list_currencies,
        )
        self.list_departments = async_to_streamed_response_wrapper(
            v1.list_departments,
        )
        self.list_devices = async_to_streamed_response_wrapper(
            v1.list_devices,
        )
        self.list_enterprises = async_to_streamed_response_wrapper(
            v1.list_enterprises,
        )
        self.list_exchange_rates = async_to_streamed_response_wrapper(
            v1.list_exchange_rates,
        )
        self.list_ledger_balances = async_to_streamed_response_wrapper(
            v1.list_ledger_balances,
        )
        self.list_outlet_items = async_to_streamed_response_wrapper(
            v1.list_outlet_items,
        )
        self.list_outlets = async_to_streamed_response_wrapper(
            v1.list_outlets,
        )
        self.list_preauthorizations_by_customers = async_to_streamed_response_wrapper(
            v1.list_preauthorizations_by_customers,
        )
        self.list_product_categories = async_to_streamed_response_wrapper(
            v1.list_product_categories,
        )
        self.list_product_service_orders = async_to_streamed_response_wrapper(
            v1.list_product_service_orders,
        )
        self.list_rate_groups = async_to_streamed_response_wrapper(
            v1.list_rate_groups,
        )
        self.list_reservation_groups = async_to_streamed_response_wrapper(
            v1.list_reservation_groups,
        )
        self.list_resource_categories = async_to_streamed_response_wrapper(
            v1.list_resource_categories,
        )
        self.list_resource_category_assignments = async_to_streamed_response_wrapper(
            v1.list_resource_category_assignments,
        )
        self.list_resource_category_image_assignments = async_to_streamed_response_wrapper(
            v1.list_resource_category_image_assignments,
        )
        self.list_resource_feature_assignments = async_to_streamed_response_wrapper(
            v1.list_resource_feature_assignments,
        )
        self.list_resource_features = async_to_streamed_response_wrapper(
            v1.list_resource_features,
        )
        self.list_rules = async_to_streamed_response_wrapper(
            v1.list_rules,
        )
        self.list_sources = async_to_streamed_response_wrapper(
            v1.list_sources,
        )
        self.list_tax_environments = async_to_streamed_response_wrapper(
            v1.list_tax_environments,
        )
        self.list_taxations = async_to_streamed_response_wrapper(
            v1.list_taxations,
        )

    @cached_property
    def account_notes(self) -> AsyncAccountNotesResourceWithStreamingResponse:
        return AsyncAccountNotesResourceWithStreamingResponse(self._v1.account_notes)

    @cached_property
    def accounting_items(self) -> AsyncAccountingItemsResourceWithStreamingResponse:
        return AsyncAccountingItemsResourceWithStreamingResponse(self._v1.accounting_items)

    @cached_property
    def accounts(self) -> AsyncAccountsResourceWithStreamingResponse:
        return AsyncAccountsResourceWithStreamingResponse(self._v1.accounts)

    @cached_property
    def addresses(self) -> AsyncAddressesResourceWithStreamingResponse:
        return AsyncAddressesResourceWithStreamingResponse(self._v1.addresses)

    @cached_property
    def availability_blocks(self) -> AsyncAvailabilityBlocksResourceWithStreamingResponse:
        return AsyncAvailabilityBlocksResourceWithStreamingResponse(self._v1.availability_blocks)

    @cached_property
    def bills(self) -> AsyncBillsResourceWithStreamingResponse:
        return AsyncBillsResourceWithStreamingResponse(self._v1.bills)

    @cached_property
    def cancellation_policies(self) -> AsyncCancellationPoliciesResourceWithStreamingResponse:
        return AsyncCancellationPoliciesResourceWithStreamingResponse(self._v1.cancellation_policies)

    @cached_property
    def commands(self) -> AsyncCommandsResourceWithStreamingResponse:
        return AsyncCommandsResourceWithStreamingResponse(self._v1.commands)

    @cached_property
    def companies(self) -> AsyncCompaniesResourceWithStreamingResponse:
        return AsyncCompaniesResourceWithStreamingResponse(self._v1.companies)

    @cached_property
    def company_contracts(self) -> AsyncCompanyContractsResourceWithStreamingResponse:
        return AsyncCompanyContractsResourceWithStreamingResponse(self._v1.company_contracts)

    @cached_property
    def credit_cards(self) -> AsyncCreditCardsResourceWithStreamingResponse:
        return AsyncCreditCardsResourceWithStreamingResponse(self._v1.credit_cards)

    @cached_property
    def customers(self) -> AsyncCustomersResourceWithStreamingResponse:
        return AsyncCustomersResourceWithStreamingResponse(self._v1.customers)

    @cached_property
    def exports(self) -> AsyncExportsResourceWithStreamingResponse:
        return AsyncExportsResourceWithStreamingResponse(self._v1.exports)

    @cached_property
    def identity_documents(self) -> AsyncIdentityDocumentsResourceWithStreamingResponse:
        return AsyncIdentityDocumentsResourceWithStreamingResponse(self._v1.identity_documents)

    @cached_property
    def languages(self) -> AsyncLanguagesResourceWithStreamingResponse:
        return AsyncLanguagesResourceWithStreamingResponse(self._v1.languages)

    @cached_property
    def loyalty_memberships(self) -> AsyncLoyaltyMembershipsResourceWithStreamingResponse:
        return AsyncLoyaltyMembershipsResourceWithStreamingResponse(self._v1.loyalty_memberships)

    @cached_property
    def loyalty_programs(self) -> AsyncLoyaltyProgramsResourceWithStreamingResponse:
        return AsyncLoyaltyProgramsResourceWithStreamingResponse(self._v1.loyalty_programs)

    @cached_property
    def loyalty_tiers(self) -> AsyncLoyaltyTiersResourceWithStreamingResponse:
        return AsyncLoyaltyTiersResourceWithStreamingResponse(self._v1.loyalty_tiers)

    @cached_property
    def message_threads(self) -> AsyncMessageThreadsResourceWithStreamingResponse:
        return AsyncMessageThreadsResourceWithStreamingResponse(self._v1.message_threads)

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithStreamingResponse:
        return AsyncMessagesResourceWithStreamingResponse(self._v1.messages)

    @cached_property
    def order_items(self) -> AsyncOrderItemsResourceWithStreamingResponse:
        return AsyncOrderItemsResourceWithStreamingResponse(self._v1.order_items)

    @cached_property
    def payment_requests(self) -> AsyncPaymentRequestsResourceWithStreamingResponse:
        return AsyncPaymentRequestsResourceWithStreamingResponse(self._v1.payment_requests)

    @cached_property
    def payments(self) -> AsyncPaymentsResourceWithStreamingResponse:
        return AsyncPaymentsResourceWithStreamingResponse(self._v1.payments)

    @cached_property
    def products(self) -> AsyncProductsResourceWithStreamingResponse:
        return AsyncProductsResourceWithStreamingResponse(self._v1.products)

    @cached_property
    def rates(self) -> AsyncRatesResourceWithStreamingResponse:
        return AsyncRatesResourceWithStreamingResponse(self._v1.rates)

    @cached_property
    def reservations(self) -> AsyncReservationsResourceWithStreamingResponse:
        return AsyncReservationsResourceWithStreamingResponse(self._v1.reservations)

    @cached_property
    def resource_access_tokens(self) -> AsyncResourceAccessTokensResourceWithStreamingResponse:
        return AsyncResourceAccessTokensResourceWithStreamingResponse(self._v1.resource_access_tokens)

    @cached_property
    def resource_blocks(self) -> AsyncResourceBlocksResourceWithStreamingResponse:
        return AsyncResourceBlocksResourceWithStreamingResponse(self._v1.resource_blocks)

    @cached_property
    def resources(self) -> AsyncResourcesResourceWithStreamingResponse:
        return AsyncResourcesResourceWithStreamingResponse(self._v1.resources)

    @cached_property
    def restrictions(self) -> AsyncRestrictionsResourceWithStreamingResponse:
        return AsyncRestrictionsResourceWithStreamingResponse(self._v1.restrictions)

    @cached_property
    def routing_rules(self) -> AsyncRoutingRulesResourceWithStreamingResponse:
        return AsyncRoutingRulesResourceWithStreamingResponse(self._v1.routing_rules)

    @cached_property
    def service_order_notes(self) -> AsyncServiceOrderNotesResourceWithStreamingResponse:
        return AsyncServiceOrderNotesResourceWithStreamingResponse(self._v1.service_order_notes)

    @cached_property
    def service_overbooking_limits(self) -> AsyncServiceOverbookingLimitsResourceWithStreamingResponse:
        return AsyncServiceOverbookingLimitsResourceWithStreamingResponse(self._v1.service_overbooking_limits)

    @cached_property
    def services(self) -> AsyncServicesResourceWithStreamingResponse:
        return AsyncServicesResourceWithStreamingResponse(self._v1.services)

    @cached_property
    def tasks(self) -> AsyncTasksResourceWithStreamingResponse:
        return AsyncTasksResourceWithStreamingResponse(self._v1.tasks)

    @cached_property
    def voucher_codes(self) -> AsyncVoucherCodesResourceWithStreamingResponse:
        return AsyncVoucherCodesResourceWithStreamingResponse(self._v1.voucher_codes)

    @cached_property
    def vouchers(self) -> AsyncVouchersResourceWithStreamingResponse:
        return AsyncVouchersResourceWithStreamingResponse(self._v1.vouchers)
