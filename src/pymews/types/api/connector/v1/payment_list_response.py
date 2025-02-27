# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = [
    "PaymentListResponse",
    "Payment",
    "PaymentAmount",
    "PaymentAmountBreakdown",
    "PaymentAmountBreakdownItem",
    "PaymentAmountTaxValue",
    "PaymentOriginalAmount",
    "PaymentOriginalAmountBreakdown",
    "PaymentOriginalAmountBreakdownItem",
    "PaymentOriginalAmountTaxValue",
    "PaymentData",
    "PaymentDataCreditCard",
    "PaymentDataCreditCardTransaction",
    "PaymentDataCreditCardTransactionChargedAmount",
    "PaymentDataCreditCardTransactionChargedAmountBreakdown",
    "PaymentDataCreditCardTransactionChargedAmountBreakdownItem",
    "PaymentDataCreditCardTransactionChargedAmountTaxValue",
    "PaymentDataCreditCardTransactionAdjustedFee",
    "PaymentDataCreditCardTransactionAdjustedFeeBreakdown",
    "PaymentDataCreditCardTransactionAdjustedFeeBreakdownItem",
    "PaymentDataCreditCardTransactionAdjustedFeeTaxValue",
    "PaymentDataCreditCardTransactionFee",
    "PaymentDataCreditCardTransactionFeeBreakdown",
    "PaymentDataCreditCardTransactionFeeBreakdownItem",
    "PaymentDataCreditCardTransactionFeeTaxValue",
    "PaymentDataCreditCardTransactionSettledAmount",
    "PaymentDataCreditCardTransactionSettledAmountBreakdown",
    "PaymentDataCreditCardTransactionSettledAmountBreakdownItem",
    "PaymentDataCreditCardTransactionSettledAmountTaxValue",
    "PaymentDataExternal",
    "PaymentDataGhost",
    "PaymentDataInvoice",
]


class PaymentAmountBreakdownItem(BaseModel):
    net_value: float = FieldInfo(alias="NetValue")
    """The net value that the tax is calculated from."""

    tax_value: float = FieldInfo(alias="TaxValue")
    """The value of the tax."""

    tax_rate_code: Optional[str] = FieldInfo(alias="TaxRateCode", default=None)
    """Tax rate code for the item. `null` for untaxed amounts."""


class PaymentAmountBreakdown(BaseModel):
    items: List[PaymentAmountBreakdownItem] = FieldInfo(alias="Items")
    """Tax breakdown items per each tax rate applied."""


class PaymentAmountTaxValue(BaseModel):
    value: float = FieldInfo(alias="Value")
    """Amount of tax applied."""

    code: Optional[str] = FieldInfo(alias="Code", default=None)
    """Code corresponding to tax type."""


class PaymentAmount(BaseModel):
    breakdown: PaymentAmountBreakdown = FieldInfo(alias="Breakdown")
    """Information about individual tax amounts."""

    currency: str = FieldInfo(alias="Currency")
    """
    ISO-4217 code of the
    [Currency](https://mews-systems.gitbook.io/connector-api/operations/currencies/#currency).
    """

    gross_value: float = FieldInfo(alias="GrossValue")
    """Gross value including all taxes."""

    net_value: float = FieldInfo(alias="NetValue")
    """Net value without taxes."""

    tax_values: List[PaymentAmountTaxValue] = FieldInfo(alias="TaxValues")
    """The tax values applied."""


class PaymentOriginalAmountBreakdownItem(BaseModel):
    net_value: float = FieldInfo(alias="NetValue")
    """The net value that the tax is calculated from."""

    tax_value: float = FieldInfo(alias="TaxValue")
    """The value of the tax."""

    tax_rate_code: Optional[str] = FieldInfo(alias="TaxRateCode", default=None)
    """Tax rate code for the item. `null` for untaxed amounts."""


class PaymentOriginalAmountBreakdown(BaseModel):
    items: List[PaymentOriginalAmountBreakdownItem] = FieldInfo(alias="Items")
    """Tax breakdown items per each tax rate applied."""


class PaymentOriginalAmountTaxValue(BaseModel):
    value: float = FieldInfo(alias="Value")
    """Amount of tax applied."""

    code: Optional[str] = FieldInfo(alias="Code", default=None)
    """Code corresponding to tax type."""


