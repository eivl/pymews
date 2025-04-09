# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pymews import Pymews, AsyncPymews
from tests.utils import assert_matches_type
from pymews._utils import parse_datetime
from pymews.types.api.connector.v1 import (
    AvailabilityBlockAddResult,
    AvailabilityBlockListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAvailabilityBlocks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Pymews) -> None:
        availability_block = client.api.connector.v1.availability_blocks.update(
            access_token="x",
            availability_blocks=[{}, {}],
            client="x",
            client_token="x",
        )
        assert_matches_type(AvailabilityBlockAddResult, availability_block, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Pymews) -> None:
        availability_block = client.api.connector.v1.availability_blocks.update(
            access_token="x",
            availability_blocks=[
                {
                    "availability_block_id": "5ee074b1-6c86-48e8-915f-c7aa4702086f",
                    "booker_id": {"value": "ebd507c5-6bfd-4ca9-96aa-ffed6fa94f72"},
                    "budget": {
                        "value": {
                            "currency": "USD",
                            "net": 0,
                            "tax": 0,
                            "tax_rate": 0,
                            "value": 48,
                        }
                    },
                    "cancellation_reason": {"value": "Value"},
                    "cancellation_reason_detail": {"value": "Value"},
                    "company_id": {"value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                    "external_identifier": {"value": "Block-0001"},
                    "first_time_unit_start_utc": {"value": "2021-07-05T00:00:00Z"},
                    "last_time_unit_start_utc": {"value": "2021-07-15T00:00:00Z"},
                    "name": {"value": "Mr. Smith's block"},
                    "notes": {"value": "Have a nice stay"},
                    "quote_id": {"value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                    "released_utc": {"value": "2021-07-01T00:00:00Z"},
                    "release_strategy": {"value": "FixedRelease"},
                    "reservation_purpose": {"value": "Leisure"},
                    "rolling_release_offset": {"value": "Value"},
                    "state": {"value": "Confirmed"},
                    "travel_agency_id": {"value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                },
                {
                    "availability_block_id": "c32386aa-1cd2-414a-a823-489325842fbe",
                    "booker_id": {"value": "ebd507c5-6bfd-4ca9-96aa-ffed6fa94f72"},
                    "budget": {
                        "value": {
                            "currency": "USD",
                            "net": 0,
                            "tax": 0,
                            "tax_rate": 0,
                            "value": 48,
                        }
                    },
                    "cancellation_reason": {"value": "Value"},
                    "cancellation_reason_detail": {"value": "Value"},
                    "company_id": {"value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                    "external_identifier": {"value": "Block-0002"},
                    "first_time_unit_start_utc": {"value": "2022-07-05T00:00:00Z"},
                    "last_time_unit_start_utc": {"value": "2022-07-15T00:00:00Z"},
                    "name": {"value": "Rolling release block"},
                    "notes": {"value": "Have a nice stay"},
                    "quote_id": {"value": "67eaf3c8-81e0-4ffb-b5f2-2b61803feb9c"},
                    "released_utc": {"value": "2021-07-01T00:00:00Z"},
                    "release_strategy": {"value": "RollingRelease"},
                    "reservation_purpose": {"value": "Leisure"},
                    "rolling_release_offset": {"value": "P-3DT4H"},
                    "state": {"value": "Confirmed"},
                    "travel_agency_id": {"value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                },
            ],
            client="x",
            client_token="x",
            enterprise_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AvailabilityBlockAddResult, availability_block, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Pymews) -> None:
        response = client.api.connector.v1.availability_blocks.with_raw_response.update(
            access_token="x",
            availability_blocks=[{}, {}],
            client="x",
            client_token="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        availability_block = response.parse()
        assert_matches_type(AvailabilityBlockAddResult, availability_block, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Pymews) -> None:
        with client.api.connector.v1.availability_blocks.with_streaming_response.update(
            access_token="x",
            availability_blocks=[{}, {}],
            client="x",
            client_token="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            availability_block = response.parse()
            assert_matches_type(AvailabilityBlockAddResult, availability_block, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Pymews) -> None:
        availability_block = client.api.connector.v1.availability_blocks.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            extent={},
            limitation={"count": 100},
        )
        assert_matches_type(AvailabilityBlockListResponse, availability_block, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Pymews) -> None:
        availability_block = client.api.connector.v1.availability_blocks.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            extent={
                "adjustments": True,
                "availability_blocks": True,
                "rates": False,
                "service_orders": False,
            },
            limitation={
                "count": 100,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            activity_states=["Active"],
            availability_block_ids=["5ee074b1-6c86-48e8-915f-c7aa4702086f"],
            colliding_utc={
                "end_utc": parse_datetime("2020-11-05T00:00:00Z"),
                "start_utc": parse_datetime("2020-11-04T00:00:00Z"),
            },
            created_utc={
                "end_utc": parse_datetime("2020-11-05T00:00:00Z"),
                "start_utc": parse_datetime("2020-11-04T00:00:00Z"),
            },
            enterprise_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            external_identifiers=["Block-0001"],
            released_utc={
                "end_utc": parse_datetime("2020-11-05T00:00:00Z"),
                "start_utc": parse_datetime("2020-11-04T00:00:00Z"),
            },
            service_ids=["bd26d8db-86da-4f96-9efc-e5a4654a4a94"],
            states=["Confirmed"],
            updated_utc={
                "end_utc": parse_datetime("2020-11-05T00:00:00Z"),
                "start_utc": parse_datetime("2020-11-04T00:00:00Z"),
            },
        )
        assert_matches_type(AvailabilityBlockListResponse, availability_block, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Pymews) -> None:
        response = client.api.connector.v1.availability_blocks.with_raw_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            extent={},
            limitation={"count": 100},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        availability_block = response.parse()
        assert_matches_type(AvailabilityBlockListResponse, availability_block, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Pymews) -> None:
        with client.api.connector.v1.availability_blocks.with_streaming_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            extent={},
            limitation={"count": 100},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            availability_block = response.parse()
            assert_matches_type(AvailabilityBlockListResponse, availability_block, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Pymews) -> None:
        availability_block = client.api.connector.v1.availability_blocks.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            availability_block_ids=["5ee074b1-6c86-48e8-915f-c7aa4702086f", "c32386aa-1cd2-414a-a823-489325842fbe"],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )
        assert_matches_type(object, availability_block, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_delete_with_all_params(self, client: Pymews) -> None:
        availability_block = client.api.connector.v1.availability_blocks.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            availability_block_ids=["5ee074b1-6c86-48e8-915f-c7aa4702086f", "c32386aa-1cd2-414a-a823-489325842fbe"],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            enterprise_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )
        assert_matches_type(object, availability_block, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Pymews) -> None:
        response = client.api.connector.v1.availability_blocks.with_raw_response.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            availability_block_ids=["5ee074b1-6c86-48e8-915f-c7aa4702086f", "c32386aa-1cd2-414a-a823-489325842fbe"],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        availability_block = response.parse()
        assert_matches_type(object, availability_block, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Pymews) -> None:
        with client.api.connector.v1.availability_blocks.with_streaming_response.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            availability_block_ids=["5ee074b1-6c86-48e8-915f-c7aa4702086f", "c32386aa-1cd2-414a-a823-489325842fbe"],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            availability_block = response.parse()
            assert_matches_type(object, availability_block, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_add(self, client: Pymews) -> None:
        availability_block = client.api.connector.v1.availability_blocks.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            availability_blocks=[
                {
                    "first_time_unit_start_utc": "2020-11-05T00:00:00Z",
                    "last_time_unit_start_utc": "2020-11-06T00:00:00Z",
                    "rate_id": "ed4b660b-19d0-434b-9360-a4de2ea42eda",
                    "service_id": "bd26d8db-86da-4f96-9efc-e5a4654a4a94",
                    "state": "Confirmed",
                },
                {
                    "first_time_unit_start_utc": "2021-11-05T00:00:00Z",
                    "last_time_unit_start_utc": "2021-11-06T00:00:00Z",
                    "rate_id": "ed4b660b-19d0-434b-9360-a4de2ea42eda",
                    "service_id": "bd26d8db-86da-4f96-9efc-e5a4654a4a94",
                    "state": "Confirmed",
                },
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )
        assert_matches_type(AvailabilityBlockAddResult, availability_block, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_add_with_all_params(self, client: Pymews) -> None:
        availability_block = client.api.connector.v1.availability_blocks.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            availability_blocks=[
                {
                    "first_time_unit_start_utc": "2020-11-05T00:00:00Z",
                    "last_time_unit_start_utc": "2020-11-06T00:00:00Z",
                    "rate_id": "ed4b660b-19d0-434b-9360-a4de2ea42eda",
                    "service_id": "bd26d8db-86da-4f96-9efc-e5a4654a4a94",
                    "state": "Confirmed",
                    "booker_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "budget": {
                        "currency": "USD",
                        "net": 0,
                        "tax": 0,
                        "tax_rate": 0,
                        "value": 48,
                    },
                    "company_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "external_identifier": "Block-0001",
                    "name": "Mr. Smith's block",
                    "notes": "Notes",
                    "quote_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "released_utc": parse_datetime("2020-11-04T00:00:00Z"),
                    "reservation_purpose": "Leisure",
                    "rolling_release_offset": "RollingReleaseOffset",
                    "travel_agency_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "voucher_code": "VoucherCode",
                },
                {
                    "first_time_unit_start_utc": "2021-11-05T00:00:00Z",
                    "last_time_unit_start_utc": "2021-11-06T00:00:00Z",
                    "rate_id": "ed4b660b-19d0-434b-9360-a4de2ea42eda",
                    "service_id": "bd26d8db-86da-4f96-9efc-e5a4654a4a94",
                    "state": "Confirmed",
                    "booker_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "budget": {
                        "currency": "USD",
                        "net": 0,
                        "tax": 0,
                        "tax_rate": 0,
                        "value": 48,
                    },
                    "company_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "external_identifier": "Block-0002",
                    "name": "Rolling release block",
                    "notes": "Notes",
                    "quote_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "released_utc": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "reservation_purpose": "Leisure",
                    "rolling_release_offset": "RollingReleaseOffset",
                    "travel_agency_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "voucher_code": "VoucherCode",
                },
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            enterprise_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )
        assert_matches_type(AvailabilityBlockAddResult, availability_block, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_add(self, client: Pymews) -> None:
        response = client.api.connector.v1.availability_blocks.with_raw_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            availability_blocks=[
                {
                    "first_time_unit_start_utc": "2020-11-05T00:00:00Z",
                    "last_time_unit_start_utc": "2020-11-06T00:00:00Z",
                    "rate_id": "ed4b660b-19d0-434b-9360-a4de2ea42eda",
                    "service_id": "bd26d8db-86da-4f96-9efc-e5a4654a4a94",
                    "state": "Confirmed",
                },
                {
                    "first_time_unit_start_utc": "2021-11-05T00:00:00Z",
                    "last_time_unit_start_utc": "2021-11-06T00:00:00Z",
                    "rate_id": "ed4b660b-19d0-434b-9360-a4de2ea42eda",
                    "service_id": "bd26d8db-86da-4f96-9efc-e5a4654a4a94",
                    "state": "Confirmed",
                },
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        availability_block = response.parse()
        assert_matches_type(AvailabilityBlockAddResult, availability_block, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_add(self, client: Pymews) -> None:
        with client.api.connector.v1.availability_blocks.with_streaming_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            availability_blocks=[
                {
                    "first_time_unit_start_utc": "2020-11-05T00:00:00Z",
                    "last_time_unit_start_utc": "2020-11-06T00:00:00Z",
                    "rate_id": "ed4b660b-19d0-434b-9360-a4de2ea42eda",
                    "service_id": "bd26d8db-86da-4f96-9efc-e5a4654a4a94",
                    "state": "Confirmed",
                },
                {
                    "first_time_unit_start_utc": "2021-11-05T00:00:00Z",
                    "last_time_unit_start_utc": "2021-11-06T00:00:00Z",
                    "rate_id": "ed4b660b-19d0-434b-9360-a4de2ea42eda",
                    "service_id": "bd26d8db-86da-4f96-9efc-e5a4654a4a94",
                    "state": "Confirmed",
                },
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            availability_block = response.parse()
            assert_matches_type(AvailabilityBlockAddResult, availability_block, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAvailabilityBlocks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncPymews) -> None:
        availability_block = await async_client.api.connector.v1.availability_blocks.update(
            access_token="x",
            availability_blocks=[{}, {}],
            client="x",
            client_token="x",
        )
        assert_matches_type(AvailabilityBlockAddResult, availability_block, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncPymews) -> None:
        availability_block = await async_client.api.connector.v1.availability_blocks.update(
            access_token="x",
            availability_blocks=[
                {
                    "availability_block_id": "5ee074b1-6c86-48e8-915f-c7aa4702086f",
                    "booker_id": {"value": "ebd507c5-6bfd-4ca9-96aa-ffed6fa94f72"},
                    "budget": {
                        "value": {
                            "currency": "USD",
                            "net": 0,
                            "tax": 0,
                            "tax_rate": 0,
                            "value": 48,
                        }
                    },
                    "cancellation_reason": {"value": "Value"},
                    "cancellation_reason_detail": {"value": "Value"},
                    "company_id": {"value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                    "external_identifier": {"value": "Block-0001"},
                    "first_time_unit_start_utc": {"value": "2021-07-05T00:00:00Z"},
                    "last_time_unit_start_utc": {"value": "2021-07-15T00:00:00Z"},
                    "name": {"value": "Mr. Smith's block"},
                    "notes": {"value": "Have a nice stay"},
                    "quote_id": {"value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                    "released_utc": {"value": "2021-07-01T00:00:00Z"},
                    "release_strategy": {"value": "FixedRelease"},
                    "reservation_purpose": {"value": "Leisure"},
                    "rolling_release_offset": {"value": "Value"},
                    "state": {"value": "Confirmed"},
                    "travel_agency_id": {"value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                },
                {
                    "availability_block_id": "c32386aa-1cd2-414a-a823-489325842fbe",
                    "booker_id": {"value": "ebd507c5-6bfd-4ca9-96aa-ffed6fa94f72"},
                    "budget": {
                        "value": {
                            "currency": "USD",
                            "net": 0,
                            "tax": 0,
                            "tax_rate": 0,
                            "value": 48,
                        }
                    },
                    "cancellation_reason": {"value": "Value"},
                    "cancellation_reason_detail": {"value": "Value"},
                    "company_id": {"value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                    "external_identifier": {"value": "Block-0002"},
                    "first_time_unit_start_utc": {"value": "2022-07-05T00:00:00Z"},
                    "last_time_unit_start_utc": {"value": "2022-07-15T00:00:00Z"},
                    "name": {"value": "Rolling release block"},
                    "notes": {"value": "Have a nice stay"},
                    "quote_id": {"value": "67eaf3c8-81e0-4ffb-b5f2-2b61803feb9c"},
                    "released_utc": {"value": "2021-07-01T00:00:00Z"},
                    "release_strategy": {"value": "RollingRelease"},
                    "reservation_purpose": {"value": "Leisure"},
                    "rolling_release_offset": {"value": "P-3DT4H"},
                    "state": {"value": "Confirmed"},
                    "travel_agency_id": {"value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                },
            ],
            client="x",
            client_token="x",
            enterprise_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AvailabilityBlockAddResult, availability_block, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.availability_blocks.with_raw_response.update(
            access_token="x",
            availability_blocks=[{}, {}],
            client="x",
            client_token="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        availability_block = await response.parse()
        assert_matches_type(AvailabilityBlockAddResult, availability_block, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.availability_blocks.with_streaming_response.update(
            access_token="x",
            availability_blocks=[{}, {}],
            client="x",
            client_token="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            availability_block = await response.parse()
            assert_matches_type(AvailabilityBlockAddResult, availability_block, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncPymews) -> None:
        availability_block = await async_client.api.connector.v1.availability_blocks.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            extent={},
            limitation={"count": 100},
        )
        assert_matches_type(AvailabilityBlockListResponse, availability_block, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPymews) -> None:
        availability_block = await async_client.api.connector.v1.availability_blocks.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            extent={
                "adjustments": True,
                "availability_blocks": True,
                "rates": False,
                "service_orders": False,
            },
            limitation={
                "count": 100,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            activity_states=["Active"],
            availability_block_ids=["5ee074b1-6c86-48e8-915f-c7aa4702086f"],
            colliding_utc={
                "end_utc": parse_datetime("2020-11-05T00:00:00Z"),
                "start_utc": parse_datetime("2020-11-04T00:00:00Z"),
            },
            created_utc={
                "end_utc": parse_datetime("2020-11-05T00:00:00Z"),
                "start_utc": parse_datetime("2020-11-04T00:00:00Z"),
            },
            enterprise_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            external_identifiers=["Block-0001"],
            released_utc={
                "end_utc": parse_datetime("2020-11-05T00:00:00Z"),
                "start_utc": parse_datetime("2020-11-04T00:00:00Z"),
            },
            service_ids=["bd26d8db-86da-4f96-9efc-e5a4654a4a94"],
            states=["Confirmed"],
            updated_utc={
                "end_utc": parse_datetime("2020-11-05T00:00:00Z"),
                "start_utc": parse_datetime("2020-11-04T00:00:00Z"),
            },
        )
        assert_matches_type(AvailabilityBlockListResponse, availability_block, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.availability_blocks.with_raw_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            extent={},
            limitation={"count": 100},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        availability_block = await response.parse()
        assert_matches_type(AvailabilityBlockListResponse, availability_block, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.availability_blocks.with_streaming_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            extent={},
            limitation={"count": 100},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            availability_block = await response.parse()
            assert_matches_type(AvailabilityBlockListResponse, availability_block, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncPymews) -> None:
        availability_block = await async_client.api.connector.v1.availability_blocks.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            availability_block_ids=["5ee074b1-6c86-48e8-915f-c7aa4702086f", "c32386aa-1cd2-414a-a823-489325842fbe"],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )
        assert_matches_type(object, availability_block, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncPymews) -> None:
        availability_block = await async_client.api.connector.v1.availability_blocks.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            availability_block_ids=["5ee074b1-6c86-48e8-915f-c7aa4702086f", "c32386aa-1cd2-414a-a823-489325842fbe"],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            enterprise_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )
        assert_matches_type(object, availability_block, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.availability_blocks.with_raw_response.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            availability_block_ids=["5ee074b1-6c86-48e8-915f-c7aa4702086f", "c32386aa-1cd2-414a-a823-489325842fbe"],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        availability_block = await response.parse()
        assert_matches_type(object, availability_block, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.availability_blocks.with_streaming_response.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            availability_block_ids=["5ee074b1-6c86-48e8-915f-c7aa4702086f", "c32386aa-1cd2-414a-a823-489325842fbe"],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            availability_block = await response.parse()
            assert_matches_type(object, availability_block, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_add(self, async_client: AsyncPymews) -> None:
        availability_block = await async_client.api.connector.v1.availability_blocks.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            availability_blocks=[
                {
                    "first_time_unit_start_utc": "2020-11-05T00:00:00Z",
                    "last_time_unit_start_utc": "2020-11-06T00:00:00Z",
                    "rate_id": "ed4b660b-19d0-434b-9360-a4de2ea42eda",
                    "service_id": "bd26d8db-86da-4f96-9efc-e5a4654a4a94",
                    "state": "Confirmed",
                },
                {
                    "first_time_unit_start_utc": "2021-11-05T00:00:00Z",
                    "last_time_unit_start_utc": "2021-11-06T00:00:00Z",
                    "rate_id": "ed4b660b-19d0-434b-9360-a4de2ea42eda",
                    "service_id": "bd26d8db-86da-4f96-9efc-e5a4654a4a94",
                    "state": "Confirmed",
                },
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )
        assert_matches_type(AvailabilityBlockAddResult, availability_block, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_add_with_all_params(self, async_client: AsyncPymews) -> None:
        availability_block = await async_client.api.connector.v1.availability_blocks.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            availability_blocks=[
                {
                    "first_time_unit_start_utc": "2020-11-05T00:00:00Z",
                    "last_time_unit_start_utc": "2020-11-06T00:00:00Z",
                    "rate_id": "ed4b660b-19d0-434b-9360-a4de2ea42eda",
                    "service_id": "bd26d8db-86da-4f96-9efc-e5a4654a4a94",
                    "state": "Confirmed",
                    "booker_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "budget": {
                        "currency": "USD",
                        "net": 0,
                        "tax": 0,
                        "tax_rate": 0,
                        "value": 48,
                    },
                    "company_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "external_identifier": "Block-0001",
                    "name": "Mr. Smith's block",
                    "notes": "Notes",
                    "quote_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "released_utc": parse_datetime("2020-11-04T00:00:00Z"),
                    "reservation_purpose": "Leisure",
                    "rolling_release_offset": "RollingReleaseOffset",
                    "travel_agency_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "voucher_code": "VoucherCode",
                },
                {
                    "first_time_unit_start_utc": "2021-11-05T00:00:00Z",
                    "last_time_unit_start_utc": "2021-11-06T00:00:00Z",
                    "rate_id": "ed4b660b-19d0-434b-9360-a4de2ea42eda",
                    "service_id": "bd26d8db-86da-4f96-9efc-e5a4654a4a94",
                    "state": "Confirmed",
                    "booker_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "budget": {
                        "currency": "USD",
                        "net": 0,
                        "tax": 0,
                        "tax_rate": 0,
                        "value": 48,
                    },
                    "company_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "external_identifier": "Block-0002",
                    "name": "Rolling release block",
                    "notes": "Notes",
                    "quote_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "released_utc": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "reservation_purpose": "Leisure",
                    "rolling_release_offset": "RollingReleaseOffset",
                    "travel_agency_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "voucher_code": "VoucherCode",
                },
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            enterprise_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )
        assert_matches_type(AvailabilityBlockAddResult, availability_block, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.availability_blocks.with_raw_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            availability_blocks=[
                {
                    "first_time_unit_start_utc": "2020-11-05T00:00:00Z",
                    "last_time_unit_start_utc": "2020-11-06T00:00:00Z",
                    "rate_id": "ed4b660b-19d0-434b-9360-a4de2ea42eda",
                    "service_id": "bd26d8db-86da-4f96-9efc-e5a4654a4a94",
                    "state": "Confirmed",
                },
                {
                    "first_time_unit_start_utc": "2021-11-05T00:00:00Z",
                    "last_time_unit_start_utc": "2021-11-06T00:00:00Z",
                    "rate_id": "ed4b660b-19d0-434b-9360-a4de2ea42eda",
                    "service_id": "bd26d8db-86da-4f96-9efc-e5a4654a4a94",
                    "state": "Confirmed",
                },
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        availability_block = await response.parse()
        assert_matches_type(AvailabilityBlockAddResult, availability_block, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.availability_blocks.with_streaming_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            availability_blocks=[
                {
                    "first_time_unit_start_utc": "2020-11-05T00:00:00Z",
                    "last_time_unit_start_utc": "2020-11-06T00:00:00Z",
                    "rate_id": "ed4b660b-19d0-434b-9360-a4de2ea42eda",
                    "service_id": "bd26d8db-86da-4f96-9efc-e5a4654a4a94",
                    "state": "Confirmed",
                },
                {
                    "first_time_unit_start_utc": "2021-11-05T00:00:00Z",
                    "last_time_unit_start_utc": "2021-11-06T00:00:00Z",
                    "rate_id": "ed4b660b-19d0-434b-9360-a4de2ea42eda",
                    "service_id": "bd26d8db-86da-4f96-9efc-e5a4654a4a94",
                    "state": "Confirmed",
                },
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            availability_block = await response.parse()
            assert_matches_type(AvailabilityBlockAddResult, availability_block, path=["response"])

        assert cast(Any, response.is_closed) is True
