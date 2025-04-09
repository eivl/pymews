# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pymews import Pymews, AsyncPymews
from tests.utils import assert_matches_type
from pymews._utils import parse_date, parse_datetime
from pymews.types.api.connector import (
    V1AddOrderResponse,
    V1ListRulesResponse,
    V1ListDevicesResponse,
    V1ListOutletsResponse,
    V1ListSourcesResponse,
    V1GetImageURLsResponse,
    V1ListCashiersResponse,
    V1ListCountersResponse,
    V1AddOutletBillResponse,
    V1ListCountriesResponse,
    V1ListTaxationsResponse,
    V1ListCurrenciesResponse,
    V1ListRateGroupsResponse,
    V1ListDepartmentsResponse,
    V1ListEnterprisesResponse,
    V1ListOutletItemsResponse,
    V1GetConfigurationResponse,
    V1ListAgeCategoriesResponse,
    V1ListExchangeRatesResponse,
    V1ListCompanionshipsResponse,
    V1ListLedgerBalancesResponse,
    V1ListTaxEnvironmentsResponse,
    V1ListBusinessSegmentsResponse,
    V1ListResourceFeaturesResponse,
    V1ListProductCategoriesResponse,
    V1ListReservationGroupsResponse,
    V1ListResourceCategoriesResponse,
    V1GetAllSourceAssignmentsResponse,
    V1ListCashierTransactionsResponse,
    V1ListAccountingCategoriesResponse,
    V1ListProductServiceOrdersResponse,
    V1ListAvailabilityAdjustmentsResponse,
    V1ListResourceFeatureAssignmentsResponse,
    V1ListResourceCategoryAssignmentsResponse,
    V1ListPreauthorizationsByCustomersResponse,
    V1GetAllSourceAssignments2024_09_20Response,
    V1ListResourceCategoryImageAssignmentsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestV1:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_add_order(self, client: Pymews) -> None:
        v1 = client.api.connector.v1.add_order(
            access_token="7059D2C25BF64EA681ACAB3A00B859CC-D91BFF2B1E3047A3E0DEC1D57BE1382",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            service_id="d2129910-1da9-4d39-be14-ab3a00c9e70c",
        )
        assert_matches_type(V1AddOrderResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_add_order_with_all_params(self, client: Pymews) -> None:
        v1 = client.api.connector.v1.add_order(
            access_token="7059D2C25BF64EA681ACAB3A00B859CC-D91BFF2B1E3047A3E0DEC1D57BE1382",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            service_id="d2129910-1da9-4d39-be14-ab3a00c9e70c",
            account_id="407a26f8-dcfc-4e29-b978-ab440117a153",
            bill_id="22b68915-05fe-4a31-b1cb-bd5efa35d305",
            business_segment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            consumption_utc=parse_datetime("2020-02-04T00:00:00Z"),
            customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            enterprise_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
            items=[
                {
                    "name": "Beer",
                    "unit_amount": {
                        "currency": "USD",
                        "tax_codes": ["US-DC-G"],
                        "gross_value": 0,
                        "net_value": 7,
                    },
                    "unit_count": 3,
                    "accounting_category_id": "90eff5aa-36b4-4689-80c0-ab3a00bb412e",
                    "category": {
                        "code": "Code",
                        "name": "Name",
                    },
                    "external_identifier": "ExternalIdentifier",
                }
            ],
            linked_reservation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            notes="Notes",
            options={"disable_item_grouping": True},
            product_orders=[
                {
                    "product_id": "2eb7ad8b-8dfb-4381-aba5-ab58009f2993",
                    "count": 2,
                    "end_utc": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "external_identifier": "ExternalIdentifier",
                    "start_utc": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "unit_amount": {
                        "currency": "x",
                        "tax_codes": ["string"],
                        "gross_value": 0,
                        "net_value": 0,
                    },
                }
            ],
        )
        assert_matches_type(V1AddOrderResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_add_order(self, client: Pymews) -> None:
        response = client.api.connector.v1.with_raw_response.add_order(
            access_token="7059D2C25BF64EA681ACAB3A00B859CC-D91BFF2B1E3047A3E0DEC1D57BE1382",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            service_id="d2129910-1da9-4d39-be14-ab3a00c9e70c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1AddOrderResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_add_order(self, client: Pymews) -> None:
        with client.api.connector.v1.with_streaming_response.add_order(
            access_token="7059D2C25BF64EA681ACAB3A00B859CC-D91BFF2B1E3047A3E0DEC1D57BE1382",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            service_id="d2129910-1da9-4d39-be14-ab3a00c9e70c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1AddOrderResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_add_outlet_bill(self, client: Pymews) -> None:
        v1 = client.api.connector.v1.add_outlet_bill(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            bills=[
                {
                    "closed_utc": "2017-01-01T00:00:00Z",
                    "items": [
                        {
                            "consumed_utc": parse_datetime("2017-01-01T00:00:00Z"),
                            "name": "Cash payment",
                            "unit_amount": {
                                "currency": "GBP",
                                "tax_codes": ["UK-S"],
                            },
                            "unit_count": 1,
                        },
                        {
                            "consumed_utc": parse_datetime("2017-01-01T00:00:00Z"),
                            "name": "Beer",
                            "unit_amount": {
                                "currency": "GBP",
                                "tax_codes": ["UK-S"],
                            },
                            "unit_count": 10,
                        },
                    ],
                    "number": "1257",
                    "outlet_id": "7700469f-7667-4ebd-a1c0-10380afc9bd0",
                }
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )
        assert_matches_type(V1AddOutletBillResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_add_outlet_bill(self, client: Pymews) -> None:
        response = client.api.connector.v1.with_raw_response.add_outlet_bill(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            bills=[
                {
                    "closed_utc": "2017-01-01T00:00:00Z",
                    "items": [
                        {
                            "consumed_utc": parse_datetime("2017-01-01T00:00:00Z"),
                            "name": "Cash payment",
                            "unit_amount": {
                                "currency": "GBP",
                                "tax_codes": ["UK-S"],
                            },
                            "unit_count": 1,
                        },
                        {
                            "consumed_utc": parse_datetime("2017-01-01T00:00:00Z"),
                            "name": "Beer",
                            "unit_amount": {
                                "currency": "GBP",
                                "tax_codes": ["UK-S"],
                            },
                            "unit_count": 10,
                        },
                    ],
                    "number": "1257",
                    "outlet_id": "7700469f-7667-4ebd-a1c0-10380afc9bd0",
                }
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1AddOutletBillResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_add_outlet_bill(self, client: Pymews) -> None:
        with client.api.connector.v1.with_streaming_response.add_outlet_bill(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            bills=[
                {
                    "closed_utc": "2017-01-01T00:00:00Z",
                    "items": [
                        {
                            "consumed_utc": parse_datetime("2017-01-01T00:00:00Z"),
                            "name": "Cash payment",
                            "unit_amount": {
                                "currency": "GBP",
                                "tax_codes": ["UK-S"],
                            },
                            "unit_count": 1,
                        },
                        {
                            "consumed_utc": parse_datetime("2017-01-01T00:00:00Z"),
                            "name": "Beer",
                            "unit_amount": {
                                "currency": "GBP",
                                "tax_codes": ["UK-S"],
                            },
                            "unit_count": 10,
                        },
                    ],
                    "number": "1257",
                    "outlet_id": "7700469f-7667-4ebd-a1c0-10380afc9bd0",
                }
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1AddOutletBillResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_all_source_assignments(self, client: Pymews) -> None:
        v1 = client.api.connector.v1.get_all_source_assignments(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )
        assert_matches_type(V1GetAllSourceAssignmentsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_all_source_assignments_with_all_params(self, client: Pymews) -> None:
        v1 = client.api.connector.v1.get_all_source_assignments(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            reservation_group_ids=["730d050c-8098-415a-95af-af2500a2de47"],
            updated_utc={
                "end_utc": parse_datetime("2023-02-28T00:00:00Z"),
                "start_utc": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
        )
        assert_matches_type(V1GetAllSourceAssignmentsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_all_source_assignments(self, client: Pymews) -> None:
        response = client.api.connector.v1.with_raw_response.get_all_source_assignments(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1GetAllSourceAssignmentsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_all_source_assignments(self, client: Pymews) -> None:
        with client.api.connector.v1.with_streaming_response.get_all_source_assignments(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1GetAllSourceAssignmentsResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_all_source_assignments_2024_09_20(self, client: Pymews) -> None:
        v1 = client.api.connector.v1.get_all_source_assignments_2024_09_20(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )
        assert_matches_type(V1GetAllSourceAssignments2024_09_20Response, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_all_source_assignments_2024_09_20_with_all_params(self, client: Pymews) -> None:
        v1 = client.api.connector.v1.get_all_source_assignments_2024_09_20(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            enterprise_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            reservation_ids=["9b59b50d-bd32-4ce5-add8-09ea0e1300e7"],
        )
        assert_matches_type(V1GetAllSourceAssignments2024_09_20Response, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_all_source_assignments_2024_09_20(self, client: Pymews) -> None:
        response = client.api.connector.v1.with_raw_response.get_all_source_assignments_2024_09_20(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1GetAllSourceAssignments2024_09_20Response, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_all_source_assignments_2024_09_20(self, client: Pymews) -> None:
        with client.api.connector.v1.with_streaming_response.get_all_source_assignments_2024_09_20(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1GetAllSourceAssignments2024_09_20Response, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_configuration(self, client: Pymews) -> None:
        v1 = client.api.connector.v1.get_configuration(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )
        assert_matches_type(V1GetConfigurationResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_configuration_with_all_params(self, client: Pymews) -> None:
        v1 = client.api.connector.v1.get_configuration(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            enterprise_id="851df8c8-90f2-4c4a-8e01-a4fc46b25178",
        )
        assert_matches_type(V1GetConfigurationResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_configuration(self, client: Pymews) -> None:
        response = client.api.connector.v1.with_raw_response.get_configuration(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1GetConfigurationResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_configuration(self, client: Pymews) -> None:
        with client.api.connector.v1.with_streaming_response.get_configuration(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1GetConfigurationResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_image_urls(self, client: Pymews) -> None:
        v1 = client.api.connector.v1.get_image_urls(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            images=[{"image_id": "57a971a5-a335-48f4-8cd1-595245d1a876"}],
        )
        assert_matches_type(V1GetImageURLsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_image_urls(self, client: Pymews) -> None:
        response = client.api.connector.v1.with_raw_response.get_image_urls(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            images=[{"image_id": "57a971a5-a335-48f4-8cd1-595245d1a876"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1GetImageURLsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_image_urls(self, client: Pymews) -> None:
        with client.api.connector.v1.with_streaming_response.get_image_urls(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            images=[{"image_id": "57a971a5-a335-48f4-8cd1-595245d1a876"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1GetImageURLsResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list_accounting_categories(self, client: Pymews) -> None:
        v1 = client.api.connector.v1.list_accounting_categories(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )
        assert_matches_type(V1ListAccountingCategoriesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_accounting_categories_with_all_params(self, client: Pymews) -> None:
        v1 = client.api.connector.v1.list_accounting_categories(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            accounting_category_ids=["0cf7aa90-736f-43e9-a7dc-787704548d86", "0b9560fb-055d-47d3-a6d4-e579c44ca558"],
            activity_states=["Active"],
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            updated_utc={
                "end_utc": parse_datetime("2023-10-31T00:00:00Z"),
                "start_utc": parse_datetime("2023-10-01T00:00:00Z"),
            },
        )
        assert_matches_type(V1ListAccountingCategoriesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_accounting_categories(self, client: Pymews) -> None:
        response = client.api.connector.v1.with_raw_response.list_accounting_categories(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1ListAccountingCategoriesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_accounting_categories(self, client: Pymews) -> None:
        with client.api.connector.v1.with_streaming_response.list_accounting_categories(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1ListAccountingCategoriesResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list_age_categories(self, client: Pymews) -> None:
        v1 = client.api.connector.v1.list_age_categories(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )
        assert_matches_type(V1ListAgeCategoriesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_age_categories_with_all_params(self, client: Pymews) -> None:
        v1 = client.api.connector.v1.list_age_categories(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            activity_states=["Active"],
            age_category_ids=["fe568bbd-1ecb-4bb2-bf77-96c3698de20d", "ab58c939-be30-4a60-8f75-ae1600c60c9f"],
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            service_ids=["bd26d8db-86da-4f96-9efc-e5a4654a4a94"],
            updated_utc={
                "end_utc": parse_datetime("2023-10-31T00:00:00Z"),
                "start_utc": parse_datetime("2023-10-01T00:00:00Z"),
            },
        )
        assert_matches_type(V1ListAgeCategoriesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_age_categories(self, client: Pymews) -> None:
        response = client.api.connector.v1.with_raw_response.list_age_categories(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1ListAgeCategoriesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_age_categories(self, client: Pymews) -> None:
        with client.api.connector.v1.with_streaming_response.list_age_categories(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1ListAgeCategoriesResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list_availability_adjustments(self, client: Pymews) -> None:
        v1 = client.api.connector.v1.list_availability_adjustments(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )
        assert_matches_type(V1ListAvailabilityAdjustmentsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_availability_adjustments_with_all_params(self, client: Pymews) -> None:
        v1 = client.api.connector.v1.list_availability_adjustments(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            activity_states=["Active", "Deleted"],
            availability_adjustment_ids=[
                "e19297af-373e-4701-b4ea-afae0129bded",
                "7413724a-6c48-46d4-ab3a-afae01280999",
            ],
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            updated_utc={
                "end_utc": parse_datetime("2023-02-20T18:00:10.155Z"),
                "start_utc": parse_datetime("2023-02-18T18:00:10.155Z"),
            },
        )
        assert_matches_type(V1ListAvailabilityAdjustmentsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_availability_adjustments(self, client: Pymews) -> None:
        response = client.api.connector.v1.with_raw_response.list_availability_adjustments(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1ListAvailabilityAdjustmentsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_availability_adjustments(self, client: Pymews) -> None:
        with client.api.connector.v1.with_streaming_response.list_availability_adjustments(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1ListAvailabilityAdjustmentsResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list_business_segments(self, client: Pymews) -> None:
        v1 = client.api.connector.v1.list_business_segments(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )
        assert_matches_type(V1ListBusinessSegmentsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_business_segments_with_all_params(self, client: Pymews) -> None:
        v1 = client.api.connector.v1.list_business_segments(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            activity_states=["Active"],
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            ids=["7760b5cb-a666-41bb-9758-76bf5d1df399", "54ec08b6-e6fc-48e9-b8ae-02943e0ac693"],
            service_ids=["bd26d8db-86da-4f96-9efc-e5a4654a4a94", "8c1bd738-a505-4b29-aa71-9ecc2982b843"],
            updated_utc={
                "end_utc": parse_datetime("2023-10-31T00:00:00Z"),
                "start_utc": parse_datetime("2023-10-01T00:00:00Z"),
            },
        )
        assert_matches_type(V1ListBusinessSegmentsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_business_segments(self, client: Pymews) -> None:
        response = client.api.connector.v1.with_raw_response.list_business_segments(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1ListBusinessSegmentsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_business_segments(self, client: Pymews) -> None:
        with client.api.connector.v1.with_streaming_response.list_business_segments(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1ListBusinessSegmentsResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list_cashier_transactions(self, client: Pymews) -> None:
        v1 = client.api.connector.v1.list_cashier_transactions(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )
        assert_matches_type(V1ListCashierTransactionsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_cashier_transactions_with_all_params(self, client: Pymews) -> None:
        v1 = client.api.connector.v1.list_cashier_transactions(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            cashier_transaction_ids=["177740c3-fec9-4338-a224-a3b03a35b3e1"],
            created_utc={
                "end_utc": parse_datetime("2020-01-10T00:00:00Z"),
                "start_utc": parse_datetime("2020-01-05T00:00:00Z"),
            },
            end_utc="EndUtc",
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            start_utc="StartUtc",
        )
        assert_matches_type(V1ListCashierTransactionsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_cashier_transactions(self, client: Pymews) -> None:
        response = client.api.connector.v1.with_raw_response.list_cashier_transactions(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1ListCashierTransactionsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_cashier_transactions(self, client: Pymews) -> None:
        with client.api.connector.v1.with_streaming_response.list_cashier_transactions(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1ListCashierTransactionsResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list_cashiers(self, client: Pymews) -> None:
        v1 = client.api.connector.v1.list_cashiers(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )
        assert_matches_type(V1ListCashiersResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_cashiers_with_all_params(self, client: Pymews) -> None:
        v1 = client.api.connector.v1.list_cashiers(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            activity_states=["Active"],
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            ids=["9a36e3fa-2299-474b-a8a2-5ea4da317abc"],
            updated_utc={
                "end_utc": parse_datetime("2023-10-31T00:00:00Z"),
                "start_utc": parse_datetime("2023-10-01T00:00:00Z"),
            },
        )
        assert_matches_type(V1ListCashiersResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_cashiers(self, client: Pymews) -> None:
        response = client.api.connector.v1.with_raw_response.list_cashiers(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1ListCashiersResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_cashiers(self, client: Pymews) -> None:
        with client.api.connector.v1.with_streaming_response.list_cashiers(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1ListCashiersResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list_companionships(self, client: Pymews) -> None:
        v1 = client.api.connector.v1.list_companionships(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            extent={},
            limitation={"count": 10},
        )
        assert_matches_type(V1ListCompanionshipsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_companionships_with_all_params(self, client: Pymews) -> None:
        v1 = client.api.connector.v1.list_companionships(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            extent={
                "customers": True,
                "reservation_groups": True,
                "reservations": True,
            },
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            companionship_ids=["72d4b117-1f84-44a3-1f84-8b2c0635ac60"],
            customer_ids=["35d4b117-4e60-44a3-9580-c582117eff98"],
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            reservation_group_ids=["c704dff3-7811-4af7-a3a0-7b2b0635ac59"],
            reservation_ids=["bfee2c44-1f84-4326-a862-5289598f6e2d"],
            updated_utc={
                "end_utc": parse_datetime("2020-02-10T00:00:00Z"),
                "start_utc": parse_datetime("2020-02-05T00:00:00Z"),
            },
        )
        assert_matches_type(V1ListCompanionshipsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_companionships(self, client: Pymews) -> None:
        response = client.api.connector.v1.with_raw_response.list_companionships(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            extent={},
            limitation={"count": 10},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1ListCompanionshipsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_companionships(self, client: Pymews) -> None:
        with client.api.connector.v1.with_streaming_response.list_companionships(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            extent={},
            limitation={"count": 10},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1ListCompanionshipsResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list_counters(self, client: Pymews) -> None:
        v1 = client.api.connector.v1.list_counters(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )
        assert_matches_type(V1ListCountersResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_counters_with_all_params(self, client: Pymews) -> None:
        v1 = client.api.connector.v1.list_counters(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            counter_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            type="Counter",
            updated_utc={
                "end_utc": parse_datetime("2023-10-31T00:00:00Z"),
                "start_utc": parse_datetime("2023-10-01T00:00:00Z"),
            },
        )
        assert_matches_type(V1ListCountersResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_counters(self, client: Pymews) -> None:
        response = client.api.connector.v1.with_raw_response.list_counters(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1ListCountersResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_counters(self, client: Pymews) -> None:
        with client.api.connector.v1.with_streaming_response.list_counters(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1ListCountersResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list_countries(self, client: Pymews) -> None:
        v1 = client.api.connector.v1.list_countries(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )
        assert_matches_type(V1ListCountriesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_countries(self, client: Pymews) -> None:
        response = client.api.connector.v1.with_raw_response.list_countries(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1ListCountriesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_countries(self, client: Pymews) -> None:
        with client.api.connector.v1.with_streaming_response.list_countries(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1ListCountriesResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list_currencies(self, client: Pymews) -> None:
        v1 = client.api.connector.v1.list_currencies(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )
        assert_matches_type(V1ListCurrenciesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_currencies(self, client: Pymews) -> None:
        response = client.api.connector.v1.with_raw_response.list_currencies(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1ListCurrenciesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_currencies(self, client: Pymews) -> None:
        with client.api.connector.v1.with_streaming_response.list_currencies(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1ListCurrenciesResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list_departments(self, client: Pymews) -> None:
        v1 = client.api.connector.v1.list_departments(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )
        assert_matches_type(V1ListDepartmentsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_departments_with_all_params(self, client: Pymews) -> None:
        v1 = client.api.connector.v1.list_departments(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            department_ids=["98776d06-60e4-495f-82f1-95ab2f644d63", "915fbb82-de35-48a0-9e9b-f4a7eac711bb"],
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            updated_utc={
                "end_utc": parse_datetime("2023-10-31T00:00:00Z"),
                "start_utc": parse_datetime("2023-10-01T00:00:00Z"),
            },
        )
        assert_matches_type(V1ListDepartmentsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_departments(self, client: Pymews) -> None:
        response = client.api.connector.v1.with_raw_response.list_departments(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1ListDepartmentsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_departments(self, client: Pymews) -> None:
        with client.api.connector.v1.with_streaming_response.list_departments(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1ListDepartmentsResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list_devices(self, client: Pymews) -> None:
        v1 = client.api.connector.v1.list_devices(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )
        assert_matches_type(V1ListDevicesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_devices(self, client: Pymews) -> None:
        response = client.api.connector.v1.with_raw_response.list_devices(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1ListDevicesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_devices(self, client: Pymews) -> None:
        with client.api.connector.v1.with_streaming_response.list_devices(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1ListDevicesResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list_enterprises(self, client: Pymews) -> None:
        v1 = client.api.connector.v1.list_enterprises(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 100},
        )
        assert_matches_type(V1ListEnterprisesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_enterprises_with_all_params(self, client: Pymews) -> None:
        v1 = client.api.connector.v1.list_enterprises(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 100,
                "cursor": "4d0201db-36f5-428b-8d11-4f0a65e960cc",
            },
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            external_identifiers=["Enterprise2023"],
            linked_utc={
                "end_utc": parse_datetime("2023-06-06T00:00:00Z"),
                "start_utc": parse_datetime("2023-06-01T00:00:00Z"),
            },
            updated_utc={
                "end_utc": parse_datetime("2023-10-31T00:00:00Z"),
                "start_utc": parse_datetime("2023-10-01T00:00:00Z"),
            },
        )
        assert_matches_type(V1ListEnterprisesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_enterprises(self, client: Pymews) -> None:
        response = client.api.connector.v1.with_raw_response.list_enterprises(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 100},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1ListEnterprisesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_enterprises(self, client: Pymews) -> None:
        with client.api.connector.v1.with_streaming_response.list_enterprises(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 100},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1ListEnterprisesResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list_exchange_rates(self, client: Pymews) -> None:
        v1 = client.api.connector.v1.list_exchange_rates(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )
        assert_matches_type(V1ListExchangeRatesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_exchange_rates_with_all_params(self, client: Pymews) -> None:
        v1 = client.api.connector.v1.list_exchange_rates(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            enterprise_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(V1ListExchangeRatesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_exchange_rates(self, client: Pymews) -> None:
        response = client.api.connector.v1.with_raw_response.list_exchange_rates(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1ListExchangeRatesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_exchange_rates(self, client: Pymews) -> None:
        with client.api.connector.v1.with_streaming_response.list_exchange_rates(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1ListExchangeRatesResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list_ledger_balances(self, client: Pymews) -> None:
        v1 = client.api.connector.v1.list_ledger_balances(
            access_token="x",
            client="x",
            client_token="x",
            date={
                "end": parse_date("2019-12-27"),
                "start": parse_date("2019-12-27"),
            },
            ledger_types=["Revenue"],
            limitation={"count": 0},
        )
        assert_matches_type(V1ListLedgerBalancesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_ledger_balances_with_all_params(self, client: Pymews) -> None:
        v1 = client.api.connector.v1.list_ledger_balances(
            access_token="x",
            client="x",
            client_token="x",
            date={
                "end": parse_date("2019-12-27"),
                "start": parse_date("2019-12-27"),
            },
            ledger_types=["Revenue"],
            limitation={
                "count": 0,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            enterprise_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(V1ListLedgerBalancesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_ledger_balances(self, client: Pymews) -> None:
        response = client.api.connector.v1.with_raw_response.list_ledger_balances(
            access_token="x",
            client="x",
            client_token="x",
            date={
                "end": parse_date("2019-12-27"),
                "start": parse_date("2019-12-27"),
            },
            ledger_types=["Revenue"],
            limitation={"count": 0},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1ListLedgerBalancesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_ledger_balances(self, client: Pymews) -> None:
        with client.api.connector.v1.with_streaming_response.list_ledger_balances(
            access_token="x",
            client="x",
            client_token="x",
            date={
                "end": parse_date("2019-12-27"),
                "start": parse_date("2019-12-27"),
            },
            ledger_types=["Revenue"],
            limitation={"count": 0},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1ListLedgerBalancesResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list_outlet_items(self, client: Pymews) -> None:
        v1 = client.api.connector.v1.list_outlet_items(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 100},
        )
        assert_matches_type(V1ListOutletItemsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_outlet_items_with_all_params(self, client: Pymews) -> None:
        v1 = client.api.connector.v1.list_outlet_items(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 100,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            closed_utc={
                "end_utc": parse_datetime("2020-01-10T00:00:00Z"),
                "start_utc": parse_datetime("2020-01-05T00:00:00Z"),
            },
            consumed_utc={
                "end_utc": parse_datetime("2020-01-10T00:00:00Z"),
                "start_utc": parse_datetime("2020-01-05T00:00:00Z"),
            },
            currency="EUR",
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            updated_utc={
                "end_utc": parse_datetime("2020-01-10T00:00:00Z"),
                "start_utc": parse_datetime("2020-01-05T00:00:00Z"),
            },
        )
        assert_matches_type(V1ListOutletItemsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_outlet_items(self, client: Pymews) -> None:
        response = client.api.connector.v1.with_raw_response.list_outlet_items(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 100},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1ListOutletItemsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_outlet_items(self, client: Pymews) -> None:
        with client.api.connector.v1.with_streaming_response.list_outlet_items(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 100},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1ListOutletItemsResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list_outlets(self, client: Pymews) -> None:
        v1 = client.api.connector.v1.list_outlets(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 100},
        )
        assert_matches_type(V1ListOutletsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_outlets_with_all_params(self, client: Pymews) -> None:
        v1 = client.api.connector.v1.list_outlets(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 100,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            outlet_ids=["7700469f-7667-4ebd-a1c0-10380afc9bd0", "2accff7b-feea-436a-9670-afa9bdb8c8d2"],
            updated_utc={
                "end_utc": parse_datetime("2023-10-31T00:00:00Z"),
                "start_utc": parse_datetime("2023-10-01T00:00:00Z"),
            },
        )
        assert_matches_type(V1ListOutletsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_outlets(self, client: Pymews) -> None:
        response = client.api.connector.v1.with_raw_response.list_outlets(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 100},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1ListOutletsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_outlets(self, client: Pymews) -> None:
        with client.api.connector.v1.with_streaming_response.list_outlets(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 100},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1ListOutletsResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list_preauthorizations_by_customers(self, client: Pymews) -> None:
        v1 = client.api.connector.v1.list_preauthorizations_by_customers(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_ids=["e98995b0-140a-4208-bbeb-b77f2c43d6ee"],
        )
        assert_matches_type(V1ListPreauthorizationsByCustomersResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_preauthorizations_by_customers(self, client: Pymews) -> None:
        response = client.api.connector.v1.with_raw_response.list_preauthorizations_by_customers(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_ids=["e98995b0-140a-4208-bbeb-b77f2c43d6ee"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1ListPreauthorizationsByCustomersResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_preauthorizations_by_customers(self, client: Pymews) -> None:
        with client.api.connector.v1.with_streaming_response.list_preauthorizations_by_customers(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_ids=["e98995b0-140a-4208-bbeb-b77f2c43d6ee"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1ListPreauthorizationsByCustomersResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list_product_categories(self, client: Pymews) -> None:
        v1 = client.api.connector.v1.list_product_categories(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )
        assert_matches_type(V1ListProductCategoriesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_product_categories_with_all_params(self, client: Pymews) -> None:
        v1 = client.api.connector.v1.list_product_categories(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            product_category_ids=["5228623e-b2cf-4f9f-8bd6-71cbe3ec5e6f", "63bc87d3-edf5-4d06-a601-6052a2ad709d"],
            service_ids=["9b3a6c54-63aa-4383-b50e-b0030078184b", "c0f71466-6c0b-4993-88ac-1794f6b7e958"],
            updated_utc={
                "end_utc": parse_datetime("2023-05-10T00:00:00Z"),
                "start_utc": parse_datetime("2023-05-05T00:00:00Z"),
            },
        )
        assert_matches_type(V1ListProductCategoriesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_product_categories(self, client: Pymews) -> None:
        response = client.api.connector.v1.with_raw_response.list_product_categories(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1ListProductCategoriesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_product_categories(self, client: Pymews) -> None:
        with client.api.connector.v1.with_streaming_response.list_product_categories(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1ListProductCategoriesResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list_product_service_orders(self, client: Pymews) -> None:
        v1 = client.api.connector.v1.list_product_service_orders(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            service_ids=["ae8da28c-e8a4-4141-9df0-8c998976c691", "6b02d015-47ac-4c41-8e9f-5b4db61d4284"],
        )
        assert_matches_type(V1ListProductServiceOrdersResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_product_service_orders_with_all_params(self, client: Pymews) -> None:
        v1 = client.api.connector.v1.list_product_service_orders(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 10,
                "cursor": "819e3435-7d5e-441f-bc68-76d89c69b8f5",
            },
            service_ids=["ae8da28c-e8a4-4141-9df0-8c998976c691", "6b02d015-47ac-4c41-8e9f-5b4db61d4284"],
            account_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            enterprise_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            linked_reservation_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            product_service_order_ids=["9b59b50d-bd32-4ce5-add8-09ea0e1300e7"],
            states=["Inquired"],
            updated_utc={
                "end_utc": parse_datetime("2023-05-05T00:00:00Z"),
                "start_utc": parse_datetime("2023-04-01T00:00:00Z"),
            },
        )
        assert_matches_type(V1ListProductServiceOrdersResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_product_service_orders(self, client: Pymews) -> None:
        response = client.api.connector.v1.with_raw_response.list_product_service_orders(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            service_ids=["ae8da28c-e8a4-4141-9df0-8c998976c691", "6b02d015-47ac-4c41-8e9f-5b4db61d4284"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1ListProductServiceOrdersResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_product_service_orders(self, client: Pymews) -> None:
        with client.api.connector.v1.with_streaming_response.list_product_service_orders(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            service_ids=["ae8da28c-e8a4-4141-9df0-8c998976c691", "6b02d015-47ac-4c41-8e9f-5b4db61d4284"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1ListProductServiceOrdersResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list_rate_groups(self, client: Pymews) -> None:
        v1 = client.api.connector.v1.list_rate_groups(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 1000},
        )
        assert_matches_type(V1ListRateGroupsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_rate_groups_with_all_params(self, client: Pymews) -> None:
        v1 = client.api.connector.v1.list_rate_groups(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 1000,
                "cursor": "e7f26210-10e7-462e-9da8-ae8300be8ab7",
            },
            activity_states=["Active"],
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            external_identifiers=["RG-001"],
            rate_group_ids=["6b3f718a-b537-45b0-a8ee-d30897723834"],
            service_ids=["bd26d8db-86da-4f96-9efc-e5a4654a4a94"],
            updated_utc={
                "end_utc": parse_datetime("2024-02-27T11:48:57Z"),
                "start_utc": parse_datetime("2024-01-27T11:48:57Z"),
            },
        )
        assert_matches_type(V1ListRateGroupsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_rate_groups(self, client: Pymews) -> None:
        response = client.api.connector.v1.with_raw_response.list_rate_groups(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 1000},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1ListRateGroupsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_rate_groups(self, client: Pymews) -> None:
        with client.api.connector.v1.with_streaming_response.list_rate_groups(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 1000},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1ListRateGroupsResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list_reservation_groups(self, client: Pymews) -> None:
        v1 = client.api.connector.v1.list_reservation_groups(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 100},
        )
        assert_matches_type(V1ListReservationGroupsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_reservation_groups_with_all_params(self, client: Pymews) -> None:
        v1 = client.api.connector.v1.list_reservation_groups(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 100,
                "cursor": "e7f26210-10e7-462e-9da8-ae8300be8ab7",
            },
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            reservation_group_ids=["fe795f96-0b64-445b-89ed-c032563f2bac"],
            updated_utc={
                "end_utc": parse_datetime("2023-04-27T11:48:57Z"),
                "start_utc": parse_datetime("2023-04-27T11:48:57Z"),
            },
        )
        assert_matches_type(V1ListReservationGroupsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_reservation_groups(self, client: Pymews) -> None:
        response = client.api.connector.v1.with_raw_response.list_reservation_groups(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 100},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1ListReservationGroupsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_reservation_groups(self, client: Pymews) -> None:
        with client.api.connector.v1.with_streaming_response.list_reservation_groups(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 100},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1ListReservationGroupsResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list_resource_categories(self, client: Pymews) -> None:
        v1 = client.api.connector.v1.list_resource_categories(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            service_ids=["9b3a6c54-63aa-4383-b50e-b0030078184b", "c0f71466-6c0b-4993-88ac-1794f6b7e958"],
        )
        assert_matches_type(V1ListResourceCategoriesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_resource_categories_with_all_params(self, client: Pymews) -> None:
        v1 = client.api.connector.v1.list_resource_categories(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            service_ids=["9b3a6c54-63aa-4383-b50e-b0030078184b", "c0f71466-6c0b-4993-88ac-1794f6b7e958"],
            activity_states=["Active"],
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            resource_category_ids=["5c0804f9-d03a-4b13-a57d-b00300781a41", "47d6b462-35ec-467e-a565-b00300781a41"],
            updated_utc={
                "end_utc": parse_datetime("2023-05-10T00:00:00Z"),
                "start_utc": parse_datetime("2023-05-05T00:00:00Z"),
            },
        )
        assert_matches_type(V1ListResourceCategoriesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_resource_categories(self, client: Pymews) -> None:
        response = client.api.connector.v1.with_raw_response.list_resource_categories(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            service_ids=["9b3a6c54-63aa-4383-b50e-b0030078184b", "c0f71466-6c0b-4993-88ac-1794f6b7e958"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1ListResourceCategoriesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_resource_categories(self, client: Pymews) -> None:
        with client.api.connector.v1.with_streaming_response.list_resource_categories(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            service_ids=["9b3a6c54-63aa-4383-b50e-b0030078184b", "c0f71466-6c0b-4993-88ac-1794f6b7e958"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1ListResourceCategoriesResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list_resource_category_assignments(self, client: Pymews) -> None:
        v1 = client.api.connector.v1.list_resource_category_assignments(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            resource_category_ids=["5c0804f9-d03a-4b13-a57d-b00300781a41", "47d6b462-35ec-467e-a565-b00300781a41"],
        )
        assert_matches_type(V1ListResourceCategoryAssignmentsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_resource_category_assignments_with_all_params(self, client: Pymews) -> None:
        v1 = client.api.connector.v1.list_resource_category_assignments(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 10,
                "cursor": "e7f26210-10e7-462e-9da8-ae8300be8ab7",
            },
            resource_category_ids=["5c0804f9-d03a-4b13-a57d-b00300781a41", "47d6b462-35ec-467e-a565-b00300781a41"],
            activity_states=["Active"],
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            resource_category_assignment_ids=[
                "fb69fc51-c4e9-4ef6-874a-24bcfe74a894",
                "28704948-77df-4bb4-8f39-f8380dc8a914",
            ],
            resource_ids=["5ee074b1-6c86-48e8-915f-c7aa4702086f", "c32386aa-1cd2-414a-a823-489325842fbe"],
            updated_utc={
                "end_utc": parse_datetime("2023-11-30T00:00:00Z"),
                "start_utc": parse_datetime("2023-11-01T00:00:00Z"),
            },
        )
        assert_matches_type(V1ListResourceCategoryAssignmentsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_resource_category_assignments(self, client: Pymews) -> None:
        response = client.api.connector.v1.with_raw_response.list_resource_category_assignments(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            resource_category_ids=["5c0804f9-d03a-4b13-a57d-b00300781a41", "47d6b462-35ec-467e-a565-b00300781a41"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1ListResourceCategoryAssignmentsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_resource_category_assignments(self, client: Pymews) -> None:
        with client.api.connector.v1.with_streaming_response.list_resource_category_assignments(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            resource_category_ids=["5c0804f9-d03a-4b13-a57d-b00300781a41", "47d6b462-35ec-467e-a565-b00300781a41"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1ListResourceCategoryAssignmentsResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list_resource_category_image_assignments(self, client: Pymews) -> None:
        v1 = client.api.connector.v1.list_resource_category_image_assignments(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            resource_category_ids=["5c0804f9-d03a-4b13-a57d-b00300781a41", "47d6b462-35ec-467e-a565-b00300781a41"],
        )
        assert_matches_type(V1ListResourceCategoryImageAssignmentsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_resource_category_image_assignments_with_all_params(self, client: Pymews) -> None:
        v1 = client.api.connector.v1.list_resource_category_image_assignments(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            resource_category_ids=["5c0804f9-d03a-4b13-a57d-b00300781a41", "47d6b462-35ec-467e-a565-b00300781a41"],
            activity_states=["Active"],
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            resource_category_image_assignment_ids=[
                "edb5f556-7afb-4650-8d4e-8c0a6fff784d",
                "9d18f5fb-cce5-4e70-9561-f7804262344b",
            ],
            updated_utc={
                "end_utc": parse_datetime("2023-11-30T00:00:00Z"),
                "start_utc": parse_datetime("2023-11-01T00:00:00Z"),
            },
        )
        assert_matches_type(V1ListResourceCategoryImageAssignmentsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_resource_category_image_assignments(self, client: Pymews) -> None:
        response = client.api.connector.v1.with_raw_response.list_resource_category_image_assignments(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            resource_category_ids=["5c0804f9-d03a-4b13-a57d-b00300781a41", "47d6b462-35ec-467e-a565-b00300781a41"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1ListResourceCategoryImageAssignmentsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_resource_category_image_assignments(self, client: Pymews) -> None:
        with client.api.connector.v1.with_streaming_response.list_resource_category_image_assignments(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            resource_category_ids=["5c0804f9-d03a-4b13-a57d-b00300781a41", "47d6b462-35ec-467e-a565-b00300781a41"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1ListResourceCategoryImageAssignmentsResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list_resource_feature_assignments(self, client: Pymews) -> None:
        v1 = client.api.connector.v1.list_resource_feature_assignments(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            resource_feature_ids=["a693dd8c-21fe-4dae-b450-ea3bd9ab3bb0"],
        )
        assert_matches_type(V1ListResourceFeatureAssignmentsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_resource_feature_assignments_with_all_params(self, client: Pymews) -> None:
        v1 = client.api.connector.v1.list_resource_feature_assignments(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            resource_feature_ids=["a693dd8c-21fe-4dae-b450-ea3bd9ab3bb0"],
            activity_states=["Active"],
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            resource_feature_assignment_ids=["ca2b5bf9-24f5-4faa-95ef-b65d38598b08"],
            updated_utc={
                "end_utc": parse_datetime("2023-11-30T00:00:00Z"),
                "start_utc": parse_datetime("2023-11-01T00:00:00Z"),
            },
        )
        assert_matches_type(V1ListResourceFeatureAssignmentsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_resource_feature_assignments(self, client: Pymews) -> None:
        response = client.api.connector.v1.with_raw_response.list_resource_feature_assignments(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            resource_feature_ids=["a693dd8c-21fe-4dae-b450-ea3bd9ab3bb0"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1ListResourceFeatureAssignmentsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_resource_feature_assignments(self, client: Pymews) -> None:
        with client.api.connector.v1.with_streaming_response.list_resource_feature_assignments(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            resource_feature_ids=["a693dd8c-21fe-4dae-b450-ea3bd9ab3bb0"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1ListResourceFeatureAssignmentsResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list_resource_features(self, client: Pymews) -> None:
        v1 = client.api.connector.v1.list_resource_features(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            service_ids=["24e2ead5-65a8-4ed9-8286-abdb00f08a1f"],
        )
        assert_matches_type(V1ListResourceFeaturesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_resource_features_with_all_params(self, client: Pymews) -> None:
        v1 = client.api.connector.v1.list_resource_features(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            service_ids=["24e2ead5-65a8-4ed9-8286-abdb00f08a1f"],
            activity_states=["Active"],
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            resource_feature_ids=["3d5201ad-4a7b-4cbe-9c22-03dd79c28443"],
            updated_utc={
                "end_utc": parse_datetime("2023-11-30T00:00:00Z"),
                "start_utc": parse_datetime("2023-11-01T00:00:00Z"),
            },
        )
        assert_matches_type(V1ListResourceFeaturesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_resource_features(self, client: Pymews) -> None:
        response = client.api.connector.v1.with_raw_response.list_resource_features(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            service_ids=["24e2ead5-65a8-4ed9-8286-abdb00f08a1f"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1ListResourceFeaturesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_resource_features(self, client: Pymews) -> None:
        with client.api.connector.v1.with_streaming_response.list_resource_features(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            service_ids=["24e2ead5-65a8-4ed9-8286-abdb00f08a1f"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1ListResourceFeaturesResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list_rules(self, client: Pymews) -> None:
        v1 = client.api.connector.v1.list_rules(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            extent={},
            limitation={"count": 10},
            service_ids=["bd26d8db-86da-4f96-9efc-e5a4654a4a94"],
        )
        assert_matches_type(V1ListRulesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_rules_with_all_params(self, client: Pymews) -> None:
        v1 = client.api.connector.v1.list_rules(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            extent={
                "business_segments": True,
                "rate_groups": True,
                "rates": True,
                "resource_categories": True,
                "rule_actions": True,
            },
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            service_ids=["bd26d8db-86da-4f96-9efc-e5a4654a4a94"],
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            updated_utc={
                "end_utc": parse_datetime("2023-10-31T00:00:00Z"),
                "start_utc": parse_datetime("2023-10-01T00:00:00Z"),
            },
        )
        assert_matches_type(V1ListRulesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_rules(self, client: Pymews) -> None:
        response = client.api.connector.v1.with_raw_response.list_rules(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            extent={},
            limitation={"count": 10},
            service_ids=["bd26d8db-86da-4f96-9efc-e5a4654a4a94"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1ListRulesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_rules(self, client: Pymews) -> None:
        with client.api.connector.v1.with_streaming_response.list_rules(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            extent={},
            limitation={"count": 10},
            service_ids=["bd26d8db-86da-4f96-9efc-e5a4654a4a94"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1ListRulesResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list_sources(self, client: Pymews) -> None:
        v1 = client.api.connector.v1.list_sources(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )
        assert_matches_type(V1ListSourcesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_sources_with_all_params(self, client: Pymews) -> None:
        v1 = client.api.connector.v1.list_sources(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 10,
                "cursor": None,
            },
            source_ids=[
                "bbe29c21-401a-4746-b97d-af1f00e1bb8b",
                "22e42a59-b321-43f8-a5d1-af1f00e1bb8b",
                "b5a55d41-bbc5-48d0-a01b-af1f00e1bb8b",
            ],
            updated_utc={
                "end_utc": parse_datetime("2023-01-10T00:00:00Z"),
                "start_utc": parse_datetime("2023-01-05T00:00:00Z"),
            },
        )
        assert_matches_type(V1ListSourcesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_sources(self, client: Pymews) -> None:
        response = client.api.connector.v1.with_raw_response.list_sources(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1ListSourcesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_sources(self, client: Pymews) -> None:
        with client.api.connector.v1.with_streaming_response.list_sources(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1ListSourcesResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list_tax_environments(self, client: Pymews) -> None:
        v1 = client.api.connector.v1.list_tax_environments(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )
        assert_matches_type(V1ListTaxEnvironmentsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_tax_environments(self, client: Pymews) -> None:
        response = client.api.connector.v1.with_raw_response.list_tax_environments(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1ListTaxEnvironmentsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_tax_environments(self, client: Pymews) -> None:
        with client.api.connector.v1.with_streaming_response.list_tax_environments(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1ListTaxEnvironmentsResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list_taxations(self, client: Pymews) -> None:
        v1 = client.api.connector.v1.list_taxations(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )
        assert_matches_type(V1ListTaxationsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_taxations(self, client: Pymews) -> None:
        response = client.api.connector.v1.with_raw_response.list_taxations(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1ListTaxationsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_taxations(self, client: Pymews) -> None:
        with client.api.connector.v1.with_streaming_response.list_taxations(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1ListTaxationsResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncV1:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_add_order(self, async_client: AsyncPymews) -> None:
        v1 = await async_client.api.connector.v1.add_order(
            access_token="7059D2C25BF64EA681ACAB3A00B859CC-D91BFF2B1E3047A3E0DEC1D57BE1382",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            service_id="d2129910-1da9-4d39-be14-ab3a00c9e70c",
        )
        assert_matches_type(V1AddOrderResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_add_order_with_all_params(self, async_client: AsyncPymews) -> None:
        v1 = await async_client.api.connector.v1.add_order(
            access_token="7059D2C25BF64EA681ACAB3A00B859CC-D91BFF2B1E3047A3E0DEC1D57BE1382",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            service_id="d2129910-1da9-4d39-be14-ab3a00c9e70c",
            account_id="407a26f8-dcfc-4e29-b978-ab440117a153",
            bill_id="22b68915-05fe-4a31-b1cb-bd5efa35d305",
            business_segment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            consumption_utc=parse_datetime("2020-02-04T00:00:00Z"),
            customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            enterprise_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
            items=[
                {
                    "name": "Beer",
                    "unit_amount": {
                        "currency": "USD",
                        "tax_codes": ["US-DC-G"],
                        "gross_value": 0,
                        "net_value": 7,
                    },
                    "unit_count": 3,
                    "accounting_category_id": "90eff5aa-36b4-4689-80c0-ab3a00bb412e",
                    "category": {
                        "code": "Code",
                        "name": "Name",
                    },
                    "external_identifier": "ExternalIdentifier",
                }
            ],
            linked_reservation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            notes="Notes",
            options={"disable_item_grouping": True},
            product_orders=[
                {
                    "product_id": "2eb7ad8b-8dfb-4381-aba5-ab58009f2993",
                    "count": 2,
                    "end_utc": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "external_identifier": "ExternalIdentifier",
                    "start_utc": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "unit_amount": {
                        "currency": "x",
                        "tax_codes": ["string"],
                        "gross_value": 0,
                        "net_value": 0,
                    },
                }
            ],
        )
        assert_matches_type(V1AddOrderResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_add_order(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.with_raw_response.add_order(
            access_token="7059D2C25BF64EA681ACAB3A00B859CC-D91BFF2B1E3047A3E0DEC1D57BE1382",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            service_id="d2129910-1da9-4d39-be14-ab3a00c9e70c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1AddOrderResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_add_order(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.with_streaming_response.add_order(
            access_token="7059D2C25BF64EA681ACAB3A00B859CC-D91BFF2B1E3047A3E0DEC1D57BE1382",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            service_id="d2129910-1da9-4d39-be14-ab3a00c9e70c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1AddOrderResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_add_outlet_bill(self, async_client: AsyncPymews) -> None:
        v1 = await async_client.api.connector.v1.add_outlet_bill(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            bills=[
                {
                    "closed_utc": "2017-01-01T00:00:00Z",
                    "items": [
                        {
                            "consumed_utc": parse_datetime("2017-01-01T00:00:00Z"),
                            "name": "Cash payment",
                            "unit_amount": {
                                "currency": "GBP",
                                "tax_codes": ["UK-S"],
                            },
                            "unit_count": 1,
                        },
                        {
                            "consumed_utc": parse_datetime("2017-01-01T00:00:00Z"),
                            "name": "Beer",
                            "unit_amount": {
                                "currency": "GBP",
                                "tax_codes": ["UK-S"],
                            },
                            "unit_count": 10,
                        },
                    ],
                    "number": "1257",
                    "outlet_id": "7700469f-7667-4ebd-a1c0-10380afc9bd0",
                }
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )
        assert_matches_type(V1AddOutletBillResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_add_outlet_bill(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.with_raw_response.add_outlet_bill(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            bills=[
                {
                    "closed_utc": "2017-01-01T00:00:00Z",
                    "items": [
                        {
                            "consumed_utc": parse_datetime("2017-01-01T00:00:00Z"),
                            "name": "Cash payment",
                            "unit_amount": {
                                "currency": "GBP",
                                "tax_codes": ["UK-S"],
                            },
                            "unit_count": 1,
                        },
                        {
                            "consumed_utc": parse_datetime("2017-01-01T00:00:00Z"),
                            "name": "Beer",
                            "unit_amount": {
                                "currency": "GBP",
                                "tax_codes": ["UK-S"],
                            },
                            "unit_count": 10,
                        },
                    ],
                    "number": "1257",
                    "outlet_id": "7700469f-7667-4ebd-a1c0-10380afc9bd0",
                }
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1AddOutletBillResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_add_outlet_bill(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.with_streaming_response.add_outlet_bill(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            bills=[
                {
                    "closed_utc": "2017-01-01T00:00:00Z",
                    "items": [
                        {
                            "consumed_utc": parse_datetime("2017-01-01T00:00:00Z"),
                            "name": "Cash payment",
                            "unit_amount": {
                                "currency": "GBP",
                                "tax_codes": ["UK-S"],
                            },
                            "unit_count": 1,
                        },
                        {
                            "consumed_utc": parse_datetime("2017-01-01T00:00:00Z"),
                            "name": "Beer",
                            "unit_amount": {
                                "currency": "GBP",
                                "tax_codes": ["UK-S"],
                            },
                            "unit_count": 10,
                        },
                    ],
                    "number": "1257",
                    "outlet_id": "7700469f-7667-4ebd-a1c0-10380afc9bd0",
                }
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1AddOutletBillResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_all_source_assignments(self, async_client: AsyncPymews) -> None:
        v1 = await async_client.api.connector.v1.get_all_source_assignments(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )
        assert_matches_type(V1GetAllSourceAssignmentsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_all_source_assignments_with_all_params(self, async_client: AsyncPymews) -> None:
        v1 = await async_client.api.connector.v1.get_all_source_assignments(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            reservation_group_ids=["730d050c-8098-415a-95af-af2500a2de47"],
            updated_utc={
                "end_utc": parse_datetime("2023-02-28T00:00:00Z"),
                "start_utc": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
        )
        assert_matches_type(V1GetAllSourceAssignmentsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_all_source_assignments(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.with_raw_response.get_all_source_assignments(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1GetAllSourceAssignmentsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_all_source_assignments(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.with_streaming_response.get_all_source_assignments(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1GetAllSourceAssignmentsResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_all_source_assignments_2024_09_20(self, async_client: AsyncPymews) -> None:
        v1 = await async_client.api.connector.v1.get_all_source_assignments_2024_09_20(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )
        assert_matches_type(V1GetAllSourceAssignments2024_09_20Response, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_all_source_assignments_2024_09_20_with_all_params(
        self, async_client: AsyncPymews
    ) -> None:
        v1 = await async_client.api.connector.v1.get_all_source_assignments_2024_09_20(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            enterprise_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            reservation_ids=["9b59b50d-bd32-4ce5-add8-09ea0e1300e7"],
        )
        assert_matches_type(V1GetAllSourceAssignments2024_09_20Response, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_all_source_assignments_2024_09_20(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.with_raw_response.get_all_source_assignments_2024_09_20(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1GetAllSourceAssignments2024_09_20Response, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_all_source_assignments_2024_09_20(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.with_streaming_response.get_all_source_assignments_2024_09_20(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1GetAllSourceAssignments2024_09_20Response, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_configuration(self, async_client: AsyncPymews) -> None:
        v1 = await async_client.api.connector.v1.get_configuration(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )
        assert_matches_type(V1GetConfigurationResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_configuration_with_all_params(self, async_client: AsyncPymews) -> None:
        v1 = await async_client.api.connector.v1.get_configuration(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            enterprise_id="851df8c8-90f2-4c4a-8e01-a4fc46b25178",
        )
        assert_matches_type(V1GetConfigurationResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_configuration(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.with_raw_response.get_configuration(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1GetConfigurationResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_configuration(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.with_streaming_response.get_configuration(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1GetConfigurationResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_image_urls(self, async_client: AsyncPymews) -> None:
        v1 = await async_client.api.connector.v1.get_image_urls(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            images=[{"image_id": "57a971a5-a335-48f4-8cd1-595245d1a876"}],
        )
        assert_matches_type(V1GetImageURLsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_image_urls(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.with_raw_response.get_image_urls(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            images=[{"image_id": "57a971a5-a335-48f4-8cd1-595245d1a876"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1GetImageURLsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_image_urls(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.with_streaming_response.get_image_urls(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            images=[{"image_id": "57a971a5-a335-48f4-8cd1-595245d1a876"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1GetImageURLsResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_accounting_categories(self, async_client: AsyncPymews) -> None:
        v1 = await async_client.api.connector.v1.list_accounting_categories(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )
        assert_matches_type(V1ListAccountingCategoriesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_accounting_categories_with_all_params(self, async_client: AsyncPymews) -> None:
        v1 = await async_client.api.connector.v1.list_accounting_categories(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            accounting_category_ids=["0cf7aa90-736f-43e9-a7dc-787704548d86", "0b9560fb-055d-47d3-a6d4-e579c44ca558"],
            activity_states=["Active"],
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            updated_utc={
                "end_utc": parse_datetime("2023-10-31T00:00:00Z"),
                "start_utc": parse_datetime("2023-10-01T00:00:00Z"),
            },
        )
        assert_matches_type(V1ListAccountingCategoriesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_accounting_categories(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.with_raw_response.list_accounting_categories(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1ListAccountingCategoriesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_accounting_categories(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.with_streaming_response.list_accounting_categories(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1ListAccountingCategoriesResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_age_categories(self, async_client: AsyncPymews) -> None:
        v1 = await async_client.api.connector.v1.list_age_categories(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )
        assert_matches_type(V1ListAgeCategoriesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_age_categories_with_all_params(self, async_client: AsyncPymews) -> None:
        v1 = await async_client.api.connector.v1.list_age_categories(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            activity_states=["Active"],
            age_category_ids=["fe568bbd-1ecb-4bb2-bf77-96c3698de20d", "ab58c939-be30-4a60-8f75-ae1600c60c9f"],
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            service_ids=["bd26d8db-86da-4f96-9efc-e5a4654a4a94"],
            updated_utc={
                "end_utc": parse_datetime("2023-10-31T00:00:00Z"),
                "start_utc": parse_datetime("2023-10-01T00:00:00Z"),
            },
        )
        assert_matches_type(V1ListAgeCategoriesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_age_categories(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.with_raw_response.list_age_categories(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1ListAgeCategoriesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_age_categories(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.with_streaming_response.list_age_categories(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1ListAgeCategoriesResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_availability_adjustments(self, async_client: AsyncPymews) -> None:
        v1 = await async_client.api.connector.v1.list_availability_adjustments(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )
        assert_matches_type(V1ListAvailabilityAdjustmentsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_availability_adjustments_with_all_params(self, async_client: AsyncPymews) -> None:
        v1 = await async_client.api.connector.v1.list_availability_adjustments(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            activity_states=["Active", "Deleted"],
            availability_adjustment_ids=[
                "e19297af-373e-4701-b4ea-afae0129bded",
                "7413724a-6c48-46d4-ab3a-afae01280999",
            ],
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            updated_utc={
                "end_utc": parse_datetime("2023-02-20T18:00:10.155Z"),
                "start_utc": parse_datetime("2023-02-18T18:00:10.155Z"),
            },
        )
        assert_matches_type(V1ListAvailabilityAdjustmentsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_availability_adjustments(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.with_raw_response.list_availability_adjustments(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1ListAvailabilityAdjustmentsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_availability_adjustments(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.with_streaming_response.list_availability_adjustments(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1ListAvailabilityAdjustmentsResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_business_segments(self, async_client: AsyncPymews) -> None:
        v1 = await async_client.api.connector.v1.list_business_segments(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )
        assert_matches_type(V1ListBusinessSegmentsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_business_segments_with_all_params(self, async_client: AsyncPymews) -> None:
        v1 = await async_client.api.connector.v1.list_business_segments(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            activity_states=["Active"],
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            ids=["7760b5cb-a666-41bb-9758-76bf5d1df399", "54ec08b6-e6fc-48e9-b8ae-02943e0ac693"],
            service_ids=["bd26d8db-86da-4f96-9efc-e5a4654a4a94", "8c1bd738-a505-4b29-aa71-9ecc2982b843"],
            updated_utc={
                "end_utc": parse_datetime("2023-10-31T00:00:00Z"),
                "start_utc": parse_datetime("2023-10-01T00:00:00Z"),
            },
        )
        assert_matches_type(V1ListBusinessSegmentsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_business_segments(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.with_raw_response.list_business_segments(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1ListBusinessSegmentsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_business_segments(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.with_streaming_response.list_business_segments(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1ListBusinessSegmentsResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_cashier_transactions(self, async_client: AsyncPymews) -> None:
        v1 = await async_client.api.connector.v1.list_cashier_transactions(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )
        assert_matches_type(V1ListCashierTransactionsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_cashier_transactions_with_all_params(self, async_client: AsyncPymews) -> None:
        v1 = await async_client.api.connector.v1.list_cashier_transactions(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            cashier_transaction_ids=["177740c3-fec9-4338-a224-a3b03a35b3e1"],
            created_utc={
                "end_utc": parse_datetime("2020-01-10T00:00:00Z"),
                "start_utc": parse_datetime("2020-01-05T00:00:00Z"),
            },
            end_utc="EndUtc",
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            start_utc="StartUtc",
        )
        assert_matches_type(V1ListCashierTransactionsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_cashier_transactions(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.with_raw_response.list_cashier_transactions(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1ListCashierTransactionsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_cashier_transactions(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.with_streaming_response.list_cashier_transactions(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1ListCashierTransactionsResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_cashiers(self, async_client: AsyncPymews) -> None:
        v1 = await async_client.api.connector.v1.list_cashiers(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )
        assert_matches_type(V1ListCashiersResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_cashiers_with_all_params(self, async_client: AsyncPymews) -> None:
        v1 = await async_client.api.connector.v1.list_cashiers(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            activity_states=["Active"],
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            ids=["9a36e3fa-2299-474b-a8a2-5ea4da317abc"],
            updated_utc={
                "end_utc": parse_datetime("2023-10-31T00:00:00Z"),
                "start_utc": parse_datetime("2023-10-01T00:00:00Z"),
            },
        )
        assert_matches_type(V1ListCashiersResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_cashiers(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.with_raw_response.list_cashiers(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1ListCashiersResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_cashiers(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.with_streaming_response.list_cashiers(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1ListCashiersResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_companionships(self, async_client: AsyncPymews) -> None:
        v1 = await async_client.api.connector.v1.list_companionships(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            extent={},
            limitation={"count": 10},
        )
        assert_matches_type(V1ListCompanionshipsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_companionships_with_all_params(self, async_client: AsyncPymews) -> None:
        v1 = await async_client.api.connector.v1.list_companionships(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            extent={
                "customers": True,
                "reservation_groups": True,
                "reservations": True,
            },
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            companionship_ids=["72d4b117-1f84-44a3-1f84-8b2c0635ac60"],
            customer_ids=["35d4b117-4e60-44a3-9580-c582117eff98"],
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            reservation_group_ids=["c704dff3-7811-4af7-a3a0-7b2b0635ac59"],
            reservation_ids=["bfee2c44-1f84-4326-a862-5289598f6e2d"],
            updated_utc={
                "end_utc": parse_datetime("2020-02-10T00:00:00Z"),
                "start_utc": parse_datetime("2020-02-05T00:00:00Z"),
            },
        )
        assert_matches_type(V1ListCompanionshipsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_companionships(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.with_raw_response.list_companionships(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            extent={},
            limitation={"count": 10},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1ListCompanionshipsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_companionships(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.with_streaming_response.list_companionships(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            extent={},
            limitation={"count": 10},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1ListCompanionshipsResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_counters(self, async_client: AsyncPymews) -> None:
        v1 = await async_client.api.connector.v1.list_counters(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )
        assert_matches_type(V1ListCountersResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_counters_with_all_params(self, async_client: AsyncPymews) -> None:
        v1 = await async_client.api.connector.v1.list_counters(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            counter_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            type="Counter",
            updated_utc={
                "end_utc": parse_datetime("2023-10-31T00:00:00Z"),
                "start_utc": parse_datetime("2023-10-01T00:00:00Z"),
            },
        )
        assert_matches_type(V1ListCountersResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_counters(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.with_raw_response.list_counters(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1ListCountersResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_counters(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.with_streaming_response.list_counters(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1ListCountersResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_countries(self, async_client: AsyncPymews) -> None:
        v1 = await async_client.api.connector.v1.list_countries(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )
        assert_matches_type(V1ListCountriesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_countries(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.with_raw_response.list_countries(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1ListCountriesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_countries(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.with_streaming_response.list_countries(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1ListCountriesResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_currencies(self, async_client: AsyncPymews) -> None:
        v1 = await async_client.api.connector.v1.list_currencies(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )
        assert_matches_type(V1ListCurrenciesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_currencies(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.with_raw_response.list_currencies(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1ListCurrenciesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_currencies(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.with_streaming_response.list_currencies(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1ListCurrenciesResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_departments(self, async_client: AsyncPymews) -> None:
        v1 = await async_client.api.connector.v1.list_departments(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )
        assert_matches_type(V1ListDepartmentsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_departments_with_all_params(self, async_client: AsyncPymews) -> None:
        v1 = await async_client.api.connector.v1.list_departments(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            department_ids=["98776d06-60e4-495f-82f1-95ab2f644d63", "915fbb82-de35-48a0-9e9b-f4a7eac711bb"],
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            updated_utc={
                "end_utc": parse_datetime("2023-10-31T00:00:00Z"),
                "start_utc": parse_datetime("2023-10-01T00:00:00Z"),
            },
        )
        assert_matches_type(V1ListDepartmentsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_departments(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.with_raw_response.list_departments(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1ListDepartmentsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_departments(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.with_streaming_response.list_departments(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1ListDepartmentsResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_devices(self, async_client: AsyncPymews) -> None:
        v1 = await async_client.api.connector.v1.list_devices(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )
        assert_matches_type(V1ListDevicesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_devices(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.with_raw_response.list_devices(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1ListDevicesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_devices(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.with_streaming_response.list_devices(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1ListDevicesResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_enterprises(self, async_client: AsyncPymews) -> None:
        v1 = await async_client.api.connector.v1.list_enterprises(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 100},
        )
        assert_matches_type(V1ListEnterprisesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_enterprises_with_all_params(self, async_client: AsyncPymews) -> None:
        v1 = await async_client.api.connector.v1.list_enterprises(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 100,
                "cursor": "4d0201db-36f5-428b-8d11-4f0a65e960cc",
            },
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            external_identifiers=["Enterprise2023"],
            linked_utc={
                "end_utc": parse_datetime("2023-06-06T00:00:00Z"),
                "start_utc": parse_datetime("2023-06-01T00:00:00Z"),
            },
            updated_utc={
                "end_utc": parse_datetime("2023-10-31T00:00:00Z"),
                "start_utc": parse_datetime("2023-10-01T00:00:00Z"),
            },
        )
        assert_matches_type(V1ListEnterprisesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_enterprises(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.with_raw_response.list_enterprises(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 100},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1ListEnterprisesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_enterprises(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.with_streaming_response.list_enterprises(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 100},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1ListEnterprisesResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_exchange_rates(self, async_client: AsyncPymews) -> None:
        v1 = await async_client.api.connector.v1.list_exchange_rates(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )
        assert_matches_type(V1ListExchangeRatesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_exchange_rates_with_all_params(self, async_client: AsyncPymews) -> None:
        v1 = await async_client.api.connector.v1.list_exchange_rates(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            enterprise_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(V1ListExchangeRatesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_exchange_rates(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.with_raw_response.list_exchange_rates(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1ListExchangeRatesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_exchange_rates(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.with_streaming_response.list_exchange_rates(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1ListExchangeRatesResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_ledger_balances(self, async_client: AsyncPymews) -> None:
        v1 = await async_client.api.connector.v1.list_ledger_balances(
            access_token="x",
            client="x",
            client_token="x",
            date={
                "end": parse_date("2019-12-27"),
                "start": parse_date("2019-12-27"),
            },
            ledger_types=["Revenue"],
            limitation={"count": 0},
        )
        assert_matches_type(V1ListLedgerBalancesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_ledger_balances_with_all_params(self, async_client: AsyncPymews) -> None:
        v1 = await async_client.api.connector.v1.list_ledger_balances(
            access_token="x",
            client="x",
            client_token="x",
            date={
                "end": parse_date("2019-12-27"),
                "start": parse_date("2019-12-27"),
            },
            ledger_types=["Revenue"],
            limitation={
                "count": 0,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            enterprise_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(V1ListLedgerBalancesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_ledger_balances(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.with_raw_response.list_ledger_balances(
            access_token="x",
            client="x",
            client_token="x",
            date={
                "end": parse_date("2019-12-27"),
                "start": parse_date("2019-12-27"),
            },
            ledger_types=["Revenue"],
            limitation={"count": 0},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1ListLedgerBalancesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_ledger_balances(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.with_streaming_response.list_ledger_balances(
            access_token="x",
            client="x",
            client_token="x",
            date={
                "end": parse_date("2019-12-27"),
                "start": parse_date("2019-12-27"),
            },
            ledger_types=["Revenue"],
            limitation={"count": 0},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1ListLedgerBalancesResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_outlet_items(self, async_client: AsyncPymews) -> None:
        v1 = await async_client.api.connector.v1.list_outlet_items(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 100},
        )
        assert_matches_type(V1ListOutletItemsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_outlet_items_with_all_params(self, async_client: AsyncPymews) -> None:
        v1 = await async_client.api.connector.v1.list_outlet_items(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 100,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            closed_utc={
                "end_utc": parse_datetime("2020-01-10T00:00:00Z"),
                "start_utc": parse_datetime("2020-01-05T00:00:00Z"),
            },
            consumed_utc={
                "end_utc": parse_datetime("2020-01-10T00:00:00Z"),
                "start_utc": parse_datetime("2020-01-05T00:00:00Z"),
            },
            currency="EUR",
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            updated_utc={
                "end_utc": parse_datetime("2020-01-10T00:00:00Z"),
                "start_utc": parse_datetime("2020-01-05T00:00:00Z"),
            },
        )
        assert_matches_type(V1ListOutletItemsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_outlet_items(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.with_raw_response.list_outlet_items(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 100},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1ListOutletItemsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_outlet_items(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.with_streaming_response.list_outlet_items(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 100},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1ListOutletItemsResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_outlets(self, async_client: AsyncPymews) -> None:
        v1 = await async_client.api.connector.v1.list_outlets(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 100},
        )
        assert_matches_type(V1ListOutletsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_outlets_with_all_params(self, async_client: AsyncPymews) -> None:
        v1 = await async_client.api.connector.v1.list_outlets(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 100,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            outlet_ids=["7700469f-7667-4ebd-a1c0-10380afc9bd0", "2accff7b-feea-436a-9670-afa9bdb8c8d2"],
            updated_utc={
                "end_utc": parse_datetime("2023-10-31T00:00:00Z"),
                "start_utc": parse_datetime("2023-10-01T00:00:00Z"),
            },
        )
        assert_matches_type(V1ListOutletsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_outlets(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.with_raw_response.list_outlets(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 100},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1ListOutletsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_outlets(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.with_streaming_response.list_outlets(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 100},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1ListOutletsResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_preauthorizations_by_customers(self, async_client: AsyncPymews) -> None:
        v1 = await async_client.api.connector.v1.list_preauthorizations_by_customers(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_ids=["e98995b0-140a-4208-bbeb-b77f2c43d6ee"],
        )
        assert_matches_type(V1ListPreauthorizationsByCustomersResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_preauthorizations_by_customers(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.with_raw_response.list_preauthorizations_by_customers(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_ids=["e98995b0-140a-4208-bbeb-b77f2c43d6ee"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1ListPreauthorizationsByCustomersResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_preauthorizations_by_customers(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.with_streaming_response.list_preauthorizations_by_customers(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_ids=["e98995b0-140a-4208-bbeb-b77f2c43d6ee"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1ListPreauthorizationsByCustomersResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_product_categories(self, async_client: AsyncPymews) -> None:
        v1 = await async_client.api.connector.v1.list_product_categories(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )
        assert_matches_type(V1ListProductCategoriesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_product_categories_with_all_params(self, async_client: AsyncPymews) -> None:
        v1 = await async_client.api.connector.v1.list_product_categories(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            product_category_ids=["5228623e-b2cf-4f9f-8bd6-71cbe3ec5e6f", "63bc87d3-edf5-4d06-a601-6052a2ad709d"],
            service_ids=["9b3a6c54-63aa-4383-b50e-b0030078184b", "c0f71466-6c0b-4993-88ac-1794f6b7e958"],
            updated_utc={
                "end_utc": parse_datetime("2023-05-10T00:00:00Z"),
                "start_utc": parse_datetime("2023-05-05T00:00:00Z"),
            },
        )
        assert_matches_type(V1ListProductCategoriesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_product_categories(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.with_raw_response.list_product_categories(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1ListProductCategoriesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_product_categories(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.with_streaming_response.list_product_categories(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1ListProductCategoriesResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_product_service_orders(self, async_client: AsyncPymews) -> None:
        v1 = await async_client.api.connector.v1.list_product_service_orders(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            service_ids=["ae8da28c-e8a4-4141-9df0-8c998976c691", "6b02d015-47ac-4c41-8e9f-5b4db61d4284"],
        )
        assert_matches_type(V1ListProductServiceOrdersResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_product_service_orders_with_all_params(self, async_client: AsyncPymews) -> None:
        v1 = await async_client.api.connector.v1.list_product_service_orders(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 10,
                "cursor": "819e3435-7d5e-441f-bc68-76d89c69b8f5",
            },
            service_ids=["ae8da28c-e8a4-4141-9df0-8c998976c691", "6b02d015-47ac-4c41-8e9f-5b4db61d4284"],
            account_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            enterprise_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            linked_reservation_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            product_service_order_ids=["9b59b50d-bd32-4ce5-add8-09ea0e1300e7"],
            states=["Inquired"],
            updated_utc={
                "end_utc": parse_datetime("2023-05-05T00:00:00Z"),
                "start_utc": parse_datetime("2023-04-01T00:00:00Z"),
            },
        )
        assert_matches_type(V1ListProductServiceOrdersResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_product_service_orders(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.with_raw_response.list_product_service_orders(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            service_ids=["ae8da28c-e8a4-4141-9df0-8c998976c691", "6b02d015-47ac-4c41-8e9f-5b4db61d4284"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1ListProductServiceOrdersResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_product_service_orders(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.with_streaming_response.list_product_service_orders(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            service_ids=["ae8da28c-e8a4-4141-9df0-8c998976c691", "6b02d015-47ac-4c41-8e9f-5b4db61d4284"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1ListProductServiceOrdersResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_rate_groups(self, async_client: AsyncPymews) -> None:
        v1 = await async_client.api.connector.v1.list_rate_groups(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 1000},
        )
        assert_matches_type(V1ListRateGroupsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_rate_groups_with_all_params(self, async_client: AsyncPymews) -> None:
        v1 = await async_client.api.connector.v1.list_rate_groups(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 1000,
                "cursor": "e7f26210-10e7-462e-9da8-ae8300be8ab7",
            },
            activity_states=["Active"],
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            external_identifiers=["RG-001"],
            rate_group_ids=["6b3f718a-b537-45b0-a8ee-d30897723834"],
            service_ids=["bd26d8db-86da-4f96-9efc-e5a4654a4a94"],
            updated_utc={
                "end_utc": parse_datetime("2024-02-27T11:48:57Z"),
                "start_utc": parse_datetime("2024-01-27T11:48:57Z"),
            },
        )
        assert_matches_type(V1ListRateGroupsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_rate_groups(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.with_raw_response.list_rate_groups(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 1000},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1ListRateGroupsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_rate_groups(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.with_streaming_response.list_rate_groups(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 1000},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1ListRateGroupsResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_reservation_groups(self, async_client: AsyncPymews) -> None:
        v1 = await async_client.api.connector.v1.list_reservation_groups(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 100},
        )
        assert_matches_type(V1ListReservationGroupsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_reservation_groups_with_all_params(self, async_client: AsyncPymews) -> None:
        v1 = await async_client.api.connector.v1.list_reservation_groups(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 100,
                "cursor": "e7f26210-10e7-462e-9da8-ae8300be8ab7",
            },
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            reservation_group_ids=["fe795f96-0b64-445b-89ed-c032563f2bac"],
            updated_utc={
                "end_utc": parse_datetime("2023-04-27T11:48:57Z"),
                "start_utc": parse_datetime("2023-04-27T11:48:57Z"),
            },
        )
        assert_matches_type(V1ListReservationGroupsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_reservation_groups(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.with_raw_response.list_reservation_groups(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 100},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1ListReservationGroupsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_reservation_groups(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.with_streaming_response.list_reservation_groups(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 100},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1ListReservationGroupsResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_resource_categories(self, async_client: AsyncPymews) -> None:
        v1 = await async_client.api.connector.v1.list_resource_categories(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            service_ids=["9b3a6c54-63aa-4383-b50e-b0030078184b", "c0f71466-6c0b-4993-88ac-1794f6b7e958"],
        )
        assert_matches_type(V1ListResourceCategoriesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_resource_categories_with_all_params(self, async_client: AsyncPymews) -> None:
        v1 = await async_client.api.connector.v1.list_resource_categories(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            service_ids=["9b3a6c54-63aa-4383-b50e-b0030078184b", "c0f71466-6c0b-4993-88ac-1794f6b7e958"],
            activity_states=["Active"],
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            resource_category_ids=["5c0804f9-d03a-4b13-a57d-b00300781a41", "47d6b462-35ec-467e-a565-b00300781a41"],
            updated_utc={
                "end_utc": parse_datetime("2023-05-10T00:00:00Z"),
                "start_utc": parse_datetime("2023-05-05T00:00:00Z"),
            },
        )
        assert_matches_type(V1ListResourceCategoriesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_resource_categories(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.with_raw_response.list_resource_categories(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            service_ids=["9b3a6c54-63aa-4383-b50e-b0030078184b", "c0f71466-6c0b-4993-88ac-1794f6b7e958"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1ListResourceCategoriesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_resource_categories(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.with_streaming_response.list_resource_categories(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            service_ids=["9b3a6c54-63aa-4383-b50e-b0030078184b", "c0f71466-6c0b-4993-88ac-1794f6b7e958"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1ListResourceCategoriesResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_resource_category_assignments(self, async_client: AsyncPymews) -> None:
        v1 = await async_client.api.connector.v1.list_resource_category_assignments(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            resource_category_ids=["5c0804f9-d03a-4b13-a57d-b00300781a41", "47d6b462-35ec-467e-a565-b00300781a41"],
        )
        assert_matches_type(V1ListResourceCategoryAssignmentsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_resource_category_assignments_with_all_params(self, async_client: AsyncPymews) -> None:
        v1 = await async_client.api.connector.v1.list_resource_category_assignments(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 10,
                "cursor": "e7f26210-10e7-462e-9da8-ae8300be8ab7",
            },
            resource_category_ids=["5c0804f9-d03a-4b13-a57d-b00300781a41", "47d6b462-35ec-467e-a565-b00300781a41"],
            activity_states=["Active"],
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            resource_category_assignment_ids=[
                "fb69fc51-c4e9-4ef6-874a-24bcfe74a894",
                "28704948-77df-4bb4-8f39-f8380dc8a914",
            ],
            resource_ids=["5ee074b1-6c86-48e8-915f-c7aa4702086f", "c32386aa-1cd2-414a-a823-489325842fbe"],
            updated_utc={
                "end_utc": parse_datetime("2023-11-30T00:00:00Z"),
                "start_utc": parse_datetime("2023-11-01T00:00:00Z"),
            },
        )
        assert_matches_type(V1ListResourceCategoryAssignmentsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_resource_category_assignments(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.with_raw_response.list_resource_category_assignments(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            resource_category_ids=["5c0804f9-d03a-4b13-a57d-b00300781a41", "47d6b462-35ec-467e-a565-b00300781a41"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1ListResourceCategoryAssignmentsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_resource_category_assignments(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.with_streaming_response.list_resource_category_assignments(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            resource_category_ids=["5c0804f9-d03a-4b13-a57d-b00300781a41", "47d6b462-35ec-467e-a565-b00300781a41"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1ListResourceCategoryAssignmentsResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_resource_category_image_assignments(self, async_client: AsyncPymews) -> None:
        v1 = await async_client.api.connector.v1.list_resource_category_image_assignments(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            resource_category_ids=["5c0804f9-d03a-4b13-a57d-b00300781a41", "47d6b462-35ec-467e-a565-b00300781a41"],
        )
        assert_matches_type(V1ListResourceCategoryImageAssignmentsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_resource_category_image_assignments_with_all_params(
        self, async_client: AsyncPymews
    ) -> None:
        v1 = await async_client.api.connector.v1.list_resource_category_image_assignments(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            resource_category_ids=["5c0804f9-d03a-4b13-a57d-b00300781a41", "47d6b462-35ec-467e-a565-b00300781a41"],
            activity_states=["Active"],
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            resource_category_image_assignment_ids=[
                "edb5f556-7afb-4650-8d4e-8c0a6fff784d",
                "9d18f5fb-cce5-4e70-9561-f7804262344b",
            ],
            updated_utc={
                "end_utc": parse_datetime("2023-11-30T00:00:00Z"),
                "start_utc": parse_datetime("2023-11-01T00:00:00Z"),
            },
        )
        assert_matches_type(V1ListResourceCategoryImageAssignmentsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_resource_category_image_assignments(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.with_raw_response.list_resource_category_image_assignments(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            resource_category_ids=["5c0804f9-d03a-4b13-a57d-b00300781a41", "47d6b462-35ec-467e-a565-b00300781a41"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1ListResourceCategoryImageAssignmentsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_resource_category_image_assignments(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.with_streaming_response.list_resource_category_image_assignments(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            resource_category_ids=["5c0804f9-d03a-4b13-a57d-b00300781a41", "47d6b462-35ec-467e-a565-b00300781a41"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1ListResourceCategoryImageAssignmentsResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_resource_feature_assignments(self, async_client: AsyncPymews) -> None:
        v1 = await async_client.api.connector.v1.list_resource_feature_assignments(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            resource_feature_ids=["a693dd8c-21fe-4dae-b450-ea3bd9ab3bb0"],
        )
        assert_matches_type(V1ListResourceFeatureAssignmentsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_resource_feature_assignments_with_all_params(self, async_client: AsyncPymews) -> None:
        v1 = await async_client.api.connector.v1.list_resource_feature_assignments(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            resource_feature_ids=["a693dd8c-21fe-4dae-b450-ea3bd9ab3bb0"],
            activity_states=["Active"],
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            resource_feature_assignment_ids=["ca2b5bf9-24f5-4faa-95ef-b65d38598b08"],
            updated_utc={
                "end_utc": parse_datetime("2023-11-30T00:00:00Z"),
                "start_utc": parse_datetime("2023-11-01T00:00:00Z"),
            },
        )
        assert_matches_type(V1ListResourceFeatureAssignmentsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_resource_feature_assignments(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.with_raw_response.list_resource_feature_assignments(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            resource_feature_ids=["a693dd8c-21fe-4dae-b450-ea3bd9ab3bb0"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1ListResourceFeatureAssignmentsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_resource_feature_assignments(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.with_streaming_response.list_resource_feature_assignments(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            resource_feature_ids=["a693dd8c-21fe-4dae-b450-ea3bd9ab3bb0"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1ListResourceFeatureAssignmentsResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_resource_features(self, async_client: AsyncPymews) -> None:
        v1 = await async_client.api.connector.v1.list_resource_features(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            service_ids=["24e2ead5-65a8-4ed9-8286-abdb00f08a1f"],
        )
        assert_matches_type(V1ListResourceFeaturesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_resource_features_with_all_params(self, async_client: AsyncPymews) -> None:
        v1 = await async_client.api.connector.v1.list_resource_features(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            service_ids=["24e2ead5-65a8-4ed9-8286-abdb00f08a1f"],
            activity_states=["Active"],
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            resource_feature_ids=["3d5201ad-4a7b-4cbe-9c22-03dd79c28443"],
            updated_utc={
                "end_utc": parse_datetime("2023-11-30T00:00:00Z"),
                "start_utc": parse_datetime("2023-11-01T00:00:00Z"),
            },
        )
        assert_matches_type(V1ListResourceFeaturesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_resource_features(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.with_raw_response.list_resource_features(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            service_ids=["24e2ead5-65a8-4ed9-8286-abdb00f08a1f"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1ListResourceFeaturesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_resource_features(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.with_streaming_response.list_resource_features(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            service_ids=["24e2ead5-65a8-4ed9-8286-abdb00f08a1f"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1ListResourceFeaturesResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_rules(self, async_client: AsyncPymews) -> None:
        v1 = await async_client.api.connector.v1.list_rules(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            extent={},
            limitation={"count": 10},
            service_ids=["bd26d8db-86da-4f96-9efc-e5a4654a4a94"],
        )
        assert_matches_type(V1ListRulesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_rules_with_all_params(self, async_client: AsyncPymews) -> None:
        v1 = await async_client.api.connector.v1.list_rules(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            extent={
                "business_segments": True,
                "rate_groups": True,
                "rates": True,
                "resource_categories": True,
                "rule_actions": True,
            },
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            service_ids=["bd26d8db-86da-4f96-9efc-e5a4654a4a94"],
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            updated_utc={
                "end_utc": parse_datetime("2023-10-31T00:00:00Z"),
                "start_utc": parse_datetime("2023-10-01T00:00:00Z"),
            },
        )
        assert_matches_type(V1ListRulesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_rules(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.with_raw_response.list_rules(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            extent={},
            limitation={"count": 10},
            service_ids=["bd26d8db-86da-4f96-9efc-e5a4654a4a94"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1ListRulesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_rules(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.with_streaming_response.list_rules(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            extent={},
            limitation={"count": 10},
            service_ids=["bd26d8db-86da-4f96-9efc-e5a4654a4a94"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1ListRulesResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_sources(self, async_client: AsyncPymews) -> None:
        v1 = await async_client.api.connector.v1.list_sources(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )
        assert_matches_type(V1ListSourcesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_sources_with_all_params(self, async_client: AsyncPymews) -> None:
        v1 = await async_client.api.connector.v1.list_sources(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 10,
                "cursor": None,
            },
            source_ids=[
                "bbe29c21-401a-4746-b97d-af1f00e1bb8b",
                "22e42a59-b321-43f8-a5d1-af1f00e1bb8b",
                "b5a55d41-bbc5-48d0-a01b-af1f00e1bb8b",
            ],
            updated_utc={
                "end_utc": parse_datetime("2023-01-10T00:00:00Z"),
                "start_utc": parse_datetime("2023-01-05T00:00:00Z"),
            },
        )
        assert_matches_type(V1ListSourcesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_sources(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.with_raw_response.list_sources(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1ListSourcesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_sources(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.with_streaming_response.list_sources(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1ListSourcesResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_tax_environments(self, async_client: AsyncPymews) -> None:
        v1 = await async_client.api.connector.v1.list_tax_environments(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )
        assert_matches_type(V1ListTaxEnvironmentsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_tax_environments(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.with_raw_response.list_tax_environments(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1ListTaxEnvironmentsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_tax_environments(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.with_streaming_response.list_tax_environments(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1ListTaxEnvironmentsResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_taxations(self, async_client: AsyncPymews) -> None:
        v1 = await async_client.api.connector.v1.list_taxations(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )
        assert_matches_type(V1ListTaxationsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_taxations(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.with_raw_response.list_taxations(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1ListTaxationsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_taxations(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.with_streaming_response.list_taxations(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1ListTaxationsResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True