class PaymentOriginalAmount(BaseModel):
    breakdown: PaymentOriginalAmountBreakdown = FieldInfo(alias="Breakdown")
    """Information about individual tax amounts."""

    currency: str = FieldInfo(alias="Currency")
    """
    ISO-4217 code of the
    [Currency](https://mews-systems.gitbook.io/connector-api/operations/currencies/#currency).
    """

    gross_value: float = FieldInfo(alias="GrossValue")
    """Gross value including all taxes."""

    net_value: float = FieldInfo(alias="NetValue")
    """Net value without taxes."""

    tax_values: List[PaymentOriginalAmountTaxValue] = FieldInfo(alias="TaxValues")
    """The tax values applied."""


class PaymentDataCreditCardTransactionChargedAmountBreakdownItem(BaseModel):
    net_value: float = FieldInfo(alias="NetValue")
    """The net value that the tax is calculated from."""

    tax_value: float = FieldInfo(alias="TaxValue")
    """The value of the tax."""

    tax_rate_code: Optional[str] = FieldInfo(alias="TaxRateCode", default=None)
    """Tax rate code for the item. `null` for untaxed amounts."""


class PaymentDataCreditCardTransactionChargedAmountBreakdown(BaseModel):
    items: List[PaymentDataCreditCardTransactionChargedAmountBreakdownItem] = FieldInfo(alias="Items")
    """Tax breakdown items per each tax rate applied."""


class PaymentDataCreditCardTransactionChargedAmountTaxValue(BaseModel):
    value: float = FieldInfo(alias="Value")
    """Amount of tax applied."""

    code: Optional[str] = FieldInfo(alias="Code", default=None)
    """Code corresponding to tax type."""


class PaymentDataCreditCardTransactionChargedAmount(BaseModel):
    breakdown: PaymentDataCreditCardTransactionChargedAmountBreakdown = FieldInfo(alias="Breakdown")
    """Information about individual tax amounts."""

    currency: str = FieldInfo(alias="Currency")
    """
    ISO-4217 code of the
    [Currency](https://mews-systems.gitbook.io/connector-api/operations/currencies/#currency).
    """

    gross_value: float = FieldInfo(alias="GrossValue")
    """Gross value including all taxes."""

    net_value: float = FieldInfo(alias="NetValue")
    """Net value without taxes."""

    tax_values: List[PaymentDataCreditCardTransactionChargedAmountTaxValue] = FieldInfo(alias="TaxValues")
    """The tax values applied."""

    net: Optional[float] = FieldInfo(alias="Net", default=None)

    tax: Optional[float] = FieldInfo(alias="Tax", default=None)

    tax_rate: Optional[float] = FieldInfo(alias="TaxRate", default=None)

    value: Optional[float] = FieldInfo(alias="Value", default=None)


class PaymentDataCreditCardTransactionAdjustedFeeBreakdownItem(BaseModel):
    net_value: float = FieldInfo(alias="NetValue")
    """The net value that the tax is calculated from."""

    tax_value: float = FieldInfo(alias="TaxValue")
    """The value of the tax."""

    tax_rate_code: Optional[str] = FieldInfo(alias="TaxRateCode", default=None)
    """Tax rate code for the item. `null` for untaxed amounts."""


class PaymentDataCreditCardTransactionAdjustedFeeBreakdown(BaseModel):
    items: List[PaymentDataCreditCardTransactionAdjustedFeeBreakdownItem] = FieldInfo(alias="Items")
    """Tax breakdown items per each tax rate applied."""


class PaymentDataCreditCardTransactionAdjustedFeeTaxValue(BaseModel):
    value: float = FieldInfo(alias="Value")
    """Amount of tax applied."""

    code: Optional[str] = FieldInfo(alias="Code", default=None)
    """Code corresponding to tax type."""


