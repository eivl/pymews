# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pymews import Pymews, AsyncPymews
from tests.utils import assert_matches_type
from pymews._utils import parse_datetime
from pymews.types.api.connector import AddCreditCardResult
from pymews.types.api.connector.v1 import (
    CreditCardResult,
    CreditCardChargeResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCreditCards:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Pymews) -> None:
        credit_card = client.api.connector.v1.credit_cards.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )
        assert_matches_type(CreditCardResult, credit_card, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Pymews) -> None:
        credit_card = client.api.connector.v1.credit_cards.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            credit_card_ids=["f1d94a32-b4be-479b-9e47-a9fcb03d5196"],
            customer_ids=["5cbbd97d-5f19-4010-9abf-ab0400a3366a"],
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            updated_utc={
                "end_utc": parse_datetime("2023-10-31T00:00:00Z"),
                "start_utc": parse_datetime("2023-10-01T00:00:00Z"),
            },
        )
        assert_matches_type(CreditCardResult, credit_card, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Pymews) -> None:
        response = client.api.connector.v1.credit_cards.with_raw_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_card = response.parse()
        assert_matches_type(CreditCardResult, credit_card, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Pymews) -> None:
        with client.api.connector.v1.credit_cards.with_streaming_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_card = response.parse()
            assert_matches_type(CreditCardResult, credit_card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_add_tokenized(self, client: Pymews) -> None:
        credit_card = client.api.connector.v1.credit_cards.add_tokenized(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            credit_card_data={
                "expiration": "2025-10",
                "storage_data": "190510170631533875",
            },
            customer_id="e98995b0-140a-4208-bbeb-b77f2c43d6ee",
        )
        assert_matches_type(AddCreditCardResult, credit_card, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_add_tokenized_with_all_params(self, client: Pymews) -> None:
        credit_card = client.api.connector.v1.credit_cards.add_tokenized(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            credit_card_data={
                "expiration": "2025-10",
                "storage_data": "190510170631533875",
                "obfuscated_number": "ObfuscatedNumber",
            },
            customer_id="e98995b0-140a-4208-bbeb-b77f2c43d6ee",
        )
        assert_matches_type(AddCreditCardResult, credit_card, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_add_tokenized(self, client: Pymews) -> None:
        response = client.api.connector.v1.credit_cards.with_raw_response.add_tokenized(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            credit_card_data={
                "expiration": "2025-10",
                "storage_data": "190510170631533875",
            },
            customer_id="e98995b0-140a-4208-bbeb-b77f2c43d6ee",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_card = response.parse()
        assert_matches_type(AddCreditCardResult, credit_card, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_add_tokenized(self, client: Pymews) -> None:
        with client.api.connector.v1.credit_cards.with_streaming_response.add_tokenized(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            credit_card_data={
                "expiration": "2025-10",
                "storage_data": "190510170631533875",
            },
            customer_id="e98995b0-140a-4208-bbeb-b77f2c43d6ee",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_card = response.parse()
            assert_matches_type(AddCreditCardResult, credit_card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_charge(self, client: Pymews) -> None:
        credit_card = client.api.connector.v1.credit_cards.charge(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            amount={"currency": "EUR"},
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )
        assert_matches_type(CreditCardChargeResponse, credit_card, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_charge_with_all_params(self, client: Pymews) -> None:
        credit_card = client.api.connector.v1.credit_cards.charge(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            amount={
                "currency": "EUR",
                "gross_value": 5,
                "net_value": 0,
                "tax_codes": ["string"],
            },
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            accounting_category_id=None,
            bill_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            credit_card_id="866d3f51-5b8b-4e8f-a3af-5b84768c522d",
            notes=None,
            receipt_identifier=None,
            reservation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CreditCardChargeResponse, credit_card, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_charge(self, client: Pymews) -> None:
        response = client.api.connector.v1.credit_cards.with_raw_response.charge(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            amount={"currency": "EUR"},
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_card = response.parse()
        assert_matches_type(CreditCardChargeResponse, credit_card, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_charge(self, client: Pymews) -> None:
        with client.api.connector.v1.credit_cards.with_streaming_response.charge(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            amount={"currency": "EUR"},
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_card = response.parse()
            assert_matches_type(CreditCardChargeResponse, credit_card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_disable(self, client: Pymews) -> None:
        credit_card = client.api.connector.v1.credit_cards.disable(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            credit_card_id="f5c6b7a8-9d4f-4e2a-8a3b-2f3b8b9e6a1f",
        )
        assert_matches_type(object, credit_card, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_disable_with_all_params(self, client: Pymews) -> None:
        credit_card = client.api.connector.v1.credit_cards.disable(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            credit_card_id="f5c6b7a8-9d4f-4e2a-8a3b-2f3b8b9e6a1f",
            enterprise_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )
        assert_matches_type(object, credit_card, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_disable(self, client: Pymews) -> None:
        response = client.api.connector.v1.credit_cards.with_raw_response.disable(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            credit_card_id="f5c6b7a8-9d4f-4e2a-8a3b-2f3b8b9e6a1f",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_card = response.parse()
        assert_matches_type(object, credit_card, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_disable(self, client: Pymews) -> None:
        with client.api.connector.v1.credit_cards.with_streaming_response.disable(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            credit_card_id="f5c6b7a8-9d4f-4e2a-8a3b-2f3b8b9e6a1f",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_card = response.parse()
            assert_matches_type(object, credit_card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list_by_customers(self, client: Pymews) -> None:
        credit_card = client.api.connector.v1.credit_cards.list_by_customers(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_ids=["e98995b0-140a-4208-bbeb-b77f2c43d6ee"],
        )
        assert_matches_type(CreditCardResult, credit_card, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_by_customers(self, client: Pymews) -> None:
        response = client.api.connector.v1.credit_cards.with_raw_response.list_by_customers(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_ids=["e98995b0-140a-4208-bbeb-b77f2c43d6ee"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_card = response.parse()
        assert_matches_type(CreditCardResult, credit_card, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_by_customers(self, client: Pymews) -> None:
        with client.api.connector.v1.credit_cards.with_streaming_response.list_by_customers(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_ids=["e98995b0-140a-4208-bbeb-b77f2c43d6ee"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_card = response.parse()
            assert_matches_type(CreditCardResult, credit_card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list_by_ids(self, client: Pymews) -> None:
        credit_card = client.api.connector.v1.credit_cards.list_by_ids(
            access_token="string",
            client="string",
            client_token="string",
        )
        assert_matches_type(CreditCardResult, credit_card, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_by_ids_with_all_params(self, client: Pymews) -> None:
        credit_card = client.api.connector.v1.credit_cards.list_by_ids(
            access_token="string",
            client="string",
            client_token="string",
            credit_card_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6"],
        )
        assert_matches_type(CreditCardResult, credit_card, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_by_ids(self, client: Pymews) -> None:
        response = client.api.connector.v1.credit_cards.with_raw_response.list_by_ids(
            access_token="string",
            client="string",
            client_token="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_card = response.parse()
        assert_matches_type(CreditCardResult, credit_card, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_by_ids(self, client: Pymews) -> None:
        with client.api.connector.v1.credit_cards.with_streaming_response.list_by_ids(
            access_token="string",
            client="string",
            client_token="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_card = response.parse()
            assert_matches_type(CreditCardResult, credit_card, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCreditCards:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncPymews) -> None:
        credit_card = await async_client.api.connector.v1.credit_cards.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )
        assert_matches_type(CreditCardResult, credit_card, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPymews) -> None:
        credit_card = await async_client.api.connector.v1.credit_cards.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            credit_card_ids=["f1d94a32-b4be-479b-9e47-a9fcb03d5196"],
            customer_ids=["5cbbd97d-5f19-4010-9abf-ab0400a3366a"],
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            updated_utc={
                "end_utc": parse_datetime("2023-10-31T00:00:00Z"),
                "start_utc": parse_datetime("2023-10-01T00:00:00Z"),
            },
        )
        assert_matches_type(CreditCardResult, credit_card, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.credit_cards.with_raw_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_card = await response.parse()
        assert_matches_type(CreditCardResult, credit_card, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.credit_cards.with_streaming_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_card = await response.parse()
            assert_matches_type(CreditCardResult, credit_card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_add_tokenized(self, async_client: AsyncPymews) -> None:
        credit_card = await async_client.api.connector.v1.credit_cards.add_tokenized(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            credit_card_data={
                "expiration": "2025-10",
                "storage_data": "190510170631533875",
            },
            customer_id="e98995b0-140a-4208-bbeb-b77f2c43d6ee",
        )
        assert_matches_type(AddCreditCardResult, credit_card, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_add_tokenized_with_all_params(self, async_client: AsyncPymews) -> None:
        credit_card = await async_client.api.connector.v1.credit_cards.add_tokenized(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            credit_card_data={
                "expiration": "2025-10",
                "storage_data": "190510170631533875",
                "obfuscated_number": "ObfuscatedNumber",
            },
            customer_id="e98995b0-140a-4208-bbeb-b77f2c43d6ee",
        )
        assert_matches_type(AddCreditCardResult, credit_card, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_add_tokenized(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.credit_cards.with_raw_response.add_tokenized(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            credit_card_data={
                "expiration": "2025-10",
                "storage_data": "190510170631533875",
            },
            customer_id="e98995b0-140a-4208-bbeb-b77f2c43d6ee",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_card = await response.parse()
        assert_matches_type(AddCreditCardResult, credit_card, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_add_tokenized(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.credit_cards.with_streaming_response.add_tokenized(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            credit_card_data={
                "expiration": "2025-10",
                "storage_data": "190510170631533875",
            },
            customer_id="e98995b0-140a-4208-bbeb-b77f2c43d6ee",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_card = await response.parse()
            assert_matches_type(AddCreditCardResult, credit_card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_charge(self, async_client: AsyncPymews) -> None:
        credit_card = await async_client.api.connector.v1.credit_cards.charge(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            amount={"currency": "EUR"},
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )
        assert_matches_type(CreditCardChargeResponse, credit_card, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_charge_with_all_params(self, async_client: AsyncPymews) -> None:
        credit_card = await async_client.api.connector.v1.credit_cards.charge(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            amount={
                "currency": "EUR",
                "gross_value": 5,
                "net_value": 0,
                "tax_codes": ["string"],
            },
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            accounting_category_id=None,
            bill_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            credit_card_id="866d3f51-5b8b-4e8f-a3af-5b84768c522d",
            notes=None,
            receipt_identifier=None,
            reservation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CreditCardChargeResponse, credit_card, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_charge(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.credit_cards.with_raw_response.charge(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            amount={"currency": "EUR"},
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_card = await response.parse()
        assert_matches_type(CreditCardChargeResponse, credit_card, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_charge(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.credit_cards.with_streaming_response.charge(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            amount={"currency": "EUR"},
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_card = await response.parse()
            assert_matches_type(CreditCardChargeResponse, credit_card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_disable(self, async_client: AsyncPymews) -> None:
        credit_card = await async_client.api.connector.v1.credit_cards.disable(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            credit_card_id="f5c6b7a8-9d4f-4e2a-8a3b-2f3b8b9e6a1f",
        )
        assert_matches_type(object, credit_card, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_disable_with_all_params(self, async_client: AsyncPymews) -> None:
        credit_card = await async_client.api.connector.v1.credit_cards.disable(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            credit_card_id="f5c6b7a8-9d4f-4e2a-8a3b-2f3b8b9e6a1f",
            enterprise_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )
        assert_matches_type(object, credit_card, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_disable(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.credit_cards.with_raw_response.disable(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            credit_card_id="f5c6b7a8-9d4f-4e2a-8a3b-2f3b8b9e6a1f",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_card = await response.parse()
        assert_matches_type(object, credit_card, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_disable(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.credit_cards.with_streaming_response.disable(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            credit_card_id="f5c6b7a8-9d4f-4e2a-8a3b-2f3b8b9e6a1f",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_card = await response.parse()
            assert_matches_type(object, credit_card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_by_customers(self, async_client: AsyncPymews) -> None:
        credit_card = await async_client.api.connector.v1.credit_cards.list_by_customers(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_ids=["e98995b0-140a-4208-bbeb-b77f2c43d6ee"],
        )
        assert_matches_type(CreditCardResult, credit_card, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_by_customers(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.credit_cards.with_raw_response.list_by_customers(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_ids=["e98995b0-140a-4208-bbeb-b77f2c43d6ee"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_card = await response.parse()
        assert_matches_type(CreditCardResult, credit_card, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_by_customers(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.credit_cards.with_streaming_response.list_by_customers(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_ids=["e98995b0-140a-4208-bbeb-b77f2c43d6ee"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_card = await response.parse()
            assert_matches_type(CreditCardResult, credit_card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_by_ids(self, async_client: AsyncPymews) -> None:
        credit_card = await async_client.api.connector.v1.credit_cards.list_by_ids(
            access_token="string",
            client="string",
            client_token="string",
        )
        assert_matches_type(CreditCardResult, credit_card, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_by_ids_with_all_params(self, async_client: AsyncPymews) -> None:
        credit_card = await async_client.api.connector.v1.credit_cards.list_by_ids(
            access_token="string",
            client="string",
            client_token="string",
            credit_card_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6"],
        )
        assert_matches_type(CreditCardResult, credit_card, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_by_ids(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.credit_cards.with_raw_response.list_by_ids(
            access_token="string",
            client="string",
            client_token="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_card = await response.parse()
        assert_matches_type(CreditCardResult, credit_card, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_by_ids(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.credit_cards.with_streaming_response.list_by_ids(
            access_token="string",
            client="string",
            client_token="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_card = await response.parse()
            assert_matches_type(CreditCardResult, credit_card, path=["response"])

        assert cast(Any, response.is_closed) is True
