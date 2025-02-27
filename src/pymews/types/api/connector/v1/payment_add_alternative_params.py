# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["PaymentAddAlternativeParams", "Amount", "Data", "DataIdeal", "DataSepaDirectDebit"]


class PaymentAddAlternativeParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    amount: Required[Annotated[Amount, PropertyInfo(alias="Amount")]]
    """Price of the product that overrides the price defined in Mews."""

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    customer_id: Required[Annotated[str, PropertyInfo(alias="CustomerId")]]
    """
    Unique identifier of the
    [Customer](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer).
    """

    data: Required[Annotated[Data, PropertyInfo(alias="Data")]]
    """Data specific to particular alternative payment method."""

    method: Annotated[Optional[Literal["Ideal", "ApplePay", "GooglePay"]], PropertyInfo(alias="Method")]
    """Payment method to use for the alternative payment."""

    redirect_url: Annotated[Optional[str], PropertyInfo(alias="RedirectUrl")]
    """URL where the customer will be redirected after completing their payment."""

    reservation_id: Annotated[Optional[str], PropertyInfo(alias="ReservationId")]
    """Unique identifier of the reservation the payment belongs to."""


class Amount(TypedDict, total=False):
    currency: Required[Annotated[str, PropertyInfo(alias="Currency")]]

    tax_codes: Required[Annotated[List[str], PropertyInfo(alias="TaxCodes")]]

    gross_value: Annotated[Optional[float], PropertyInfo(alias="GrossValue")]

    net_value: Annotated[Optional[float], PropertyInfo(alias="NetValue")]


class DataIdeal(TypedDict, total=False):
    redirect_url: Required[Annotated[str, PropertyInfo(alias="RedirectUrl")]]
    """URL where the customer will be redirected after completing their iDEAL payment."""


class DataSepaDirectDebit(TypedDict, total=False):
    email: Required[Annotated[str, PropertyInfo(alias="Email")]]
    """Email address of the customer."""

    iban: Required[Annotated[str, PropertyInfo(alias="Iban")]]
    """The customer's bank account number in IBAN format."""

    name: Required[Annotated[str, PropertyInfo(alias="Name")]]
    """Full name of the customer."""

    remote_ip_address: Required[Annotated[str, PropertyInfo(alias="RemoteIpAddress")]]
    """The IP address from which the Mandate was accepted by the customer."""

    user_agent: Required[Annotated[str, PropertyInfo(alias="UserAgent")]]
    """
    The user agent of the browser from which the Mandate was accepted by the
    customer.
    """


class Data(TypedDict, total=False):
    discriminator: Required[
        Annotated[Literal["Ideal", "ApplePay", "GooglePay", "SepaDirectDebit"], PropertyInfo(alias="Discriminator")]
    ]
    """Ideal (iDEAL data.)

    ApplePay (No additional data.)

    GooglePay (No additional data.)

    SepaDirectDebit (SEPA Direct Debit data.)

    - `Ideal` - iDEAL data.
    - `ApplePay` - No additional data.
    - `GooglePay` - No additional data.
    - `SepaDirectDebit` - SEPA Direct Debit data.
    """

    ideal: Annotated[Optional[DataIdeal], PropertyInfo(alias="Ideal")]
    """iDEAL payment method data. Required when `Discriminator` is `Ideal`."""

    sepa_direct_debit: Annotated[Optional[DataSepaDirectDebit], PropertyInfo(alias="SepaDirectDebit")]
    """SEPA Direct Debit payment method data.

    Required when `Discriminator` is `SepaDirectDebit`.
    """