class PaymentDataCreditCardTransactionAdjustedFee(BaseModel):
    breakdown: PaymentDataCreditCardTransactionAdjustedFeeBreakdown = FieldInfo(alias="Breakdown")
    """Information about individual tax amounts."""

    currency: str = FieldInfo(alias="Currency")
    """
    ISO-4217 code of the
    [Currency](https://mews-systems.gitbook.io/connector-api/operations/currencies/#currency).
    """

    gross_value: float = FieldInfo(alias="GrossValue")
    """Gross value including all taxes."""

    net_value: float = FieldInfo(alias="NetValue")
    """Net value without taxes."""

    tax_values: List[PaymentDataCreditCardTransactionAdjustedFeeTaxValue] = FieldInfo(alias="TaxValues")
    """The tax values applied."""

    net: Optional[float] = FieldInfo(alias="Net", default=None)

    tax: Optional[float] = FieldInfo(alias="Tax", default=None)

    tax_rate: Optional[float] = FieldInfo(alias="TaxRate", default=None)

    value: Optional[float] = FieldInfo(alias="Value", default=None)


class PaymentDataCreditCardTransactionFeeBreakdownItem(BaseModel):
    net_value: float = FieldInfo(alias="NetValue")
    """The net value that the tax is calculated from."""

    tax_value: float = FieldInfo(alias="TaxValue")
    """The value of the tax."""

    tax_rate_code: Optional[str] = FieldInfo(alias="TaxRateCode", default=None)
    """Tax rate code for the item. `null` for untaxed amounts."""


class PaymentDataCreditCardTransactionFeeBreakdown(BaseModel):
    items: List[PaymentDataCreditCardTransactionFeeBreakdownItem] = FieldInfo(alias="Items")
    """Tax breakdown items per each tax rate applied."""


class PaymentDataCreditCardTransactionFeeTaxValue(BaseModel):
    value: float = FieldInfo(alias="Value")
    """Amount of tax applied."""

    code: Optional[str] = FieldInfo(alias="Code", default=None)
    """Code corresponding to tax type."""


class PaymentDataCreditCardTransactionFee(BaseModel):
    breakdown: PaymentDataCreditCardTransactionFeeBreakdown = FieldInfo(alias="Breakdown")
    """Information about individual tax amounts."""

    currency: str = FieldInfo(alias="Currency")
    """
    ISO-4217 code of the
    [Currency](https://mews-systems.gitbook.io/connector-api/operations/currencies/#currency).
    """

    gross_value: float = FieldInfo(alias="GrossValue")
    """Gross value including all taxes."""

    net_value: float = FieldInfo(alias="NetValue")
    """Net value without taxes."""

    tax_values: List[PaymentDataCreditCardTransactionFeeTaxValue] = FieldInfo(alias="TaxValues")
    """The tax values applied."""

    net: Optional[float] = FieldInfo(alias="Net", default=None)

    tax: Optional[float] = FieldInfo(alias="Tax", default=None)

    tax_rate: Optional[float] = FieldInfo(alias="TaxRate", default=None)

    value: Optional[float] = FieldInfo(alias="Value", default=None)


class PaymentDataCreditCardTransactionSettledAmountBreakdownItem(BaseModel):
    net_value: float = FieldInfo(alias="NetValue")
    """The net value that the tax is calculated from."""

    tax_value: float = FieldInfo(alias="TaxValue")
    """The value of the tax."""

    tax_rate_code: Optional[str] = FieldInfo(alias="TaxRateCode", default=None)
    """Tax rate code for the item. `null` for untaxed amounts."""


class PaymentDataCreditCardTransactionSettledAmountBreakdown(BaseModel):
    items: List[PaymentDataCreditCardTransactionSettledAmountBreakdownItem] = FieldInfo(alias="Items")
    """Tax breakdown items per each tax rate applied."""


class PaymentDataCreditCardTransactionSettledAmountTaxValue(BaseModel):
    value: float = FieldInfo(alias="Value")
    """Amount of tax applied."""

    code: Optional[str] = FieldInfo(alias="Code", default=None)
    """Code corresponding to tax type."""


class PaymentDataCreditCardTransactionSettledAmount(BaseModel):
    breakdown: PaymentDataCreditCardTransactionSettledAmountBreakdown = FieldInfo(alias="Breakdown")
    """Information about individual tax amounts."""

    currency: str = FieldInfo(alias="Currency")
    """
    ISO-4217 code of the
    [Currency](https://mews-systems.gitbook.io/connector-api/operations/currencies/#currency).
    """

    gross_value: float = FieldInfo(alias="GrossValue")
    """Gross value including all taxes."""

    net_value: float = FieldInfo(alias="NetValue")
    """Net value without taxes."""

    tax_values: List[PaymentDataCreditCardTransactionSettledAmountTaxValue] = FieldInfo(alias="TaxValues")
    """The tax values applied."""

    net: Optional[float] = FieldInfo(alias="Net", default=None)

    tax: Optional[float] = FieldInfo(alias="Tax", default=None)

    tax_rate: Optional[float] = FieldInfo(alias="TaxRate", default=None)

    value: Optional[float] = FieldInfo(alias="Value", default=None)


