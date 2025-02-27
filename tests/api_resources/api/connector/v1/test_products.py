# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pymews import Pymews, AsyncPymews
from tests.utils import assert_matches_type
from pymews._utils import parse_datetime
from pymews.types.api.connector.v1 import (
    ProductListResponse,
    ProductGetPricingResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProducts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Pymews) -> None:
        product = client.api.connector.v1.products.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            service_ids=["bd26d8db-86da-4f96-9efc-e5a4654a4a94"],
        )
        assert_matches_type(ProductListResponse, product, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Pymews) -> None:
        product = client.api.connector.v1.products.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            service_ids=["bd26d8db-86da-4f96-9efc-e5a4654a4a94"],
            enterprise_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            include_default=True,
            product_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            updated_utc={
                "end_utc": parse_datetime("2023-10-31T00:00:00Z"),
                "start_utc": parse_datetime("2023-10-01T00:00:00Z"),
            },
        )
        assert_matches_type(ProductListResponse, product, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Pymews) -> None:
        response = client.api.connector.v1.products.with_raw_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            service_ids=["bd26d8db-86da-4f96-9efc-e5a4654a4a94"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = response.parse()
        assert_matches_type(ProductListResponse, product, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Pymews) -> None:
        with client.api.connector.v1.products.with_streaming_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            service_ids=["bd26d8db-86da-4f96-9efc-e5a4654a4a94"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = response.parse()
            assert_matches_type(ProductListResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Pymews) -> None:
        product = client.api.connector.v1.products.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            product_ids=["1f60b9de-c042-4841-bcab-b07000d2201f"],
        )
        assert_matches_type(object, product, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_delete_with_all_params(self, client: Pymews) -> None:
        product = client.api.connector.v1.products.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            product_ids=["1f60b9de-c042-4841-bcab-b07000d2201f"],
            enterprise_id="aff75fbb-5cce-4fae-8039-b07000d16650",
        )
        assert_matches_type(object, product, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Pymews) -> None:
        response = client.api.connector.v1.products.with_raw_response.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            product_ids=["1f60b9de-c042-4841-bcab-b07000d2201f"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = response.parse()
        assert_matches_type(object, product, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Pymews) -> None:
        with client.api.connector.v1.products.with_streaming_response.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            product_ids=["1f60b9de-c042-4841-bcab-b07000d2201f"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = response.parse()
            assert_matches_type(object, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_pricing(self, client: Pymews) -> None:
        product = client.api.connector.v1.products.get_pricing(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            first_time_unit_start_utc=parse_datetime("2024-03-01T23:00:00.000Z"),
            last_time_unit_start_utc=parse_datetime("2024-03-03T23:00:00.000Z"),
            product_id="6b97a38b-0043-41e0-afbd-3f083bdbc0d2",
        )
        assert_matches_type(ProductGetPricingResponse, product, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_pricing_with_all_params(self, client: Pymews) -> None:
        product = client.api.connector.v1.products.get_pricing(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            first_time_unit_start_utc=parse_datetime("2024-03-01T23:00:00.000Z"),
            last_time_unit_start_utc=parse_datetime("2024-03-03T23:00:00.000Z"),
            product_id="6b97a38b-0043-41e0-afbd-3f083bdbc0d2",
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
        )
        assert_matches_type(ProductGetPricingResponse, product, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_pricing(self, client: Pymews) -> None:
        response = client.api.connector.v1.products.with_raw_response.get_pricing(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            first_time_unit_start_utc=parse_datetime("2024-03-01T23:00:00.000Z"),
            last_time_unit_start_utc=parse_datetime("2024-03-03T23:00:00.000Z"),
            product_id="6b97a38b-0043-41e0-afbd-3f083bdbc0d2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = response.parse()
        assert_matches_type(ProductGetPricingResponse, product, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_pricing(self, client: Pymews) -> None:
        with client.api.connector.v1.products.with_streaming_response.get_pricing(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            first_time_unit_start_utc=parse_datetime("2024-03-01T23:00:00.000Z"),
            last_time_unit_start_utc=parse_datetime("2024-03-03T23:00:00.000Z"),
            product_id="6b97a38b-0043-41e0-afbd-3f083bdbc0d2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = response.parse()
            assert_matches_type(ProductGetPricingResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_update_price(self, client: Pymews) -> None:
        product = client.api.connector.v1.products.update_price(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            price_updates=[{}, {}],
            product_id="6b97a38b-0043-41e0-afbd-3f083bdbc0d2",
        )
        assert_matches_type(object, product, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_price_with_all_params(self, client: Pymews) -> None:
        product = client.api.connector.v1.products.update_price(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            price_updates=[
                {
                    "first_time_unit_start_utc": parse_datetime("2024-03-01T23:00:00.000Z"),
                    "last_time_unit_start_utc": parse_datetime("2024-03-03T23:00:00.000Z"),
                    "value": 100,
                },
                {
                    "first_time_unit_start_utc": parse_datetime("2024-03-06T23:00:00.000Z"),
                    "last_time_unit_start_utc": parse_datetime("2024-03-08T23:00:00.000Z"),
                    "value": 200,
                },
            ],
            product_id="6b97a38b-0043-41e0-afbd-3f083bdbc0d2",
            enterprise_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )
        assert_matches_type(object, product, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update_price(self, client: Pymews) -> None:
        response = client.api.connector.v1.products.with_raw_response.update_price(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            price_updates=[{}, {}],
            product_id="6b97a38b-0043-41e0-afbd-3f083bdbc0d2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = response.parse()
        assert_matches_type(object, product, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update_price(self, client: Pymews) -> None:
        with client.api.connector.v1.products.with_streaming_response.update_price(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            price_updates=[{}, {}],
            product_id="6b97a38b-0043-41e0-afbd-3f083bdbc0d2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = response.parse()
            assert_matches_type(object, product, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncProducts:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncPymews) -> None:
        product = await async_client.api.connector.v1.products.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            service_ids=["bd26d8db-86da-4f96-9efc-e5a4654a4a94"],
        )
        assert_matches_type(ProductListResponse, product, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPymews) -> None:
        product = await async_client.api.connector.v1.products.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            service_ids=["bd26d8db-86da-4f96-9efc-e5a4654a4a94"],
            enterprise_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            include_default=True,
            product_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            updated_utc={
                "end_utc": parse_datetime("2023-10-31T00:00:00Z"),
                "start_utc": parse_datetime("2023-10-01T00:00:00Z"),
            },
        )
        assert_matches_type(ProductListResponse, product, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.products.with_raw_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            service_ids=["bd26d8db-86da-4f96-9efc-e5a4654a4a94"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = await response.parse()
        assert_matches_type(ProductListResponse, product, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.products.with_streaming_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            service_ids=["bd26d8db-86da-4f96-9efc-e5a4654a4a94"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = await response.parse()
            assert_matches_type(ProductListResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncPymews) -> None:
        product = await async_client.api.connector.v1.products.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            product_ids=["1f60b9de-c042-4841-bcab-b07000d2201f"],
        )
        assert_matches_type(object, product, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncPymews) -> None:
        product = await async_client.api.connector.v1.products.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            product_ids=["1f60b9de-c042-4841-bcab-b07000d2201f"],
            enterprise_id="aff75fbb-5cce-4fae-8039-b07000d16650",
        )
        assert_matches_type(object, product, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.products.with_raw_response.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            product_ids=["1f60b9de-c042-4841-bcab-b07000d2201f"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = await response.parse()
        assert_matches_type(object, product, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.products.with_streaming_response.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            product_ids=["1f60b9de-c042-4841-bcab-b07000d2201f"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = await response.parse()
            assert_matches_type(object, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_pricing(self, async_client: AsyncPymews) -> None:
        product = await async_client.api.connector.v1.products.get_pricing(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            first_time_unit_start_utc=parse_datetime("2024-03-01T23:00:00.000Z"),
            last_time_unit_start_utc=parse_datetime("2024-03-03T23:00:00.000Z"),
            product_id="6b97a38b-0043-41e0-afbd-3f083bdbc0d2",
        )
        assert_matches_type(ProductGetPricingResponse, product, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_pricing_with_all_params(self, async_client: AsyncPymews) -> None:
        product = await async_client.api.connector.v1.products.get_pricing(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            first_time_unit_start_utc=parse_datetime("2024-03-01T23:00:00.000Z"),
            last_time_unit_start_utc=parse_datetime("2024-03-03T23:00:00.000Z"),
            product_id="6b97a38b-0043-41e0-afbd-3f083bdbc0d2",
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
        )
        assert_matches_type(ProductGetPricingResponse, product, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_pricing(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.products.with_raw_response.get_pricing(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            first_time_unit_start_utc=parse_datetime("2024-03-01T23:00:00.000Z"),
            last_time_unit_start_utc=parse_datetime("2024-03-03T23:00:00.000Z"),
            product_id="6b97a38b-0043-41e0-afbd-3f083bdbc0d2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = await response.parse()
        assert_matches_type(ProductGetPricingResponse, product, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_pricing(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.products.with_streaming_response.get_pricing(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            first_time_unit_start_utc=parse_datetime("2024-03-01T23:00:00.000Z"),
            last_time_unit_start_utc=parse_datetime("2024-03-03T23:00:00.000Z"),
            product_id="6b97a38b-0043-41e0-afbd-3f083bdbc0d2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = await response.parse()
            assert_matches_type(ProductGetPricingResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_price(self, async_client: AsyncPymews) -> None:
        product = await async_client.api.connector.v1.products.update_price(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            price_updates=[{}, {}],
            product_id="6b97a38b-0043-41e0-afbd-3f083bdbc0d2",
        )
        assert_matches_type(object, product, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_price_with_all_params(self, async_client: AsyncPymews) -> None:
        product = await async_client.api.connector.v1.products.update_price(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            price_updates=[
                {
                    "first_time_unit_start_utc": parse_datetime("2024-03-01T23:00:00.000Z"),
                    "last_time_unit_start_utc": parse_datetime("2024-03-03T23:00:00.000Z"),
                    "value": 100,
                },
                {
                    "first_time_unit_start_utc": parse_datetime("2024-03-06T23:00:00.000Z"),
                    "last_time_unit_start_utc": parse_datetime("2024-03-08T23:00:00.000Z"),
                    "value": 200,
                },
            ],
            product_id="6b97a38b-0043-41e0-afbd-3f083bdbc0d2",
            enterprise_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )
        assert_matches_type(object, product, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update_price(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.products.with_raw_response.update_price(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            price_updates=[{}, {}],
            product_id="6b97a38b-0043-41e0-afbd-3f083bdbc0d2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = await response.parse()
        assert_matches_type(object, product, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update_price(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.products.with_streaming_response.update_price(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            price_updates=[{}, {}],
            product_id="6b97a38b-0043-41e0-afbd-3f083bdbc0d2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = await response.parse()
            assert_matches_type(object, product, path=["response"])

        assert cast(Any, response.is_closed) is True
