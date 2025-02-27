# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["PaymentAddExternalParams", "Amount"]


class PaymentAddExternalParams(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="AccessToken")]]
    """Access token of the client application."""

    account_id: Required[Annotated[str, PropertyInfo(alias="AccountId")]]
    """
    Unique identifier of the
    [Customer](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer)
    or
    [Company](https://mews-systems.gitbook.io/connector-api/operations/companies/#company).
    Company billing may not be enabled for your integration.
    """

    amount: Required[Annotated[Amount, PropertyInfo(alias="Amount")]]

    client: Required[Annotated[str, PropertyInfo(alias="Client")]]
    """Name and version of the client application."""

    client_token: Required[Annotated[str, PropertyInfo(alias="ClientToken")]]
    """Token identifying the client application."""

    accounting_category_id: Annotated[Optional[str], PropertyInfo(alias="AccountingCategoryId")]
    """
    Unique identifier of an
    [Accounting category](https://mews-systems.gitbook.io/connector-api/operations/accountingcategories/#accounting-category)
    to be assigned to the external payment.
    """

    bill_id: Annotated[Optional[str], PropertyInfo(alias="BillId")]
    """Unique identifier of an open bill of the customer where to assign the payment."""

    customer_id: Annotated[Optional[str], PropertyInfo(alias="CustomerId")]
    """
    Unique identifier of the
    [Customer](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer).
    **Deprecated!**
    """

    enterprise_id: Annotated[Optional[str], PropertyInfo(alias="EnterpriseId")]
    """Unique identifier of the enterprise.

    Required when using
    [Portfolio Access Tokens](https://mews-systems.gitbook.io/connector-api/concepts/multi-property),
    ignored otherwise.
    """

    external_identifier: Annotated[Optional[str], PropertyInfo(alias="ExternalIdentifier")]
    """Identifier of the payment from external system."""

    notes: Annotated[Optional[str], PropertyInfo(alias="Notes")]
    """Additional payment notes."""

    reservation_id: Annotated[Optional[str], PropertyInfo(alias="ReservationId")]
    """Unique identifier of the reservation the payment belongs to."""

    type: Annotated[
        Optional[
            Literal[
                "Unspecified",
                "BadDebts",
                "Bacs",
                "WireTransfer",
                "Invoice",
                "ExchangeRateDifference",
                "Complimentary",
                "Reseller",
                "ExchangeRoundingDifference",
                "Barter",
                "Commission",
                "BankCharges",
                "CrossSettlement",
                "Cash",
                "CreditCard",
                "Prepayment",
                "Cheque",
                "Bancontact",
                "IDeal",
                "PayPal",
                "GiftCard",
                "LoyaltyPoints",
                "ChequeVacances",
                "OnlinePayment",
                "CardCheck",
                "PaymentHubRedirection",
                "Voucher",
                "MasterCard",
                "Visa",
                "Amex",
                "Discover",
                "DinersClub",
                "Jcb",
                "UnionPay",
                "Twint",
                "Reka",
                "LoyaltyCard",
                "PosDiningAndSpaReward",
                "DirectDebit",
                "DepositCheck",
                "DepositCash",
                "DepositCreditCard",
                "DepositWireTransfer",
            ]
        ],
        PropertyInfo(alias="Type"),
    ]
    """Unspecified (Unspecified (unavailable in French Legal Environment))

    BadDebts (Bad debts)

    Bacs (Bacs payment)

    WireTransfer (Wire transfer)

    Invoice (Invoice)

    ExchangeRateDifference (Exchange rate difference)

    Complimentary (Complimentary)

    Reseller (Reseller)

    ExchangeRoundingDifference (Exchange rounding difference)

    Barter (Barter)

    Commission (Commission)

    BankCharges (Bank charges)

    CrossSettlement (Cross settlement)

    Cash (Cash)

    CreditCard (Credit card)

    Prepayment (Prepayment)

    Cheque (Cheque)

    Bancontact (Bancontact)

    IDeal (iDeal)

    PayPal (PayPal)

    GiftCard (Gift card)

    LoyaltyPoints (Loyalty points)

    ChequeVacances (Chèque-Vacances)

    OnlinePayment (Online payment)

    CardCheck (Card check)

    PaymentHubRedirection (Payment hub redirection)

    Voucher (Voucher)

    MasterCard (MasterCard)

    Visa (Visa)

    Amex (American Express)

    Discover (Discover)

    DinersClub (Diners Club)

    Jcb (JCB)

    UnionPay (UnionPay)

    Twint (TWINT)

    Reka (Reka)

    LoyaltyCard (Loyalty card)

    PosDiningAndSpaReward (POS Dining & Spa Reward)

    DirectDebit (Direct debit)

    DepositCheck (Deposit - check)

    DepositCash (Deposit - cash)

    DepositCreditCard (Deposit - credit card)

    DepositWireTransfer (Deposit - wire transfer)

    - `Unspecified` - Unspecified (unavailable in French Legal Environment)
    - `BadDebts` - Bad debts
    - `Bacs` - Bacs payment
    - `WireTransfer` - Wire transfer
    - `Invoice` - Invoice
    - `ExchangeRateDifference` - Exchange rate difference
    - `Complimentary` - Complimentary
    - `Reseller` - Reseller
    - `ExchangeRoundingDifference` - Exchange rounding difference
    - `Barter` - Barter
    - `Commission` - Commission
    - `BankCharges` - Bank charges
    - `CrossSettlement` - Cross settlement
    - `Cash` - Cash
    - `CreditCard` - Credit card
    - `Prepayment` - Prepayment
    - `Cheque` - Cheque
    - `Bancontact` - Bancontact
    - `IDeal` - iDeal
    - `PayPal` - PayPal
    - `GiftCard` - Gift card
    - `LoyaltyPoints` - Loyalty points
    - `ChequeVacances` - Chèque-Vacances
    - `OnlinePayment` - Online payment
    - `CardCheck` - Card check
    - `PaymentHubRedirection` - Payment hub redirection
    - `Voucher` - Voucher
    - `MasterCard` - MasterCard
    - `Visa` - Visa
    - `Amex` - American Express
    - `Discover` - Discover
    - `DinersClub` - Diners Club
    - `Jcb` - JCB
    - `UnionPay` - UnionPay
    - `Twint` - TWINT
    - `Reka` - Reka
    - `LoyaltyCard` - Loyalty card
    - `PosDiningAndSpaReward` - POS Dining & Spa Reward
    - `DirectDebit` - Direct debit
    - `DepositCheck` - Deposit - check
    - `DepositCash` - Deposit - cash
    - `DepositCreditCard` - Deposit - credit card
    - `DepositWireTransfer` - Deposit - wire transfer
    """


class Amount(TypedDict, total=False):
    currency: Required[Annotated[str, PropertyInfo(alias="Currency")]]
    """ISO-4217 code of the `Currency`."""

    gross_value: Annotated[Optional[float], PropertyInfo(alias="GrossValue")]
    """Gross value including all taxes."""

    net_value: Annotated[Optional[float], PropertyInfo(alias="NetValue")]
    """Net value in case the item is taxed."""

    tax_codes: Annotated[Optional[List[str]], PropertyInfo(alias="TaxCodes")]
    """The tax values applied."""
