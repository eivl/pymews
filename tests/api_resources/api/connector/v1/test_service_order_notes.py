# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pymews import Pymews, AsyncPymews
from tests.utils import assert_matches_type
from pymews._utils import parse_datetime
from pymews.types.api.connector.v1 import (
    ServiceOrderNoteAddResponse,
    ServiceOrderNoteListResponse,
    ServiceOrderNoteUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestServiceOrderNotes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Pymews) -> None:
        service_order_note = client.api.connector.v1.service_order_notes.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            service_order_note_updates=[{"service_order_note_id": "a06a225b-00f7-48c8-a463-af5c016768e9"}],
        )
        assert_matches_type(ServiceOrderNoteUpdateResponse, service_order_note, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Pymews) -> None:
        response = client.api.connector.v1.service_order_notes.with_raw_response.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            service_order_note_updates=[{"service_order_note_id": "a06a225b-00f7-48c8-a463-af5c016768e9"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service_order_note = response.parse()
        assert_matches_type(ServiceOrderNoteUpdateResponse, service_order_note, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Pymews) -> None:
        with client.api.connector.v1.service_order_notes.with_streaming_response.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            service_order_note_updates=[{"service_order_note_id": "a06a225b-00f7-48c8-a463-af5c016768e9"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service_order_note = response.parse()
            assert_matches_type(ServiceOrderNoteUpdateResponse, service_order_note, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Pymews) -> None:
        service_order_note = client.api.connector.v1.service_order_notes.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 100},
            service_order_ids=["1dc0c6bf-2ce6-4a9f-af97-af5c01676720"],
        )
        assert_matches_type(ServiceOrderNoteListResponse, service_order_note, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Pymews) -> None:
        service_order_note = client.api.connector.v1.service_order_notes.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 100,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            service_order_ids=["1dc0c6bf-2ce6-4a9f-af97-af5c01676720"],
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            service_order_note_ids=["a06a225b-00f7-48c8-a463-af5c016768e9"],
            types=["General"],
            updated_utc={
                "end_utc": parse_datetime("2019-12-27T18:11:19.117Z"),
                "start_utc": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
        )
        assert_matches_type(ServiceOrderNoteListResponse, service_order_note, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Pymews) -> None:
        response = client.api.connector.v1.service_order_notes.with_raw_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 100},
            service_order_ids=["1dc0c6bf-2ce6-4a9f-af97-af5c01676720"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service_order_note = response.parse()
        assert_matches_type(ServiceOrderNoteListResponse, service_order_note, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Pymews) -> None:
        with client.api.connector.v1.service_order_notes.with_streaming_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 100},
            service_order_ids=["1dc0c6bf-2ce6-4a9f-af97-af5c01676720"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service_order_note = response.parse()
            assert_matches_type(ServiceOrderNoteListResponse, service_order_note, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Pymews) -> None:
        service_order_note = client.api.connector.v1.service_order_notes.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            service_order_note_ids=["a06a225b-00f7-48c8-a463-af5c016768e9"],
        )
        assert_matches_type(object, service_order_note, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Pymews) -> None:
        response = client.api.connector.v1.service_order_notes.with_raw_response.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            service_order_note_ids=["a06a225b-00f7-48c8-a463-af5c016768e9"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service_order_note = response.parse()
        assert_matches_type(object, service_order_note, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Pymews) -> None:
        with client.api.connector.v1.service_order_notes.with_streaming_response.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            service_order_note_ids=["a06a225b-00f7-48c8-a463-af5c016768e9"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service_order_note = response.parse()
            assert_matches_type(object, service_order_note, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_add(self, client: Pymews) -> None:
        service_order_note = client.api.connector.v1.service_order_notes.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            service_order_notes=[
                {
                    "service_order_id": "1dc0c6bf-2ce6-4a9f-af97-af5c01676720",
                    "text": "Shaken, not stirred.",
                }
            ],
        )
        assert_matches_type(ServiceOrderNoteAddResponse, service_order_note, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_add(self, client: Pymews) -> None:
        response = client.api.connector.v1.service_order_notes.with_raw_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            service_order_notes=[
                {
                    "service_order_id": "1dc0c6bf-2ce6-4a9f-af97-af5c01676720",
                    "text": "Shaken, not stirred.",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service_order_note = response.parse()
        assert_matches_type(ServiceOrderNoteAddResponse, service_order_note, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_add(self, client: Pymews) -> None:
        with client.api.connector.v1.service_order_notes.with_streaming_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            service_order_notes=[
                {
                    "service_order_id": "1dc0c6bf-2ce6-4a9f-af97-af5c01676720",
                    "text": "Shaken, not stirred.",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service_order_note = response.parse()
            assert_matches_type(ServiceOrderNoteAddResponse, service_order_note, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncServiceOrderNotes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncPymews) -> None:
        service_order_note = await async_client.api.connector.v1.service_order_notes.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            service_order_note_updates=[{"service_order_note_id": "a06a225b-00f7-48c8-a463-af5c016768e9"}],
        )
        assert_matches_type(ServiceOrderNoteUpdateResponse, service_order_note, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.service_order_notes.with_raw_response.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            service_order_note_updates=[{"service_order_note_id": "a06a225b-00f7-48c8-a463-af5c016768e9"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service_order_note = await response.parse()
        assert_matches_type(ServiceOrderNoteUpdateResponse, service_order_note, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.service_order_notes.with_streaming_response.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            service_order_note_updates=[{"service_order_note_id": "a06a225b-00f7-48c8-a463-af5c016768e9"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service_order_note = await response.parse()
            assert_matches_type(ServiceOrderNoteUpdateResponse, service_order_note, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncPymews) -> None:
        service_order_note = await async_client.api.connector.v1.service_order_notes.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 100},
            service_order_ids=["1dc0c6bf-2ce6-4a9f-af97-af5c01676720"],
        )
        assert_matches_type(ServiceOrderNoteListResponse, service_order_note, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPymews) -> None:
        service_order_note = await async_client.api.connector.v1.service_order_notes.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 100,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            service_order_ids=["1dc0c6bf-2ce6-4a9f-af97-af5c01676720"],
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            service_order_note_ids=["a06a225b-00f7-48c8-a463-af5c016768e9"],
            types=["General"],
            updated_utc={
                "end_utc": parse_datetime("2019-12-27T18:11:19.117Z"),
                "start_utc": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
        )
        assert_matches_type(ServiceOrderNoteListResponse, service_order_note, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.service_order_notes.with_raw_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 100},
            service_order_ids=["1dc0c6bf-2ce6-4a9f-af97-af5c01676720"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service_order_note = await response.parse()
        assert_matches_type(ServiceOrderNoteListResponse, service_order_note, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.service_order_notes.with_streaming_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 100},
            service_order_ids=["1dc0c6bf-2ce6-4a9f-af97-af5c01676720"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service_order_note = await response.parse()
            assert_matches_type(ServiceOrderNoteListResponse, service_order_note, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncPymews) -> None:
        service_order_note = await async_client.api.connector.v1.service_order_notes.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            service_order_note_ids=["a06a225b-00f7-48c8-a463-af5c016768e9"],
        )
        assert_matches_type(object, service_order_note, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.service_order_notes.with_raw_response.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            service_order_note_ids=["a06a225b-00f7-48c8-a463-af5c016768e9"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service_order_note = await response.parse()
        assert_matches_type(object, service_order_note, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.service_order_notes.with_streaming_response.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            service_order_note_ids=["a06a225b-00f7-48c8-a463-af5c016768e9"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service_order_note = await response.parse()
            assert_matches_type(object, service_order_note, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_add(self, async_client: AsyncPymews) -> None:
        service_order_note = await async_client.api.connector.v1.service_order_notes.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            service_order_notes=[
                {
                    "service_order_id": "1dc0c6bf-2ce6-4a9f-af97-af5c01676720",
                    "text": "Shaken, not stirred.",
                }
            ],
        )
        assert_matches_type(ServiceOrderNoteAddResponse, service_order_note, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.service_order_notes.with_raw_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            service_order_notes=[
                {
                    "service_order_id": "1dc0c6bf-2ce6-4a9f-af97-af5c01676720",
                    "text": "Shaken, not stirred.",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service_order_note = await response.parse()
        assert_matches_type(ServiceOrderNoteAddResponse, service_order_note, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.service_order_notes.with_streaming_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            service_order_notes=[
                {
                    "service_order_id": "1dc0c6bf-2ce6-4a9f-af97-af5c01676720",
                    "text": "Shaken, not stirred.",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service_order_note = await response.parse()
            assert_matches_type(ServiceOrderNoteAddResponse, service_order_note, path=["response"])

        assert cast(Any, response.is_closed) is True
