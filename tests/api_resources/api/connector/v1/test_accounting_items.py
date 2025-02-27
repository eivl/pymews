# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pymews import Pymews, AsyncPymews
from tests.utils import assert_matches_type
from pymews._utils import parse_datetime
from pymews.types.api.connector.v1 import (
    AccountingItemResult,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccountingItems:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Pymews) -> None:
        accounting_item = client.api.connector.v1.accounting_items.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            accounting_item_updates=[
                {
                    "accounting_item_id": "6c2897de-620a-4f48-af1e-ada8004202bd",
                    "bill_id": {},
                }
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )
        assert_matches_type(AccountingItemResult, accounting_item, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Pymews) -> None:
        accounting_item = client.api.connector.v1.accounting_items.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            accounting_item_updates=[
                {
                    "accounting_item_id": "6c2897de-620a-4f48-af1e-ada8004202bd",
                    "bill_id": {"value": "9e3791dc-95c7-439a-aa8a-ada8007de0ca"},
                    "account_id": {"value": "182a56ee-037d-4da5-b6f8-ada8006e7d5c"},
                }
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            enterprise_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )
        assert_matches_type(AccountingItemResult, accounting_item, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Pymews) -> None:
        response = client.api.connector.v1.accounting_items.with_raw_response.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            accounting_item_updates=[
                {
                    "accounting_item_id": "6c2897de-620a-4f48-af1e-ada8004202bd",
                    "bill_id": {},
                }
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        accounting_item = response.parse()
        assert_matches_type(AccountingItemResult, accounting_item, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Pymews) -> None:
        with client.api.connector.v1.accounting_items.with_streaming_response.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            accounting_item_updates=[
                {
                    "accounting_item_id": "6c2897de-620a-4f48-af1e-ada8004202bd",
                    "bill_id": {},
                }
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            accounting_item = response.parse()
            assert_matches_type(AccountingItemResult, accounting_item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Pymews) -> None:
        accounting_item = client.api.connector.v1.accounting_items.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            end_utc=parse_datetime("2019-12-27T18:11:19.117Z"),
            extent={},
            start_utc=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AccountingItemResult, accounting_item, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Pymews) -> None:
        accounting_item = client.api.connector.v1.accounting_items.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            end_utc=parse_datetime("2019-12-27T18:11:19.117Z"),
            extent={
                "accounting_items": True,
                "credit_card_transactions": False,
                "order_items": True,
                "payment_items": True,
            },
            start_utc=parse_datetime("2019-12-27T18:11:19.117Z"),
            closed_utc={
                "end_utc": parse_datetime("2020-01-10T00:00:00Z"),
                "start_utc": parse_datetime("2020-01-05T00:00:00Z"),
            },
            consumed_utc={
                "end_utc": parse_datetime("2020-01-10T00:00:00Z"),
                "start_utc": parse_datetime("2020-01-05T00:00:00Z"),
            },
            currency="Currency",
            item_ids=["cb643cb7-8b6e-48a6-b67e-ad4c0041f550", "44ca12b8-f009-455e-be91-ad4c013fcbc5"],
            rebated_item_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            states=["Open"],
            time_filter="TimeFilter",
            updated_utc={
                "end_utc": parse_datetime("2020-01-10T00:00:00Z"),
                "start_utc": parse_datetime("2020-01-05T00:00:00Z"),
            },
        )
        assert_matches_type(AccountingItemResult, accounting_item, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Pymews) -> None:
        response = client.api.connector.v1.accounting_items.with_raw_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            end_utc=parse_datetime("2019-12-27T18:11:19.117Z"),
            extent={},
            start_utc=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        accounting_item = response.parse()
        assert_matches_type(AccountingItemResult, accounting_item, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Pymews) -> None:
        with client.api.connector.v1.accounting_items.with_streaming_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            end_utc=parse_datetime("2019-12-27T18:11:19.117Z"),
            extent={},
            start_utc=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            accounting_item = response.parse()
            assert_matches_type(AccountingItemResult, accounting_item, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAccountingItems:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncPymews) -> None:
        accounting_item = await async_client.api.connector.v1.accounting_items.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            accounting_item_updates=[
                {
                    "accounting_item_id": "6c2897de-620a-4f48-af1e-ada8004202bd",
                    "bill_id": {},
                }
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )
        assert_matches_type(AccountingItemResult, accounting_item, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncPymews) -> None:
        accounting_item = await async_client.api.connector.v1.accounting_items.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            accounting_item_updates=[
                {
                    "accounting_item_id": "6c2897de-620a-4f48-af1e-ada8004202bd",
                    "bill_id": {"value": "9e3791dc-95c7-439a-aa8a-ada8007de0ca"},
                    "account_id": {"value": "182a56ee-037d-4da5-b6f8-ada8006e7d5c"},
                }
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            enterprise_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )
        assert_matches_type(AccountingItemResult, accounting_item, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.accounting_items.with_raw_response.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            accounting_item_updates=[
                {
                    "accounting_item_id": "6c2897de-620a-4f48-af1e-ada8004202bd",
                    "bill_id": {},
                }
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        accounting_item = await response.parse()
        assert_matches_type(AccountingItemResult, accounting_item, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.accounting_items.with_streaming_response.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            accounting_item_updates=[
                {
                    "accounting_item_id": "6c2897de-620a-4f48-af1e-ada8004202bd",
                    "bill_id": {},
                }
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            accounting_item = await response.parse()
            assert_matches_type(AccountingItemResult, accounting_item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncPymews) -> None:
        accounting_item = await async_client.api.connector.v1.accounting_items.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            end_utc=parse_datetime("2019-12-27T18:11:19.117Z"),
            extent={},
            start_utc=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AccountingItemResult, accounting_item, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPymews) -> None:
        accounting_item = await async_client.api.connector.v1.accounting_items.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            end_utc=parse_datetime("2019-12-27T18:11:19.117Z"),
            extent={
                "accounting_items": True,
                "credit_card_transactions": False,
                "order_items": True,
                "payment_items": True,
            },
            start_utc=parse_datetime("2019-12-27T18:11:19.117Z"),
            closed_utc={
                "end_utc": parse_datetime("2020-01-10T00:00:00Z"),
                "start_utc": parse_datetime("2020-01-05T00:00:00Z"),
            },
            consumed_utc={
                "end_utc": parse_datetime("2020-01-10T00:00:00Z"),
                "start_utc": parse_datetime("2020-01-05T00:00:00Z"),
            },
            currency="Currency",
            item_ids=["cb643cb7-8b6e-48a6-b67e-ad4c0041f550", "44ca12b8-f009-455e-be91-ad4c013fcbc5"],
            rebated_item_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            states=["Open"],
            time_filter="TimeFilter",
            updated_utc={
                "end_utc": parse_datetime("2020-01-10T00:00:00Z"),
                "start_utc": parse_datetime("2020-01-05T00:00:00Z"),
            },
        )
        assert_matches_type(AccountingItemResult, accounting_item, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.accounting_items.with_raw_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            end_utc=parse_datetime("2019-12-27T18:11:19.117Z"),
            extent={},
            start_utc=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        accounting_item = await response.parse()
        assert_matches_type(AccountingItemResult, accounting_item, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.accounting_items.with_streaming_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            end_utc=parse_datetime("2019-12-27T18:11:19.117Z"),
            extent={},
            start_utc=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            accounting_item = await response.parse()
            assert_matches_type(AccountingItemResult, accounting_item, path=["response"])

        assert cast(Any, response.is_closed) is True
