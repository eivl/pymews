# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pymews import Pymews, AsyncPymews
from tests.utils import assert_matches_type
from pymews._utils import parse_datetime
from pymews.types.api.connector.v1 import (
    ServiceOverbookingLimitListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestServiceOverbookingLimits:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Pymews) -> None:
        service_overbooking_limit = client.api.connector.v1.service_overbooking_limits.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 100},
            service_ids=["bd26d8db-86da-4f96-9efc-e5a4654a4a94", "8c1bd738-a505-4b29-aa71-9ecc2982b843"],
        )
        assert_matches_type(ServiceOverbookingLimitListResponse, service_overbooking_limit, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Pymews) -> None:
        service_overbooking_limit = client.api.connector.v1.service_overbooking_limits.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 100,
                "cursor": "e7f26210-10e7-462e-9da8-ae8300be8ab7",
            },
            service_ids=["bd26d8db-86da-4f96-9efc-e5a4654a4a94", "8c1bd738-a505-4b29-aa71-9ecc2982b843"],
            activity_states=["Active"],
            colliding_utc={
                "end_utc": parse_datetime("2024-11-30T00:00:00Z"),
                "start_utc": parse_datetime("2024-11-01T00:00:00Z"),
            },
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            service_overbooking_limit_ids=["e654f217-d1b5-46be-a820-e93ba568dfac"],
            updated_utc={
                "end_utc": parse_datetime("2024-11-30T00:00:00Z"),
                "start_utc": parse_datetime("2024-11-01T00:00:00Z"),
            },
        )
        assert_matches_type(ServiceOverbookingLimitListResponse, service_overbooking_limit, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Pymews) -> None:
        response = client.api.connector.v1.service_overbooking_limits.with_raw_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 100},
            service_ids=["bd26d8db-86da-4f96-9efc-e5a4654a4a94", "8c1bd738-a505-4b29-aa71-9ecc2982b843"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service_overbooking_limit = response.parse()
        assert_matches_type(ServiceOverbookingLimitListResponse, service_overbooking_limit, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Pymews) -> None:
        with client.api.connector.v1.service_overbooking_limits.with_streaming_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 100},
            service_ids=["bd26d8db-86da-4f96-9efc-e5a4654a4a94", "8c1bd738-a505-4b29-aa71-9ecc2982b843"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service_overbooking_limit = response.parse()
            assert_matches_type(ServiceOverbookingLimitListResponse, service_overbooking_limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_clear(self, client: Pymews) -> None:
        service_overbooking_limit = client.api.connector.v1.service_overbooking_limits.clear(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            clear_service_overbooking_limits=[
                {
                    "first_time_unit_start_utc": parse_datetime("2024-11-01T00:00:00Z"),
                    "last_time_unit_start_utc": parse_datetime("2024-11-30T00:00:00Z"),
                }
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
        )
        assert_matches_type(object, service_overbooking_limit, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_clear_with_all_params(self, client: Pymews) -> None:
        service_overbooking_limit = client.api.connector.v1.service_overbooking_limits.clear(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            clear_service_overbooking_limits=[
                {
                    "first_time_unit_start_utc": parse_datetime("2024-11-01T00:00:00Z"),
                    "last_time_unit_start_utc": parse_datetime("2024-11-30T00:00:00Z"),
                }
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
            enterprise_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )
        assert_matches_type(object, service_overbooking_limit, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_clear(self, client: Pymews) -> None:
        response = client.api.connector.v1.service_overbooking_limits.with_raw_response.clear(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            clear_service_overbooking_limits=[
                {
                    "first_time_unit_start_utc": parse_datetime("2024-11-01T00:00:00Z"),
                    "last_time_unit_start_utc": parse_datetime("2024-11-30T00:00:00Z"),
                }
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service_overbooking_limit = response.parse()
        assert_matches_type(object, service_overbooking_limit, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_clear(self, client: Pymews) -> None:
        with client.api.connector.v1.service_overbooking_limits.with_streaming_response.clear(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            clear_service_overbooking_limits=[
                {
                    "first_time_unit_start_utc": parse_datetime("2024-11-01T00:00:00Z"),
                    "last_time_unit_start_utc": parse_datetime("2024-11-30T00:00:00Z"),
                }
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service_overbooking_limit = response.parse()
            assert_matches_type(object, service_overbooking_limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_set(self, client: Pymews) -> None:
        service_overbooking_limit = client.api.connector.v1.service_overbooking_limits.set(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
            set_service_overbooking_limits=[
                {
                    "first_time_unit_start_utc": parse_datetime("2024-11-01T00:00:00Z"),
                    "last_time_unit_start_utc": parse_datetime("2024-11-30T00:00:00Z"),
                    "limit": 10,
                }
            ],
        )
        assert_matches_type(object, service_overbooking_limit, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_set_with_all_params(self, client: Pymews) -> None:
        service_overbooking_limit = client.api.connector.v1.service_overbooking_limits.set(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
            set_service_overbooking_limits=[
                {
                    "first_time_unit_start_utc": parse_datetime("2024-11-01T00:00:00Z"),
                    "last_time_unit_start_utc": parse_datetime("2024-11-30T00:00:00Z"),
                    "limit": 10,
                }
            ],
            enterprise_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )
        assert_matches_type(object, service_overbooking_limit, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_set(self, client: Pymews) -> None:
        response = client.api.connector.v1.service_overbooking_limits.with_raw_response.set(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
            set_service_overbooking_limits=[
                {
                    "first_time_unit_start_utc": parse_datetime("2024-11-01T00:00:00Z"),
                    "last_time_unit_start_utc": parse_datetime("2024-11-30T00:00:00Z"),
                    "limit": 10,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service_overbooking_limit = response.parse()
        assert_matches_type(object, service_overbooking_limit, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_set(self, client: Pymews) -> None:
        with client.api.connector.v1.service_overbooking_limits.with_streaming_response.set(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
            set_service_overbooking_limits=[
                {
                    "first_time_unit_start_utc": parse_datetime("2024-11-01T00:00:00Z"),
                    "last_time_unit_start_utc": parse_datetime("2024-11-30T00:00:00Z"),
                    "limit": 10,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service_overbooking_limit = response.parse()
            assert_matches_type(object, service_overbooking_limit, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncServiceOverbookingLimits:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncPymews) -> None:
        service_overbooking_limit = await async_client.api.connector.v1.service_overbooking_limits.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 100},
            service_ids=["bd26d8db-86da-4f96-9efc-e5a4654a4a94", "8c1bd738-a505-4b29-aa71-9ecc2982b843"],
        )
        assert_matches_type(ServiceOverbookingLimitListResponse, service_overbooking_limit, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPymews) -> None:
        service_overbooking_limit = await async_client.api.connector.v1.service_overbooking_limits.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 100,
                "cursor": "e7f26210-10e7-462e-9da8-ae8300be8ab7",
            },
            service_ids=["bd26d8db-86da-4f96-9efc-e5a4654a4a94", "8c1bd738-a505-4b29-aa71-9ecc2982b843"],
            activity_states=["Active"],
            colliding_utc={
                "end_utc": parse_datetime("2024-11-30T00:00:00Z"),
                "start_utc": parse_datetime("2024-11-01T00:00:00Z"),
            },
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            service_overbooking_limit_ids=["e654f217-d1b5-46be-a820-e93ba568dfac"],
            updated_utc={
                "end_utc": parse_datetime("2024-11-30T00:00:00Z"),
                "start_utc": parse_datetime("2024-11-01T00:00:00Z"),
            },
        )
        assert_matches_type(ServiceOverbookingLimitListResponse, service_overbooking_limit, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.service_overbooking_limits.with_raw_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 100},
            service_ids=["bd26d8db-86da-4f96-9efc-e5a4654a4a94", "8c1bd738-a505-4b29-aa71-9ecc2982b843"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service_overbooking_limit = await response.parse()
        assert_matches_type(ServiceOverbookingLimitListResponse, service_overbooking_limit, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.service_overbooking_limits.with_streaming_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 100},
            service_ids=["bd26d8db-86da-4f96-9efc-e5a4654a4a94", "8c1bd738-a505-4b29-aa71-9ecc2982b843"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service_overbooking_limit = await response.parse()
            assert_matches_type(ServiceOverbookingLimitListResponse, service_overbooking_limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_clear(self, async_client: AsyncPymews) -> None:
        service_overbooking_limit = await async_client.api.connector.v1.service_overbooking_limits.clear(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            clear_service_overbooking_limits=[
                {
                    "first_time_unit_start_utc": parse_datetime("2024-11-01T00:00:00Z"),
                    "last_time_unit_start_utc": parse_datetime("2024-11-30T00:00:00Z"),
                }
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
        )
        assert_matches_type(object, service_overbooking_limit, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_clear_with_all_params(self, async_client: AsyncPymews) -> None:
        service_overbooking_limit = await async_client.api.connector.v1.service_overbooking_limits.clear(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            clear_service_overbooking_limits=[
                {
                    "first_time_unit_start_utc": parse_datetime("2024-11-01T00:00:00Z"),
                    "last_time_unit_start_utc": parse_datetime("2024-11-30T00:00:00Z"),
                }
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
            enterprise_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )
        assert_matches_type(object, service_overbooking_limit, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_clear(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.service_overbooking_limits.with_raw_response.clear(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            clear_service_overbooking_limits=[
                {
                    "first_time_unit_start_utc": parse_datetime("2024-11-01T00:00:00Z"),
                    "last_time_unit_start_utc": parse_datetime("2024-11-30T00:00:00Z"),
                }
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service_overbooking_limit = await response.parse()
        assert_matches_type(object, service_overbooking_limit, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_clear(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.service_overbooking_limits.with_streaming_response.clear(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            clear_service_overbooking_limits=[
                {
                    "first_time_unit_start_utc": parse_datetime("2024-11-01T00:00:00Z"),
                    "last_time_unit_start_utc": parse_datetime("2024-11-30T00:00:00Z"),
                }
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service_overbooking_limit = await response.parse()
            assert_matches_type(object, service_overbooking_limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_set(self, async_client: AsyncPymews) -> None:
        service_overbooking_limit = await async_client.api.connector.v1.service_overbooking_limits.set(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
            set_service_overbooking_limits=[
                {
                    "first_time_unit_start_utc": parse_datetime("2024-11-01T00:00:00Z"),
                    "last_time_unit_start_utc": parse_datetime("2024-11-30T00:00:00Z"),
                    "limit": 10,
                }
            ],
        )
        assert_matches_type(object, service_overbooking_limit, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_set_with_all_params(self, async_client: AsyncPymews) -> None:
        service_overbooking_limit = await async_client.api.connector.v1.service_overbooking_limits.set(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
            set_service_overbooking_limits=[
                {
                    "first_time_unit_start_utc": parse_datetime("2024-11-01T00:00:00Z"),
                    "last_time_unit_start_utc": parse_datetime("2024-11-30T00:00:00Z"),
                    "limit": 10,
                }
            ],
            enterprise_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )
        assert_matches_type(object, service_overbooking_limit, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_set(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.service_overbooking_limits.with_raw_response.set(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
            set_service_overbooking_limits=[
                {
                    "first_time_unit_start_utc": parse_datetime("2024-11-01T00:00:00Z"),
                    "last_time_unit_start_utc": parse_datetime("2024-11-30T00:00:00Z"),
                    "limit": 10,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service_overbooking_limit = await response.parse()
        assert_matches_type(object, service_overbooking_limit, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_set(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.service_overbooking_limits.with_streaming_response.set(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
            set_service_overbooking_limits=[
                {
                    "first_time_unit_start_utc": parse_datetime("2024-11-01T00:00:00Z"),
                    "last_time_unit_start_utc": parse_datetime("2024-11-30T00:00:00Z"),
                    "limit": 10,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service_overbooking_limit = await response.parse()
            assert_matches_type(object, service_overbooking_limit, path=["response"])

        assert cast(Any, response.is_closed) is True
