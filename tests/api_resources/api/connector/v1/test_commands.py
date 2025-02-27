# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pymews import Pymews, AsyncPymews
from tests.utils import assert_matches_type
from pymews.types.api.connector.v1 import (
    DeviceCommandResult,
    DeviceCommandAddResult,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCommands:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Pymews) -> None:
        command = client.api.connector.v1.commands.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            command_id="aa20961f-6d9e-4b35-ad25-071213530aec",
            state="Pending",
        )
        assert_matches_type(object, command, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Pymews) -> None:
        command = client.api.connector.v1.commands.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            command_id="aa20961f-6d9e-4b35-ad25-071213530aec",
            state="Pending",
            external_request_identifier={"value": "Value"},
            notes="Notes",
            progress=0,
        )
        assert_matches_type(object, command, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Pymews) -> None:
        response = client.api.connector.v1.commands.with_raw_response.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            command_id="aa20961f-6d9e-4b35-ad25-071213530aec",
            state="Pending",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        command = response.parse()
        assert_matches_type(object, command, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Pymews) -> None:
        with client.api.connector.v1.commands.with_streaming_response.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            command_id="aa20961f-6d9e-4b35-ad25-071213530aec",
            state="Pending",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            command = response.parse()
            assert_matches_type(object, command, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_add_key_cutter(self, client: Pymews) -> None:
        command = client.api.connector.v1.commands.add_key_cutter(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            key_count=1,
            key_cutter_id="7dafffff-a727-4917-a203-bd53995f21bf",
            reservation_id="be35b39e-ad7e-460a-8de9-4c7581e016a2",
        )
        assert_matches_type(DeviceCommandAddResult, command, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_add_key_cutter_with_all_params(self, client: Pymews) -> None:
        command = client.api.connector.v1.commands.add_key_cutter(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            key_count=1,
            key_cutter_id="7dafffff-a727-4917-a203-bd53995f21bf",
            reservation_id="be35b39e-ad7e-460a-8de9-4c7581e016a2",
            enterprise_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )
        assert_matches_type(DeviceCommandAddResult, command, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_add_key_cutter(self, client: Pymews) -> None:
        response = client.api.connector.v1.commands.with_raw_response.add_key_cutter(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            key_count=1,
            key_cutter_id="7dafffff-a727-4917-a203-bd53995f21bf",
            reservation_id="be35b39e-ad7e-460a-8de9-4c7581e016a2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        command = response.parse()
        assert_matches_type(DeviceCommandAddResult, command, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_add_key_cutter(self, client: Pymews) -> None:
        with client.api.connector.v1.commands.with_streaming_response.add_key_cutter(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            key_count=1,
            key_cutter_id="7dafffff-a727-4917-a203-bd53995f21bf",
            reservation_id="be35b39e-ad7e-460a-8de9-4c7581e016a2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            command = response.parse()
            assert_matches_type(DeviceCommandAddResult, command, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_add_payment_terminal(self, client: Pymews) -> None:
        command = client.api.connector.v1.commands.add_payment_terminal(
            access_token="7059D2C25BF64EA681ACAB3A00B859CC-D91BFF2B1E3047A3E0DEC1D57BE1382",
            client="MyPOS 1.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_id="35d4b117-4e60-44a3-9580-c582117eff98",
            terminal_id="be35b39e-ad7e-460a-8de9-4c7581e016a2",
            type="Payment",
        )
        assert_matches_type(DeviceCommandAddResult, command, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_add_payment_terminal_with_all_params(self, client: Pymews) -> None:
        command = client.api.connector.v1.commands.add_payment_terminal(
            access_token="7059D2C25BF64EA681ACAB3A00B859CC-D91BFF2B1E3047A3E0DEC1D57BE1382",
            client="MyPOS 1.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_id="35d4b117-4e60-44a3-9580-c582117eff98",
            terminal_id="be35b39e-ad7e-460a-8de9-4c7581e016a2",
            type="Payment",
            amount={
                "currency": "EUR",
                "net": 0,
                "tax": 0,
                "tax_rate": 0,
                "value": 230,
            },
            bill_id=None,
            payment_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            reservation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DeviceCommandAddResult, command, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_add_payment_terminal(self, client: Pymews) -> None:
        response = client.api.connector.v1.commands.with_raw_response.add_payment_terminal(
            access_token="7059D2C25BF64EA681ACAB3A00B859CC-D91BFF2B1E3047A3E0DEC1D57BE1382",
            client="MyPOS 1.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_id="35d4b117-4e60-44a3-9580-c582117eff98",
            terminal_id="be35b39e-ad7e-460a-8de9-4c7581e016a2",
            type="Payment",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        command = response.parse()
        assert_matches_type(DeviceCommandAddResult, command, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_add_payment_terminal(self, client: Pymews) -> None:
        with client.api.connector.v1.commands.with_streaming_response.add_payment_terminal(
            access_token="7059D2C25BF64EA681ACAB3A00B859CC-D91BFF2B1E3047A3E0DEC1D57BE1382",
            client="MyPOS 1.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_id="35d4b117-4e60-44a3-9580-c582117eff98",
            terminal_id="be35b39e-ad7e-460a-8de9-4c7581e016a2",
            type="Payment",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            command = response.parse()
            assert_matches_type(DeviceCommandAddResult, command, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_add_printer(self, client: Pymews) -> None:
        command = client.api.connector.v1.commands.add_printer(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            copy_count=1,
            data="JVBERi0xLjcKCjEgMCBvYmogICUgZW50cnkgcG9pbnQKPDwKICAvVHlwZSAvQ2F0YWxvZwogIC9QYWdlcyAyIDAgUgo+PgplbmRvYmoKCjIgMCBvYmoKPDwKICAvVHlwZSAvUGFnZXMKICAvTWVkaWFCb3ggWyAwIDAgMjAwIDIwMCBdCiAgL0NvdW50IDEKICAvS2lkcyBbIDMgMCBSIF0KPj4KZW5kb2JqCgozIDAgb2JqCjw8CiAgL1R5cGUgL1BhZ2UKICAvUGFyZW50IDIgMCBSCiAgL1Jlc291cmNlcyA8PAogICAgL0ZvbnQgPDwKICAgICAgL0YxIDQgMCBSIAogICAgPj4KICA+PgogIC9Db250ZW50cyA1IDAgUgo+PgplbmRvYmoKCjQgMCBvYmoKPDwKICAvVHlwZSAvRm9udAogIC9TdWJ0eXBlIC9UeXBlMQogIC9CYXNlRm9udCAvVGltZXMtUm9tYW4KPj4KZW5kb2JqCgo1IDAgb2JqICAlIHBhZ2UgY29udGVudAo8PAogIC9MZW5ndGggNDQKPj4Kc3RyZWFtCkJUCjcwIDUwIFRECi9GMSAxMiBUZgooSGVsbG8sIHdvcmxkISkgVGoKRVQKZW5kc3RyZWFtCmVuZG9iagoKeHJlZgowIDYKMDAwMDAwMDAwMCA2NTUzNSBmIAowMDAwMDAwMDEwIDAwMDAwIG4gCjAwMDAwMDAwNzkgMDAwMDAgbiAKMDAwMDAwMDE3MyAwMDAwMCBuIAowMDAwMDAwMzAxIDAwMDAwIG4gCjAwMDAwMDAzODAgMDAwMDAgbiAKdHJhaWxlcgo8PAogIC9TaXplIDYKICAvUm9vdCAxIDAgUgo+PgpzdGFydHhyZWYKNDkyCiUlRU9G",
            printer_id="d117866d-78de-4459-9077-42d7ea0120e3",
        )
        assert_matches_type(DeviceCommandAddResult, command, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_add_printer_with_all_params(self, client: Pymews) -> None:
        command = client.api.connector.v1.commands.add_printer(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            copy_count=1,
            data="JVBERi0xLjcKCjEgMCBvYmogICUgZW50cnkgcG9pbnQKPDwKICAvVHlwZSAvQ2F0YWxvZwogIC9QYWdlcyAyIDAgUgo+PgplbmRvYmoKCjIgMCBvYmoKPDwKICAvVHlwZSAvUGFnZXMKICAvTWVkaWFCb3ggWyAwIDAgMjAwIDIwMCBdCiAgL0NvdW50IDEKICAvS2lkcyBbIDMgMCBSIF0KPj4KZW5kb2JqCgozIDAgb2JqCjw8CiAgL1R5cGUgL1BhZ2UKICAvUGFyZW50IDIgMCBSCiAgL1Jlc291cmNlcyA8PAogICAgL0ZvbnQgPDwKICAgICAgL0YxIDQgMCBSIAogICAgPj4KICA+PgogIC9Db250ZW50cyA1IDAgUgo+PgplbmRvYmoKCjQgMCBvYmoKPDwKICAvVHlwZSAvRm9udAogIC9TdWJ0eXBlIC9UeXBlMQogIC9CYXNlRm9udCAvVGltZXMtUm9tYW4KPj4KZW5kb2JqCgo1IDAgb2JqICAlIHBhZ2UgY29udGVudAo8PAogIC9MZW5ndGggNDQKPj4Kc3RyZWFtCkJUCjcwIDUwIFRECi9GMSAxMiBUZgooSGVsbG8sIHdvcmxkISkgVGoKRVQKZW5kc3RyZWFtCmVuZG9iagoKeHJlZgowIDYKMDAwMDAwMDAwMCA2NTUzNSBmIAowMDAwMDAwMDEwIDAwMDAwIG4gCjAwMDAwMDAwNzkgMDAwMDAgbiAKMDAwMDAwMDE3MyAwMDAwMCBuIAowMDAwMDAwMzAxIDAwMDAwIG4gCjAwMDAwMDAzODAgMDAwMDAgbiAKdHJhaWxlcgo8PAogIC9TaXplIDYKICAvUm9vdCAxIDAgUgo+PgpzdGFydHhyZWYKNDkyCiUlRU9G",
            printer_id="d117866d-78de-4459-9077-42d7ea0120e3",
            enterprise_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )
        assert_matches_type(DeviceCommandAddResult, command, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_add_printer(self, client: Pymews) -> None:
        response = client.api.connector.v1.commands.with_raw_response.add_printer(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            copy_count=1,
            data="JVBERi0xLjcKCjEgMCBvYmogICUgZW50cnkgcG9pbnQKPDwKICAvVHlwZSAvQ2F0YWxvZwogIC9QYWdlcyAyIDAgUgo+PgplbmRvYmoKCjIgMCBvYmoKPDwKICAvVHlwZSAvUGFnZXMKICAvTWVkaWFCb3ggWyAwIDAgMjAwIDIwMCBdCiAgL0NvdW50IDEKICAvS2lkcyBbIDMgMCBSIF0KPj4KZW5kb2JqCgozIDAgb2JqCjw8CiAgL1R5cGUgL1BhZ2UKICAvUGFyZW50IDIgMCBSCiAgL1Jlc291cmNlcyA8PAogICAgL0ZvbnQgPDwKICAgICAgL0YxIDQgMCBSIAogICAgPj4KICA+PgogIC9Db250ZW50cyA1IDAgUgo+PgplbmRvYmoKCjQgMCBvYmoKPDwKICAvVHlwZSAvRm9udAogIC9TdWJ0eXBlIC9UeXBlMQogIC9CYXNlRm9udCAvVGltZXMtUm9tYW4KPj4KZW5kb2JqCgo1IDAgb2JqICAlIHBhZ2UgY29udGVudAo8PAogIC9MZW5ndGggNDQKPj4Kc3RyZWFtCkJUCjcwIDUwIFRECi9GMSAxMiBUZgooSGVsbG8sIHdvcmxkISkgVGoKRVQKZW5kc3RyZWFtCmVuZG9iagoKeHJlZgowIDYKMDAwMDAwMDAwMCA2NTUzNSBmIAowMDAwMDAwMDEwIDAwMDAwIG4gCjAwMDAwMDAwNzkgMDAwMDAgbiAKMDAwMDAwMDE3MyAwMDAwMCBuIAowMDAwMDAwMzAxIDAwMDAwIG4gCjAwMDAwMDAzODAgMDAwMDAgbiAKdHJhaWxlcgo8PAogIC9TaXplIDYKICAvUm9vdCAxIDAgUgo+PgpzdGFydHhyZWYKNDkyCiUlRU9G",
            printer_id="d117866d-78de-4459-9077-42d7ea0120e3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        command = response.parse()
        assert_matches_type(DeviceCommandAddResult, command, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_add_printer(self, client: Pymews) -> None:
        with client.api.connector.v1.commands.with_streaming_response.add_printer(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            copy_count=1,
            data="JVBERi0xLjcKCjEgMCBvYmogICUgZW50cnkgcG9pbnQKPDwKICAvVHlwZSAvQ2F0YWxvZwogIC9QYWdlcyAyIDAgUgo+PgplbmRvYmoKCjIgMCBvYmoKPDwKICAvVHlwZSAvUGFnZXMKICAvTWVkaWFCb3ggWyAwIDAgMjAwIDIwMCBdCiAgL0NvdW50IDEKICAvS2lkcyBbIDMgMCBSIF0KPj4KZW5kb2JqCgozIDAgb2JqCjw8CiAgL1R5cGUgL1BhZ2UKICAvUGFyZW50IDIgMCBSCiAgL1Jlc291cmNlcyA8PAogICAgL0ZvbnQgPDwKICAgICAgL0YxIDQgMCBSIAogICAgPj4KICA+PgogIC9Db250ZW50cyA1IDAgUgo+PgplbmRvYmoKCjQgMCBvYmoKPDwKICAvVHlwZSAvRm9udAogIC9TdWJ0eXBlIC9UeXBlMQogIC9CYXNlRm9udCAvVGltZXMtUm9tYW4KPj4KZW5kb2JqCgo1IDAgb2JqICAlIHBhZ2UgY29udGVudAo8PAogIC9MZW5ndGggNDQKPj4Kc3RyZWFtCkJUCjcwIDUwIFRECi9GMSAxMiBUZgooSGVsbG8sIHdvcmxkISkgVGoKRVQKZW5kc3RyZWFtCmVuZG9iagoKeHJlZgowIDYKMDAwMDAwMDAwMCA2NTUzNSBmIAowMDAwMDAwMDEwIDAwMDAwIG4gCjAwMDAwMDAwNzkgMDAwMDAgbiAKMDAwMDAwMDE3MyAwMDAwMCBuIAowMDAwMDAwMzAxIDAwMDAwIG4gCjAwMDAwMDAzODAgMDAwMDAgbiAKdHJhaWxlcgo8PAogIC9TaXplIDYKICAvUm9vdCAxIDAgUgo+PgpzdGFydHhyZWYKNDkyCiUlRU9G",
            printer_id="d117866d-78de-4459-9077-42d7ea0120e3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            command = response.parse()
            assert_matches_type(DeviceCommandAddResult, command, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list_active(self, client: Pymews) -> None:
        command = client.api.connector.v1.commands.list_active(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )
        assert_matches_type(DeviceCommandResult, command, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_active(self, client: Pymews) -> None:
        response = client.api.connector.v1.commands.with_raw_response.list_active(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        command = response.parse()
        assert_matches_type(DeviceCommandResult, command, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_active(self, client: Pymews) -> None:
        with client.api.connector.v1.commands.with_streaming_response.list_active(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            command = response.parse()
            assert_matches_type(DeviceCommandResult, command, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list_by_ids(self, client: Pymews) -> None:
        command = client.api.connector.v1.commands.list_by_ids(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            command_ids=["aa20961f-6d9e-4b35-ad25-071213530aec"],
        )
        assert_matches_type(DeviceCommandResult, command, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_by_ids_with_all_params(self, client: Pymews) -> None:
        command = client.api.connector.v1.commands.list_by_ids(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            command_ids=["aa20961f-6d9e-4b35-ad25-071213530aec"],
            limitation={
                "count": 0,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
        )
        assert_matches_type(DeviceCommandResult, command, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_by_ids(self, client: Pymews) -> None:
        response = client.api.connector.v1.commands.with_raw_response.list_by_ids(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            command_ids=["aa20961f-6d9e-4b35-ad25-071213530aec"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        command = response.parse()
        assert_matches_type(DeviceCommandResult, command, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_by_ids(self, client: Pymews) -> None:
        with client.api.connector.v1.commands.with_streaming_response.list_by_ids(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            command_ids=["aa20961f-6d9e-4b35-ad25-071213530aec"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            command = response.parse()
            assert_matches_type(DeviceCommandResult, command, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCommands:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncPymews) -> None:
        command = await async_client.api.connector.v1.commands.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            command_id="aa20961f-6d9e-4b35-ad25-071213530aec",
            state="Pending",
        )
        assert_matches_type(object, command, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncPymews) -> None:
        command = await async_client.api.connector.v1.commands.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            command_id="aa20961f-6d9e-4b35-ad25-071213530aec",
            state="Pending",
            external_request_identifier={"value": "Value"},
            notes="Notes",
            progress=0,
        )
        assert_matches_type(object, command, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.commands.with_raw_response.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            command_id="aa20961f-6d9e-4b35-ad25-071213530aec",
            state="Pending",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        command = await response.parse()
        assert_matches_type(object, command, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.commands.with_streaming_response.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            command_id="aa20961f-6d9e-4b35-ad25-071213530aec",
            state="Pending",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            command = await response.parse()
            assert_matches_type(object, command, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_add_key_cutter(self, async_client: AsyncPymews) -> None:
        command = await async_client.api.connector.v1.commands.add_key_cutter(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            key_count=1,
            key_cutter_id="7dafffff-a727-4917-a203-bd53995f21bf",
            reservation_id="be35b39e-ad7e-460a-8de9-4c7581e016a2",
        )
        assert_matches_type(DeviceCommandAddResult, command, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_add_key_cutter_with_all_params(self, async_client: AsyncPymews) -> None:
        command = await async_client.api.connector.v1.commands.add_key_cutter(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            key_count=1,
            key_cutter_id="7dafffff-a727-4917-a203-bd53995f21bf",
            reservation_id="be35b39e-ad7e-460a-8de9-4c7581e016a2",
            enterprise_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )
        assert_matches_type(DeviceCommandAddResult, command, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_add_key_cutter(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.commands.with_raw_response.add_key_cutter(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            key_count=1,
            key_cutter_id="7dafffff-a727-4917-a203-bd53995f21bf",
            reservation_id="be35b39e-ad7e-460a-8de9-4c7581e016a2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        command = await response.parse()
        assert_matches_type(DeviceCommandAddResult, command, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_add_key_cutter(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.commands.with_streaming_response.add_key_cutter(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            key_count=1,
            key_cutter_id="7dafffff-a727-4917-a203-bd53995f21bf",
            reservation_id="be35b39e-ad7e-460a-8de9-4c7581e016a2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            command = await response.parse()
            assert_matches_type(DeviceCommandAddResult, command, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_add_payment_terminal(self, async_client: AsyncPymews) -> None:
        command = await async_client.api.connector.v1.commands.add_payment_terminal(
            access_token="7059D2C25BF64EA681ACAB3A00B859CC-D91BFF2B1E3047A3E0DEC1D57BE1382",
            client="MyPOS 1.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_id="35d4b117-4e60-44a3-9580-c582117eff98",
            terminal_id="be35b39e-ad7e-460a-8de9-4c7581e016a2",
            type="Payment",
        )
        assert_matches_type(DeviceCommandAddResult, command, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_add_payment_terminal_with_all_params(self, async_client: AsyncPymews) -> None:
        command = await async_client.api.connector.v1.commands.add_payment_terminal(
            access_token="7059D2C25BF64EA681ACAB3A00B859CC-D91BFF2B1E3047A3E0DEC1D57BE1382",
            client="MyPOS 1.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_id="35d4b117-4e60-44a3-9580-c582117eff98",
            terminal_id="be35b39e-ad7e-460a-8de9-4c7581e016a2",
            type="Payment",
            amount={
                "currency": "EUR",
                "net": 0,
                "tax": 0,
                "tax_rate": 0,
                "value": 230,
            },
            bill_id=None,
            payment_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            reservation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DeviceCommandAddResult, command, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_add_payment_terminal(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.commands.with_raw_response.add_payment_terminal(
            access_token="7059D2C25BF64EA681ACAB3A00B859CC-D91BFF2B1E3047A3E0DEC1D57BE1382",
            client="MyPOS 1.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_id="35d4b117-4e60-44a3-9580-c582117eff98",
            terminal_id="be35b39e-ad7e-460a-8de9-4c7581e016a2",
            type="Payment",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        command = await response.parse()
        assert_matches_type(DeviceCommandAddResult, command, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_add_payment_terminal(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.commands.with_streaming_response.add_payment_terminal(
            access_token="7059D2C25BF64EA681ACAB3A00B859CC-D91BFF2B1E3047A3E0DEC1D57BE1382",
            client="MyPOS 1.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            customer_id="35d4b117-4e60-44a3-9580-c582117eff98",
            terminal_id="be35b39e-ad7e-460a-8de9-4c7581e016a2",
            type="Payment",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            command = await response.parse()
            assert_matches_type(DeviceCommandAddResult, command, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_add_printer(self, async_client: AsyncPymews) -> None:
        command = await async_client.api.connector.v1.commands.add_printer(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            copy_count=1,
            data="JVBERi0xLjcKCjEgMCBvYmogICUgZW50cnkgcG9pbnQKPDwKICAvVHlwZSAvQ2F0YWxvZwogIC9QYWdlcyAyIDAgUgo+PgplbmRvYmoKCjIgMCBvYmoKPDwKICAvVHlwZSAvUGFnZXMKICAvTWVkaWFCb3ggWyAwIDAgMjAwIDIwMCBdCiAgL0NvdW50IDEKICAvS2lkcyBbIDMgMCBSIF0KPj4KZW5kb2JqCgozIDAgb2JqCjw8CiAgL1R5cGUgL1BhZ2UKICAvUGFyZW50IDIgMCBSCiAgL1Jlc291cmNlcyA8PAogICAgL0ZvbnQgPDwKICAgICAgL0YxIDQgMCBSIAogICAgPj4KICA+PgogIC9Db250ZW50cyA1IDAgUgo+PgplbmRvYmoKCjQgMCBvYmoKPDwKICAvVHlwZSAvRm9udAogIC9TdWJ0eXBlIC9UeXBlMQogIC9CYXNlRm9udCAvVGltZXMtUm9tYW4KPj4KZW5kb2JqCgo1IDAgb2JqICAlIHBhZ2UgY29udGVudAo8PAogIC9MZW5ndGggNDQKPj4Kc3RyZWFtCkJUCjcwIDUwIFRECi9GMSAxMiBUZgooSGVsbG8sIHdvcmxkISkgVGoKRVQKZW5kc3RyZWFtCmVuZG9iagoKeHJlZgowIDYKMDAwMDAwMDAwMCA2NTUzNSBmIAowMDAwMDAwMDEwIDAwMDAwIG4gCjAwMDAwMDAwNzkgMDAwMDAgbiAKMDAwMDAwMDE3MyAwMDAwMCBuIAowMDAwMDAwMzAxIDAwMDAwIG4gCjAwMDAwMDAzODAgMDAwMDAgbiAKdHJhaWxlcgo8PAogIC9TaXplIDYKICAvUm9vdCAxIDAgUgo+PgpzdGFydHhyZWYKNDkyCiUlRU9G",
            printer_id="d117866d-78de-4459-9077-42d7ea0120e3",
        )
        assert_matches_type(DeviceCommandAddResult, command, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_add_printer_with_all_params(self, async_client: AsyncPymews) -> None:
        command = await async_client.api.connector.v1.commands.add_printer(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            copy_count=1,
            data="JVBERi0xLjcKCjEgMCBvYmogICUgZW50cnkgcG9pbnQKPDwKICAvVHlwZSAvQ2F0YWxvZwogIC9QYWdlcyAyIDAgUgo+PgplbmRvYmoKCjIgMCBvYmoKPDwKICAvVHlwZSAvUGFnZXMKICAvTWVkaWFCb3ggWyAwIDAgMjAwIDIwMCBdCiAgL0NvdW50IDEKICAvS2lkcyBbIDMgMCBSIF0KPj4KZW5kb2JqCgozIDAgb2JqCjw8CiAgL1R5cGUgL1BhZ2UKICAvUGFyZW50IDIgMCBSCiAgL1Jlc291cmNlcyA8PAogICAgL0ZvbnQgPDwKICAgICAgL0YxIDQgMCBSIAogICAgPj4KICA+PgogIC9Db250ZW50cyA1IDAgUgo+PgplbmRvYmoKCjQgMCBvYmoKPDwKICAvVHlwZSAvRm9udAogIC9TdWJ0eXBlIC9UeXBlMQogIC9CYXNlRm9udCAvVGltZXMtUm9tYW4KPj4KZW5kb2JqCgo1IDAgb2JqICAlIHBhZ2UgY29udGVudAo8PAogIC9MZW5ndGggNDQKPj4Kc3RyZWFtCkJUCjcwIDUwIFRECi9GMSAxMiBUZgooSGVsbG8sIHdvcmxkISkgVGoKRVQKZW5kc3RyZWFtCmVuZG9iagoKeHJlZgowIDYKMDAwMDAwMDAwMCA2NTUzNSBmIAowMDAwMDAwMDEwIDAwMDAwIG4gCjAwMDAwMDAwNzkgMDAwMDAgbiAKMDAwMDAwMDE3MyAwMDAwMCBuIAowMDAwMDAwMzAxIDAwMDAwIG4gCjAwMDAwMDAzODAgMDAwMDAgbiAKdHJhaWxlcgo8PAogIC9TaXplIDYKICAvUm9vdCAxIDAgUgo+PgpzdGFydHhyZWYKNDkyCiUlRU9G",
            printer_id="d117866d-78de-4459-9077-42d7ea0120e3",
            enterprise_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )
        assert_matches_type(DeviceCommandAddResult, command, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_add_printer(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.commands.with_raw_response.add_printer(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            copy_count=1,
            data="JVBERi0xLjcKCjEgMCBvYmogICUgZW50cnkgcG9pbnQKPDwKICAvVHlwZSAvQ2F0YWxvZwogIC9QYWdlcyAyIDAgUgo+PgplbmRvYmoKCjIgMCBvYmoKPDwKICAvVHlwZSAvUGFnZXMKICAvTWVkaWFCb3ggWyAwIDAgMjAwIDIwMCBdCiAgL0NvdW50IDEKICAvS2lkcyBbIDMgMCBSIF0KPj4KZW5kb2JqCgozIDAgb2JqCjw8CiAgL1R5cGUgL1BhZ2UKICAvUGFyZW50IDIgMCBSCiAgL1Jlc291cmNlcyA8PAogICAgL0ZvbnQgPDwKICAgICAgL0YxIDQgMCBSIAogICAgPj4KICA+PgogIC9Db250ZW50cyA1IDAgUgo+PgplbmRvYmoKCjQgMCBvYmoKPDwKICAvVHlwZSAvRm9udAogIC9TdWJ0eXBlIC9UeXBlMQogIC9CYXNlRm9udCAvVGltZXMtUm9tYW4KPj4KZW5kb2JqCgo1IDAgb2JqICAlIHBhZ2UgY29udGVudAo8PAogIC9MZW5ndGggNDQKPj4Kc3RyZWFtCkJUCjcwIDUwIFRECi9GMSAxMiBUZgooSGVsbG8sIHdvcmxkISkgVGoKRVQKZW5kc3RyZWFtCmVuZG9iagoKeHJlZgowIDYKMDAwMDAwMDAwMCA2NTUzNSBmIAowMDAwMDAwMDEwIDAwMDAwIG4gCjAwMDAwMDAwNzkgMDAwMDAgbiAKMDAwMDAwMDE3MyAwMDAwMCBuIAowMDAwMDAwMzAxIDAwMDAwIG4gCjAwMDAwMDAzODAgMDAwMDAgbiAKdHJhaWxlcgo8PAogIC9TaXplIDYKICAvUm9vdCAxIDAgUgo+PgpzdGFydHhyZWYKNDkyCiUlRU9G",
            printer_id="d117866d-78de-4459-9077-42d7ea0120e3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        command = await response.parse()
        assert_matches_type(DeviceCommandAddResult, command, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_add_printer(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.commands.with_streaming_response.add_printer(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            copy_count=1,
            data="JVBERi0xLjcKCjEgMCBvYmogICUgZW50cnkgcG9pbnQKPDwKICAvVHlwZSAvQ2F0YWxvZwogIC9QYWdlcyAyIDAgUgo+PgplbmRvYmoKCjIgMCBvYmoKPDwKICAvVHlwZSAvUGFnZXMKICAvTWVkaWFCb3ggWyAwIDAgMjAwIDIwMCBdCiAgL0NvdW50IDEKICAvS2lkcyBbIDMgMCBSIF0KPj4KZW5kb2JqCgozIDAgb2JqCjw8CiAgL1R5cGUgL1BhZ2UKICAvUGFyZW50IDIgMCBSCiAgL1Jlc291cmNlcyA8PAogICAgL0ZvbnQgPDwKICAgICAgL0YxIDQgMCBSIAogICAgPj4KICA+PgogIC9Db250ZW50cyA1IDAgUgo+PgplbmRvYmoKCjQgMCBvYmoKPDwKICAvVHlwZSAvRm9udAogIC9TdWJ0eXBlIC9UeXBlMQogIC9CYXNlRm9udCAvVGltZXMtUm9tYW4KPj4KZW5kb2JqCgo1IDAgb2JqICAlIHBhZ2UgY29udGVudAo8PAogIC9MZW5ndGggNDQKPj4Kc3RyZWFtCkJUCjcwIDUwIFRECi9GMSAxMiBUZgooSGVsbG8sIHdvcmxkISkgVGoKRVQKZW5kc3RyZWFtCmVuZG9iagoKeHJlZgowIDYKMDAwMDAwMDAwMCA2NTUzNSBmIAowMDAwMDAwMDEwIDAwMDAwIG4gCjAwMDAwMDAwNzkgMDAwMDAgbiAKMDAwMDAwMDE3MyAwMDAwMCBuIAowMDAwMDAwMzAxIDAwMDAwIG4gCjAwMDAwMDAzODAgMDAwMDAgbiAKdHJhaWxlcgo8PAogIC9TaXplIDYKICAvUm9vdCAxIDAgUgo+PgpzdGFydHhyZWYKNDkyCiUlRU9G",
            printer_id="d117866d-78de-4459-9077-42d7ea0120e3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            command = await response.parse()
            assert_matches_type(DeviceCommandAddResult, command, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_active(self, async_client: AsyncPymews) -> None:
        command = await async_client.api.connector.v1.commands.list_active(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )
        assert_matches_type(DeviceCommandResult, command, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_active(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.commands.with_raw_response.list_active(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        command = await response.parse()
        assert_matches_type(DeviceCommandResult, command, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_active(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.commands.with_streaming_response.list_active(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            command = await response.parse()
            assert_matches_type(DeviceCommandResult, command, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_by_ids(self, async_client: AsyncPymews) -> None:
        command = await async_client.api.connector.v1.commands.list_by_ids(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            command_ids=["aa20961f-6d9e-4b35-ad25-071213530aec"],
        )
        assert_matches_type(DeviceCommandResult, command, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_by_ids_with_all_params(self, async_client: AsyncPymews) -> None:
        command = await async_client.api.connector.v1.commands.list_by_ids(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            command_ids=["aa20961f-6d9e-4b35-ad25-071213530aec"],
            limitation={
                "count": 0,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
        )
        assert_matches_type(DeviceCommandResult, command, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_by_ids(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.commands.with_raw_response.list_by_ids(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            command_ids=["aa20961f-6d9e-4b35-ad25-071213530aec"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        command = await response.parse()
        assert_matches_type(DeviceCommandResult, command, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_by_ids(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.commands.with_streaming_response.list_by_ids(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            command_ids=["aa20961f-6d9e-4b35-ad25-071213530aec"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            command = await response.parse()
            assert_matches_type(DeviceCommandResult, command, path=["response"])

        assert cast(Any, response.is_closed) is True
