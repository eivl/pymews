# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pymews import Pymews, AsyncPymews
from tests.utils import assert_matches_type
from pymews._utils import parse_datetime
from pymews.types.api.connector.v1 import (
    RestrictionAddResponse,
    RestrictionListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRestrictions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Pymews) -> None:
        restriction = client.api.connector.v1.restrictions.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            service_ids=["bd26d8db-86da-4f96-9efc-e5a4654a4a94"],
        )
        assert_matches_type(RestrictionListResponse, restriction, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Pymews) -> None:
        restriction = client.api.connector.v1.restrictions.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            service_ids=["bd26d8db-86da-4f96-9efc-e5a4654a4a94"],
            base_rate_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            colliding_utc={
                "end_utc": parse_datetime("2020-02-20T00:00:00Z"),
                "start_utc": parse_datetime("2020-02-15T00:00:00Z"),
            },
            created_utc={
                "end_utc": parse_datetime("2020-02-15T00:00:00Z"),
                "start_utc": parse_datetime("2020-02-05T00:00:00Z"),
            },
            end_utc="EndUtc",
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            exact_rate_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            origin="Integration",
            rate_ids=["ed4b660b-19d0-434b-9360-a4de2ea42eda"],
            resource_category_ids=["34c29e73-c8db-4e93-b51b-981e42655e03"],
            restriction_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            start_utc="StartUtc",
            time_filter="TimeFilter",
            updated_utc={
                "end_utc": parse_datetime("2020-02-15T00:00:00Z"),
                "start_utc": parse_datetime("2020-02-05T00:00:00Z"),
            },
        )
        assert_matches_type(RestrictionListResponse, restriction, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Pymews) -> None:
        response = client.api.connector.v1.restrictions.with_raw_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            service_ids=["bd26d8db-86da-4f96-9efc-e5a4654a4a94"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        restriction = response.parse()
        assert_matches_type(RestrictionListResponse, restriction, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Pymews) -> None:
        with client.api.connector.v1.restrictions.with_streaming_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            service_ids=["bd26d8db-86da-4f96-9efc-e5a4654a4a94"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            restriction = response.parse()
            assert_matches_type(RestrictionListResponse, restriction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Pymews) -> None:
        restriction = client.api.connector.v1.restrictions.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            restriction_ids=["af4949ce-c061-4f27-89f9-5a6a9ef725a7", "e2f8aa29-0c09-4097-801c-7888c9fb57ae"],
        )
        assert_matches_type(object, restriction, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Pymews) -> None:
        response = client.api.connector.v1.restrictions.with_raw_response.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            restriction_ids=["af4949ce-c061-4f27-89f9-5a6a9ef725a7", "e2f8aa29-0c09-4097-801c-7888c9fb57ae"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        restriction = response.parse()
        assert_matches_type(object, restriction, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Pymews) -> None:
        with client.api.connector.v1.restrictions.with_streaming_response.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            restriction_ids=["af4949ce-c061-4f27-89f9-5a6a9ef725a7", "e2f8aa29-0c09-4097-801c-7888c9fb57ae"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            restriction = response.parse()
            assert_matches_type(object, restriction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_add(self, client: Pymews) -> None:
        restriction = client.api.connector.v1.restrictions.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="x",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            restrictions=[{"conditions": {"type": "Start"}}, {"conditions": {"type": "Start"}}],
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
        )
        assert_matches_type(RestrictionAddResponse, restriction, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_add(self, client: Pymews) -> None:
        response = client.api.connector.v1.restrictions.with_raw_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="x",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            restrictions=[{"conditions": {"type": "Start"}}, {"conditions": {"type": "Start"}}],
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        restriction = response.parse()
        assert_matches_type(RestrictionAddResponse, restriction, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_add(self, client: Pymews) -> None:
        with client.api.connector.v1.restrictions.with_streaming_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="x",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            restrictions=[{"conditions": {"type": "Start"}}, {"conditions": {"type": "Start"}}],
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            restriction = response.parse()
            assert_matches_type(RestrictionAddResponse, restriction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_clear(self, client: Pymews) -> None:
        restriction = client.api.connector.v1.restrictions.clear(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            data=[
                {
                    "days": {
                        "friday": True,
                        "monday": False,
                        "saturday": True,
                        "sunday": True,
                        "thursday": False,
                        "tuesday": False,
                        "wednesday": False,
                    },
                    "type": "Start",
                },
                {
                    "days": {
                        "friday": True,
                        "monday": True,
                        "saturday": False,
                        "sunday": False,
                        "thursday": True,
                        "tuesday": True,
                        "wednesday": True,
                    },
                    "type": "Start",
                },
            ],
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
        )
        assert_matches_type(object, restriction, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_clear(self, client: Pymews) -> None:
        response = client.api.connector.v1.restrictions.with_raw_response.clear(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            data=[
                {
                    "days": {
                        "friday": True,
                        "monday": False,
                        "saturday": True,
                        "sunday": True,
                        "thursday": False,
                        "tuesday": False,
                        "wednesday": False,
                    },
                    "type": "Start",
                },
                {
                    "days": {
                        "friday": True,
                        "monday": True,
                        "saturday": False,
                        "sunday": False,
                        "thursday": True,
                        "tuesday": True,
                        "wednesday": True,
                    },
                    "type": "Start",
                },
            ],
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        restriction = response.parse()
        assert_matches_type(object, restriction, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_clear(self, client: Pymews) -> None:
        with client.api.connector.v1.restrictions.with_streaming_response.clear(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            data=[
                {
                    "days": {
                        "friday": True,
                        "monday": False,
                        "saturday": True,
                        "sunday": True,
                        "thursday": False,
                        "tuesday": False,
                        "wednesday": False,
                    },
                    "type": "Start",
                },
                {
                    "days": {
                        "friday": True,
                        "monday": True,
                        "saturday": False,
                        "sunday": False,
                        "thursday": True,
                        "tuesday": True,
                        "wednesday": True,
                    },
                    "type": "Start",
                },
            ],
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            restriction = response.parse()
            assert_matches_type(object, restriction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_set(self, client: Pymews) -> None:
        restriction = client.api.connector.v1.restrictions.set(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            data=[
                {
                    "days": {
                        "friday": True,
                        "monday": False,
                        "saturday": True,
                        "sunday": True,
                        "thursday": False,
                        "tuesday": False,
                        "wednesday": False,
                    },
                    "type": "Start",
                },
                {
                    "days": {
                        "friday": True,
                        "monday": True,
                        "saturday": False,
                        "sunday": False,
                        "thursday": True,
                        "tuesday": True,
                        "wednesday": True,
                    },
                    "type": "Start",
                },
            ],
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
        )
        assert_matches_type(object, restriction, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_set(self, client: Pymews) -> None:
        response = client.api.connector.v1.restrictions.with_raw_response.set(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            data=[
                {
                    "days": {
                        "friday": True,
                        "monday": False,
                        "saturday": True,
                        "sunday": True,
                        "thursday": False,
                        "tuesday": False,
                        "wednesday": False,
                    },
                    "type": "Start",
                },
                {
                    "days": {
                        "friday": True,
                        "monday": True,
                        "saturday": False,
                        "sunday": False,
                        "thursday": True,
                        "tuesday": True,
                        "wednesday": True,
                    },
                    "type": "Start",
                },
            ],
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        restriction = response.parse()
        assert_matches_type(object, restriction, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_set(self, client: Pymews) -> None:
        with client.api.connector.v1.restrictions.with_streaming_response.set(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            data=[
                {
                    "days": {
                        "friday": True,
                        "monday": False,
                        "saturday": True,
                        "sunday": True,
                        "thursday": False,
                        "tuesday": False,
                        "wednesday": False,
                    },
                    "type": "Start",
                },
                {
                    "days": {
                        "friday": True,
                        "monday": True,
                        "saturday": False,
                        "sunday": False,
                        "thursday": True,
                        "tuesday": True,
                        "wednesday": True,
                    },
                    "type": "Start",
                },
            ],
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            restriction = response.parse()
            assert_matches_type(object, restriction, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRestrictions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncPymews) -> None:
        restriction = await async_client.api.connector.v1.restrictions.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            service_ids=["bd26d8db-86da-4f96-9efc-e5a4654a4a94"],
        )
        assert_matches_type(RestrictionListResponse, restriction, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPymews) -> None:
        restriction = await async_client.api.connector.v1.restrictions.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={
                "count": 10,
                "cursor": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            service_ids=["bd26d8db-86da-4f96-9efc-e5a4654a4a94"],
            base_rate_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            colliding_utc={
                "end_utc": parse_datetime("2020-02-20T00:00:00Z"),
                "start_utc": parse_datetime("2020-02-15T00:00:00Z"),
            },
            created_utc={
                "end_utc": parse_datetime("2020-02-15T00:00:00Z"),
                "start_utc": parse_datetime("2020-02-05T00:00:00Z"),
            },
            end_utc="EndUtc",
            enterprise_ids=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "4d0201db-36f5-428b-8d11-4f0a65e960cc"],
            exact_rate_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            origin="Integration",
            rate_ids=["ed4b660b-19d0-434b-9360-a4de2ea42eda"],
            resource_category_ids=["34c29e73-c8db-4e93-b51b-981e42655e03"],
            restriction_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            start_utc="StartUtc",
            time_filter="TimeFilter",
            updated_utc={
                "end_utc": parse_datetime("2020-02-15T00:00:00Z"),
                "start_utc": parse_datetime("2020-02-05T00:00:00Z"),
            },
        )
        assert_matches_type(RestrictionListResponse, restriction, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.restrictions.with_raw_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            service_ids=["bd26d8db-86da-4f96-9efc-e5a4654a4a94"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        restriction = await response.parse()
        assert_matches_type(RestrictionListResponse, restriction, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.restrictions.with_streaming_response.list(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            limitation={"count": 10},
            service_ids=["bd26d8db-86da-4f96-9efc-e5a4654a4a94"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            restriction = await response.parse()
            assert_matches_type(RestrictionListResponse, restriction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncPymews) -> None:
        restriction = await async_client.api.connector.v1.restrictions.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            restriction_ids=["af4949ce-c061-4f27-89f9-5a6a9ef725a7", "e2f8aa29-0c09-4097-801c-7888c9fb57ae"],
        )
        assert_matches_type(object, restriction, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.restrictions.with_raw_response.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            restriction_ids=["af4949ce-c061-4f27-89f9-5a6a9ef725a7", "e2f8aa29-0c09-4097-801c-7888c9fb57ae"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        restriction = await response.parse()
        assert_matches_type(object, restriction, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.restrictions.with_streaming_response.delete(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            restriction_ids=["af4949ce-c061-4f27-89f9-5a6a9ef725a7", "e2f8aa29-0c09-4097-801c-7888c9fb57ae"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            restriction = await response.parse()
            assert_matches_type(object, restriction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_add(self, async_client: AsyncPymews) -> None:
        restriction = await async_client.api.connector.v1.restrictions.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="x",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            restrictions=[{"conditions": {"type": "Start"}}, {"conditions": {"type": "Start"}}],
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
        )
        assert_matches_type(RestrictionAddResponse, restriction, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.restrictions.with_raw_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="x",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            restrictions=[{"conditions": {"type": "Start"}}, {"conditions": {"type": "Start"}}],
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        restriction = await response.parse()
        assert_matches_type(RestrictionAddResponse, restriction, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.restrictions.with_streaming_response.add(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="x",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            restrictions=[{"conditions": {"type": "Start"}}, {"conditions": {"type": "Start"}}],
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            restriction = await response.parse()
            assert_matches_type(RestrictionAddResponse, restriction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_clear(self, async_client: AsyncPymews) -> None:
        restriction = await async_client.api.connector.v1.restrictions.clear(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            data=[
                {
                    "days": {
                        "friday": True,
                        "monday": False,
                        "saturday": True,
                        "sunday": True,
                        "thursday": False,
                        "tuesday": False,
                        "wednesday": False,
                    },
                    "type": "Start",
                },
                {
                    "days": {
                        "friday": True,
                        "monday": True,
                        "saturday": False,
                        "sunday": False,
                        "thursday": True,
                        "tuesday": True,
                        "wednesday": True,
                    },
                    "type": "Start",
                },
            ],
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
        )
        assert_matches_type(object, restriction, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_clear(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.restrictions.with_raw_response.clear(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            data=[
                {
                    "days": {
                        "friday": True,
                        "monday": False,
                        "saturday": True,
                        "sunday": True,
                        "thursday": False,
                        "tuesday": False,
                        "wednesday": False,
                    },
                    "type": "Start",
                },
                {
                    "days": {
                        "friday": True,
                        "monday": True,
                        "saturday": False,
                        "sunday": False,
                        "thursday": True,
                        "tuesday": True,
                        "wednesday": True,
                    },
                    "type": "Start",
                },
            ],
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        restriction = await response.parse()
        assert_matches_type(object, restriction, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_clear(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.restrictions.with_streaming_response.clear(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            data=[
                {
                    "days": {
                        "friday": True,
                        "monday": False,
                        "saturday": True,
                        "sunday": True,
                        "thursday": False,
                        "tuesday": False,
                        "wednesday": False,
                    },
                    "type": "Start",
                },
                {
                    "days": {
                        "friday": True,
                        "monday": True,
                        "saturday": False,
                        "sunday": False,
                        "thursday": True,
                        "tuesday": True,
                        "wednesday": True,
                    },
                    "type": "Start",
                },
            ],
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            restriction = await response.parse()
            assert_matches_type(object, restriction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_set(self, async_client: AsyncPymews) -> None:
        restriction = await async_client.api.connector.v1.restrictions.set(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            data=[
                {
                    "days": {
                        "friday": True,
                        "monday": False,
                        "saturday": True,
                        "sunday": True,
                        "thursday": False,
                        "tuesday": False,
                        "wednesday": False,
                    },
                    "type": "Start",
                },
                {
                    "days": {
                        "friday": True,
                        "monday": True,
                        "saturday": False,
                        "sunday": False,
                        "thursday": True,
                        "tuesday": True,
                        "wednesday": True,
                    },
                    "type": "Start",
                },
            ],
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
        )
        assert_matches_type(object, restriction, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_set(self, async_client: AsyncPymews) -> None:
        response = await async_client.api.connector.v1.restrictions.with_raw_response.set(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            data=[
                {
                    "days": {
                        "friday": True,
                        "monday": False,
                        "saturday": True,
                        "sunday": True,
                        "thursday": False,
                        "tuesday": False,
                        "wednesday": False,
                    },
                    "type": "Start",
                },
                {
                    "days": {
                        "friday": True,
                        "monday": True,
                        "saturday": False,
                        "sunday": False,
                        "thursday": True,
                        "tuesday": True,
                        "wednesday": True,
                    },
                    "type": "Start",
                },
            ],
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        restriction = await response.parse()
        assert_matches_type(object, restriction, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_set(self, async_client: AsyncPymews) -> None:
        async with async_client.api.connector.v1.restrictions.with_streaming_response.set(
            access_token="C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
            client="Sample Client 1.0.0",
            client_token="E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
            data=[
                {
                    "days": {
                        "friday": True,
                        "monday": False,
                        "saturday": True,
                        "sunday": True,
                        "thursday": False,
                        "tuesday": False,
                        "wednesday": False,
                    },
                    "type": "Start",
                },
                {
                    "days": {
                        "friday": True,
                        "monday": True,
                        "saturday": False,
                        "sunday": False,
                        "thursday": True,
                        "tuesday": True,
                        "wednesday": True,
                    },
                    "type": "Start",
                },
            ],
            service_id="bd26d8db-86da-4f96-9efc-e5a4654a4a94",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            restriction = await response.parse()
            assert_matches_type(object, restriction, path=["response"])

        assert cast(Any, response.is_closed) is True
