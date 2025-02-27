# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pymews import Pymews, AsyncPymews
from tests.utils import assert_matches_type
from pymews._utils import parse_datetime
from pymews.types.api.connector.v1 import (
    RoutingRuleResult,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRoutingRules:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Pymews) -> None:
        routing_rule = client.api.connector.v1.routing_rules.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            routing_rule_updates=[
                {"routing_rule_id": "ff785b22-5422-4d1d-87f4-af2e00b3dfda"},
                {"routing_rule_id": "d98c9611-0006-4691-a835-af2e00b170c4"},
            ],
        )
        assert_matches_type(RoutingRuleResult, routing_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Pymews) -> None:
        response = client.api.connector.v1.routing_rules.with_raw_response.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            routing_rule_updates=[
                {"routing_rule_id": "ff785b22-5422-4d1d-87f4-af2e00b3dfda"},
                {"routing_rule_id": "d98c9611-0006-4691-a835-af2e00b170c4"},
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routing_rule = response.parse()
        assert_matches_type(RoutingRuleResult, routing_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Pymews) -> None:
        with client.api.connector.v1.routing_rules.with_streaming_response.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            routing_rule_updates=[
                {"routing_rule_id": "ff785b22-5422-4d1d-87f4-af2e00b3dfda"},
                {"routing_rule_id": "d98c9611-0006-4691-a835-af2e00b170c4"},
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routing_rule = response.parse()
            assert_matches_type(RoutingRuleResult, routing_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Pymews) -> None:
        routing_rule = client.api.connector.v1.routing_rules.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )
        assert_matches_type(RoutingRuleResult, routing_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Pymews) -> None:
        routing_rule = client.api.connector.v1.routing_rules.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            company_ids=["cd441e1a-6f19-4960-887a-af2a00d5d5f8", "ddc23f8d-131d-44d6-b150-af2a00d5d5f8"],
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            routing_rule_ids=["ff785b22-5422-4d1d-87f4-af2e00b3dfda", "d98c9611-0006-4691-a835-af2e00b170c4"],
            updated_utc={
                "end_utc": parse_datetime("2023-10-31T00:00:00Z"),
                "start_utc": parse_datetime("2023-10-01T00:00:00Z"),
            },
        )
        assert_matches_type(RoutingRuleResult, routing_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Pymews) -> None:
        response = client.api.connector.v1.routing_rules.with_raw_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routing_rule = response.parse()
        assert_matches_type(RoutingRuleResult, routing_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Pymews) -> None:
        with client.api.connector.v1.routing_rules.with_streaming_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routing_rule = response.parse()
            assert_matches_type(RoutingRuleResult, routing_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Pymews) -> None:
        routing_rule = client.api.connector.v1.routing_rules.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            routing_rule_ids=["ff785b22-5422-4d1d-87f4-af2e00b3dfda", "d98c9611-0006-4691-a835-af2e00b170c4"],
        )
        assert_matches_type(object, routing_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Pymews) -> None:
        response = client.api.connector.v1.routing_rules.with_raw_response.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            routing_rule_ids=["ff785b22-5422-4d1d-87f4-af2e00b3dfda", "d98c9611-0006-4691-a835-af2e00b170c4"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routing_rule = response.parse()
        assert_matches_type(object, routing_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Pymews) -> None:
        with client.api.connector.v1.routing_rules.with_streaming_response.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            routing_rule_ids=["ff785b22-5422-4d1d-87f4-af2e00b3dfda", "d98c9611-0006-4691-a835-af2e00b170c4"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routing_rule = response.parse()
            assert_matches_type(object, routing_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_add(self, client: Pymews) -> None:
        routing_rule = client.api.connector.v1.routing_rules.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            routing_rules=[
                {
                    "applicability": "Always",
                    "company_id": "cd441e1a-6f19-4960-887a-af2a00d5d5f8",
                    "company_relation": "PartnerCompany",
                    "route_type": "AllStayItems",
                    "service_id": "0907a1b4-ef7a-4aa8-b8a1-af2a00d5ca22",
                },
                {
                    "applicability": "Always",
                    "company_id": "ddc23f8d-131d-44d6-b150-af2a00d5d5f8",
                    "company_relation": "PartnerCompany",
                    "route_type": "AllStayItems",
                    "service_id": "0907a1b4-ef7a-4aa8-b8a1-af2a00d5ca22",
                },
            ],
        )
        assert_matches_type(RoutingRuleResult, routing_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_add(self, client: Pymews) -> None:
        response = client.api.connector.v1.routing_rules.with_raw_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            routing_rules=[
                {
                    "applicability": "Always",
                    "company_id": "cd441e1a-6f19-4960-887a-af2a00d5d5f8",
                    "company_relation": "PartnerCompany",
                    "route_type": "AllStayItems",
                    "service_id": "0907a1b4-ef7a-4aa8-b8a1-af2a00d5ca22",
                },
                {
                    "applicability": "Always",
                    "company_id": "ddc23f8d-131d-44d6-b150-af2a00d5d5f8",
                    "company_relation": "PartnerCompany",
                    "route_type": "AllStayItems",
                    "service_id": "0907a1b4-ef7a-4aa8-b8a1-af2a00d5ca22",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routing_rule = response.parse()
        assert_matches_type(RoutingRuleResult, routing_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_add(self, client: Pymews) -> None:
        with client.api.connector.v1.routing_rules.with_streaming_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            routing_rules=[
                {
                    "applicability": "Always",
                    "company_id": "cd441e1a-6f19-4960-887a-af2a00d5d5f8",
                    "company_relation": "PartnerCompany",
                    "route_type": "AllStayItems",
                    "service_id": "0907a1b4-ef7a-4aa8-b8a1-af2a00d5ca22",
                },
                {
                    "applicability": "Always",
                    "company_id": "ddc23f8d-131d-44d6-b150-af2a00d5d5f8",
                    "company_relation": "PartnerCompany",
                    "route_type": "AllStayItems",
                    "service_id": "0907a1b4-ef7a-4aa8-b8a1-af2a00d5ca22",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routing_rule = response.parse()
            assert_matches_type(RoutingRuleResult, routing_rule, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRoutingRules:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncPymews) -> None:
        routing_rule = await async_client.api.connector.v1.routing_rules.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            routing_rule_updates=[
                {"routing_rule_id": "ff785b22-5422-4d1d-87f4-af2e00b3dfda"},
                {"routing_rule_id": "d98c9611-0006-4691-a835-af2e00b170c4"},
            ],
        )
        assert_matches_type(RoutingRuleResult, routing_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.routing_rules.with_raw_response.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            routing_rule_updates=[
                {"routing_rule_id": "ff785b22-5422-4d1d-87f4-af2e00b3dfda"},
                {"routing_rule_id": "d98c9611-0006-4691-a835-af2e00b170c4"},
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routing_rule = await response.parse()
        assert_matches_type(RoutingRuleResult, routing_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.routing_rules.with_streaming_response.update(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            routing_rule_updates=[
                {"routing_rule_id": "ff785b22-5422-4d1d-87f4-af2e00b3dfda"},
                {"routing_rule_id": "d98c9611-0006-4691-a835-af2e00b170c4"},
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routing_rule = await response.parse()
            assert_matches_type(RoutingRuleResult, routing_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncPymews) -> None:
        routing_rule = await async_client.api.connector.v1.routing_rules.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )
        assert_matches_type(RoutingRuleResult, routing_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPymews) -> None:
        routing_rule = await async_client.api.connector.v1.routing_rules.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            company_ids=["cd441e1a-6f19-4960-887a-af2a00d5d5f8", "ddc23f8d-131d-44d6-b150-af2a00d5d5f8"],
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            routing_rule_ids=["ff785b22-5422-4d1d-87f4-af2e00b3dfda", "d98c9611-0006-4691-a835-af2e00b170c4"],
            updated_utc={
                "end_utc": parse_datetime("2023-10-31T00:00:00Z"),
                "start_utc": parse_datetime("2023-10-01T00:00:00Z"),
            },
        )
        assert_matches_type(RoutingRuleResult, routing_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.routing_rules.with_raw_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routing_rule = await response.parse()
        assert_matches_type(RoutingRuleResult, routing_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.routing_rules.with_streaming_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routing_rule = await response.parse()
            assert_matches_type(RoutingRuleResult, routing_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncPymews) -> None:
        routing_rule = await async_client.api.connector.v1.routing_rules.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            routing_rule_ids=["ff785b22-5422-4d1d-87f4-af2e00b3dfda", "d98c9611-0006-4691-a835-af2e00b170c4"],
        )
        assert_matches_type(object, routing_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.routing_rules.with_raw_response.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            routing_rule_ids=["ff785b22-5422-4d1d-87f4-af2e00b3dfda", "d98c9611-0006-4691-a835-af2e00b170c4"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routing_rule = await response.parse()
        assert_matches_type(object, routing_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.routing_rules.with_streaming_response.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            routing_rule_ids=["ff785b22-5422-4d1d-87f4-af2e00b3dfda", "d98c9611-0006-4691-a835-af2e00b170c4"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routing_rule = await response.parse()
            assert_matches_type(object, routing_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_add(self, async_client: AsyncPymews) -> None:
        routing_rule = await async_client.api.connector.v1.routing_rules.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            routing_rules=[
                {
                    "applicability": "Always",
                    "company_id": "cd441e1a-6f19-4960-887a-af2a00d5d5f8",
                    "company_relation": "PartnerCompany",
                    "route_type": "AllStayItems",
                    "service_id": "0907a1b4-ef7a-4aa8-b8a1-af2a00d5ca22",
                },
                {
                    "applicability": "Always",
                    "company_id": "ddc23f8d-131d-44d6-b150-af2a00d5d5f8",
                    "company_relation": "PartnerCompany",
                    "route_type": "AllStayItems",
                    "service_id": "0907a1b4-ef7a-4aa8-b8a1-af2a00d5ca22",
                },
            ],
        )
        assert_matches_type(RoutingRuleResult, routing_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.routing_rules.with_raw_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            routing_rules=[
                {
                    "applicability": "Always",
                    "company_id": "cd441e1a-6f19-4960-887a-af2a00d5d5f8",
                    "company_relation": "PartnerCompany",
                    "route_type": "AllStayItems",
                    "service_id": "0907a1b4-ef7a-4aa8-b8a1-af2a00d5ca22",
                },
                {
                    "applicability": "Always",
                    "company_id": "ddc23f8d-131d-44d6-b150-af2a00d5d5f8",
                    "company_relation": "PartnerCompany",
                    "route_type": "AllStayItems",
                    "service_id": "0907a1b4-ef7a-4aa8-b8a1-af2a00d5ca22",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routing_rule = await response.parse()
        assert_matches_type(RoutingRuleResult, routing_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.routing_rules.with_streaming_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            routing_rules=[
                {
                    "applicability": "Always",
                    "company_id": "cd441e1a-6f19-4960-887a-af2a00d5d5f8",
                    "company_relation": "PartnerCompany",
                    "route_type": "AllStayItems",
                    "service_id": "0907a1b4-ef7a-4aa8-b8a1-af2a00d5ca22",
                },
                {
                    "applicability": "Always",
                    "company_id": "ddc23f8d-131d-44d6-b150-af2a00d5d5f8",
                    "company_relation": "PartnerCompany",
                    "route_type": "AllStayItems",
                    "service_id": "0907a1b4-ef7a-4aa8-b8a1-af2a00d5ca22",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routing_rule = await response.parse()
            assert_matches_type(RoutingRuleResult, routing_rule, path=["response"])

        assert cast(Any, response.is_closed) is True