class PaymentDataCreditCardTransaction(BaseModel):
    charged_amount: PaymentDataCreditCardTransactionChargedAmount = FieldInfo(alias="ChargedAmount")

    payment_id: str = FieldInfo(alias="PaymentId")
    """Unique identifier of the `PaymentItem`."""

    adjusted_fee: Optional[PaymentDataCreditCardTransactionAdjustedFee] = FieldInfo(alias="AdjustedFee", default=None)

    fee: Optional[PaymentDataCreditCardTransactionFee] = FieldInfo(alias="Fee", default=None)

    settled_amount: Optional[PaymentDataCreditCardTransactionSettledAmount] = FieldInfo(
        alias="SettledAmount", default=None
    )

    settled_utc: Optional[datetime] = FieldInfo(alias="SettledUtc", default=None)
    """Settlement date and time in UTC timezone in ISO 8601 format."""

    settlement_id: Optional[str] = FieldInfo(alias="SettlementId", default=None)
    """Identifier of the settlement."""


class PaymentDataCreditCard(BaseModel):
    credit_card_id: Optional[str] = FieldInfo(alias="CreditCardId", default=None)
    """Unique identifier of the payment card."""

    transaction: Optional[PaymentDataCreditCardTransaction] = FieldInfo(alias="Transaction", default=None)
    """The credit card payment transaction."""


class PaymentDataExternal(BaseModel):
    type: Literal[
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
    ] = FieldInfo(alias="Type")
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

    external_identifier: Optional[str] = FieldInfo(alias="ExternalIdentifier", default=None)
    """Identifier of the payment from external system."""


class PaymentDataGhost(BaseModel):
    original_payment_id: str = FieldInfo(alias="OriginalPaymentId")
    """Unique identifier of the original payment."""


class PaymentDataInvoice(BaseModel):
    type: Literal[
        "Receivable", "Balancing", "UnderpaymentBalancingReceivable", "OverpaymentBalancingReceivable", "Overpayment"
    ] = FieldInfo(alias="Type")
    """Receivable

    Balancing

    UnderpaymentBalancingReceivable

    OverpaymentBalancingReceivable

    Overpayment
    """

    invoice_id: Optional[str] = FieldInfo(alias="InvoiceId", default=None)
    """Unique identifier of the invoice `Bill`."""


class PaymentData(BaseModel):
    discriminator: Literal["CreditCard", "Invoice", "External", "Ghost"] = FieldInfo(alias="Discriminator")
    """CreditCard

    Invoice

    External

    Ghost
    """

    credit_card: Optional[PaymentDataCreditCard] = FieldInfo(alias="CreditCard", default=None)
    """Contains additional data in the case of a card payment."""

    external: Optional[PaymentDataExternal] = FieldInfo(alias="External", default=None)
    """Contains additional data in the case of an external payment."""

    ghost: Optional[PaymentDataGhost] = FieldInfo(alias="Ghost", default=None)
    """Contains additional data in the case of a ghost payment."""

    invoice: Optional[PaymentDataInvoice] = FieldInfo(alias="Invoice", default=None)
    """Contains additional data in the case of an invoice payment."""


