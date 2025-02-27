# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal

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
    identity_document_add_params,
    identity_document_list_params,
    identity_document_clear_params,
    identity_document_delete_params,
    identity_document_update_params,
)
from .....types.api.connector.v1.identity_document_write_result import IdentityDocumentWriteResult
from .....types.api.connector.v1.identity_document_list_response import IdentityDocumentListResponse

__all__ = ["IdentityDocumentsResource", "AsyncIdentityDocumentsResource"]


class IdentityDocumentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IdentityDocumentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return IdentityDocumentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IdentityDocumentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return IdentityDocumentsResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        identity_documents: Iterable[identity_document_update_params.IdentityDocument],
        chain_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityDocumentWriteResult:
        """Updates specified identity documents.

        This operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          identity_documents: Identity documents to be updated.

          chain_id: Unique identifier of the chain. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/identityDocuments/update",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "identity_documents": identity_documents,
                    "chain_id": chain_id,
                },
                identity_document_update_params.IdentityDocumentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IdentityDocumentWriteResult,
        )

    def list(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        customer_ids: List[str],
        limitation: identity_document_list_params.Limitation,
        chain_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        identity_document_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        types: Optional[List[Literal["IdentityCard", "Passport", "Visa", "DriversLicense"]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityDocumentListResponse:
        """
        Returns all identity documents for the specified customers, with additional
        filtering options available. This operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          customer_ids: Unique identifiers of `Customer`.

          limitation: Limitation on the quantity of data returned.

          chain_ids: Unique identifiers of `Chain`. If not specified, the operation returns data for
              all chains within scope of the Access Token.

          identity_document_ids: Unique identifiers of `Identity document`.

          types: Type of the identity document.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/identityDocuments/getAll",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "customer_ids": customer_ids,
                    "limitation": limitation,
                    "chain_ids": chain_ids,
                    "identity_document_ids": identity_document_ids,
                    "types": types,
                },
                identity_document_list_params.IdentityDocumentListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IdentityDocumentListResponse,
        )

    def delete(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        identity_document_ids: List[str],
        chain_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Deletes specified identity documents.

        This operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          identity_document_ids: Unique identifiers of the identity documents to be deleted.

          chain_id: Unique identifier of the chain. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/identityDocuments/delete",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "identity_document_ids": identity_document_ids,
                    "chain_id": chain_id,
                },
                identity_document_delete_params.IdentityDocumentDeleteParams,
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
        identity_documents: Iterable[identity_document_add_params.IdentityDocument],
        chain_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityDocumentWriteResult:
        """Adds identity documents.

        This operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          identity_documents: Identity documents to be added.

          chain_id: Unique identifier of the chain. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/identityDocuments/add",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "identity_documents": identity_documents,
                    "chain_id": chain_id,
                },
                identity_document_add_params.IdentityDocumentAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IdentityDocumentWriteResult,
        )

    def clear(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        customer_ids: List[str],
        chain_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Deletes all identity documents for the specified customers.

        This operation
        supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          customer_ids: Unique identifiers of the `Customer` for whom documents will be deleted.

          chain_id: Unique identifier of the chain. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/identityDocuments/clear",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "customer_ids": customer_ids,
                    "chain_id": chain_id,
                },
                identity_document_clear_params.IdentityDocumentClearParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncIdentityDocumentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIdentityDocumentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return AsyncIdentityDocumentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIdentityDocumentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return AsyncIdentityDocumentsResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        identity_documents: Iterable[identity_document_update_params.IdentityDocument],
        chain_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityDocumentWriteResult:
        """Updates specified identity documents.

        This operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          identity_documents: Identity documents to be updated.

          chain_id: Unique identifier of the chain. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/identityDocuments/update",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "identity_documents": identity_documents,
                    "chain_id": chain_id,
                },
                identity_document_update_params.IdentityDocumentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IdentityDocumentWriteResult,
        )

    async def list(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        customer_ids: List[str],
        limitation: identity_document_list_params.Limitation,
        chain_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        identity_document_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        types: Optional[List[Literal["IdentityCard", "Passport", "Visa", "DriversLicense"]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityDocumentListResponse:
        """
        Returns all identity documents for the specified customers, with additional
        filtering options available. This operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          customer_ids: Unique identifiers of `Customer`.

          limitation: Limitation on the quantity of data returned.

          chain_ids: Unique identifiers of `Chain`. If not specified, the operation returns data for
              all chains within scope of the Access Token.

          identity_document_ids: Unique identifiers of `Identity document`.

          types: Type of the identity document.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/identityDocuments/getAll",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "customer_ids": customer_ids,
                    "limitation": limitation,
                    "chain_ids": chain_ids,
                    "identity_document_ids": identity_document_ids,
                    "types": types,
                },
                identity_document_list_params.IdentityDocumentListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IdentityDocumentListResponse,
        )

    async def delete(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        identity_document_ids: List[str],
        chain_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Deletes specified identity documents.

        This operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          identity_document_ids: Unique identifiers of the identity documents to be deleted.

          chain_id: Unique identifier of the chain. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/identityDocuments/delete",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "identity_document_ids": identity_document_ids,
                    "chain_id": chain_id,
                },
                identity_document_delete_params.IdentityDocumentDeleteParams,
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
        identity_documents: Iterable[identity_document_add_params.IdentityDocument],
        chain_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityDocumentWriteResult:
        """Adds identity documents.

        This operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          identity_documents: Identity documents to be added.

          chain_id: Unique identifier of the chain. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/identityDocuments/add",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "identity_documents": identity_documents,
                    "chain_id": chain_id,
                },
                identity_document_add_params.IdentityDocumentAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IdentityDocumentWriteResult,
        )

    async def clear(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        customer_ids: List[str],
        chain_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Deletes all identity documents for the specified customers.

        This operation
        supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property/).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          customer_ids: Unique identifiers of the `Customer` for whom documents will be deleted.

          chain_id: Unique identifier of the chain. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/identityDocuments/clear",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "customer_ids": customer_ids,
                    "chain_id": chain_id,
                },
                identity_document_clear_params.IdentityDocumentClearParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class IdentityDocumentsResourceWithRawResponse:
    def __init__(self, identity_documents: IdentityDocumentsResource) -> None:
        self._identity_documents = identity_documents

        self.update = to_raw_response_wrapper(
            identity_documents.update,
        )
        self.list = to_raw_response_wrapper(
            identity_documents.list,
        )
        self.delete = to_raw_response_wrapper(
            identity_documents.delete,
        )
        self.add = to_raw_response_wrapper(
            identity_documents.add,
        )
        self.clear = to_raw_response_wrapper(
            identity_documents.clear,
        )


