# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pymews import Pymews, AsyncPymews
from tests.utils import assert_matches_type
from pymews._utils import parse_datetime
from pymews.types.api.connector.v1 import (
    ServiceListResponse,
    ServiceGetAvailabilityResponse,
    ServiceGetAvailability2024_01_22Response,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestServices:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Pymews) -> None:
        service = client.api.connector.v1.services.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )
        assert_matches_type(ServiceListResponse, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Pymews) -> None:
        service = client.api.connector.v1.services.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            service_ids=["fc79a518-bc69-45b8-93bd-83326201bd14", "bd26d8db-86da-4f96-9efc-e5a4654a4a94"],
            updated_utc={
                "end_utc": parse_datetime("2020-01-10T00:00:00Z"),
                "start_utc": parse_datetime("2020-01-05T00:00:00Z"),
            },
        )
        assert_matches_type(ServiceListResponse, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Pymews) -> None:
        response = client.api.connector.v1.services.with_raw_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = response.parse()
        assert_matches_type(ServiceListResponse, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Pymews) -> None:
        with client.api.connector.v1.services.with_streaming_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = response.parse()
            assert_matches_type(ServiceListResponse, service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_availability(self, client: Pymews) -> None:
        service = client.api.connector.v1.services.get_availability(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            first_time_unit_start_utc=parse_datetime("2017-01-01T23:00:00.000Z"),
            last_time_unit_start_utc=parse_datetime("2017-01-03T23:00:00.000Z"),
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
        )
        assert_matches_type(ServiceGetAvailabilityResponse, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_availability_with_all_params(self, client: Pymews) -> None:
        service = client.api.connector.v1.services.get_availability(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            first_time_unit_start_utc=parse_datetime("2017-01-01T23:00:00.000Z"),
            last_time_unit_start_utc=parse_datetime("2017-01-03T23:00:00.000Z"),
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
            end_utc=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_utc=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ServiceGetAvailabilityResponse, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_availability(self, client: Pymews) -> None:
        response = client.api.connector.v1.services.with_raw_response.get_availability(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            first_time_unit_start_utc=parse_datetime("2017-01-01T23:00:00.000Z"),
            last_time_unit_start_utc=parse_datetime("2017-01-03T23:00:00.000Z"),
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = response.parse()
        assert_matches_type(ServiceGetAvailabilityResponse, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_availability(self, client: Pymews) -> None:
        with client.api.connector.v1.services.with_streaming_response.get_availability(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            first_time_unit_start_utc=parse_datetime("2017-01-01T23:00:00.000Z"),
            last_time_unit_start_utc=parse_datetime("2017-01-03T23:00:00.000Z"),
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = response.parse()
            assert_matches_type(ServiceGetAvailabilityResponse, service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_availability_2024_01_22(self, client: Pymews) -> None:
        service = client.api.connector.v1.services.get_availability_2024_01_22(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            first_time_unit_start_utc=parse_datetime("2024-02-01T23:00:00.000Z"),
            last_time_unit_start_utc=parse_datetime("2024-02-05T23:00:00.000Z"),
            metrics=[
                "OutOfOrderBlocks",
                "PublicAvailabilityAdjustment",
                "OtherServiceReservationCount",
                "Occupied",
                "ConfirmedReservations",
                "OptionalReservations",
                "BlockAvailability",
                "AllocatedBlockAvailability",
                "UsableResources",
                "ActiveResources",
            ],
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
        )
        assert_matches_type(ServiceGetAvailability2024_01_22Response, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_availability_2024_01_22(self, client: Pymews) -> None:
        response = client.api.connector.v1.services.with_raw_response.get_availability_2024_01_22(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            first_time_unit_start_utc=parse_datetime("2024-02-01T23:00:00.000Z"),
            last_time_unit_start_utc=parse_datetime("2024-02-05T23:00:00.000Z"),
            metrics=[
                "OutOfOrderBlocks",
                "PublicAvailabilityAdjustment",
                "OtherServiceReservationCount",
                "Occupied",
                "ConfirmedReservations",
                "OptionalReservations",
                "BlockAvailability",
                "AllocatedBlockAvailability",
                "UsableResources",
                "ActiveResources",
            ],
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = response.parse()
        assert_matches_type(ServiceGetAvailability2024_01_22Response, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_availability_2024_01_22(self, client: Pymews) -> None:
        with client.api.connector.v1.services.with_streaming_response.get_availability_2024_01_22(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            first_time_unit_start_utc=parse_datetime("2024-02-01T23:00:00.000Z"),
            last_time_unit_start_utc=parse_datetime("2024-02-05T23:00:00.000Z"),
            metrics=[
                "OutOfOrderBlocks",
                "PublicAvailabilityAdjustment",
                "OtherServiceReservationCount",
                "Occupied",
                "ConfirmedReservations",
                "OptionalReservations",
                "BlockAvailability",
                "AllocatedBlockAvailability",
                "UsableResources",
                "ActiveResources",
            ],
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = response.parse()
            assert_matches_type(ServiceGetAvailability2024_01_22Response, service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_update_availability(self, client: Pymews) -> None:
        service = client.api.connector.v1.services.update_availability(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            availability_updates=[
                {
                    "first_time_unit_start_utc": parse_datetime("2020-10-05T23:00:00Z"),
                    "last_time_unit_start_utc": parse_datetime("2020-10-05T23:00:00Z"),
                    "resource_category_id": "46bc1498-38cf-4d03-b144-aa69012f5d50",
                    "unit_count_adjustment": {},
                },
                {
                    "first_time_unit_start_utc": parse_datetime("2020-10-07T23:00:00Z"),
                    "last_time_unit_start_utc": parse_datetime("2020-10-08T23:00:00Z"),
                    "resource_category_id": "46bc1498-38cf-4d03-b144-aa69012f5d50",
                    "unit_count_adjustment": {},
                },
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
        )
        assert_matches_type(object, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update_availability(self, client: Pymews) -> None:
        response = client.api.connector.v1.services.with_raw_response.update_availability(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            availability_updates=[
                {
                    "first_time_unit_start_utc": parse_datetime("2020-10-05T23:00:00Z"),
                    "last_time_unit_start_utc": parse_datetime("2020-10-05T23:00:00Z"),
                    "resource_category_id": "46bc1498-38cf-4d03-b144-aa69012f5d50",
                    "unit_count_adjustment": {},
                },
                {
                    "first_time_unit_start_utc": parse_datetime("2020-10-07T23:00:00Z"),
                    "last_time_unit_start_utc": parse_datetime("2020-10-08T23:00:00Z"),
                    "resource_category_id": "46bc1498-38cf-4d03-b144-aa69012f5d50",
                    "unit_count_adjustment": {},
                },
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = response.parse()
        assert_matches_type(object, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update_availability(self, client: Pymews) -> None:
        with client.api.connector.v1.services.with_streaming_response.update_availability(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            availability_updates=[
                {
                    "first_time_unit_start_utc": parse_datetime("2020-10-05T23:00:00Z"),
                    "last_time_unit_start_utc": parse_datetime("2020-10-05T23:00:00Z"),
                    "resource_category_id": "46bc1498-38cf-4d03-b144-aa69012f5d50",
                    "unit_count_adjustment": {},
                },
                {
                    "first_time_unit_start_utc": parse_datetime("2020-10-07T23:00:00Z"),
                    "last_time_unit_start_utc": parse_datetime("2020-10-08T23:00:00Z"),
                    "resource_category_id": "46bc1498-38cf-4d03-b144-aa69012f5d50",
                    "unit_count_adjustment": {},
                },
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = response.parse()
            assert_matches_type(object, service, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncServices:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncPymews) -> None:
        service = await async_client.api.connector.v1.services.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )
        assert_matches_type(ServiceListResponse, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPymews) -> None:
        service = await async_client.api.connector.v1.services.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            service_ids=["fc79a518-bc69-45b8-93bd-83326201bd14", "bd26d8db-86da-4f96-9efc-e5a4654a4a94"],
            updated_utc={
                "end_utc": parse_datetime("2020-01-10T00:00:00Z"),
                "start_utc": parse_datetime("2020-01-05T00:00:00Z"),
            },
        )
        assert_matches_type(ServiceListResponse, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.services.with_raw_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = await response.parse()
        assert_matches_type(ServiceListResponse, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.services.with_streaming_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = await response.parse()
            assert_matches_type(ServiceListResponse, service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_availability(self, async_client: AsyncPymews) -> None:
        service = await async_client.api.connector.v1.services.get_availability(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            first_time_unit_start_utc=parse_datetime("2017-01-01T23:00:00.000Z"),
            last_time_unit_start_utc=parse_datetime("2017-01-03T23:00:00.000Z"),
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
        )
        assert_matches_type(ServiceGetAvailabilityResponse, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_availability_with_all_params(self, async_client: AsyncPymews) -> None:
        service = await async_client.api.connector.v1.services.get_availability(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            first_time_unit_start_utc=parse_datetime("2017-01-01T23:00:00.000Z"),
            last_time_unit_start_utc=parse_datetime("2017-01-03T23:00:00.000Z"),
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
            end_utc=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_utc=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ServiceGetAvailabilityResponse, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_availability(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.services.with_raw_response.get_availability(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            first_time_unit_start_utc=parse_datetime("2017-01-01T23:00:00.000Z"),
            last_time_unit_start_utc=parse_datetime("2017-01-03T23:00:00.000Z"),
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = await response.parse()
        assert_matches_type(ServiceGetAvailabilityResponse, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_availability(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.services.with_streaming_response.get_availability(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            first_time_unit_start_utc=parse_datetime("2017-01-01T23:00:00.000Z"),
            last_time_unit_start_utc=parse_datetime("2017-01-03T23:00:00.000Z"),
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = await response.parse()
            assert_matches_type(ServiceGetAvailabilityResponse, service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_availability_2024_01_22(self, async_client: AsyncPymews) -> None:
        service = await async_client.api.connector.v1.services.get_availability_2024_01_22(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            first_time_unit_start_utc=parse_datetime("2024-02-01T23:00:00.000Z"),
            last_time_unit_start_utc=parse_datetime("2024-02-05T23:00:00.000Z"),
            metrics=[
                "OutOfOrderBlocks",
                "PublicAvailabilityAdjustment",
                "OtherServiceReservationCount",
                "Occupied",
                "ConfirmedReservations",
                "OptionalReservations",
                "BlockAvailability",
                "AllocatedBlockAvailability",
                "UsableResources",
                "ActiveResources",
            ],
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
        )
        assert_matches_type(ServiceGetAvailability2024_01_22Response, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_availability_2024_01_22(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.services.with_raw_response.get_availability_2024_01_22(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            first_time_unit_start_utc=parse_datetime("2024-02-01T23:00:00.000Z"),
            last_time_unit_start_utc=parse_datetime("2024-02-05T23:00:00.000Z"),
            metrics=[
                "OutOfOrderBlocks",
                "PublicAvailabilityAdjustment",
                "OtherServiceReservationCount",
                "Occupied",
                "ConfirmedReservations",
                "OptionalReservations",
                "BlockAvailability",
                "AllocatedBlockAvailability",
                "UsableResources",
                "ActiveResources",
            ],
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = await response.parse()
        assert_matches_type(ServiceGetAvailability2024_01_22Response, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_availability_2024_01_22(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.services.with_streaming_response.get_availability_2024_01_22(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            first_time_unit_start_utc=parse_datetime("2024-02-01T23:00:00.000Z"),
            last_time_unit_start_utc=parse_datetime("2024-02-05T23:00:00.000Z"),
            metrics=[
                "OutOfOrderBlocks",
                "PublicAvailabilityAdjustment",
                "OtherServiceReservationCount",
                "Occupied",
                "ConfirmedReservations",
                "OptionalReservations",
                "BlockAvailability",
                "AllocatedBlockAvailability",
                "UsableResources",
                "ActiveResources",
            ],
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = await response.parse()
            assert_matches_type(ServiceGetAvailability2024_01_22Response, service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_availability(self, async_client: AsyncPymews) -> None:
        service = await async_client.api.connector.v1.services.update_availability(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            availability_updates=[
                {
                    "first_time_unit_start_utc": parse_datetime("2020-10-05T23:00:00Z"),
                    "last_time_unit_start_utc": parse_datetime("2020-10-05T23:00:00Z"),
                    "resource_category_id": "46bc1498-38cf-4d03-b144-aa69012f5d50",
                    "unit_count_adjustment": {},
                },
                {
                    "first_time_unit_start_utc": parse_datetime("2020-10-07T23:00:00Z"),
                    "last_time_unit_start_utc": parse_datetime("2020-10-08T23:00:00Z"),
                    "resource_category_id": "46bc1498-38cf-4d03-b144-aa69012f5d50",
                    "unit_count_adjustment": {},
                },
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
        )
        assert_matches_type(object, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update_availability(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.services.with_raw_response.update_availability(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            availability_updates=[
                {
                    "first_time_unit_start_utc": parse_datetime("2020-10-05T23:00:00Z"),
                    "last_time_unit_start_utc": parse_datetime("2020-10-05T23:00:00Z"),
                    "resource_category_id": "46bc1498-38cf-4d03-b144-aa69012f5d50",
                    "unit_count_adjustment": {},
                },
                {
                    "first_time_unit_start_utc": parse_datetime("2020-10-07T23:00:00Z"),
                    "last_time_unit_start_utc": parse_datetime("2020-10-08T23:00:00Z"),
                    "resource_category_id": "46bc1498-38cf-4d03-b144-aa69012f5d50",
                    "unit_count_adjustment": {},
                },
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = await response.parse()
        assert_matches_type(object, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update_availability(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.services.with_streaming_response.update_availability(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            availability_updates=[
                {
                    "first_time_unit_start_utc": parse_datetime("2020-10-05T23:00:00Z"),
                    "last_time_unit_start_utc": parse_datetime("2020-10-05T23:00:00Z"),
                    "resource_category_id": "46bc1498-38cf-4d03-b144-aa69012f5d50",
                    "unit_count_adjustment": {},
                },
                {
                    "first_time_unit_start_utc": parse_datetime("2020-10-07T23:00:00Z"),
                    "last_time_unit_start_utc": parse_datetime("2020-10-08T23:00:00Z"),
                    "resource_category_id": "46bc1498-38cf-4d03-b144-aa69012f5d50",
                    "unit_count_adjustment": {},
                },
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = await response.parse()
            assert_matches_type(object, service, path=["response"])

        assert cast(Any, response.is_closed) is True
