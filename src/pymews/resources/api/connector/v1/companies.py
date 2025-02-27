# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
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
    company_add_params,
    company_list_params,
    company_delete_params,
    company_update_params,
)
from .....types.api.connector.v1.company_result import CompanyResult

__all__ = ["CompaniesResource", "AsyncCompaniesResource"]


class CompaniesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CompaniesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return CompaniesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CompaniesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return CompaniesResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        company_id: str,
        accounting_code: Optional[company_update_params.AccountingCode] | NotGiven = NOT_GIVEN,
        additional_tax_identifier: Optional[company_update_params.AdditionalTaxIdentifier] | NotGiven = NOT_GIVEN,
        billing_code: Optional[company_update_params.BillingCode] | NotGiven = NOT_GIVEN,
        chain_id: Optional[str] | NotGiven = NOT_GIVEN,
        contact: Optional[company_update_params.Contact] | NotGiven = NOT_GIVEN,
        contact_person: Optional[company_update_params.ContactPerson] | NotGiven = NOT_GIVEN,
        credit_rating: Optional[company_update_params.CreditRating] | NotGiven = NOT_GIVEN,
        department: Optional[company_update_params.Department] | NotGiven = NOT_GIVEN,
        duns_number: Optional[company_update_params.DunsNumber] | NotGiven = NOT_GIVEN,
        external_identifier: Optional[company_update_params.ExternalIdentifier] | NotGiven = NOT_GIVEN,
        iata: Optional[company_update_params.Iata] | NotGiven = NOT_GIVEN,
        identifier: Optional[company_update_params.Identifier] | NotGiven = NOT_GIVEN,
        invoice_due_interval: Optional[company_update_params.InvoiceDueInterval] | NotGiven = NOT_GIVEN,
        invoicing_email: Optional[company_update_params.InvoicingEmail] | NotGiven = NOT_GIVEN,
        mother_company_id: Optional[company_update_params.MotherCompanyID] | NotGiven = NOT_GIVEN,
        name: Optional[company_update_params.Name] | NotGiven = NOT_GIVEN,
        notes: Optional[company_update_params.Notes] | NotGiven = NOT_GIVEN,
        options: Optional[company_update_params.Options] | NotGiven = NOT_GIVEN,
        reference_identifier: Optional[company_update_params.ReferenceIdentifier] | NotGiven = NOT_GIVEN,
        tax_identifier: Optional[company_update_params.TaxIdentifier] | NotGiven = NOT_GIVEN,
        telephone: Optional[company_update_params.Telephone] | NotGiven = NOT_GIVEN,
        website_url: Optional[company_update_params.WebsiteURL] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompanyResult:
        """Updates information of the company.

        Note this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          company_id: Unique identifier of the
              [Company](https://mews-systems.gitbook.io/connector-api/operations/#company).

          accounting_code: Accounting code of the company (or `null` if the accounting code should not be
              updated).

          additional_tax_identifier: Additional tax identifier of the company (or `null` if the additional tax
              identifier should not be updated).

          billing_code: Billing code of the company (or `null` if the billing code should not be
              updated).

          chain_id: Unique identifier of the chain. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          contact: Other contact details, such as telephone, email or similar (or `null` if the
              contact should not be updated).

          contact_person: Contact person of the company (or `null` if the contact person should not be
              updated).

          credit_rating: Credit rating to define creditworthiness of the company.

          department: The internal segmentation of a company, e.g. sales department (or `null` if the
              department should not be updated).

          duns_number: The Dun & Bradstreet unique 9-digit DUNS number (or `null` if the Duns number
              should not be updated).

          external_identifier: Identifier of the company from external system (or `null` if the External
              Identifier should not be updated).

          iata: Iata of the company (or `null` if the Iata should not be updated).

          identifier: Identifier of the company, e.g. legal identifier (or `null` if the identifier
              should not be updated).

          invoice_due_interval: The maximum time, when the invoice has to be be paid in ISO 8601 duration format
              (or `null` if the interval should not be updated).

          invoicing_email: Email for issuing invoices to the company (or `null` if the email for issuing
              invoices should not be updated).

          mother_company_id: Unique identifier of the mother company (or `null` if the mother company should
              not be updated).

          name: Name of the company (or `null` if the name should not be updated).

          notes: Notes of the company (or `null` if the notes should not be updated).

          options: Options of the company.

          reference_identifier: External system identifier - custom identifier used by an external system such
              as an external database (or `null` if the identifier should not be updated).

          tax_identifier: Tax identification number of the company (or `null` if the tax identifier should
              not be updated).

          telephone: Contact telephone number (or `null` if the telephone number should not be
              updated).

          website_url: The website url of the company (or `null` if the website url should not be
              updated).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/companies/update",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "company_id": company_id,
                    "accounting_code": accounting_code,
                    "additional_tax_identifier": additional_tax_identifier,
                    "billing_code": billing_code,
                    "chain_id": chain_id,
                    "contact": contact,
                    "contact_person": contact_person,
                    "credit_rating": credit_rating,
                    "department": department,
                    "duns_number": duns_number,
                    "external_identifier": external_identifier,
                    "iata": iata,
                    "identifier": identifier,
                    "invoice_due_interval": invoice_due_interval,
                    "invoicing_email": invoicing_email,
                    "mother_company_id": mother_company_id,
                    "name": name,
                    "notes": notes,
                    "options": options,
                    "reference_identifier": reference_identifier,
                    "tax_identifier": tax_identifier,
                    "telephone": telephone,
                    "website_url": website_url,
                },
                company_update_params.CompanyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompanyResult,
        )

    def list(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        activity_states: Optional[List[Literal["Deleted", "Active"]]] | NotGiven = NOT_GIVEN,
        chain_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        created_utc: Optional[company_list_params.CreatedUtc] | NotGiven = NOT_GIVEN,
        end_utc: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        external_identifiers: Optional[List[str]] | NotGiven = NOT_GIVEN,
        ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        limitation: Optional[company_list_params.Limitation] | NotGiven = NOT_GIVEN,
        mother_company_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        names: Optional[List[str]] | NotGiven = NOT_GIVEN,
        start_utc: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        time_filter: Optional[Literal["Created", "Updated"]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[company_list_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompanyResult:
        """
        Returns all company profiles of the enterprise, possibly filtered by
        identifiers, names or other filters. Note this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          activity_states: Whether to return only active, only deleted, or both types of record. If not
              specified, both active and deleted records will be returned.

          chain_ids: Unique identifiers of the chain. If not specified, the operation returns data
              for all chains within scope of the Access Token.

          external_identifiers: Identifiers of
              [Company](https://mews-systems.gitbook.io/connector-api/operations/#company)
              from external system.

          ids: Unique identifiers of
              [Companies](https://mews-systems.gitbook.io/connector-api/operations/#company).

          limitation: Limitation on the quantity of data returned.

          mother_company_ids: Unique identifiers of mother `Company`.

          names: Names of
              [Companies](https://mews-systems.gitbook.io/connector-api/operations/#company).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/companies/getAll",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "activity_states": activity_states,
                    "chain_ids": chain_ids,
                    "created_utc": created_utc,
                    "end_utc": end_utc,
                    "external_identifiers": external_identifiers,
                    "ids": ids,
                    "limitation": limitation,
                    "mother_company_ids": mother_company_ids,
                    "names": names,
                    "start_utc": start_utc,
                    "time_filter": time_filter,
                    "updated_utc": updated_utc,
                },
                company_list_params.CompanyListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompanyResult,
        )

    def delete(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        company_ids: List[str],
        chain_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Deletes specified companies.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          company_ids: Unique identifiers of the companies to be deleted.

          chain_id: Unique identifier of the chain. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/companies/delete",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "company_ids": company_ids,
                    "chain_id": chain_id,
                },
                company_delete_params.CompanyDeleteParams,
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
        name: str,
        options: company_add_params.Options,
        accounting_code: Optional[str] | NotGiven = NOT_GIVEN,
        additional_tax_identifier: Optional[str] | NotGiven = NOT_GIVEN,
        address: Optional[company_add_params.Address] | NotGiven = NOT_GIVEN,
        billing_code: Optional[str] | NotGiven = NOT_GIVEN,
        chain_id: Optional[str] | NotGiven = NOT_GIVEN,
        contact: Optional[str] | NotGiven = NOT_GIVEN,
        contact_person: Optional[str] | NotGiven = NOT_GIVEN,
        credit_rating: Optional[company_add_params.CreditRating] | NotGiven = NOT_GIVEN,
        department: Optional[str] | NotGiven = NOT_GIVEN,
        duns_number: Optional[str] | NotGiven = NOT_GIVEN,
        external_identifier: Optional[str] | NotGiven = NOT_GIVEN,
        iata: Optional[str] | NotGiven = NOT_GIVEN,
        identifier: Optional[str] | NotGiven = NOT_GIVEN,
        invoice_due_interval: Optional[str] | NotGiven = NOT_GIVEN,
        invoicing_email: Optional[str] | NotGiven = NOT_GIVEN,
        mother_company_id: Optional[str] | NotGiven = NOT_GIVEN,
        notes: Optional[str] | NotGiven = NOT_GIVEN,
        reference_identifier: Optional[str] | NotGiven = NOT_GIVEN,
        tax_identifier: Optional[str] | NotGiven = NOT_GIVEN,
        telephone: Optional[str] | NotGiven = NOT_GIVEN,
        website_url: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompanyResult:
        """Adds a new company.

        Note this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          name: Name of the company.

          options: Options of the company.

          accounting_code: Accounting code of the company.

          additional_tax_identifier: Additional tax identifer of the company.

          address: New address details.

          billing_code: Billing code of the company.

          chain_id: Unique identifier of the chain. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          contact: Other contact details, such as telephone, email or similar.

          contact_person: Contact person of the company.

          credit_rating: Credit rating to define creditworthiness of the company.

          department: The internal segmentation of a company, e.g. sales department.

          duns_number: The Dun & Bradstreet unique 9-digit DUNS number.

          external_identifier: Identifier of the company from external system.

          iata: Iata of the company.

          identifier: Identifier of the company (e.g. legal identifier).

          invoice_due_interval: The maximum time, when the invoice has to be be paid in ISO 8601 duration
              format.

          invoicing_email: Email for issuing invoices to the company.

          mother_company_id: Unique identifier of the mother company.

          notes: Notes of the company.

          reference_identifier: External system identifier - custom identifier used by an external system such
              as an external database.

          tax_identifier: Tax identification number of the company.

          telephone: Contact telephone number.

          website_url: The website url of the company.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/companies/add",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "name": name,
                    "options": options,
                    "accounting_code": accounting_code,
                    "additional_tax_identifier": additional_tax_identifier,
                    "address": address,
                    "billing_code": billing_code,
                    "chain_id": chain_id,
                    "contact": contact,
                    "contact_person": contact_person,
                    "credit_rating": credit_rating,
                    "department": department,
                    "duns_number": duns_number,
                    "external_identifier": external_identifier,
                    "iata": iata,
                    "identifier": identifier,
                    "invoice_due_interval": invoice_due_interval,
                    "invoicing_email": invoicing_email,
                    "mother_company_id": mother_company_id,
                    "notes": notes,
                    "reference_identifier": reference_identifier,
                    "tax_identifier": tax_identifier,
                    "telephone": telephone,
                    "website_url": website_url,
                },
                company_add_params.CompanyAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompanyResult,
        )


class AsyncCompaniesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCompaniesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return AsyncCompaniesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCompaniesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return AsyncCompaniesResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        company_id: str,
        accounting_code: Optional[company_update_params.AccountingCode] | NotGiven = NOT_GIVEN,
        additional_tax_identifier: Optional[company_update_params.AdditionalTaxIdentifier] | NotGiven = NOT_GIVEN,
        billing_code: Optional[company_update_params.BillingCode] | NotGiven = NOT_GIVEN,
        chain_id: Optional[str] | NotGiven = NOT_GIVEN,
        contact: Optional[company_update_params.Contact] | NotGiven = NOT_GIVEN,
        contact_person: Optional[company_update_params.ContactPerson] | NotGiven = NOT_GIVEN,
        credit_rating: Optional[company_update_params.CreditRating] | NotGiven = NOT_GIVEN,
        department: Optional[company_update_params.Department] | NotGiven = NOT_GIVEN,
        duns_number: Optional[company_update_params.DunsNumber] | NotGiven = NOT_GIVEN,
        external_identifier: Optional[company_update_params.ExternalIdentifier] | NotGiven = NOT_GIVEN,
        iata: Optional[company_update_params.Iata] | NotGiven = NOT_GIVEN,
        identifier: Optional[company_update_params.Identifier] | NotGiven = NOT_GIVEN,
        invoice_due_interval: Optional[company_update_params.InvoiceDueInterval] | NotGiven = NOT_GIVEN,
        invoicing_email: Optional[company_update_params.InvoicingEmail] | NotGiven = NOT_GIVEN,
        mother_company_id: Optional[company_update_params.MotherCompanyID] | NotGiven = NOT_GIVEN,
        name: Optional[company_update_params.Name] | NotGiven = NOT_GIVEN,
        notes: Optional[company_update_params.Notes] | NotGiven = NOT_GIVEN,
        options: Optional[company_update_params.Options] | NotGiven = NOT_GIVEN,
        reference_identifier: Optional[company_update_params.ReferenceIdentifier] | NotGiven = NOT_GIVEN,
        tax_identifier: Optional[company_update_params.TaxIdentifier] | NotGiven = NOT_GIVEN,
        telephone: Optional[company_update_params.Telephone] | NotGiven = NOT_GIVEN,
        website_url: Optional[company_update_params.WebsiteURL] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompanyResult:
        """Updates information of the company.

        Note this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          company_id: Unique identifier of the
              [Company](https://mews-systems.gitbook.io/connector-api/operations/#company).

          accounting_code: Accounting code of the company (or `null` if the accounting code should not be
              updated).

          additional_tax_identifier: Additional tax identifier of the company (or `null` if the additional tax
              identifier should not be updated).

          billing_code: Billing code of the company (or `null` if the billing code should not be
              updated).

          chain_id: Unique identifier of the chain. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          contact: Other contact details, such as telephone, email or similar (or `null` if the
              contact should not be updated).

          contact_person: Contact person of the company (or `null` if the contact person should not be
              updated).

          credit_rating: Credit rating to define creditworthiness of the company.

          department: The internal segmentation of a company, e.g. sales department (or `null` if the
              department should not be updated).

          duns_number: The Dun & Bradstreet unique 9-digit DUNS number (or `null` if the Duns number
              should not be updated).

          external_identifier: Identifier of the company from external system (or `null` if the External
              Identifier should not be updated).

          iata: Iata of the company (or `null` if the Iata should not be updated).

          identifier: Identifier of the company, e.g. legal identifier (or `null` if the identifier
              should not be updated).

          invoice_due_interval: The maximum time, when the invoice has to be be paid in ISO 8601 duration format
              (or `null` if the interval should not be updated).

          invoicing_email: Email for issuing invoices to the company (or `null` if the email for issuing
              invoices should not be updated).

          mother_company_id: Unique identifier of the mother company (or `null` if the mother company should
              not be updated).

          name: Name of the company (or `null` if the name should not be updated).

          notes: Notes of the company (or `null` if the notes should not be updated).

          options: Options of the company.

          reference_identifier: External system identifier - custom identifier used by an external system such
              as an external database (or `null` if the identifier should not be updated).

          tax_identifier: Tax identification number of the company (or `null` if the tax identifier should
              not be updated).

          telephone: Contact telephone number (or `null` if the telephone number should not be
              updated).

          website_url: The website url of the company (or `null` if the website url should not be
              updated).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/companies/update",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "company_id": company_id,
                    "accounting_code": accounting_code,
                    "additional_tax_identifier": additional_tax_identifier,
                    "billing_code": billing_code,
                    "chain_id": chain_id,
                    "contact": contact,
                    "contact_person": contact_person,
                    "credit_rating": credit_rating,
                    "department": department,
                    "duns_number": duns_number,
                    "external_identifier": external_identifier,
                    "iata": iata,
                    "identifier": identifier,
                    "invoice_due_interval": invoice_due_interval,
                    "invoicing_email": invoicing_email,
                    "mother_company_id": mother_company_id,
                    "name": name,
                    "notes": notes,
                    "options": options,
                    "reference_identifier": reference_identifier,
                    "tax_identifier": tax_identifier,
                    "telephone": telephone,
                    "website_url": website_url,
                },
                company_update_params.CompanyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompanyResult,
        )

    async def list(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        activity_states: Optional[List[Literal["Deleted", "Active"]]] | NotGiven = NOT_GIVEN,
        chain_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        created_utc: Optional[company_list_params.CreatedUtc] | NotGiven = NOT_GIVEN,
        end_utc: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        external_identifiers: Optional[List[str]] | NotGiven = NOT_GIVEN,
        ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        limitation: Optional[company_list_params.Limitation] | NotGiven = NOT_GIVEN,
        mother_company_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        names: Optional[List[str]] | NotGiven = NOT_GIVEN,
        start_utc: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        time_filter: Optional[Literal["Created", "Updated"]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[company_list_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompanyResult:
        """
        Returns all company profiles of the enterprise, possibly filtered by
        identifiers, names or other filters. Note this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          activity_states: Whether to return only active, only deleted, or both types of record. If not
              specified, both active and deleted records will be returned.

          chain_ids: Unique identifiers of the chain. If not specified, the operation returns data
              for all chains within scope of the Access Token.

          external_identifiers: Identifiers of
              [Company](https://mews-systems.gitbook.io/connector-api/operations/#company)
              from external system.

          ids: Unique identifiers of
              [Companies](https://mews-systems.gitbook.io/connector-api/operations/#company).

          limitation: Limitation on the quantity of data returned.

          mother_company_ids: Unique identifiers of mother `Company`.

          names: Names of
              [Companies](https://mews-systems.gitbook.io/connector-api/operations/#company).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/companies/getAll",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "activity_states": activity_states,
                    "chain_ids": chain_ids,
                    "created_utc": created_utc,
                    "end_utc": end_utc,
                    "external_identifiers": external_identifiers,
                    "ids": ids,
                    "limitation": limitation,
                    "mother_company_ids": mother_company_ids,
                    "names": names,
                    "start_utc": start_utc,
                    "time_filter": time_filter,
                    "updated_utc": updated_utc,
                },
                company_list_params.CompanyListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompanyResult,
        )

    async def delete(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        company_ids: List[str],
        chain_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Deletes specified companies.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          company_ids: Unique identifiers of the companies to be deleted.

          chain_id: Unique identifier of the chain. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/companies/delete",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "company_ids": company_ids,
                    "chain_id": chain_id,
                },
                company_delete_params.CompanyDeleteParams,
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
        name: str,
        options: company_add_params.Options,
        accounting_code: Optional[str] | NotGiven = NOT_GIVEN,
        additional_tax_identifier: Optional[str] | NotGiven = NOT_GIVEN,
        address: Optional[company_add_params.Address] | NotGiven = NOT_GIVEN,
        billing_code: Optional[str] | NotGiven = NOT_GIVEN,
        chain_id: Optional[str] | NotGiven = NOT_GIVEN,
        contact: Optional[str] | NotGiven = NOT_GIVEN,
        contact_person: Optional[str] | NotGiven = NOT_GIVEN,
        credit_rating: Optional[company_add_params.CreditRating] | NotGiven = NOT_GIVEN,
        department: Optional[str] | NotGiven = NOT_GIVEN,
        duns_number: Optional[str] | NotGiven = NOT_GIVEN,
        external_identifier: Optional[str] | NotGiven = NOT_GIVEN,
        iata: Optional[str] | NotGiven = NOT_GIVEN,
        identifier: Optional[str] | NotGiven = NOT_GIVEN,
        invoice_due_interval: Optional[str] | NotGiven = NOT_GIVEN,
        invoicing_email: Optional[str] | NotGiven = NOT_GIVEN,
        mother_company_id: Optional[str] | NotGiven = NOT_GIVEN,
        notes: Optional[str] | NotGiven = NOT_GIVEN,
        reference_identifier: Optional[str] | NotGiven = NOT_GIVEN,
        tax_identifier: Optional[str] | NotGiven = NOT_GIVEN,
        telephone: Optional[str] | NotGiven = NOT_GIVEN,
        website_url: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompanyResult:
        """Adds a new company.

        Note this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          name: Name of the company.

          options: Options of the company.

          accounting_code: Accounting code of the company.

          additional_tax_identifier: Additional tax identifer of the company.

          address: New address details.

          billing_code: Billing code of the company.

          chain_id: Unique identifier of the chain. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          contact: Other contact details, such as telephone, email or similar.

          contact_person: Contact person of the company.

          credit_rating: Credit rating to define creditworthiness of the company.

          department: The internal segmentation of a company, e.g. sales department.

          duns_number: The Dun & Bradstreet unique 9-digit DUNS number.

          external_identifier: Identifier of the company from external system.

          iata: Iata of the company.

          identifier: Identifier of the company (e.g. legal identifier).

          invoice_due_interval: The maximum time, when the invoice has to be be paid in ISO 8601 duration
              format.

          invoicing_email: Email for issuing invoices to the company.

          mother_company_id: Unique identifier of the mother company.

          notes: Notes of the company.

          reference_identifier: External system identifier - custom identifier used by an external system such
              as an external database.

          tax_identifier: Tax identification number of the company.

          telephone: Contact telephone number.

          website_url: The website url of the company.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/companies/add",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "name": name,
                    "options": options,
                    "accounting_code": accounting_code,
                    "additional_tax_identifier": additional_tax_identifier,
                    "address": address,
                    "billing_code": billing_code,
                    "chain_id": chain_id,
                    "contact": contact,
                    "contact_person": contact_person,
                    "credit_rating": credit_rating,
                    "department": department,
                    "duns_number": duns_number,
                    "external_identifier": external_identifier,
                    "iata": iata,
                    "identifier": identifier,
                    "invoice_due_interval": invoice_due_interval,
                    "invoicing_email": invoicing_email,
                    "mother_company_id": mother_company_id,
                    "notes": notes,
                    "reference_identifier": reference_identifier,
                    "tax_identifier": tax_identifier,
                    "telephone": telephone,
                    "website_url": website_url,
                },
                company_add_params.CompanyAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompanyResult,
        )


class CompaniesResourceWithRawResponse:
    def __init__(self, companies: CompaniesResource) -> None:
        self._companies = companies

        self.update = to_raw_response_wrapper(
            companies.update,
        )
        self.list = to_raw_response_wrapper(
            companies.list,
        )
        self.delete = to_raw_response_wrapper(
            companies.delete,
        )
        self.add = to_raw_response_wrapper(
            companies.add,
        )


class AsyncCompaniesResourceWithRawResponse:
    def __init__(self, companies: AsyncCompaniesResource) -> None:
        self._companies = companies

        self.update = async_to_raw_response_wrapper(
            companies.update,
        )
        self.list = async_to_raw_response_wrapper(
            companies.list,
        )
        self.delete = async_to_raw_response_wrapper(
            companies.delete,
        )
        self.add = async_to_raw_response_wrapper(
            companies.add,
        )


class CompaniesResourceWithStreamingResponse:
    def __init__(self, companies: CompaniesResource) -> None:
        self._companies = companies

        self.update = to_streamed_response_wrapper(
            companies.update,
        )
        self.list = to_streamed_response_wrapper(
            companies.list,
        )
        self.delete = to_streamed_response_wrapper(
            companies.delete,
        )
        self.add = to_streamed_response_wrapper(
            companies.add,
        )


class AsyncCompaniesResourceWithStreamingResponse:
    def __init__(self, companies: AsyncCompaniesResource) -> None:
        self._companies = companies

        self.update = async_to_streamed_response_wrapper(
            companies.update,
        )
        self.list = async_to_streamed_response_wrapper(
            companies.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            companies.delete,
        )
        self.add = async_to_streamed_response_wrapper(
            companies.add,
        )
