# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pymews import Pymews, AsyncPymews
from tests.utils import assert_matches_type
from pymews._utils import parse_datetime
from pymews.types.api.connector.v1 import OrderItemListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOrderItems:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Pymews) -> None:
        order_item = client.api.connector.v1.order_items.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )
        assert_matches_type(OrderItemListResponse, order_item, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Pymews) -> None:
        order_item = client.api.connector.v1.order_items.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 10,
                "cursor": None,
            },
            accounting_states=["Open", "Closed"],
            bill_ids=["d27ffe99-ff92-4afb-ac03-9268f24f0556", "297de6f8-bd67-4ebd-98b6-ecc1cd8f920c"],
            canceled_utc={
                "end_utc": parse_datetime("2023-03-31T00:00:00Z"),
                "start_utc": parse_datetime("2023-03-01T00:00:00Z"),
            },
            closed_utc={
                "end_utc": parse_datetime("2023-03-31T00:00:00Z"),
                "start_utc": parse_datetime("2023-03-01T00:00:00Z"),
            },
            consumed_utc={
                "end_utc": parse_datetime("2023-03-31T00:00:00Z"),
                "start_utc": parse_datetime("2023-03-01T00:00:00Z"),
            },
            created_utc={
                "end_utc": parse_datetime("2023-03-31T00:00:00Z"),
                "start_utc": parse_datetime("2023-03-01T00:00:00Z"),
            },
            currency="EUR",
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            order_item_ids=["3e982ab5-6245-4c39-80af-1118d40e7494", "bd11dc4a-8f9e-442b-bb1e-f5361b31dfa2"],
            service_ids=["294c7859-63ba-46ad-a8bf-34fad2019383", "05089c0c-5d55-4756-827b-c4bcee1edf00"],
            service_order_ids=["ac5ef5eb-c5b2-4083-879f-83f04a5ebda5", "5d603823-b40a-43a4-8244-d5d2b515deb5"],
            types=["CityTax", "SpaceOrder"],
            updated_utc={
                "end_utc": parse_datetime("2023-03-31T00:00:00Z"),
                "start_utc": parse_datetime("2023-03-01T00:00:00Z"),
            },
        )
        assert_matches_type(OrderItemListResponse, order_item, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Pymews) -> None:
        response = client.api.connector.v1.order_items.with_raw_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order_item = response.parse()
        assert_matches_type(OrderItemListResponse, order_item, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Pymews) -> None:
        with client.api.connector.v1.order_items.with_streaming_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order_item = response.parse()
            assert_matches_type(OrderItemListResponse, order_item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_cancel(self, client: Pymews) -> None:
        order_item = client.api.connector.v1.order_items.cancel(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            order_item_ids=["f5c6b7a8-9d4f-4e2a-8a3b-2f3b8b9e6a1f", "a6b7c8d9-0e1f-4d2a-9b3c-5d6e7f8a9b0c"],
        )
        assert_matches_type(object, order_item, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_cancel_with_all_params(self, client: Pymews) -> None:
        order_item = client.api.connector.v1.order_items.cancel(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            order_item_ids=["f5c6b7a8-9d4f-4e2a-8a3b-2f3b8b9e6a1f", "a6b7c8d9-0e1f-4d2a-9b3c-5d6e7f8a9b0c"],
            enterprise_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )
        assert_matches_type(object, order_item, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_cancel(self, client: Pymews) -> None:
        response = client.api.connector.v1.order_items.with_raw_response.cancel(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            order_item_ids=["f5c6b7a8-9d4f-4e2a-8a3b-2f3b8b9e6a1f", "a6b7c8d9-0e1f-4d2a-9b3c-5d6e7f8a9b0c"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order_item = response.parse()
        assert_matches_type(object, order_item, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_cancel(self, client: Pymews) -> None:
        with client.api.connector.v1.order_items.with_streaming_response.cancel(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            order_item_ids=["f5c6b7a8-9d4f-4e2a-8a3b-2f3b8b9e6a1f", "a6b7c8d9-0e1f-4d2a-9b3c-5d6e7f8a9b0c"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order_item = response.parse()
            assert_matches_type(object, order_item, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOrderItems:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncPymews) -> None:
        order_item = await async_client.api.connector.v1.order_items.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )
        assert_matches_type(OrderItemListResponse, order_item, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPymews) -> None:
        order_item = await async_client.api.connector.v1.order_items.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 10,
                "cursor": None,
            },
            accounting_states=["Open", "Closed"],
            bill_ids=["d27ffe99-ff92-4afb-ac03-9268f24f0556", "297de6f8-bd67-4ebd-98b6-ecc1cd8f920c"],
            canceled_utc={
                "end_utc": parse_datetime("2023-03-31T00:00:00Z"),
                "start_utc": parse_datetime("2023-03-01T00:00:00Z"),
            },
            closed_utc={
                "end_utc": parse_datetime("2023-03-31T00:00:00Z"),
                "start_utc": parse_datetime("2023-03-01T00:00:00Z"),
            },
            consumed_utc={
                "end_utc": parse_datetime("2023-03-31T00:00:00Z"),
                "start_utc": parse_datetime("2023-03-01T00:00:00Z"),
            },
            created_utc={
                "end_utc": parse_datetime("2023-03-31T00:00:00Z"),
                "start_utc": parse_datetime("2023-03-01T00:00:00Z"),
            },
            currency="EUR",
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            order_item_ids=["3e982ab5-6245-4c39-80af-1118d40e7494", "bd11dc4a-8f9e-442b-bb1e-f5361b31dfa2"],
            service_ids=["294c7859-63ba-46ad-a8bf-34fad2019383", "05089c0c-5d55-4756-827b-c4bcee1edf00"],
            service_order_ids=["ac5ef5eb-c5b2-4083-879f-83f04a5ebda5", "5d603823-b40a-43a4-8244-d5d2b515deb5"],
            types=["CityTax", "SpaceOrder"],
            updated_utc={
                "end_utc": parse_datetime("2023-03-31T00:00:00Z"),
                "start_utc": parse_datetime("2023-03-01T00:00:00Z"),
            },
        )
        assert_matches_type(OrderItemListResponse, order_item, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.order_items.with_raw_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order_item = await response.parse()
        assert_matches_type(OrderItemListResponse, order_item, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.order_items.with_streaming_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order_item = await response.parse()
            assert_matches_type(OrderItemListResponse, order_item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_cancel(self, async_client: AsyncPymews) -> None:
        order_item = await async_client.api.connector.v1.order_items.cancel(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            order_item_ids=["f5c6b7a8-9d4f-4e2a-8a3b-2f3b8b9e6a1f", "a6b7c8d9-0e1f-4d2a-9b3c-5d6e7f8a9b0c"],
        )
        assert_matches_type(object, order_item, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_cancel_with_all_params(self, async_client: AsyncPymews) -> None:
        order_item = await async_client.api.connector.v1.order_items.cancel(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            order_item_ids=["f5c6b7a8-9d4f-4e2a-8a3b-2f3b8b9e6a1f", "a6b7c8d9-0e1f-4d2a-9b3c-5d6e7f8a9b0c"],
            enterprise_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )
        assert_matches_type(object, order_item, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.order_items.with_raw_response.cancel(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            order_item_ids=["f5c6b7a8-9d4f-4e2a-8a3b-2f3b8b9e6a1f", "a6b7c8d9-0e1f-4d2a-9b3c-5d6e7f8a9b0c"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order_item = await response.parse()
        assert_matches_type(object, order_item, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.order_items.with_streaming_response.cancel(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            order_item_ids=["f5c6b7a8-9d4f-4e2a-8a3b-2f3b8b9e6a1f", "a6b7c8d9-0e1f-4d2a-9b3c-5d6e7f8a9b0c"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order_item = await response.parse()
            assert_matches_type(object, order_item, path=["response"])

        assert cast(Any, response.is_closed) is True
