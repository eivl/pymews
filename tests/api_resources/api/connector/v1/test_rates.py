# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pymews import Pymews, AsyncPymews
from tests.utils import assert_matches_type
from pymews._utils import parse_datetime
from pymews.types.api.connector.v1 import (
    RateAddResponse,
    RateSetResponse,
    RateListResponse,
    RateGetPricingResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRates:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Pymews) -> None:
        rate = client.api.connector.v1.rates.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            service_ids=["bd26d8db-86da-4f96-9efc-e5a4654a4a94"],
        )
        assert_matches_type(RateListResponse, rate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Pymews) -> None:
        rate = client.api.connector.v1.rates.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            service_ids=["bd26d8db-86da-4f96-9efc-e5a4654a4a94"],
            activity_states=["Active"],
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            extent={
                "availability_block_assignments": True,
                "rate_groups": True,
                "rates": True,
            },
            external_identifiers=["Rate-001", "Rate-002"],
            rate_ids=["ed4b660b-19d0-434b-9360-a4de2ea42eda"],
            updated_utc={
                "end_utc": parse_datetime("2022-10-20T00:00:00Z"),
                "start_utc": parse_datetime("2022-10-15T00:00:00Z"),
            },
        )
        assert_matches_type(RateListResponse, rate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Pymews) -> None:
        response = client.api.connector.v1.rates.with_raw_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            service_ids=["bd26d8db-86da-4f96-9efc-e5a4654a4a94"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate = response.parse()
        assert_matches_type(RateListResponse, rate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Pymews) -> None:
        with client.api.connector.v1.rates.with_streaming_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            service_ids=["bd26d8db-86da-4f96-9efc-e5a4654a4a94"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rate = response.parse()
            assert_matches_type(RateListResponse, rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Pymews) -> None:
        rate = client.api.connector.v1.rates.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            rate_ids=["7e89ee8e-11a0-4d9d-8880-f8d8494824b5", "eid:BasicRate"],
        )
        assert_matches_type(object, rate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_delete_with_all_params(self, client: Pymews) -> None:
        rate = client.api.connector.v1.rates.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            rate_ids=["7e89ee8e-11a0-4d9d-8880-f8d8494824b5", "eid:BasicRate"],
            enterprise_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )
        assert_matches_type(object, rate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Pymews) -> None:
        response = client.api.connector.v1.rates.with_raw_response.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            rate_ids=["7e89ee8e-11a0-4d9d-8880-f8d8494824b5", "eid:BasicRate"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate = response.parse()
        assert_matches_type(object, rate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Pymews) -> None:
        with client.api.connector.v1.rates.with_streaming_response.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            rate_ids=["7e89ee8e-11a0-4d9d-8880-f8d8494824b5", "eid:BasicRate"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rate = response.parse()
            assert_matches_type(object, rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_add(self, client: Pymews) -> None:
        rate = client.api.connector.v1.rates.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            rates=[
                {
                    "names": {"EN": "My rate"},
                    "pricing_type": "DependentRatePricing",
                    "rate_group_id": "b9f25a45-9b9a-4b33-99bd-b06f008eb6f5",
                    "service_id": "bd26d8db-86da-4f96-9efc-e5a4654a4a94",
                }
            ],
        )
        assert_matches_type(RateAddResponse, rate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_add_with_all_params(self, client: Pymews) -> None:
        rate = client.api.connector.v1.rates.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            rates=[
                {
                    "names": {"EN": "My rate"},
                    "pricing_type": "DependentRatePricing",
                    "rate_group_id": "b9f25a45-9b9a-4b33-99bd-b06f008eb6f5",
                    "service_id": "bd26d8db-86da-4f96-9efc-e5a4654a4a94",
                    "accounting_category_id": "3620c660-a4ec-4e0f-a0bc-b06f008eb8bf",
                    "business_segment_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "descriptions": {"foo": "string"},
                    "external_identifier": "D001",
                    "external_names": {"foo": "string"},
                    "is_enabled": True,
                    "pricing": {
                        "base_rate_pricing": {
                            "amount": {
                                "currency": "x",
                                "tax_codes": ["string"],
                                "gross_value": 0,
                                "net_value": 0,
                            },
                            "extra_occupancy_adjustment": 0,
                            "negative_occupancy_adjustment": 0,
                        },
                        "dependent_rate_pricing": {
                            "base_rate_id": "1a1ddd3b-e106-4a70-aef1-54a75b483943",
                            "absolute_adjustment": 10,
                            "relative_adjustment": 0.15,
                        },
                    },
                    "short_names": {"foo": "string"},
                    "type": "Public",
                }
            ],
            enterprise_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )
        assert_matches_type(RateAddResponse, rate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_add(self, client: Pymews) -> None:
        response = client.api.connector.v1.rates.with_raw_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            rates=[
                {
                    "names": {"EN": "My rate"},
                    "pricing_type": "DependentRatePricing",
                    "rate_group_id": "b9f25a45-9b9a-4b33-99bd-b06f008eb6f5",
                    "service_id": "bd26d8db-86da-4f96-9efc-e5a4654a4a94",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate = response.parse()
        assert_matches_type(RateAddResponse, rate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_add(self, client: Pymews) -> None:
        with client.api.connector.v1.rates.with_streaming_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            rates=[
                {
                    "names": {"EN": "My rate"},
                    "pricing_type": "DependentRatePricing",
                    "rate_group_id": "b9f25a45-9b9a-4b33-99bd-b06f008eb6f5",
                    "service_id": "bd26d8db-86da-4f96-9efc-e5a4654a4a94",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rate = response.parse()
            assert_matches_type(RateAddResponse, rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_pricing(self, client: Pymews) -> None:
        rate = client.api.connector.v1.rates.get_pricing(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            first_time_unit_start_utc=parse_datetime("2022-01-01T23:00:00.000Z"),
            last_time_unit_start_utc=parse_datetime("2022-01-03T23:00:00.000Z"),
            rate_id="ed4b660b-19d0-434b-9360-a4de2ea42eda",
        )
        assert_matches_type(RateGetPricingResponse, rate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_pricing_with_all_params(self, client: Pymews) -> None:
        rate = client.api.connector.v1.rates.get_pricing(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            first_time_unit_start_utc=parse_datetime("2022-01-01T23:00:00.000Z"),
            last_time_unit_start_utc=parse_datetime("2022-01-03T23:00:00.000Z"),
            rate_id="ed4b660b-19d0-434b-9360-a4de2ea42eda",
            product_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RateGetPricingResponse, rate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_pricing(self, client: Pymews) -> None:
        response = client.api.connector.v1.rates.with_raw_response.get_pricing(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            first_time_unit_start_utc=parse_datetime("2022-01-01T23:00:00.000Z"),
            last_time_unit_start_utc=parse_datetime("2022-01-03T23:00:00.000Z"),
            rate_id="ed4b660b-19d0-434b-9360-a4de2ea42eda",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate = response.parse()
        assert_matches_type(RateGetPricingResponse, rate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_pricing(self, client: Pymews) -> None:
        with client.api.connector.v1.rates.with_streaming_response.get_pricing(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            first_time_unit_start_utc=parse_datetime("2022-01-01T23:00:00.000Z"),
            last_time_unit_start_utc=parse_datetime("2022-01-03T23:00:00.000Z"),
            rate_id="ed4b660b-19d0-434b-9360-a4de2ea42eda",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rate = response.parse()
            assert_matches_type(RateGetPricingResponse, rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_set(self, client: Pymews) -> None:
        rate = client.api.connector.v1.rates.set(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            rates=[
                {
                    "names": {"en-US": "Base rate"},
                    "pricing_type": "BaseRatePricing",
                    "rate_group_id": "d7adfddc-c2dc-4798-ace2-28de7b25408f",
                    "service_id": "956176af-e10b-4f3c-beb7-274801bce328",
                    "type": "Public",
                },
                {
                    "names": {"en-US": "Dependent rate"},
                    "pricing_type": "DependentRatePricing",
                    "rate_group_id": "eid:RG10",
                    "service_id": "eid:Stay",
                    "type": "Private",
                },
            ],
        )
        assert_matches_type(RateSetResponse, rate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_set_with_all_params(self, client: Pymews) -> None:
        rate = client.api.connector.v1.rates.set(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            rates=[
                {
                    "names": {"en-US": "Base rate"},
                    "pricing_type": "BaseRatePricing",
                    "rate_group_id": "d7adfddc-c2dc-4798-ace2-28de7b25408f",
                    "service_id": "956176af-e10b-4f3c-beb7-274801bce328",
                    "type": "Public",
                    "accounting_category_id": "07781f3c-94b6-4b31-9175-03786a84cd50",
                    "business_segment_id": "dc9188f6-fb61-412c-b3fd-af32dab082ed",
                    "descriptions": {"en-US": "Base rate description."},
                    "external_identifier": "ExternalIdentifier",
                    "external_names": {"en-US": "External base rate"},
                    "id": "e1b0bf46-32a3-4f7c-99c1-1ff78447d55d",
                    "is_enabled": True,
                    "pricing": {
                        "base_rate_pricing": {
                            "amount": {
                                "currency": "EUR",
                                "tax_codes": ["string"],
                                "gross_value": 0,
                                "net_value": 100,
                            }
                        },
                        "dependent_rate_pricing": {
                            "base_rate_id": "x",
                            "absolute_adjustment": 0,
                            "relative_adjustment": 0,
                        },
                    },
                    "short_names": {"en-US": "BR"},
                },
                {
                    "names": {"en-US": "Dependent rate"},
                    "pricing_type": "DependentRatePricing",
                    "rate_group_id": "eid:RG10",
                    "service_id": "eid:Stay",
                    "type": "Private",
                    "accounting_category_id": "07781f3c-94b6-4b31-9175-03786a84cd50",
                    "business_segment_id": "dc9188f6-fb61-412c-b3fd-af32dab082ed",
                    "descriptions": {"en-US": "Dependent rate description."},
                    "external_identifier": "55698",
                    "external_names": {"en-US": "External dependent rate"},
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "is_enabled": False,
                    "pricing": {
                        "base_rate_pricing": {
                            "amount": {
                                "currency": "x",
                                "tax_codes": ["string"],
                                "gross_value": 0,
                                "net_value": 0,
                            }
                        },
                        "dependent_rate_pricing": {
                            "base_rate_id": "00392166-3869-4174-b491-cf0162524a38",
                            "absolute_adjustment": 10,
                            "relative_adjustment": 0.25,
                        },
                    },
                    "short_names": {"en-US": "DR"},
                },
            ],
            enterprise_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )
        assert_matches_type(RateSetResponse, rate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_set(self, client: Pymews) -> None:
        response = client.api.connector.v1.rates.with_raw_response.set(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            rates=[
                {
                    "names": {"en-US": "Base rate"},
                    "pricing_type": "BaseRatePricing",
                    "rate_group_id": "d7adfddc-c2dc-4798-ace2-28de7b25408f",
                    "service_id": "956176af-e10b-4f3c-beb7-274801bce328",
                    "type": "Public",
                },
                {
                    "names": {"en-US": "Dependent rate"},
                    "pricing_type": "DependentRatePricing",
                    "rate_group_id": "eid:RG10",
                    "service_id": "eid:Stay",
                    "type": "Private",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate = response.parse()
        assert_matches_type(RateSetResponse, rate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_set(self, client: Pymews) -> None:
        with client.api.connector.v1.rates.with_streaming_response.set(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            rates=[
                {
                    "names": {"en-US": "Base rate"},
                    "pricing_type": "BaseRatePricing",
                    "rate_group_id": "d7adfddc-c2dc-4798-ace2-28de7b25408f",
                    "service_id": "956176af-e10b-4f3c-beb7-274801bce328",
                    "type": "Public",
                },
                {
                    "names": {"en-US": "Dependent rate"},
                    "pricing_type": "DependentRatePricing",
                    "rate_group_id": "eid:RG10",
                    "service_id": "eid:Stay",
                    "type": "Private",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rate = response.parse()
            assert_matches_type(RateSetResponse, rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_update_price(self, client: Pymews) -> None:
        rate = client.api.connector.v1.rates.update_price(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            price_updates=[{}, {}],
            rate_id="ed4b660b-19d0-434b-9360-a4de2ea42eda",
        )
        assert_matches_type(object, rate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_price_with_all_params(self, client: Pymews) -> None:
        rate = client.api.connector.v1.rates.update_price(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            price_updates=[
                {
                    "category_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "first_time_unit_start_utc": parse_datetime("2022-01-01T23:00:00.000Z"),
                    "last_time_unit_start_utc": parse_datetime("2022-01-03T23:00:00.000Z"),
                    "value": 111,
                },
                {
                    "category_id": "e3aa3117-dff0-46b7-b49a-2c0391e70ff9",
                    "first_time_unit_start_utc": parse_datetime("2022-01-04T23:00:00.000Z"),
                    "last_time_unit_start_utc": parse_datetime("2022-01-05T23:00:00.000Z"),
                    "value": 222,
                },
            ],
            rate_id="ed4b660b-19d0-434b-9360-a4de2ea42eda",
            product_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, rate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update_price(self, client: Pymews) -> None:
        response = client.api.connector.v1.rates.with_raw_response.update_price(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            price_updates=[{}, {}],
            rate_id="ed4b660b-19d0-434b-9360-a4de2ea42eda",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate = response.parse()
        assert_matches_type(object, rate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update_price(self, client: Pymews) -> None:
        with client.api.connector.v1.rates.with_streaming_response.update_price(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            price_updates=[{}, {}],
            rate_id="ed4b660b-19d0-434b-9360-a4de2ea42eda",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rate = response.parse()
            assert_matches_type(object, rate, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRates:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncPymews) -> None:
        rate = await async_client.api.connector.v1.rates.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            service_ids=["bd26d8db-86da-4f96-9efc-e5a4654a4a94"],
        )
        assert_matches_type(RateListResponse, rate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPymews) -> None:
        rate = await async_client.api.connector.v1.rates.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            service_ids=["bd26d8db-86da-4f96-9efc-e5a4654a4a94"],
            activity_states=["Active"],
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            extent={
                "availability_block_assignments": True,
                "rate_groups": True,
                "rates": True,
            },
            external_identifiers=["Rate-001", "Rate-002"],
            rate_ids=["ed4b660b-19d0-434b-9360-a4de2ea42eda"],
            updated_utc={
                "end_utc": parse_datetime("2022-10-20T00:00:00Z"),
                "start_utc": parse_datetime("2022-10-15T00:00:00Z"),
            },
        )
        assert_matches_type(RateListResponse, rate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.rates.with_raw_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            service_ids=["bd26d8db-86da-4f96-9efc-e5a4654a4a94"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate = await response.parse()
        assert_matches_type(RateListResponse, rate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.rates.with_streaming_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            service_ids=["bd26d8db-86da-4f96-9efc-e5a4654a4a94"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rate = await response.parse()
            assert_matches_type(RateListResponse, rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncPymews) -> None:
        rate = await async_client.api.connector.v1.rates.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            rate_ids=["7e89ee8e-11a0-4d9d-8880-f8d8494824b5", "eid:BasicRate"],
        )
        assert_matches_type(object, rate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncPymews) -> None:
        rate = await async_client.api.connector.v1.rates.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            rate_ids=["7e89ee8e-11a0-4d9d-8880-f8d8494824b5", "eid:BasicRate"],
            enterprise_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )
        assert_matches_type(object, rate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.rates.with_raw_response.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            rate_ids=["7e89ee8e-11a0-4d9d-8880-f8d8494824b5", "eid:BasicRate"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate = await response.parse()
        assert_matches_type(object, rate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.rates.with_streaming_response.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            rate_ids=["7e89ee8e-11a0-4d9d-8880-f8d8494824b5", "eid:BasicRate"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rate = await response.parse()
            assert_matches_type(object, rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_add(self, async_client: AsyncPymews) -> None:
        rate = await async_client.api.connector.v1.rates.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            rates=[
                {
                    "names": {"EN": "My rate"},
                    "pricing_type": "DependentRatePricing",
                    "rate_group_id": "b9f25a45-9b9a-4b33-99bd-b06f008eb6f5",
                    "service_id": "bd26d8db-86da-4f96-9efc-e5a4654a4a94",
                }
            ],
        )
        assert_matches_type(RateAddResponse, rate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_add_with_all_params(self, async_client: AsyncPymews) -> None:
        rate = await async_client.api.connector.v1.rates.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            rates=[
                {
                    "names": {"EN": "My rate"},
                    "pricing_type": "DependentRatePricing",
                    "rate_group_id": "b9f25a45-9b9a-4b33-99bd-b06f008eb6f5",
                    "service_id": "bd26d8db-86da-4f96-9efc-e5a4654a4a94",
                    "accounting_category_id": "3620c660-a4ec-4e0f-a0bc-b06f008eb8bf",
                    "business_segment_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "descriptions": {"foo": "string"},
                    "external_identifier": "D001",
                    "external_names": {"foo": "string"},
                    "is_enabled": True,
                    "pricing": {
                        "base_rate_pricing": {
                            "amount": {
                                "currency": "x",
                                "tax_codes": ["string"],
                                "gross_value": 0,
                                "net_value": 0,
                            },
                            "extra_occupancy_adjustment": 0,
                            "negative_occupancy_adjustment": 0,
                        },
                        "dependent_rate_pricing": {
                            "base_rate_id": "1a1ddd3b-e106-4a70-aef1-54a75b483943",
                            "absolute_adjustment": 10,
                            "relative_adjustment": 0.15,
                        },
                    },
                    "short_names": {"foo": "string"},
                    "type": "Public",
                }
            ],
            enterprise_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )
        assert_matches_type(RateAddResponse, rate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.rates.with_raw_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            rates=[
                {
                    "names": {"EN": "My rate"},
                    "pricing_type": "DependentRatePricing",
                    "rate_group_id": "b9f25a45-9b9a-4b33-99bd-b06f008eb6f5",
                    "service_id": "bd26d8db-86da-4f96-9efc-e5a4654a4a94",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate = await response.parse()
        assert_matches_type(RateAddResponse, rate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.rates.with_streaming_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            rates=[
                {
                    "names": {"EN": "My rate"},
                    "pricing_type": "DependentRatePricing",
                    "rate_group_id": "b9f25a45-9b9a-4b33-99bd-b06f008eb6f5",
                    "service_id": "bd26d8db-86da-4f96-9efc-e5a4654a4a94",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rate = await response.parse()
            assert_matches_type(RateAddResponse, rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_pricing(self, async_client: AsyncPymews) -> None:
        rate = await async_client.api.connector.v1.rates.get_pricing(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            first_time_unit_start_utc=parse_datetime("2022-01-01T23:00:00.000Z"),
            last_time_unit_start_utc=parse_datetime("2022-01-03T23:00:00.000Z"),
            rate_id="ed4b660b-19d0-434b-9360-a4de2ea42eda",
        )
        assert_matches_type(RateGetPricingResponse, rate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_pricing_with_all_params(self, async_client: AsyncPymews) -> None:
        rate = await async_client.api.connector.v1.rates.get_pricing(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            first_time_unit_start_utc=parse_datetime("2022-01-01T23:00:00.000Z"),
            last_time_unit_start_utc=parse_datetime("2022-01-03T23:00:00.000Z"),
            rate_id="ed4b660b-19d0-434b-9360-a4de2ea42eda",
            product_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RateGetPricingResponse, rate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_pricing(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.rates.with_raw_response.get_pricing(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            first_time_unit_start_utc=parse_datetime("2022-01-01T23:00:00.000Z"),
            last_time_unit_start_utc=parse_datetime("2022-01-03T23:00:00.000Z"),
            rate_id="ed4b660b-19d0-434b-9360-a4de2ea42eda",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate = await response.parse()
        assert_matches_type(RateGetPricingResponse, rate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_pricing(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.rates.with_streaming_response.get_pricing(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            first_time_unit_start_utc=parse_datetime("2022-01-01T23:00:00.000Z"),
            last_time_unit_start_utc=parse_datetime("2022-01-03T23:00:00.000Z"),
            rate_id="ed4b660b-19d0-434b-9360-a4de2ea42eda",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rate = await response.parse()
            assert_matches_type(RateGetPricingResponse, rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_set(self, async_client: AsyncPymews) -> None:
        rate = await async_client.api.connector.v1.rates.set(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            rates=[
                {
                    "names": {"en-US": "Base rate"},
                    "pricing_type": "BaseRatePricing",
                    "rate_group_id": "d7adfddc-c2dc-4798-ace2-28de7b25408f",
                    "service_id": "956176af-e10b-4f3c-beb7-274801bce328",
                    "type": "Public",
                },
                {
                    "names": {"en-US": "Dependent rate"},
                    "pricing_type": "DependentRatePricing",
                    "rate_group_id": "eid:RG10",
                    "service_id": "eid:Stay",
                    "type": "Private",
                },
            ],
        )
        assert_matches_type(RateSetResponse, rate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_set_with_all_params(self, async_client: AsyncPymews) -> None:
        rate = await async_client.api.connector.v1.rates.set(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            rates=[
                {
                    "names": {"en-US": "Base rate"},
                    "pricing_type": "BaseRatePricing",
                    "rate_group_id": "d7adfddc-c2dc-4798-ace2-28de7b25408f",
                    "service_id": "956176af-e10b-4f3c-beb7-274801bce328",
                    "type": "Public",
                    "accounting_category_id": "07781f3c-94b6-4b31-9175-03786a84cd50",
                    "business_segment_id": "dc9188f6-fb61-412c-b3fd-af32dab082ed",
                    "descriptions": {"en-US": "Base rate description."},
                    "external_identifier": "ExternalIdentifier",
                    "external_names": {"en-US": "External base rate"},
                    "id": "e1b0bf46-32a3-4f7c-99c1-1ff78447d55d",
                    "is_enabled": True,
                    "pricing": {
                        "base_rate_pricing": {
                            "amount": {
                                "currency": "EUR",
                                "tax_codes": ["string"],
                                "gross_value": 0,
                                "net_value": 100,
                            }
                        },
                        "dependent_rate_pricing": {
                            "base_rate_id": "x",
                            "absolute_adjustment": 0,
                            "relative_adjustment": 0,
                        },
                    },
                    "short_names": {"en-US": "BR"},
                },
                {
                    "names": {"en-US": "Dependent rate"},
                    "pricing_type": "DependentRatePricing",
                    "rate_group_id": "eid:RG10",
                    "service_id": "eid:Stay",
                    "type": "Private",
                    "accounting_category_id": "07781f3c-94b6-4b31-9175-03786a84cd50",
                    "business_segment_id": "dc9188f6-fb61-412c-b3fd-af32dab082ed",
                    "descriptions": {"en-US": "Dependent rate description."},
                    "external_identifier": "55698",
                    "external_names": {"en-US": "External dependent rate"},
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "is_enabled": False,
                    "pricing": {
                        "base_rate_pricing": {
                            "amount": {
                                "currency": "x",
                                "tax_codes": ["string"],
                                "gross_value": 0,
                                "net_value": 0,
                            }
                        },
                        "dependent_rate_pricing": {
                            "base_rate_id": "00392166-3869-4174-b491-cf0162524a38",
                            "absolute_adjustment": 10,
                            "relative_adjustment": 0.25,
                        },
                    },
                    "short_names": {"en-US": "DR"},
                },
            ],
            enterprise_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )
        assert_matches_type(RateSetResponse, rate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_set(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.rates.with_raw_response.set(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            rates=[
                {
                    "names": {"en-US": "Base rate"},
                    "pricing_type": "BaseRatePricing",
                    "rate_group_id": "d7adfddc-c2dc-4798-ace2-28de7b25408f",
                    "service_id": "956176af-e10b-4f3c-beb7-274801bce328",
                    "type": "Public",
                },
                {
                    "names": {"en-US": "Dependent rate"},
                    "pricing_type": "DependentRatePricing",
                    "rate_group_id": "eid:RG10",
                    "service_id": "eid:Stay",
                    "type": "Private",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate = await response.parse()
        assert_matches_type(RateSetResponse, rate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_set(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.rates.with_streaming_response.set(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            rates=[
                {
                    "names": {"en-US": "Base rate"},
                    "pricing_type": "BaseRatePricing",
                    "rate_group_id": "d7adfddc-c2dc-4798-ace2-28de7b25408f",
                    "service_id": "956176af-e10b-4f3c-beb7-274801bce328",
                    "type": "Public",
                },
                {
                    "names": {"en-US": "Dependent rate"},
                    "pricing_type": "DependentRatePricing",
                    "rate_group_id": "eid:RG10",
                    "service_id": "eid:Stay",
                    "type": "Private",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rate = await response.parse()
            assert_matches_type(RateSetResponse, rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_price(self, async_client: AsyncPymews) -> None:
        rate = await async_client.api.connector.v1.rates.update_price(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            price_updates=[{}, {}],
            rate_id="ed4b660b-19d0-434b-9360-a4de2ea42eda",
        )
        assert_matches_type(object, rate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_price_with_all_params(self, async_client: AsyncPymews) -> None:
        rate = await async_client.api.connector.v1.rates.update_price(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            price_updates=[
                {
                    "category_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "first_time_unit_start_utc": parse_datetime("2022-01-01T23:00:00.000Z"),
                    "last_time_unit_start_utc": parse_datetime("2022-01-03T23:00:00.000Z"),
                    "value": 111,
                },
                {
                    "category_id": "e3aa3117-dff0-46b7-b49a-2c0391e70ff9",
                    "first_time_unit_start_utc": parse_datetime("2022-01-04T23:00:00.000Z"),
                    "last_time_unit_start_utc": parse_datetime("2022-01-05T23:00:00.000Z"),
                    "value": 222,
                },
            ],
            rate_id="ed4b660b-19d0-434b-9360-a4de2ea42eda",
            product_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, rate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update_price(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.rates.with_raw_response.update_price(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            price_updates=[{}, {}],
            rate_id="ed4b660b-19d0-434b-9360-a4de2ea42eda",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate = await response.parse()
        assert_matches_type(object, rate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update_price(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.rates.with_streaming_response.update_price(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            price_updates=[{}, {}],
            rate_id="ed4b660b-19d0-434b-9360-a4de2ea42eda",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rate = await response.parse()
            assert_matches_type(object, rate, path=["response"])

        assert cast(Any, response.is_closed) is True
