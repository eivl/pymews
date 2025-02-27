# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pymews import Pymews, AsyncPymews
from tests.utils import assert_matches_type
from pymews._utils import parse_datetime
from pymews.types.api.connector.v1 import (
    PaymentRequestResult,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPaymentRequests:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Pymews) -> None:
        payment_request = client.api.connector.v1.payment_requests.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )
        assert_matches_type(PaymentRequestResult, payment_request, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Pymews) -> None:
        payment_request = client.api.connector.v1.payment_requests.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            account_ids=["8466DFDD-0964-4002-8719-AFA900D0F1BA"],
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            payment_request_ids=["bcc76295-4e47-4cf1-a7cb-afae00bd1c35"],
            reservation_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            states=["Pending", "Completed"],
            updated_utc={
                "end_utc": parse_datetime("2020-01-10T00:00:00Z"),
                "start_utc": parse_datetime("2020-01-05T00:00:00Z"),
            },
        )
        assert_matches_type(PaymentRequestResult, payment_request, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Pymews) -> None:
        response = client.api.connector.v1.payment_requests.with_raw_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_request = response.parse()
        assert_matches_type(PaymentRequestResult, payment_request, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Pymews) -> None:
        with client.api.connector.v1.payment_requests.with_streaming_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_request = response.parse()
            assert_matches_type(PaymentRequestResult, payment_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_add(self, client: Pymews) -> None:
        payment_request = client.api.connector.v1.payment_requests.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            payment_requests=[
                {
                    "account_id": "8466dfdd-0964-4002-8719-afa900d0f1ba",
                    "amount": {
                        "currency": "EUR",
                        "value": 10,
                    },
                    "description": "Payment required",
                    "expiration_utc": parse_datetime("2023-02-20T12:00:00.000Z"),
                    "reason": "Other",
                    "type": "Payment",
                }
            ],
        )
        assert_matches_type(PaymentRequestResult, payment_request, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_add_with_all_params(self, client: Pymews) -> None:
        payment_request = client.api.connector.v1.payment_requests.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            payment_requests=[
                {
                    "account_id": "8466dfdd-0964-4002-8719-afa900d0f1ba",
                    "amount": {
                        "currency": "EUR",
                        "value": 10,
                    },
                    "description": "Payment required",
                    "expiration_utc": parse_datetime("2023-02-20T12:00:00.000Z"),
                    "reason": "Other",
                    "type": "Payment",
                    "notes": "Internal notes.",
                    "reservation_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
            enterprise_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )
        assert_matches_type(PaymentRequestResult, payment_request, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_add(self, client: Pymews) -> None:
        response = client.api.connector.v1.payment_requests.with_raw_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            payment_requests=[
                {
                    "account_id": "8466dfdd-0964-4002-8719-afa900d0f1ba",
                    "amount": {
                        "currency": "EUR",
                        "value": 10,
                    },
                    "description": "Payment required",
                    "expiration_utc": parse_datetime("2023-02-20T12:00:00.000Z"),
                    "reason": "Other",
                    "type": "Payment",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_request = response.parse()
        assert_matches_type(PaymentRequestResult, payment_request, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_add(self, client: Pymews) -> None:
        with client.api.connector.v1.payment_requests.with_streaming_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            payment_requests=[
                {
                    "account_id": "8466dfdd-0964-4002-8719-afa900d0f1ba",
                    "amount": {
                        "currency": "EUR",
                        "value": 10,
                    },
                    "description": "Payment required",
                    "expiration_utc": parse_datetime("2023-02-20T12:00:00.000Z"),
                    "reason": "Other",
                    "type": "Payment",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_request = response.parse()
            assert_matches_type(PaymentRequestResult, payment_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_cancel(self, client: Pymews) -> None:
        payment_request = client.api.connector.v1.payment_requests.cancel(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            payment_request_ids=["6282d17b-a068-4a9f-83d3-afae00c39bfb"],
        )
        assert_matches_type(PaymentRequestResult, payment_request, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_cancel(self, client: Pymews) -> None:
        response = client.api.connector.v1.payment_requests.with_raw_response.cancel(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            payment_request_ids=["6282d17b-a068-4a9f-83d3-afae00c39bfb"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_request = response.parse()
        assert_matches_type(PaymentRequestResult, payment_request, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_cancel(self, client: Pymews) -> None:
        with client.api.connector.v1.payment_requests.with_streaming_response.cancel(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            payment_request_ids=["6282d17b-a068-4a9f-83d3-afae00c39bfb"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_request = response.parse()
            assert_matches_type(PaymentRequestResult, payment_request, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPaymentRequests:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncPymews) -> None:
        payment_request = await async_client.api.connector.v1.payment_requests.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )
        assert_matches_type(PaymentRequestResult, payment_request, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPymews) -> None:
        payment_request = await async_client.api.connector.v1.payment_requests.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            account_ids=["8466DFDD-0964-4002-8719-AFA900D0F1BA"],
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            payment_request_ids=["bcc76295-4e47-4cf1-a7cb-afae00bd1c35"],
            reservation_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            states=["Pending", "Completed"],
            updated_utc={
                "end_utc": parse_datetime("2020-01-10T00:00:00Z"),
                "start_utc": parse_datetime("2020-01-05T00:00:00Z"),
            },
        )
        assert_matches_type(PaymentRequestResult, payment_request, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.payment_requests.with_raw_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_request = await response.parse()
        assert_matches_type(PaymentRequestResult, payment_request, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.payment_requests.with_streaming_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_request = await response.parse()
            assert_matches_type(PaymentRequestResult, payment_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_add(self, async_client: AsyncPymews) -> None:
        payment_request = await async_client.api.connector.v1.payment_requests.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            payment_requests=[
                {
                    "account_id": "8466dfdd-0964-4002-8719-afa900d0f1ba",
                    "amount": {
                        "currency": "EUR",
                        "value": 10,
                    },
                    "description": "Payment required",
                    "expiration_utc": parse_datetime("2023-02-20T12:00:00.000Z"),
                    "reason": "Other",
                    "type": "Payment",
                }
            ],
        )
        assert_matches_type(PaymentRequestResult, payment_request, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_add_with_all_params(self, async_client: AsyncPymews) -> None:
        payment_request = await async_client.api.connector.v1.payment_requests.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            payment_requests=[
                {
                    "account_id": "8466dfdd-0964-4002-8719-afa900d0f1ba",
                    "amount": {
                        "currency": "EUR",
                        "value": 10,
                    },
                    "description": "Payment required",
                    "expiration_utc": parse_datetime("2023-02-20T12:00:00.000Z"),
                    "reason": "Other",
                    "type": "Payment",
                    "notes": "Internal notes.",
                    "reservation_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
            enterprise_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )
        assert_matches_type(PaymentRequestResult, payment_request, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.payment_requests.with_raw_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            payment_requests=[
                {
                    "account_id": "8466dfdd-0964-4002-8719-afa900d0f1ba",
                    "amount": {
                        "currency": "EUR",
                        "value": 10,
                    },
                    "description": "Payment required",
                    "expiration_utc": parse_datetime("2023-02-20T12:00:00.000Z"),
                    "reason": "Other",
                    "type": "Payment",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_request = await response.parse()
        assert_matches_type(PaymentRequestResult, payment_request, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.payment_requests.with_streaming_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            payment_requests=[
                {
                    "account_id": "8466dfdd-0964-4002-8719-afa900d0f1ba",
                    "amount": {
                        "currency": "EUR",
                        "value": 10,
                    },
                    "description": "Payment required",
                    "expiration_utc": parse_datetime("2023-02-20T12:00:00.000Z"),
                    "reason": "Other",
                    "type": "Payment",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_request = await response.parse()
            assert_matches_type(PaymentRequestResult, payment_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_cancel(self, async_client: AsyncPymews) -> None:
        payment_request = await async_client.api.connector.v1.payment_requests.cancel(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            payment_request_ids=["6282d17b-a068-4a9f-83d3-afae00c39bfb"],
        )
        assert_matches_type(PaymentRequestResult, payment_request, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.payment_requests.with_raw_response.cancel(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            payment_request_ids=["6282d17b-a068-4a9f-83d3-afae00c39bfb"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_request = await response.parse()
        assert_matches_type(PaymentRequestResult, payment_request, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.payment_requests.with_streaming_response.cancel(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            payment_request_ids=["6282d17b-a068-4a9f-83d3-afae00c39bfb"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_request = await response.parse()
            assert_matches_type(PaymentRequestResult, payment_request, path=["response"])

        assert cast(Any, response.is_closed) is True
