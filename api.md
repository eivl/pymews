# API

## Connector

### V1

Types:

```python
from pymews.types.api.connector import (
    AddCreditCardResult,
    MultipleCustomerParameters,
    Parameters,
    Unit,
    V1AddOrderResponse,
    V1AddOutletBillResponse,
    V1GetAllSourceAssignmentsResponse,
    V1GetAllSourceAssignments2024_09_20Response,
    V1GetConfigurationResponse,
    V1GetImageURLsResponse,
    V1ListAccountingCategoriesResponse,
    V1ListAgeCategoriesResponse,
    V1ListAvailabilityAdjustmentsResponse,
    V1ListBusinessSegmentsResponse,
    V1ListCashierTransactionsResponse,
    V1ListCashiersResponse,
    V1ListCompanionshipsResponse,
    V1ListCountersResponse,
    V1ListCountriesResponse,
    V1ListCurrenciesResponse,
    V1ListDepartmentsResponse,
    V1ListDevicesResponse,
    V1ListEnterprisesResponse,
    V1ListExchangeRatesResponse,
    V1ListLedgerBalancesResponse,
    V1ListOutletItemsResponse,
    V1ListOutletsResponse,
    V1ListPreauthorizationsByCustomersResponse,
    V1ListProductCategoriesResponse,
    V1ListProductServiceOrdersResponse,
    V1ListRateGroupsResponse,
    V1ListReservationGroupsResponse,
    V1ListResourceCategoriesResponse,
    V1ListResourceCategoryAssignmentsResponse,
    V1ListResourceCategoryImageAssignmentsResponse,
    V1ListResourceFeatureAssignmentsResponse,
    V1ListResourceFeaturesResponse,
    V1ListRulesResponse,
    V1ListSourcesResponse,
    V1ListTaxEnvironmentsResponse,
    V1ListTaxationsResponse,
)
```

Methods:

