# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pymews import Pymews, AsyncPymews
from tests.utils import assert_matches_type
from pymews._utils import parse_datetime
from pymews.types.api.connector.v1 import (
    LoyaltyTierResult,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLoyaltyTiers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Pymews) -> None:
        loyalty_tier = client.api.connector.v1.loyalty_tiers.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            loyalty_tier_updates=[{"loyalty_tier_id": "a58ff7cb-77e3-495a-bd61-aecf00a3f19d"}],
        )
        assert_matches_type(LoyaltyTierResult, loyalty_tier, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Pymews) -> None:
        response = client.api.connector.v1.loyalty_tiers.with_raw_response.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            loyalty_tier_updates=[{"loyalty_tier_id": "a58ff7cb-77e3-495a-bd61-aecf00a3f19d"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        loyalty_tier = response.parse()
        assert_matches_type(LoyaltyTierResult, loyalty_tier, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Pymews) -> None:
        with client.api.connector.v1.loyalty_tiers.with_streaming_response.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            loyalty_tier_updates=[{"loyalty_tier_id": "a58ff7cb-77e3-495a-bd61-aecf00a3f19d"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            loyalty_tier = response.parse()
            assert_matches_type(LoyaltyTierResult, loyalty_tier, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Pymews) -> None:
        loyalty_tier = client.api.connector.v1.loyalty_tiers.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            loyalty_program_ids=["3ed9e2f3-4bba-4df6-8d41-ab1b009b6425", "8a98965a-7c03-48a1-a28c-ab1b009b53c8"],
        )
        assert_matches_type(LoyaltyTierResult, loyalty_tier, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Pymews) -> None:
        loyalty_tier = client.api.connector.v1.loyalty_tiers.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            loyalty_program_ids=["3ed9e2f3-4bba-4df6-8d41-ab1b009b6425", "8a98965a-7c03-48a1-a28c-ab1b009b53c8"],
            activity_states=["Active"],
            chain_ids=["1df21f06-0cfc-4960-9c58-a3bf1261663e", "5fcd1933-22f2-40b9-84da-7db04cbecec2"],
            limitation={
                "count": 100,
                "cursor": "e7f26210-10e7-462e-9da8-ae8300be8ab7",
            },
            loyalty_tier_ids=["a6738390-c241-45b7-8e46-14f47207abe5", "435d4d5f-d14f-48dc-a47e-0481fc28ead0"],
            updated_utc={
                "end_utc": parse_datetime("2022-10-17T00:00:00Z"),
                "start_utc": parse_datetime("2022-10-10T00:00:00Z"),
            },
        )
        assert_matches_type(LoyaltyTierResult, loyalty_tier, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Pymews) -> None:
        response = client.api.connector.v1.loyalty_tiers.with_raw_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            loyalty_program_ids=["3ed9e2f3-4bba-4df6-8d41-ab1b009b6425", "8a98965a-7c03-48a1-a28c-ab1b009b53c8"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        loyalty_tier = response.parse()
        assert_matches_type(LoyaltyTierResult, loyalty_tier, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Pymews) -> None:
        with client.api.connector.v1.loyalty_tiers.with_streaming_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            loyalty_program_ids=["3ed9e2f3-4bba-4df6-8d41-ab1b009b6425", "8a98965a-7c03-48a1-a28c-ab1b009b53c8"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            loyalty_tier = response.parse()
            assert_matches_type(LoyaltyTierResult, loyalty_tier, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Pymews) -> None:
        loyalty_tier = client.api.connector.v1.loyalty_tiers.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            loyalty_tier_ids=["a58ff7cb-77e3-495a-bd61-aecf00a3f19d", "da34b396-41f7-47f6-8847-aecf00a3f19e"],
        )
        assert_matches_type(object, loyalty_tier, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Pymews) -> None:
        response = client.api.connector.v1.loyalty_tiers.with_raw_response.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            loyalty_tier_ids=["a58ff7cb-77e3-495a-bd61-aecf00a3f19d", "da34b396-41f7-47f6-8847-aecf00a3f19e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        loyalty_tier = response.parse()
        assert_matches_type(object, loyalty_tier, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Pymews) -> None:
        with client.api.connector.v1.loyalty_tiers.with_streaming_response.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            loyalty_tier_ids=["a58ff7cb-77e3-495a-bd61-aecf00a3f19d", "da34b396-41f7-47f6-8847-aecf00a3f19e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            loyalty_tier = response.parse()
            assert_matches_type(object, loyalty_tier, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_add(self, client: Pymews) -> None:
        loyalty_tier = client.api.connector.v1.loyalty_tiers.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            loyalty_tiers=[
                {
                    "code": "P1",
                    "loyalty_program_id": "8ddea57b-6a5c-4eec-8c4c-24467dce118e",
                    "name": "Platinum",
                    "ordering": 1,
                }
            ],
        )
        assert_matches_type(LoyaltyTierResult, loyalty_tier, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_add_with_all_params(self, client: Pymews) -> None:
        loyalty_tier = client.api.connector.v1.loyalty_tiers.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            loyalty_tiers=[
                {
                    "code": "P1",
                    "loyalty_program_id": "8ddea57b-6a5c-4eec-8c4c-24467dce118e",
                    "name": "Platinum",
                    "ordering": 1,
                }
            ],
            chain_id="1df21f06-0cfc-4960-9c58-a3bf1261663e",
        )
        assert_matches_type(LoyaltyTierResult, loyalty_tier, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_add(self, client: Pymews) -> None:
        response = client.api.connector.v1.loyalty_tiers.with_raw_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            loyalty_tiers=[
                {
                    "code": "P1",
                    "loyalty_program_id": "8ddea57b-6a5c-4eec-8c4c-24467dce118e",
                    "name": "Platinum",
                    "ordering": 1,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        loyalty_tier = response.parse()
        assert_matches_type(LoyaltyTierResult, loyalty_tier, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_add(self, client: Pymews) -> None:
        with client.api.connector.v1.loyalty_tiers.with_streaming_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            loyalty_tiers=[
                {
                    "code": "P1",
                    "loyalty_program_id": "8ddea57b-6a5c-4eec-8c4c-24467dce118e",
                    "name": "Platinum",
                    "ordering": 1,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            loyalty_tier = response.parse()
            assert_matches_type(LoyaltyTierResult, loyalty_tier, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLoyaltyTiers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncPymews) -> None:
        loyalty_tier = await async_client.api.connector.v1.loyalty_tiers.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            loyalty_tier_updates=[{"loyalty_tier_id": "a58ff7cb-77e3-495a-bd61-aecf00a3f19d"}],
        )
        assert_matches_type(LoyaltyTierResult, loyalty_tier, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.loyalty_tiers.with_raw_response.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            loyalty_tier_updates=[{"loyalty_tier_id": "a58ff7cb-77e3-495a-bd61-aecf00a3f19d"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        loyalty_tier = await response.parse()
        assert_matches_type(LoyaltyTierResult, loyalty_tier, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.loyalty_tiers.with_streaming_response.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            loyalty_tier_updates=[{"loyalty_tier_id": "a58ff7cb-77e3-495a-bd61-aecf00a3f19d"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            loyalty_tier = await response.parse()
            assert_matches_type(LoyaltyTierResult, loyalty_tier, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncPymews) -> None:
        loyalty_tier = await async_client.api.connector.v1.loyalty_tiers.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            loyalty_program_ids=["3ed9e2f3-4bba-4df6-8d41-ab1b009b6425", "8a98965a-7c03-48a1-a28c-ab1b009b53c8"],
        )
        assert_matches_type(LoyaltyTierResult, loyalty_tier, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPymews) -> None:
        loyalty_tier = await async_client.api.connector.v1.loyalty_tiers.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            loyalty_program_ids=["3ed9e2f3-4bba-4df6-8d41-ab1b009b6425", "8a98965a-7c03-48a1-a28c-ab1b009b53c8"],
            activity_states=["Active"],
            chain_ids=["1df21f06-0cfc-4960-9c58-a3bf1261663e", "5fcd1933-22f2-40b9-84da-7db04cbecec2"],
            limitation={
                "count": 100,
                "cursor": "e7f26210-10e7-462e-9da8-ae8300be8ab7",
            },
            loyalty_tier_ids=["a6738390-c241-45b7-8e46-14f47207abe5", "435d4d5f-d14f-48dc-a47e-0481fc28ead0"],
            updated_utc={
                "end_utc": parse_datetime("2022-10-17T00:00:00Z"),
                "start_utc": parse_datetime("2022-10-10T00:00:00Z"),
            },
        )
        assert_matches_type(LoyaltyTierResult, loyalty_tier, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.loyalty_tiers.with_raw_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            loyalty_program_ids=["3ed9e2f3-4bba-4df6-8d41-ab1b009b6425", "8a98965a-7c03-48a1-a28c-ab1b009b53c8"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        loyalty_tier = await response.parse()
        assert_matches_type(LoyaltyTierResult, loyalty_tier, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.loyalty_tiers.with_streaming_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            loyalty_program_ids=["3ed9e2f3-4bba-4df6-8d41-ab1b009b6425", "8a98965a-7c03-48a1-a28c-ab1b009b53c8"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            loyalty_tier = await response.parse()
            assert_matches_type(LoyaltyTierResult, loyalty_tier, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncPymews) -> None:
        loyalty_tier = await async_client.api.connector.v1.loyalty_tiers.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            loyalty_tier_ids=["a58ff7cb-77e3-495a-bd61-aecf00a3f19d", "da34b396-41f7-47f6-8847-aecf00a3f19e"],
        )
        assert_matches_type(object, loyalty_tier, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.loyalty_tiers.with_raw_response.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            loyalty_tier_ids=["a58ff7cb-77e3-495a-bd61-aecf00a3f19d", "da34b396-41f7-47f6-8847-aecf00a3f19e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        loyalty_tier = await response.parse()
        assert_matches_type(object, loyalty_tier, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.loyalty_tiers.with_streaming_response.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            loyalty_tier_ids=["a58ff7cb-77e3-495a-bd61-aecf00a3f19d", "da34b396-41f7-47f6-8847-aecf00a3f19e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            loyalty_tier = await response.parse()
            assert_matches_type(object, loyalty_tier, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_add(self, async_client: AsyncPymews) -> None:
        loyalty_tier = await async_client.api.connector.v1.loyalty_tiers.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            loyalty_tiers=[
                {
                    "code": "P1",
                    "loyalty_program_id": "8ddea57b-6a5c-4eec-8c4c-24467dce118e",
                    "name": "Platinum",
                    "ordering": 1,
                }
            ],
        )
        assert_matches_type(LoyaltyTierResult, loyalty_tier, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_add_with_all_params(self, async_client: AsyncPymews) -> None:
        loyalty_tier = await async_client.api.connector.v1.loyalty_tiers.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            loyalty_tiers=[
                {
                    "code": "P1",
                    "loyalty_program_id": "8ddea57b-6a5c-4eec-8c4c-24467dce118e",
                    "name": "Platinum",
                    "ordering": 1,
                }
            ],
            chain_id="1df21f06-0cfc-4960-9c58-a3bf1261663e",
        )
        assert_matches_type(LoyaltyTierResult, loyalty_tier, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.loyalty_tiers.with_raw_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            loyalty_tiers=[
                {
                    "code": "P1",
                    "loyalty_program_id": "8ddea57b-6a5c-4eec-8c4c-24467dce118e",
                    "name": "Platinum",
                    "ordering": 1,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        loyalty_tier = await response.parse()
        assert_matches_type(LoyaltyTierResult, loyalty_tier, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.loyalty_tiers.with_streaming_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            loyalty_tiers=[
                {
                    "code": "P1",
                    "loyalty_program_id": "8ddea57b-6a5c-4eec-8c4c-24467dce118e",
                    "name": "Platinum",
                    "ordering": 1,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            loyalty_tier = await response.parse()
            assert_matches_type(LoyaltyTierResult, loyalty_tier, path=["response"])

        assert cast(Any, response.is_closed) is True
