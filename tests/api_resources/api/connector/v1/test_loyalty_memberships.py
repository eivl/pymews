# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pymews import Pymews, AsyncPymews
from tests.utils import assert_matches_type
from pymews._utils import parse_date, parse_datetime
from pymews.types.api.connector.v1 import (
    LoyaltyMembershipResult,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLoyaltyMemberships:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Pymews) -> None:
        loyalty_membership = client.api.connector.v1.loyalty_memberships.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            loyalty_membership_updates=[{"loyalty_membership_id": "f9e434a3-720c-4820-b82e-202cb2efa2fd"}],
        )
        assert_matches_type(LoyaltyMembershipResult, loyalty_membership, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Pymews) -> None:
        loyalty_membership = client.api.connector.v1.loyalty_memberships.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            loyalty_membership_updates=[
                {
                    "loyalty_membership_id": "f9e434a3-720c-4820-b82e-202cb2efa2fd",
                    "code": {"value": "Value"},
                    "expiration_date": {"value": "2030-12-31"},
                    "is_primary": {"value": True},
                    "loyalty_program_id": {"value": "3ed9e2f3-4bba-4df6-8d41-ab1b009b6425"},
                    "loyalty_tier_id": {"value": "34c29a01-c075-49e4-906a-3b1d4012463e"},
                    "points": {"value": 0},
                    "state": {"value": "Canceled"},
                    "url": {"value": "https://www.mews.com/"},
                }
            ],
            chain_id="1df21f06-0cfc-4960-9c58-a3bf1261663e",
        )
        assert_matches_type(LoyaltyMembershipResult, loyalty_membership, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Pymews) -> None:
        response = client.api.connector.v1.loyalty_memberships.with_raw_response.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            loyalty_membership_updates=[{"loyalty_membership_id": "f9e434a3-720c-4820-b82e-202cb2efa2fd"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        loyalty_membership = response.parse()
        assert_matches_type(LoyaltyMembershipResult, loyalty_membership, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Pymews) -> None:
        with client.api.connector.v1.loyalty_memberships.with_streaming_response.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            loyalty_membership_updates=[{"loyalty_membership_id": "f9e434a3-720c-4820-b82e-202cb2efa2fd"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            loyalty_membership = response.parse()
            assert_matches_type(LoyaltyMembershipResult, loyalty_membership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Pymews) -> None:
        loyalty_membership = client.api.connector.v1.loyalty_memberships.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 100},
        )
        assert_matches_type(LoyaltyMembershipResult, loyalty_membership, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Pymews) -> None:
        loyalty_membership = client.api.connector.v1.loyalty_memberships.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 100,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            account_ids=["87d4c7c4-4832-4341-8b54-e45c1a73df34", "0ed43ab7-4592-4c99-906a-426588de1c00"],
            activity_states=["Active"],
            chain_ids=["1df21f06-0cfc-4960-9c58-a3bf1261663e", "5fcd1933-22f2-40b9-84da-7db04cbecec2"],
            codes=["string"],
            created_utc={
                "end_utc": parse_datetime("2022-10-20T00:00:00Z"),
                "start_utc": parse_datetime("2022-10-15T00:00:00Z"),
            },
            loyalty_membership_ids=["3f4d9db2-9910-4a63-b9f0-e94a13fab9ac", "ea7da00f-fdc9-4014-b0f7-71003b87e3d0"],
            loyalty_program_ids=["3ed9e2f3-4bba-4df6-8d41-ab1b009b6425", "8a98965a-7c03-48a1-a28c-ab1b009b53c8"],
            membership_states=["New", "Enrolled"],
            updated_utc={
                "end_utc": parse_datetime("2022-10-20T00:00:00Z"),
                "start_utc": parse_datetime("2022-10-15T00:00:00Z"),
            },
        )
        assert_matches_type(LoyaltyMembershipResult, loyalty_membership, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Pymews) -> None:
        response = client.api.connector.v1.loyalty_memberships.with_raw_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 100},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        loyalty_membership = response.parse()
        assert_matches_type(LoyaltyMembershipResult, loyalty_membership, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Pymews) -> None:
        with client.api.connector.v1.loyalty_memberships.with_streaming_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 100},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            loyalty_membership = response.parse()
            assert_matches_type(LoyaltyMembershipResult, loyalty_membership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Pymews) -> None:
        loyalty_membership = client.api.connector.v1.loyalty_memberships.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            loyalty_membership_ids=["f9e434a3-720c-4820-b82e-202cb2efa2fd"],
        )
        assert_matches_type(object, loyalty_membership, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Pymews) -> None:
        response = client.api.connector.v1.loyalty_memberships.with_raw_response.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            loyalty_membership_ids=["f9e434a3-720c-4820-b82e-202cb2efa2fd"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        loyalty_membership = response.parse()
        assert_matches_type(object, loyalty_membership, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Pymews) -> None:
        with client.api.connector.v1.loyalty_memberships.with_streaming_response.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            loyalty_membership_ids=["f9e434a3-720c-4820-b82e-202cb2efa2fd"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            loyalty_membership = response.parse()
            assert_matches_type(object, loyalty_membership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_add(self, client: Pymews) -> None:
        loyalty_membership = client.api.connector.v1.loyalty_memberships.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            loyalty_memberships=[
                {
                    "account_id": "87d4c7c4-4832-4341-8b54-e45c1a73df34",
                    "is_primary": True,
                    "loyalty_program_id": "3ed9e2f3-4bba-4df6-8d41-ab1b009b6425",
                }
            ],
        )
        assert_matches_type(LoyaltyMembershipResult, loyalty_membership, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_add_with_all_params(self, client: Pymews) -> None:
        loyalty_membership = client.api.connector.v1.loyalty_memberships.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            loyalty_memberships=[
                {
                    "account_id": "87d4c7c4-4832-4341-8b54-e45c1a73df34",
                    "is_primary": True,
                    "loyalty_program_id": "3ed9e2f3-4bba-4df6-8d41-ab1b009b6425",
                    "code": "Code-003",
                    "expiration_date": parse_date("2022-12-31"),
                    "loyalty_tier_id": "34c29a01-c075-49e4-906a-3b1d4012463e",
                    "points": 5,
                    "state": "New",
                    "url": "",
                }
            ],
            chain_id="1df21f06-0cfc-4960-9c58-a3bf1261663e",
        )
        assert_matches_type(LoyaltyMembershipResult, loyalty_membership, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_add(self, client: Pymews) -> None:
        response = client.api.connector.v1.loyalty_memberships.with_raw_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            loyalty_memberships=[
                {
                    "account_id": "87d4c7c4-4832-4341-8b54-e45c1a73df34",
                    "is_primary": True,
                    "loyalty_program_id": "3ed9e2f3-4bba-4df6-8d41-ab1b009b6425",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        loyalty_membership = response.parse()
        assert_matches_type(LoyaltyMembershipResult, loyalty_membership, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_add(self, client: Pymews) -> None:
        with client.api.connector.v1.loyalty_memberships.with_streaming_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            loyalty_memberships=[
                {
                    "account_id": "87d4c7c4-4832-4341-8b54-e45c1a73df34",
                    "is_primary": True,
                    "loyalty_program_id": "3ed9e2f3-4bba-4df6-8d41-ab1b009b6425",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            loyalty_membership = response.parse()
            assert_matches_type(LoyaltyMembershipResult, loyalty_membership, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLoyaltyMemberships:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncPymews) -> None:
        loyalty_membership = await async_client.api.connector.v1.loyalty_memberships.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            loyalty_membership_updates=[{"loyalty_membership_id": "f9e434a3-720c-4820-b82e-202cb2efa2fd"}],
        )
        assert_matches_type(LoyaltyMembershipResult, loyalty_membership, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncPymews) -> None:
        loyalty_membership = await async_client.api.connector.v1.loyalty_memberships.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            loyalty_membership_updates=[
                {
                    "loyalty_membership_id": "f9e434a3-720c-4820-b82e-202cb2efa2fd",
                    "code": {"value": "Value"},
                    "expiration_date": {"value": "2030-12-31"},
                    "is_primary": {"value": True},
                    "loyalty_program_id": {"value": "3ed9e2f3-4bba-4df6-8d41-ab1b009b6425"},
                    "loyalty_tier_id": {"value": "34c29a01-c075-49e4-906a-3b1d4012463e"},
                    "points": {"value": 0},
                    "state": {"value": "Canceled"},
                    "url": {"value": "https://www.mews.com/"},
                }
            ],
            chain_id="1df21f06-0cfc-4960-9c58-a3bf1261663e",
        )
        assert_matches_type(LoyaltyMembershipResult, loyalty_membership, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.loyalty_memberships.with_raw_response.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            loyalty_membership_updates=[{"loyalty_membership_id": "f9e434a3-720c-4820-b82e-202cb2efa2fd"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        loyalty_membership = await response.parse()
        assert_matches_type(LoyaltyMembershipResult, loyalty_membership, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.loyalty_memberships.with_streaming_response.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            loyalty_membership_updates=[{"loyalty_membership_id": "f9e434a3-720c-4820-b82e-202cb2efa2fd"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            loyalty_membership = await response.parse()
            assert_matches_type(LoyaltyMembershipResult, loyalty_membership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncPymews) -> None:
        loyalty_membership = await async_client.api.connector.v1.loyalty_memberships.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 100},
        )
        assert_matches_type(LoyaltyMembershipResult, loyalty_membership, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPymews) -> None:
        loyalty_membership = await async_client.api.connector.v1.loyalty_memberships.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 100,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            account_ids=["87d4c7c4-4832-4341-8b54-e45c1a73df34", "0ed43ab7-4592-4c99-906a-426588de1c00"],
            activity_states=["Active"],
            chain_ids=["1df21f06-0cfc-4960-9c58-a3bf1261663e", "5fcd1933-22f2-40b9-84da-7db04cbecec2"],
            codes=["string"],
            created_utc={
                "end_utc": parse_datetime("2022-10-20T00:00:00Z"),
                "start_utc": parse_datetime("2022-10-15T00:00:00Z"),
            },
            loyalty_membership_ids=["3f4d9db2-9910-4a63-b9f0-e94a13fab9ac", "ea7da00f-fdc9-4014-b0f7-71003b87e3d0"],
            loyalty_program_ids=["3ed9e2f3-4bba-4df6-8d41-ab1b009b6425", "8a98965a-7c03-48a1-a28c-ab1b009b53c8"],
            membership_states=["New", "Enrolled"],
            updated_utc={
                "end_utc": parse_datetime("2022-10-20T00:00:00Z"),
                "start_utc": parse_datetime("2022-10-15T00:00:00Z"),
            },
        )
        assert_matches_type(LoyaltyMembershipResult, loyalty_membership, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.loyalty_memberships.with_raw_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 100},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        loyalty_membership = await response.parse()
        assert_matches_type(LoyaltyMembershipResult, loyalty_membership, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.loyalty_memberships.with_streaming_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 100},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            loyalty_membership = await response.parse()
            assert_matches_type(LoyaltyMembershipResult, loyalty_membership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncPymews) -> None:
        loyalty_membership = await async_client.api.connector.v1.loyalty_memberships.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            loyalty_membership_ids=["f9e434a3-720c-4820-b82e-202cb2efa2fd"],
        )
        assert_matches_type(object, loyalty_membership, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.loyalty_memberships.with_raw_response.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            loyalty_membership_ids=["f9e434a3-720c-4820-b82e-202cb2efa2fd"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        loyalty_membership = await response.parse()
        assert_matches_type(object, loyalty_membership, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.loyalty_memberships.with_streaming_response.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            loyalty_membership_ids=["f9e434a3-720c-4820-b82e-202cb2efa2fd"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            loyalty_membership = await response.parse()
            assert_matches_type(object, loyalty_membership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_add(self, async_client: AsyncPymews) -> None:
        loyalty_membership = await async_client.api.connector.v1.loyalty_memberships.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            loyalty_memberships=[
                {
                    "account_id": "87d4c7c4-4832-4341-8b54-e45c1a73df34",
                    "is_primary": True,
                    "loyalty_program_id": "3ed9e2f3-4bba-4df6-8d41-ab1b009b6425",
                }
            ],
        )
        assert_matches_type(LoyaltyMembershipResult, loyalty_membership, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_add_with_all_params(self, async_client: AsyncPymews) -> None:
        loyalty_membership = await async_client.api.connector.v1.loyalty_memberships.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            loyalty_memberships=[
                {
                    "account_id": "87d4c7c4-4832-4341-8b54-e45c1a73df34",
                    "is_primary": True,
                    "loyalty_program_id": "3ed9e2f3-4bba-4df6-8d41-ab1b009b6425",
                    "code": "Code-003",
                    "expiration_date": parse_date("2022-12-31"),
                    "loyalty_tier_id": "34c29a01-c075-49e4-906a-3b1d4012463e",
                    "points": 5,
                    "state": "New",
                    "url": "",
                }
            ],
            chain_id="1df21f06-0cfc-4960-9c58-a3bf1261663e",
        )
        assert_matches_type(LoyaltyMembershipResult, loyalty_membership, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.loyalty_memberships.with_raw_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            loyalty_memberships=[
                {
                    "account_id": "87d4c7c4-4832-4341-8b54-e45c1a73df34",
                    "is_primary": True,
                    "loyalty_program_id": "3ed9e2f3-4bba-4df6-8d41-ab1b009b6425",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        loyalty_membership = await response.parse()
        assert_matches_type(LoyaltyMembershipResult, loyalty_membership, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.loyalty_memberships.with_streaming_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            loyalty_memberships=[
                {
                    "account_id": "87d4c7c4-4832-4341-8b54-e45c1a73df34",
                    "is_primary": True,
                    "loyalty_program_id": "3ed9e2f3-4bba-4df6-8d41-ab1b009b6425",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            loyalty_membership = await response.parse()
            assert_matches_type(LoyaltyMembershipResult, loyalty_membership, path=["response"])

        assert cast(Any, response.is_closed) is True
