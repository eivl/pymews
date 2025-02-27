# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pymews import Pymews, AsyncPymews
from tests.utils import assert_matches_type
from pymews._utils import parse_datetime
from pymews.types.api.connector.v1 import (
    ContractResult,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCompanyContracts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Pymews) -> None:
        company_contract = client.api.connector.v1.company_contracts.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            travel_agency_contract_updates=[{"travel_agency_contract_id": "652d4a22-ac33-42b7-abe7-af1f00820023"}],
        )
        assert_matches_type(ContractResult, company_contract, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Pymews) -> None:
        response = client.api.connector.v1.company_contracts.with_raw_response.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            travel_agency_contract_updates=[{"travel_agency_contract_id": "652d4a22-ac33-42b7-abe7-af1f00820023"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company_contract = response.parse()
        assert_matches_type(ContractResult, company_contract, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Pymews) -> None:
        with client.api.connector.v1.company_contracts.with_streaming_response.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            travel_agency_contract_updates=[{"travel_agency_contract_id": "652d4a22-ac33-42b7-abe7-af1f00820023"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company_contract = response.parse()
            assert_matches_type(ContractResult, company_contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Pymews) -> None:
        company_contract = client.api.connector.v1.company_contracts.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            service_ids=["c8f88563-dc60-47f3-aca3-af150065d951"],
        )
        assert_matches_type(ContractResult, company_contract, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Pymews) -> None:
        company_contract = client.api.connector.v1.company_contracts.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            service_ids=["c8f88563-dc60-47f3-aca3-af150065d951"],
            company_contract_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            company_ids=["bfd5667b-533f-424f-860d-af150065f4d6"],
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            updated_utc={
                "end_utc": parse_datetime("2023-10-31T00:00:00Z"),
                "start_utc": parse_datetime("2023-10-01T00:00:00Z"),
            },
        )
        assert_matches_type(ContractResult, company_contract, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Pymews) -> None:
        response = client.api.connector.v1.company_contracts.with_raw_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            service_ids=["c8f88563-dc60-47f3-aca3-af150065d951"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company_contract = response.parse()
        assert_matches_type(ContractResult, company_contract, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Pymews) -> None:
        with client.api.connector.v1.company_contracts.with_streaming_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            service_ids=["c8f88563-dc60-47f3-aca3-af150065d951"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company_contract = response.parse()
            assert_matches_type(ContractResult, company_contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Pymews) -> None:
        company_contract = client.api.connector.v1.company_contracts.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            service_ids=["a1d6dee8-355b-44c3-b6be-faef1a7eb6c0", "d5a2aac3-5194-479b-ba05-6c073398e0fd"],
            travel_agency_contract_ids=["0078f370-3787-43dc-a615-af150066bb88", "652d4a22-ac33-42b7-abe7-af1f00820023"],
        )
        assert_matches_type(object, company_contract, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_delete_with_all_params(self, client: Pymews) -> None:
        company_contract = client.api.connector.v1.company_contracts.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            service_ids=["a1d6dee8-355b-44c3-b6be-faef1a7eb6c0", "d5a2aac3-5194-479b-ba05-6c073398e0fd"],
            travel_agency_contract_ids=["0078f370-3787-43dc-a615-af150066bb88", "652d4a22-ac33-42b7-abe7-af1f00820023"],
            enterprise_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, company_contract, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Pymews) -> None:
        response = client.api.connector.v1.company_contracts.with_raw_response.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            service_ids=["a1d6dee8-355b-44c3-b6be-faef1a7eb6c0", "d5a2aac3-5194-479b-ba05-6c073398e0fd"],
            travel_agency_contract_ids=["0078f370-3787-43dc-a615-af150066bb88", "652d4a22-ac33-42b7-abe7-af1f00820023"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company_contract = response.parse()
        assert_matches_type(object, company_contract, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Pymews) -> None:
        with client.api.connector.v1.company_contracts.with_streaming_response.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            service_ids=["a1d6dee8-355b-44c3-b6be-faef1a7eb6c0", "d5a2aac3-5194-479b-ba05-6c073398e0fd"],
            travel_agency_contract_ids=["0078f370-3787-43dc-a615-af150066bb88", "652d4a22-ac33-42b7-abe7-af1f00820023"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company_contract = response.parse()
            assert_matches_type(object, company_contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_add(self, client: Pymews) -> None:
        company_contract = client.api.connector.v1.company_contracts.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            travel_agency_contracts=[
                {
                    "company_id": "896e9313-477d-4306-9d37-af150065f4d6",
                    "service_id": "c8f88563-dc60-47f3-aca3-af150065d951",
                }
            ],
        )
        assert_matches_type(ContractResult, company_contract, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_add(self, client: Pymews) -> None:
        response = client.api.connector.v1.company_contracts.with_raw_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            travel_agency_contracts=[
                {
                    "company_id": "896e9313-477d-4306-9d37-af150065f4d6",
                    "service_id": "c8f88563-dc60-47f3-aca3-af150065d951",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company_contract = response.parse()
        assert_matches_type(ContractResult, company_contract, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_add(self, client: Pymews) -> None:
        with client.api.connector.v1.company_contracts.with_streaming_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            travel_agency_contracts=[
                {
                    "company_id": "896e9313-477d-4306-9d37-af150065f4d6",
                    "service_id": "c8f88563-dc60-47f3-aca3-af150065d951",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company_contract = response.parse()
            assert_matches_type(ContractResult, company_contract, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCompanyContracts:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncPymews) -> None:
        company_contract = await async_client.api.connector.v1.company_contracts.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            travel_agency_contract_updates=[{"travel_agency_contract_id": "652d4a22-ac33-42b7-abe7-af1f00820023"}],
        )
        assert_matches_type(ContractResult, company_contract, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.company_contracts.with_raw_response.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            travel_agency_contract_updates=[{"travel_agency_contract_id": "652d4a22-ac33-42b7-abe7-af1f00820023"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company_contract = await response.parse()
        assert_matches_type(ContractResult, company_contract, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.company_contracts.with_streaming_response.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            travel_agency_contract_updates=[{"travel_agency_contract_id": "652d4a22-ac33-42b7-abe7-af1f00820023"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company_contract = await response.parse()
            assert_matches_type(ContractResult, company_contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncPymews) -> None:
        company_contract = await async_client.api.connector.v1.company_contracts.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            service_ids=["c8f88563-dc60-47f3-aca3-af150065d951"],
        )
        assert_matches_type(ContractResult, company_contract, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPymews) -> None:
        company_contract = await async_client.api.connector.v1.company_contracts.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            service_ids=["c8f88563-dc60-47f3-aca3-af150065d951"],
            company_contract_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            company_ids=["bfd5667b-533f-424f-860d-af150065f4d6"],
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            updated_utc={
                "end_utc": parse_datetime("2023-10-31T00:00:00Z"),
                "start_utc": parse_datetime("2023-10-01T00:00:00Z"),
            },
        )
        assert_matches_type(ContractResult, company_contract, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.company_contracts.with_raw_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            service_ids=["c8f88563-dc60-47f3-aca3-af150065d951"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company_contract = await response.parse()
        assert_matches_type(ContractResult, company_contract, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.company_contracts.with_streaming_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            service_ids=["c8f88563-dc60-47f3-aca3-af150065d951"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company_contract = await response.parse()
            assert_matches_type(ContractResult, company_contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncPymews) -> None:
        company_contract = await async_client.api.connector.v1.company_contracts.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            service_ids=["a1d6dee8-355b-44c3-b6be-faef1a7eb6c0", "d5a2aac3-5194-479b-ba05-6c073398e0fd"],
            travel_agency_contract_ids=["0078f370-3787-43dc-a615-af150066bb88", "652d4a22-ac33-42b7-abe7-af1f00820023"],
        )
        assert_matches_type(object, company_contract, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncPymews) -> None:
        company_contract = await async_client.api.connector.v1.company_contracts.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            service_ids=["a1d6dee8-355b-44c3-b6be-faef1a7eb6c0", "d5a2aac3-5194-479b-ba05-6c073398e0fd"],
            travel_agency_contract_ids=["0078f370-3787-43dc-a615-af150066bb88", "652d4a22-ac33-42b7-abe7-af1f00820023"],
            enterprise_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, company_contract, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.company_contracts.with_raw_response.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            service_ids=["a1d6dee8-355b-44c3-b6be-faef1a7eb6c0", "d5a2aac3-5194-479b-ba05-6c073398e0fd"],
            travel_agency_contract_ids=["0078f370-3787-43dc-a615-af150066bb88", "652d4a22-ac33-42b7-abe7-af1f00820023"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company_contract = await response.parse()
        assert_matches_type(object, company_contract, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.company_contracts.with_streaming_response.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            service_ids=["a1d6dee8-355b-44c3-b6be-faef1a7eb6c0", "d5a2aac3-5194-479b-ba05-6c073398e0fd"],
            travel_agency_contract_ids=["0078f370-3787-43dc-a615-af150066bb88", "652d4a22-ac33-42b7-abe7-af1f00820023"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company_contract = await response.parse()
            assert_matches_type(object, company_contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_add(self, async_client: AsyncPymews) -> None:
        company_contract = await async_client.api.connector.v1.company_contracts.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            travel_agency_contracts=[
                {
                    "company_id": "896e9313-477d-4306-9d37-af150065f4d6",
                    "service_id": "c8f88563-dc60-47f3-aca3-af150065d951",
                }
            ],
        )
        assert_matches_type(ContractResult, company_contract, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.company_contracts.with_raw_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            travel_agency_contracts=[
                {
                    "company_id": "896e9313-477d-4306-9d37-af150065f4d6",
                    "service_id": "c8f88563-dc60-47f3-aca3-af150065d951",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company_contract = await response.parse()
        assert_matches_type(ContractResult, company_contract, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.company_contracts.with_streaming_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            travel_agency_contracts=[
                {
                    "company_id": "896e9313-477d-4306-9d37-af150065f4d6",
                    "service_id": "c8f88563-dc60-47f3-aca3-af150065d951",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company_contract = await response.parse()
            assert_matches_type(ContractResult, company_contract, path=["response"])

        assert cast(Any, response.is_closed) is True
