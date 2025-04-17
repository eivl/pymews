# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pymews import Pymews, AsyncPymews
from tests.utils import assert_matches_type
from pymews._utils import parse_datetime
from pymews.types.api.connector.v1 import (
    AccountNoteAddResponse,
    AccountNoteListResponse,
    AccountNoteUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccountNotes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Pymews) -> None:
        account_note = client.api.connector.v1.account_notes.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            account_note_updates=[
                {
                    "account_note_id": "a58ff7cb-77e3-495a-bd61-aecf00a3f19d",
                    "classifications": {},
                }
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )
        assert_matches_type(AccountNoteUpdateResponse, account_note, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Pymews) -> None:
        account_note = client.api.connector.v1.account_notes.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            account_note_updates=[
                {
                    "account_note_id": "a58ff7cb-77e3-495a-bd61-aecf00a3f19d",
                    "classifications": {
                        "accounting": {"value": True},
                        "complaints": {"value": True},
                        "family_relations": {"value": True},
                        "food_and_beverage": {"value": True},
                        "front_office": {"value": True},
                        "general": {"value": True},
                        "gifts": {"value": True},
                        "housekeeping": {"value": False},
                        "maintenance": {"value": True},
                        "other": {"value": True},
                        "previous_stay": {"value": True},
                        "reservations": {"value": True},
                    },
                    "content": {"value": "The AC in the room doesn't work anymore"},
                }
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            chain_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AccountNoteUpdateResponse, account_note, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Pymews) -> None:
        response = client.api.connector.v1.account_notes.with_raw_response.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            account_note_updates=[
                {
                    "account_note_id": "a58ff7cb-77e3-495a-bd61-aecf00a3f19d",
                    "classifications": {},
                }
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_note = response.parse()
        assert_matches_type(AccountNoteUpdateResponse, account_note, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Pymews) -> None:
        with client.api.connector.v1.account_notes.with_streaming_response.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            account_note_updates=[
                {
                    "account_note_id": "a58ff7cb-77e3-495a-bd61-aecf00a3f19d",
                    "classifications": {},
                }
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_note = response.parse()
            assert_matches_type(AccountNoteUpdateResponse, account_note, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Pymews) -> None:
        account_note = client.api.connector.v1.account_notes.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 100},
        )
        assert_matches_type(AccountNoteListResponse, account_note, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Pymews) -> None:
        account_note = client.api.connector.v1.account_notes.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 100,
                "cursor": "e7f26210-10e7-462e-9da8-ae8300be8ab7",
            },
            account_ids=["a6738390-c241-45b7-8e46-14f47207abe5", "435d4d5f-d14f-48dc-a47e-0481fc28ead0"],
            account_note_ids=["3ed9e2f3-4bba-4df6-8d41-ab1b009b6425", "8a98965a-7c03-48a1-a28c-ab1b009b53c8"],
            activity_states=["Active"],
            chain_ids=["1df21f06-0cfc-4960-9c58-a3bf1261663e", "5fcd1933-22f2-40b9-84da-7db04cbecec2"],
            updated_utc={
                "end_utc": parse_datetime("2022-10-17T00:00:00Z"),
                "start_utc": parse_datetime("2022-10-10T00:00:00Z"),
            },
        )
        assert_matches_type(AccountNoteListResponse, account_note, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Pymews) -> None:
        response = client.api.connector.v1.account_notes.with_raw_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 100},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_note = response.parse()
        assert_matches_type(AccountNoteListResponse, account_note, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Pymews) -> None:
        with client.api.connector.v1.account_notes.with_streaming_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 100},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_note = response.parse()
            assert_matches_type(AccountNoteListResponse, account_note, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Pymews) -> None:
        account_note = client.api.connector.v1.account_notes.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            account_note_ids=["a58ff7cb-77e3-495a-bd61-aecf00a3f19d", "da34b396-41f7-47f6-8847-aecf00a3f19e"],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )
        assert_matches_type(object, account_note, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_delete_with_all_params(self, client: Pymews) -> None:
        account_note = client.api.connector.v1.account_notes.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            account_note_ids=["a58ff7cb-77e3-495a-bd61-aecf00a3f19d", "da34b396-41f7-47f6-8847-aecf00a3f19e"],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            chain_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, account_note, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Pymews) -> None:
        response = client.api.connector.v1.account_notes.with_raw_response.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            account_note_ids=["a58ff7cb-77e3-495a-bd61-aecf00a3f19d", "da34b396-41f7-47f6-8847-aecf00a3f19e"],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_note = response.parse()
        assert_matches_type(object, account_note, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Pymews) -> None:
        with client.api.connector.v1.account_notes.with_streaming_response.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            account_note_ids=["a58ff7cb-77e3-495a-bd61-aecf00a3f19d", "da34b396-41f7-47f6-8847-aecf00a3f19e"],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_note = response.parse()
            assert_matches_type(object, account_note, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_add(self, client: Pymews) -> None:
        account_note = client.api.connector.v1.account_notes.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            account_notes=[
                {
                    "account_id": "8ddea57b-6a5c-4eec-8c4c-24467dce118e",
                    "classifications": ["FamilyRelations"],
                    "content": "Brother of the CEO",
                }
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )
        assert_matches_type(AccountNoteAddResponse, account_note, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_add_with_all_params(self, client: Pymews) -> None:
        account_note = client.api.connector.v1.account_notes.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            account_notes=[
                {
                    "account_id": "8ddea57b-6a5c-4eec-8c4c-24467dce118e",
                    "classifications": ["FamilyRelations"],
                    "content": "Brother of the CEO",
                }
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            chain_id="1df21f06-0cfc-4960-9c58-a3bf1261663e",
        )
        assert_matches_type(AccountNoteAddResponse, account_note, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_add(self, client: Pymews) -> None:
        response = client.api.connector.v1.account_notes.with_raw_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            account_notes=[
                {
                    "account_id": "8ddea57b-6a5c-4eec-8c4c-24467dce118e",
                    "classifications": ["FamilyRelations"],
                    "content": "Brother of the CEO",
                }
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_note = response.parse()
        assert_matches_type(AccountNoteAddResponse, account_note, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_add(self, client: Pymews) -> None:
        with client.api.connector.v1.account_notes.with_streaming_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            account_notes=[
                {
                    "account_id": "8ddea57b-6a5c-4eec-8c4c-24467dce118e",
                    "classifications": ["FamilyRelations"],
                    "content": "Brother of the CEO",
                }
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_note = response.parse()
            assert_matches_type(AccountNoteAddResponse, account_note, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAccountNotes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncPymews) -> None:
        account_note = await async_client.api.connector.v1.account_notes.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            account_note_updates=[
                {
                    "account_note_id": "a58ff7cb-77e3-495a-bd61-aecf00a3f19d",
                    "classifications": {},
                }
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )
        assert_matches_type(AccountNoteUpdateResponse, account_note, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncPymews) -> None:
        account_note = await async_client.api.connector.v1.account_notes.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            account_note_updates=[
                {
                    "account_note_id": "a58ff7cb-77e3-495a-bd61-aecf00a3f19d",
                    "classifications": {
                        "accounting": {"value": True},
                        "complaints": {"value": True},
                        "family_relations": {"value": True},
                        "food_and_beverage": {"value": True},
                        "front_office": {"value": True},
                        "general": {"value": True},
                        "gifts": {"value": True},
                        "housekeeping": {"value": False},
                        "maintenance": {"value": True},
                        "other": {"value": True},
                        "previous_stay": {"value": True},
                        "reservations": {"value": True},
                    },
                    "content": {"value": "The AC in the room doesn't work anymore"},
                }
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            chain_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AccountNoteUpdateResponse, account_note, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.account_notes.with_raw_response.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            account_note_updates=[
                {
                    "account_note_id": "a58ff7cb-77e3-495a-bd61-aecf00a3f19d",
                    "classifications": {},
                }
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_note = await response.parse()
        assert_matches_type(AccountNoteUpdateResponse, account_note, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.account_notes.with_streaming_response.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            account_note_updates=[
                {
                    "account_note_id": "a58ff7cb-77e3-495a-bd61-aecf00a3f19d",
                    "classifications": {},
                }
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_note = await response.parse()
            assert_matches_type(AccountNoteUpdateResponse, account_note, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncPymews) -> None:
        account_note = await async_client.api.connector.v1.account_notes.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 100},
        )
        assert_matches_type(AccountNoteListResponse, account_note, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPymews) -> None:
        account_note = await async_client.api.connector.v1.account_notes.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 100,
                "cursor": "e7f26210-10e7-462e-9da8-ae8300be8ab7",
            },
            account_ids=["a6738390-c241-45b7-8e46-14f47207abe5", "435d4d5f-d14f-48dc-a47e-0481fc28ead0"],
            account_note_ids=["3ed9e2f3-4bba-4df6-8d41-ab1b009b6425", "8a98965a-7c03-48a1-a28c-ab1b009b53c8"],
            activity_states=["Active"],
            chain_ids=["1df21f06-0cfc-4960-9c58-a3bf1261663e", "5fcd1933-22f2-40b9-84da-7db04cbecec2"],
            updated_utc={
                "end_utc": parse_datetime("2022-10-17T00:00:00Z"),
                "start_utc": parse_datetime("2022-10-10T00:00:00Z"),
            },
        )
        assert_matches_type(AccountNoteListResponse, account_note, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.account_notes.with_raw_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 100},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_note = await response.parse()
        assert_matches_type(AccountNoteListResponse, account_note, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.account_notes.with_streaming_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 100},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_note = await response.parse()
            assert_matches_type(AccountNoteListResponse, account_note, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncPymews) -> None:
        account_note = await async_client.api.connector.v1.account_notes.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            account_note_ids=["a58ff7cb-77e3-495a-bd61-aecf00a3f19d", "da34b396-41f7-47f6-8847-aecf00a3f19e"],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )
        assert_matches_type(object, account_note, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncPymews) -> None:
        account_note = await async_client.api.connector.v1.account_notes.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            account_note_ids=["a58ff7cb-77e3-495a-bd61-aecf00a3f19d", "da34b396-41f7-47f6-8847-aecf00a3f19e"],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            chain_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, account_note, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.account_notes.with_raw_response.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            account_note_ids=["a58ff7cb-77e3-495a-bd61-aecf00a3f19d", "da34b396-41f7-47f6-8847-aecf00a3f19e"],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_note = await response.parse()
        assert_matches_type(object, account_note, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.account_notes.with_streaming_response.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            account_note_ids=["a58ff7cb-77e3-495a-bd61-aecf00a3f19d", "da34b396-41f7-47f6-8847-aecf00a3f19e"],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_note = await response.parse()
            assert_matches_type(object, account_note, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_add(self, async_client: AsyncPymews) -> None:
        account_note = await async_client.api.connector.v1.account_notes.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            account_notes=[
                {
                    "account_id": "8ddea57b-6a5c-4eec-8c4c-24467dce118e",
                    "classifications": ["FamilyRelations"],
                    "content": "Brother of the CEO",
                }
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )
        assert_matches_type(AccountNoteAddResponse, account_note, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_add_with_all_params(self, async_client: AsyncPymews) -> None:
        account_note = await async_client.api.connector.v1.account_notes.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            account_notes=[
                {
                    "account_id": "8ddea57b-6a5c-4eec-8c4c-24467dce118e",
                    "classifications": ["FamilyRelations"],
                    "content": "Brother of the CEO",
                }
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            chain_id="1df21f06-0cfc-4960-9c58-a3bf1261663e",
        )
        assert_matches_type(AccountNoteAddResponse, account_note, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.account_notes.with_raw_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            account_notes=[
                {
                    "account_id": "8ddea57b-6a5c-4eec-8c4c-24467dce118e",
                    "classifications": ["FamilyRelations"],
                    "content": "Brother of the CEO",
                }
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_note = await response.parse()
        assert_matches_type(AccountNoteAddResponse, account_note, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.account_notes.with_streaming_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            account_notes=[
                {
                    "account_id": "8ddea57b-6a5c-4eec-8c4c-24467dce118e",
                    "classifications": ["FamilyRelations"],
                    "content": "Brother of the CEO",
                }
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_note = await response.parse()
            assert_matches_type(AccountNoteAddResponse, account_note, path=["response"])

        assert cast(Any, response.is_closed) is True
