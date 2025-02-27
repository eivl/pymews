# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pymews import Pymews, AsyncPymews
from tests.utils import assert_matches_type
from pymews._utils import parse_date, parse_datetime
from pymews.types.api.connector.v1 import (
    Customer,
    CustomerListResponse,
    CustomerSearchResponse,
    CustomerAddFileResponse,
    CustomerGetOpenItemsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCustomers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Pymews) -> None:
        customer = client.api.connector.v1.customers.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_id="99b4f0af-9558-463b-8452-07a9bc414708",
        )
        assert_matches_type(Customer, customer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Pymews) -> None:
        customer = client.api.connector.v1.customers.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_id="99b4f0af-9558-463b-8452-07a9bc414708",
            address={
                "city": "Liborio laziale",
                "country_code": "IT",
                "country_subdivision_code": "IT-65",
                "line1": "Via Antimo 474 Piano 5",
                "line2": "Line2",
                "postal_code": "30228",
            },
            birth_date=parse_date("1985-09-30"),
            birth_place="Pescara (BI)",
            car_registration_number="AA 111AA",
            chain_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
            classifications=["PaymasterAccount", "Blacklist"],
            company_id="f3b4f0af-9558-463b-8452-07a9bc414708",
            dietary_requirements="DietaryRequirements",
            drivers_license={
                "expiration": parse_date("2019-12-27"),
                "issuance": parse_date("2019-12-27"),
                "issuing_city": "IssuingCity",
                "issuing_country_code": "IssuingCountryCode",
                "number": "Number",
            },
            email="thea@quotidiano.example",
            first_name="Thea",
            identity_card={
                "expiration": parse_date("2019-12-27"),
                "issuance": parse_date("2019-12-27"),
                "issuing_city": "IssuingCity",
                "issuing_country_code": "IssuingCountryCode",
                "number": "Number",
            },
            italian_destination_code={"value": "7654321"},
            italian_fiscal_code={"value": "ZGNZLR17U72P554F"},
            last_name="Carbone",
            loyalty_code="LoyaltyCode",
            nationality_code="NationalityCode",
            notes="Check-in notturno.",
            occupation="Giornalista",
            options=["SendMarketingEmails"],
            passport={
                "expiration": parse_date("2019-12-27"),
                "issuance": parse_date("2019-12-27"),
                "issuing_city": "IssuingCity",
                "issuing_country_code": "IssuingCountryCode",
                "number": "Number",
            },
            phone="+39 06 555 5555",
            second_last_name="SecondLastName",
            sex="Male",
            tax_identification_number="ZGNZLR17U72P554F",
            title="Mister",
            visa={
                "expiration": parse_date("2019-12-27"),
                "issuance": parse_date("2019-12-27"),
                "issuing_city": "IssuingCity",
                "issuing_country_code": "IssuingCountryCode",
                "number": "Number",
            },
        )
        assert_matches_type(Customer, customer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Pymews) -> None:
        response = client.api.connector.v1.customers.with_raw_response.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_id="99b4f0af-9558-463b-8452-07a9bc414708",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(Customer, customer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Pymews) -> None:
        with client.api.connector.v1.customers.with_streaming_response.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_id="99b4f0af-9558-463b-8452-07a9bc414708",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(Customer, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Pymews) -> None:
        customer = client.api.connector.v1.customers.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            extent={},
            limitation={"count": 10},
        )
        assert_matches_type(CustomerListResponse, customer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Pymews) -> None:
        customer = client.api.connector.v1.customers.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            extent={
                "addresses": False,
                "customers": True,
                "documents": False,
            },
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            activity_states=["Deleted"],
            chain_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "5fcd1933-22f2-40b9-84da-7db04cbecec2"],
            company_ids=["c6f5c82d-621a-4c8a-903b-1b0a9a23b71f"],
            created_utc={
                "end_utc": parse_datetime("2018-01-30T00:00:00Z"),
                "start_utc": parse_datetime("2018-01-01T00:00:00Z"),
            },
            customer_ids=["fadd5bb6-b428-45d5-94f8-fd0d89fece6d"],
            deleted_utc={
                "end_utc": parse_datetime("2019-12-27T18:11:19.117Z"),
                "start_utc": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            emails=["j.smith@example.com"],
            first_names=["John", "Jane"],
            last_names=["Doe", "Smith"],
            loyalty_codes=["LL810213"],
            updated_utc={
                "end_utc": parse_datetime("2018-01-30T00:00:00Z"),
                "start_utc": parse_datetime("2018-01-02T00:00:00Z"),
            },
        )
        assert_matches_type(CustomerListResponse, customer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Pymews) -> None:
        response = client.api.connector.v1.customers.with_raw_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            extent={},
            limitation={"count": 10},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(CustomerListResponse, customer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Pymews) -> None:
        with client.api.connector.v1.customers.with_streaming_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            extent={},
            limitation={"count": 10},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(CustomerListResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_add(self, client: Pymews) -> None:
        customer = client.api.connector.v1.customers.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            last_name="Carbone",
            overwrite_existing=False,
        )
        assert_matches_type(Customer, customer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_add_with_all_params(self, client: Pymews) -> None:
        customer = client.api.connector.v1.customers.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            last_name="Carbone",
            overwrite_existing=False,
            address={
                "city": "Liborio laziale",
                "country_code": "IT",
                "country_subdivision_code": "IT-65",
                "line1": "Via Antimo 474 Piano 5",
                "line2": "Line2",
                "postal_code": "30228",
            },
            birth_date=parse_date("1985-09-30"),
            birth_place="Pescara (BI)",
            car_registration_number="AA 111AA",
            chain_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
            classifications=["PaymasterAccount", "Blacklist"],
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dietary_requirements="DietaryRequirements",
            drivers_license={
                "expiration": parse_date("2019-12-27"),
                "issuance": parse_date("2019-12-27"),
                "issuing_city": "IssuingCity",
                "issuing_country_code": "IssuingCountryCode",
                "number": "Number",
            },
            email="thea@quotidiano.example",
            first_name="Thea",
            identity_card={
                "expiration": parse_date("2019-12-27"),
                "issuance": parse_date("2019-12-27"),
                "issuing_city": "IssuingCity",
                "issuing_country_code": "IssuingCountryCode",
                "number": "Number",
            },
            italian_destination_code="7654321",
            italian_fiscal_code="ZGNZLR17U72P554F",
            loyalty_code="LoyaltyCode",
            nationality_code="NationalityCode",
            notes="Check-in notturno.",
            occupation="Giornalista",
            options=["SendMarketingEmails"],
            passport={
                "expiration": parse_date("2019-12-27"),
                "issuance": parse_date("2019-12-27"),
                "issuing_city": "IssuingCity",
                "issuing_country_code": "IssuingCountryCode",
                "number": "Number",
            },
            phone="+39 06 555 5555",
            second_last_name="SecondLastName",
            sex="Male",
            tax_identification_number="ZGNZLR17U72P554F",
            title="Mister",
            visa={
                "expiration": parse_date("2019-12-27"),
                "issuance": parse_date("2019-12-27"),
                "issuing_city": "IssuingCity",
                "issuing_country_code": "IssuingCountryCode",
                "number": "Number",
            },
        )
        assert_matches_type(Customer, customer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_add(self, client: Pymews) -> None:
        response = client.api.connector.v1.customers.with_raw_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            last_name="Carbone",
            overwrite_existing=False,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(Customer, customer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_add(self, client: Pymews) -> None:
        with client.api.connector.v1.customers.with_streaming_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            last_name="Carbone",
            overwrite_existing=False,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(Customer, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_add_file(self, client: Pymews) -> None:
        customer = client.api.connector.v1.customers.add_file(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
            data="JVBERi0xLjAKMSAwIG9iajw8L1BhZ2VzIDIgMCBSPj5lbmRvYmogMiAwIG9iajw8L0tpZHNbMyAwIFJdL0NvdW50IDE+PmVuZG9iaiAzIDAgb2JqPDwvTWVkaWFCb3hbMCAwIDMgM10+PmVuZG9iagp0cmFpbGVyPDwvUm9vdCAxIDAgUj4+Cg==",
            name="document.pdf",
            type="application/pdf",
        )
        assert_matches_type(CustomerAddFileResponse, customer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_add_file_with_all_params(self, client: Pymews) -> None:
        customer = client.api.connector.v1.customers.add_file(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
            data="JVBERi0xLjAKMSAwIG9iajw8L1BhZ2VzIDIgMCBSPj5lbmRvYmogMiAwIG9iajw8L0tpZHNbMyAwIFJdL0NvdW50IDE+PmVuZG9iaiAzIDAgb2JqPDwvTWVkaWFCb3hbMCAwIDMgM10+PmVuZG9iagp0cmFpbGVyPDwvUm9vdCAxIDAgUj4+Cg==",
            name="document.pdf",
            type="application/pdf",
            chain_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )
        assert_matches_type(CustomerAddFileResponse, customer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_add_file(self, client: Pymews) -> None:
        response = client.api.connector.v1.customers.with_raw_response.add_file(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
            data="JVBERi0xLjAKMSAwIG9iajw8L1BhZ2VzIDIgMCBSPj5lbmRvYmogMiAwIG9iajw8L0tpZHNbMyAwIFJdL0NvdW50IDE+PmVuZG9iaiAzIDAgb2JqPDwvTWVkaWFCb3hbMCAwIDMgM10+PmVuZG9iagp0cmFpbGVyPDwvUm9vdCAxIDAgUj4+Cg==",
            name="document.pdf",
            type="application/pdf",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(CustomerAddFileResponse, customer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_add_file(self, client: Pymews) -> None:
        with client.api.connector.v1.customers.with_streaming_response.add_file(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
            data="JVBERi0xLjAKMSAwIG9iajw8L1BhZ2VzIDIgMCBSPj5lbmRvYmogMiAwIG9iajw8L0tpZHNbMyAwIFJdL0NvdW50IDE+PmVuZG9iaiAzIDAgb2JqPDwvTWVkaWFCb3hbMCAwIDMgM10+PmVuZG9iagp0cmFpbGVyPDwvUm9vdCAxIDAgUj4+Cg==",
            name="document.pdf",
            type="application/pdf",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(CustomerAddFileResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_open_items(self, client: Pymews) -> None:
        customer = client.api.connector.v1.customers.get_open_items(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_ids=["2a1a4315-7e6f-4131-af21-402cec59b8b9"],
        )
        assert_matches_type(CustomerGetOpenItemsResponse, customer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_open_items_with_all_params(self, client: Pymews) -> None:
        customer = client.api.connector.v1.customers.get_open_items(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_ids=["2a1a4315-7e6f-4131-af21-402cec59b8b9"],
            currency=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(CustomerGetOpenItemsResponse, customer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_open_items(self, client: Pymews) -> None:
        response = client.api.connector.v1.customers.with_raw_response.get_open_items(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_ids=["2a1a4315-7e6f-4131-af21-402cec59b8b9"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(CustomerGetOpenItemsResponse, customer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_open_items(self, client: Pymews) -> None:
        with client.api.connector.v1.customers.with_streaming_response.get_open_items(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_ids=["2a1a4315-7e6f-4131-af21-402cec59b8b9"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(CustomerGetOpenItemsResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_merge(self, client: Pymews) -> None:
        customer = client.api.connector.v1.customers.merge(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            source_customer_id="e11801ff-4148-4010-87f3-0d111e2893e3",
            target_customer_id="35d4b117-4e60-44a3-9580-c582117eff98",
        )
        assert_matches_type(object, customer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_merge(self, client: Pymews) -> None:
        response = client.api.connector.v1.customers.with_raw_response.merge(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            source_customer_id="e11801ff-4148-4010-87f3-0d111e2893e3",
            target_customer_id="35d4b117-4e60-44a3-9580-c582117eff98",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(object, customer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_merge(self, client: Pymews) -> None:
        with client.api.connector.v1.customers.with_streaming_response.merge(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            source_customer_id="e11801ff-4148-4010-87f3-0d111e2893e3",
            target_customer_id="35d4b117-4e60-44a3-9580-c582117eff98",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(object, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_search(self, client: Pymews) -> None:
        customer = client.api.connector.v1.customers.search(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )
        assert_matches_type(CustomerSearchResponse, customer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_search_with_all_params(self, client: Pymews) -> None:
        customer = client.api.connector.v1.customers.search(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            extent={
                "addresses": False,
                "customers": True,
                "documents": False,
            },
            name="Smith",
            resource_id=None,
        )
        assert_matches_type(CustomerSearchResponse, customer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_search(self, client: Pymews) -> None:
        response = client.api.connector.v1.customers.with_raw_response.search(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(CustomerSearchResponse, customer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_search(self, client: Pymews) -> None:
        with client.api.connector.v1.customers.with_streaming_response.search(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(CustomerSearchResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCustomers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncPymews) -> None:
        customer = await async_client.api.connector.v1.customers.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_id="99b4f0af-9558-463b-8452-07a9bc414708",
        )
        assert_matches_type(Customer, customer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncPymews) -> None:
        customer = await async_client.api.connector.v1.customers.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_id="99b4f0af-9558-463b-8452-07a9bc414708",
            address={
                "city": "Liborio laziale",
                "country_code": "IT",
                "country_subdivision_code": "IT-65",
                "line1": "Via Antimo 474 Piano 5",
                "line2": "Line2",
                "postal_code": "30228",
            },
            birth_date=parse_date("1985-09-30"),
            birth_place="Pescara (BI)",
            car_registration_number="AA 111AA",
            chain_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
            classifications=["PaymasterAccount", "Blacklist"],
            company_id="f3b4f0af-9558-463b-8452-07a9bc414708",
            dietary_requirements="DietaryRequirements",
            drivers_license={
                "expiration": parse_date("2019-12-27"),
                "issuance": parse_date("2019-12-27"),
                "issuing_city": "IssuingCity",
                "issuing_country_code": "IssuingCountryCode",
                "number": "Number",
            },
            email="thea@quotidiano.example",
            first_name="Thea",
            identity_card={
                "expiration": parse_date("2019-12-27"),
                "issuance": parse_date("2019-12-27"),
                "issuing_city": "IssuingCity",
                "issuing_country_code": "IssuingCountryCode",
                "number": "Number",
            },
            italian_destination_code={"value": "7654321"},
            italian_fiscal_code={"value": "ZGNZLR17U72P554F"},
            last_name="Carbone",
            loyalty_code="LoyaltyCode",
            nationality_code="NationalityCode",
            notes="Check-in notturno.",
            occupation="Giornalista",
            options=["SendMarketingEmails"],
            passport={
                "expiration": parse_date("2019-12-27"),
                "issuance": parse_date("2019-12-27"),
                "issuing_city": "IssuingCity",
                "issuing_country_code": "IssuingCountryCode",
                "number": "Number",
            },
            phone="+39 06 555 5555",
            second_last_name="SecondLastName",
            sex="Male",
            tax_identification_number="ZGNZLR17U72P554F",
            title="Mister",
            visa={
                "expiration": parse_date("2019-12-27"),
                "issuance": parse_date("2019-12-27"),
                "issuing_city": "IssuingCity",
                "issuing_country_code": "IssuingCountryCode",
                "number": "Number",
            },
        )
        assert_matches_type(Customer, customer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.customers.with_raw_response.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_id="99b4f0af-9558-463b-8452-07a9bc414708",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert_matches_type(Customer, customer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.customers.with_streaming_response.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_id="99b4f0af-9558-463b-8452-07a9bc414708",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(Customer, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncPymews) -> None:
        customer = await async_client.api.connector.v1.customers.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            extent={},
            limitation={"count": 10},
        )
        assert_matches_type(CustomerListResponse, customer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPymews) -> None:
        customer = await async_client.api.connector.v1.customers.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            extent={
                "addresses": False,
                "customers": True,
                "documents": False,
            },
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            activity_states=["Deleted"],
            chain_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "5fcd1933-22f2-40b9-84da-7db04cbecec2"],
            company_ids=["c6f5c82d-621a-4c8a-903b-1b0a9a23b71f"],
            created_utc={
                "end_utc": parse_datetime("2018-01-30T00:00:00Z"),
                "start_utc": parse_datetime("2018-01-01T00:00:00Z"),
            },
            customer_ids=["fadd5bb6-b428-45d5-94f8-fd0d89fece6d"],
            deleted_utc={
                "end_utc": parse_datetime("2019-12-27T18:11:19.117Z"),
                "start_utc": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            emails=["j.smith@example.com"],
            first_names=["John", "Jane"],
            last_names=["Doe", "Smith"],
            loyalty_codes=["LL810213"],
            updated_utc={
                "end_utc": parse_datetime("2018-01-30T00:00:00Z"),
                "start_utc": parse_datetime("2018-01-02T00:00:00Z"),
            },
        )
        assert_matches_type(CustomerListResponse, customer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.customers.with_raw_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            extent={},
            limitation={"count": 10},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert_matches_type(CustomerListResponse, customer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.customers.with_streaming_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            extent={},
            limitation={"count": 10},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(CustomerListResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_add(self, async_client: AsyncPymews) -> None:
        customer = await async_client.api.connector.v1.customers.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            last_name="Carbone",
            overwrite_existing=False,
        )
        assert_matches_type(Customer, customer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_add_with_all_params(self, async_client: AsyncPymews) -> None:
        customer = await async_client.api.connector.v1.customers.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            last_name="Carbone",
            overwrite_existing=False,
            address={
                "city": "Liborio laziale",
                "country_code": "IT",
                "country_subdivision_code": "IT-65",
                "line1": "Via Antimo 474 Piano 5",
                "line2": "Line2",
                "postal_code": "30228",
            },
            birth_date=parse_date("1985-09-30"),
            birth_place="Pescara (BI)",
            car_registration_number="AA 111AA",
            chain_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
            classifications=["PaymasterAccount", "Blacklist"],
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dietary_requirements="DietaryRequirements",
            drivers_license={
                "expiration": parse_date("2019-12-27"),
                "issuance": parse_date("2019-12-27"),
                "issuing_city": "IssuingCity",
                "issuing_country_code": "IssuingCountryCode",
                "number": "Number",
            },
            email="thea@quotidiano.example",
            first_name="Thea",
            identity_card={
                "expiration": parse_date("2019-12-27"),
                "issuance": parse_date("2019-12-27"),
                "issuing_city": "IssuingCity",
                "issuing_country_code": "IssuingCountryCode",
                "number": "Number",
            },
            italian_destination_code="7654321",
            italian_fiscal_code="ZGNZLR17U72P554F",
            loyalty_code="LoyaltyCode",
            nationality_code="NationalityCode",
            notes="Check-in notturno.",
            occupation="Giornalista",
            options=["SendMarketingEmails"],
            passport={
                "expiration": parse_date("2019-12-27"),
                "issuance": parse_date("2019-12-27"),
                "issuing_city": "IssuingCity",
                "issuing_country_code": "IssuingCountryCode",
                "number": "Number",
            },
            phone="+39 06 555 5555",
            second_last_name="SecondLastName",
            sex="Male",
            tax_identification_number="ZGNZLR17U72P554F",
            title="Mister",
            visa={
                "expiration": parse_date("2019-12-27"),
                "issuance": parse_date("2019-12-27"),
                "issuing_city": "IssuingCity",
                "issuing_country_code": "IssuingCountryCode",
                "number": "Number",
            },
        )
        assert_matches_type(Customer, customer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.customers.with_raw_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            last_name="Carbone",
            overwrite_existing=False,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert_matches_type(Customer, customer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.customers.with_streaming_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            last_name="Carbone",
            overwrite_existing=False,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(Customer, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_add_file(self, async_client: AsyncPymews) -> None:
        customer = await async_client.api.connector.v1.customers.add_file(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
            data="JVBERi0xLjAKMSAwIG9iajw8L1BhZ2VzIDIgMCBSPj5lbmRvYmogMiAwIG9iajw8L0tpZHNbMyAwIFJdL0NvdW50IDE+PmVuZG9iaiAzIDAgb2JqPDwvTWVkaWFCb3hbMCAwIDMgM10+PmVuZG9iagp0cmFpbGVyPDwvUm9vdCAxIDAgUj4+Cg==",
            name="document.pdf",
            type="application/pdf",
        )
        assert_matches_type(CustomerAddFileResponse, customer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_add_file_with_all_params(self, async_client: AsyncPymews) -> None:
        customer = await async_client.api.connector.v1.customers.add_file(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
            data="JVBERi0xLjAKMSAwIG9iajw8L1BhZ2VzIDIgMCBSPj5lbmRvYmogMiAwIG9iajw8L0tpZHNbMyAwIFJdL0NvdW50IDE+PmVuZG9iaiAzIDAgb2JqPDwvTWVkaWFCb3hbMCAwIDMgM10+PmVuZG9iagp0cmFpbGVyPDwvUm9vdCAxIDAgUj4+Cg==",
            name="document.pdf",
            type="application/pdf",
            chain_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )
        assert_matches_type(CustomerAddFileResponse, customer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_add_file(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.customers.with_raw_response.add_file(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
            data="JVBERi0xLjAKMSAwIG9iajw8L1BhZ2VzIDIgMCBSPj5lbmRvYmogMiAwIG9iajw8L0tpZHNbMyAwIFJdL0NvdW50IDE+PmVuZG9iaiAzIDAgb2JqPDwvTWVkaWFCb3hbMCAwIDMgM10+PmVuZG9iagp0cmFpbGVyPDwvUm9vdCAxIDAgUj4+Cg==",
            name="document.pdf",
            type="application/pdf",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert_matches_type(CustomerAddFileResponse, customer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_add_file(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.customers.with_streaming_response.add_file(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
            data="JVBERi0xLjAKMSAwIG9iajw8L1BhZ2VzIDIgMCBSPj5lbmRvYmogMiAwIG9iajw8L0tpZHNbMyAwIFJdL0NvdW50IDE+PmVuZG9iaiAzIDAgb2JqPDwvTWVkaWFCb3hbMCAwIDMgM10+PmVuZG9iagp0cmFpbGVyPDwvUm9vdCAxIDAgUj4+Cg==",
            name="document.pdf",
            type="application/pdf",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(CustomerAddFileResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_open_items(self, async_client: AsyncPymews) -> None:
        customer = await async_client.api.connector.v1.customers.get_open_items(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_ids=["2a1a4315-7e6f-4131-af21-402cec59b8b9"],
        )
        assert_matches_type(CustomerGetOpenItemsResponse, customer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_open_items_with_all_params(self, async_client: AsyncPymews) -> None:
        customer = await async_client.api.connector.v1.customers.get_open_items(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_ids=["2a1a4315-7e6f-4131-af21-402cec59b8b9"],
            currency=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(CustomerGetOpenItemsResponse, customer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_open_items(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.customers.with_raw_response.get_open_items(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_ids=["2a1a4315-7e6f-4131-af21-402cec59b8b9"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert_matches_type(CustomerGetOpenItemsResponse, customer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_open_items(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.customers.with_streaming_response.get_open_items(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_ids=["2a1a4315-7e6f-4131-af21-402cec59b8b9"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(CustomerGetOpenItemsResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_merge(self, async_client: AsyncPymews) -> None:
        customer = await async_client.api.connector.v1.customers.merge(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            source_customer_id="e11801ff-4148-4010-87f3-0d111e2893e3",
            target_customer_id="35d4b117-4e60-44a3-9580-c582117eff98",
        )
        assert_matches_type(object, customer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_merge(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.customers.with_raw_response.merge(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            source_customer_id="e11801ff-4148-4010-87f3-0d111e2893e3",
            target_customer_id="35d4b117-4e60-44a3-9580-c582117eff98",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert_matches_type(object, customer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_merge(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.customers.with_streaming_response.merge(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            source_customer_id="e11801ff-4148-4010-87f3-0d111e2893e3",
            target_customer_id="35d4b117-4e60-44a3-9580-c582117eff98",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(object, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_search(self, async_client: AsyncPymews) -> None:
        customer = await async_client.api.connector.v1.customers.search(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )
        assert_matches_type(CustomerSearchResponse, customer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncPymews) -> None:
        customer = await async_client.api.connector.v1.customers.search(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            extent={
                "addresses": False,
                "customers": True,
                "documents": False,
            },
            name="Smith",
            resource_id=None,
        )
        assert_matches_type(CustomerSearchResponse, customer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.customers.with_raw_response.search(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert_matches_type(CustomerSearchResponse, customer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.customers.with_streaming_response.search(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(CustomerSearchResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True