class Payment(BaseModel):
    account_id: str = FieldInfo(alias="AccountId")
    """
    Unique identifier of the account (for example `Customer`) the payment belongs
    to.
    """

    accounting_state: Literal["Open", "Closed", "Inactive", "Canceled"] = FieldInfo(alias="AccountingState")
    """
    Open (Order items which carry a non-zero value, are open, and have not been
    closed on a bill or invoice.)

    Closed (Order items which carry a non-zero value and have been closed on a bill
    or invoice.)

    Inactive (Order items which are either of zero value and have not been canceled,
    if the state of the payment item is Pending or Failed, or items of optional
    reservations. Until the reservation is confirmed, all its accounting items are
    Inactive.)

    Canceled (Order items which have been canceled, regardless of whether the item
    is of zero value.)

    - `Open` - Order items which carry a non-zero value, are open, and have not been
      closed on a bill or invoice.
    - `Closed` - Order items which carry a non-zero value and have been closed on a
      bill or invoice.
    - `Inactive` - Order items which are either of zero value and have not been
      canceled, if the state of the payment item is Pending or Failed, or items of
      optional reservations. Until the reservation is confirmed, all its accounting
      items are Inactive.
    - `Canceled` - Order items which have been canceled, regardless of whether the
      item is of zero value.
    """

    amount: PaymentAmount = FieldInfo(alias="Amount")

    created_utc: datetime = FieldInfo(alias="CreatedUtc")
    """
    Creation date and time of the payment created in UTC timezone in ISO 8601
    format.
    """

    enterprise_id: str = FieldInfo(alias="EnterpriseId")
    """Unique identifier of the `Enterprise`."""

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the payment."""

    original_amount: PaymentOriginalAmount = FieldInfo(alias="OriginalAmount")

    settlement_utc: datetime = FieldInfo(alias="SettlementUtc")
    """Date and time of the payment settlement in UTC timezone in ISO 8601 format."""

    state: Literal["Charged", "Canceled", "Pending", "Failed", "Verifying"] = FieldInfo(alias="State")
    """Charged

    Canceled

    Pending

    Failed

    Verifying
    """

    type: Literal[
        "Payment",
        "CreditCardPayment",
        "AlternativePayment",
        "CashPayment",
        "InvoicePayment",
        "ExternalPayment",
        "GhostPayment",
        "TaxDeductedPayment",
    ] = FieldInfo(alias="Type")
    """Payment

    CreditCardPayment

    AlternativePayment

    CashPayment

    InvoicePayment

    ExternalPayment

    GhostPayment

    TaxDeductedPayment
    """

    updated_utc: datetime = FieldInfo(alias="UpdatedUtc")
    """Last update date and time of the payment in UTC timezone in ISO 8601 format."""

    accounting_category_id: Optional[str] = FieldInfo(alias="AccountingCategoryId", default=None)
    """Unique identifier of the `AccountingCategory` the payment belongs to."""

    account_type: Optional[Literal["Company", "Customer"]] = FieldInfo(alias="AccountType", default=None)
    """A discriminator specifying the account type, e.g. `Customer` or `Company`."""

    bill_id: Optional[str] = FieldInfo(alias="BillId", default=None)
    """Unique identifier of the `Bill` the payment is assigned to."""

    charged_utc: Optional[datetime] = FieldInfo(alias="ChargedUtc", default=None)
    """Charged date and time of the payment in UTC timezone in ISO 8601 format."""

    closed_utc: Optional[datetime] = FieldInfo(alias="ClosedUtc", default=None)
    """Date and time of the payment bill closure in UTC timezone in ISO 8601 format."""

    consumed_utc: Optional[datetime] = FieldInfo(alias="ConsumedUtc", default=None)
    """Date and time of the item consumption in UTC timezone in ISO 8601 format."""

    data: Optional[PaymentData] = FieldInfo(alias="Data", default=None)
    """Additional payment data."""

    identifier: Optional[str] = FieldInfo(alias="Identifier", default=None)
    """Additional unique identifier of the payment."""

    kind: Optional[Literal["Payment", "Chargeback", "ChargebackReversal", "Refund"]] = FieldInfo(
        alias="Kind", default=None
    )
    """Payment

    Chargeback

    ChargebackReversal

    Refund
    """

    notes: Optional[str] = FieldInfo(alias="Notes", default=None)
    """Additional notes."""

    reservation_id: Optional[str] = FieldInfo(alias="ReservationId", default=None)
    """Unique identifier of the `Reservation` the payment belongs to."""

    settlement_id: Optional[str] = FieldInfo(alias="SettlementId", default=None)
    """
    Identifier of the settled payment from the external system (ApplePay/GooglePay).
    """


class PaymentListResponse(BaseModel):
    payments: List[Payment] = FieldInfo(alias="Payments")
    """The list of filtered payments."""

    cursor: Optional[str] = FieldInfo(alias="Cursor", default=None)
    """Unique identifier of the last and hence oldest payment returned.

    This can be used in
    [Limitation](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/#limitation)
    in a subsequent request to fetch the next batch of payments.
    """
