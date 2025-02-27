# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pymews import Pymews, AsyncPymews
from tests.utils import assert_matches_type
from pymews._utils import parse_datetime
from pymews.types.api.connector.v1 import (
    ReservationResult,
    ReservationAddResponse,
    ReservationPriceResponse,
    MultipleReservationResult,
    ReservationAddProductResponse,
    ReservationGetAllItemsResponse,
    ReservationAddCompanionResponse,
    ReservationGetAll2023_06_06Response,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReservations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Pymews) -> None:
        reservation = client.api.connector.v1.reservations.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            reservation_updates=[
                {
                    "access_token": "x",
                    "client": "x",
                    "client_token": "x",
                    "reservation_id": "622605a9-2969-441f-9610-aa720099ae1c",
                }
            ],
        )
        assert_matches_type(ReservationResult, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Pymews) -> None:
        reservation = client.api.connector.v1.reservations.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            reservation_updates=[
                {
                    "access_token": "x",
                    "client": "x",
                    "client_token": "x",
                    "reservation_id": "622605a9-2969-441f-9610-aa720099ae1c",
                    "assigned_resource_id": {"value": "16ce4335-2198-408b-8949-9722894a42fb"},
                    "assigned_resource_locked": {"value": True},
                    "availability_block_id": {"value": "aaaa654a4a94-4f96-9efc-86da-bd26d8db"},
                    "booker_id": {"value": "92923102-bf91-4a4a-8ee8-9dcb79c9d6de"},
                    "business_segment_id": {"value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                    "channel_number": {"value": "Value"},
                    "company_id": {"value": "73ba34d1-f375-460c-bf2d-8a63e71677a6"},
                    "credit_card_id": {"value": "5d802a8f-3238-42b2-94be-ab0300ab2b6c"},
                    "end_utc": {"value": "2019-10-03T10:00:00Z"},
                    "enterprise_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "options": {"owner_checked_in": {"value": True}},
                    "person_counts": {
                        "value": [
                            {
                                "age_category_id": "ab58c939-be30-4a60-8f75-ae1600c60c9f",
                                "count": 2,
                            },
                            {
                                "age_category_id": "1f67644f-052d-4863-acdf-ae1600c60ca0",
                                "count": 2,
                            },
                        ]
                    },
                    "purpose": {"value": "Business"},
                    "rate_id": {"value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                    "released_utc": {"value": "Value"},
                    "requested_category_id": {"value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                    "start_utc": {"value": "2019-10-01T14:00:00Z"},
                    "time_unit_prices": {
                        "value": [
                            {
                                "amount": {
                                    "currency": "GBP",
                                    "tax_codes": ["UK-S"],
                                    "gross_value": 20,
                                    "net_value": 0,
                                },
                                "index": 0,
                            },
                            {
                                "amount": {
                                    "currency": "GBP",
                                    "tax_codes": ["UK-S"],
                                    "gross_value": 30,
                                    "net_value": 0,
                                },
                                "index": 1,
                            },
                        ]
                    },
                    "travel_agency_id": {"value": None},
                }
            ],
            apply_cancellation_fee=True,
            assigned_resource_id={"value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
            assigned_resource_locked={"value": True},
            availability_block_id={"value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
            booker_id={"value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
            business_segment_id={"value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
            channel_number={"value": "Value"},
            check_overbooking=True,
            check_rate_applicability=True,
            company_id={"value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
            credit_card_id={"value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
            end_utc={"value": "Value"},
            enterprise_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
            options={"owner_checked_in": {"value": True}},
            person_counts={
                "value": [
                    {
                        "age_category_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "count": 0,
                    }
                ]
            },
            purpose={"value": "Value"},
            rate_id={"value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
            reason="Testing",
            released_utc={"value": "Value"},
            reprice=True,
            requested_category_id={"value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
            start_utc={"value": "Value"},
            time_unit_prices={
                "value": [
                    {
                        "amount": {
                            "currency": "x",
                            "tax_codes": ["string"],
                            "gross_value": 0,
                            "net_value": 0,
                        },
                        "index": 0,
                    }
                ]
            },
            travel_agency_id={"value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
        )
        assert_matches_type(ReservationResult, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Pymews) -> None:
        response = client.api.connector.v1.reservations.with_raw_response.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            reservation_updates=[
                {
                    "access_token": "x",
                    "client": "x",
                    "client_token": "x",
                    "reservation_id": "622605a9-2969-441f-9610-aa720099ae1c",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reservation = response.parse()
        assert_matches_type(ReservationResult, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Pymews) -> None:
        with client.api.connector.v1.reservations.with_streaming_response.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            reservation_updates=[
                {
                    "access_token": "x",
                    "client": "x",
                    "client_token": "x",
                    "reservation_id": "622605a9-2969-441f-9610-aa720099ae1c",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reservation = response.parse()
            assert_matches_type(ReservationResult, reservation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_add(self, client: Pymews) -> None:
        reservation = client.api.connector.v1.reservations.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservations=[
                {
                    "customer_id": "e465c031-fd99-4546-8c70-abcf0029c249",
                    "end_utc": parse_datetime("2021-01-03T10:00:00Z"),
                    "person_counts": [
                        {
                            "age_category_id": "1f67644f-052d-4863-acdf-ae1600c60ca0",
                            "count": 2,
                        },
                        {
                            "age_category_id": "ab58c939-be30-4a60-8f75-ae1600c60c9f",
                            "count": 2,
                        },
                    ],
                    "rate_id": "a39a59fa-3a08-4822-bdd4-ab0b00e3d21f",
                    "requested_category_id": "0a5da171-3663-4496-a61e-35ecbd78b9b1",
                    "start_utc": parse_datetime("2021-01-01T14:00:00Z"),
                }
            ],
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
        )
        assert_matches_type(ReservationAddResponse, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_add_with_all_params(self, client: Pymews) -> None:
        reservation = client.api.connector.v1.reservations.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservations=[
                {
                    "customer_id": "e465c031-fd99-4546-8c70-abcf0029c249",
                    "end_utc": parse_datetime("2021-01-03T10:00:00Z"),
                    "person_counts": [
                        {
                            "age_category_id": "1f67644f-052d-4863-acdf-ae1600c60ca0",
                            "count": 2,
                        },
                        {
                            "age_category_id": "ab58c939-be30-4a60-8f75-ae1600c60c9f",
                            "count": 2,
                        },
                    ],
                    "rate_id": "a39a59fa-3a08-4822-bdd4-ab0b00e3d21f",
                    "requested_category_id": "0a5da171-3663-4496-a61e-35ecbd78b9b1",
                    "start_utc": parse_datetime("2021-01-01T14:00:00Z"),
                    "adult_count": 0,
                    "availability_block_id": None,
                    "booker_id": "e465c031-fd99-4546-8c70-abcf0029c249",
                    "business_segment_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "channel_number": "ChannelNumber",
                    "child_count": 0,
                    "company_id": None,
                    "credit_card_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "identifier": "1234",
                    "notes": "Test reservation",
                    "product_orders": [
                        {
                            "product_id": "2e9eb3fc-8a77-466a-9cd9-abcf002a2a01",
                            "count": 0,
                            "end_utc": parse_datetime("2021-01-03T00:00:00Z"),
                            "external_identifier": "ExternalIdentifier",
                            "start_utc": parse_datetime("2021-01-02T00:00:00Z"),
                            "unit_amount": {
                                "currency": "x",
                                "tax_codes": ["string"],
                                "gross_value": 0,
                                "net_value": 0,
                            },
                        }
                    ],
                    "released_utc": None,
                    "state": "Inquired",
                    "time_unit_amount": {
                        "currency": "x",
                        "tax_codes": ["string"],
                        "gross_value": 0,
                        "net_value": 0,
                    },
                    "time_unit_prices": [
                        {
                            "amount": {
                                "currency": "GBP",
                                "tax_codes": ["UK-S"],
                                "gross_value": 20,
                                "net_value": 0,
                            },
                            "index": 0,
                        },
                        {
                            "amount": {
                                "currency": "GBP",
                                "tax_codes": ["UK-S"],
                                "gross_value": 30,
                                "net_value": 0,
                            },
                            "index": 1,
                        },
                    ],
                    "travel_agency_id": None,
                    "voucher_code": "SpringSale2021",
                }
            ],
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
            check_overbooking=True,
            check_rate_applicability=True,
            enterprise_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            group_id=None,
            group_name=None,
            send_confirmation_email=True,
        )
        assert_matches_type(ReservationAddResponse, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_add(self, client: Pymews) -> None:
        response = client.api.connector.v1.reservations.with_raw_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservations=[
                {
                    "customer_id": "e465c031-fd99-4546-8c70-abcf0029c249",
                    "end_utc": parse_datetime("2021-01-03T10:00:00Z"),
                    "person_counts": [
                        {
                            "age_category_id": "1f67644f-052d-4863-acdf-ae1600c60ca0",
                            "count": 2,
                        },
                        {
                            "age_category_id": "ab58c939-be30-4a60-8f75-ae1600c60c9f",
                            "count": 2,
                        },
                    ],
                    "rate_id": "a39a59fa-3a08-4822-bdd4-ab0b00e3d21f",
                    "requested_category_id": "0a5da171-3663-4496-a61e-35ecbd78b9b1",
                    "start_utc": parse_datetime("2021-01-01T14:00:00Z"),
                }
            ],
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reservation = response.parse()
        assert_matches_type(ReservationAddResponse, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_add(self, client: Pymews) -> None:
        with client.api.connector.v1.reservations.with_streaming_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservations=[
                {
                    "customer_id": "e465c031-fd99-4546-8c70-abcf0029c249",
                    "end_utc": parse_datetime("2021-01-03T10:00:00Z"),
                    "person_counts": [
                        {
                            "age_category_id": "1f67644f-052d-4863-acdf-ae1600c60ca0",
                            "count": 2,
                        },
                        {
                            "age_category_id": "ab58c939-be30-4a60-8f75-ae1600c60c9f",
                            "count": 2,
                        },
                    ],
                    "rate_id": "a39a59fa-3a08-4822-bdd4-ab0b00e3d21f",
                    "requested_category_id": "0a5da171-3663-4496-a61e-35ecbd78b9b1",
                    "start_utc": parse_datetime("2021-01-01T14:00:00Z"),
                }
            ],
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reservation = response.parse()
            assert_matches_type(ReservationAddResponse, reservation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_add_companion(self, client: Pymews) -> None:
        reservation = client.api.connector.v1.reservations.add_companion(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_id="35d4b117-4e60-44a3-9580-c582117eff98",
            reservation_id="e6ea708c-2a2a-412f-a152-b6c76ffad49b",
        )
        assert_matches_type(ReservationAddCompanionResponse, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_add_companion_with_all_params(self, client: Pymews) -> None:
        reservation = client.api.connector.v1.reservations.add_companion(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_id="35d4b117-4e60-44a3-9580-c582117eff98",
            reservation_id="e6ea708c-2a2a-412f-a152-b6c76ffad49b",
            enterprise_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ReservationAddCompanionResponse, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_add_companion(self, client: Pymews) -> None:
        response = client.api.connector.v1.reservations.with_raw_response.add_companion(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_id="35d4b117-4e60-44a3-9580-c582117eff98",
            reservation_id="e6ea708c-2a2a-412f-a152-b6c76ffad49b",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reservation = response.parse()
        assert_matches_type(ReservationAddCompanionResponse, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_add_companion(self, client: Pymews) -> None:
        with client.api.connector.v1.reservations.with_streaming_response.add_companion(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_id="35d4b117-4e60-44a3-9580-c582117eff98",
            reservation_id="e6ea708c-2a2a-412f-a152-b6c76ffad49b",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reservation = response.parse()
            assert_matches_type(ReservationAddCompanionResponse, reservation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_add_product(self, client: Pymews) -> None:
        reservation = client.api.connector.v1.reservations.add_product(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            count=1,
            product_id="47312820-2268-4f5c-864d-aa4100ed82bc",
            reservation_id="4d2aa234-5d30-472c-899f-ab45008c3479",
        )
        assert_matches_type(ReservationAddProductResponse, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_add_product_with_all_params(self, client: Pymews) -> None:
        reservation = client.api.connector.v1.reservations.add_product(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            count=1,
            product_id="47312820-2268-4f5c-864d-aa4100ed82bc",
            reservation_id="4d2aa234-5d30-472c-899f-ab45008c3479",
            end_utc=parse_datetime("2021-01-03T00:00:00Z"),
            start_utc=parse_datetime("2021-01-02T00:00:00Z"),
            unit_amount={
                "currency": "GBP",
                "tax_codes": ["UK-S"],
                "gross_value": 10,
                "net_value": 0,
            },
        )
        assert_matches_type(ReservationAddProductResponse, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_add_product(self, client: Pymews) -> None:
        response = client.api.connector.v1.reservations.with_raw_response.add_product(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            count=1,
            product_id="47312820-2268-4f5c-864d-aa4100ed82bc",
            reservation_id="4d2aa234-5d30-472c-899f-ab45008c3479",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reservation = response.parse()
        assert_matches_type(ReservationAddProductResponse, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_add_product(self, client: Pymews) -> None:
        with client.api.connector.v1.reservations.with_streaming_response.add_product(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            count=1,
            product_id="47312820-2268-4f5c-864d-aa4100ed82bc",
            reservation_id="4d2aa234-5d30-472c-899f-ab45008c3479",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reservation = response.parse()
            assert_matches_type(ReservationAddProductResponse, reservation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_cancel(self, client: Pymews) -> None:
        reservation = client.api.connector.v1.reservations.cancel(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservation_ids=["5ca70705-cbb7-48c4-8cc4-abb900aa278c"],
        )
        assert_matches_type(MultipleReservationResult, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_cancel_with_all_params(self, client: Pymews) -> None:
        reservation = client.api.connector.v1.reservations.cancel(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservation_ids=["5ca70705-cbb7-48c4-8cc4-abb900aa278c"],
            enterprise_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
            notes="Cancellation through Connector API",
            post_cancellation_fee=True,
            reservation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            send_email=True,
        )
        assert_matches_type(MultipleReservationResult, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_cancel(self, client: Pymews) -> None:
        response = client.api.connector.v1.reservations.with_raw_response.cancel(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservation_ids=["5ca70705-cbb7-48c4-8cc4-abb900aa278c"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reservation = response.parse()
        assert_matches_type(MultipleReservationResult, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_cancel(self, client: Pymews) -> None:
        with client.api.connector.v1.reservations.with_streaming_response.cancel(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservation_ids=["5ca70705-cbb7-48c4-8cc4-abb900aa278c"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reservation = response.parse()
            assert_matches_type(MultipleReservationResult, reservation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_confirm(self, client: Pymews) -> None:
        reservation = client.api.connector.v1.reservations.confirm(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservation_ids=["9af9d8b0-43ae-414d-80a8-abc1012a2a59"],
        )
        assert_matches_type(MultipleReservationResult, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_confirm_with_all_params(self, client: Pymews) -> None:
        reservation = client.api.connector.v1.reservations.confirm(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservation_ids=["9af9d8b0-43ae-414d-80a8-abc1012a2a59"],
            enterprise_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            send_confirmation_email=True,
        )
        assert_matches_type(MultipleReservationResult, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_confirm(self, client: Pymews) -> None:
        response = client.api.connector.v1.reservations.with_raw_response.confirm(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservation_ids=["9af9d8b0-43ae-414d-80a8-abc1012a2a59"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reservation = response.parse()
        assert_matches_type(MultipleReservationResult, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_confirm(self, client: Pymews) -> None:
        with client.api.connector.v1.reservations.with_streaming_response.confirm(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservation_ids=["9af9d8b0-43ae-414d-80a8-abc1012a2a59"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reservation = response.parse()
            assert_matches_type(MultipleReservationResult, reservation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete_companion(self, client: Pymews) -> None:
        reservation = client.api.connector.v1.reservations.delete_companion(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_id="35d4b117-4e60-44a3-9580-c582117eff98",
            reservation_id="e6ea708c-2a2a-412f-a152-b6c76ffad49b",
        )
        assert_matches_type(object, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_delete_companion_with_all_params(self, client: Pymews) -> None:
        reservation = client.api.connector.v1.reservations.delete_companion(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_id="35d4b117-4e60-44a3-9580-c582117eff98",
            reservation_id="e6ea708c-2a2a-412f-a152-b6c76ffad49b",
            enterprise_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete_companion(self, client: Pymews) -> None:
        response = client.api.connector.v1.reservations.with_raw_response.delete_companion(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_id="35d4b117-4e60-44a3-9580-c582117eff98",
            reservation_id="e6ea708c-2a2a-412f-a152-b6c76ffad49b",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reservation = response.parse()
        assert_matches_type(object, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete_companion(self, client: Pymews) -> None:
        with client.api.connector.v1.reservations.with_streaming_response.delete_companion(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_id="35d4b117-4e60-44a3-9580-c582117eff98",
            reservation_id="e6ea708c-2a2a-412f-a152-b6c76ffad49b",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reservation = response.parse()
            assert_matches_type(object, reservation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_all(self, client: Pymews) -> None:
        reservation = client.api.connector.v1.reservations.get_all(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            extent={},
            limitation={"count": 10},
            service_ids=["bd26d8db-86da-4f96-9efc-e5a4654a4a94"],
        )
        assert_matches_type(ReservationResult, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_all_with_all_params(self, client: Pymews) -> None:
        reservation = client.api.connector.v1.reservations.get_all(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            extent={
                "accounting_states": ["Open"],
                "business_segments": True,
                "companies": True,
                "customer_adresses": True,
                "customer_identity_documents": True,
                "customers": True,
                "items": True,
                "notes": True,
                "order_items": True,
                "products": True,
                "qr_code_data": True,
                "rates": True,
                "reservation_groups": True,
                "reservations": True,
                "resource_categories": True,
                "resource_category_assignments": True,
                "resources": True,
                "services": True,
            },
            limitation={
                "count": 10,
                "cursor": "e7f26210-10e7-462e-9da8-ae8300be8ab7",
            },
            service_ids=["bd26d8db-86da-4f96-9efc-e5a4654a4a94"],
            assigned_resource_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            business_segment_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            channel_numbers=["TW48ZP"],
            currency="Currency",
            customer_ids=["8e1d0ca6-1dde-4be0-8566-aafc01866110"],
            end_utc=parse_datetime("2016-01-07T00:00:00Z"),
            group_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            numbers=["string"],
            rate_ids=["ed4b660b-19d0-434b-9360-a4de2ea42eda"],
            reservation_ids=["db6cad34-9a91-448b-bea1-abbe01240d9c"],
            service_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            start_utc=parse_datetime("2016-01-01T00:00:00Z"),
            states=["Enquired"],
            time_filter="Colliding",
        )
        assert_matches_type(ReservationResult, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_all(self, client: Pymews) -> None:
        response = client.api.connector.v1.reservations.with_raw_response.get_all(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            extent={},
            limitation={"count": 10},
            service_ids=["bd26d8db-86da-4f96-9efc-e5a4654a4a94"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reservation = response.parse()
        assert_matches_type(ReservationResult, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_all(self, client: Pymews) -> None:
        with client.api.connector.v1.reservations.with_streaming_response.get_all(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            extent={},
            limitation={"count": 10},
            service_ids=["bd26d8db-86da-4f96-9efc-e5a4654a4a94"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reservation = response.parse()
            assert_matches_type(ReservationResult, reservation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_all_2023_06_06(self, client: Pymews) -> None:
        reservation = client.api.connector.v1.reservations.get_all_2023_06_06(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )
        assert_matches_type(ReservationGetAll2023_06_06Response, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_all_2023_06_06_with_all_params(self, client: Pymews) -> None:
        reservation = client.api.connector.v1.reservations.get_all_2023_06_06(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            account_ids=["fadd5bb6-b428-45d5-94f8-fd0d89fece6d"],
            actual_start_utc={
                "end_utc": parse_datetime("2019-12-27T18:11:19.117Z"),
                "start_utc": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            assigned_resource_ids=["5ee074b1-6c86-48e8-915f-c7aa4702086f", "c32386aa-1cd2-414a-a823-489325842fbe"],
            availability_block_ids=["5ee074b1-6c86-48e8-915f-c7aa4702086f", "c32386aa-1cd2-414a-a823-489325842fbe"],
            colliding_utc={
                "end_utc": parse_datetime("2023-05-05T00:00:00Z"),
                "start_utc": parse_datetime("2023-04-01T00:00:00Z"),
            },
            created_utc={
                "end_utc": parse_datetime("2023-05-05T00:00:00Z"),
                "start_utc": parse_datetime("2023-04-01T00:00:00Z"),
            },
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            numbers=["50", "51", "52", "53"],
            reservation_group_ids=["94843f6f-3be3-481b-a1c7-06458774c3df"],
            reservation_ids=["0f515589-99b4-423d-b83a-b237009f0509", "9b59b50d-bd32-4ce5-add8-09ea0e1300e7"],
            scheduled_end_utc={
                "end_utc": parse_datetime("2023-05-05T00:00:00Z"),
                "start_utc": parse_datetime("2023-04-01T00:00:00Z"),
            },
            scheduled_start_utc={
                "end_utc": parse_datetime("2023-05-05T00:00:00Z"),
                "start_utc": parse_datetime("2023-04-01T00:00:00Z"),
            },
            service_ids=["bd26d8db-86da-4f96-9efc-e5a4654a4a94", "8c1bd738-a505-4b29-aa71-9ecc2982b843"],
            states=["Inquired", "Confirmed"],
            updated_utc={
                "end_utc": parse_datetime("2023-05-05T00:00:00Z"),
                "start_utc": parse_datetime("2023-04-01T00:00:00Z"),
            },
        )
        assert_matches_type(ReservationGetAll2023_06_06Response, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_all_2023_06_06(self, client: Pymews) -> None:
        response = client.api.connector.v1.reservations.with_raw_response.get_all_2023_06_06(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reservation = response.parse()
        assert_matches_type(ReservationGetAll2023_06_06Response, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_all_2023_06_06(self, client: Pymews) -> None:
        with client.api.connector.v1.reservations.with_streaming_response.get_all_2023_06_06(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reservation = response.parse()
            assert_matches_type(ReservationGetAll2023_06_06Response, reservation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_all_items(self, client: Pymews) -> None:
        reservation = client.api.connector.v1.reservations.get_all_items(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservation_ids=["e6ea708c-2a2a-412f-a152-b6c76ffad49b"],
        )
        assert_matches_type(ReservationGetAllItemsResponse, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_all_items_with_all_params(self, client: Pymews) -> None:
        reservation = client.api.connector.v1.reservations.get_all_items(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservation_ids=["e6ea708c-2a2a-412f-a152-b6c76ffad49b"],
            accounting_states=["Closed"],
            currency="EUR",
        )
        assert_matches_type(ReservationGetAllItemsResponse, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_all_items(self, client: Pymews) -> None:
        response = client.api.connector.v1.reservations.with_raw_response.get_all_items(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservation_ids=["e6ea708c-2a2a-412f-a152-b6c76ffad49b"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reservation = response.parse()
        assert_matches_type(ReservationGetAllItemsResponse, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_all_items(self, client: Pymews) -> None:
        with client.api.connector.v1.reservations.with_streaming_response.get_all_items(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservation_ids=["e6ea708c-2a2a-412f-a152-b6c76ffad49b"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reservation = response.parse()
            assert_matches_type(ReservationGetAllItemsResponse, reservation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_price(self, client: Pymews) -> None:
        reservation = client.api.connector.v1.reservations.price(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservations=[
                {
                    "customer_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "end_utc": parse_datetime("2018-01-02T10:00:00Z"),
                    "person_counts": [
                        {
                            "age_category_id": "1f67644f-052d-4863-acdf-ae1600c60ca0",
                            "count": 2,
                        },
                        {
                            "age_category_id": "ab58c939-be30-4a60-8f75-ae1600c60c9f",
                            "count": 2,
                        },
                    ],
                    "rate_id": "33667cab-f17f-4089-ad07-c2cd50fa0df1",
                    "requested_category_id": "0a5da171-3663-4496-a61e-35ecbd78b9b1",
                    "start_utc": parse_datetime("2018-01-01T14:00:00Z"),
                }
            ],
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
        )
        assert_matches_type(ReservationPriceResponse, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_price(self, client: Pymews) -> None:
        response = client.api.connector.v1.reservations.with_raw_response.price(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservations=[
                {
                    "customer_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "end_utc": parse_datetime("2018-01-02T10:00:00Z"),
                    "person_counts": [
                        {
                            "age_category_id": "1f67644f-052d-4863-acdf-ae1600c60ca0",
                            "count": 2,
                        },
                        {
                            "age_category_id": "ab58c939-be30-4a60-8f75-ae1600c60c9f",
                            "count": 2,
                        },
                    ],
                    "rate_id": "33667cab-f17f-4089-ad07-c2cd50fa0df1",
                    "requested_category_id": "0a5da171-3663-4496-a61e-35ecbd78b9b1",
                    "start_utc": parse_datetime("2018-01-01T14:00:00Z"),
                }
            ],
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reservation = response.parse()
        assert_matches_type(ReservationPriceResponse, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_price(self, client: Pymews) -> None:
        with client.api.connector.v1.reservations.with_streaming_response.price(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservations=[
                {
                    "customer_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "end_utc": parse_datetime("2018-01-02T10:00:00Z"),
                    "person_counts": [
                        {
                            "age_category_id": "1f67644f-052d-4863-acdf-ae1600c60ca0",
                            "count": 2,
                        },
                        {
                            "age_category_id": "ab58c939-be30-4a60-8f75-ae1600c60c9f",
                            "count": 2,
                        },
                    ],
                    "rate_id": "33667cab-f17f-4089-ad07-c2cd50fa0df1",
                    "requested_category_id": "0a5da171-3663-4496-a61e-35ecbd78b9b1",
                    "start_utc": parse_datetime("2018-01-01T14:00:00Z"),
                }
            ],
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reservation = response.parse()
            assert_matches_type(ReservationPriceResponse, reservation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_process(self, client: Pymews) -> None:
        reservation = client.api.connector.v1.reservations.process(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservation_id="e6ea708c-2a2a-412f-a152-b6c76ffad49b",
        )
        assert_matches_type(object, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_process_with_all_params(self, client: Pymews) -> None:
        reservation = client.api.connector.v1.reservations.process(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservation_id="e6ea708c-2a2a-412f-a152-b6c76ffad49b",
            allow_open_balance=False,
            close_bills=False,
            enterprise_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
            notes=None,
        )
        assert_matches_type(object, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_process(self, client: Pymews) -> None:
        response = client.api.connector.v1.reservations.with_raw_response.process(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservation_id="e6ea708c-2a2a-412f-a152-b6c76ffad49b",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reservation = response.parse()
        assert_matches_type(object, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_process(self, client: Pymews) -> None:
        with client.api.connector.v1.reservations.with_streaming_response.process(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservation_id="e6ea708c-2a2a-412f-a152-b6c76ffad49b",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reservation = response.parse()
            assert_matches_type(object, reservation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_start(self, client: Pymews) -> None:
        reservation = client.api.connector.v1.reservations.start(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservation_id="e6ea708c-2a2a-412f-a152-b6c76ffad49b",
        )
        assert_matches_type(object, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_start_with_all_params(self, client: Pymews) -> None:
        reservation = client.api.connector.v1.reservations.start(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservation_id="e6ea708c-2a2a-412f-a152-b6c76ffad49b",
            enterprise_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )
        assert_matches_type(object, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_start(self, client: Pymews) -> None:
        response = client.api.connector.v1.reservations.with_raw_response.start(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservation_id="e6ea708c-2a2a-412f-a152-b6c76ffad49b",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reservation = response.parse()
        assert_matches_type(object, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_start(self, client: Pymews) -> None:
        with client.api.connector.v1.reservations.with_streaming_response.start(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservation_id="e6ea708c-2a2a-412f-a152-b6c76ffad49b",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reservation = response.parse()
            assert_matches_type(object, reservation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_update_customer(self, client: Pymews) -> None:
        reservation = client.api.connector.v1.reservations.update_customer(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_id="35d4b117-4e60-44a3-9580-c582117eff98",
            reservation_id="209d984d-4985-4efb-96ec-f6591fc597bf",
        )
        assert_matches_type(object, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_customer_with_all_params(self, client: Pymews) -> None:
        reservation = client.api.connector.v1.reservations.update_customer(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_id="35d4b117-4e60-44a3-9580-c582117eff98",
            reservation_id="209d984d-4985-4efb-96ec-f6591fc597bf",
            enterprise_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )
        assert_matches_type(object, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update_customer(self, client: Pymews) -> None:
        response = client.api.connector.v1.reservations.with_raw_response.update_customer(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_id="35d4b117-4e60-44a3-9580-c582117eff98",
            reservation_id="209d984d-4985-4efb-96ec-f6591fc597bf",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reservation = response.parse()
        assert_matches_type(object, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update_customer(self, client: Pymews) -> None:
        with client.api.connector.v1.reservations.with_streaming_response.update_customer(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_id="35d4b117-4e60-44a3-9580-c582117eff98",
            reservation_id="209d984d-4985-4efb-96ec-f6591fc597bf",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reservation = response.parse()
            assert_matches_type(object, reservation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_update_interval(self, client: Pymews) -> None:
        reservation = client.api.connector.v1.reservations.update_interval(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            charge_cancellation_fee=False,
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservation_id="209d984d-4985-4efb-96ec-f6591fc597bf",
        )
        assert_matches_type(object, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_interval_with_all_params(self, client: Pymews) -> None:
        reservation = client.api.connector.v1.reservations.update_interval(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            charge_cancellation_fee=False,
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservation_id="209d984d-4985-4efb-96ec-f6591fc597bf",
            end_utc=parse_datetime("2017-08-15T12:00:00Z"),
            enterprise_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
            start_utc=parse_datetime("2017-08-12T15:00:00Z"),
        )
        assert_matches_type(object, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update_interval(self, client: Pymews) -> None:
        response = client.api.connector.v1.reservations.with_raw_response.update_interval(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            charge_cancellation_fee=False,
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservation_id="209d984d-4985-4efb-96ec-f6591fc597bf",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reservation = response.parse()
        assert_matches_type(object, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update_interval(self, client: Pymews) -> None:
        with client.api.connector.v1.reservations.with_streaming_response.update_interval(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            charge_cancellation_fee=False,
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservation_id="209d984d-4985-4efb-96ec-f6591fc597bf",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reservation = response.parse()
            assert_matches_type(object, reservation, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncReservations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncPymews) -> None:
        reservation = await async_client.api.connector.v1.reservations.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            reservation_updates=[
                {
                    "access_token": "x",
                    "client": "x",
                    "client_token": "x",
                    "reservation_id": "622605a9-2969-441f-9610-aa720099ae1c",
                }
            ],
        )
        assert_matches_type(ReservationResult, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncPymews) -> None:
        reservation = await async_client.api.connector.v1.reservations.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            reservation_updates=[
                {
                    "access_token": "x",
                    "client": "x",
                    "client_token": "x",
                    "reservation_id": "622605a9-2969-441f-9610-aa720099ae1c",
                    "assigned_resource_id": {"value": "16ce4335-2198-408b-8949-9722894a42fb"},
                    "assigned_resource_locked": {"value": True},
                    "availability_block_id": {"value": "aaaa654a4a94-4f96-9efc-86da-bd26d8db"},
                    "booker_id": {"value": "92923102-bf91-4a4a-8ee8-9dcb79c9d6de"},
                    "business_segment_id": {"value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                    "channel_number": {"value": "Value"},
                    "company_id": {"value": "73ba34d1-f375-460c-bf2d-8a63e71677a6"},
                    "credit_card_id": {"value": "5d802a8f-3238-42b2-94be-ab0300ab2b6c"},
                    "end_utc": {"value": "2019-10-03T10:00:00Z"},
                    "enterprise_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "options": {"owner_checked_in": {"value": True}},
                    "person_counts": {
                        "value": [
                            {
                                "age_category_id": "ab58c939-be30-4a60-8f75-ae1600c60c9f",
                                "count": 2,
                            },
                            {
                                "age_category_id": "1f67644f-052d-4863-acdf-ae1600c60ca0",
                                "count": 2,
                            },
                        ]
                    },
                    "purpose": {"value": "Business"},
                    "rate_id": {"value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                    "released_utc": {"value": "Value"},
                    "requested_category_id": {"value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                    "start_utc": {"value": "2019-10-01T14:00:00Z"},
                    "time_unit_prices": {
                        "value": [
                            {
                                "amount": {
                                    "currency": "GBP",
                                    "tax_codes": ["UK-S"],
                                    "gross_value": 20,
                                    "net_value": 0,
                                },
                                "index": 0,
                            },
                            {
                                "amount": {
                                    "currency": "GBP",
                                    "tax_codes": ["UK-S"],
                                    "gross_value": 30,
                                    "net_value": 0,
                                },
                                "index": 1,
                            },
                        ]
                    },
                    "travel_agency_id": {"value": None},
                }
            ],
            apply_cancellation_fee=True,
            assigned_resource_id={"value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
            assigned_resource_locked={"value": True},
            availability_block_id={"value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
            booker_id={"value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
            business_segment_id={"value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
            channel_number={"value": "Value"},
            check_overbooking=True,
            check_rate_applicability=True,
            company_id={"value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
            credit_card_id={"value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
            end_utc={"value": "Value"},
            enterprise_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
            options={"owner_checked_in": {"value": True}},
            person_counts={
                "value": [
                    {
                        "age_category_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "count": 0,
                    }
                ]
            },
            purpose={"value": "Value"},
            rate_id={"value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
            reason="Testing",
            released_utc={"value": "Value"},
            reprice=True,
            requested_category_id={"value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
            start_utc={"value": "Value"},
            time_unit_prices={
                "value": [
                    {
                        "amount": {
                            "currency": "x",
                            "tax_codes": ["string"],
                            "gross_value": 0,
                            "net_value": 0,
                        },
                        "index": 0,
                    }
                ]
            },
            travel_agency_id={"value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
        )
        assert_matches_type(ReservationResult, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.reservations.with_raw_response.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            reservation_updates=[
                {
                    "access_token": "x",
                    "client": "x",
                    "client_token": "x",
                    "reservation_id": "622605a9-2969-441f-9610-aa720099ae1c",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reservation = await response.parse()
        assert_matches_type(ReservationResult, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.reservations.with_streaming_response.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            reservation_updates=[
                {
                    "access_token": "x",
                    "client": "x",
                    "client_token": "x",
                    "reservation_id": "622605a9-2969-441f-9610-aa720099ae1c",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reservation = await response.parse()
            assert_matches_type(ReservationResult, reservation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_add(self, async_client: AsyncPymews) -> None:
        reservation = await async_client.api.connector.v1.reservations.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservations=[
                {
                    "customer_id": "e465c031-fd99-4546-8c70-abcf0029c249",
                    "end_utc": parse_datetime("2021-01-03T10:00:00Z"),
                    "person_counts": [
                        {
                            "age_category_id": "1f67644f-052d-4863-acdf-ae1600c60ca0",
                            "count": 2,
                        },
                        {
                            "age_category_id": "ab58c939-be30-4a60-8f75-ae1600c60c9f",
                            "count": 2,
                        },
                    ],
                    "rate_id": "a39a59fa-3a08-4822-bdd4-ab0b00e3d21f",
                    "requested_category_id": "0a5da171-3663-4496-a61e-35ecbd78b9b1",
                    "start_utc": parse_datetime("2021-01-01T14:00:00Z"),
                }
            ],
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
        )
        assert_matches_type(ReservationAddResponse, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_add_with_all_params(self, async_client: AsyncPymews) -> None:
        reservation = await async_client.api.connector.v1.reservations.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservations=[
                {
                    "customer_id": "e465c031-fd99-4546-8c70-abcf0029c249",
                    "end_utc": parse_datetime("2021-01-03T10:00:00Z"),
                    "person_counts": [
                        {
                            "age_category_id": "1f67644f-052d-4863-acdf-ae1600c60ca0",
                            "count": 2,
                        },
                        {
                            "age_category_id": "ab58c939-be30-4a60-8f75-ae1600c60c9f",
                            "count": 2,
                        },
                    ],
                    "rate_id": "a39a59fa-3a08-4822-bdd4-ab0b00e3d21f",
                    "requested_category_id": "0a5da171-3663-4496-a61e-35ecbd78b9b1",
                    "start_utc": parse_datetime("2021-01-01T14:00:00Z"),
                    "adult_count": 0,
                    "availability_block_id": None,
                    "booker_id": "e465c031-fd99-4546-8c70-abcf0029c249",
                    "business_segment_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "channel_number": "ChannelNumber",
                    "child_count": 0,
                    "company_id": None,
                    "credit_card_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "identifier": "1234",
                    "notes": "Test reservation",
                    "product_orders": [
                        {
                            "product_id": "2e9eb3fc-8a77-466a-9cd9-abcf002a2a01",
                            "count": 0,
                            "end_utc": parse_datetime("2021-01-03T00:00:00Z"),
                            "external_identifier": "ExternalIdentifier",
                            "start_utc": parse_datetime("2021-01-02T00:00:00Z"),
                            "unit_amount": {
                                "currency": "x",
                                "tax_codes": ["string"],
                                "gross_value": 0,
                                "net_value": 0,
                            },
                        }
                    ],
                    "released_utc": None,
                    "state": "Inquired",
                    "time_unit_amount": {
                        "currency": "x",
                        "tax_codes": ["string"],
                        "gross_value": 0,
                        "net_value": 0,
                    },
                    "time_unit_prices": [
                        {
                            "amount": {
                                "currency": "GBP",
                                "tax_codes": ["UK-S"],
                                "gross_value": 20,
                                "net_value": 0,
                            },
                            "index": 0,
                        },
                        {
                            "amount": {
                                "currency": "GBP",
                                "tax_codes": ["UK-S"],
                                "gross_value": 30,
                                "net_value": 0,
                            },
                            "index": 1,
                        },
                    ],
                    "travel_agency_id": None,
                    "voucher_code": "SpringSale2021",
                }
            ],
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
            check_overbooking=True,
            check_rate_applicability=True,
            enterprise_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            group_id=None,
            group_name=None,
            send_confirmation_email=True,
        )
        assert_matches_type(ReservationAddResponse, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.reservations.with_raw_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservations=[
                {
                    "customer_id": "e465c031-fd99-4546-8c70-abcf0029c249",
                    "end_utc": parse_datetime("2021-01-03T10:00:00Z"),
                    "person_counts": [
                        {
                            "age_category_id": "1f67644f-052d-4863-acdf-ae1600c60ca0",
                            "count": 2,
                        },
                        {
                            "age_category_id": "ab58c939-be30-4a60-8f75-ae1600c60c9f",
                            "count": 2,
                        },
                    ],
                    "rate_id": "a39a59fa-3a08-4822-bdd4-ab0b00e3d21f",
                    "requested_category_id": "0a5da171-3663-4496-a61e-35ecbd78b9b1",
                    "start_utc": parse_datetime("2021-01-01T14:00:00Z"),
                }
            ],
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reservation = await response.parse()
        assert_matches_type(ReservationAddResponse, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.reservations.with_streaming_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservations=[
                {
                    "customer_id": "e465c031-fd99-4546-8c70-abcf0029c249",
                    "end_utc": parse_datetime("2021-01-03T10:00:00Z"),
                    "person_counts": [
                        {
                            "age_category_id": "1f67644f-052d-4863-acdf-ae1600c60ca0",
                            "count": 2,
                        },
                        {
                            "age_category_id": "ab58c939-be30-4a60-8f75-ae1600c60c9f",
                            "count": 2,
                        },
                    ],
                    "rate_id": "a39a59fa-3a08-4822-bdd4-ab0b00e3d21f",
                    "requested_category_id": "0a5da171-3663-4496-a61e-35ecbd78b9b1",
                    "start_utc": parse_datetime("2021-01-01T14:00:00Z"),
                }
            ],
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reservation = await response.parse()
            assert_matches_type(ReservationAddResponse, reservation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_add_companion(self, async_client: AsyncPymews) -> None:
        reservation = await async_client.api.connector.v1.reservations.add_companion(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_id="35d4b117-4e60-44a3-9580-c582117eff98",
            reservation_id="e6ea708c-2a2a-412f-a152-b6c76ffad49b",
        )
        assert_matches_type(ReservationAddCompanionResponse, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_add_companion_with_all_params(self, async_client: AsyncPymews) -> None:
        reservation = await async_client.api.connector.v1.reservations.add_companion(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_id="35d4b117-4e60-44a3-9580-c582117eff98",
            reservation_id="e6ea708c-2a2a-412f-a152-b6c76ffad49b",
            enterprise_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ReservationAddCompanionResponse, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_add_companion(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.reservations.with_raw_response.add_companion(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_id="35d4b117-4e60-44a3-9580-c582117eff98",
            reservation_id="e6ea708c-2a2a-412f-a152-b6c76ffad49b",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reservation = await response.parse()
        assert_matches_type(ReservationAddCompanionResponse, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_add_companion(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.reservations.with_streaming_response.add_companion(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_id="35d4b117-4e60-44a3-9580-c582117eff98",
            reservation_id="e6ea708c-2a2a-412f-a152-b6c76ffad49b",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reservation = await response.parse()
            assert_matches_type(ReservationAddCompanionResponse, reservation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_add_product(self, async_client: AsyncPymews) -> None:
        reservation = await async_client.api.connector.v1.reservations.add_product(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            count=1,
            product_id="47312820-2268-4f5c-864d-aa4100ed82bc",
            reservation_id="4d2aa234-5d30-472c-899f-ab45008c3479",
        )
        assert_matches_type(ReservationAddProductResponse, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_add_product_with_all_params(self, async_client: AsyncPymews) -> None:
        reservation = await async_client.api.connector.v1.reservations.add_product(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            count=1,
            product_id="47312820-2268-4f5c-864d-aa4100ed82bc",
            reservation_id="4d2aa234-5d30-472c-899f-ab45008c3479",
            end_utc=parse_datetime("2021-01-03T00:00:00Z"),
            start_utc=parse_datetime("2021-01-02T00:00:00Z"),
            unit_amount={
                "currency": "GBP",
                "tax_codes": ["UK-S"],
                "gross_value": 10,
                "net_value": 0,
            },
        )
        assert_matches_type(ReservationAddProductResponse, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_add_product(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.reservations.with_raw_response.add_product(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            count=1,
            product_id="47312820-2268-4f5c-864d-aa4100ed82bc",
            reservation_id="4d2aa234-5d30-472c-899f-ab45008c3479",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reservation = await response.parse()
        assert_matches_type(ReservationAddProductResponse, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_add_product(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.reservations.with_streaming_response.add_product(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            count=1,
            product_id="47312820-2268-4f5c-864d-aa4100ed82bc",
            reservation_id="4d2aa234-5d30-472c-899f-ab45008c3479",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reservation = await response.parse()
            assert_matches_type(ReservationAddProductResponse, reservation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_cancel(self, async_client: AsyncPymews) -> None:
        reservation = await async_client.api.connector.v1.reservations.cancel(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservation_ids=["5ca70705-cbb7-48c4-8cc4-abb900aa278c"],
        )
        assert_matches_type(MultipleReservationResult, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_cancel_with_all_params(self, async_client: AsyncPymews) -> None:
        reservation = await async_client.api.connector.v1.reservations.cancel(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservation_ids=["5ca70705-cbb7-48c4-8cc4-abb900aa278c"],
            enterprise_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
            notes="Cancellation through Connector API",
            post_cancellation_fee=True,
            reservation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            send_email=True,
        )
        assert_matches_type(MultipleReservationResult, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.reservations.with_raw_response.cancel(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservation_ids=["5ca70705-cbb7-48c4-8cc4-abb900aa278c"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reservation = await response.parse()
        assert_matches_type(MultipleReservationResult, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.reservations.with_streaming_response.cancel(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservation_ids=["5ca70705-cbb7-48c4-8cc4-abb900aa278c"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reservation = await response.parse()
            assert_matches_type(MultipleReservationResult, reservation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_confirm(self, async_client: AsyncPymews) -> None:
        reservation = await async_client.api.connector.v1.reservations.confirm(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservation_ids=["9af9d8b0-43ae-414d-80a8-abc1012a2a59"],
        )
        assert_matches_type(MultipleReservationResult, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_confirm_with_all_params(self, async_client: AsyncPymews) -> None:
        reservation = await async_client.api.connector.v1.reservations.confirm(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservation_ids=["9af9d8b0-43ae-414d-80a8-abc1012a2a59"],
            enterprise_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            send_confirmation_email=True,
        )
        assert_matches_type(MultipleReservationResult, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_confirm(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.reservations.with_raw_response.confirm(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservation_ids=["9af9d8b0-43ae-414d-80a8-abc1012a2a59"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reservation = await response.parse()
        assert_matches_type(MultipleReservationResult, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_confirm(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.reservations.with_streaming_response.confirm(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservation_ids=["9af9d8b0-43ae-414d-80a8-abc1012a2a59"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reservation = await response.parse()
            assert_matches_type(MultipleReservationResult, reservation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete_companion(self, async_client: AsyncPymews) -> None:
        reservation = await async_client.api.connector.v1.reservations.delete_companion(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_id="35d4b117-4e60-44a3-9580-c582117eff98",
            reservation_id="e6ea708c-2a2a-412f-a152-b6c76ffad49b",
        )
        assert_matches_type(object, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete_companion_with_all_params(self, async_client: AsyncPymews) -> None:
        reservation = await async_client.api.connector.v1.reservations.delete_companion(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_id="35d4b117-4e60-44a3-9580-c582117eff98",
            reservation_id="e6ea708c-2a2a-412f-a152-b6c76ffad49b",
            enterprise_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete_companion(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.reservations.with_raw_response.delete_companion(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_id="35d4b117-4e60-44a3-9580-c582117eff98",
            reservation_id="e6ea708c-2a2a-412f-a152-b6c76ffad49b",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reservation = await response.parse()
        assert_matches_type(object, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete_companion(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.reservations.with_streaming_response.delete_companion(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_id="35d4b117-4e60-44a3-9580-c582117eff98",
            reservation_id="e6ea708c-2a2a-412f-a152-b6c76ffad49b",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reservation = await response.parse()
            assert_matches_type(object, reservation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_all(self, async_client: AsyncPymews) -> None:
        reservation = await async_client.api.connector.v1.reservations.get_all(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            extent={},
            limitation={"count": 10},
            service_ids=["bd26d8db-86da-4f96-9efc-e5a4654a4a94"],
        )
        assert_matches_type(ReservationResult, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_all_with_all_params(self, async_client: AsyncPymews) -> None:
        reservation = await async_client.api.connector.v1.reservations.get_all(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            extent={
                "accounting_states": ["Open"],
                "business_segments": True,
                "companies": True,
                "customer_adresses": True,
                "customer_identity_documents": True,
                "customers": True,
                "items": True,
                "notes": True,
                "order_items": True,
                "products": True,
                "qr_code_data": True,
                "rates": True,
                "reservation_groups": True,
                "reservations": True,
                "resource_categories": True,
                "resource_category_assignments": True,
                "resources": True,
                "services": True,
            },
            limitation={
                "count": 10,
                "cursor": "e7f26210-10e7-462e-9da8-ae8300be8ab7",
            },
            service_ids=["bd26d8db-86da-4f96-9efc-e5a4654a4a94"],
            assigned_resource_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            business_segment_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            channel_numbers=["TW48ZP"],
            currency="Currency",
            customer_ids=["8e1d0ca6-1dde-4be0-8566-aafc01866110"],
            end_utc=parse_datetime("2016-01-07T00:00:00Z"),
            group_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            numbers=["string"],
            rate_ids=["ed4b660b-19d0-434b-9360-a4de2ea42eda"],
            reservation_ids=["db6cad34-9a91-448b-bea1-abbe01240d9c"],
            service_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            start_utc=parse_datetime("2016-01-01T00:00:00Z"),
            states=["Enquired"],
            time_filter="Colliding",
        )
        assert_matches_type(ReservationResult, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_all(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.reservations.with_raw_response.get_all(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            extent={},
            limitation={"count": 10},
            service_ids=["bd26d8db-86da-4f96-9efc-e5a4654a4a94"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reservation = await response.parse()
        assert_matches_type(ReservationResult, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_all(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.reservations.with_streaming_response.get_all(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            extent={},
            limitation={"count": 10},
            service_ids=["bd26d8db-86da-4f96-9efc-e5a4654a4a94"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reservation = await response.parse()
            assert_matches_type(ReservationResult, reservation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_all_2023_06_06(self, async_client: AsyncPymews) -> None:
        reservation = await async_client.api.connector.v1.reservations.get_all_2023_06_06(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )
        assert_matches_type(ReservationGetAll2023_06_06Response, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_all_2023_06_06_with_all_params(self, async_client: AsyncPymews) -> None:
        reservation = await async_client.api.connector.v1.reservations.get_all_2023_06_06(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            account_ids=["fadd5bb6-b428-45d5-94f8-fd0d89fece6d"],
            actual_start_utc={
                "end_utc": parse_datetime("2019-12-27T18:11:19.117Z"),
                "start_utc": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            assigned_resource_ids=["5ee074b1-6c86-48e8-915f-c7aa4702086f", "c32386aa-1cd2-414a-a823-489325842fbe"],
            availability_block_ids=["5ee074b1-6c86-48e8-915f-c7aa4702086f", "c32386aa-1cd2-414a-a823-489325842fbe"],
            colliding_utc={
                "end_utc": parse_datetime("2023-05-05T00:00:00Z"),
                "start_utc": parse_datetime("2023-04-01T00:00:00Z"),
            },
            created_utc={
                "end_utc": parse_datetime("2023-05-05T00:00:00Z"),
                "start_utc": parse_datetime("2023-04-01T00:00:00Z"),
            },
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            numbers=["50", "51", "52", "53"],
            reservation_group_ids=["94843f6f-3be3-481b-a1c7-06458774c3df"],
            reservation_ids=["0f515589-99b4-423d-b83a-b237009f0509", "9b59b50d-bd32-4ce5-add8-09ea0e1300e7"],
            scheduled_end_utc={
                "end_utc": parse_datetime("2023-05-05T00:00:00Z"),
                "start_utc": parse_datetime("2023-04-01T00:00:00Z"),
            },
            scheduled_start_utc={
                "end_utc": parse_datetime("2023-05-05T00:00:00Z"),
                "start_utc": parse_datetime("2023-04-01T00:00:00Z"),
            },
            service_ids=["bd26d8db-86da-4f96-9efc-e5a4654a4a94", "8c1bd738-a505-4b29-aa71-9ecc2982b843"],
            states=["Inquired", "Confirmed"],
            updated_utc={
                "end_utc": parse_datetime("2023-05-05T00:00:00Z"),
                "start_utc": parse_datetime("2023-04-01T00:00:00Z"),
            },
        )
        assert_matches_type(ReservationGetAll2023_06_06Response, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_all_2023_06_06(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.reservations.with_raw_response.get_all_2023_06_06(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reservation = await response.parse()
        assert_matches_type(ReservationGetAll2023_06_06Response, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_all_2023_06_06(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.reservations.with_streaming_response.get_all_2023_06_06(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reservation = await response.parse()
            assert_matches_type(ReservationGetAll2023_06_06Response, reservation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_all_items(self, async_client: AsyncPymews) -> None:
        reservation = await async_client.api.connector.v1.reservations.get_all_items(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservation_ids=["e6ea708c-2a2a-412f-a152-b6c76ffad49b"],
        )
        assert_matches_type(ReservationGetAllItemsResponse, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_all_items_with_all_params(self, async_client: AsyncPymews) -> None:
        reservation = await async_client.api.connector.v1.reservations.get_all_items(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservation_ids=["e6ea708c-2a2a-412f-a152-b6c76ffad49b"],
            accounting_states=["Closed"],
            currency="EUR",
        )
        assert_matches_type(ReservationGetAllItemsResponse, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_all_items(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.reservations.with_raw_response.get_all_items(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservation_ids=["e6ea708c-2a2a-412f-a152-b6c76ffad49b"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reservation = await response.parse()
        assert_matches_type(ReservationGetAllItemsResponse, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_all_items(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.reservations.with_streaming_response.get_all_items(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservation_ids=["e6ea708c-2a2a-412f-a152-b6c76ffad49b"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reservation = await response.parse()
            assert_matches_type(ReservationGetAllItemsResponse, reservation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_price(self, async_client: AsyncPymews) -> None:
        reservation = await async_client.api.connector.v1.reservations.price(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservations=[
                {
                    "customer_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "end_utc": parse_datetime("2018-01-02T10:00:00Z"),
                    "person_counts": [
                        {
                            "age_category_id": "1f67644f-052d-4863-acdf-ae1600c60ca0",
                            "count": 2,
                        },
                        {
                            "age_category_id": "ab58c939-be30-4a60-8f75-ae1600c60c9f",
                            "count": 2,
                        },
                    ],
                    "rate_id": "33667cab-f17f-4089-ad07-c2cd50fa0df1",
                    "requested_category_id": "0a5da171-3663-4496-a61e-35ecbd78b9b1",
                    "start_utc": parse_datetime("2018-01-01T14:00:00Z"),
                }
            ],
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
        )
        assert_matches_type(ReservationPriceResponse, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_price(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.reservations.with_raw_response.price(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservations=[
                {
                    "customer_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "end_utc": parse_datetime("2018-01-02T10:00:00Z"),
                    "person_counts": [
                        {
                            "age_category_id": "1f67644f-052d-4863-acdf-ae1600c60ca0",
                            "count": 2,
                        },
                        {
                            "age_category_id": "ab58c939-be30-4a60-8f75-ae1600c60c9f",
                            "count": 2,
                        },
                    ],
                    "rate_id": "33667cab-f17f-4089-ad07-c2cd50fa0df1",
                    "requested_category_id": "0a5da171-3663-4496-a61e-35ecbd78b9b1",
                    "start_utc": parse_datetime("2018-01-01T14:00:00Z"),
                }
            ],
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reservation = await response.parse()
        assert_matches_type(ReservationPriceResponse, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_price(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.reservations.with_streaming_response.price(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservations=[
                {
                    "customer_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "end_utc": parse_datetime("2018-01-02T10:00:00Z"),
                    "person_counts": [
                        {
                            "age_category_id": "1f67644f-052d-4863-acdf-ae1600c60ca0",
                            "count": 2,
                        },
                        {
                            "age_category_id": "ab58c939-be30-4a60-8f75-ae1600c60c9f",
                            "count": 2,
                        },
                    ],
                    "rate_id": "33667cab-f17f-4089-ad07-c2cd50fa0df1",
                    "requested_category_id": "0a5da171-3663-4496-a61e-35ecbd78b9b1",
                    "start_utc": parse_datetime("2018-01-01T14:00:00Z"),
                }
            ],
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reservation = await response.parse()
            assert_matches_type(ReservationPriceResponse, reservation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_process(self, async_client: AsyncPymews) -> None:
        reservation = await async_client.api.connector.v1.reservations.process(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservation_id="e6ea708c-2a2a-412f-a152-b6c76ffad49b",
        )
        assert_matches_type(object, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_process_with_all_params(self, async_client: AsyncPymews) -> None:
        reservation = await async_client.api.connector.v1.reservations.process(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservation_id="e6ea708c-2a2a-412f-a152-b6c76ffad49b",
            allow_open_balance=False,
            close_bills=False,
            enterprise_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
            notes=None,
        )
        assert_matches_type(object, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_process(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.reservations.with_raw_response.process(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservation_id="e6ea708c-2a2a-412f-a152-b6c76ffad49b",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reservation = await response.parse()
        assert_matches_type(object, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_process(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.reservations.with_streaming_response.process(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservation_id="e6ea708c-2a2a-412f-a152-b6c76ffad49b",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reservation = await response.parse()
            assert_matches_type(object, reservation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_start(self, async_client: AsyncPymews) -> None:
        reservation = await async_client.api.connector.v1.reservations.start(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservation_id="e6ea708c-2a2a-412f-a152-b6c76ffad49b",
        )
        assert_matches_type(object, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_start_with_all_params(self, async_client: AsyncPymews) -> None:
        reservation = await async_client.api.connector.v1.reservations.start(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservation_id="e6ea708c-2a2a-412f-a152-b6c76ffad49b",
            enterprise_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )
        assert_matches_type(object, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_start(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.reservations.with_raw_response.start(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservation_id="e6ea708c-2a2a-412f-a152-b6c76ffad49b",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reservation = await response.parse()
        assert_matches_type(object, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_start(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.reservations.with_streaming_response.start(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservation_id="e6ea708c-2a2a-412f-a152-b6c76ffad49b",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reservation = await response.parse()
            assert_matches_type(object, reservation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_customer(self, async_client: AsyncPymews) -> None:
        reservation = await async_client.api.connector.v1.reservations.update_customer(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_id="35d4b117-4e60-44a3-9580-c582117eff98",
            reservation_id="209d984d-4985-4efb-96ec-f6591fc597bf",
        )
        assert_matches_type(object, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_customer_with_all_params(self, async_client: AsyncPymews) -> None:
        reservation = await async_client.api.connector.v1.reservations.update_customer(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_id="35d4b117-4e60-44a3-9580-c582117eff98",
            reservation_id="209d984d-4985-4efb-96ec-f6591fc597bf",
            enterprise_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )
        assert_matches_type(object, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update_customer(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.reservations.with_raw_response.update_customer(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_id="35d4b117-4e60-44a3-9580-c582117eff98",
            reservation_id="209d984d-4985-4efb-96ec-f6591fc597bf",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reservation = await response.parse()
        assert_matches_type(object, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update_customer(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.reservations.with_streaming_response.update_customer(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_id="35d4b117-4e60-44a3-9580-c582117eff98",
            reservation_id="209d984d-4985-4efb-96ec-f6591fc597bf",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reservation = await response.parse()
            assert_matches_type(object, reservation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_interval(self, async_client: AsyncPymews) -> None:
        reservation = await async_client.api.connector.v1.reservations.update_interval(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            charge_cancellation_fee=False,
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservation_id="209d984d-4985-4efb-96ec-f6591fc597bf",
        )
        assert_matches_type(object, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_interval_with_all_params(self, async_client: AsyncPymews) -> None:
        reservation = await async_client.api.connector.v1.reservations.update_interval(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            charge_cancellation_fee=False,
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservation_id="209d984d-4985-4efb-96ec-f6591fc597bf",
            end_utc=parse_datetime("2017-08-15T12:00:00Z"),
            enterprise_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
            start_utc=parse_datetime("2017-08-12T15:00:00Z"),
        )
        assert_matches_type(object, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update_interval(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.reservations.with_raw_response.update_interval(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            charge_cancellation_fee=False,
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservation_id="209d984d-4985-4efb-96ec-f6591fc597bf",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reservation = await response.parse()
        assert_matches_type(object, reservation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update_interval(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.reservations.with_streaming_response.update_interval(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            charge_cancellation_fee=False,
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            reservation_id="209d984d-4985-4efb-96ec-f6591fc597bf",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reservation = await response.parse()
            assert_matches_type(object, reservation, path=["response"])

        assert cast(Any, response.is_closed) is True
