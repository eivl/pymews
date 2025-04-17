# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pymews import Pymews, AsyncPymews
from tests.utils import assert_matches_type
from pymews._utils import parse_datetime
from pymews.types.api.connector.v1 import ResourceListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestResources:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Pymews) -> None:
        resource = client.api.connector.v1.resources.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            resource_updates=[{"resource_id": "5ee074b1-6c86-48e8-915f-c7aa4702086f"}],
        )
        assert_matches_type(object, resource, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Pymews) -> None:
        response = client.api.connector.v1.resources.with_raw_response.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            resource_updates=[{"resource_id": "5ee074b1-6c86-48e8-915f-c7aa4702086f"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resource = response.parse()
        assert_matches_type(object, resource, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Pymews) -> None:
        with client.api.connector.v1.resources.with_streaming_response.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            resource_updates=[{"resource_id": "5ee074b1-6c86-48e8-915f-c7aa4702086f"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resource = response.parse()
            assert_matches_type(object, resource, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Pymews) -> None:
        resource = client.api.connector.v1.resources.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )
        assert_matches_type(ResourceListResponse, resource, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Pymews) -> None:
        resource = client.api.connector.v1.resources.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            created_utc={
                "end_utc": parse_datetime("2022-10-20T00:00:00Z"),
                "start_utc": parse_datetime("2022-10-15T00:00:00Z"),
            },
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            extent={
                "inactive": False,
                "resource_categories": False,
                "resource_category_assignments": False,
                "resource_category_image_assignments": False,
                "resource_feature_assignments": False,
                "resource_features": False,
                "resources": True,
            },
            names=["string"],
            resource_ids=["5ee074b1-6c86-48e8-915f-c7aa4702086f", "c32386aa-1cd2-414a-a823-489325842fbe"],
            updated_utc={
                "end_utc": parse_datetime("2022-10-20T00:00:00Z"),
                "start_utc": parse_datetime("2022-10-15T00:00:00Z"),
            },
        )
        assert_matches_type(ResourceListResponse, resource, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Pymews) -> None:
        response = client.api.connector.v1.resources.with_raw_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resource = response.parse()
        assert_matches_type(ResourceListResponse, resource, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Pymews) -> None:
        with client.api.connector.v1.resources.with_streaming_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resource = response.parse()
            assert_matches_type(ResourceListResponse, resource, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncResources:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncPymews) -> None:
        resource = await async_client.api.connector.v1.resources.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            resource_updates=[{"resource_id": "5ee074b1-6c86-48e8-915f-c7aa4702086f"}],
        )
        assert_matches_type(object, resource, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.resources.with_raw_response.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            resource_updates=[{"resource_id": "5ee074b1-6c86-48e8-915f-c7aa4702086f"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resource = await response.parse()
        assert_matches_type(object, resource, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.resources.with_streaming_response.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            resource_updates=[{"resource_id": "5ee074b1-6c86-48e8-915f-c7aa4702086f"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resource = await response.parse()
            assert_matches_type(object, resource, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncPymews) -> None:
        resource = await async_client.api.connector.v1.resources.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )
        assert_matches_type(ResourceListResponse, resource, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPymews) -> None:
        resource = await async_client.api.connector.v1.resources.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            created_utc={
                "end_utc": parse_datetime("2022-10-20T00:00:00Z"),
                "start_utc": parse_datetime("2022-10-15T00:00:00Z"),
            },
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            extent={
                "inactive": False,
                "resource_categories": False,
                "resource_category_assignments": False,
                "resource_category_image_assignments": False,
                "resource_feature_assignments": False,
                "resource_features": False,
                "resources": True,
            },
            names=["string"],
            resource_ids=["5ee074b1-6c86-48e8-915f-c7aa4702086f", "c32386aa-1cd2-414a-a823-489325842fbe"],
            updated_utc={
                "end_utc": parse_datetime("2022-10-20T00:00:00Z"),
                "start_utc": parse_datetime("2022-10-15T00:00:00Z"),
            },
        )
        assert_matches_type(ResourceListResponse, resource, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.resources.with_raw_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resource = await response.parse()
        assert_matches_type(ResourceListResponse, resource, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.resources.with_streaming_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resource = await response.parse()
            assert_matches_type(ResourceListResponse, resource, path=["response"])

        assert cast(Any, response.is_closed) is True
