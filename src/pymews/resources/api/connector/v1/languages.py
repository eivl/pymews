# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

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
from .....types.api.connector.v1 import language_list_params, language_get_texts_params
from .....types.api.connector.v1.language_list_response import LanguageListResponse
from .....types.api.connector.v1.language_get_texts_response import LanguageGetTextsResponse

__all__ = ["LanguagesResource", "AsyncLanguagesResource"]


class LanguagesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LanguagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return LanguagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LanguagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return LanguagesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LanguageListResponse:
        """
        Returns all languages supported by the API.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/languages/getAll",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                },
                language_list_params.LanguageListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LanguageListResponse,
        )

    def get_texts(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        language_codes: List[str],
        scope: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LanguageGetTextsResponse:
        """
        Returns translations of texts in the specified languages.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          language_codes: Language-culture codes of the
              [Languages](https://mews-systems.gitbook.io/connector-api/operations/#language)
              whose texts to return.

          scope: Scope of texts to return.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/languages/getTexts",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "language_codes": language_codes,
                    "scope": scope,
                },
                language_get_texts_params.LanguageGetTextsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LanguageGetTextsResponse,
        )


class AsyncLanguagesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLanguagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return AsyncLanguagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLanguagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return AsyncLanguagesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LanguageListResponse:
        """
        Returns all languages supported by the API.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/languages/getAll",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                },
                language_list_params.LanguageListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LanguageListResponse,
        )

    async def get_texts(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        language_codes: List[str],
        scope: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LanguageGetTextsResponse:
        """
        Returns translations of texts in the specified languages.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          language_codes: Language-culture codes of the
              [Languages](https://mews-systems.gitbook.io/connector-api/operations/#language)
              whose texts to return.

          scope: Scope of texts to return.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/languages/getTexts",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "language_codes": language_codes,
                    "scope": scope,
                },
                language_get_texts_params.LanguageGetTextsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LanguageGetTextsResponse,
        )


class LanguagesResourceWithRawResponse:
    def __init__(self, languages: LanguagesResource) -> None:
        self._languages = languages

        self.list = to_raw_response_wrapper(
            languages.list,
        )
        self.get_texts = to_raw_response_wrapper(
            languages.get_texts,
        )


class AsyncLanguagesResourceWithRawResponse:
    def __init__(self, languages: AsyncLanguagesResource) -> None:
        self._languages = languages

        self.list = async_to_raw_response_wrapper(
            languages.list,
        )
        self.get_texts = async_to_raw_response_wrapper(
            languages.get_texts,
        )


class LanguagesResourceWithStreamingResponse:
    def __init__(self, languages: LanguagesResource) -> None:
        self._languages = languages

        self.list = to_streamed_response_wrapper(
            languages.list,
        )
        self.get_texts = to_streamed_response_wrapper(
            languages.get_texts,
        )


class AsyncLanguagesResourceWithStreamingResponse:
    def __init__(self, languages: AsyncLanguagesResource) -> None:
        self._languages = languages

        self.list = async_to_streamed_response_wrapper(
            languages.list,
        )
        self.get_texts = async_to_streamed_response_wrapper(
            languages.get_texts,
        )
