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
    PaymentListResponse,
    PaymentRefundResponse,
    PaymentAddExternalResponse,
    PaymentAddAlternativeResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPayments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Pymews) -> None:
        payment = client.api.connector.v1.payments.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )
        assert_matches_type(PaymentListResponse, payment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Pymews) -> None:
        payment = client.api.connector.v1.payments.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            account_ids=["fadd5bb6-b428-45d5-94f8-fd0d89fece6d"],
            accounting_states=["Closed", "Open"],
            bill_ids=["ea087d64-3901-4eee-b0b7-9fce4c58a005", "d23ac52f-9b86-4a03-a6fe-5822dfcfc5c4"],
            charged_utc={
                "end_utc": parse_datetime("2023-03-31T00:00:00Z"),
                "start_utc": parse_datetime("2023-03-01T00:00:00Z"),
            },
            closed_utc={
                "end_utc": parse_datetime("2023-03-31T00:00:00Z"),
                "start_utc": parse_datetime("2023-03-01T00:00:00Z"),
            },
            created_utc={
                "end_utc": parse_datetime("2023-03-31T00:00:00Z"),
                "start_utc": parse_datetime("2023-03-01T00:00:00Z"),
            },
            currency="EUR",
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            payment_ids=["f6313945-94c1-4e27-b402-031c2a8c989f", "be922eb7-bc5f-4877-b847-1120c0c2acd2"],
            reservation_ids=["0f515589-99b4-423d-b83a-b237009f0509", "b7a3f5cb-1e69-4a5f-a069-10f461996d7f"],
            settlement_utc={
                "end_utc": parse_datetime("2023-03-31T00:00:00Z"),
                "start_utc": parse_datetime("2023-03-01T00:00:00Z"),
            },
            states=["Charged", "Pending"],
            type="Payment",
            updated_utc={
                "end_utc": parse_datetime("2023-03-31T00:00:00Z"),
                "start_utc": parse_datetime("2023-03-01T00:00:00Z"),
            },
        )
        assert_matches_type(PaymentListResponse, payment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Pymews) -> None:
        response = client.api.connector.v1.payments.with_raw_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(PaymentListResponse, payment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Pymews) -> None:
        with client.api.connector.v1.payments.with_streaming_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = response.parse()
            assert_matches_type(PaymentListResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_add_alternative(self, client: Pymews) -> None:
        payment = client.api.connector.v1.payments.add_alternative(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            amount={
                "currency": "GBP",
                "tax_codes": ["string"],
            },
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_id="35d4b117-4e60-44a3-9580-c582117eff98",
            data={"discriminator": "Ideal"},
        )
        assert_matches_type(PaymentAddAlternativeResponse, payment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_add_alternative_with_all_params(self, client: Pymews) -> None:
        payment = client.api.connector.v1.payments.add_alternative(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            amount={
                "currency": "GBP",
                "tax_codes": ["string"],
                "gross_value": 100,
                "net_value": 0,
            },
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_id="35d4b117-4e60-44a3-9580-c582117eff98",
            data={
                "discriminator": "Ideal",
                "ideal": {"redirect_url": "https://example.com"},
                "sepa_direct_debit": {
                    "email": "dev@stainless.com",
                    "iban": "x",
                    "name": "x",
                    "remote_ip_address": "x",
                    "user_agent": "x",
                },
            },
            method="Ideal",
            redirect_url="https://mews.com",
            reservation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PaymentAddAlternativeResponse, payment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_add_alternative(self, client: Pymews) -> None:
        response = client.api.connector.v1.payments.with_raw_response.add_alternative(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            amount={
                "currency": "GBP",
                "tax_codes": ["string"],
            },
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_id="35d4b117-4e60-44a3-9580-c582117eff98",
            data={"discriminator": "Ideal"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(PaymentAddAlternativeResponse, payment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_add_alternative(self, client: Pymews) -> None:
        with client.api.connector.v1.payments.with_streaming_response.add_alternative(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            amount={
                "currency": "GBP",
                "tax_codes": ["string"],
            },
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_id="35d4b117-4e60-44a3-9580-c582117eff98",
            data={"discriminator": "Ideal"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = response.parse()
            assert_matches_type(PaymentAddAlternativeResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_add_credit_card(self, client: Pymews) -> None:
        payment = client.api.connector.v1.payments.add_credit_card(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            amount={"currency": "GBP"},
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            credit_card={
                "name": "John Smith",
                "number": "411111******1111",
                "type": "Visa",
            },
            customer_id="35d4b117-4e60-44a3-9580-c582117eff98",
        )
        assert_matches_type(AddCreditCardResult, payment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_add_credit_card_with_all_params(self, client: Pymews) -> None:
        payment = client.api.connector.v1.payments.add_credit_card(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            amount={
                "currency": "GBP",
                "gross_value": 100,
                "net_value": 0,
                "tax_codes": ["string"],
            },
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            credit_card={
                "name": "John Smith",
                "number": "411111******1111",
                "type": "Visa",
                "expiration": "12/2016",
            },
            customer_id="35d4b117-4e60-44a3-9580-c582117eff98",
            accounting_category_id=None,
            bill_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            notes="Terminal A",
            receipt_identifier="123456",
            reservation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AddCreditCardResult, payment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_add_credit_card(self, client: Pymews) -> None:
        response = client.api.connector.v1.payments.with_raw_response.add_credit_card(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            amount={"currency": "GBP"},
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            credit_card={
                "name": "John Smith",
                "number": "411111******1111",
                "type": "Visa",
            },
            customer_id="35d4b117-4e60-44a3-9580-c582117eff98",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(AddCreditCardResult, payment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_add_credit_card(self, client: Pymews) -> None:
        with client.api.connector.v1.payments.with_streaming_response.add_credit_card(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            amount={"currency": "GBP"},
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            credit_card={
                "name": "John Smith",
                "number": "411111******1111",
                "type": "Visa",
            },
            customer_id="35d4b117-4e60-44a3-9580-c582117eff98",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = response.parse()
            assert_matches_type(AddCreditCardResult, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_add_external(self, client: Pymews) -> None:
        payment = client.api.connector.v1.payments.add_external(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            account_id="35d4b117-4e60-44a3-9580-c582117eff98",
            amount={"currency": "GBP"},
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )
        assert_matches_type(PaymentAddExternalResponse, payment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_add_external_with_all_params(self, client: Pymews) -> None:
        payment = client.api.connector.v1.payments.add_external(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            account_id="35d4b117-4e60-44a3-9580-c582117eff98",
            amount={
                "currency": "GBP",
                "gross_value": 100,
                "net_value": 0,
                "tax_codes": ["string"],
            },
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            accounting_category_id=None,
            bill_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            enterprise_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
            external_identifier="b06de5e4-7137-47ec-8a49-3303131b02c0",
            notes="Notes",
            reservation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="Cash",
        )
        assert_matches_type(PaymentAddExternalResponse, payment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_add_external(self, client: Pymews) -> None:
        response = client.api.connector.v1.payments.with_raw_response.add_external(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            account_id="35d4b117-4e60-44a3-9580-c582117eff98",
            amount={"currency": "GBP"},
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(PaymentAddExternalResponse, payment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_add_external(self, client: Pymews) -> None:
        with client.api.connector.v1.payments.with_streaming_response.add_external(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            account_id="35d4b117-4e60-44a3-9580-c582117eff98",
            amount={"currency": "GBP"},
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = response.parse()
            assert_matches_type(PaymentAddExternalResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_refund(self, client: Pymews) -> None:
        payment = client.api.connector.v1.payments.refund(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            account_id="fadd5bb6-b428-45d5-94f8-fd0d89fece6d",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            payment_id="f6313945-94c1-4e27-b402-031c2a8c989f",
            reason="Sample reason",
        )
        assert_matches_type(PaymentRefundResponse, payment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_refund_with_all_params(self, client: Pymews) -> None:
        payment = client.api.connector.v1.payments.refund(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            account_id="fadd5bb6-b428-45d5-94f8-fd0d89fece6d",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            payment_id="f6313945-94c1-4e27-b402-031c2a8c989f",
            reason="Sample reason",
            enterprise_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
            value_to_refund=110.5,
        )
        assert_matches_type(PaymentRefundResponse, payment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_refund(self, client: Pymews) -> None:
        response = client.api.connector.v1.payments.with_raw_response.refund(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            account_id="fadd5bb6-b428-45d5-94f8-fd0d89fece6d",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            payment_id="f6313945-94c1-4e27-b402-031c2a8c989f",
            reason="Sample reason",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(PaymentRefundResponse, payment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_refund(self, client: Pymews) -> None:
        with client.api.connector.v1.payments.with_streaming_response.refund(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            account_id="fadd5bb6-b428-45d5-94f8-fd0d89fece6d",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            payment_id="f6313945-94c1-4e27-b402-031c2a8c989f",
            reason="Sample reason",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = response.parse()
            assert_matches_type(PaymentRefundResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPayments:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncPymews) -> None:
        payment = await async_client.api.connector.v1.payments.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )
        assert_matches_type(PaymentListResponse, payment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPymews) -> None:
        payment = await async_client.api.connector.v1.payments.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            account_ids=["fadd5bb6-b428-45d5-94f8-fd0d89fece6d"],
            accounting_states=["Closed", "Open"],
            bill_ids=["ea087d64-3901-4eee-b0b7-9fce4c58a005", "d23ac52f-9b86-4a03-a6fe-5822dfcfc5c4"],
            charged_utc={
                "end_utc": parse_datetime("2023-03-31T00:00:00Z"),
                "start_utc": parse_datetime("2023-03-01T00:00:00Z"),
            },
            closed_utc={
                "end_utc": parse_datetime("2023-03-31T00:00:00Z"),
                "start_utc": parse_datetime("2023-03-01T00:00:00Z"),
            },
            created_utc={
                "end_utc": parse_datetime("2023-03-31T00:00:00Z"),
                "start_utc": parse_datetime("2023-03-01T00:00:00Z"),
            },
            currency="EUR",
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            payment_ids=["f6313945-94c1-4e27-b402-031c2a8c989f", "be922eb7-bc5f-4877-b847-1120c0c2acd2"],
            reservation_ids=["0f515589-99b4-423d-b83a-b237009f0509", "b7a3f5cb-1e69-4a5f-a069-10f461996d7f"],
            settlement_utc={
                "end_utc": parse_datetime("2023-03-31T00:00:00Z"),
                "start_utc": parse_datetime("2023-03-01T00:00:00Z"),
            },
            states=["Charged", "Pending"],
            type="Payment",
            updated_utc={
                "end_utc": parse_datetime("2023-03-31T00:00:00Z"),
                "start_utc": parse_datetime("2023-03-01T00:00:00Z"),
            },
        )
        assert_matches_type(PaymentListResponse, payment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.payments.with_raw_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = await response.parse()
        assert_matches_type(PaymentListResponse, payment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.payments.with_streaming_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert_matches_type(PaymentListResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_add_alternative(self, async_client: AsyncPymews) -> None:
        payment = await async_client.api.connector.v1.payments.add_alternative(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            amount={
                "currency": "GBP",
                "tax_codes": ["string"],
            },
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_id="35d4b117-4e60-44a3-9580-c582117eff98",
            data={"discriminator": "Ideal"},
        )
        assert_matches_type(PaymentAddAlternativeResponse, payment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_add_alternative_with_all_params(self, async_client: AsyncPymews) -> None:
        payment = await async_client.api.connector.v1.payments.add_alternative(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            amount={
                "currency": "GBP",
                "tax_codes": ["string"],
                "gross_value": 100,
                "net_value": 0,
            },
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_id="35d4b117-4e60-44a3-9580-c582117eff98",
            data={
                "discriminator": "Ideal",
                "ideal": {"redirect_url": "https://example.com"},
                "sepa_direct_debit": {
                    "email": "dev@stainless.com",
                    "iban": "x",
                    "name": "x",
                    "remote_ip_address": "x",
                    "user_agent": "x",
                },
            },
            method="Ideal",
            redirect_url="https://mews.com",
            reservation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PaymentAddAlternativeResponse, payment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_add_alternative(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.payments.with_raw_response.add_alternative(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            amount={
                "currency": "GBP",
                "tax_codes": ["string"],
            },
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_id="35d4b117-4e60-44a3-9580-c582117eff98",
            data={"discriminator": "Ideal"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = await response.parse()
        assert_matches_type(PaymentAddAlternativeResponse, payment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_add_alternative(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.payments.with_streaming_response.add_alternative(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            amount={
                "currency": "GBP",
                "tax_codes": ["string"],
            },
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_id="35d4b117-4e60-44a3-9580-c582117eff98",
            data={"discriminator": "Ideal"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert_matches_type(PaymentAddAlternativeResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_add_credit_card(self, async_client: AsyncPymews) -> None:
        payment = await async_client.api.connector.v1.payments.add_credit_card(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            amount={"currency": "GBP"},
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            credit_card={
                "name": "John Smith",
                "number": "411111******1111",
                "type": "Visa",
            },
            customer_id="35d4b117-4e60-44a3-9580-c582117eff98",
        )
        assert_matches_type(AddCreditCardResult, payment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_add_credit_card_with_all_params(self, async_client: AsyncPymews) -> None:
        payment = await async_client.api.connector.v1.payments.add_credit_card(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            amount={
                "currency": "GBP",
                "gross_value": 100,
                "net_value": 0,
                "tax_codes": ["string"],
            },
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            credit_card={
                "name": "John Smith",
                "number": "411111******1111",
                "type": "Visa",
                "expiration": "12/2016",
            },
            customer_id="35d4b117-4e60-44a3-9580-c582117eff98",
            accounting_category_id=None,
            bill_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            notes="Terminal A",
            receipt_identifier="123456",
            reservation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AddCreditCardResult, payment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_add_credit_card(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.payments.with_raw_response.add_credit_card(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            amount={"currency": "GBP"},
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            credit_card={
                "name": "John Smith",
                "number": "411111******1111",
                "type": "Visa",
            },
            customer_id="35d4b117-4e60-44a3-9580-c582117eff98",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = await response.parse()
        assert_matches_type(AddCreditCardResult, payment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_add_credit_card(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.payments.with_streaming_response.add_credit_card(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            amount={"currency": "GBP"},
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            credit_card={
                "name": "John Smith",
                "number": "411111******1111",
                "type": "Visa",
            },
            customer_id="35d4b117-4e60-44a3-9580-c582117eff98",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert_matches_type(AddCreditCardResult, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_add_external(self, async_client: AsyncPymews) -> None:
        payment = await async_client.api.connector.v1.payments.add_external(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            account_id="35d4b117-4e60-44a3-9580-c582117eff98",
            amount={"currency": "GBP"},
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )
        assert_matches_type(PaymentAddExternalResponse, payment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_add_external_with_all_params(self, async_client: AsyncPymews) -> None:
        payment = await async_client.api.connector.v1.payments.add_external(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            account_id="35d4b117-4e60-44a3-9580-c582117eff98",
            amount={
                "currency": "GBP",
                "gross_value": 100,
                "net_value": 0,
                "tax_codes": ["string"],
            },
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            accounting_category_id=None,
            bill_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            enterprise_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
            external_identifier="b06de5e4-7137-47ec-8a49-3303131b02c0",
            notes="Notes",
            reservation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="Cash",
        )
        assert_matches_type(PaymentAddExternalResponse, payment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_add_external(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.payments.with_raw_response.add_external(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            account_id="35d4b117-4e60-44a3-9580-c582117eff98",
            amount={"currency": "GBP"},
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = await response.parse()
        assert_matches_type(PaymentAddExternalResponse, payment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_add_external(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.payments.with_streaming_response.add_external(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            account_id="35d4b117-4e60-44a3-9580-c582117eff98",
            amount={"currency": "GBP"},
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert_matches_type(PaymentAddExternalResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_refund(self, async_client: AsyncPymews) -> None:
        payment = await async_client.api.connector.v1.payments.refund(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            account_id="fadd5bb6-b428-45d5-94f8-fd0d89fece6d",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            payment_id="f6313945-94c1-4e27-b402-031c2a8c989f",
            reason="Sample reason",
        )
        assert_matches_type(PaymentRefundResponse, payment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_refund_with_all_params(self, async_client: AsyncPymews) -> None:
        payment = await async_client.api.connector.v1.payments.refund(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            account_id="fadd5bb6-b428-45d5-94f8-fd0d89fece6d",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            payment_id="f6313945-94c1-4e27-b402-031c2a8c989f",
            reason="Sample reason",
            enterprise_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
            value_to_refund=110.5,
        )
        assert_matches_type(PaymentRefundResponse, payment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_refund(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.payments.with_raw_response.refund(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            account_id="fadd5bb6-b428-45d5-94f8-fd0d89fece6d",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            payment_id="f6313945-94c1-4e27-b402-031c2a8c989f",
            reason="Sample reason",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = await response.parse()
        assert_matches_type(PaymentRefundResponse, payment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_refund(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.payments.with_streaming_response.refund(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            account_id="fadd5bb6-b428-45d5-94f8-fd0d89fece6d",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            payment_id="f6313945-94c1-4e27-b402-031c2a8c989f",
            reason="Sample reason",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert_matches_type(PaymentRefundResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True
