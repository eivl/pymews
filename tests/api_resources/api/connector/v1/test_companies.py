# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pymews import Pymews, AsyncPymews
from tests.utils import assert_matches_type
from pymews._utils import parse_datetime
from pymews.types.api.connector.v1 import (
    CompanyResult,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCompanies:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Pymews) -> None:
        company = client.api.connector.v1.companies.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            company_id="7a1e4d67-d6a2-4a4c-a464-ab1100bea786",
        )
        assert_matches_type(CompanyResult, company, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Pymews) -> None:
        company = client.api.connector.v1.companies.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            company_id="7a1e4d67-d6a2-4a4c-a464-ab1100bea786",
            accounting_code={"value": "Value"},
            additional_tax_identifier={"value": "Value"},
            billing_code={"value": "Value"},
            chain_id="1df21f06-0cfc-4960-9c58-a3bf1261663e",
            contact={"value": "John Snow"},
            contact_person={"value": "John Snow"},
            credit_rating={"basic": {"value": "CreditOk"}},
            department={"value": "Marketing"},
            duns_number={"value": "123456789"},
            external_identifier={"value": "4321"},
            iata={"value": "PAO"},
            identifier={"value": "Value"},
            invoice_due_interval={"value": "P2DT23H"},
            invoicing_email={"value": "Value"},
            mother_company_id={"value": "ff649bce-0c4b-4395-9cdd-02039acb7cb3"},
            name={"value": "Sample company name"},
            notes={"value": "Notes"},
            options={
                "add_fees_to_invoices": {"value": False},
                "add_tax_deducted_payment_to_invoices": {"value": True},
                "invoiceable": {"value": True},
            },
            reference_identifier={"value": "ff64395-9cdd-4395-9cdd-02039acb7cb3"},
            tax_identifier={"value": "Value"},
            telephone={"value": "Value"},
            website_url={"value": "https://www.mews.com"},
        )
        assert_matches_type(CompanyResult, company, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Pymews) -> None:
        response = client.api.connector.v1.companies.with_raw_response.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            company_id="7a1e4d67-d6a2-4a4c-a464-ab1100bea786",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = response.parse()
        assert_matches_type(CompanyResult, company, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Pymews) -> None:
        with client.api.connector.v1.companies.with_streaming_response.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            company_id="7a1e4d67-d6a2-4a4c-a464-ab1100bea786",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = response.parse()
            assert_matches_type(CompanyResult, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Pymews) -> None:
        company = client.api.connector.v1.companies.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )
        assert_matches_type(CompanyResult, company, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Pymews) -> None:
        company = client.api.connector.v1.companies.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            activity_states=["Deleted"],
            chain_ids=["1df21f06-0cfc-4960-9c58-a3bf1261663e", "5fcd1933-22f2-40b9-84da-7db04cbecec2"],
            created_utc={
                "end_utc": parse_datetime("2019-12-10T00:00:00Z"),
                "start_utc": parse_datetime("2019-12-05T00:00:00Z"),
            },
            end_utc=parse_datetime("2019-12-27T18:11:19.117Z"),
            external_identifiers=["12345", "4312343"],
            ids=["3ed9e2f3-4bba-4df6-8d41-ab1b009b6425", "8a98965a-7c03-48a1-a28c-ab1b009b53c8"],
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            mother_company_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            names=["AC Company"],
            start_utc=parse_datetime("2019-12-27T18:11:19.117Z"),
            time_filter="Created",
            updated_utc={
                "end_utc": parse_datetime("2019-12-17T00:00:00Z"),
                "start_utc": parse_datetime("2019-12-10T00:00:00Z"),
            },
        )
        assert_matches_type(CompanyResult, company, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Pymews) -> None:
        response = client.api.connector.v1.companies.with_raw_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = response.parse()
        assert_matches_type(CompanyResult, company, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Pymews) -> None:
        with client.api.connector.v1.companies.with_streaming_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = response.parse()
            assert_matches_type(CompanyResult, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Pymews) -> None:
        company = client.api.connector.v1.companies.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            company_ids=["eb02cbff-353d-48ec-97da-7def2305a5c5", "63551515-1740-49b3-914e-309a8b1429f0"],
        )
        assert_matches_type(object, company, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_delete_with_all_params(self, client: Pymews) -> None:
        company = client.api.connector.v1.companies.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            company_ids=["eb02cbff-353d-48ec-97da-7def2305a5c5", "63551515-1740-49b3-914e-309a8b1429f0"],
            chain_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, company, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Pymews) -> None:
        response = client.api.connector.v1.companies.with_raw_response.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            company_ids=["eb02cbff-353d-48ec-97da-7def2305a5c5", "63551515-1740-49b3-914e-309a8b1429f0"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = response.parse()
        assert_matches_type(object, company, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Pymews) -> None:
        with client.api.connector.v1.companies.with_streaming_response.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            company_ids=["eb02cbff-353d-48ec-97da-7def2305a5c5", "63551515-1740-49b3-914e-309a8b1429f0"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = response.parse()
            assert_matches_type(object, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_add(self, client: Pymews) -> None:
        company = client.api.connector.v1.companies.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            name="Mews",
            options={},
        )
        assert_matches_type(CompanyResult, company, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_add_with_all_params(self, client: Pymews) -> None:
        company = client.api.connector.v1.companies.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            name="Mews",
            options={
                "add_fees_to_invoices": True,
                "add_tax_deducted_payment_to_invoices": True,
                "invoiceable": True,
            },
            accounting_code=None,
            additional_tax_identifier=None,
            address={
                "city": "City",
                "country_code": "CountryCode",
                "country_subdivision_code": "CountrySubdivisionCode",
                "line1": "Line1",
                "line2": "Line2",
                "postal_code": "PostalCode",
            },
            billing_code=None,
            chain_id="1df21f06-0cfc-4960-9c58-a3bf1261663e",
            contact="ContactInfo",
            contact_person="ContactPerson",
            credit_rating={"basic": "CreditOk"},
            department="Sales",
            duns_number="987654321",
            external_identifier="1234",
            iata="PAO",
            identifier=None,
            invoice_due_interval="P2DT23H",
            invoicing_email="dev@stainlessapi.com",
            mother_company_id=None,
            notes="Note1",
            reference_identifier="a58ff7cb-77e3-495a-bd61-aecf00a3f19d",
            tax_identifier=None,
            telephone="111-222-333",
            website_url="https://www.mews.com",
        )
        assert_matches_type(CompanyResult, company, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_add(self, client: Pymews) -> None:
        response = client.api.connector.v1.companies.with_raw_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            name="Mews",
            options={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = response.parse()
        assert_matches_type(CompanyResult, company, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_add(self, client: Pymews) -> None:
        with client.api.connector.v1.companies.with_streaming_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            name="Mews",
            options={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = response.parse()
            assert_matches_type(CompanyResult, company, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCompanies:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncPymews) -> None:
        company = await async_client.api.connector.v1.companies.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            company_id="7a1e4d67-d6a2-4a4c-a464-ab1100bea786",
        )
        assert_matches_type(CompanyResult, company, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncPymews) -> None:
        company = await async_client.api.connector.v1.companies.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            company_id="7a1e4d67-d6a2-4a4c-a464-ab1100bea786",
            accounting_code={"value": "Value"},
            additional_tax_identifier={"value": "Value"},
            billing_code={"value": "Value"},
            chain_id="1df21f06-0cfc-4960-9c58-a3bf1261663e",
            contact={"value": "John Snow"},
            contact_person={"value": "John Snow"},
            credit_rating={"basic": {"value": "CreditOk"}},
            department={"value": "Marketing"},
            duns_number={"value": "123456789"},
            external_identifier={"value": "4321"},
            iata={"value": "PAO"},
            identifier={"value": "Value"},
            invoice_due_interval={"value": "P2DT23H"},
            invoicing_email={"value": "Value"},
            mother_company_id={"value": "ff649bce-0c4b-4395-9cdd-02039acb7cb3"},
            name={"value": "Sample company name"},
            notes={"value": "Notes"},
            options={
                "add_fees_to_invoices": {"value": False},
                "add_tax_deducted_payment_to_invoices": {"value": True},
                "invoiceable": {"value": True},
            },
            reference_identifier={"value": "ff64395-9cdd-4395-9cdd-02039acb7cb3"},
            tax_identifier={"value": "Value"},
            telephone={"value": "Value"},
            website_url={"value": "https://www.mews.com"},
        )
        assert_matches_type(CompanyResult, company, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.companies.with_raw_response.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            company_id="7a1e4d67-d6a2-4a4c-a464-ab1100bea786",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = await response.parse()
        assert_matches_type(CompanyResult, company, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.companies.with_streaming_response.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            company_id="7a1e4d67-d6a2-4a4c-a464-ab1100bea786",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = await response.parse()
            assert_matches_type(CompanyResult, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncPymews) -> None:
        company = await async_client.api.connector.v1.companies.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )
        assert_matches_type(CompanyResult, company, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPymews) -> None:
        company = await async_client.api.connector.v1.companies.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            activity_states=["Deleted"],
            chain_ids=["1df21f06-0cfc-4960-9c58-a3bf1261663e", "5fcd1933-22f2-40b9-84da-7db04cbecec2"],
            created_utc={
                "end_utc": parse_datetime("2019-12-10T00:00:00Z"),
                "start_utc": parse_datetime("2019-12-05T00:00:00Z"),
            },
            end_utc=parse_datetime("2019-12-27T18:11:19.117Z"),
            external_identifiers=["12345", "4312343"],
            ids=["3ed9e2f3-4bba-4df6-8d41-ab1b009b6425", "8a98965a-7c03-48a1-a28c-ab1b009b53c8"],
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            mother_company_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            names=["AC Company"],
            start_utc=parse_datetime("2019-12-27T18:11:19.117Z"),
            time_filter="Created",
            updated_utc={
                "end_utc": parse_datetime("2019-12-17T00:00:00Z"),
                "start_utc": parse_datetime("2019-12-10T00:00:00Z"),
            },
        )
        assert_matches_type(CompanyResult, company, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.companies.with_raw_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = await response.parse()
        assert_matches_type(CompanyResult, company, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.companies.with_streaming_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = await response.parse()
            assert_matches_type(CompanyResult, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncPymews) -> None:
        company = await async_client.api.connector.v1.companies.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            company_ids=["eb02cbff-353d-48ec-97da-7def2305a5c5", "63551515-1740-49b3-914e-309a8b1429f0"],
        )
        assert_matches_type(object, company, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncPymews) -> None:
        company = await async_client.api.connector.v1.companies.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            company_ids=["eb02cbff-353d-48ec-97da-7def2305a5c5", "63551515-1740-49b3-914e-309a8b1429f0"],
            chain_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, company, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.companies.with_raw_response.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            company_ids=["eb02cbff-353d-48ec-97da-7def2305a5c5", "63551515-1740-49b3-914e-309a8b1429f0"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = await response.parse()
        assert_matches_type(object, company, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.companies.with_streaming_response.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            company_ids=["eb02cbff-353d-48ec-97da-7def2305a5c5", "63551515-1740-49b3-914e-309a8b1429f0"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = await response.parse()
            assert_matches_type(object, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_add(self, async_client: AsyncPymews) -> None:
        company = await async_client.api.connector.v1.companies.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            name="Mews",
            options={},
        )
        assert_matches_type(CompanyResult, company, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_add_with_all_params(self, async_client: AsyncPymews) -> None:
        company = await async_client.api.connector.v1.companies.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            name="Mews",
            options={
                "add_fees_to_invoices": True,
                "add_tax_deducted_payment_to_invoices": True,
                "invoiceable": True,
            },
            accounting_code=None,
            additional_tax_identifier=None,
            address={
                "city": "City",
                "country_code": "CountryCode",
                "country_subdivision_code": "CountrySubdivisionCode",
                "line1": "Line1",
                "line2": "Line2",
                "postal_code": "PostalCode",
            },
            billing_code=None,
            chain_id="1df21f06-0cfc-4960-9c58-a3bf1261663e",
            contact="ContactInfo",
            contact_person="ContactPerson",
            credit_rating={"basic": "CreditOk"},
            department="Sales",
            duns_number="987654321",
            external_identifier="1234",
            iata="PAO",
            identifier=None,
            invoice_due_interval="P2DT23H",
            invoicing_email="dev@stainlessapi.com",
            mother_company_id=None,
            notes="Note1",
            reference_identifier="a58ff7cb-77e3-495a-bd61-aecf00a3f19d",
            tax_identifier=None,
            telephone="111-222-333",
            website_url="https://www.mews.com",
        )
        assert_matches_type(CompanyResult, company, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.companies.with_raw_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            name="Mews",
            options={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = await response.parse()
        assert_matches_type(CompanyResult, company, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.companies.with_streaming_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            name="Mews",
            options={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = await response.parse()
            assert_matches_type(CompanyResult, company, path=["response"])

        assert cast(Any, response.is_closed) is True
