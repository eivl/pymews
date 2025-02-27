# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pymews import Pymews, AsyncPymews
from tests.utils import assert_matches_type
from pymews._utils import parse_datetime
from pymews.types.api.connector.v1 import (
    CancellationPolicyListResponse,
    CancellationPolicyGetByRatesResponse,
    CancellationPolicyGetByReservationsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCancellationPolicies:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Pymews) -> None:
        cancellation_policy = client.api.connector.v1.cancellation_policies.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            service_ids=["e654f217-d1b5-46be-a820-e93ba568dfac"],
        )
        assert_matches_type(CancellationPolicyListResponse, cancellation_policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Pymews) -> None:
        cancellation_policy = client.api.connector.v1.cancellation_policies.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            service_ids=["e654f217-d1b5-46be-a820-e93ba568dfac"],
            activity_states=["Deleted"],
            cancellation_policy_ids=["fe795f96-0b64-445b-89ed-c032563f2bac"],
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            rate_group_ids=["deb9444e-6897-4f2a-86b4-aff100c2896e"],
            updated_utc={
                "end_utc": parse_datetime("2023-04-27T11:48:57Z"),
                "start_utc": parse_datetime("2023-04-27T11:48:57Z"),
            },
        )
        assert_matches_type(CancellationPolicyListResponse, cancellation_policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Pymews) -> None:
        response = client.api.connector.v1.cancellation_policies.with_raw_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            service_ids=["e654f217-d1b5-46be-a820-e93ba568dfac"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cancellation_policy = response.parse()
        assert_matches_type(CancellationPolicyListResponse, cancellation_policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Pymews) -> None:
        with client.api.connector.v1.cancellation_policies.with_streaming_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            service_ids=["e654f217-d1b5-46be-a820-e93ba568dfac"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cancellation_policy = response.parse()
            assert_matches_type(CancellationPolicyListResponse, cancellation_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_by_rates(self, client: Pymews) -> None:
        cancellation_policy = client.api.connector.v1.cancellation_policies.get_by_rates(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            rate_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            reservation_end_utc=parse_datetime("2019-12-27T18:11:19.117Z"),
            reservation_start_utc=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(CancellationPolicyGetByRatesResponse, cancellation_policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_by_rates(self, client: Pymews) -> None:
        response = client.api.connector.v1.cancellation_policies.with_raw_response.get_by_rates(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            rate_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            reservation_end_utc=parse_datetime("2019-12-27T18:11:19.117Z"),
            reservation_start_utc=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cancellation_policy = response.parse()
        assert_matches_type(CancellationPolicyGetByRatesResponse, cancellation_policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_by_rates(self, client: Pymews) -> None:
        with client.api.connector.v1.cancellation_policies.with_streaming_response.get_by_rates(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            rate_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            reservation_end_utc=parse_datetime("2019-12-27T18:11:19.117Z"),
            reservation_start_utc=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cancellation_policy = response.parse()
            assert_matches_type(CancellationPolicyGetByRatesResponse, cancellation_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_by_reservations(self, client: Pymews) -> None:
        cancellation_policy = client.api.connector.v1.cancellation_policies.get_by_reservations(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservation_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
        )
        assert_matches_type(CancellationPolicyGetByReservationsResponse, cancellation_policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_by_reservations(self, client: Pymews) -> None:
        response = client.api.connector.v1.cancellation_policies.with_raw_response.get_by_reservations(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservation_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cancellation_policy = response.parse()
        assert_matches_type(CancellationPolicyGetByReservationsResponse, cancellation_policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_by_reservations(self, client: Pymews) -> None:
        with client.api.connector.v1.cancellation_policies.with_streaming_response.get_by_reservations(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservation_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cancellation_policy = response.parse()
            assert_matches_type(CancellationPolicyGetByReservationsResponse, cancellation_policy, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCancellationPolicies:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncPymews) -> None:
        cancellation_policy = await async_client.api.connector.v1.cancellation_policies.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            service_ids=["e654f217-d1b5-46be-a820-e93ba568dfac"],
        )
        assert_matches_type(CancellationPolicyListResponse, cancellation_policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPymews) -> None:
        cancellation_policy = await async_client.api.connector.v1.cancellation_policies.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            service_ids=["e654f217-d1b5-46be-a820-e93ba568dfac"],
            activity_states=["Deleted"],
            cancellation_policy_ids=["fe795f96-0b64-445b-89ed-c032563f2bac"],
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            rate_group_ids=["deb9444e-6897-4f2a-86b4-aff100c2896e"],
            updated_utc={
                "end_utc": parse_datetime("2023-04-27T11:48:57Z"),
                "start_utc": parse_datetime("2023-04-27T11:48:57Z"),
            },
        )
        assert_matches_type(CancellationPolicyListResponse, cancellation_policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.cancellation_policies.with_raw_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            service_ids=["e654f217-d1b5-46be-a820-e93ba568dfac"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cancellation_policy = await response.parse()
        assert_matches_type(CancellationPolicyListResponse, cancellation_policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.cancellation_policies.with_streaming_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            service_ids=["e654f217-d1b5-46be-a820-e93ba568dfac"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cancellation_policy = await response.parse()
            assert_matches_type(CancellationPolicyListResponse, cancellation_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_by_rates(self, async_client: AsyncPymews) -> None:
        cancellation_policy = await async_client.api.connector.v1.cancellation_policies.get_by_rates(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            rate_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            reservation_end_utc=parse_datetime("2019-12-27T18:11:19.117Z"),
            reservation_start_utc=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(CancellationPolicyGetByRatesResponse, cancellation_policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_by_rates(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.cancellation_policies.with_raw_response.get_by_rates(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            rate_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            reservation_end_utc=parse_datetime("2019-12-27T18:11:19.117Z"),
            reservation_start_utc=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cancellation_policy = await response.parse()
        assert_matches_type(CancellationPolicyGetByRatesResponse, cancellation_policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_by_rates(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.cancellation_policies.with_streaming_response.get_by_rates(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            rate_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            reservation_end_utc=parse_datetime("2019-12-27T18:11:19.117Z"),
            reservation_start_utc=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cancellation_policy = await response.parse()
            assert_matches_type(CancellationPolicyGetByRatesResponse, cancellation_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_by_reservations(self, async_client: AsyncPymews) -> None:
        cancellation_policy = await async_client.api.connector.v1.cancellation_policies.get_by_reservations(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservation_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
        )
        assert_matches_type(CancellationPolicyGetByReservationsResponse, cancellation_policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_by_reservations(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.cancellation_policies.with_raw_response.get_by_reservations(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservation_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cancellation_policy = await response.parse()
        assert_matches_type(CancellationPolicyGetByReservationsResponse, cancellation_policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_by_reservations(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.cancellation_policies.with_streaming_response.get_by_reservations(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservation_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cancellation_policy = await response.parse()
            assert_matches_type(CancellationPolicyGetByReservationsResponse, cancellation_policy, path=["response"])

        assert cast(Any, response.is_closed) is True
