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
    company_contract_add_params,
    company_contract_list_params,
    company_contract_delete_params,
    company_contract_update_params,
)
from .....types.api.connector.v1.contract_result import ContractResult

__all__ = ["CompanyContractsResource", "AsyncCompanyContractsResource"]


class CompanyContractsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CompanyContractsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return CompanyContractsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CompanyContractsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return CompanyContractsResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        travel_agency_contract_updates: Iterable[company_contract_update_params.TravelAgencyContractUpdate],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContractResult:
        """
        Updates one or more company contracts.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          travel_agency_contract_updates: Information about travel agency contracts to be updated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/companyContracts/update",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "travel_agency_contract_updates": travel_agency_contract_updates,
                },
                company_contract_update_params.CompanyContractUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractResult,
        )

    def list(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: company_contract_list_params.Limitation,
        service_ids: List[str],
        company_contract_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        company_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[company_contract_list_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContractResult:
        """Returns all contracts between the enterprise and other companies.

        Note this
        operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          service_ids: Unique identifiers of
              [Services](https://mews-systems.gitbook.io/connector-api/operations/services/#service)
              where the Travel agency contract belong to.

          company_contract_ids: Unique identifier of the Travel agency contract to fetch.

          company_ids: Unique identifiers of
              [Companies](https://mews-systems.gitbook.io/connector-api/operations/companies/#company)
              assigned with Travel agency contracts.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/companyContracts/getAll",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "service_ids": service_ids,
                    "company_contract_ids": company_contract_ids,
                    "company_ids": company_ids,
                    "enterprise_ids": enterprise_ids,
                    "updated_utc": updated_utc,
                },
                company_contract_list_params.CompanyContractListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractResult,
        )

    def delete(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        service_ids: List[str],
        travel_agency_contract_ids: List[str],
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Deletes one or more company contracts.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          service_ids: Unique identifiers of the
              [Service](https://mews-systems.gitbook.io/connector-api/operations/services/#service)
              the travel agency contract belongs to.

          travel_agency_contract_ids: Unique identifiers of the Travel agency contract to delete.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/companyContracts/delete",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "service_ids": service_ids,
                    "travel_agency_contract_ids": travel_agency_contract_ids,
                    "enterprise_id": enterprise_id,
                },
                company_contract_delete_params.CompanyContractDeleteParams,
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
        travel_agency_contracts: Iterable[company_contract_add_params.TravelAgencyContract],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContractResult:
        """
        Adds one or more company contracts.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          travel_agency_contracts: Information about travel agency contracts to be created.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/companyContracts/add",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "travel_agency_contracts": travel_agency_contracts,
                },
                company_contract_add_params.CompanyContractAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractResult,
        )


class AsyncCompanyContractsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCompanyContractsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return AsyncCompanyContractsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCompanyContractsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return AsyncCompanyContractsResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        travel_agency_contract_updates: Iterable[company_contract_update_params.TravelAgencyContractUpdate],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContractResult:
        """
        Updates one or more company contracts.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          travel_agency_contract_updates: Information about travel agency contracts to be updated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/companyContracts/update",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "travel_agency_contract_updates": travel_agency_contract_updates,
                },
                company_contract_update_params.CompanyContractUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractResult,
        )

    async def list(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: company_contract_list_params.Limitation,
        service_ids: List[str],
        company_contract_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        company_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[company_contract_list_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContractResult:
        """Returns all contracts between the enterprise and other companies.

        Note this
        operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          service_ids: Unique identifiers of
              [Services](https://mews-systems.gitbook.io/connector-api/operations/services/#service)
              where the Travel agency contract belong to.

          company_contract_ids: Unique identifier of the Travel agency contract to fetch.

          company_ids: Unique identifiers of
              [Companies](https://mews-systems.gitbook.io/connector-api/operations/companies/#company)
              assigned with Travel agency contracts.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/companyContracts/getAll",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "service_ids": service_ids,
                    "company_contract_ids": company_contract_ids,
                    "company_ids": company_ids,
                    "enterprise_ids": enterprise_ids,
                    "updated_utc": updated_utc,
                },
                company_contract_list_params.CompanyContractListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractResult,
        )

    async def delete(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        service_ids: List[str],
        travel_agency_contract_ids: List[str],
        enterprise_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Deletes one or more company contracts.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          service_ids: Unique identifiers of the
              [Service](https://mews-systems.gitbook.io/connector-api/operations/services/#service)
              the travel agency contract belongs to.

          travel_agency_contract_ids: Unique identifiers of the Travel agency contract to delete.

          enterprise_id: Unique identifier of the enterprise. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/companyContracts/delete",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "service_ids": service_ids,
                    "travel_agency_contract_ids": travel_agency_contract_ids,
                    "enterprise_id": enterprise_id,
                },
                company_contract_delete_params.CompanyContractDeleteParams,
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
        travel_agency_contracts: Iterable[company_contract_add_params.TravelAgencyContract],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContractResult:
        """
        Adds one or more company contracts.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          travel_agency_contracts: Information about travel agency contracts to be created.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/companyContracts/add",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "travel_agency_contracts": travel_agency_contracts,
                },
                company_contract_add_params.CompanyContractAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractResult,
        )


class CompanyContractsResourceWithRawResponse:
    def __init__(self, company_contracts: CompanyContractsResource) -> None:
        self._company_contracts = company_contracts

        self.update = to_raw_response_wrapper(
            company_contracts.update,
        )
        self.list = to_raw_response_wrapper(
            company_contracts.list,
        )
        self.delete = to_raw_response_wrapper(
            company_contracts.delete,
        )
        self.add = to_raw_response_wrapper(
            company_contracts.add,
        )


class AsyncCompanyContractsResourceWithRawResponse:
    def __init__(self, company_contracts: AsyncCompanyContractsResource) -> None:
        self._company_contracts = company_contracts

        self.update = async_to_raw_response_wrapper(
            company_contracts.update,
        )
        self.list = async_to_raw_response_wrapper(
            company_contracts.list,
        )
        self.delete = async_to_raw_response_wrapper(
            company_contracts.delete,
        )
        self.add = async_to_raw_response_wrapper(
            company_contracts.add,
        )


class CompanyContractsResourceWithStreamingResponse:
    def __init__(self, company_contracts: CompanyContractsResource) -> None:
        self._company_contracts = company_contracts

        self.update = to_streamed_response_wrapper(
            company_contracts.update,
        )
        self.list = to_streamed_response_wrapper(
            company_contracts.list,
        )
        self.delete = to_streamed_response_wrapper(
            company_contracts.delete,
        )
        self.add = to_streamed_response_wrapper(
            company_contracts.add,
        )


class AsyncCompanyContractsResourceWithStreamingResponse:
    def __init__(self, company_contracts: AsyncCompanyContractsResource) -> None:
        self._company_contracts = company_contracts

        self.update = async_to_streamed_response_wrapper(
            company_contracts.update,
        )
        self.list = async_to_streamed_response_wrapper(
            company_contracts.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            company_contracts.delete,
        )
        self.add = async_to_streamed_response_wrapper(
            company_contracts.add,
        )