class AsyncIdentityDocumentsResourceWithRawResponse:
    def __init__(self, identity_documents: AsyncIdentityDocumentsResource) -> None:
        self._identity_documents = identity_documents

        self.update = async_to_raw_response_wrapper(
            identity_documents.update,
        )
        self.list = async_to_raw_response_wrapper(
            identity_documents.list,
        )
        self.delete = async_to_raw_response_wrapper(
            identity_documents.delete,
        )
        self.add = async_to_raw_response_wrapper(
            identity_documents.add,
        )
        self.clear = async_to_raw_response_wrapper(
            identity_documents.clear,
        )


class IdentityDocumentsResourceWithStreamingResponse:
    def __init__(self, identity_documents: IdentityDocumentsResource) -> None:
        self._identity_documents = identity_documents

        self.update = to_streamed_response_wrapper(
            identity_documents.update,
        )
        self.list = to_streamed_response_wrapper(
            identity_documents.list,
        )
        self.delete = to_streamed_response_wrapper(
            identity_documents.delete,
        )
        self.add = to_streamed_response_wrapper(
            identity_documents.add,
        )
        self.clear = to_streamed_response_wrapper(
            identity_documents.clear,
        )


class AsyncIdentityDocumentsResourceWithStreamingResponse:
    def __init__(self, identity_documents: AsyncIdentityDocumentsResource) -> None:
        self._identity_documents = identity_documents

        self.update = async_to_streamed_response_wrapper(
            identity_documents.update,
        )
        self.list = async_to_streamed_response_wrapper(
            identity_documents.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            identity_documents.delete,
        )
        self.add = async_to_streamed_response_wrapper(
            identity_documents.add,
        )
        self.clear = async_to_streamed_response_wrapper(
            identity_documents.clear,
        )
