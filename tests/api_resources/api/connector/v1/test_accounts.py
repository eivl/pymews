# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pymews import Pymews, AsyncPymews
from tests.utils import assert_matches_type
from pymews.types.api.connector.v1 import (
    AccountUpdateResponse,
    AccountAddFileResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccounts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Pymews) -> None:
        account = client.api.connector.v1.accounts.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            account_updates=[
                {
                    "discriminator": "Customer",
                    "id": "3ff104e6-3ba8-4dfc-8d35-b0ec00c5fd4c",
                },
                {
                    "discriminator": "Customer",
                    "id": "71db411f-c1d6-4e1c-9cd7-44e8bf45f936",
                },
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )
        assert_matches_type(AccountUpdateResponse, account, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Pymews) -> None:
        account = client.api.connector.v1.accounts.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            account_updates=[
                {
                    "discriminator": "Customer",
                    "id": "3ff104e6-3ba8-4dfc-8d35-b0ec00c5fd4c",
                    "company": {
                        "accounting_code": {"value": None},
                        "additional_tax_identifier": {"value": "XY00112233445"},
                        "billing_code": {"value": None},
                        "classifications": {
                            "corporate": {"value": True},
                            "global_distribution_system": {"value": True},
                            "government_entity": {"value": True},
                            "inactive": {"value": True},
                            "internal": {"value": True},
                            "marketing": {"value": True},
                            "online_travel_agency": {"value": True},
                            "private": {"value": True},
                        },
                        "contact": {"value": "Sample contact"},
                        "contact_person": {"value": "Sample person"},
                        "credit_rating_basic": {"value": "CreditOk"},
                        "department": {"value": "Accounting"},
                        "duns_number": {"value": "987654321"},
                        "email": {"value": "example@example.com"},
                        "external_identifier": {"value": "COM-123"},
                        "fiscal_identifier": {"value": "FiscalIdentifier"},
                        "iata": {"value": "PAO"},
                        "invoice_due_interval": {"value": None},
                        "mother_company_id": {"value": "839e9d92-aa8b-48bf-8384-b0ec0081bb34"},
                        "name": {"value": "Example company"},
                        "notes": {"value": "Example notes"},
                        "options": {
                            "add_fees_to_invoices": {"value": True},
                            "add_tax_deducted_payment_to_invoices": {"value": True},
                            "invoiceable": {"value": True},
                        },
                        "reference_id": {"value": None},
                        "source_id": {"value": "F42098A0-8507-4963-ACC9-B0EC00821949"},
                        "tax_identifier": {"value": "CZ8810310963"},
                        "telephone": {"value": "111-222-333"},
                        "website_url": {"value": "https://www.example.com"},
                    },
                    "customer": {
                        "accounting_code": {"value": "Value"},
                        "billing_code": {"value": "Value"},
                        "birth_date": {"value": "Value"},
                        "birth_place": {"value": "Value"},
                        "car_registration_number": {"value": "Value"},
                        "classifications": {
                            "airline": {"value": True},
                            "blacklist": {"value": True},
                            "cashlist": {"value": True},
                            "disabled_person": {"value": True},
                            "friend_or_family": {"value": True},
                            "health_compliant": {"value": True},
                            "important": {"value": True},
                            "in_room": {"value": True},
                            "loyalty_program": {"value": True},
                            "media": {"value": True},
                            "military": {"value": True},
                            "paymaster_account": {"value": True},
                            "previous_complaint": {"value": True},
                            "problematic": {"value": True},
                            "returning": {"value": True},
                            "staff": {"value": True},
                            "student": {"value": True},
                            "top_management": {"value": True},
                            "very_important": {"value": True},
                            "waiting_for_room": {"value": True},
                        },
                        "company_id": {"value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                        "dietary_requirements": {"value": "Value"},
                        "email": {"value": "Value"},
                        "first_name": {"value": "Value"},
                        "last_name": {"value": "Value"},
                        "legal_entity_identifiers": {
                            "it_destination_code": {"value": "Value"},
                            "it_fiscal_code": {"value": "Value"},
                        },
                        "loyalty_code": {"value": "Value"},
                        "nationality_code": {"value": "Value"},
                        "notes": {"value": "Value"},
                        "occupation": {"value": "Value"},
                        "options": {
                            "bill_address_objection": {"value": True},
                            "invoiceable": {"value": True},
                            "send_marketing_emails": {"value": True},
                        },
                        "preferred_language_code": {"value": "Value"},
                        "second_last_name": {"value": "Value"},
                        "sex": {"value": "Value"},
                        "tax_identifier": {"value": "Value"},
                        "telephone": {"value": "Value"},
                        "title": {"value": "Value"},
                    },
                },
                {
                    "discriminator": "Customer",
                    "id": "71db411f-c1d6-4e1c-9cd7-44e8bf45f936",
                    "company": {
                        "accounting_code": {"value": "Value"},
                        "additional_tax_identifier": {"value": "Value"},
                        "billing_code": {"value": "Value"},
                        "classifications": {
                            "corporate": {"value": True},
                            "global_distribution_system": {"value": True},
                            "government_entity": {"value": True},
                            "inactive": {"value": True},
                            "internal": {"value": True},
                            "marketing": {"value": True},
                            "online_travel_agency": {"value": True},
                            "private": {"value": True},
                        },
                        "contact": {"value": "Value"},
                        "contact_person": {"value": "Value"},
                        "credit_rating_basic": {"value": "Value"},
                        "department": {"value": "Value"},
                        "duns_number": {"value": "Value"},
                        "email": {"value": "Value"},
                        "external_identifier": {"value": "Value"},
                        "fiscal_identifier": {"value": "Value"},
                        "iata": {"value": "Value"},
                        "invoice_due_interval": {"value": "Value"},
                        "mother_company_id": {"value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                        "name": {"value": "Value"},
                        "notes": {"value": "Value"},
                        "options": {
                            "add_fees_to_invoices": {"value": True},
                            "add_tax_deducted_payment_to_invoices": {"value": True},
                            "invoiceable": {"value": True},
                        },
                        "reference_id": {"value": "Value"},
                        "source_id": {"value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                        "tax_identifier": {"value": "Value"},
                        "telephone": {"value": "Value"},
                        "website_url": {"value": "Value"},
                    },
                    "customer": {
                        "accounting_code": {"value": None},
                        "billing_code": {"value": None},
                        "birth_date": {"value": "2000-01-01"},
                        "birth_place": {"value": "Sample place"},
                        "car_registration_number": {"value": None},
                        "classifications": {
                            "airline": {"value": True},
                            "blacklist": {"value": True},
                            "cashlist": {"value": True},
                            "disabled_person": {"value": True},
                            "friend_or_family": {"value": True},
                            "health_compliant": {"value": True},
                            "important": {"value": True},
                            "in_room": {"value": True},
                            "loyalty_program": {"value": True},
                            "media": {"value": True},
                            "military": {"value": True},
                            "paymaster_account": {"value": True},
                            "previous_complaint": {"value": True},
                            "problematic": {"value": True},
                            "returning": {"value": True},
                            "staff": {"value": True},
                            "student": {"value": True},
                            "top_management": {"value": True},
                            "very_important": {"value": True},
                            "waiting_for_room": {"value": True},
                        },
                        "company_id": {"value": "839e9d92-aa8b-48bf-8384-b0ec0081bb34"},
                        "dietary_requirements": {"value": "Value"},
                        "email": {"value": "example@example.com"},
                        "first_name": {"value": "Sample"},
                        "last_name": {"value": "Sample"},
                        "legal_entity_identifiers": {
                            "it_destination_code": {"value": None},
                            "it_fiscal_code": {"value": None},
                        },
                        "loyalty_code": {"value": None},
                        "nationality_code": {"value": "US"},
                        "notes": {"value": "Example notes"},
                        "occupation": {"value": None},
                        "options": {
                            "bill_address_objection": {"value": True},
                            "invoiceable": {"value": True},
                            "send_marketing_emails": {"value": True},
                        },
                        "preferred_language_code": {"value": None},
                        "second_last_name": {"value": None},
                        "sex": {"value": "Male"},
                        "tax_identifier": {"value": "CZ8810310963"},
                        "telephone": {"value": "111-222-333"},
                        "title": {"value": "Mister"},
                    },
                },
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            chain_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AccountUpdateResponse, account, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Pymews) -> None:
        response = client.api.connector.v1.accounts.with_raw_response.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            account_updates=[
                {
                    "discriminator": "Customer",
                    "id": "3ff104e6-3ba8-4dfc-8d35-b0ec00c5fd4c",
                },
                {
                    "discriminator": "Customer",
                    "id": "71db411f-c1d6-4e1c-9cd7-44e8bf45f936",
                },
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountUpdateResponse, account, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Pymews) -> None:
        with client.api.connector.v1.accounts.with_streaming_response.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            account_updates=[
                {
                    "discriminator": "Customer",
                    "id": "3ff104e6-3ba8-4dfc-8d35-b0ec00c5fd4c",
                },
                {
                    "discriminator": "Customer",
                    "id": "71db411f-c1d6-4e1c-9cd7-44e8bf45f936",
                },
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountUpdateResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_add_file(self, client: Pymews) -> None:
        account = client.api.connector.v1.accounts.add_file(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            account_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            data="x",
            name="document.pdf",
            type="application/pdf",
        )
        assert_matches_type(AccountAddFileResponse, account, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_add_file_with_all_params(self, client: Pymews) -> None:
        account = client.api.connector.v1.accounts.add_file(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            account_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            data="x",
            name="document.pdf",
            type="application/pdf",
            chain_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )
        assert_matches_type(AccountAddFileResponse, account, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_add_file(self, client: Pymews) -> None:
        response = client.api.connector.v1.accounts.with_raw_response.add_file(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            account_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            data="x",
            name="document.pdf",
            type="application/pdf",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountAddFileResponse, account, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_add_file(self, client: Pymews) -> None:
        with client.api.connector.v1.accounts.with_streaming_response.add_file(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            account_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            data="x",
            name="document.pdf",
            type="application/pdf",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountAddFileResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_merge(self, client: Pymews) -> None:
        account = client.api.connector.v1.accounts.merge(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            account_merge_parameters=[
                {
                    "account_type": "Customer",
                    "source_account_ids": [
                        "b0c10ced-34eb-44b4-92e8-af5b008f3fb4",
                        "5176d000-bf17-40be-b140-9041d2b70eee",
                    ],
                    "target_account_id": "51262225-8130-4320-8210-af5b008f64e5",
                },
                {
                    "account_type": "Customer",
                    "source_account_ids": [
                        "7799f19a-c9c9-42bf-968f-a759e3ea1ea6",
                        "bb926ffe-5310-48bc-8202-6165fa3bdcad",
                    ],
                    "target_account_id": "49b2abd4-df58-4f1d-bead-0fa6342f8a78",
                },
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )
        assert_matches_type(object, account, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_merge(self, client: Pymews) -> None:
        response = client.api.connector.v1.accounts.with_raw_response.merge(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            account_merge_parameters=[
                {
                    "account_type": "Customer",
                    "source_account_ids": [
                        "b0c10ced-34eb-44b4-92e8-af5b008f3fb4",
                        "5176d000-bf17-40be-b140-9041d2b70eee",
                    ],
                    "target_account_id": "51262225-8130-4320-8210-af5b008f64e5",
                },
                {
                    "account_type": "Customer",
                    "source_account_ids": [
                        "7799f19a-c9c9-42bf-968f-a759e3ea1ea6",
                        "bb926ffe-5310-48bc-8202-6165fa3bdcad",
                    ],
                    "target_account_id": "49b2abd4-df58-4f1d-bead-0fa6342f8a78",
                },
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(object, account, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_merge(self, client: Pymews) -> None:
        with client.api.connector.v1.accounts.with_streaming_response.merge(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            account_merge_parameters=[
                {
                    "account_type": "Customer",
                    "source_account_ids": [
                        "b0c10ced-34eb-44b4-92e8-af5b008f3fb4",
                        "5176d000-bf17-40be-b140-9041d2b70eee",
                    ],
                    "target_account_id": "51262225-8130-4320-8210-af5b008f64e5",
                },
                {
                    "account_type": "Customer",
                    "source_account_ids": [
                        "7799f19a-c9c9-42bf-968f-a759e3ea1ea6",
                        "bb926ffe-5310-48bc-8202-6165fa3bdcad",
                    ],
                    "target_account_id": "49b2abd4-df58-4f1d-bead-0fa6342f8a78",
                },
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(object, account, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAccounts:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncPymews) -> None:
        account = await async_client.api.connector.v1.accounts.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            account_updates=[
                {
                    "discriminator": "Customer",
                    "id": "3ff104e6-3ba8-4dfc-8d35-b0ec00c5fd4c",
                },
                {
                    "discriminator": "Customer",
                    "id": "71db411f-c1d6-4e1c-9cd7-44e8bf45f936",
                },
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )
        assert_matches_type(AccountUpdateResponse, account, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncPymews) -> None:
        account = await async_client.api.connector.v1.accounts.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            account_updates=[
                {
                    "discriminator": "Customer",
                    "id": "3ff104e6-3ba8-4dfc-8d35-b0ec00c5fd4c",
                    "company": {
                        "accounting_code": {"value": None},
                        "additional_tax_identifier": {"value": "XY00112233445"},
                        "billing_code": {"value": None},
                        "classifications": {
                            "corporate": {"value": True},
                            "global_distribution_system": {"value": True},
                            "government_entity": {"value": True},
                            "inactive": {"value": True},
                            "internal": {"value": True},
                            "marketing": {"value": True},
                            "online_travel_agency": {"value": True},
                            "private": {"value": True},
                        },
                        "contact": {"value": "Sample contact"},
                        "contact_person": {"value": "Sample person"},
                        "credit_rating_basic": {"value": "CreditOk"},
                        "department": {"value": "Accounting"},
                        "duns_number": {"value": "987654321"},
                        "email": {"value": "example@example.com"},
                        "external_identifier": {"value": "COM-123"},
                        "fiscal_identifier": {"value": "FiscalIdentifier"},
                        "iata": {"value": "PAO"},
                        "invoice_due_interval": {"value": None},
                        "mother_company_id": {"value": "839e9d92-aa8b-48bf-8384-b0ec0081bb34"},
                        "name": {"value": "Example company"},
                        "notes": {"value": "Example notes"},
                        "options": {
                            "add_fees_to_invoices": {"value": True},
                            "add_tax_deducted_payment_to_invoices": {"value": True},
                            "invoiceable": {"value": True},
                        },
                        "reference_id": {"value": None},
                        "source_id": {"value": "F42098A0-8507-4963-ACC9-B0EC00821949"},
                        "tax_identifier": {"value": "CZ8810310963"},
                        "telephone": {"value": "111-222-333"},
                        "website_url": {"value": "https://www.example.com"},
                    },
                    "customer": {
                        "accounting_code": {"value": "Value"},
                        "billing_code": {"value": "Value"},
                        "birth_date": {"value": "Value"},
                        "birth_place": {"value": "Value"},
                        "car_registration_number": {"value": "Value"},
                        "classifications": {
                            "airline": {"value": True},
                            "blacklist": {"value": True},
                            "cashlist": {"value": True},
                            "disabled_person": {"value": True},
                            "friend_or_family": {"value": True},
                            "health_compliant": {"value": True},
                            "important": {"value": True},
                            "in_room": {"value": True},
                            "loyalty_program": {"value": True},
                            "media": {"value": True},
                            "military": {"value": True},
                            "paymaster_account": {"value": True},
                            "previous_complaint": {"value": True},
                            "problematic": {"value": True},
                            "returning": {"value": True},
                            "staff": {"value": True},
                            "student": {"value": True},
                            "top_management": {"value": True},
                            "very_important": {"value": True},
                            "waiting_for_room": {"value": True},
                        },
                        "company_id": {"value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                        "dietary_requirements": {"value": "Value"},
                        "email": {"value": "Value"},
                        "first_name": {"value": "Value"},
                        "last_name": {"value": "Value"},
                        "legal_entity_identifiers": {
                            "it_destination_code": {"value": "Value"},
                            "it_fiscal_code": {"value": "Value"},
                        },
                        "loyalty_code": {"value": "Value"},
                        "nationality_code": {"value": "Value"},
                        "notes": {"value": "Value"},
                        "occupation": {"value": "Value"},
                        "options": {
                            "bill_address_objection": {"value": True},
                            "invoiceable": {"value": True},
                            "send_marketing_emails": {"value": True},
                        },
                        "preferred_language_code": {"value": "Value"},
                        "second_last_name": {"value": "Value"},
                        "sex": {"value": "Value"},
                        "tax_identifier": {"value": "Value"},
                        "telephone": {"value": "Value"},
                        "title": {"value": "Value"},
                    },
                },
                {
                    "discriminator": "Customer",
                    "id": "71db411f-c1d6-4e1c-9cd7-44e8bf45f936",
                    "company": {
                        "accounting_code": {"value": "Value"},
                        "additional_tax_identifier": {"value": "Value"},
                        "billing_code": {"value": "Value"},
                        "classifications": {
                            "corporate": {"value": True},
                            "global_distribution_system": {"value": True},
                            "government_entity": {"value": True},
                            "inactive": {"value": True},
                            "internal": {"value": True},
                            "marketing": {"value": True},
                            "online_travel_agency": {"value": True},
                            "private": {"value": True},
                        },
                        "contact": {"value": "Value"},
                        "contact_person": {"value": "Value"},
                        "credit_rating_basic": {"value": "Value"},
                        "department": {"value": "Value"},
                        "duns_number": {"value": "Value"},
                        "email": {"value": "Value"},
                        "external_identifier": {"value": "Value"},
                        "fiscal_identifier": {"value": "Value"},
                        "iata": {"value": "Value"},
                        "invoice_due_interval": {"value": "Value"},
                        "mother_company_id": {"value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                        "name": {"value": "Value"},
                        "notes": {"value": "Value"},
                        "options": {
                            "add_fees_to_invoices": {"value": True},
                            "add_tax_deducted_payment_to_invoices": {"value": True},
                            "invoiceable": {"value": True},
                        },
                        "reference_id": {"value": "Value"},
                        "source_id": {"value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                        "tax_identifier": {"value": "Value"},
                        "telephone": {"value": "Value"},
                        "website_url": {"value": "Value"},
                    },
                    "customer": {
                        "accounting_code": {"value": None},
                        "billing_code": {"value": None},
                        "birth_date": {"value": "2000-01-01"},
                        "birth_place": {"value": "Sample place"},
                        "car_registration_number": {"value": None},
                        "classifications": {
                            "airline": {"value": True},
                            "blacklist": {"value": True},
                            "cashlist": {"value": True},
                            "disabled_person": {"value": True},
                            "friend_or_family": {"value": True},
                            "health_compliant": {"value": True},
                            "important": {"value": True},
                            "in_room": {"value": True},
                            "loyalty_program": {"value": True},
                            "media": {"value": True},
                            "military": {"value": True},
                            "paymaster_account": {"value": True},
                            "previous_complaint": {"value": True},
                            "problematic": {"value": True},
                            "returning": {"value": True},
                            "staff": {"value": True},
                            "student": {"value": True},
                            "top_management": {"value": True},
                            "very_important": {"value": True},
                            "waiting_for_room": {"value": True},
                        },
                        "company_id": {"value": "839e9d92-aa8b-48bf-8384-b0ec0081bb34"},
                        "dietary_requirements": {"value": "Value"},
                        "email": {"value": "example@example.com"},
                        "first_name": {"value": "Sample"},
                        "last_name": {"value": "Sample"},
                        "legal_entity_identifiers": {
                            "it_destination_code": {"value": None},
                            "it_fiscal_code": {"value": None},
                        },
                        "loyalty_code": {"value": None},
                        "nationality_code": {"value": "US"},
                        "notes": {"value": "Example notes"},
                        "occupation": {"value": None},
                        "options": {
                            "bill_address_objection": {"value": True},
                            "invoiceable": {"value": True},
                            "send_marketing_emails": {"value": True},
                        },
                        "preferred_language_code": {"value": None},
                        "second_last_name": {"value": None},
                        "sex": {"value": "Male"},
                        "tax_identifier": {"value": "CZ8810310963"},
                        "telephone": {"value": "111-222-333"},
                        "title": {"value": "Mister"},
                    },
                },
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            chain_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AccountUpdateResponse, account, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.accounts.with_raw_response.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            account_updates=[
                {
                    "discriminator": "Customer",
                    "id": "3ff104e6-3ba8-4dfc-8d35-b0ec00c5fd4c",
                },
                {
                    "discriminator": "Customer",
                    "id": "71db411f-c1d6-4e1c-9cd7-44e8bf45f936",
                },
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountUpdateResponse, account, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.accounts.with_streaming_response.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            account_updates=[
                {
                    "discriminator": "Customer",
                    "id": "3ff104e6-3ba8-4dfc-8d35-b0ec00c5fd4c",
                },
                {
                    "discriminator": "Customer",
                    "id": "71db411f-c1d6-4e1c-9cd7-44e8bf45f936",
                },
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountUpdateResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_add_file(self, async_client: AsyncPymews) -> None:
        account = await async_client.api.connector.v1.accounts.add_file(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            account_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            data="x",
            name="document.pdf",
            type="application/pdf",
        )
        assert_matches_type(AccountAddFileResponse, account, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_add_file_with_all_params(self, async_client: AsyncPymews) -> None:
        account = await async_client.api.connector.v1.accounts.add_file(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            account_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            data="x",
            name="document.pdf",
            type="application/pdf",
            chain_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )
        assert_matches_type(AccountAddFileResponse, account, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_add_file(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.accounts.with_raw_response.add_file(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            account_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            data="x",
            name="document.pdf",
            type="application/pdf",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountAddFileResponse, account, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_add_file(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.accounts.with_streaming_response.add_file(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            account_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            data="x",
            name="document.pdf",
            type="application/pdf",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountAddFileResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_merge(self, async_client: AsyncPymews) -> None:
        account = await async_client.api.connector.v1.accounts.merge(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            account_merge_parameters=[
                {
                    "account_type": "Customer",
                    "source_account_ids": [
                        "b0c10ced-34eb-44b4-92e8-af5b008f3fb4",
                        "5176d000-bf17-40be-b140-9041d2b70eee",
                    ],
                    "target_account_id": "51262225-8130-4320-8210-af5b008f64e5",
                },
                {
                    "account_type": "Customer",
                    "source_account_ids": [
                        "7799f19a-c9c9-42bf-968f-a759e3ea1ea6",
                        "bb926ffe-5310-48bc-8202-6165fa3bdcad",
                    ],
                    "target_account_id": "49b2abd4-df58-4f1d-bead-0fa6342f8a78",
                },
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )
        assert_matches_type(object, account, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_merge(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.accounts.with_raw_response.merge(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            account_merge_parameters=[
                {
                    "account_type": "Customer",
                    "source_account_ids": [
                        "b0c10ced-34eb-44b4-92e8-af5b008f3fb4",
                        "5176d000-bf17-40be-b140-9041d2b70eee",
                    ],
                    "target_account_id": "51262225-8130-4320-8210-af5b008f64e5",
                },
                {
                    "account_type": "Customer",
                    "source_account_ids": [
                        "7799f19a-c9c9-42bf-968f-a759e3ea1ea6",
                        "bb926ffe-5310-48bc-8202-6165fa3bdcad",
                    ],
                    "target_account_id": "49b2abd4-df58-4f1d-bead-0fa6342f8a78",
                },
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(object, account, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_merge(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.accounts.with_streaming_response.merge(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            account_merge_parameters=[
                {
                    "account_type": "Customer",
                    "source_account_ids": [
                        "b0c10ced-34eb-44b4-92e8-af5b008f3fb4",
                        "5176d000-bf17-40be-b140-9041d2b70eee",
                    ],
                    "target_account_id": "51262225-8130-4320-8210-af5b008f64e5",
                },
                {
                    "account_type": "Customer",
                    "source_account_ids": [
                        "7799f19a-c9c9-42bf-968f-a759e3ea1ea6",
                        "bb926ffe-5310-48bc-8202-6165fa3bdcad",
                    ],
                    "target_account_id": "49b2abd4-df58-4f1d-bead-0fa6342f8a78",
                },
            ],
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(object, account, path=["response"])

        assert cast(Any, response.is_closed) is True
