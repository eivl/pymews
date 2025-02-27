# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import date, datetime
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
    customer_add_params,
    customer_list_params,
    customer_merge_params,
    customer_search_params,
    customer_update_params,
    customer_add_file_params,
    customer_get_open_items_params,
)
from .....types.api.connector.v1.customer import Customer
from .....types.api.connector.v1.customer_list_response import CustomerListResponse
from .....types.api.connector.v1.customer_search_response import CustomerSearchResponse
from .....types.api.connector.v1.customer_add_file_response import CustomerAddFileResponse
from .....types.api.connector.v1.customer_get_open_items_response import CustomerGetOpenItemsResponse

__all__ = ["CustomersResource", "AsyncCustomersResource"]


class CustomersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CustomersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return CustomersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return CustomersResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        customer_id: str,
        address: Optional[customer_update_params.Address] | NotGiven = NOT_GIVEN,
        birth_date: Union[str, date, None] | NotGiven = NOT_GIVEN,
        birth_place: Optional[str] | NotGiven = NOT_GIVEN,
        car_registration_number: Optional[str] | NotGiven = NOT_GIVEN,
        chain_id: Optional[str] | NotGiven = NOT_GIVEN,
        classifications: Optional[
            List[
                Literal[
                    "PaymasterAccount",
                    "Blacklist",
                    "Media",
                    "LoyaltyProgram",
                    "PreviousComplaint",
                    "Returning",
                    "Staff",
                    "FriendOrFamily",
                    "TopManagement",
                    "Important",
                    "VeryImportant",
                    "Problematic",
                    "Cashlist",
                    "DisabledPerson",
                    "Military",
                    "Airline",
                    "HealthCompliant",
                    "InRoom",
                    "WaitingForRoom",
                    "Student",
                ]
            ]
        ]
        | NotGiven = NOT_GIVEN,
        company_id: Optional[str] | NotGiven = NOT_GIVEN,
        dietary_requirements: Optional[str] | NotGiven = NOT_GIVEN,
        drivers_license: Optional[customer_update_params.DriversLicense] | NotGiven = NOT_GIVEN,
        email: Optional[str] | NotGiven = NOT_GIVEN,
        first_name: Optional[str] | NotGiven = NOT_GIVEN,
        identity_card: Optional[customer_update_params.IdentityCard] | NotGiven = NOT_GIVEN,
        italian_destination_code: Optional[customer_update_params.ItalianDestinationCode] | NotGiven = NOT_GIVEN,
        italian_fiscal_code: Optional[customer_update_params.ItalianFiscalCode] | NotGiven = NOT_GIVEN,
        last_name: Optional[str] | NotGiven = NOT_GIVEN,
        loyalty_code: Optional[str] | NotGiven = NOT_GIVEN,
        nationality_code: Optional[str] | NotGiven = NOT_GIVEN,
        notes: Optional[str] | NotGiven = NOT_GIVEN,
        occupation: Optional[str] | NotGiven = NOT_GIVEN,
        options: Optional[
            List[
                Literal[
                    "SendMarketingEmails",
                    "Invoiceable",
                    "BillAddressObjection",
                    "SendMarketingPostalMail",
                    "SendPartnerMarketingEmails",
                    "SendPartnerMarketingPostalMail",
                    "WithdrawCardConsent",
                ]
            ]
        ]
        | NotGiven = NOT_GIVEN,
        passport: Optional[customer_update_params.Passport] | NotGiven = NOT_GIVEN,
        phone: Optional[str] | NotGiven = NOT_GIVEN,
        second_last_name: Optional[str] | NotGiven = NOT_GIVEN,
        sex: Optional[Literal["Male", "Female"]] | NotGiven = NOT_GIVEN,
        tax_identification_number: Optional[str] | NotGiven = NOT_GIVEN,
        title: Optional[Literal["Mister", "Miss", "Misses"]] | NotGiven = NOT_GIVEN,
        visa: Optional[customer_update_params.Visa] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Customer:
        """Updates personal information of a customer.

        Note that if any of the fields is
        left blank, it won't clear the field in Mews. The field will be left intact. In
        case of email update, the email will change in Mews only if there is no other
        customer profile in the hotel with such email. Otherwise an error response is
        returned. Note this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          customer_id: Unique identifier of the `Customer` to be updated.

          address: New address details.

          birth_date: New birth date in ISO 8601 format.

          birth_place: New birth place.

          car_registration_number: New registration number of the customer's car.

          chain_id: Unique identifier of the chain. Required when using `PortfolioAccessTokens`,
              ignored otherwise.

          classifications: New classifications of the customer.

          company_id: Unique identifier of `Company` the customer is associated with.

          dietary_requirements: Customer's dietary requirements, e.g. Vegan, Halal.

          drivers_license

          email: New email address.

          first_name: New first name.

          identity_card

          italian_destination_code: New Italian destination code of customer.

          italian_fiscal_code: New Italian fiscal code of customer.

          last_name: New last name.

          loyalty_code: Loyalty code of the customer.

          nationality_code: New nationality code as ISO 3166-1 code of the `Country`.

          notes: Internal notes about the customer. Old value will be overwritten.

          occupation: Occupation of the customer.

          options: Options of the customer.

          passport

          phone: New phone number.

          second_last_name: New second last name.

          sex: Sex of the customer.

          tax_identification_number: New tax identification number of the customer.

          title: Type of the title prefix of the customer.

              Note that the value should not be used as-is, but localized. For example, the
              value `Misses` should be displayed as `Mrs.` in English and `Fr.` in German.

              Mister (Mr.)

              Miss (Ms.)

              Misses (Mrs.)

              - `Mister` - Mr.
              - `Miss` - Ms.
              - `Misses` - Mrs.

          visa

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/customers/update",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "customer_id": customer_id,
                    "address": address,
                    "birth_date": birth_date,
                    "birth_place": birth_place,
                    "car_registration_number": car_registration_number,
                    "chain_id": chain_id,
                    "classifications": classifications,
                    "company_id": company_id,
                    "dietary_requirements": dietary_requirements,
                    "drivers_license": drivers_license,
                    "email": email,
                    "first_name": first_name,
                    "identity_card": identity_card,
                    "italian_destination_code": italian_destination_code,
                    "italian_fiscal_code": italian_fiscal_code,
                    "last_name": last_name,
                    "loyalty_code": loyalty_code,
                    "nationality_code": nationality_code,
                    "notes": notes,
                    "occupation": occupation,
                    "options": options,
                    "passport": passport,
                    "phone": phone,
                    "second_last_name": second_last_name,
                    "sex": sex,
                    "tax_identification_number": tax_identification_number,
                    "title": title,
                    "visa": visa,
                },
                customer_update_params.CustomerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Customer,
        )

    def list(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        extent: customer_list_params.Extent,
        limitation: customer_list_params.Limitation,
        activity_states: Optional[List[Literal["Deleted", "Active"]]] | NotGiven = NOT_GIVEN,
        chain_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        company_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        created_utc: Optional[customer_list_params.CreatedUtc] | NotGiven = NOT_GIVEN,
        customer_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        deleted_utc: Optional[customer_list_params.DeletedUtc] | NotGiven = NOT_GIVEN,
        emails: Optional[List[str]] | NotGiven = NOT_GIVEN,
        first_names: Optional[List[str]] | NotGiven = NOT_GIVEN,
        last_names: Optional[List[str]] | NotGiven = NOT_GIVEN,
        loyalty_codes: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[customer_list_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomerListResponse:
        """
        Returns all customers filtered by identifiers, emails, names and other filters.
        Note this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          extent

          limitation: Limitation on the quantity of data returned.

          activity_states: Whether to return only active, only deleted or both records.

          chain_ids: Unique identifiers of the chains. Required when using Portfolio Access Tokens,
              ignored otherwise.

          company_ids: Unique identifier of the Company the customer is associated with.

          created_utc: Interval in which Customer was created.

          customer_ids: Unique identifiers of Customers. Required if no other filter is provided.

          deleted_utc: Interval in which Customer was deleted. `ActivityStates` value `Deleted` should
              be provided with this filter to get expected results.

          emails: Emails of the
              [Customers](https://mews-systems.gitbook.io/connector-api/operations/#customer).

          first_names: First names of the
              [Customers](https://mews-systems.gitbook.io/connector-api/operations/#customer).

          last_names: Last names of the
              [Customers](https://mews-systems.gitbook.io/connector-api/operations/#customer).

          loyalty_codes: Loyalty codes of the
              [Customers](https://mews-systems.gitbook.io/connector-api/operations/#customer).

          updated_utc: Interval in which Customer was updated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/customers/getAll",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "extent": extent,
                    "limitation": limitation,
                    "activity_states": activity_states,
                    "chain_ids": chain_ids,
                    "company_ids": company_ids,
                    "created_utc": created_utc,
                    "customer_ids": customer_ids,
                    "deleted_utc": deleted_utc,
                    "emails": emails,
                    "first_names": first_names,
                    "last_names": last_names,
                    "loyalty_codes": loyalty_codes,
                    "updated_utc": updated_utc,
                },
                customer_list_params.CustomerListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerListResponse,
        )

    def add(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        last_name: str,
        overwrite_existing: bool,
        address: Optional[customer_add_params.Address] | NotGiven = NOT_GIVEN,
        birth_date: Union[str, date, None] | NotGiven = NOT_GIVEN,
        birth_place: Optional[str] | NotGiven = NOT_GIVEN,
        car_registration_number: Optional[str] | NotGiven = NOT_GIVEN,
        chain_id: Optional[str] | NotGiven = NOT_GIVEN,
        classifications: Optional[
            List[
                Literal[
                    "PaymasterAccount",
                    "Blacklist",
                    "Media",
                    "LoyaltyProgram",
                    "PreviousComplaint",
                    "Returning",
                    "Staff",
                    "FriendOrFamily",
                    "TopManagement",
                    "Important",
                    "VeryImportant",
                    "Problematic",
                    "Cashlist",
                    "DisabledPerson",
                    "Military",
                    "Airline",
                    "HealthCompliant",
                    "InRoom",
                    "WaitingForRoom",
                    "Student",
                ]
            ]
        ]
        | NotGiven = NOT_GIVEN,
        company_id: Optional[str] | NotGiven = NOT_GIVEN,
        dietary_requirements: Optional[str] | NotGiven = NOT_GIVEN,
        drivers_license: Optional[customer_add_params.DriversLicense] | NotGiven = NOT_GIVEN,
        email: Optional[str] | NotGiven = NOT_GIVEN,
        first_name: Optional[str] | NotGiven = NOT_GIVEN,
        identity_card: Optional[customer_add_params.IdentityCard] | NotGiven = NOT_GIVEN,
        italian_destination_code: Optional[str] | NotGiven = NOT_GIVEN,
        italian_fiscal_code: Optional[str] | NotGiven = NOT_GIVEN,
        loyalty_code: Optional[str] | NotGiven = NOT_GIVEN,
        nationality_code: Optional[str] | NotGiven = NOT_GIVEN,
        notes: Optional[str] | NotGiven = NOT_GIVEN,
        occupation: Optional[str] | NotGiven = NOT_GIVEN,
        options: Optional[
            List[
                Literal[
                    "SendMarketingEmails",
                    "Invoiceable",
                    "BillAddressObjection",
                    "SendMarketingPostalMail",
                    "SendPartnerMarketingEmails",
                    "SendPartnerMarketingPostalMail",
                    "WithdrawCardConsent",
                ]
            ]
        ]
        | NotGiven = NOT_GIVEN,
        passport: Optional[customer_add_params.Passport] | NotGiven = NOT_GIVEN,
        phone: Optional[str] | NotGiven = NOT_GIVEN,
        second_last_name: Optional[str] | NotGiven = NOT_GIVEN,
        sex: Optional[Literal["Male", "Female"]] | NotGiven = NOT_GIVEN,
        tax_identification_number: Optional[str] | NotGiven = NOT_GIVEN,
        title: Optional[Literal["Mister", "Miss", "Misses"]] | NotGiven = NOT_GIVEN,
        visa: Optional[customer_add_params.Visa] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Customer:
        """Adds a new customer to the system and returns details of the added customer.

        If
        a customer with the specified email already exists, and `OverwriteExisting` is
        set to `true`, then the existing customer profile information is overwritten and
        the existing customer data returned. If `OverwriteExisting` is set to `false`,
        an error response is returned. Note this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          last_name: Last name of the customer.

          overwrite_existing: Whether an existing customer should be overwritten in case of duplicity. This
              applies only to basic personal information (`Title`, `FirstName`, `LastName`,
              ...).

          address: New address details.

          birth_date: Date of birth in ISO 8601 format.

          birth_place: Place of birth.

          car_registration_number: Registration number of the customer's car.

          chain_id: Unique identifier of the chain. Required when using `PortfolioAccessTokens`,
              ignored otherwise.

          classifications: Classifications of the customer.

          company_id: Unique identifier of `Company` the customer is associated with.

          dietary_requirements: Customer's dietary requirements, e.g. Vegan, Halal.

          drivers_license

          email: Email address of the customer.

          first_name: First name of the customer.

          identity_card

          italian_destination_code: Value of Italian destination code.

          italian_fiscal_code: Value of Italian fiscal code.

          loyalty_code: Loyalty code of the customer.

          nationality_code: ISO 3166-1 code of the `Country`.

          notes: Internal notes about the customer.

          occupation: Occupation of the customer.

          options: Options of the customer.

          passport

          phone: Phone number of the customer (possibly mobile).

          second_last_name: Second last name of the customer.

          sex: Sex of the customer.

          tax_identification_number: Tax identification number of the customer.

          title: Type of the title prefix of the customer.

              Note that the value should not be used as-is, but localized. For example, the
              value `Misses` should be displayed as `Mrs.` in English and `Fr.` in German.

              Mister (Mr.)

              Miss (Ms.)

              Misses (Mrs.)

              - `Mister` - Mr.
              - `Miss` - Ms.
              - `Misses` - Mrs.

          visa

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/customers/add",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "last_name": last_name,
                    "overwrite_existing": overwrite_existing,
                    "address": address,
                    "birth_date": birth_date,
                    "birth_place": birth_place,
                    "car_registration_number": car_registration_number,
                    "chain_id": chain_id,
                    "classifications": classifications,
                    "company_id": company_id,
                    "dietary_requirements": dietary_requirements,
                    "drivers_license": drivers_license,
                    "email": email,
                    "first_name": first_name,
                    "identity_card": identity_card,
                    "italian_destination_code": italian_destination_code,
                    "italian_fiscal_code": italian_fiscal_code,
                    "loyalty_code": loyalty_code,
                    "nationality_code": nationality_code,
                    "notes": notes,
                    "occupation": occupation,
                    "options": options,
                    "passport": passport,
                    "phone": phone,
                    "second_last_name": second_last_name,
                    "sex": sex,
                    "tax_identification_number": tax_identification_number,
                    "title": title,
                    "visa": visa,
                },
                customer_add_params.CustomerAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Customer,
        )

    def add_file(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        customer_id: str,
        data: str,
        name: str,
        type: str,
        chain_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomerAddFileResponse:
        """
        Attaches the specified file to the customer profile.

        Allowed MIME types: `application/pdf`, `image/bmp`, `image/gif`, `image/jpeg`,
        `image/png`, `image/tiff`.

        Note this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/guidelines/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          customer_id: Unique identifier of the
              [Customer](https://mews-systems.gitbook.io/connector-api/operations/#customer).

          data: Base64-encoded data of the file.

          name: Name of the file.

          type: MIME type of the file (e.g. `application/pdf`).

          chain_id: Unique identifier of the chain. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/customers/addFile",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "customer_id": customer_id,
                    "data": data,
                    "name": name,
                    "type": type,
                    "chain_id": chain_id,
                },
                customer_add_file_params.CustomerAddFileParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerAddFileResponse,
        )

    def get_open_items(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        customer_ids: List[str],
        currency: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomerGetOpenItemsResponse:
        """
        Use
        [Get all payments](https://mews-systems.gitbook.io/connector-api/operations/payments#get-all-payments)
        and
        [Get all order items](https://mews-systems.gitbook.io/connector-api/operations/orderitems#get-all-order-items)
        instead.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          customer_ids: Unique identifiers of the
              [Customers](https://mews-systems.gitbook.io/connector-api/operations/#customer).

          currency: ISO-4217 code of the
              [Currency](https://mews-systems.gitbook.io/connector-api/operations/currencies/#currency)
              the item costs should be converted to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/customers/getOpenItems",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "customer_ids": customer_ids,
                    "currency": currency,
                },
                customer_get_open_items_params.CustomerGetOpenItemsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerGetOpenItemsResponse,
        )

    def merge(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        source_customer_id: str,
        target_customer_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Use
        [Merge accounts](https://mews-systems.gitbook.io/connector-api/operations/accounts#merge-accounts)
        instead.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          source_customer_id: Unique identifier of the source
              [Customer](https://mews-systems.gitbook.io/connector-api/operations/#customer).

          target_customer_id: Unique identifier of the target
              [Customer](https://mews-systems.gitbook.io/connector-api/operations/#customer).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/customers/merge",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "source_customer_id": source_customer_id,
                    "target_customer_id": target_customer_id,
                },
                customer_merge_params.CustomerMergeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def search(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        extent: Optional[customer_search_params.Extent] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        resource_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomerSearchResponse:
        """
        Searches for customers that are active at the moment in the enterprise (e.g.
        companions of checked-in reservations or paymasters).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          extent

          name: Name to search by (applies to first name, last name, and full name).

          resource_id: Identifier of
              [Resource](https://mews-systems.gitbook.io/connector-api/operations/resources/#resource)
              to search by (members of reservation assigned there will be returned).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/customers/search",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "extent": extent,
                    "name": name,
                    "resource_id": resource_id,
                },
                customer_search_params.CustomerSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerSearchResponse,
        )


class AsyncCustomersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCustomersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return AsyncCustomersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return AsyncCustomersResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        customer_id: str,
        address: Optional[customer_update_params.Address] | NotGiven = NOT_GIVEN,
        birth_date: Union[str, date, None] | NotGiven = NOT_GIVEN,
        birth_place: Optional[str] | NotGiven = NOT_GIVEN,
        car_registration_number: Optional[str] | NotGiven = NOT_GIVEN,
        chain_id: Optional[str] | NotGiven = NOT_GIVEN,
        classifications: Optional[
            List[
                Literal[
                    "PaymasterAccount",
                    "Blacklist",
                    "Media",
                    "LoyaltyProgram",
                    "PreviousComplaint",
                    "Returning",
                    "Staff",
                    "FriendOrFamily",
                    "TopManagement",
                    "Important",
                    "VeryImportant",
                    "Problematic",
                    "Cashlist",
                    "DisabledPerson",
                    "Military",
                    "Airline",
                    "HealthCompliant",
                    "InRoom",
                    "WaitingForRoom",
                    "Student",
                ]
            ]
        ]
        | NotGiven = NOT_GIVEN,
        company_id: Optional[str] | NotGiven = NOT_GIVEN,
        dietary_requirements: Optional[str] | NotGiven = NOT_GIVEN,
        drivers_license: Optional[customer_update_params.DriversLicense] | NotGiven = NOT_GIVEN,
        email: Optional[str] | NotGiven = NOT_GIVEN,
        first_name: Optional[str] | NotGiven = NOT_GIVEN,
        identity_card: Optional[customer_update_params.IdentityCard] | NotGiven = NOT_GIVEN,
        italian_destination_code: Optional[customer_update_params.ItalianDestinationCode] | NotGiven = NOT_GIVEN,
        italian_fiscal_code: Optional[customer_update_params.ItalianFiscalCode] | NotGiven = NOT_GIVEN,
        last_name: Optional[str] | NotGiven = NOT_GIVEN,
        loyalty_code: Optional[str] | NotGiven = NOT_GIVEN,
        nationality_code: Optional[str] | NotGiven = NOT_GIVEN,
        notes: Optional[str] | NotGiven = NOT_GIVEN,
        occupation: Optional[str] | NotGiven = NOT_GIVEN,
        options: Optional[
            List[
                Literal[
                    "SendMarketingEmails",
                    "Invoiceable",
                    "BillAddressObjection",
                    "SendMarketingPostalMail",
                    "SendPartnerMarketingEmails",
                    "SendPartnerMarketingPostalMail",
                    "WithdrawCardConsent",
                ]
            ]
        ]
        | NotGiven = NOT_GIVEN,
        passport: Optional[customer_update_params.Passport] | NotGiven = NOT_GIVEN,
        phone: Optional[str] | NotGiven = NOT_GIVEN,
        second_last_name: Optional[str] | NotGiven = NOT_GIVEN,
        sex: Optional[Literal["Male", "Female"]] | NotGiven = NOT_GIVEN,
        tax_identification_number: Optional[str] | NotGiven = NOT_GIVEN,
        title: Optional[Literal["Mister", "Miss", "Misses"]] | NotGiven = NOT_GIVEN,
        visa: Optional[customer_update_params.Visa] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Customer:
        """Updates personal information of a customer.

        Note that if any of the fields is
        left blank, it won't clear the field in Mews. The field will be left intact. In
        case of email update, the email will change in Mews only if there is no other
        customer profile in the hotel with such email. Otherwise an error response is
        returned. Note this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          customer_id: Unique identifier of the `Customer` to be updated.

          address: New address details.

          birth_date: New birth date in ISO 8601 format.

          birth_place: New birth place.

          car_registration_number: New registration number of the customer's car.

          chain_id: Unique identifier of the chain. Required when using `PortfolioAccessTokens`,
              ignored otherwise.

          classifications: New classifications of the customer.

          company_id: Unique identifier of `Company` the customer is associated with.

          dietary_requirements: Customer's dietary requirements, e.g. Vegan, Halal.

          drivers_license

          email: New email address.

          first_name: New first name.

          identity_card

          italian_destination_code: New Italian destination code of customer.

          italian_fiscal_code: New Italian fiscal code of customer.

          last_name: New last name.

          loyalty_code: Loyalty code of the customer.

          nationality_code: New nationality code as ISO 3166-1 code of the `Country`.

          notes: Internal notes about the customer. Old value will be overwritten.

          occupation: Occupation of the customer.

          options: Options of the customer.

          passport

          phone: New phone number.

          second_last_name: New second last name.

          sex: Sex of the customer.

          tax_identification_number: New tax identification number of the customer.

          title: Type of the title prefix of the customer.

              Note that the value should not be used as-is, but localized. For example, the
              value `Misses` should be displayed as `Mrs.` in English and `Fr.` in German.

              Mister (Mr.)

              Miss (Ms.)

              Misses (Mrs.)

              - `Mister` - Mr.
              - `Miss` - Ms.
              - `Misses` - Mrs.

          visa

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/customers/update",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "customer_id": customer_id,
                    "address": address,
                    "birth_date": birth_date,
                    "birth_place": birth_place,
                    "car_registration_number": car_registration_number,
                    "chain_id": chain_id,
                    "classifications": classifications,
                    "company_id": company_id,
                    "dietary_requirements": dietary_requirements,
                    "drivers_license": drivers_license,
                    "email": email,
                    "first_name": first_name,
                    "identity_card": identity_card,
                    "italian_destination_code": italian_destination_code,
                    "italian_fiscal_code": italian_fiscal_code,
                    "last_name": last_name,
                    "loyalty_code": loyalty_code,
                    "nationality_code": nationality_code,
                    "notes": notes,
                    "occupation": occupation,
                    "options": options,
                    "passport": passport,
                    "phone": phone,
                    "second_last_name": second_last_name,
                    "sex": sex,
                    "tax_identification_number": tax_identification_number,
                    "title": title,
                    "visa": visa,
                },
                customer_update_params.CustomerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Customer,
        )

    async def list(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        extent: customer_list_params.Extent,
        limitation: customer_list_params.Limitation,
        activity_states: Optional[List[Literal["Deleted", "Active"]]] | NotGiven = NOT_GIVEN,
        chain_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        company_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        created_utc: Optional[customer_list_params.CreatedUtc] | NotGiven = NOT_GIVEN,
        customer_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        deleted_utc: Optional[customer_list_params.DeletedUtc] | NotGiven = NOT_GIVEN,
        emails: Optional[List[str]] | NotGiven = NOT_GIVEN,
        first_names: Optional[List[str]] | NotGiven = NOT_GIVEN,
        last_names: Optional[List[str]] | NotGiven = NOT_GIVEN,
        loyalty_codes: Optional[List[str]] | NotGiven = NOT_GIVEN,
        updated_utc: Optional[customer_list_params.UpdatedUtc] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomerListResponse:
        """
        Returns all customers filtered by identifiers, emails, names and other filters.
        Note this operation uses
        [Pagination](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/)
        and supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          extent

          limitation: Limitation on the quantity of data returned.

          activity_states: Whether to return only active, only deleted or both records.

          chain_ids: Unique identifiers of the chains. Required when using Portfolio Access Tokens,
              ignored otherwise.

          company_ids: Unique identifier of the Company the customer is associated with.

          created_utc: Interval in which Customer was created.

          customer_ids: Unique identifiers of Customers. Required if no other filter is provided.

          deleted_utc: Interval in which Customer was deleted. `ActivityStates` value `Deleted` should
              be provided with this filter to get expected results.

          emails: Emails of the
              [Customers](https://mews-systems.gitbook.io/connector-api/operations/#customer).

          first_names: First names of the
              [Customers](https://mews-systems.gitbook.io/connector-api/operations/#customer).

          last_names: Last names of the
              [Customers](https://mews-systems.gitbook.io/connector-api/operations/#customer).

          loyalty_codes: Loyalty codes of the
              [Customers](https://mews-systems.gitbook.io/connector-api/operations/#customer).

          updated_utc: Interval in which Customer was updated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/customers/getAll",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "extent": extent,
                    "limitation": limitation,
                    "activity_states": activity_states,
                    "chain_ids": chain_ids,
                    "company_ids": company_ids,
                    "created_utc": created_utc,
                    "customer_ids": customer_ids,
                    "deleted_utc": deleted_utc,
                    "emails": emails,
                    "first_names": first_names,
                    "last_names": last_names,
                    "loyalty_codes": loyalty_codes,
                    "updated_utc": updated_utc,
                },
                customer_list_params.CustomerListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerListResponse,
        )

    async def add(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        last_name: str,
        overwrite_existing: bool,
        address: Optional[customer_add_params.Address] | NotGiven = NOT_GIVEN,
        birth_date: Union[str, date, None] | NotGiven = NOT_GIVEN,
        birth_place: Optional[str] | NotGiven = NOT_GIVEN,
        car_registration_number: Optional[str] | NotGiven = NOT_GIVEN,
        chain_id: Optional[str] | NotGiven = NOT_GIVEN,
        classifications: Optional[
            List[
                Literal[
                    "PaymasterAccount",
                    "Blacklist",
                    "Media",
                    "LoyaltyProgram",
                    "PreviousComplaint",
                    "Returning",
                    "Staff",
                    "FriendOrFamily",
                    "TopManagement",
                    "Important",
                    "VeryImportant",
                    "Problematic",
                    "Cashlist",
                    "DisabledPerson",
                    "Military",
                    "Airline",
                    "HealthCompliant",
                    "InRoom",
                    "WaitingForRoom",
                    "Student",
                ]
            ]
        ]
        | NotGiven = NOT_GIVEN,
        company_id: Optional[str] | NotGiven = NOT_GIVEN,
        dietary_requirements: Optional[str] | NotGiven = NOT_GIVEN,
        drivers_license: Optional[customer_add_params.DriversLicense] | NotGiven = NOT_GIVEN,
        email: Optional[str] | NotGiven = NOT_GIVEN,
        first_name: Optional[str] | NotGiven = NOT_GIVEN,
        identity_card: Optional[customer_add_params.IdentityCard] | NotGiven = NOT_GIVEN,
        italian_destination_code: Optional[str] | NotGiven = NOT_GIVEN,
        italian_fiscal_code: Optional[str] | NotGiven = NOT_GIVEN,
        loyalty_code: Optional[str] | NotGiven = NOT_GIVEN,
        nationality_code: Optional[str] | NotGiven = NOT_GIVEN,
        notes: Optional[str] | NotGiven = NOT_GIVEN,
        occupation: Optional[str] | NotGiven = NOT_GIVEN,
        options: Optional[
            List[
                Literal[
                    "SendMarketingEmails",
                    "Invoiceable",
                    "BillAddressObjection",
                    "SendMarketingPostalMail",
                    "SendPartnerMarketingEmails",
                    "SendPartnerMarketingPostalMail",
                    "WithdrawCardConsent",
                ]
            ]
        ]
        | NotGiven = NOT_GIVEN,
        passport: Optional[customer_add_params.Passport] | NotGiven = NOT_GIVEN,
        phone: Optional[str] | NotGiven = NOT_GIVEN,
        second_last_name: Optional[str] | NotGiven = NOT_GIVEN,
        sex: Optional[Literal["Male", "Female"]] | NotGiven = NOT_GIVEN,
        tax_identification_number: Optional[str] | NotGiven = NOT_GIVEN,
        title: Optional[Literal["Mister", "Miss", "Misses"]] | NotGiven = NOT_GIVEN,
        visa: Optional[customer_add_params.Visa] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Customer:
        """Adds a new customer to the system and returns details of the added customer.

        If
        a customer with the specified email already exists, and `OverwriteExisting` is
        set to `true`, then the existing customer profile information is overwritten and
        the existing customer data returned. If `OverwriteExisting` is set to `false`,
        an error response is returned. Note this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          last_name: Last name of the customer.

          overwrite_existing: Whether an existing customer should be overwritten in case of duplicity. This
              applies only to basic personal information (`Title`, `FirstName`, `LastName`,
              ...).

          address: New address details.

          birth_date: Date of birth in ISO 8601 format.

          birth_place: Place of birth.

          car_registration_number: Registration number of the customer's car.

          chain_id: Unique identifier of the chain. Required when using `PortfolioAccessTokens`,
              ignored otherwise.

          classifications: Classifications of the customer.

          company_id: Unique identifier of `Company` the customer is associated with.

          dietary_requirements: Customer's dietary requirements, e.g. Vegan, Halal.

          drivers_license

          email: Email address of the customer.

          first_name: First name of the customer.

          identity_card

          italian_destination_code: Value of Italian destination code.

          italian_fiscal_code: Value of Italian fiscal code.

          loyalty_code: Loyalty code of the customer.

          nationality_code: ISO 3166-1 code of the `Country`.

          notes: Internal notes about the customer.

          occupation: Occupation of the customer.

          options: Options of the customer.

          passport

          phone: Phone number of the customer (possibly mobile).

          second_last_name: Second last name of the customer.

          sex: Sex of the customer.

          tax_identification_number: Tax identification number of the customer.

          title: Type of the title prefix of the customer.

              Note that the value should not be used as-is, but localized. For example, the
              value `Misses` should be displayed as `Mrs.` in English and `Fr.` in German.

              Mister (Mr.)

              Miss (Ms.)

              Misses (Mrs.)

              - `Mister` - Mr.
              - `Miss` - Ms.
              - `Misses` - Mrs.

          visa

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/customers/add",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "last_name": last_name,
                    "overwrite_existing": overwrite_existing,
                    "address": address,
                    "birth_date": birth_date,
                    "birth_place": birth_place,
                    "car_registration_number": car_registration_number,
                    "chain_id": chain_id,
                    "classifications": classifications,
                    "company_id": company_id,
                    "dietary_requirements": dietary_requirements,
                    "drivers_license": drivers_license,
                    "email": email,
                    "first_name": first_name,
                    "identity_card": identity_card,
                    "italian_destination_code": italian_destination_code,
                    "italian_fiscal_code": italian_fiscal_code,
                    "loyalty_code": loyalty_code,
                    "nationality_code": nationality_code,
                    "notes": notes,
                    "occupation": occupation,
                    "options": options,
                    "passport": passport,
                    "phone": phone,
                    "second_last_name": second_last_name,
                    "sex": sex,
                    "tax_identification_number": tax_identification_number,
                    "title": title,
                    "visa": visa,
                },
                customer_add_params.CustomerAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Customer,
        )

    async def add_file(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        customer_id: str,
        data: str,
        name: str,
        type: str,
        chain_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomerAddFileResponse:
        """
        Attaches the specified file to the customer profile.

        Allowed MIME types: `application/pdf`, `image/bmp`, `image/gif`, `image/jpeg`,
        `image/png`, `image/tiff`.

        Note this operation supports
        [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/guidelines/multi-property).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          customer_id: Unique identifier of the
              [Customer](https://mews-systems.gitbook.io/connector-api/operations/#customer).

          data: Base64-encoded data of the file.

          name: Name of the file.

          type: MIME type of the file (e.g. `application/pdf`).

          chain_id: Unique identifier of the chain. Required when using
              [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
              ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/customers/addFile",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "customer_id": customer_id,
                    "data": data,
                    "name": name,
                    "type": type,
                    "chain_id": chain_id,
                },
                customer_add_file_params.CustomerAddFileParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerAddFileResponse,
        )

    async def get_open_items(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        customer_ids: List[str],
        currency: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomerGetOpenItemsResponse:
        """
        Use
        [Get all payments](https://mews-systems.gitbook.io/connector-api/operations/payments#get-all-payments)
        and
        [Get all order items](https://mews-systems.gitbook.io/connector-api/operations/orderitems#get-all-order-items)
        instead.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          customer_ids: Unique identifiers of the
              [Customers](https://mews-systems.gitbook.io/connector-api/operations/#customer).

          currency: ISO-4217 code of the
              [Currency](https://mews-systems.gitbook.io/connector-api/operations/currencies/#currency)
              the item costs should be converted to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/customers/getOpenItems",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "customer_ids": customer_ids,
                    "currency": currency,
                },
                customer_get_open_items_params.CustomerGetOpenItemsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerGetOpenItemsResponse,
        )

    async def merge(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        source_customer_id: str,
        target_customer_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Use
        [Merge accounts](https://mews-systems.gitbook.io/connector-api/operations/accounts#merge-accounts)
        instead.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          source_customer_id: Unique identifier of the source
              [Customer](https://mews-systems.gitbook.io/connector-api/operations/#customer).

          target_customer_id: Unique identifier of the target
              [Customer](https://mews-systems.gitbook.io/connector-api/operations/#customer).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/customers/merge",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "source_customer_id": source_customer_id,
                    "target_customer_id": target_customer_id,
                },
                customer_merge_params.CustomerMergeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def search(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        extent: Optional[customer_search_params.Extent] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        resource_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomerSearchResponse:
        """
        Searches for customers that are active at the moment in the enterprise (e.g.
        companions of checked-in reservations or paymasters).

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          extent

          name: Name to search by (applies to first name, last name, and full name).

          resource_id: Identifier of
              [Resource](https://mews-systems.gitbook.io/connector-api/operations/resources/#resource)
              to search by (members of reservation assigned there will be returned).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/customers/search",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "extent": extent,
                    "name": name,
                    "resource_id": resource_id,
                },
                customer_search_params.CustomerSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerSearchResponse,
        )


class CustomersResourceWithRawResponse:
    def __init__(self, customers: CustomersResource) -> None:
        self._customers = customers

        self.update = to_raw_response_wrapper(
            customers.update,
        )
        self.list = to_raw_response_wrapper(
            customers.list,
        )
        self.add = to_raw_response_wrapper(
            customers.add,
        )
        self.add_file = to_raw_response_wrapper(
            customers.add_file,
        )
        self.get_open_items = to_raw_response_wrapper(
            customers.get_open_items,
        )
        self.merge = to_raw_response_wrapper(
            customers.merge,
        )
        self.search = to_raw_response_wrapper(
            customers.search,
        )


class AsyncCustomersResourceWithRawResponse:
    def __init__(self, customers: AsyncCustomersResource) -> None:
        self._customers = customers

        self.update = async_to_raw_response_wrapper(
            customers.update,
        )
        self.list = async_to_raw_response_wrapper(
            customers.list,
        )
        self.add = async_to_raw_response_wrapper(
            customers.add,
        )
        self.add_file = async_to_raw_response_wrapper(
            customers.add_file,
        )
        self.get_open_items = async_to_raw_response_wrapper(
            customers.get_open_items,
        )
        self.merge = async_to_raw_response_wrapper(
            customers.merge,
        )
        self.search = async_to_raw_response_wrapper(
            customers.search,
        )


class CustomersResourceWithStreamingResponse:
    def __init__(self, customers: CustomersResource) -> None:
        self._customers = customers

        self.update = to_streamed_response_wrapper(
            customers.update,
        )
        self.list = to_streamed_response_wrapper(
            customers.list,
        )
        self.add = to_streamed_response_wrapper(
            customers.add,
        )
        self.add_file = to_streamed_response_wrapper(
            customers.add_file,
        )
        self.get_open_items = to_streamed_response_wrapper(
            customers.get_open_items,
        )
        self.merge = to_streamed_response_wrapper(
            customers.merge,
        )
        self.search = to_streamed_response_wrapper(
            customers.search,
        )


class AsyncCustomersResourceWithStreamingResponse:
    def __init__(self, customers: AsyncCustomersResource) -> None:
        self._customers = customers

        self.update = async_to_streamed_response_wrapper(
            customers.update,
        )
        self.list = async_to_streamed_response_wrapper(
            customers.list,
        )
        self.add = async_to_streamed_response_wrapper(
            customers.add,
        )
        self.add_file = async_to_streamed_response_wrapper(
            customers.add_file,
        )
        self.get_open_items = async_to_streamed_response_wrapper(
            customers.get_open_items,
        )
        self.merge = async_to_streamed_response_wrapper(
            customers.merge,
        )
        self.search = async_to_streamed_response_wrapper(
            customers.search,
        )
