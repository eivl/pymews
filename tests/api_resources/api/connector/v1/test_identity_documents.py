# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pymews import Pymews, AsyncPymews
from tests.utils import assert_matches_type
from pymews._utils import parse_date
from pymews.types.api.connector.v1 import (
    IdentityDocumentWriteResult,
    IdentityDocumentListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIdentityDocuments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Pymews) -> None:
        identity_document = client.api.connector.v1.identity_documents.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            identity_documents=[{"id": "e8a72a69-c20b-4278-b699-ab0400a32ecc"}],
        )
        assert_matches_type(IdentityDocumentWriteResult, identity_document, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Pymews) -> None:
        identity_document = client.api.connector.v1.identity_documents.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            identity_documents=[
                {
                    "id": "e8a72a69-c20b-4278-b699-ab0400a32ecc",
                    "expiration_date": {"value": "2040-11-20T00:00:00Z"},
                    "identity_document_support_number": {"value": "S-123456"},
                    "issuance_date": {"value": "2020-11-20T00:00:00Z"},
                    "issuing_city": {"value": "Prague"},
                    "issuing_country_code": {"value": "CZ"},
                    "number": {"value": "123456789"},
                    "type": {"value": "IdentityCard"},
                }
            ],
            chain_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )
        assert_matches_type(IdentityDocumentWriteResult, identity_document, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Pymews) -> None:
        response = client.api.connector.v1.identity_documents.with_raw_response.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            identity_documents=[{"id": "e8a72a69-c20b-4278-b699-ab0400a32ecc"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_document = response.parse()
        assert_matches_type(IdentityDocumentWriteResult, identity_document, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Pymews) -> None:
        with client.api.connector.v1.identity_documents.with_streaming_response.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            identity_documents=[{"id": "e8a72a69-c20b-4278-b699-ab0400a32ecc"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_document = response.parse()
            assert_matches_type(IdentityDocumentWriteResult, identity_document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Pymews) -> None:
        identity_document = client.api.connector.v1.identity_documents.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_ids=["fadd5bb6-b428-45d5-94f8-fd0d89fece6d", "bccdafd1-3e44-439d-861f-341526b597a9"],
            limitation={"count": 0},
        )
        assert_matches_type(IdentityDocumentListResponse, identity_document, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Pymews) -> None:
        identity_document = client.api.connector.v1.identity_documents.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_ids=["fadd5bb6-b428-45d5-94f8-fd0d89fece6d", "bccdafd1-3e44-439d-861f-341526b597a9"],
            limitation={
                "count": 0,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            chain_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "5fcd1933-22f2-40b9-84da-7db04cbecec2"],
            identity_document_ids=["e8a72a69-c20b-4278-b699-ab0400a32ecc", "24a3f051-49ed-411b-9384-78187f9daae6"],
            types=["IdentityCard"],
        )
        assert_matches_type(IdentityDocumentListResponse, identity_document, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Pymews) -> None:
        response = client.api.connector.v1.identity_documents.with_raw_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_ids=["fadd5bb6-b428-45d5-94f8-fd0d89fece6d", "bccdafd1-3e44-439d-861f-341526b597a9"],
            limitation={"count": 0},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_document = response.parse()
        assert_matches_type(IdentityDocumentListResponse, identity_document, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Pymews) -> None:
        with client.api.connector.v1.identity_documents.with_streaming_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_ids=["fadd5bb6-b428-45d5-94f8-fd0d89fece6d", "bccdafd1-3e44-439d-861f-341526b597a9"],
            limitation={"count": 0},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_document = response.parse()
            assert_matches_type(IdentityDocumentListResponse, identity_document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Pymews) -> None:
        identity_document = client.api.connector.v1.identity_documents.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            identity_document_ids=["e8a72a69-c20b-4278-b699-ab0400a32ecc", "2e1c6096-3a28-411d-a375-150a7350b278"],
        )
        assert_matches_type(object, identity_document, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_delete_with_all_params(self, client: Pymews) -> None:
        identity_document = client.api.connector.v1.identity_documents.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            identity_document_ids=["e8a72a69-c20b-4278-b699-ab0400a32ecc", "2e1c6096-3a28-411d-a375-150a7350b278"],
            chain_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )
        assert_matches_type(object, identity_document, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Pymews) -> None:
        response = client.api.connector.v1.identity_documents.with_raw_response.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            identity_document_ids=["e8a72a69-c20b-4278-b699-ab0400a32ecc", "2e1c6096-3a28-411d-a375-150a7350b278"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_document = response.parse()
        assert_matches_type(object, identity_document, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Pymews) -> None:
        with client.api.connector.v1.identity_documents.with_streaming_response.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            identity_document_ids=["e8a72a69-c20b-4278-b699-ab0400a32ecc", "2e1c6096-3a28-411d-a375-150a7350b278"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_document = response.parse()
            assert_matches_type(object, identity_document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_add(self, client: Pymews) -> None:
        identity_document = client.api.connector.v1.identity_documents.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            identity_documents=[
                {
                    "customer_id": "e8a72a69-c20b-4278-b699-ab0400a32ecc",
                    "number": "123456789",
                    "type": "IdentityCard",
                }
            ],
        )
        assert_matches_type(IdentityDocumentWriteResult, identity_document, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_add_with_all_params(self, client: Pymews) -> None:
        identity_document = client.api.connector.v1.identity_documents.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            identity_documents=[
                {
                    "customer_id": "e8a72a69-c20b-4278-b699-ab0400a32ecc",
                    "number": "123456789",
                    "type": "IdentityCard",
                    "expiration_date": parse_date("2019-12-27"),
                    "identity_document_support_number": "S-123456",
                    "issuance_date": parse_date("2019-12-27"),
                    "issuing_city": "Prague",
                    "issuing_country_code": "CZ",
                }
            ],
            chain_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )
        assert_matches_type(IdentityDocumentWriteResult, identity_document, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_add(self, client: Pymews) -> None:
        response = client.api.connector.v1.identity_documents.with_raw_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            identity_documents=[
                {
                    "customer_id": "e8a72a69-c20b-4278-b699-ab0400a32ecc",
                    "number": "123456789",
                    "type": "IdentityCard",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_document = response.parse()
        assert_matches_type(IdentityDocumentWriteResult, identity_document, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_add(self, client: Pymews) -> None:
        with client.api.connector.v1.identity_documents.with_streaming_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            identity_documents=[
                {
                    "customer_id": "e8a72a69-c20b-4278-b699-ab0400a32ecc",
                    "number": "123456789",
                    "type": "IdentityCard",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_document = response.parse()
            assert_matches_type(IdentityDocumentWriteResult, identity_document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_clear(self, client: Pymews) -> None:
        identity_document = client.api.connector.v1.identity_documents.clear(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_ids=["fadd5bb6-b428-45d5-94f8-fd0d89fece6d", "bccdafd1-3e44-439d-861f-341526b597a9"],
        )
        assert_matches_type(object, identity_document, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_clear_with_all_params(self, client: Pymews) -> None:
        identity_document = client.api.connector.v1.identity_documents.clear(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_ids=["fadd5bb6-b428-45d5-94f8-fd0d89fece6d", "bccdafd1-3e44-439d-861f-341526b597a9"],
            chain_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )
        assert_matches_type(object, identity_document, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_clear(self, client: Pymews) -> None:
        response = client.api.connector.v1.identity_documents.with_raw_response.clear(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_ids=["fadd5bb6-b428-45d5-94f8-fd0d89fece6d", "bccdafd1-3e44-439d-861f-341526b597a9"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_document = response.parse()
        assert_matches_type(object, identity_document, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_clear(self, client: Pymews) -> None:
        with client.api.connector.v1.identity_documents.with_streaming_response.clear(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_ids=["fadd5bb6-b428-45d5-94f8-fd0d89fece6d", "bccdafd1-3e44-439d-861f-341526b597a9"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_document = response.parse()
            assert_matches_type(object, identity_document, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncIdentityDocuments:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncPymews) -> None:
        identity_document = await async_client.api.connector.v1.identity_documents.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            identity_documents=[{"id": "e8a72a69-c20b-4278-b699-ab0400a32ecc"}],
        )
        assert_matches_type(IdentityDocumentWriteResult, identity_document, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncPymews) -> None:
        identity_document = await async_client.api.connector.v1.identity_documents.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            identity_documents=[
                {
                    "id": "e8a72a69-c20b-4278-b699-ab0400a32ecc",
                    "expiration_date": {"value": "2040-11-20T00:00:00Z"},
                    "identity_document_support_number": {"value": "S-123456"},
                    "issuance_date": {"value": "2020-11-20T00:00:00Z"},
                    "issuing_city": {"value": "Prague"},
                    "issuing_country_code": {"value": "CZ"},
                    "number": {"value": "123456789"},
                    "type": {"value": "IdentityCard"},
                }
            ],
            chain_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )
        assert_matches_type(IdentityDocumentWriteResult, identity_document, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.identity_documents.with_raw_response.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            identity_documents=[{"id": "e8a72a69-c20b-4278-b699-ab0400a32ecc"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_document = await response.parse()
        assert_matches_type(IdentityDocumentWriteResult, identity_document, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.identity_documents.with_streaming_response.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            identity_documents=[{"id": "e8a72a69-c20b-4278-b699-ab0400a32ecc"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_document = await response.parse()
            assert_matches_type(IdentityDocumentWriteResult, identity_document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncPymews) -> None:
        identity_document = await async_client.api.connector.v1.identity_documents.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_ids=["fadd5bb6-b428-45d5-94f8-fd0d89fece6d", "bccdafd1-3e44-439d-861f-341526b597a9"],
            limitation={"count": 0},
        )
        assert_matches_type(IdentityDocumentListResponse, identity_document, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPymews) -> None:
        identity_document = await async_client.api.connector.v1.identity_documents.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_ids=["fadd5bb6-b428-45d5-94f8-fd0d89fece6d", "bccdafd1-3e44-439d-861f-341526b597a9"],
            limitation={
                "count": 0,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            chain_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "5fcd1933-22f2-40b9-84da-7db04cbecec2"],
            identity_document_ids=["e8a72a69-c20b-4278-b699-ab0400a32ecc", "24a3f051-49ed-411b-9384-78187f9daae6"],
            types=["IdentityCard"],
        )
        assert_matches_type(IdentityDocumentListResponse, identity_document, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.identity_documents.with_raw_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_ids=["fadd5bb6-b428-45d5-94f8-fd0d89fece6d", "bccdafd1-3e44-439d-861f-341526b597a9"],
            limitation={"count": 0},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_document = await response.parse()
        assert_matches_type(IdentityDocumentListResponse, identity_document, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.identity_documents.with_streaming_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_ids=["fadd5bb6-b428-45d5-94f8-fd0d89fece6d", "bccdafd1-3e44-439d-861f-341526b597a9"],
            limitation={"count": 0},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_document = await response.parse()
            assert_matches_type(IdentityDocumentListResponse, identity_document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncPymews) -> None:
        identity_document = await async_client.api.connector.v1.identity_documents.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            identity_document_ids=["e8a72a69-c20b-4278-b699-ab0400a32ecc", "2e1c6096-3a28-411d-a375-150a7350b278"],
        )
        assert_matches_type(object, identity_document, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncPymews) -> None:
        identity_document = await async_client.api.connector.v1.identity_documents.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            identity_document_ids=["e8a72a69-c20b-4278-b699-ab0400a32ecc", "2e1c6096-3a28-411d-a375-150a7350b278"],
            chain_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )
        assert_matches_type(object, identity_document, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.identity_documents.with_raw_response.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            identity_document_ids=["e8a72a69-c20b-4278-b699-ab0400a32ecc", "2e1c6096-3a28-411d-a375-150a7350b278"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_document = await response.parse()
        assert_matches_type(object, identity_document, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.identity_documents.with_streaming_response.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            identity_document_ids=["e8a72a69-c20b-4278-b699-ab0400a32ecc", "2e1c6096-3a28-411d-a375-150a7350b278"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_document = await response.parse()
            assert_matches_type(object, identity_document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_add(self, async_client: AsyncPymews) -> None:
        identity_document = await async_client.api.connector.v1.identity_documents.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            identity_documents=[
                {
                    "customer_id": "e8a72a69-c20b-4278-b699-ab0400a32ecc",
                    "number": "123456789",
                    "type": "IdentityCard",
                }
            ],
        )
        assert_matches_type(IdentityDocumentWriteResult, identity_document, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_add_with_all_params(self, async_client: AsyncPymews) -> None:
        identity_document = await async_client.api.connector.v1.identity_documents.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            identity_documents=[
                {
                    "customer_id": "e8a72a69-c20b-4278-b699-ab0400a32ecc",
                    "number": "123456789",
                    "type": "IdentityCard",
                    "expiration_date": parse_date("2019-12-27"),
                    "identity_document_support_number": "S-123456",
                    "issuance_date": parse_date("2019-12-27"),
                    "issuing_city": "Prague",
                    "issuing_country_code": "CZ",
                }
            ],
            chain_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )
        assert_matches_type(IdentityDocumentWriteResult, identity_document, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.identity_documents.with_raw_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            identity_documents=[
                {
                    "customer_id": "e8a72a69-c20b-4278-b699-ab0400a32ecc",
                    "number": "123456789",
                    "type": "IdentityCard",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_document = await response.parse()
        assert_matches_type(IdentityDocumentWriteResult, identity_document, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.identity_documents.with_streaming_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            identity_documents=[
                {
                    "customer_id": "e8a72a69-c20b-4278-b699-ab0400a32ecc",
                    "number": "123456789",
                    "type": "IdentityCard",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_document = await response.parse()
            assert_matches_type(IdentityDocumentWriteResult, identity_document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_clear(self, async_client: AsyncPymews) -> None:
        identity_document = await async_client.api.connector.v1.identity_documents.clear(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_ids=["fadd5bb6-b428-45d5-94f8-fd0d89fece6d", "bccdafd1-3e44-439d-861f-341526b597a9"],
        )
        assert_matches_type(object, identity_document, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_clear_with_all_params(self, async_client: AsyncPymews) -> None:
        identity_document = await async_client.api.connector.v1.identity_documents.clear(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_ids=["fadd5bb6-b428-45d5-94f8-fd0d89fece6d", "bccdafd1-3e44-439d-861f-341526b597a9"],
            chain_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )
        assert_matches_type(object, identity_document, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_clear(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.identity_documents.with_raw_response.clear(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_ids=["fadd5bb6-b428-45d5-94f8-fd0d89fece6d", "bccdafd1-3e44-439d-861f-341526b597a9"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_document = await response.parse()
        assert_matches_type(object, identity_document, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_clear(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.identity_documents.with_streaming_response.clear(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_ids=["fadd5bb6-b428-45d5-94f8-fd0d89fece6d", "bccdafd1-3e44-439d-861f-341526b597a9"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_document = await response.parse()
            assert_matches_type(object, identity_document, path=["response"])

        assert cast(Any, response.is_closed) is True
