# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pymews import Pymews, AsyncPymews
from tests.utils import assert_matches_type
from pymews._utils import parse_datetime
from pymews.types.api.connector.v1 import (
    VoucherCodeResult,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVoucherCodes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Pymews) -> None:
        voucher_code = client.api.connector.v1.voucher_codes.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            voucher_ids=["fe568bbd-1ecb-4bb2-bf77-96c3698de20d"],
        )
        assert_matches_type(VoucherCodeResult, voucher_code, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Pymews) -> None:
        voucher_code = client.api.connector.v1.voucher_codes.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            voucher_ids=["fe568bbd-1ecb-4bb2-bf77-96c3698de20d"],
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            updated_utc={
                "end_utc": parse_datetime("2023-10-17T00:00:00Z"),
                "start_utc": parse_datetime("2023-10-10T00:00:00Z"),
            },
            voucher_code_ids=["8c364829-c7ae-4972-b67f-93ea704d7228", "dc9d3488-7fc4-4fc9-a524-14e6504d8734"],
        )
        assert_matches_type(VoucherCodeResult, voucher_code, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Pymews) -> None:
        response = client.api.connector.v1.voucher_codes.with_raw_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            voucher_ids=["fe568bbd-1ecb-4bb2-bf77-96c3698de20d"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voucher_code = response.parse()
        assert_matches_type(VoucherCodeResult, voucher_code, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Pymews) -> None:
        with client.api.connector.v1.voucher_codes.with_streaming_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            voucher_ids=["fe568bbd-1ecb-4bb2-bf77-96c3698de20d"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voucher_code = response.parse()
            assert_matches_type(VoucherCodeResult, voucher_code, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Pymews) -> None:
        voucher_code = client.api.connector.v1.voucher_codes.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            voucher_code_ids=["8c364829-c7ae-4972-b67f-93ea704d7228", "dc9d3488-7fc4-4fc9-a524-14e6504d8734"],
        )
        assert_matches_type(object, voucher_code, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_delete_with_all_params(self, client: Pymews) -> None:
        voucher_code = client.api.connector.v1.voucher_codes.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            voucher_code_ids=["8c364829-c7ae-4972-b67f-93ea704d7228", "dc9d3488-7fc4-4fc9-a524-14e6504d8734"],
            enterprise_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )
        assert_matches_type(object, voucher_code, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Pymews) -> None:
        response = client.api.connector.v1.voucher_codes.with_raw_response.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            voucher_code_ids=["8c364829-c7ae-4972-b67f-93ea704d7228", "dc9d3488-7fc4-4fc9-a524-14e6504d8734"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voucher_code = response.parse()
        assert_matches_type(object, voucher_code, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Pymews) -> None:
        with client.api.connector.v1.voucher_codes.with_streaming_response.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            voucher_code_ids=["8c364829-c7ae-4972-b67f-93ea704d7228", "dc9d3488-7fc4-4fc9-a524-14e6504d8734"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voucher_code = response.parse()
            assert_matches_type(object, voucher_code, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_add(self, client: Pymews) -> None:
        voucher_code = client.api.connector.v1.voucher_codes.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            voucher_code_parameters=[
                {
                    "value": "0E5856B0A73E62B7E446",
                    "voucher_id": "8c364829-c7ae-4972-b67f-93ea704d7228",
                },
                {
                    "value": "021D047E42A5FD522CBA",
                    "voucher_id": "dc9d3488-7fc4-4fc9-a524-14e6504d8734",
                },
            ],
        )
        assert_matches_type(VoucherCodeResult, voucher_code, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_add_with_all_params(self, client: Pymews) -> None:
        voucher_code = client.api.connector.v1.voucher_codes.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            voucher_code_parameters=[
                {
                    "value": "0E5856B0A73E62B7E446",
                    "voucher_id": "8c364829-c7ae-4972-b67f-93ea704d7228",
                    "validity_end_utc": parse_datetime("2023-10-09T22:00:00Z"),
                    "validity_start_utc": parse_datetime("2023-10-09T22:00:00Z"),
                },
                {
                    "value": "021D047E42A5FD522CBA",
                    "voucher_id": "dc9d3488-7fc4-4fc9-a524-14e6504d8734",
                    "validity_end_utc": parse_datetime("2023-10-09T22:00:00Z"),
                    "validity_start_utc": parse_datetime("2023-10-09T22:00:00Z"),
                },
            ],
            enterprise_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )
        assert_matches_type(VoucherCodeResult, voucher_code, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_add(self, client: Pymews) -> None:
        response = client.api.connector.v1.voucher_codes.with_raw_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            voucher_code_parameters=[
                {
                    "value": "0E5856B0A73E62B7E446",
                    "voucher_id": "8c364829-c7ae-4972-b67f-93ea704d7228",
                },
                {
                    "value": "021D047E42A5FD522CBA",
                    "voucher_id": "dc9d3488-7fc4-4fc9-a524-14e6504d8734",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voucher_code = response.parse()
        assert_matches_type(VoucherCodeResult, voucher_code, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_add(self, client: Pymews) -> None:
        with client.api.connector.v1.voucher_codes.with_streaming_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            voucher_code_parameters=[
                {
                    "value": "0E5856B0A73E62B7E446",
                    "voucher_id": "8c364829-c7ae-4972-b67f-93ea704d7228",
                },
                {
                    "value": "021D047E42A5FD522CBA",
                    "voucher_id": "dc9d3488-7fc4-4fc9-a524-14e6504d8734",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voucher_code = response.parse()
            assert_matches_type(VoucherCodeResult, voucher_code, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncVoucherCodes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncPymews) -> None:
        voucher_code = await async_client.api.connector.v1.voucher_codes.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            voucher_ids=["fe568bbd-1ecb-4bb2-bf77-96c3698de20d"],
        )
        assert_matches_type(VoucherCodeResult, voucher_code, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPymews) -> None:
        voucher_code = await async_client.api.connector.v1.voucher_codes.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            voucher_ids=["fe568bbd-1ecb-4bb2-bf77-96c3698de20d"],
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            updated_utc={
                "end_utc": parse_datetime("2023-10-17T00:00:00Z"),
                "start_utc": parse_datetime("2023-10-10T00:00:00Z"),
            },
            voucher_code_ids=["8c364829-c7ae-4972-b67f-93ea704d7228", "dc9d3488-7fc4-4fc9-a524-14e6504d8734"],
        )
        assert_matches_type(VoucherCodeResult, voucher_code, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.voucher_codes.with_raw_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            voucher_ids=["fe568bbd-1ecb-4bb2-bf77-96c3698de20d"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voucher_code = await response.parse()
        assert_matches_type(VoucherCodeResult, voucher_code, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.voucher_codes.with_streaming_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            voucher_ids=["fe568bbd-1ecb-4bb2-bf77-96c3698de20d"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voucher_code = await response.parse()
            assert_matches_type(VoucherCodeResult, voucher_code, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncPymews) -> None:
        voucher_code = await async_client.api.connector.v1.voucher_codes.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            voucher_code_ids=["8c364829-c7ae-4972-b67f-93ea704d7228", "dc9d3488-7fc4-4fc9-a524-14e6504d8734"],
        )
        assert_matches_type(object, voucher_code, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncPymews) -> None:
        voucher_code = await async_client.api.connector.v1.voucher_codes.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            voucher_code_ids=["8c364829-c7ae-4972-b67f-93ea704d7228", "dc9d3488-7fc4-4fc9-a524-14e6504d8734"],
            enterprise_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )
        assert_matches_type(object, voucher_code, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.voucher_codes.with_raw_response.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            voucher_code_ids=["8c364829-c7ae-4972-b67f-93ea704d7228", "dc9d3488-7fc4-4fc9-a524-14e6504d8734"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voucher_code = await response.parse()
        assert_matches_type(object, voucher_code, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.voucher_codes.with_streaming_response.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            voucher_code_ids=["8c364829-c7ae-4972-b67f-93ea704d7228", "dc9d3488-7fc4-4fc9-a524-14e6504d8734"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voucher_code = await response.parse()
            assert_matches_type(object, voucher_code, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_add(self, async_client: AsyncPymews) -> None:
        voucher_code = await async_client.api.connector.v1.voucher_codes.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            voucher_code_parameters=[
                {
                    "value": "0E5856B0A73E62B7E446",
                    "voucher_id": "8c364829-c7ae-4972-b67f-93ea704d7228",
                },
                {
                    "value": "021D047E42A5FD522CBA",
                    "voucher_id": "dc9d3488-7fc4-4fc9-a524-14e6504d8734",
                },
            ],
        )
        assert_matches_type(VoucherCodeResult, voucher_code, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_add_with_all_params(self, async_client: AsyncPymews) -> None:
        voucher_code = await async_client.api.connector.v1.voucher_codes.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            voucher_code_parameters=[
                {
                    "value": "0E5856B0A73E62B7E446",
                    "voucher_id": "8c364829-c7ae-4972-b67f-93ea704d7228",
                    "validity_end_utc": parse_datetime("2023-10-09T22:00:00Z"),
                    "validity_start_utc": parse_datetime("2023-10-09T22:00:00Z"),
                },
                {
                    "value": "021D047E42A5FD522CBA",
                    "voucher_id": "dc9d3488-7fc4-4fc9-a524-14e6504d8734",
                    "validity_end_utc": parse_datetime("2023-10-09T22:00:00Z"),
                    "validity_start_utc": parse_datetime("2023-10-09T22:00:00Z"),
                },
            ],
            enterprise_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )
        assert_matches_type(VoucherCodeResult, voucher_code, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.voucher_codes.with_raw_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            voucher_code_parameters=[
                {
                    "value": "0E5856B0A73E62B7E446",
                    "voucher_id": "8c364829-c7ae-4972-b67f-93ea704d7228",
                },
                {
                    "value": "021D047E42A5FD522CBA",
                    "voucher_id": "dc9d3488-7fc4-4fc9-a524-14e6504d8734",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voucher_code = await response.parse()
        assert_matches_type(VoucherCodeResult, voucher_code, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.voucher_codes.with_streaming_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            voucher_code_parameters=[
                {
                    "value": "0E5856B0A73E62B7E446",
                    "voucher_id": "8c364829-c7ae-4972-b67f-93ea704d7228",
                },
                {
                    "value": "021D047E42A5FD522CBA",
                    "voucher_id": "dc9d3488-7fc4-4fc9-a524-14e6504d8734",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voucher_code = await response.parse()
            assert_matches_type(VoucherCodeResult, voucher_code, path=["response"])

        assert cast(Any, response.is_closed) is True
