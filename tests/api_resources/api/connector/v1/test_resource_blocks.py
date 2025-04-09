# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pymews import Pymews, AsyncPymews
from tests.utils import assert_matches_type
from pymews._utils import parse_datetime
from pymews.types.api.connector.v1 import (
    ResourceBlockResult,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestResourceBlocks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Pymews) -> None:
        resource_block = client.api.connector.v1.resource_blocks.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            extent={},
            limitation={"count": 10},
        )
        assert_matches_type(ResourceBlockResult, resource_block, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Pymews) -> None:
        resource_block = client.api.connector.v1.resource_blocks.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            extent={"inactive": True},
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            assigned_resource_ids=["b64f088d-49b5-4d5f-9766-2e27c4b75e27"],
            colliding_utc={
                "end_utc": parse_datetime("2020-01-30T00:00:00Z"),
                "start_utc": parse_datetime("2020-01-25T00:00:00Z"),
            },
            created_utc={
                "end_utc": parse_datetime("2020-01-10T00:00:00Z"),
                "start_utc": parse_datetime("2020-01-05T00:00:00Z"),
            },
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            resource_block_ids=["c478f1b3-7edb-4ccc-8f07-dd32fae1ca70"],
            updated_utc={
                "end_utc": parse_datetime("2020-01-20T00:00:00Z"),
                "start_utc": parse_datetime("2020-01-15T00:00:00Z"),
            },
        )
        assert_matches_type(ResourceBlockResult, resource_block, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Pymews) -> None:
        response = client.api.connector.v1.resource_blocks.with_raw_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            extent={},
            limitation={"count": 10},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resource_block = response.parse()
        assert_matches_type(ResourceBlockResult, resource_block, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Pymews) -> None:
        with client.api.connector.v1.resource_blocks.with_streaming_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            extent={},
            limitation={"count": 10},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resource_block = response.parse()
            assert_matches_type(ResourceBlockResult, resource_block, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Pymews) -> None:
        resource_block = client.api.connector.v1.resource_blocks.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            resource_block_ids=["bf1e10b7-8a03-4675-9e27-05fc84312a58", "e8fb6bfb-d64a-4e7c-acfe-ab0400d01183"],
        )
        assert_matches_type(object, resource_block, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Pymews) -> None:
        response = client.api.connector.v1.resource_blocks.with_raw_response.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            resource_block_ids=["bf1e10b7-8a03-4675-9e27-05fc84312a58", "e8fb6bfb-d64a-4e7c-acfe-ab0400d01183"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resource_block = response.parse()
        assert_matches_type(object, resource_block, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Pymews) -> None:
        with client.api.connector.v1.resource_blocks.with_streaming_response.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            resource_block_ids=["bf1e10b7-8a03-4675-9e27-05fc84312a58", "e8fb6bfb-d64a-4e7c-acfe-ab0400d01183"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resource_block = response.parse()
            assert_matches_type(object, resource_block, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_add(self, client: Pymews) -> None:
        resource_block = client.api.connector.v1.resource_blocks.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            resource_blocks=[
                {
                    "end_utc": parse_datetime("2019-10-20T10:00:00Z"),
                    "name": "Resource block 1",
                    "resource_id": "0d71d44e-3d85-4506-9b6f-aab500b69c52",
                    "start_utc": parse_datetime("2019-10-15T10:00:00Z"),
                    "type": "OutOfOrder",
                },
                {
                    "end_utc": parse_datetime("2019-10-20T10:00:00Z"),
                    "name": "Resource block 2",
                    "resource_id": "f7c4b4f5-ac83-4977-a41a-63d27cc6e3e9",
                    "start_utc": parse_datetime("2019-10-15T10:00:00Z"),
                    "type": "InternalUse",
                },
            ],
        )
        assert_matches_type(ResourceBlockResult, resource_block, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_add(self, client: Pymews) -> None:
        response = client.api.connector.v1.resource_blocks.with_raw_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            resource_blocks=[
                {
                    "end_utc": parse_datetime("2019-10-20T10:00:00Z"),
                    "name": "Resource block 1",
                    "resource_id": "0d71d44e-3d85-4506-9b6f-aab500b69c52",
                    "start_utc": parse_datetime("2019-10-15T10:00:00Z"),
                    "type": "OutOfOrder",
                },
                {
                    "end_utc": parse_datetime("2019-10-20T10:00:00Z"),
                    "name": "Resource block 2",
                    "resource_id": "f7c4b4f5-ac83-4977-a41a-63d27cc6e3e9",
                    "start_utc": parse_datetime("2019-10-15T10:00:00Z"),
                    "type": "InternalUse",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resource_block = response.parse()
        assert_matches_type(ResourceBlockResult, resource_block, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_add(self, client: Pymews) -> None:
        with client.api.connector.v1.resource_blocks.with_streaming_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            resource_blocks=[
                {
                    "end_utc": parse_datetime("2019-10-20T10:00:00Z"),
                    "name": "Resource block 1",
                    "resource_id": "0d71d44e-3d85-4506-9b6f-aab500b69c52",
                    "start_utc": parse_datetime("2019-10-15T10:00:00Z"),
                    "type": "OutOfOrder",
                },
                {
                    "end_utc": parse_datetime("2019-10-20T10:00:00Z"),
                    "name": "Resource block 2",
                    "resource_id": "f7c4b4f5-ac83-4977-a41a-63d27cc6e3e9",
                    "start_utc": parse_datetime("2019-10-15T10:00:00Z"),
                    "type": "InternalUse",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resource_block = response.parse()
            assert_matches_type(ResourceBlockResult, resource_block, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncResourceBlocks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncPymews) -> None:
        resource_block = await async_client.api.connector.v1.resource_blocks.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            extent={},
            limitation={"count": 10},
        )
        assert_matches_type(ResourceBlockResult, resource_block, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPymews) -> None:
        resource_block = await async_client.api.connector.v1.resource_blocks.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            extent={"inactive": True},
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            assigned_resource_ids=["b64f088d-49b5-4d5f-9766-2e27c4b75e27"],
            colliding_utc={
                "end_utc": parse_datetime("2020-01-30T00:00:00Z"),
                "start_utc": parse_datetime("2020-01-25T00:00:00Z"),
            },
            created_utc={
                "end_utc": parse_datetime("2020-01-10T00:00:00Z"),
                "start_utc": parse_datetime("2020-01-05T00:00:00Z"),
            },
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            resource_block_ids=["c478f1b3-7edb-4ccc-8f07-dd32fae1ca70"],
            updated_utc={
                "end_utc": parse_datetime("2020-01-20T00:00:00Z"),
                "start_utc": parse_datetime("2020-01-15T00:00:00Z"),
            },
        )
        assert_matches_type(ResourceBlockResult, resource_block, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.resource_blocks.with_raw_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            extent={},
            limitation={"count": 10},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resource_block = await response.parse()
        assert_matches_type(ResourceBlockResult, resource_block, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.resource_blocks.with_streaming_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            extent={},
            limitation={"count": 10},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resource_block = await response.parse()
            assert_matches_type(ResourceBlockResult, resource_block, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncPymews) -> None:
        resource_block = await async_client.api.connector.v1.resource_blocks.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            resource_block_ids=["bf1e10b7-8a03-4675-9e27-05fc84312a58", "e8fb6bfb-d64a-4e7c-acfe-ab0400d01183"],
        )
        assert_matches_type(object, resource_block, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.resource_blocks.with_raw_response.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            resource_block_ids=["bf1e10b7-8a03-4675-9e27-05fc84312a58", "e8fb6bfb-d64a-4e7c-acfe-ab0400d01183"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resource_block = await response.parse()
        assert_matches_type(object, resource_block, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.resource_blocks.with_streaming_response.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            resource_block_ids=["bf1e10b7-8a03-4675-9e27-05fc84312a58", "e8fb6bfb-d64a-4e7c-acfe-ab0400d01183"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resource_block = await response.parse()
            assert_matches_type(object, resource_block, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_add(self, async_client: AsyncPymews) -> None:
        resource_block = await async_client.api.connector.v1.resource_blocks.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            resource_blocks=[
                {
                    "end_utc": parse_datetime("2019-10-20T10:00:00Z"),
                    "name": "Resource block 1",
                    "resource_id": "0d71d44e-3d85-4506-9b6f-aab500b69c52",
                    "start_utc": parse_datetime("2019-10-15T10:00:00Z"),
                    "type": "OutOfOrder",
                },
                {
                    "end_utc": parse_datetime("2019-10-20T10:00:00Z"),
                    "name": "Resource block 2",
                    "resource_id": "f7c4b4f5-ac83-4977-a41a-63d27cc6e3e9",
                    "start_utc": parse_datetime("2019-10-15T10:00:00Z"),
                    "type": "InternalUse",
                },
            ],
        )
        assert_matches_type(ResourceBlockResult, resource_block, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.resource_blocks.with_raw_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            resource_blocks=[
                {
                    "end_utc": parse_datetime("2019-10-20T10:00:00Z"),
                    "name": "Resource block 1",
                    "resource_id": "0d71d44e-3d85-4506-9b6f-aab500b69c52",
                    "start_utc": parse_datetime("2019-10-15T10:00:00Z"),
                    "type": "OutOfOrder",
                },
                {
                    "end_utc": parse_datetime("2019-10-20T10:00:00Z"),
                    "name": "Resource block 2",
                    "resource_id": "f7c4b4f5-ac83-4977-a41a-63d27cc6e3e9",
                    "start_utc": parse_datetime("2019-10-15T10:00:00Z"),
                    "type": "InternalUse",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resource_block = await response.parse()
        assert_matches_type(ResourceBlockResult, resource_block, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.resource_blocks.with_streaming_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            resource_blocks=[
                {
                    "end_utc": parse_datetime("2019-10-20T10:00:00Z"),
                    "name": "Resource block 1",
                    "resource_id": "0d71d44e-3d85-4506-9b6f-aab500b69c52",
                    "start_utc": parse_datetime("2019-10-15T10:00:00Z"),
                    "type": "OutOfOrder",
                },
                {
                    "end_utc": parse_datetime("2019-10-20T10:00:00Z"),
                    "name": "Resource block 2",
                    "resource_id": "f7c4b4f5-ac83-4977-a41a-63d27cc6e3e9",
                    "start_utc": parse_datetime("2019-10-15T10:00:00Z"),
                    "type": "InternalUse",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resource_block = await response.parse()
            assert_matches_type(ResourceBlockResult, resource_block, path=["response"])

        assert cast(Any, response.is_closed) is True
