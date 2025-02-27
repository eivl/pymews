# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.api.connector.v1 import (
    routing_rule_add_params,
    routing_rule_list_params,
    routing_rule_delete_params,
    routing_rule_update_params,
)
from .....types.api.connector.v1.routing_rule_result import RoutingRuleResult

__all__ = ["RoutingRulesResource", "AsyncRoutingRulesResource"]


class RoutingRulesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RoutingRulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return RoutingRulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RoutingRulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return RoutingRulesResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        routing_rule_updates: Iterable[routing_rule_update_params.RoutingRuleUpdate],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RoutingRuleResult:
        """
        Updates routing rules.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          routing_rule_updates: Collection of Routing rules to be updated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/routingRules/update",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "routing_rule_updates": routing_rule_updates,
                },
                routing_rule_update_params.RoutingRuleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoutingRuleResult,
        )

    def list(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: routing_rule_list_params.Limitation,
        company_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        routing_rule_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[routing_rule_list_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RoutingRuleResult:
        """Returns all routing rules.

        Note this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          company_ids: Unique identifier of the
              [Company](https://mews-systems.gitbook.io/connector-api/operations/companies/#company).

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          routing_rule_ids: Unique identifier of the
              [Routing rule](https://mews-systems.gitbook.io/connector-api/operations/routingrules/#routing-rule).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/routingRules/getAll",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "company_ids": company_ids,
                    "enterprise_ids": enterprise_ids,
                    "routing_rule_ids": routing_rule_ids,
                    "updated_utc": updated_utc,
                },
                routing_rule_list_params.RoutingRuleListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoutingRuleResult,
        )

    def delete(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        routing_rule_ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Deletes routing rules.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          routing_rule_ids: Unique identifiers of the routing rules to be deleted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/routingRules/delete",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "routing_rule_ids": routing_rule_ids,
                },
                routing_rule_delete_params.RoutingRuleDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def add(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        routing_rules: Iterable[routing_rule_add_params.RoutingRule],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RoutingRuleResult:
        """
        Adds a new routing rules.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          routing_rules: Collection of Routing rules to be added.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/routingRules/add",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "routing_rules": routing_rules,
                },
                routing_rule_add_params.RoutingRuleAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoutingRuleResult,
        )


class AsyncRoutingRulesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRoutingRulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return AsyncRoutingRulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRoutingRulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return AsyncRoutingRulesResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        routing_rule_updates: Iterable[routing_rule_update_params.RoutingRuleUpdate],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RoutingRuleResult:
        """
        Updates routing rules.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          routing_rule_updates: Collection of Routing rules to be updated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/routingRules/update",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "routing_rule_updates": routing_rule_updates,
                },
                routing_rule_update_params.RoutingRuleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoutingRuleResult,
        )

    async def list(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: routing_rule_list_params.Limitation,
        company_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        routing_rule_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[routing_rule_list_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RoutingRuleResult:
        """Returns all routing rules.

        Note this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          company_ids: Unique identifier of the
              [Company](https://mews-systems.gitbook.io/connector-api/operations/companies/#company).

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          routing_rule_ids: Unique identifier of the
              [Routing rule](https://mews-systems.gitbook.io/connector-api/operations/routingrules/#routing-rule).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/routingRules/getAll",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "company_ids": company_ids,
                    "enterprise_ids": enterprise_ids,
                    "routing_rule_ids": routing_rule_ids,
                    "updated_utc": updated_utc,
                },
                routing_rule_list_params.RoutingRuleListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoutingRuleResult,
        )

    async def delete(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        routing_rule_ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Deletes routing rules.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          routing_rule_ids: Unique identifiers of the routing rules to be deleted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/routingRules/delete",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "routing_rule_ids": routing_rule_ids,
                },
                routing_rule_delete_params.RoutingRuleDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def add(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        routing_rules: Iterable[routing_rule_add_params.RoutingRule],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RoutingRuleResult:
        """
        Adds a new routing rules.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          routing_rules: Collection of Routing rules to be added.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/routingRules/add",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "routing_rules": routing_rules,
                },
                routing_rule_add_params.RoutingRuleAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoutingRuleResult,
        )


class RoutingRulesResourceWithRawResponse:
    def __init__(self, routing_rules: RoutingRulesResource) -> None:
        self._routing_rules = routing_rules

        self.update = to_raw_response_wrapper(
            routing_rules.update,
        )
        self.list = to_raw_response_wrapper(
            routing_rules.list,
        )
        self.delete = to_raw_response_wrapper(
            routing_rules.delete,
        )
        self.add = to_raw_response_wrapper(
            routing_rules.add,
        )


class AsyncRoutingRulesResourceWithRawResponse:
    def __init__(self, routing_rules: AsyncRoutingRulesResource) -> None:
        self._routing_rules = routing_rules

        self.update = async_to_raw_response_wrapper(
            routing_rules.update,
        )
        self.list = async_to_raw_response_wrapper(
            routing_rules.list,
        )
        self.delete = async_to_raw_response_wrapper(
            routing_rules.delete,
        )
        self.add = async_to_raw_response_wrapper(
            routing_rules.add,
        )


class RoutingRulesResourceWithStreamingResponse:
    def __init__(self, routing_rules: RoutingRulesResource) -> None:
        self._routing_rules = routing_rules

        self.update = to_streamed_response_wrapper(
            routing_rules.update,
        )
        self.list = to_streamed_response_wrapper(
            routing_rules.list,
        )
        self.delete = to_streamed_response_wrapper(
            routing_rules.delete,
        )
        self.add = to_streamed_response_wrapper(
            routing_rules.add,
        )


class AsyncRoutingRulesResourceWithStreamingResponse:
    def __init__(self, routing_rules: AsyncRoutingRulesResource) -> None:
        self._routing_rules = routing_rules

        self.update = async_to_streamed_response_wrapper(
            routing_rules.update,
        )
        self.list = async_to_streamed_response_wrapper(
            routing_rules.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            routing_rules.delete,
        )
        self.add = async_to_streamed_response_wrapper(
            routing_rules.add,
        )