- <code title="post /api/connector/v1/orders/add">client.api.connector.v1.<a href="./src/pymews/resources/api/connector/v1/v1.py">add_order</a>(\*\*<a href="src/pymews/types/api/connector/v1_add_order_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1_add_order_response.py">V1AddOrderResponse</a></code>
- <code title="post /api/connector/v1/outletBills/add">client.api.connector.v1.<a href="./src/pymews/resources/api/connector/v1/v1.py">add_outlet_bill</a>(\*\*<a href="src/pymews/types/api/connector/v1_add_outlet_bill_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1_add_outlet_bill_response.py">V1AddOutletBillResponse</a></code>
- <code title="post /api/connector/v1/sourceAssignments/getAll">client.api.connector.v1.<a href="./src/pymews/resources/api/connector/v1/v1.py">get_all_source_assignments</a>(\*\*<a href="src/pymews/types/api/connector/v1_get_all_source_assignments_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1_get_all_source_assignments_response.py">V1GetAllSourceAssignmentsResponse</a></code>
- <code title="post /api/connector/v1/sourceAssignments/getAll/2024-09-20">client.api.connector.v1.<a href="./src/pymews/resources/api/connector/v1/v1.py">get_all_source_assignments_2024_09_20</a>(\*\*<a href="src/pymews/types/api/connector/v1_get_all_source_assignments_2024_09_20_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1_get_all_source_assignments_2024_09_20_response.py">V1GetAllSourceAssignments2024_09_20Response</a></code>
- <code title="post /api/connector/v1/configuration/get">client.api.connector.v1.<a href="./src/pymews/resources/api/connector/v1/v1.py">get_configuration</a>(\*\*<a href="src/pymews/types/api/connector/v1_get_configuration_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1_get_configuration_response.py">V1GetConfigurationResponse</a></code>
- <code title="post /api/connector/v1/images/getUrls">client.api.connector.v1.<a href="./src/pymews/resources/api/connector/v1/v1.py">get_image_urls</a>(\*\*<a href="src/pymews/types/api/connector/v1_get_image_urls_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1_get_image_urls_response.py">V1GetImageURLsResponse</a></code>
- <code title="post /api/connector/v1/accountingCategories/getAll">client.api.connector.v1.<a href="./src/pymews/resources/api/connector/v1/v1.py">list_accounting_categories</a>(\*\*<a href="src/pymews/types/api/connector/v1_list_accounting_categories_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1_list_accounting_categories_response.py">V1ListAccountingCategoriesResponse</a></code>
- <code title="post /api/connector/v1/ageCategories/getAll">client.api.connector.v1.<a href="./src/pymews/resources/api/connector/v1/v1.py">list_age_categories</a>(\*\*<a href="src/pymews/types/api/connector/v1_list_age_categories_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1_list_age_categories_response.py">V1ListAgeCategoriesResponse</a></code>
- <code title="post /api/connector/v1/availabilityAdjustments/getAll">client.api.connector.v1.<a href="./src/pymews/resources/api/connector/v1/v1.py">list_availability_adjustments</a>(\*\*<a href="src/pymews/types/api/connector/v1_list_availability_adjustments_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1_list_availability_adjustments_response.py">V1ListAvailabilityAdjustmentsResponse</a></code>
- <code title="post /api/connector/v1/businessSegments/getAll">client.api.connector.v1.<a href="./src/pymews/resources/api/connector/v1/v1.py">list_business_segments</a>(\*\*<a href="src/pymews/types/api/connector/v1_list_business_segments_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1_list_business_segments_response.py">V1ListBusinessSegmentsResponse</a></code>
- <code title="post /api/connector/v1/cashierTransactions/getAll">client.api.connector.v1.<a href="./src/pymews/resources/api/connector/v1/v1.py">list_cashier_transactions</a>(\*\*<a href="src/pymews/types/api/connector/v1_list_cashier_transactions_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1_list_cashier_transactions_response.py">V1ListCashierTransactionsResponse</a></code>
- <code title="post /api/connector/v1/cashiers/getAll">client.api.connector.v1.<a href="./src/pymews/resources/api/connector/v1/v1.py">list_cashiers</a>(\*\*<a href="src/pymews/types/api/connector/v1_list_cashiers_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1_list_cashiers_response.py">V1ListCashiersResponse</a></code>
- <code title="post /api/connector/v1/companionships/getAll">client.api.connector.v1.<a href="./src/pymews/resources/api/connector/v1/v1.py">list_companionships</a>(\*\*<a href="src/pymews/types/api/connector/v1_list_companionships_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1_list_companionships_response.py">V1ListCompanionshipsResponse</a></code>
- <code title="post /api/connector/v1/counters/getAll">client.api.connector.v1.<a href="./src/pymews/resources/api/connector/v1/v1.py">list_counters</a>(\*\*<a href="src/pymews/types/api/connector/v1_list_counters_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1_list_counters_response.py">V1ListCountersResponse</a></code>
- <code title="post /api/connector/v1/countries/getAll">client.api.connector.v1.<a href="./src/pymews/resources/api/connector/v1/v1.py">list_countries</a>(\*\*<a href="src/pymews/types/api/connector/v1_list_countries_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1_list_countries_response.py">V1ListCountriesResponse</a></code>
- <code title="post /api/connector/v1/currencies/getAll">client.api.connector.v1.<a href="./src/pymews/resources/api/connector/v1/v1.py">list_currencies</a>(\*\*<a href="src/pymews/types/api/connector/v1_list_currencies_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1_list_currencies_response.py">V1ListCurrenciesResponse</a></code>
- <code title="post /api/connector/v1/departments/getAll">client.api.connector.v1.<a href="./src/pymews/resources/api/connector/v1/v1.py">list_departments</a>(\*\*<a href="src/pymews/types/api/connector/v1_list_departments_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1_list_departments_response.py">V1ListDepartmentsResponse</a></code>
- <code title="post /api/connector/v1/devices/getAll">client.api.connector.v1.<a href="./src/pymews/resources/api/connector/v1/v1.py">list_devices</a>(\*\*<a href="src/pymews/types/api/connector/v1_list_devices_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1_list_devices_response.py">V1ListDevicesResponse</a></code>
- <code title="post /api/connector/v1/enterprises/getAll">client.api.connector.v1.<a href="./src/pymews/resources/api/connector/v1/v1.py">list_enterprises</a>(\*\*<a href="src/pymews/types/api/connector/v1_list_enterprises_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1_list_enterprises_response.py">V1ListEnterprisesResponse</a></code>
- <code title="post /api/connector/v1/exchangeRates/getAll">client.api.connector.v1.<a href="./src/pymews/resources/api/connector/v1/v1.py">list_exchange_rates</a>(\*\*<a href="src/pymews/types/api/connector/v1_list_exchange_rates_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1_list_exchange_rates_response.py">V1ListExchangeRatesResponse</a></code>
- <code title="post /api/connector/v1/ledgerBalances/getAll">client.api.connector.v1.<a href="./src/pymews/resources/api/connector/v1/v1.py">list_ledger_balances</a>(\*\*<a href="src/pymews/types/api/connector/v1_list_ledger_balances_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1_list_ledger_balances_response.py">V1ListLedgerBalancesResponse</a></code>
- <code title="post /api/connector/v1/outletItems/getAll">client.api.connector.v1.<a href="./src/pymews/resources/api/connector/v1/v1.py">list_outlet_items</a>(\*\*<a href="src/pymews/types/api/connector/v1_list_outlet_items_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1_list_outlet_items_response.py">V1ListOutletItemsResponse</a></code>
- <code title="post /api/connector/v1/outlets/getAll">client.api.connector.v1.<a href="./src/pymews/resources/api/connector/v1/v1.py">list_outlets</a>(\*\*<a href="src/pymews/types/api/connector/v1_list_outlets_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1_list_outlets_response.py">V1ListOutletsResponse</a></code>
- <code title="post /api/connector/v1/preauthorizations/getAllByCustomers">client.api.connector.v1.<a href="./src/pymews/resources/api/connector/v1/v1.py">list_preauthorizations_by_customers</a>(\*\*<a href="src/pymews/types/api/connector/v1_list_preauthorizations_by_customers_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1_list_preauthorizations_by_customers_response.py">V1ListPreauthorizationsByCustomersResponse</a></code>
- <code title="post /api/connector/v1/productCategories/getAll">client.api.connector.v1.<a href="./src/pymews/resources/api/connector/v1/v1.py">list_product_categories</a>(\*\*<a href="src/pymews/types/api/connector/v1_list_product_categories_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1_list_product_categories_response.py">V1ListProductCategoriesResponse</a></code>
- <code title="post /api/connector/v1/productServiceOrders/getAll">client.api.connector.v1.<a href="./src/pymews/resources/api/connector/v1/v1.py">list_product_service_orders</a>(\*\*<a href="src/pymews/types/api/connector/v1_list_product_service_orders_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1_list_product_service_orders_response.py">V1ListProductServiceOrdersResponse</a></code>
- <code title="post /api/connector/v1/rateGroups/getAll">client.api.connector.v1.<a href="./src/pymews/resources/api/connector/v1/v1.py">list_rate_groups</a>(\*\*<a href="src/pymews/types/api/connector/v1_list_rate_groups_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1_list_rate_groups_response.py">V1ListRateGroupsResponse</a></code>
- <code title="post /api/connector/v1/reservationGroups/getAll">client.api.connector.v1.<a href="./src/pymews/resources/api/connector/v1/v1.py">list_reservation_groups</a>(\*\*<a href="src/pymews/types/api/connector/v1_list_reservation_groups_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1_list_reservation_groups_response.py">V1ListReservationGroupsResponse</a></code>
- <code title="post /api/connector/v1/resourceCategories/getAll">client.api.connector.v1.<a href="./src/pymews/resources/api/connector/v1/v1.py">list_resource_categories</a>(\*\*<a href="src/pymews/types/api/connector/v1_list_resource_categories_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1_list_resource_categories_response.py">V1ListResourceCategoriesResponse</a></code>
- <code title="post /api/connector/v1/resourceCategoryAssignments/getAll">client.api.connector.v1.<a href="./src/pymews/resources/api/connector/v1/v1.py">list_resource_category_assignments</a>(\*\*<a href="src/pymews/types/api/connector/v1_list_resource_category_assignments_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1_list_resource_category_assignments_response.py">V1ListResourceCategoryAssignmentsResponse</a></code>
- <code title="post /api/connector/v1/resourceCategoryImageAssignments/getAll">client.api.connector.v1.<a href="./src/pymews/resources/api/connector/v1/v1.py">list_resource_category_image_assignments</a>(\*\*<a href="src/pymews/types/api/connector/v1_list_resource_category_image_assignments_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1_list_resource_category_image_assignments_response.py">V1ListResourceCategoryImageAssignmentsResponse</a></code>
- <code title="post /api/connector/v1/resourceFeatureAssignments/getAll">client.api.connector.v1.<a href="./src/pymews/resources/api/connector/v1/v1.py">list_resource_feature_assignments</a>(\*\*<a href="src/pymews/types/api/connector/v1_list_resource_feature_assignments_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1_list_resource_feature_assignments_response.py">V1ListResourceFeatureAssignmentsResponse</a></code>
- <code title="post /api/connector/v1/resourceFeatures/getAll">client.api.connector.v1.<a href="./src/pymews/resources/api/connector/v1/v1.py">list_resource_features</a>(\*\*<a href="src/pymews/types/api/connector/v1_list_resource_features_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1_list_resource_features_response.py">V1ListResourceFeaturesResponse</a></code>
- <code title="post /api/connector/v1/rules/getAll">client.api.connector.v1.<a href="./src/pymews/resources/api/connector/v1/v1.py">list_rules</a>(\*\*<a href="src/pymews/types/api/connector/v1_list_rules_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1_list_rules_response.py">V1ListRulesResponse</a></code>
- <code title="post /api/connector/v1/sources/getAll">client.api.connector.v1.<a href="./src/pymews/resources/api/connector/v1/v1.py">list_sources</a>(\*\*<a href="src/pymews/types/api/connector/v1_list_sources_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1_list_sources_response.py">V1ListSourcesResponse</a></code>
- <code title="post /api/connector/v1/taxEnvironments/getAll">client.api.connector.v1.<a href="./src/pymews/resources/api/connector/v1/v1.py">list_tax_environments</a>(\*\*<a href="src/pymews/types/api/connector/v1_list_tax_environments_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1_list_tax_environments_response.py">V1ListTaxEnvironmentsResponse</a></code>
- <code title="post /api/connector/v1/taxations/getAll">client.api.connector.v1.<a href="./src/pymews/resources/api/connector/v1/v1.py">list_taxations</a>(\*\*<a href="src/pymews/types/api/connector/v1_list_taxations_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1_list_taxations_response.py">V1ListTaxationsResponse</a></code>

#### AccountNotes

Types:

```python
from pymews.types.api.connector.v1 import (
    AccountNoteUpdateResponse,
    AccountNoteListResponse,
    AccountNoteAddResponse,
)
```

Methods:

- <code title="post /api/connector/v1/accountNotes/update">client.api.connector.v1.account_notes.<a href="./src/pymews/resources/api/connector/v1/account_notes.py">update</a>(\*\*<a href="src/pymews/types/api/connector/v1/account_note_update_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/account_note_update_response.py">AccountNoteUpdateResponse</a></code>
- <code title="post /api/connector/v1/accountNotes/getAll">client.api.connector.v1.account_notes.<a href="./src/pymews/resources/api/connector/v1/account_notes.py">list</a>(\*\*<a href="src/pymews/types/api/connector/v1/account_note_list_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/account_note_list_response.py">AccountNoteListResponse</a></code>
- <code title="post /api/connector/v1/accountNotes/delete">client.api.connector.v1.account_notes.<a href="./src/pymews/resources/api/connector/v1/account_notes.py">delete</a>(\*\*<a href="src/pymews/types/api/connector/v1/account_note_delete_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/unit.py">object</a></code>
- <code title="post /api/connector/v1/accountNotes/add">client.api.connector.v1.account_notes.<a href="./src/pymews/resources/api/connector/v1/account_notes.py">add</a>(\*\*<a href="src/pymews/types/api/connector/v1/account_note_add_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/account_note_add_response.py">AccountNoteAddResponse</a></code>

#### AccountingItems

Types:

```python
from pymews.types.api.connector.v1 import AccountingItemResult
```

Methods:

- <code title="post /api/connector/v1/accountingItems/update">client.api.connector.v1.accounting_items.<a href="./src/pymews/resources/api/connector/v1/accounting_items.py">update</a>(\*\*<a href="src/pymews/types/api/connector/v1/accounting_item_update_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/accounting_item_result.py">AccountingItemResult</a></code>
- <code title="post /api/connector/v1/accountingItems/getAll">client.api.connector.v1.accounting_items.<a href="./src/pymews/resources/api/connector/v1/accounting_items.py">list</a>(\*\*<a href="src/pymews/types/api/connector/v1/accounting_item_list_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/accounting_item_result.py">AccountingItemResult</a></code>

#### Accounts

Types:

```python
from pymews.types.api.connector.v1 import AccountUpdateResponse, AccountAddFileResponse
```

Methods:

- <code title="post /api/connector/v1/accounts/update">client.api.connector.v1.accounts.<a href="./src/pymews/resources/api/connector/v1/accounts.py">update</a>(\*\*<a href="src/pymews/types/api/connector/v1/account_update_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/account_update_response.py">AccountUpdateResponse</a></code>
- <code title="post /api/connector/v1/accounts/addFile">client.api.connector.v1.accounts.<a href="./src/pymews/resources/api/connector/v1/accounts.py">add_file</a>(\*\*<a href="src/pymews/types/api/connector/v1/account_add_file_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/account_add_file_response.py">AccountAddFileResponse</a></code>
- <code title="post /api/connector/v1/accounts/merge">client.api.connector.v1.accounts.<a href="./src/pymews/resources/api/connector/v1/accounts.py">merge</a>(\*\*<a href="src/pymews/types/api/connector/v1/account_merge_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/unit.py">object</a></code>

#### Addresses

Types:

```python
from pymews.types.api.connector.v1 import AddressResult, AddressListResponse
```

Methods:

- <code title="post /api/connector/v1/addresses/update">client.api.connector.v1.addresses.<a href="./src/pymews/resources/api/connector/v1/addresses.py">update</a>(\*\*<a href="src/pymews/types/api/connector/v1/address_update_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/address_result.py">AddressResult</a></code>
- <code title="post /api/connector/v1/addresses/getAll">client.api.connector.v1.addresses.<a href="./src/pymews/resources/api/connector/v1/addresses.py">list</a>(\*\*<a href="src/pymews/types/api/connector/v1/address_list_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/address_list_response.py">AddressListResponse</a></code>
- <code title="post /api/connector/v1/addresses/delete">client.api.connector.v1.addresses.<a href="./src/pymews/resources/api/connector/v1/addresses.py">delete</a>(\*\*<a href="src/pymews/types/api/connector/v1/address_delete_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/unit.py">object</a></code>
- <code title="post /api/connector/v1/addresses/add">client.api.connector.v1.addresses.<a href="./src/pymews/resources/api/connector/v1/addresses.py">add</a>(\*\*<a href="src/pymews/types/api/connector/v1/address_add_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/address_result.py">AddressResult</a></code>

#### AvailabilityBlocks

Types:

```python
from pymews.types.api.connector.v1 import AvailabilityBlockAddResult, AvailabilityBlockListResponse
```

Methods:

- <code title="post /api/connector/v1/availabilityBlocks/update">client.api.connector.v1.availability_blocks.<a href="./src/pymews/resources/api/connector/v1/availability_blocks.py">update</a>(\*\*<a href="src/pymews/types/api/connector/v1/availability_block_update_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/availability_block_add_result.py">AvailabilityBlockAddResult</a></code>
- <code title="post /api/connector/v1/availabilityBlocks/getAll">client.api.connector.v1.availability_blocks.<a href="./src/pymews/resources/api/connector/v1/availability_blocks.py">list</a>(\*\*<a href="src/pymews/types/api/connector/v1/availability_block_list_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/availability_block_list_response.py">AvailabilityBlockListResponse</a></code>
- <code title="post /api/connector/v1/availabilityBlocks/delete">client.api.connector.v1.availability_blocks.<a href="./src/pymews/resources/api/connector/v1/availability_blocks.py">delete</a>(\*\*<a href="src/pymews/types/api/connector/v1/availability_block_delete_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/unit.py">object</a></code>
- <code title="post /api/connector/v1/availabilityBlocks/add">client.api.connector.v1.availability_blocks.<a href="./src/pymews/resources/api/connector/v1/availability_blocks.py">add</a>(\*\*<a href="src/pymews/types/api/connector/v1/availability_block_add_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/availability_block_add_result.py">AvailabilityBlockAddResult</a></code>

#### Bills

Types:

```python
from pymews.types.api.connector.v1 import (
    BillUpdateResponse,
    BillListResponse,
    BillAddResponse,
    BillCloseResponse,
    BillGetPdfResponse,
)
```

Methods:

- <code title="post /api/connector/v1/bills/update">client.api.connector.v1.bills.<a href="./src/pymews/resources/api/connector/v1/bills.py">update</a>(\*\*<a href="src/pymews/types/api/connector/v1/bill_update_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/bill_update_response.py">BillUpdateResponse</a></code>
- <code title="post /api/connector/v1/bills/getAll">client.api.connector.v1.bills.<a href="./src/pymews/resources/api/connector/v1/bills.py">list</a>(\*\*<a href="src/pymews/types/api/connector/v1/bill_list_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/bill_list_response.py">BillListResponse</a></code>
- <code title="post /api/connector/v1/bills/delete">client.api.connector.v1.bills.<a href="./src/pymews/resources/api/connector/v1/bills.py">delete</a>(\*\*<a href="src/pymews/types/api/connector/v1/bill_delete_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/unit.py">object</a></code>
- <code title="post /api/connector/v1/bills/add">client.api.connector.v1.bills.<a href="./src/pymews/resources/api/connector/v1/bills.py">add</a>(\*\*<a href="src/pymews/types/api/connector/v1/bill_add_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/bill_add_response.py">BillAddResponse</a></code>
- <code title="post /api/connector/v1/bills/close">client.api.connector.v1.bills.<a href="./src/pymews/resources/api/connector/v1/bills.py">close</a>(\*\*<a href="src/pymews/types/api/connector/v1/bill_close_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/bill_close_response.py">BillCloseResponse</a></code>
- <code title="post /api/connector/v1/bills/getPdf">client.api.connector.v1.bills.<a href="./src/pymews/resources/api/connector/v1/bills.py">get_pdf</a>(\*\*<a href="src/pymews/types/api/connector/v1/bill_get_pdf_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/bill_get_pdf_response.py">BillGetPdfResponse</a></code>

#### CancellationPolicies

Types:

```python
from pymews.types.api.connector.v1 import (
    CancellationPolicyListResponse,
    CancellationPolicyGetByRatesResponse,
    CancellationPolicyGetByReservationsResponse,
)
```

Methods:

- <code title="post /api/connector/v1/cancellationPolicies/getAll">client.api.connector.v1.cancellation_policies.<a href="./src/pymews/resources/api/connector/v1/cancellation_policies.py">list</a>(\*\*<a href="src/pymews/types/api/connector/v1/cancellation_policy_list_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/cancellation_policy_list_response.py">CancellationPolicyListResponse</a></code>
- <code title="post /api/connector/v1/cancellationPolicies/getByRates">client.api.connector.v1.cancellation_policies.<a href="./src/pymews/resources/api/connector/v1/cancellation_policies.py">get_by_rates</a>(\*\*<a href="src/pymews/types/api/connector/v1/cancellation_policy_get_by_rates_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/cancellation_policy_get_by_rates_response.py">CancellationPolicyGetByRatesResponse</a></code>
- <code title="post /api/connector/v1/cancellationPolicies/getByReservations">client.api.connector.v1.cancellation_policies.<a href="./src/pymews/resources/api/connector/v1/cancellation_policies.py">get_by_reservations</a>(\*\*<a href="src/pymews/types/api/connector/v1/cancellation_policy_get_by_reservations_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/cancellation_policy_get_by_reservations_response.py">CancellationPolicyGetByReservationsResponse</a></code>

#### Commands

Types:

```python
from pymews.types.api.connector.v1 import DeviceCommandAddResult, DeviceCommandResult
```

Methods:

- <code title="post /api/connector/v1/commands/update">client.api.connector.v1.commands.<a href="./src/pymews/resources/api/connector/v1/commands.py">update</a>(\*\*<a href="src/pymews/types/api/connector/v1/command_update_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/unit.py">object</a></code>
- <code title="post /api/connector/v1/commands/addKeyCutter">client.api.connector.v1.commands.<a href="./src/pymews/resources/api/connector/v1/commands.py">add_key_cutter</a>(\*\*<a href="src/pymews/types/api/connector/v1/command_add_key_cutter_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/device_command_add_result.py">DeviceCommandAddResult</a></code>
- <code title="post /api/connector/v1/commands/addPaymentTerminal">client.api.connector.v1.commands.<a href="./src/pymews/resources/api/connector/v1/commands.py">add_payment_terminal</a>(\*\*<a href="src/pymews/types/api/connector/v1/command_add_payment_terminal_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/device_command_add_result.py">DeviceCommandAddResult</a></code>
- <code title="post /api/connector/v1/commands/addPrinter">client.api.connector.v1.commands.<a href="./src/pymews/resources/api/connector/v1/commands.py">add_printer</a>(\*\*<a href="src/pymews/types/api/connector/v1/command_add_printer_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/device_command_add_result.py">DeviceCommandAddResult</a></code>
- <code title="post /api/connector/v1/commands/getAllActive">client.api.connector.v1.commands.<a href="./src/pymews/resources/api/connector/v1/commands.py">list_active</a>(\*\*<a href="src/pymews/types/api/connector/v1/command_list_active_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/device_command_result.py">DeviceCommandResult</a></code>
- <code title="post /api/connector/v1/commands/getAllByIds">client.api.connector.v1.commands.<a href="./src/pymews/resources/api/connector/v1/commands.py">list_by_ids</a>(\*\*<a href="src/pymews/types/api/connector/v1/command_list_by_ids_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/device_command_result.py">DeviceCommandResult</a></code>

#### Companies

Types:

```python
from pymews.types.api.connector.v1 import CompanyResult
```

Methods:

- <code title="post /api/connector/v1/companies/update">client.api.connector.v1.companies.<a href="./src/pymews/resources/api/connector/v1/companies.py">update</a>(\*\*<a href="src/pymews/types/api/connector/v1/company_update_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/company_result.py">CompanyResult</a></code>
- <code title="post /api/connector/v1/companies/getAll">client.api.connector.v1.companies.<a href="./src/pymews/resources/api/connector/v1/companies.py">list</a>(\*\*<a href="src/pymews/types/api/connector/v1/company_list_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/company_result.py">CompanyResult</a></code>
- <code title="post /api/connector/v1/companies/delete">client.api.connector.v1.companies.<a href="./src/pymews/resources/api/connector/v1/companies.py">delete</a>(\*\*<a href="src/pymews/types/api/connector/v1/company_delete_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/unit.py">object</a></code>
- <code title="post /api/connector/v1/companies/add">client.api.connector.v1.companies.<a href="./src/pymews/resources/api/connector/v1/companies.py">add</a>(\*\*<a href="src/pymews/types/api/connector/v1/company_add_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/company_result.py">CompanyResult</a></code>

#### CompanyContracts

Types:

```python
from pymews.types.api.connector.v1 import ContractResult
```

Methods:

- <code title="post /api/connector/v1/companyContracts/update">client.api.connector.v1.company_contracts.<a href="./src/pymews/resources/api/connector/v1/company_contracts.py">update</a>(\*\*<a href="src/pymews/types/api/connector/v1/company_contract_update_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/contract_result.py">ContractResult</a></code>
- <code title="post /api/connector/v1/companyContracts/getAll">client.api.connector.v1.company_contracts.<a href="./src/pymews/resources/api/connector/v1/company_contracts.py">list</a>(\*\*<a href="src/pymews/types/api/connector/v1/company_contract_list_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/contract_result.py">ContractResult</a></code>
- <code title="post /api/connector/v1/companyContracts/delete">client.api.connector.v1.company_contracts.<a href="./src/pymews/resources/api/connector/v1/company_contracts.py">delete</a>(\*\*<a href="src/pymews/types/api/connector/v1/company_contract_delete_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/unit.py">object</a></code>
- <code title="post /api/connector/v1/companyContracts/add">client.api.connector.v1.company_contracts.<a href="./src/pymews/resources/api/connector/v1/company_contracts.py">add</a>(\*\*<a href="src/pymews/types/api/connector/v1/company_contract_add_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/contract_result.py">ContractResult</a></code>

#### CreditCards

Types:

```python
from pymews.types.api.connector.v1 import CreditCardResult, CreditCardChargeResponse
```

Methods:

- <code title="post /api/connector/v1/creditCards/getAll">client.api.connector.v1.credit_cards.<a href="./src/pymews/resources/api/connector/v1/credit_cards.py">list</a>(\*\*<a href="src/pymews/types/api/connector/v1/credit_card_list_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/credit_card_result.py">CreditCardResult</a></code>
- <code title="post /api/connector/v1/creditCards/addTokenized">client.api.connector.v1.credit_cards.<a href="./src/pymews/resources/api/connector/v1/credit_cards.py">add_tokenized</a>(\*\*<a href="src/pymews/types/api/connector/v1/credit_card_add_tokenized_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/add_credit_card_result.py">AddCreditCardResult</a></code>
- <code title="post /api/connector/v1/creditCards/charge">client.api.connector.v1.credit_cards.<a href="./src/pymews/resources/api/connector/v1/credit_cards.py">charge</a>(\*\*<a href="src/pymews/types/api/connector/v1/credit_card_charge_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/credit_card_charge_response.py">CreditCardChargeResponse</a></code>
- <code title="post /api/connector/v1/creditCards/disable">client.api.connector.v1.credit_cards.<a href="./src/pymews/resources/api/connector/v1/credit_cards.py">disable</a>(\*\*<a href="src/pymews/types/api/connector/v1/credit_card_disable_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/unit.py">object</a></code>
- <code title="post /api/connector/v1/creditCards/getAllByCustomers">client.api.connector.v1.credit_cards.<a href="./src/pymews/resources/api/connector/v1/credit_cards.py">list_by_customers</a>(\*\*<a href="src/pymews/types/api/connector/v1/credit_card_list_by_customers_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/credit_card_result.py">CreditCardResult</a></code>
- <code title="post /api/connector/v1/creditCards/getAllByIds">client.api.connector.v1.credit_cards.<a href="./src/pymews/resources/api/connector/v1/credit_cards.py">list_by_ids</a>(\*\*<a href="src/pymews/types/api/connector/v1/credit_card_list_by_ids_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/credit_card_result.py">CreditCardResult</a></code>

#### Customers

Types:

```python
from pymews.types.api.connector.v1 import (
    Customer,
    CustomerListResponse,
    CustomerAddFileResponse,
    CustomerGetOpenItemsResponse,
    CustomerSearchResponse,
)
```

Methods:

- <code title="post /api/connector/v1/customers/update">client.api.connector.v1.customers.<a href="./src/pymews/resources/api/connector/v1/customers.py">update</a>(\*\*<a href="src/pymews/types/api/connector/v1/customer_update_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/customer.py">Customer</a></code>
- <code title="post /api/connector/v1/customers/getAll">client.api.connector.v1.customers.<a href="./src/pymews/resources/api/connector/v1/customers.py">list</a>(\*\*<a href="src/pymews/types/api/connector/v1/customer_list_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/customer_list_response.py">CustomerListResponse</a></code>
- <code title="post /api/connector/v1/customers/add">client.api.connector.v1.customers.<a href="./src/pymews/resources/api/connector/v1/customers.py">add</a>(\*\*<a href="src/pymews/types/api/connector/v1/customer_add_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/customer.py">Customer</a></code>
- <code title="post /api/connector/v1/customers/addFile">client.api.connector.v1.customers.<a href="./src/pymews/resources/api/connector/v1/customers.py">add_file</a>(\*\*<a href="src/pymews/types/api/connector/v1/customer_add_file_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/customer_add_file_response.py">CustomerAddFileResponse</a></code>
- <code title="post /api/connector/v1/customers/getOpenItems">client.api.connector.v1.customers.<a href="./src/pymews/resources/api/connector/v1/customers.py">get_open_items</a>(\*\*<a href="src/pymews/types/api/connector/v1/customer_get_open_items_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/customer_get_open_items_response.py">CustomerGetOpenItemsResponse</a></code>
- <code title="post /api/connector/v1/customers/merge">client.api.connector.v1.customers.<a href="./src/pymews/resources/api/connector/v1/customers.py">merge</a>(\*\*<a href="src/pymews/types/api/connector/v1/customer_merge_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/unit.py">object</a></code>
- <code title="post /api/connector/v1/customers/search">client.api.connector.v1.customers.<a href="./src/pymews/resources/api/connector/v1/customers.py">search</a>(\*\*<a href="src/pymews/types/api/connector/v1/customer_search_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/customer_search_response.py">CustomerSearchResponse</a></code>

#### Exports

Types:

```python
from pymews.types.api.connector.v1 import ExportListResponse, ExportAddResponse
```

Methods:

- <code title="post /api/connector/v1/exports/getAll">client.api.connector.v1.exports.<a href="./src/pymews/resources/api/connector/v1/exports.py">list</a>(\*\*<a href="src/pymews/types/api/connector/v1/export_list_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/export_list_response.py">ExportListResponse</a></code>
- <code title="post /api/connector/v1/exports/add">client.api.connector.v1.exports.<a href="./src/pymews/resources/api/connector/v1/exports.py">add</a>(\*\*<a href="src/pymews/types/api/connector/v1/export_add_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/export_add_response.py">ExportAddResponse</a></code>

#### IdentityDocuments

Types:

```python
from pymews.types.api.connector.v1 import IdentityDocumentWriteResult, IdentityDocumentListResponse
```

Methods:

- <code title="post /api/connector/v1/identityDocuments/update">client.api.connector.v1.identity_documents.<a href="./src/pymews/resources/api/connector/v1/identity_documents.py">update</a>(\*\*<a href="src/pymews/types/api/connector/v1/identity_document_update_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/identity_document_write_result.py">IdentityDocumentWriteResult</a></code>
- <code title="post /api/connector/v1/identityDocuments/getAll">client.api.connector.v1.identity_documents.<a href="./src/pymews/resources/api/connector/v1/identity_documents.py">list</a>(\*\*<a href="src/pymews/types/api/connector/v1/identity_document_list_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/identity_document_list_response.py">IdentityDocumentListResponse</a></code>
- <code title="post /api/connector/v1/identityDocuments/delete">client.api.connector.v1.identity_documents.<a href="./src/pymews/resources/api/connector/v1/identity_documents.py">delete</a>(\*\*<a href="src/pymews/types/api/connector/v1/identity_document_delete_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/unit.py">object</a></code>
- <code title="post /api/connector/v1/identityDocuments/add">client.api.connector.v1.identity_documents.<a href="./src/pymews/resources/api/connector/v1/identity_documents.py">add</a>(\*\*<a href="src/pymews/types/api/connector/v1/identity_document_add_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/identity_document_write_result.py">IdentityDocumentWriteResult</a></code>
- <code title="post /api/connector/v1/identityDocuments/clear">client.api.connector.v1.identity_documents.<a href="./src/pymews/resources/api/connector/v1/identity_documents.py">clear</a>(\*\*<a href="src/pymews/types/api/connector/v1/identity_document_clear_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/unit.py">object</a></code>

#### Languages

Types:

```python
from pymews.types.api.connector.v1 import LanguageListResponse, LanguageGetTextsResponse
```

Methods:

- <code title="post /api/connector/v1/languages/getAll">client.api.connector.v1.languages.<a href="./src/pymews/resources/api/connector/v1/languages.py">list</a>(\*\*<a href="src/pymews/types/api/connector/v1/language_list_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/language_list_response.py">LanguageListResponse</a></code>
- <code title="post /api/connector/v1/languages/getTexts">client.api.connector.v1.languages.<a href="./src/pymews/resources/api/connector/v1/languages.py">get_texts</a>(\*\*<a href="src/pymews/types/api/connector/v1/language_get_texts_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/language_get_texts_response.py">LanguageGetTextsResponse</a></code>

#### LoyaltyMemberships

Types:

```python
from pymews.types.api.connector.v1 import LoyaltyMembershipResult
```

Methods:

- <code title="post /api/connector/v1/loyaltyMemberships/update">client.api.connector.v1.loyalty_memberships.<a href="./src/pymews/resources/api/connector/v1/loyalty_memberships.py">update</a>(\*\*<a href="src/pymews/types/api/connector/v1/loyalty_membership_update_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/loyalty_membership_result.py">LoyaltyMembershipResult</a></code>
- <code title="post /api/connector/v1/loyaltyMemberships/getAll">client.api.connector.v1.loyalty_memberships.<a href="./src/pymews/resources/api/connector/v1/loyalty_memberships.py">list</a>(\*\*<a href="src/pymews/types/api/connector/v1/loyalty_membership_list_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/loyalty_membership_result.py">LoyaltyMembershipResult</a></code>
- <code title="post /api/connector/v1/loyaltyMemberships/delete">client.api.connector.v1.loyalty_memberships.<a href="./src/pymews/resources/api/connector/v1/loyalty_memberships.py">delete</a>(\*\*<a href="src/pymews/types/api/connector/v1/loyalty_membership_delete_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/unit.py">object</a></code>
- <code title="post /api/connector/v1/loyaltyMemberships/add">client.api.connector.v1.loyalty_memberships.<a href="./src/pymews/resources/api/connector/v1/loyalty_memberships.py">add</a>(\*\*<a href="src/pymews/types/api/connector/v1/loyalty_membership_add_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/loyalty_membership_result.py">LoyaltyMembershipResult</a></code>

#### LoyaltyPrograms

Types:

```python
from pymews.types.api.connector.v1 import LoyaltyProgramResult
```

Methods:

- <code title="post /api/connector/v1/loyaltyPrograms/update">client.api.connector.v1.loyalty_programs.<a href="./src/pymews/resources/api/connector/v1/loyalty_programs.py">update</a>(\*\*<a href="src/pymews/types/api/connector/v1/loyalty_program_update_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/loyalty_program_result.py">LoyaltyProgramResult</a></code>
- <code title="post /api/connector/v1/loyaltyPrograms/getAll">client.api.connector.v1.loyalty_programs.<a href="./src/pymews/resources/api/connector/v1/loyalty_programs.py">list</a>(\*\*<a href="src/pymews/types/api/connector/v1/loyalty_program_list_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/loyalty_program_result.py">LoyaltyProgramResult</a></code>
- <code title="post /api/connector/v1/loyaltyPrograms/delete">client.api.connector.v1.loyalty_programs.<a href="./src/pymews/resources/api/connector/v1/loyalty_programs.py">delete</a>(\*\*<a href="src/pymews/types/api/connector/v1/loyalty_program_delete_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/unit.py">object</a></code>
- <code title="post /api/connector/v1/loyaltyPrograms/add">client.api.connector.v1.loyalty_programs.<a href="./src/pymews/resources/api/connector/v1/loyalty_programs.py">add</a>(\*\*<a href="src/pymews/types/api/connector/v1/loyalty_program_add_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/loyalty_program_result.py">LoyaltyProgramResult</a></code>

#### LoyaltyTiers

Types:

```python
from pymews.types.api.connector.v1 import LoyaltyTierResult
```

Methods:

- <code title="post /api/connector/v1/loyaltyTiers/update">client.api.connector.v1.loyalty_tiers.<a href="./src/pymews/resources/api/connector/v1/loyalty_tiers.py">update</a>(\*\*<a href="src/pymews/types/api/connector/v1/loyalty_tier_update_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/loyalty_tier_result.py">LoyaltyTierResult</a></code>
- <code title="post /api/connector/v1/loyaltyTiers/getAll">client.api.connector.v1.loyalty_tiers.<a href="./src/pymews/resources/api/connector/v1/loyalty_tiers.py">list</a>(\*\*<a href="src/pymews/types/api/connector/v1/loyalty_tier_list_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/loyalty_tier_result.py">LoyaltyTierResult</a></code>
- <code title="post /api/connector/v1/loyaltyTiers/delete">client.api.connector.v1.loyalty_tiers.<a href="./src/pymews/resources/api/connector/v1/loyalty_tiers.py">delete</a>(\*\*<a href="src/pymews/types/api/connector/v1/loyalty_tier_delete_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/unit.py">object</a></code>
- <code title="post /api/connector/v1/loyaltyTiers/add">client.api.connector.v1.loyalty_tiers.<a href="./src/pymews/resources/api/connector/v1/loyalty_tiers.py">add</a>(\*\*<a href="src/pymews/types/api/connector/v1/loyalty_tier_add_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/loyalty_tier_result.py">LoyaltyTierResult</a></code>

#### MessageThreads

Types:

```python
from pymews.types.api.connector.v1 import MessageThreadResult
```

Methods:

- <code title="post /api/connector/v1/messageThreads/getAll">client.api.connector.v1.message_threads.<a href="./src/pymews/resources/api/connector/v1/message_threads.py">list</a>(\*\*<a href="src/pymews/types/api/connector/v1/message_thread_list_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/message_thread_result.py">MessageThreadResult</a></code>
- <code title="post /api/connector/v1/messageThreads/add">client.api.connector.v1.message_threads.<a href="./src/pymews/resources/api/connector/v1/message_threads.py">add</a>(\*\*<a href="src/pymews/types/api/connector/v1/message_thread_add_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/message_thread_result.py">MessageThreadResult</a></code>

#### Messages

Types:

```python
from pymews.types.api.connector.v1 import MessageListResponse, MessageAddResponse
```

Methods:

- <code title="post /api/connector/v1/messages/getAll">client.api.connector.v1.messages.<a href="./src/pymews/resources/api/connector/v1/messages.py">list</a>(\*\*<a href="src/pymews/types/api/connector/v1/message_list_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/message_list_response.py">MessageListResponse</a></code>
- <code title="post /api/connector/v1/messages/add">client.api.connector.v1.messages.<a href="./src/pymews/resources/api/connector/v1/messages.py">add</a>(\*\*<a href="src/pymews/types/api/connector/v1/message_add_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/message_add_response.py">MessageAddResponse</a></code>

#### OrderItems

Types:

```python
from pymews.types.api.connector.v1 import OrderItemListResponse
```

Methods:

- <code title="post /api/connector/v1/orderItems/getAll">client.api.connector.v1.order_items.<a href="./src/pymews/resources/api/connector/v1/order_items.py">list</a>(\*\*<a href="src/pymews/types/api/connector/v1/order_item_list_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/order_item_list_response.py">OrderItemListResponse</a></code>
- <code title="post /api/connector/v1/orderItems/cancel">client.api.connector.v1.order_items.<a href="./src/pymews/resources/api/connector/v1/order_items.py">cancel</a>(\*\*<a href="src/pymews/types/api/connector/v1/order_item_cancel_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/unit.py">object</a></code>

#### PaymentRequests

Types:

```python
from pymews.types.api.connector.v1 import PaymentRequestResult
```

Methods:

- <code title="post /api/connector/v1/paymentRequests/getAll">client.api.connector.v1.payment_requests.<a href="./src/pymews/resources/api/connector/v1/payment_requests.py">list</a>(\*\*<a href="src/pymews/types/api/connector/v1/payment_request_list_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/payment_request_result.py">PaymentRequestResult</a></code>
- <code title="post /api/connector/v1/paymentRequests/add">client.api.connector.v1.payment_requests.<a href="./src/pymews/resources/api/connector/v1/payment_requests.py">add</a>(\*\*<a href="src/pymews/types/api/connector/v1/payment_request_add_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/payment_request_result.py">PaymentRequestResult</a></code>
- <code title="post /api/connector/v1/paymentRequests/cancel">client.api.connector.v1.payment_requests.<a href="./src/pymews/resources/api/connector/v1/payment_requests.py">cancel</a>(\*\*<a href="src/pymews/types/api/connector/v1/payment_request_cancel_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/payment_request_result.py">PaymentRequestResult</a></code>

#### Payments

Types:

```python
from pymews.types.api.connector.v1 import (
    PaymentListResponse,
    PaymentAddAlternativeResponse,
    PaymentAddExternalResponse,
    PaymentRefundResponse,
)
```

Methods:

- <code title="post /api/connector/v1/payments/getAll">client.api.connector.v1.payments.<a href="./src/pymews/resources/api/connector/v1/payments.py">list</a>(\*\*<a href="src/pymews/types/api/connector/v1/payment_list_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/payment_list_response.py">PaymentListResponse</a></code>
- <code title="post /api/connector/v1/payments/addAlternative">client.api.connector.v1.payments.<a href="./src/pymews/resources/api/connector/v1/payments.py">add_alternative</a>(\*\*<a href="src/pymews/types/api/connector/v1/payment_add_alternative_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/payment_add_alternative_response.py">PaymentAddAlternativeResponse</a></code>
- <code title="post /api/connector/v1/payments/addCreditCard">client.api.connector.v1.payments.<a href="./src/pymews/resources/api/connector/v1/payments.py">add_credit_card</a>(\*\*<a href="src/pymews/types/api/connector/v1/payment_add_credit_card_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/add_credit_card_result.py">AddCreditCardResult</a></code>
- <code title="post /api/connector/v1/payments/addExternal">client.api.connector.v1.payments.<a href="./src/pymews/resources/api/connector/v1/payments.py">add_external</a>(\*\*<a href="src/pymews/types/api/connector/v1/payment_add_external_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/payment_add_external_response.py">PaymentAddExternalResponse</a></code>
- <code title="post /api/connector/v1/payments/refund">client.api.connector.v1.payments.<a href="./src/pymews/resources/api/connector/v1/payments.py">refund</a>(\*\*<a href="src/pymews/types/api/connector/v1/payment_refund_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/payment_refund_response.py">PaymentRefundResponse</a></code>

#### Products

Types:

```python
from pymews.types.api.connector.v1 import ProductListResponse, ProductGetPricingResponse
```

Methods:

- <code title="post /api/connector/v1/products/getAll">client.api.connector.v1.products.<a href="./src/pymews/resources/api/connector/v1/products.py">list</a>(\*\*<a href="src/pymews/types/api/connector/v1/product_list_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/product_list_response.py">ProductListResponse</a></code>
- <code title="post /api/connector/v1/products/delete">client.api.connector.v1.products.<a href="./src/pymews/resources/api/connector/v1/products.py">delete</a>(\*\*<a href="src/pymews/types/api/connector/v1/product_delete_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/unit.py">object</a></code>
- <code title="post /api/connector/v1/products/getPricing">client.api.connector.v1.products.<a href="./src/pymews/resources/api/connector/v1/products.py">get_pricing</a>(\*\*<a href="src/pymews/types/api/connector/v1/product_get_pricing_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/product_get_pricing_response.py">ProductGetPricingResponse</a></code>
- <code title="post /api/connector/v1/products/updatePrice">client.api.connector.v1.products.<a href="./src/pymews/resources/api/connector/v1/products.py">update_price</a>(\*\*<a href="src/pymews/types/api/connector/v1/product_update_price_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/unit.py">object</a></code>

#### Rates

Types:

```python
from pymews.types.api.connector.v1 import (
    RateListResponse,
    RateAddResponse,
    RateGetPricingResponse,
    RateSetResponse,
)
```

Methods:

- <code title="post /api/connector/v1/rates/getAll">client.api.connector.v1.rates.<a href="./src/pymews/resources/api/connector/v1/rates.py">list</a>(\*\*<a href="src/pymews/types/api/connector/v1/rate_list_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/rate_list_response.py">RateListResponse</a></code>
- <code title="post /api/connector/v1/rates/delete">client.api.connector.v1.rates.<a href="./src/pymews/resources/api/connector/v1/rates.py">delete</a>(\*\*<a href="src/pymews/types/api/connector/v1/rate_delete_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/unit.py">object</a></code>
- <code title="post /api/connector/v1/rates/add">client.api.connector.v1.rates.<a href="./src/pymews/resources/api/connector/v1/rates.py">add</a>(\*\*<a href="src/pymews/types/api/connector/v1/rate_add_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/rate_add_response.py">RateAddResponse</a></code>
- <code title="post /api/connector/v1/rates/getPricing">client.api.connector.v1.rates.<a href="./src/pymews/resources/api/connector/v1/rates.py">get_pricing</a>(\*\*<a href="src/pymews/types/api/connector/v1/rate_get_pricing_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/rate_get_pricing_response.py">RateGetPricingResponse</a></code>
- <code title="post /api/connector/v1/rates/set">client.api.connector.v1.rates.<a href="./src/pymews/resources/api/connector/v1/rates.py">set</a>(\*\*<a href="src/pymews/types/api/connector/v1/rate_set_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/rate_set_response.py">RateSetResponse</a></code>
- <code title="post /api/connector/v1/rates/updatePrice">client.api.connector.v1.rates.<a href="./src/pymews/resources/api/connector/v1/rates.py">update_price</a>(\*\*<a href="src/pymews/types/api/connector/v1/rate_update_price_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/unit.py">object</a></code>

#### Reservations

Types:

```python
from pymews.types.api.connector.v1 import (
    MultipleReservationResult,
    ReservationResult,
    ReservationAddResponse,
    ReservationAddCompanionResponse,
    ReservationAddProductResponse,
    ReservationGetAll2023_06_06Response,
    ReservationGetAllItemsResponse,
    ReservationPriceResponse,
)
```

Methods:

- <code title="post /api/connector/v1/reservations/update">client.api.connector.v1.reservations.<a href="./src/pymews/resources/api/connector/v1/reservations.py">update</a>(\*\*<a href="src/pymews/types/api/connector/v1/reservation_update_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/reservation_result.py">ReservationResult</a></code>
- <code title="post /api/connector/v1/reservations/add">client.api.connector.v1.reservations.<a href="./src/pymews/resources/api/connector/v1/reservations.py">add</a>(\*\*<a href="src/pymews/types/api/connector/v1/reservation_add_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/reservation_add_response.py">ReservationAddResponse</a></code>
- <code title="post /api/connector/v1/reservations/addCompanion">client.api.connector.v1.reservations.<a href="./src/pymews/resources/api/connector/v1/reservations.py">add_companion</a>(\*\*<a href="src/pymews/types/api/connector/v1/reservation_add_companion_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/reservation_add_companion_response.py">ReservationAddCompanionResponse</a></code>
- <code title="post /api/connector/v1/reservations/addProduct">client.api.connector.v1.reservations.<a href="./src/pymews/resources/api/connector/v1/reservations.py">add_product</a>(\*\*<a href="src/pymews/types/api/connector/v1/reservation_add_product_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/reservation_add_product_response.py">ReservationAddProductResponse</a></code>
- <code title="post /api/connector/v1/reservations/cancel">client.api.connector.v1.reservations.<a href="./src/pymews/resources/api/connector/v1/reservations.py">cancel</a>(\*\*<a href="src/pymews/types/api/connector/v1/reservation_cancel_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/multiple_reservation_result.py">MultipleReservationResult</a></code>
- <code title="post /api/connector/v1/reservations/confirm">client.api.connector.v1.reservations.<a href="./src/pymews/resources/api/connector/v1/reservations.py">confirm</a>(\*\*<a href="src/pymews/types/api/connector/v1/reservation_confirm_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/multiple_reservation_result.py">MultipleReservationResult</a></code>
- <code title="post /api/connector/v1/reservations/deleteCompanion">client.api.connector.v1.reservations.<a href="./src/pymews/resources/api/connector/v1/reservations.py">delete_companion</a>(\*\*<a href="src/pymews/types/api/connector/v1/reservation_delete_companion_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/unit.py">object</a></code>
- <code title="post /api/connector/v1/reservations/getAll">client.api.connector.v1.reservations.<a href="./src/pymews/resources/api/connector/v1/reservations.py">get_all</a>(\*\*<a href="src/pymews/types/api/connector/v1/reservation_get_all_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/reservation_result.py">ReservationResult</a></code>
- <code title="post /api/connector/v1/reservations/getAll/2023-06-06">client.api.connector.v1.reservations.<a href="./src/pymews/resources/api/connector/v1/reservations.py">get_all_2023_06_06</a>(\*\*<a href="src/pymews/types/api/connector/v1/reservation_get_all_2023_06_06_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/reservation_get_all_2023_06_06_response.py">ReservationGetAll2023_06_06Response</a></code>
- <code title="post /api/connector/v1/reservations/getAllItems">client.api.connector.v1.reservations.<a href="./src/pymews/resources/api/connector/v1/reservations.py">get_all_items</a>(\*\*<a href="src/pymews/types/api/connector/v1/reservation_get_all_items_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/reservation_get_all_items_response.py">ReservationGetAllItemsResponse</a></code>
- <code title="post /api/connector/v1/reservations/price">client.api.connector.v1.reservations.<a href="./src/pymews/resources/api/connector/v1/reservations.py">price</a>(\*\*<a href="src/pymews/types/api/connector/v1/reservation_price_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/reservation_price_response.py">ReservationPriceResponse</a></code>
- <code title="post /api/connector/v1/reservations/process">client.api.connector.v1.reservations.<a href="./src/pymews/resources/api/connector/v1/reservations.py">process</a>(\*\*<a href="src/pymews/types/api/connector/v1/reservation_process_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/unit.py">object</a></code>
- <code title="post /api/connector/v1/reservations/start">client.api.connector.v1.reservations.<a href="./src/pymews/resources/api/connector/v1/reservations.py">start</a>(\*\*<a href="src/pymews/types/api/connector/v1/reservation_start_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/unit.py">object</a></code>
- <code title="post /api/connector/v1/reservations/updateCustomer">client.api.connector.v1.reservations.<a href="./src/pymews/resources/api/connector/v1/reservations.py">update_customer</a>(\*\*<a href="src/pymews/types/api/connector/v1/reservation_update_customer_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/unit.py">object</a></code>
- <code title="post /api/connector/v1/reservations/updateInterval">client.api.connector.v1.reservations.<a href="./src/pymews/resources/api/connector/v1/reservations.py">update_interval</a>(\*\*<a href="src/pymews/types/api/connector/v1/reservation_update_interval_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/unit.py">object</a></code>

#### ResourceAccessTokens

Types:

```python
from pymews.types.api.connector.v1 import ResourceAccessTokenResult
```

Methods:

- <code title="post /api/connector/v1/resourceAccessTokens/update">client.api.connector.v1.resource_access_tokens.<a href="./src/pymews/resources/api/connector/v1/resource_access_tokens.py">update</a>(\*\*<a href="src/pymews/types/api/connector/v1/resource_access_token_update_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/resource_access_token_result.py">ResourceAccessTokenResult</a></code>
- <code title="post /api/connector/v1/resourceAccessTokens/getAll">client.api.connector.v1.resource_access_tokens.<a href="./src/pymews/resources/api/connector/v1/resource_access_tokens.py">list</a>(\*\*<a href="src/pymews/types/api/connector/v1/resource_access_token_list_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/resource_access_token_result.py">ResourceAccessTokenResult</a></code>
- <code title="post /api/connector/v1/resourceAccessTokens/delete">client.api.connector.v1.resource_access_tokens.<a href="./src/pymews/resources/api/connector/v1/resource_access_tokens.py">delete</a>(\*\*<a href="src/pymews/types/api/connector/v1/resource_access_token_delete_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/unit.py">object</a></code>
- <code title="post /api/connector/v1/resourceAccessTokens/add">client.api.connector.v1.resource_access_tokens.<a href="./src/pymews/resources/api/connector/v1/resource_access_tokens.py">add</a>(\*\*<a href="src/pymews/types/api/connector/v1/resource_access_token_add_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/resource_access_token_result.py">ResourceAccessTokenResult</a></code>

#### ResourceBlocks

Types:

```python
from pymews.types.api.connector.v1 import ResourceBlockResult
```

Methods:

- <code title="post /api/connector/v1/resourceBlocks/getAll">client.api.connector.v1.resource_blocks.<a href="./src/pymews/resources/api/connector/v1/resource_blocks.py">list</a>(\*\*<a href="src/pymews/types/api/connector/v1/resource_block_list_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/resource_block_result.py">ResourceBlockResult</a></code>
- <code title="post /api/connector/v1/resourceBlocks/delete">client.api.connector.v1.resource_blocks.<a href="./src/pymews/resources/api/connector/v1/resource_blocks.py">delete</a>(\*\*<a href="src/pymews/types/api/connector/v1/resource_block_delete_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/unit.py">object</a></code>
- <code title="post /api/connector/v1/resourceBlocks/add">client.api.connector.v1.resource_blocks.<a href="./src/pymews/resources/api/connector/v1/resource_blocks.py">add</a>(\*\*<a href="src/pymews/types/api/connector/v1/resource_block_add_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/resource_block_result.py">ResourceBlockResult</a></code>

#### Resources

Types:

```python
from pymews.types.api.connector.v1 import ResourceListResponse
```

Methods:

- <code title="post /api/connector/v1/resources/update">client.api.connector.v1.resources.<a href="./src/pymews/resources/api/connector/v1/resources.py">update</a>(\*\*<a href="src/pymews/types/api/connector/v1/resource_update_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/unit.py">object</a></code>
- <code title="post /api/connector/v1/resources/getAll">client.api.connector.v1.resources.<a href="./src/pymews/resources/api/connector/v1/resources.py">list</a>(\*\*<a href="src/pymews/types/api/connector/v1/resource_list_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/resource_list_response.py">ResourceListResponse</a></code>

#### Restrictions

Types:

```python
from pymews.types.api.connector.v1 import RestrictionListResponse, RestrictionAddResponse
```

Methods:

- <code title="post /api/connector/v1/restrictions/getAll">client.api.connector.v1.restrictions.<a href="./src/pymews/resources/api/connector/v1/restrictions.py">list</a>(\*\*<a href="src/pymews/types/api/connector/v1/restriction_list_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/restriction_list_response.py">RestrictionListResponse</a></code>
- <code title="post /api/connector/v1/restrictions/delete">client.api.connector.v1.restrictions.<a href="./src/pymews/resources/api/connector/v1/restrictions.py">delete</a>(\*\*<a href="src/pymews/types/api/connector/v1/restriction_delete_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/unit.py">object</a></code>
- <code title="post /api/connector/v1/restrictions/add">client.api.connector.v1.restrictions.<a href="./src/pymews/resources/api/connector/v1/restrictions.py">add</a>(\*\*<a href="src/pymews/types/api/connector/v1/restriction_add_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/restriction_add_response.py">RestrictionAddResponse</a></code>
- <code title="post /api/connector/v1/restrictions/clear">client.api.connector.v1.restrictions.<a href="./src/pymews/resources/api/connector/v1/restrictions.py">clear</a>(\*\*<a href="src/pymews/types/api/connector/v1/restriction_clear_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/unit.py">object</a></code>
- <code title="post /api/connector/v1/restrictions/set">client.api.connector.v1.restrictions.<a href="./src/pymews/resources/api/connector/v1/restrictions.py">set</a>(\*\*<a href="src/pymews/types/api/connector/v1/restriction_set_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/unit.py">object</a></code>

#### RoutingRules

Types:

```python
from pymews.types.api.connector.v1 import RoutingRuleResult
```

Methods:

- <code title="post /api/connector/v1/routingRules/update">client.api.connector.v1.routing_rules.<a href="./src/pymews/resources/api/connector/v1/routing_rules.py">update</a>(\*\*<a href="src/pymews/types/api/connector/v1/routing_rule_update_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/routing_rule_result.py">RoutingRuleResult</a></code>
- <code title="post /api/connector/v1/routingRules/getAll">client.api.connector.v1.routing_rules.<a href="./src/pymews/resources/api/connector/v1/routing_rules.py">list</a>(\*\*<a href="src/pymews/types/api/connector/v1/routing_rule_list_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/routing_rule_result.py">RoutingRuleResult</a></code>
- <code title="post /api/connector/v1/routingRules/delete">client.api.connector.v1.routing_rules.<a href="./src/pymews/resources/api/connector/v1/routing_rules.py">delete</a>(\*\*<a href="src/pymews/types/api/connector/v1/routing_rule_delete_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/unit.py">object</a></code>
- <code title="post /api/connector/v1/routingRules/add">client.api.connector.v1.routing_rules.<a href="./src/pymews/resources/api/connector/v1/routing_rules.py">add</a>(\*\*<a href="src/pymews/types/api/connector/v1/routing_rule_add_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/routing_rule_result.py">RoutingRuleResult</a></code>

#### ServiceOrderNotes

Types:

```python
from pymews.types.api.connector.v1 import (
    ServiceOrderNoteUpdateResponse,
    ServiceOrderNoteListResponse,
    ServiceOrderNoteAddResponse,
)
```

Methods:

- <code title="post /api/connector/v1/serviceOrderNotes/update">client.api.connector.v1.service_order_notes.<a href="./src/pymews/resources/api/connector/v1/service_order_notes.py">update</a>(\*\*<a href="src/pymews/types/api/connector/v1/service_order_note_update_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/service_order_note_update_response.py">ServiceOrderNoteUpdateResponse</a></code>
- <code title="post /api/connector/v1/serviceOrderNotes/getAll">client.api.connector.v1.service_order_notes.<a href="./src/pymews/resources/api/connector/v1/service_order_notes.py">list</a>(\*\*<a href="src/pymews/types/api/connector/v1/service_order_note_list_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/service_order_note_list_response.py">ServiceOrderNoteListResponse</a></code>
- <code title="post /api/connector/v1/serviceOrderNotes/delete">client.api.connector.v1.service_order_notes.<a href="./src/pymews/resources/api/connector/v1/service_order_notes.py">delete</a>(\*\*<a href="src/pymews/types/api/connector/v1/service_order_note_delete_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/unit.py">object</a></code>
- <code title="post /api/connector/v1/serviceOrderNotes/add">client.api.connector.v1.service_order_notes.<a href="./src/pymews/resources/api/connector/v1/service_order_notes.py">add</a>(\*\*<a href="src/pymews/types/api/connector/v1/service_order_note_add_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/service_order_note_add_response.py">ServiceOrderNoteAddResponse</a></code>

#### ServiceOverbookingLimits

Types:

```python
from pymews.types.api.connector.v1 import ServiceOverbookingLimitListResponse
```

Methods:

- <code title="post /api/connector/v1/serviceOverbookingLimits/getAll">client.api.connector.v1.service_overbooking_limits.<a href="./src/pymews/resources/api/connector/v1/service_overbooking_limits.py">list</a>(\*\*<a href="src/pymews/types/api/connector/v1/service_overbooking_limit_list_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/service_overbooking_limit_list_response.py">ServiceOverbookingLimitListResponse</a></code>
- <code title="post /api/connector/v1/serviceOverbookingLimits/clear">client.api.connector.v1.service_overbooking_limits.<a href="./src/pymews/resources/api/connector/v1/service_overbooking_limits.py">clear</a>(\*\*<a href="src/pymews/types/api/connector/v1/service_overbooking_limit_clear_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/unit.py">object</a></code>
- <code title="post /api/connector/v1/serviceOverbookingLimits/set">client.api.connector.v1.service_overbooking_limits.<a href="./src/pymews/resources/api/connector/v1/service_overbooking_limits.py">set</a>(\*\*<a href="src/pymews/types/api/connector/v1/service_overbooking_limit_set_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/unit.py">object</a></code>

#### Services

Types:

```python
from pymews.types.api.connector.v1 import (
    ServiceListResponse,
    ServiceGetAvailabilityResponse,
    ServiceGetAvailability2024_01_22Response,
)
```

Methods:

- <code title="post /api/connector/v1/services/getAll">client.api.connector.v1.services.<a href="./src/pymews/resources/api/connector/v1/services.py">list</a>(\*\*<a href="src/pymews/types/api/connector/v1/service_list_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/service_list_response.py">ServiceListResponse</a></code>
- <code title="post /api/connector/v1/services/getAvailability">client.api.connector.v1.services.<a href="./src/pymews/resources/api/connector/v1/services.py">get_availability</a>(\*\*<a href="src/pymews/types/api/connector/v1/service_get_availability_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/service_get_availability_response.py">ServiceGetAvailabilityResponse</a></code>
- <code title="post /api/connector/v1/services/getAvailability/2024-01-22">client.api.connector.v1.services.<a href="./src/pymews/resources/api/connector/v1/services.py">get_availability_2024_01_22</a>(\*\*<a href="src/pymews/types/api/connector/v1/service_get_availability_2024_01_22_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/service_get_availability_2024_01_22_response.py">ServiceGetAvailability2024_01_22Response</a></code>
- <code title="post /api/connector/v1/services/updateAvailability">client.api.connector.v1.services.<a href="./src/pymews/resources/api/connector/v1/services.py">update_availability</a>(\*\*<a href="src/pymews/types/api/connector/v1/service_update_availability_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/unit.py">object</a></code>

#### Tasks

Types:

```python
from pymews.types.api.connector.v1 import TaskListResponse, TaskAddResponse
```

Methods:

- <code title="post /api/connector/v1/tasks/getAll">client.api.connector.v1.tasks.<a href="./src/pymews/resources/api/connector/v1/tasks.py">list</a>(\*\*<a href="src/pymews/types/api/connector/v1/task_list_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/task_list_response.py">TaskListResponse</a></code>
- <code title="post /api/connector/v1/tasks/add">client.api.connector.v1.tasks.<a href="./src/pymews/resources/api/connector/v1/tasks.py">add</a>(\*\*<a href="src/pymews/types/api/connector/v1/task_add_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/task_add_response.py">TaskAddResponse</a></code>

#### VoucherCodes

Types:

```python
from pymews.types.api.connector.v1 import VoucherCodeResult
```

Methods:

- <code title="post /api/connector/v1/voucherCodes/getAll">client.api.connector.v1.voucher_codes.<a href="./src/pymews/resources/api/connector/v1/voucher_codes.py">list</a>(\*\*<a href="src/pymews/types/api/connector/v1/voucher_code_list_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/voucher_code_result.py">VoucherCodeResult</a></code>
- <code title="post /api/connector/v1/voucherCodes/delete">client.api.connector.v1.voucher_codes.<a href="./src/pymews/resources/api/connector/v1/voucher_codes.py">delete</a>(\*\*<a href="src/pymews/types/api/connector/v1/voucher_code_delete_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/unit.py">object</a></code>
- <code title="post /api/connector/v1/voucherCodes/add">client.api.connector.v1.voucher_codes.<a href="./src/pymews/resources/api/connector/v1/voucher_codes.py">add</a>(\*\*<a href="src/pymews/types/api/connector/v1/voucher_code_add_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/voucher_code_result.py">VoucherCodeResult</a></code>

#### Vouchers

Types:

```python
from pymews.types.api.connector.v1 import VoucherWriteResult, VoucherListResponse
```

Methods:

- <code title="post /api/connector/v1/vouchers/update">client.api.connector.v1.vouchers.<a href="./src/pymews/resources/api/connector/v1/vouchers.py">update</a>(\*\*<a href="src/pymews/types/api/connector/v1/voucher_update_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/voucher_write_result.py">VoucherWriteResult</a></code>
- <code title="post /api/connector/v1/vouchers/getAll">client.api.connector.v1.vouchers.<a href="./src/pymews/resources/api/connector/v1/vouchers.py">list</a>(\*\*<a href="src/pymews/types/api/connector/v1/voucher_list_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/voucher_list_response.py">VoucherListResponse</a></code>
- <code title="post /api/connector/v1/vouchers/delete">client.api.connector.v1.vouchers.<a href="./src/pymews/resources/api/connector/v1/vouchers.py">delete</a>(\*\*<a href="src/pymews/types/api/connector/v1/voucher_delete_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/unit.py">object</a></code>
- <code title="post /api/connector/v1/vouchers/add">client.api.connector.v1.vouchers.<a href="./src/pymews/resources/api/connector/v1/vouchers.py">add</a>(\*\*<a href="src/pymews/types/api/connector/v1/voucher_add_params.py">params</a>) -> <a href="./src/pymews/types/api/connector/v1/voucher_write_result.py">VoucherWriteResult</a></code>
