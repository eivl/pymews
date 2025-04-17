# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pymews import Pymews, AsyncPymews
from tests.utils import assert_matches_type
from pymews._utils import parse_datetime
from pymews.types.api.connector.v1 import (
    BillAddResponse,
    BillListResponse,
    BillCloseResponse,
    BillGetPdfResponse,
    BillUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBills:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Pymews) -> None:
        bill = client.api.connector.v1.bills.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            bills_updates=[{"bill_id": "ea087d64-3901-4eee-b0b7-9fce4c58a005"}],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )
        assert_matches_type(BillUpdateResponse, bill, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Pymews) -> None:
        bill = client.api.connector.v1.bills.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            bills_updates=[
                {
                    "bill_id": "ea087d64-3901-4eee-b0b7-9fce4c58a005",
                    "account_id": {"value": "c6f5c82d-621a-4c8a-903b-1b0a9a23b71f"},
                    "associated_account_ids": {"value": ["fadd5bb6-b428-45d5-94f8-fd0d89fece6d"]},
                }
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            enterprise_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )
        assert_matches_type(BillUpdateResponse, bill, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Pymews) -> None:
        response = client.api.connector.v1.bills.with_raw_response.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            bills_updates=[{"bill_id": "ea087d64-3901-4eee-b0b7-9fce4c58a005"}],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bill = response.parse()
        assert_matches_type(BillUpdateResponse, bill, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Pymews) -> None:
        with client.api.connector.v1.bills.with_streaming_response.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            bills_updates=[{"bill_id": "ea087d64-3901-4eee-b0b7-9fce4c58a005"}],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bill = response.parse()
            assert_matches_type(BillUpdateResponse, bill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Pymews) -> None:
        bill = client.api.connector.v1.bills.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 100},
        )
        assert_matches_type(BillListResponse, bill, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Pymews) -> None:
        bill = client.api.connector.v1.bills.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 100,
                "cursor": "e7f26210-10e7-462e-9da8-ae8300be8ab7",
            },
            bill_ids=["e654f217-d1b5-46be-a820-e93ba568dfac"],
            closed_utc={
                "end_utc": parse_datetime("2020-02-10T00:00:00Z"),
                "start_utc": parse_datetime("2020-02-05T00:00:00Z"),
            },
            correction_state=["Bill"],
            created_utc={
                "end_utc": parse_datetime("2020-02-10T00:00:00Z"),
                "start_utc": parse_datetime("2020-02-05T00:00:00Z"),
            },
            customer_ids=["fe795f96-0b64-445b-89ed-c032563f2bac"],
            due_utc={
                "end_utc": parse_datetime("2019-12-27T18:11:19.117Z"),
                "start_utc": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            extent={"items": False},
            paid_utc={
                "end_utc": parse_datetime("2019-12-27T18:11:19.117Z"),
                "start_utc": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            state="Closed",
            updated_utc={
                "end_utc": parse_datetime("2020-02-10T00:00:00Z"),
                "start_utc": parse_datetime("2020-02-05T00:00:00Z"),
            },
        )
        assert_matches_type(BillListResponse, bill, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Pymews) -> None:
        response = client.api.connector.v1.bills.with_raw_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 100},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bill = response.parse()
        assert_matches_type(BillListResponse, bill, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Pymews) -> None:
        with client.api.connector.v1.bills.with_streaming_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 100},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bill = response.parse()
            assert_matches_type(BillListResponse, bill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Pymews) -> None:
        bill = client.api.connector.v1.bills.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            bill_ids=["177966b7-f3d9-42b7-ba49-abd80057329b"],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )
        assert_matches_type(object, bill, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_delete_with_all_params(self, client: Pymews) -> None:
        bill = client.api.connector.v1.bills.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            bill_ids=["177966b7-f3d9-42b7-ba49-abd80057329b"],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            enterprise_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )
        assert_matches_type(object, bill, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Pymews) -> None:
        response = client.api.connector.v1.bills.with_raw_response.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            bill_ids=["177966b7-f3d9-42b7-ba49-abd80057329b"],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bill = response.parse()
        assert_matches_type(object, bill, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Pymews) -> None:
        with client.api.connector.v1.bills.with_streaming_response.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            bill_ids=["177966b7-f3d9-42b7-ba49-abd80057329b"],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bill = response.parse()
            assert_matches_type(object, bill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_add(self, client: Pymews) -> None:
        bill = client.api.connector.v1.bills.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            bills=[{"account_id": "a5786a7b-a388-43cc-a838-abd7007b5ff7"}],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )
        assert_matches_type(BillAddResponse, bill, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_add_with_all_params(self, client: Pymews) -> None:
        bill = client.api.connector.v1.bills.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            bills=[
                {
                    "account_id": "a5786a7b-a388-43cc-a838-abd7007b5ff7",
                    "associated_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "name": "Bill of Joe Doe",
                }
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            enterprise_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )
        assert_matches_type(BillAddResponse, bill, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_add(self, client: Pymews) -> None:
        response = client.api.connector.v1.bills.with_raw_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            bills=[{"account_id": "a5786a7b-a388-43cc-a838-abd7007b5ff7"}],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bill = response.parse()
        assert_matches_type(BillAddResponse, bill, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_add(self, client: Pymews) -> None:
        with client.api.connector.v1.bills.with_streaming_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            bills=[{"account_id": "a5786a7b-a388-43cc-a838-abd7007b5ff7"}],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bill = response.parse()
            assert_matches_type(BillAddResponse, bill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_close(self, client: Pymews) -> None:
        bill = client.api.connector.v1.bills.close(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            bill_id="44eba542-193e-47c7-8077-abd7008eb206",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            type="Receipt",
        )
        assert_matches_type(BillCloseResponse, bill, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_close_with_all_params(self, client: Pymews) -> None:
        bill = client.api.connector.v1.bills.close(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            bill_id="44eba542-193e-47c7-8077-abd7008eb206",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            type="Receipt",
            account_address={
                "city": "Havířov",
                "country_code": "CZ",
                "country_subdivision_code": None,
                "line1": "Astronautů 2",
                "line2": "",
                "postal_code": "736 01",
            },
            account_tax_identifier={"value": "446768"},
            address={
                "city": "City",
                "country_code": "CountryCode",
                "country_subdivision_code": "CountrySubdivisionCode",
                "line1": "Line1",
                "line2": "Line2",
                "postal_code": "PostalCode",
            },
            associated_account_data=[
                {
                    "id": "84b25778-c1dd-48dc-8c00-ab3a00b6df14",
                    "address": {
                        "city": "Havířov",
                        "country_code": "CZ",
                        "country_subdivision_code": None,
                        "line1": "Astronautů 2",
                        "line2": "",
                        "postal_code": "736 01",
                    },
                    "tax_identifier": {"value": "123459"},
                }
            ],
            bill_counter_id="84b25778-c1dd-48dc-8c00-ab3a00b6df14",
            company_tax_identifier={"value": "Value"},
            due_date={"value": "2020-07-14"},
            enterprise_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
            fiscal_machine_id=None,
            notes={"value": "Bill closing note"},
            options={
                "display_customer": {"value": False},
                "display_taxation": {"value": True},
            },
            purchase_order_number={"value": "XX-123"},
            taxed_date={"value": "2020-07-07"},
            tax_identifier={"value": "Value"},
            variable_symbol={"value": "5343"},
        )
        assert_matches_type(BillCloseResponse, bill, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_close(self, client: Pymews) -> None:
        response = client.api.connector.v1.bills.with_raw_response.close(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            bill_id="44eba542-193e-47c7-8077-abd7008eb206",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            type="Receipt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bill = response.parse()
        assert_matches_type(BillCloseResponse, bill, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_close(self, client: Pymews) -> None:
        with client.api.connector.v1.bills.with_streaming_response.close(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            bill_id="44eba542-193e-47c7-8077-abd7008eb206",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            type="Receipt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bill = response.parse()
            assert_matches_type(BillCloseResponse, bill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_pdf(self, client: Pymews) -> None:
        bill = client.api.connector.v1.bills.get_pdf(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            bill_id="44eba542-193e-47c7-8077-abd7008eb206",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )
        assert_matches_type(BillGetPdfResponse, bill, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_pdf_with_all_params(self, client: Pymews) -> None:
        bill = client.api.connector.v1.bills.get_pdf(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            bill_id="44eba542-193e-47c7-8077-abd7008eb206",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            bill_print_event_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            pdf_template="Detailed",
            print_reason="PrintReason",
        )
        assert_matches_type(BillGetPdfResponse, bill, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_pdf(self, client: Pymews) -> None:
        response = client.api.connector.v1.bills.with_raw_response.get_pdf(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            bill_id="44eba542-193e-47c7-8077-abd7008eb206",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bill = response.parse()
        assert_matches_type(BillGetPdfResponse, bill, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_pdf(self, client: Pymews) -> None:
        with client.api.connector.v1.bills.with_streaming_response.get_pdf(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            bill_id="44eba542-193e-47c7-8077-abd7008eb206",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bill = response.parse()
            assert_matches_type(BillGetPdfResponse, bill, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBills:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncPymews) -> None:
        bill = await async_client.api.connector.v1.bills.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            bills_updates=[{"bill_id": "ea087d64-3901-4eee-b0b7-9fce4c58a005"}],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )
        assert_matches_type(BillUpdateResponse, bill, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncPymews) -> None:
        bill = await async_client.api.connector.v1.bills.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            bills_updates=[
                {
                    "bill_id": "ea087d64-3901-4eee-b0b7-9fce4c58a005",
                    "account_id": {"value": "c6f5c82d-621a-4c8a-903b-1b0a9a23b71f"},
                    "associated_account_ids": {"value": ["fadd5bb6-b428-45d5-94f8-fd0d89fece6d"]},
                }
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            enterprise_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )
        assert_matches_type(BillUpdateResponse, bill, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.bills.with_raw_response.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            bills_updates=[{"bill_id": "ea087d64-3901-4eee-b0b7-9fce4c58a005"}],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bill = await response.parse()
        assert_matches_type(BillUpdateResponse, bill, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.bills.with_streaming_response.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            bills_updates=[{"bill_id": "ea087d64-3901-4eee-b0b7-9fce4c58a005"}],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bill = await response.parse()
            assert_matches_type(BillUpdateResponse, bill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncPymews) -> None:
        bill = await async_client.api.connector.v1.bills.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 100},
        )
        assert_matches_type(BillListResponse, bill, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPymews) -> None:
        bill = await async_client.api.connector.v1.bills.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 100,
                "cursor": "e7f26210-10e7-462e-9da8-ae8300be8ab7",
            },
            bill_ids=["e654f217-d1b5-46be-a820-e93ba568dfac"],
            closed_utc={
                "end_utc": parse_datetime("2020-02-10T00:00:00Z"),
                "start_utc": parse_datetime("2020-02-05T00:00:00Z"),
            },
            correction_state=["Bill"],
            created_utc={
                "end_utc": parse_datetime("2020-02-10T00:00:00Z"),
                "start_utc": parse_datetime("2020-02-05T00:00:00Z"),
            },
            customer_ids=["fe795f96-0b64-445b-89ed-c032563f2bac"],
            due_utc={
                "end_utc": parse_datetime("2019-12-27T18:11:19.117Z"),
                "start_utc": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            extent={"items": False},
            paid_utc={
                "end_utc": parse_datetime("2019-12-27T18:11:19.117Z"),
                "start_utc": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            state="Closed",
            updated_utc={
                "end_utc": parse_datetime("2020-02-10T00:00:00Z"),
                "start_utc": parse_datetime("2020-02-05T00:00:00Z"),
            },
        )
        assert_matches_type(BillListResponse, bill, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.bills.with_raw_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 100},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bill = await response.parse()
        assert_matches_type(BillListResponse, bill, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.bills.with_streaming_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 100},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bill = await response.parse()
            assert_matches_type(BillListResponse, bill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncPymews) -> None:
        bill = await async_client.api.connector.v1.bills.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            bill_ids=["177966b7-f3d9-42b7-ba49-abd80057329b"],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )
        assert_matches_type(object, bill, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncPymews) -> None:
        bill = await async_client.api.connector.v1.bills.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            bill_ids=["177966b7-f3d9-42b7-ba49-abd80057329b"],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            enterprise_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )
        assert_matches_type(object, bill, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.bills.with_raw_response.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            bill_ids=["177966b7-f3d9-42b7-ba49-abd80057329b"],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bill = await response.parse()
        assert_matches_type(object, bill, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.bills.with_streaming_response.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            bill_ids=["177966b7-f3d9-42b7-ba49-abd80057329b"],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bill = await response.parse()
            assert_matches_type(object, bill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_add(self, async_client: AsyncPymews) -> None:
        bill = await async_client.api.connector.v1.bills.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            bills=[{"account_id": "a5786a7b-a388-43cc-a838-abd7007b5ff7"}],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )
        assert_matches_type(BillAddResponse, bill, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_add_with_all_params(self, async_client: AsyncPymews) -> None:
        bill = await async_client.api.connector.v1.bills.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            bills=[
                {
                    "account_id": "a5786a7b-a388-43cc-a838-abd7007b5ff7",
                    "associated_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "name": "Bill of Joe Doe",
                }
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            enterprise_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )
        assert_matches_type(BillAddResponse, bill, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.bills.with_raw_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            bills=[{"account_id": "a5786a7b-a388-43cc-a838-abd7007b5ff7"}],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bill = await response.parse()
        assert_matches_type(BillAddResponse, bill, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.bills.with_streaming_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            bills=[{"account_id": "a5786a7b-a388-43cc-a838-abd7007b5ff7"}],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bill = await response.parse()
            assert_matches_type(BillAddResponse, bill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_close(self, async_client: AsyncPymews) -> None:
        bill = await async_client.api.connector.v1.bills.close(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            bill_id="44eba542-193e-47c7-8077-abd7008eb206",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            type="Receipt",
        )
        assert_matches_type(BillCloseResponse, bill, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_close_with_all_params(self, async_client: AsyncPymews) -> None:
        bill = await async_client.api.connector.v1.bills.close(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            bill_id="44eba542-193e-47c7-8077-abd7008eb206",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            type="Receipt",
            account_address={
                "city": "Havířov",
                "country_code": "CZ",
                "country_subdivision_code": None,
                "line1": "Astronautů 2",
                "line2": "",
                "postal_code": "736 01",
            },
            account_tax_identifier={"value": "446768"},
            address={
                "city": "City",
                "country_code": "CountryCode",
                "country_subdivision_code": "CountrySubdivisionCode",
                "line1": "Line1",
                "line2": "Line2",
                "postal_code": "PostalCode",
            },
            associated_account_data=[
                {
                    "id": "84b25778-c1dd-48dc-8c00-ab3a00b6df14",
                    "address": {
                        "city": "Havířov",
                        "country_code": "CZ",
                        "country_subdivision_code": None,
                        "line1": "Astronautů 2",
                        "line2": "",
                        "postal_code": "736 01",
                    },
                    "tax_identifier": {"value": "123459"},
                }
            ],
            bill_counter_id="84b25778-c1dd-48dc-8c00-ab3a00b6df14",
            company_tax_identifier={"value": "Value"},
            due_date={"value": "2020-07-14"},
            enterprise_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
            fiscal_machine_id=None,
            notes={"value": "Bill closing note"},
            options={
                "display_customer": {"value": False},
                "display_taxation": {"value": True},
            },
            purchase_order_number={"value": "XX-123"},
            taxed_date={"value": "2020-07-07"},
            tax_identifier={"value": "Value"},
            variable_symbol={"value": "5343"},
        )
        assert_matches_type(BillCloseResponse, bill, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_close(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.bills.with_raw_response.close(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            bill_id="44eba542-193e-47c7-8077-abd7008eb206",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            type="Receipt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bill = await response.parse()
        assert_matches_type(BillCloseResponse, bill, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_close(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.bills.with_streaming_response.close(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            bill_id="44eba542-193e-47c7-8077-abd7008eb206",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            type="Receipt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bill = await response.parse()
            assert_matches_type(BillCloseResponse, bill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_pdf(self, async_client: AsyncPymews) -> None:
        bill = await async_client.api.connector.v1.bills.get_pdf(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            bill_id="44eba542-193e-47c7-8077-abd7008eb206",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )
        assert_matches_type(BillGetPdfResponse, bill, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_pdf_with_all_params(self, async_client: AsyncPymews) -> None:
        bill = await async_client.api.connector.v1.bills.get_pdf(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            bill_id="44eba542-193e-47c7-8077-abd7008eb206",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            bill_print_event_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            pdf_template="Detailed",
            print_reason="PrintReason",
        )
        assert_matches_type(BillGetPdfResponse, bill, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_pdf(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.bills.with_raw_response.get_pdf(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            bill_id="44eba542-193e-47c7-8077-abd7008eb206",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bill = await response.parse()
        assert_matches_type(BillGetPdfResponse, bill, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_pdf(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.bills.with_streaming_response.get_pdf(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            bill_id="44eba542-193e-47c7-8077-abd7008eb206",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bill = await response.parse()
            assert_matches_type(BillGetPdfResponse, bill, path=["response"])

        assert cast(Any, response.is_closed) is True
