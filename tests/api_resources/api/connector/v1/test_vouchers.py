# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pymews import Pymews, AsyncPymews
from tests.utils import assert_matches_type
from pymews._utils import parse_datetime
from pymews.types.api.connector.v1 import (
    VoucherWriteResult,
    VoucherListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVouchers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Pymews) -> None:
        voucher = client.api.connector.v1.vouchers.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            voucher_updates=[
                {"voucher_id": "fe568bbd-1ecb-4bb2-bf77-96c3698de20d"},
                {"voucher_id": "f4a9942c-2616-4074-b1f4-4b959515e933"},
            ],
        )
        assert_matches_type(VoucherWriteResult, voucher, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Pymews) -> None:
        voucher = client.api.connector.v1.vouchers.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            voucher_updates=[
                {
                    "voucher_id": "fe568bbd-1ecb-4bb2-bf77-96c3698de20d",
                    "assigned_rate_ids": {
                        "value": ["181f8cdd-04ee-4bf5-ba3e-44c108eca3cb", "8bebeddc-9137-432d-810c-1b998a90ac9a"]
                    },
                    "company_id": {"value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                    "external_identifier": {"value": "Value"},
                    "name": {"value": "Weekend Voucher"},
                    "occupiable_interval_end_utc": {"value": "Value"},
                    "occupiable_interval_start_utc": {"value": "Value"},
                    "type": {"value": "Public"},
                },
                {
                    "voucher_id": "f4a9942c-2616-4074-b1f4-4b959515e933",
                    "assigned_rate_ids": {
                        "value": ["181f8cdd-04ee-4bf5-ba3e-44c108eca3cb", "8bebeddc-9137-432d-810c-1b998a90ac9a"]
                    },
                    "company_id": {"value": "3506994b-3c0b-49ba-9f57-ac4700641440"},
                    "external_identifier": {"value": "VCHR-278"},
                    "name": {"value": "Weekend Voucher"},
                    "occupiable_interval_end_utc": {"value": "2024-01-01T22:00:00Z"},
                    "occupiable_interval_start_utc": {"value": "2023-12-31T22:00:00Z"},
                    "type": {"value": "PartnerCompany"},
                },
            ],
            enterprise_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )
        assert_matches_type(VoucherWriteResult, voucher, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Pymews) -> None:
        response = client.api.connector.v1.vouchers.with_raw_response.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            voucher_updates=[
                {"voucher_id": "fe568bbd-1ecb-4bb2-bf77-96c3698de20d"},
                {"voucher_id": "f4a9942c-2616-4074-b1f4-4b959515e933"},
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voucher = response.parse()
        assert_matches_type(VoucherWriteResult, voucher, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Pymews) -> None:
        with client.api.connector.v1.vouchers.with_streaming_response.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            voucher_updates=[
                {"voucher_id": "fe568bbd-1ecb-4bb2-bf77-96c3698de20d"},
                {"voucher_id": "f4a9942c-2616-4074-b1f4-4b959515e933"},
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voucher = response.parse()
            assert_matches_type(VoucherWriteResult, voucher, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Pymews) -> None:
        voucher = client.api.connector.v1.vouchers.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            extent={},
            limitation={"count": 10},
            service_ids=["bd26d8db-86da-4f96-9efc-e5a4654a4a94"],
        )
        assert_matches_type(VoucherListResponse, voucher, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Pymews) -> None:
        voucher = client.api.connector.v1.vouchers.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            extent={
                "companies": False,
                "rates": False,
                "voucher_assignments": True,
                "voucher_codes": True,
                "vouchers": True,
            },
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            service_ids=["bd26d8db-86da-4f96-9efc-e5a4654a4a94"],
            activity_states=["Active"],
            company_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            external_identifiers=["Voucher-001", "Voucher-002"],
            updated_utc={
                "end_utc": parse_datetime("2023-10-17T00:00:00Z"),
                "start_utc": parse_datetime("2023-10-10T00:00:00Z"),
            },
            voucher_code_values=["TEST-VOUCHER-CODE"],
            voucher_ids=["fe568bbd-1ecb-4bb2-bf77-96c3698de20d"],
        )
        assert_matches_type(VoucherListResponse, voucher, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Pymews) -> None:
        response = client.api.connector.v1.vouchers.with_raw_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            extent={},
            limitation={"count": 10},
            service_ids=["bd26d8db-86da-4f96-9efc-e5a4654a4a94"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voucher = response.parse()
        assert_matches_type(VoucherListResponse, voucher, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Pymews) -> None:
        with client.api.connector.v1.vouchers.with_streaming_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            extent={},
            limitation={"count": 10},
            service_ids=["bd26d8db-86da-4f96-9efc-e5a4654a4a94"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voucher = response.parse()
            assert_matches_type(VoucherListResponse, voucher, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Pymews) -> None:
        voucher = client.api.connector.v1.vouchers.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            voucher_ids=["fe568bbd-1ecb-4bb2-bf77-96c3698de20d", "f4a9942c-2616-4074-b1f4-4b959515e933"],
        )
        assert_matches_type(object, voucher, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_delete_with_all_params(self, client: Pymews) -> None:
        voucher = client.api.connector.v1.vouchers.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            voucher_ids=["fe568bbd-1ecb-4bb2-bf77-96c3698de20d", "f4a9942c-2616-4074-b1f4-4b959515e933"],
            enterprise_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )
        assert_matches_type(object, voucher, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Pymews) -> None:
        response = client.api.connector.v1.vouchers.with_raw_response.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            voucher_ids=["fe568bbd-1ecb-4bb2-bf77-96c3698de20d", "f4a9942c-2616-4074-b1f4-4b959515e933"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voucher = response.parse()
        assert_matches_type(object, voucher, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Pymews) -> None:
        with client.api.connector.v1.vouchers.with_streaming_response.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            voucher_ids=["fe568bbd-1ecb-4bb2-bf77-96c3698de20d", "f4a9942c-2616-4074-b1f4-4b959515e933"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voucher = response.parse()
            assert_matches_type(object, voucher, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_add(self, client: Pymews) -> None:
        voucher = client.api.connector.v1.vouchers.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            voucher_parameters=[
                {
                    "name": "Weekend Voucher",
                    "service_id": "bd26d8db-86da-4f96-9efc-e5a4654a4a94",
                    "type": "Public",
                },
                {
                    "name": "Sample company voucher",
                    "service_id": "bd26d8db-86da-4f96-9efc-e5a4654a4a94",
                    "type": "PartnerCompany",
                },
            ],
        )
        assert_matches_type(VoucherWriteResult, voucher, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_add_with_all_params(self, client: Pymews) -> None:
        voucher = client.api.connector.v1.vouchers.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            voucher_parameters=[
                {
                    "name": "Weekend Voucher",
                    "service_id": "bd26d8db-86da-4f96-9efc-e5a4654a4a94",
                    "type": "Public",
                    "assigned_rate_ids": [
                        "181f8cdd-04ee-4bf5-ba3e-44c108eca3cb",
                        "8bebeddc-9137-432d-810c-1b998a90ac9a",
                    ],
                    "company_id": None,
                    "external_identifier": None,
                    "occupiable_interval_end_utc": None,
                    "occupiable_interval_start_utc": None,
                },
                {
                    "name": "Sample company voucher",
                    "service_id": "bd26d8db-86da-4f96-9efc-e5a4654a4a94",
                    "type": "PartnerCompany",
                    "assigned_rate_ids": [
                        "181f8cdd-04ee-4bf5-ba3e-44c108eca3cb",
                        "8bebeddc-9137-432d-810c-1b998a90ac9a",
                    ],
                    "company_id": "3506994b-3c0b-49ba-9f57-ac4700641440",
                    "external_identifier": "VCHR-278",
                    "occupiable_interval_end_utc": parse_datetime("2024-01-01T22:00:00Z"),
                    "occupiable_interval_start_utc": parse_datetime("2023-12-31T22:00:00Z"),
                },
            ],
            enterprise_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )
        assert_matches_type(VoucherWriteResult, voucher, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_add(self, client: Pymews) -> None:
        response = client.api.connector.v1.vouchers.with_raw_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            voucher_parameters=[
                {
                    "name": "Weekend Voucher",
                    "service_id": "bd26d8db-86da-4f96-9efc-e5a4654a4a94",
                    "type": "Public",
                },
                {
                    "name": "Sample company voucher",
                    "service_id": "bd26d8db-86da-4f96-9efc-e5a4654a4a94",
                    "type": "PartnerCompany",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voucher = response.parse()
        assert_matches_type(VoucherWriteResult, voucher, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_add(self, client: Pymews) -> None:
        with client.api.connector.v1.vouchers.with_streaming_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            voucher_parameters=[
                {
                    "name": "Weekend Voucher",
                    "service_id": "bd26d8db-86da-4f96-9efc-e5a4654a4a94",
                    "type": "Public",
                },
                {
                    "name": "Sample company voucher",
                    "service_id": "bd26d8db-86da-4f96-9efc-e5a4654a4a94",
                    "type": "PartnerCompany",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voucher = response.parse()
            assert_matches_type(VoucherWriteResult, voucher, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncVouchers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncPymews) -> None:
        voucher = await async_client.api.connector.v1.vouchers.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            voucher_updates=[
                {"voucher_id": "fe568bbd-1ecb-4bb2-bf77-96c3698de20d"},
                {"voucher_id": "f4a9942c-2616-4074-b1f4-4b959515e933"},
            ],
        )
        assert_matches_type(VoucherWriteResult, voucher, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncPymews) -> None:
        voucher = await async_client.api.connector.v1.vouchers.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            voucher_updates=[
                {
                    "voucher_id": "fe568bbd-1ecb-4bb2-bf77-96c3698de20d",
                    "assigned_rate_ids": {
                        "value": ["181f8cdd-04ee-4bf5-ba3e-44c108eca3cb", "8bebeddc-9137-432d-810c-1b998a90ac9a"]
                    },
                    "company_id": {"value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                    "external_identifier": {"value": "Value"},
                    "name": {"value": "Weekend Voucher"},
                    "occupiable_interval_end_utc": {"value": "Value"},
                    "occupiable_interval_start_utc": {"value": "Value"},
                    "type": {"value": "Public"},
                },
                {
                    "voucher_id": "f4a9942c-2616-4074-b1f4-4b959515e933",
                    "assigned_rate_ids": {
                        "value": ["181f8cdd-04ee-4bf5-ba3e-44c108eca3cb", "8bebeddc-9137-432d-810c-1b998a90ac9a"]
                    },
                    "company_id": {"value": "3506994b-3c0b-49ba-9f57-ac4700641440"},
                    "external_identifier": {"value": "VCHR-278"},
                    "name": {"value": "Weekend Voucher"},
                    "occupiable_interval_end_utc": {"value": "2024-01-01T22:00:00Z"},
                    "occupiable_interval_start_utc": {"value": "2023-12-31T22:00:00Z"},
                    "type": {"value": "PartnerCompany"},
                },
            ],
            enterprise_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )
        assert_matches_type(VoucherWriteResult, voucher, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.vouchers.with_raw_response.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            voucher_updates=[
                {"voucher_id": "fe568bbd-1ecb-4bb2-bf77-96c3698de20d"},
                {"voucher_id": "f4a9942c-2616-4074-b1f4-4b959515e933"},
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voucher = await response.parse()
        assert_matches_type(VoucherWriteResult, voucher, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.vouchers.with_streaming_response.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            voucher_updates=[
                {"voucher_id": "fe568bbd-1ecb-4bb2-bf77-96c3698de20d"},
                {"voucher_id": "f4a9942c-2616-4074-b1f4-4b959515e933"},
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voucher = await response.parse()
            assert_matches_type(VoucherWriteResult, voucher, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncPymews) -> None:
        voucher = await async_client.api.connector.v1.vouchers.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            extent={},
            limitation={"count": 10},
            service_ids=["bd26d8db-86da-4f96-9efc-e5a4654a4a94"],
        )
        assert_matches_type(VoucherListResponse, voucher, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPymews) -> None:
        voucher = await async_client.api.connector.v1.vouchers.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            extent={
                "companies": False,
                "rates": False,
                "voucher_assignments": True,
                "voucher_codes": True,
                "vouchers": True,
            },
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            service_ids=["bd26d8db-86da-4f96-9efc-e5a4654a4a94"],
            activity_states=["Active"],
            company_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            external_identifiers=["Voucher-001", "Voucher-002"],
            updated_utc={
                "end_utc": parse_datetime("2023-10-17T00:00:00Z"),
                "start_utc": parse_datetime("2023-10-10T00:00:00Z"),
            },
            voucher_code_values=["TEST-VOUCHER-CODE"],
            voucher_ids=["fe568bbd-1ecb-4bb2-bf77-96c3698de20d"],
        )
        assert_matches_type(VoucherListResponse, voucher, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.vouchers.with_raw_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            extent={},
            limitation={"count": 10},
            service_ids=["bd26d8db-86da-4f96-9efc-e5a4654a4a94"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voucher = await response.parse()
        assert_matches_type(VoucherListResponse, voucher, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.vouchers.with_streaming_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            extent={},
            limitation={"count": 10},
            service_ids=["bd26d8db-86da-4f96-9efc-e5a4654a4a94"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voucher = await response.parse()
            assert_matches_type(VoucherListResponse, voucher, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncPymews) -> None:
        voucher = await async_client.api.connector.v1.vouchers.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            voucher_ids=["fe568bbd-1ecb-4bb2-bf77-96c3698de20d", "f4a9942c-2616-4074-b1f4-4b959515e933"],
        )
        assert_matches_type(object, voucher, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncPymews) -> None:
        voucher = await async_client.api.connector.v1.vouchers.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            voucher_ids=["fe568bbd-1ecb-4bb2-bf77-96c3698de20d", "f4a9942c-2616-4074-b1f4-4b959515e933"],
            enterprise_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )
        assert_matches_type(object, voucher, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.vouchers.with_raw_response.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            voucher_ids=["fe568bbd-1ecb-4bb2-bf77-96c3698de20d", "f4a9942c-2616-4074-b1f4-4b959515e933"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voucher = await response.parse()
        assert_matches_type(object, voucher, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.vouchers.with_streaming_response.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            voucher_ids=["fe568bbd-1ecb-4bb2-bf77-96c3698de20d", "f4a9942c-2616-4074-b1f4-4b959515e933"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voucher = await response.parse()
            assert_matches_type(object, voucher, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_add(self, async_client: AsyncPymews) -> None:
        voucher = await async_client.api.connector.v1.vouchers.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            voucher_parameters=[
                {
                    "name": "Weekend Voucher",
                    "service_id": "bd26d8db-86da-4f96-9efc-e5a4654a4a94",
                    "type": "Public",
                },
                {
                    "name": "Sample company voucher",
                    "service_id": "bd26d8db-86da-4f96-9efc-e5a4654a4a94",
                    "type": "PartnerCompany",
                },
            ],
        )
        assert_matches_type(VoucherWriteResult, voucher, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_add_with_all_params(self, async_client: AsyncPymews) -> None:
        voucher = await async_client.api.connector.v1.vouchers.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            voucher_parameters=[
                {
                    "name": "Weekend Voucher",
                    "service_id": "bd26d8db-86da-4f96-9efc-e5a4654a4a94",
                    "type": "Public",
                    "assigned_rate_ids": [
                        "181f8cdd-04ee-4bf5-ba3e-44c108eca3cb",
                        "8bebeddc-9137-432d-810c-1b998a90ac9a",
                    ],
                    "company_id": None,
                    "external_identifier": None,
                    "occupiable_interval_end_utc": None,
                    "occupiable_interval_start_utc": None,
                },
                {
                    "name": "Sample company voucher",
                    "service_id": "bd26d8db-86da-4f96-9efc-e5a4654a4a94",
                    "type": "PartnerCompany",
                    "assigned_rate_ids": [
                        "181f8cdd-04ee-4bf5-ba3e-44c108eca3cb",
                        "8bebeddc-9137-432d-810c-1b998a90ac9a",
                    ],
                    "company_id": "3506994b-3c0b-49ba-9f57-ac4700641440",
                    "external_identifier": "VCHR-278",
                    "occupiable_interval_end_utc": parse_datetime("2024-01-01T22:00:00Z"),
                    "occupiable_interval_start_utc": parse_datetime("2023-12-31T22:00:00Z"),
                },
            ],
            enterprise_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )
        assert_matches_type(VoucherWriteResult, voucher, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.vouchers.with_raw_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            voucher_parameters=[
                {
                    "name": "Weekend Voucher",
                    "service_id": "bd26d8db-86da-4f96-9efc-e5a4654a4a94",
                    "type": "Public",
                },
                {
                    "name": "Sample company voucher",
                    "service_id": "bd26d8db-86da-4f96-9efc-e5a4654a4a94",
                    "type": "PartnerCompany",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voucher = await response.parse()
        assert_matches_type(VoucherWriteResult, voucher, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.vouchers.with_streaming_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            voucher_parameters=[
                {
                    "name": "Weekend Voucher",
                    "service_id": "bd26d8db-86da-4f96-9efc-e5a4654a4a94",
                    "type": "Public",
                },
                {
                    "name": "Sample company voucher",
                    "service_id": "bd26d8db-86da-4f96-9efc-e5a4654a4a94",
                    "type": "PartnerCompany",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voucher = await response.parse()
            assert_matches_type(VoucherWriteResult, voucher, path=["response"])

        assert cast(Any, response.is_closed) is True
