# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import date, datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .customer import Customer
from ....._models import BaseModel

__all__ = [
    "ReservationResult",
    "BusinessSegment",
    "Company",
    "CompanyCreditRating",
    "CompanyOptions",
    "CompanyAddress",
    "Item",
    "ItemAmount",
    "ItemAmountBreakdown",
    "ItemAmountBreakdownItem",
    "ItemAmountTaxValue",
    "Note",
    "OrderItem",
    "OrderItemAmount",
    "OrderItemAmountBreakdown",
    "OrderItemAmountBreakdownItem",
    "OrderItemAmountTaxValue",
    "OrderItemData",
    "OrderItemDataValue",
    "OrderItemDataValueRebateOrderItemData",
    "OrderItemDataValueProductOrderItemData",
    "OrderItemOriginalAmount",
    "OrderItemOriginalAmountBreakdown",
    "OrderItemOriginalAmountBreakdownItem",
    "OrderItemOriginalAmountTaxValue",
    "OrderItemUnitAmount",
    "OrderItemUnitAmountBreakdown",
    "OrderItemUnitAmountBreakdownItem",
    "OrderItemUnitAmountTaxValue",
    "Product",
    "ProductClassifications",
    "ProductOptions",
    "ProductPrice",
    "ProductPriceBreakdown",
    "ProductPriceBreakdownItem",
    "ProductPriceTaxValue",
    "ProductPromotions",
    "ProductPricing",
    "ProductPricingValue",
    "ProductPricingValueExtendedAmount",
    "ProductPricingValueExtendedAmountBreakdown",
    "ProductPricingValueExtendedAmountBreakdownItem",
    "ProductPricingValueExtendedAmountTaxValue",
    "ProductPricingValueRelativeProductPrice",
    "QrCodeData",
    "RateGroup",
    "Rate",
    "ReservationGroup",
    "Reservation",
    "ReservationOptions",
    "ReservationPersonCount",
    "ResourceAccessToken",
    "ResourceAccessTokenPermissions",
    "ResourceCategory",
    "ResourceCategoryAssignment",
    "Resource",
    "ResourceData",
    "ResourceDataValue",
    "ResourceDataValueSpaceData",
    "Service",
    "ServiceData",
    "ServiceDataValue",
    "ServiceDataValueBookableServiceData",
    "ServiceDataValueAdditionalServiceData",
    "ServiceDataValueAdditionalServiceDataPromotions",
    "ServiceOptions",
    "ServicePromotions",
]


class BusinessSegment(BaseModel):
    created_utc: datetime = FieldInfo(alias="CreatedUtc")
    """
    Creation date and time of the business segment in UTC timezone in ISO 8601
    format.
    """

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the business segment."""

    is_active: bool = FieldInfo(alias="IsActive")
    """Whether the business segment is still active."""

    name: str = FieldInfo(alias="Name")
    """Name of the business segment."""

    service_id: str = FieldInfo(alias="ServiceId")
    """Unique identifier of the `Service`."""

    updated_utc: datetime = FieldInfo(alias="UpdatedUtc")
    """
    Last update date and time of the business segment in UTC timezone in ISO 8601
    format.
    """


class CompanyCreditRating(BaseModel):
    basic: Optional[Literal["CreditOk", "PaymentRequiredUpfront", "LocalDecisionRequired"]] = FieldInfo(
        alias="Basic", default=None
    )
    """CreditOk (Company can book services.)

    PaymentRequiredUpfront (Company must pay upfront.)

    LocalDecisionRequired (Requires local approval.)

    - `CreditOk` - Company can book services.
    - `PaymentRequiredUpfront` - Company must pay upfront.
    - `LocalDecisionRequired` - Requires local approval.
    """


class CompanyOptions(BaseModel):
    add_fees_to_invoices: Optional[bool] = FieldInfo(alias="AddFeesToInvoices", default=None)
    """Whether the company has an additional fee applied for invoicing or not."""

    add_tax_deducted_payment_to_invoices: Optional[bool] = FieldInfo(
        alias="AddTaxDeductedPaymentToInvoices", default=None
    )
    """Whether tax-deducted payments should be automatically added to invoices."""

    invoiceable: Optional[bool] = FieldInfo(alias="Invoiceable", default=None)
    """Whether the company is invoiceable or not."""


class CompanyAddress(BaseModel):
    city: Optional[str] = FieldInfo(alias="City", default=None)
    """The city."""

    country_code: Optional[str] = FieldInfo(alias="CountryCode", default=None)
    """ISO 3166-1 code of the `Country`."""

    country_subdivision_code: Optional[str] = FieldInfo(alias="CountrySubdivisionCode", default=None)
    """ISO 3166-2 code of the administrative division, e.g. `DE-BW`."""

    id: Optional[str] = FieldInfo(alias="Id", default=None)
    """Unique identifier of the address."""

    latitude: Optional[float] = FieldInfo(alias="Latitude", default=None)
    """The latitude."""

    line1: Optional[str] = FieldInfo(alias="Line1", default=None)
    """First line of the address."""

    line2: Optional[str] = FieldInfo(alias="Line2", default=None)
    """Second line of the address."""

    longitude: Optional[float] = FieldInfo(alias="Longitude", default=None)
    """The longitude."""

    postal_code: Optional[str] = FieldInfo(alias="PostalCode", default=None)
    """Postal code."""


class Company(BaseModel):
    chain_id: str = FieldInfo(alias="ChainId")
    """Unique identifier of the chain."""

    credit_rating: CompanyCreditRating = FieldInfo(alias="CreditRating")
    """Credit rating to define creditworthiness of the company."""

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the company."""

    is_active: bool = FieldInfo(alias="IsActive")
    """Whether the company is still active."""

    name: str = FieldInfo(alias="Name")
    """Name of the company."""

    number: int = FieldInfo(alias="Number")
    """Unique number of the company."""

    options: CompanyOptions = FieldInfo(alias="Options")
    """Options of the company."""

    accounting_code: Optional[str] = FieldInfo(alias="AccountingCode", default=None)
    """Accounting code of the company."""

    additional_tax_identifier: Optional[str] = FieldInfo(alias="AdditionalTaxIdentifier", default=None)
    """Additional tax identifier of the company."""

    address: Optional[CompanyAddress] = FieldInfo(alias="Address", default=None)

    address_id: Optional[str] = FieldInfo(alias="AddressId", default=None)
    """
    Unique identifier of the company
    [Address](https://mews-systems.gitbook.io/connector-api/operations/addresses/#account-address).
    """

    billing_code: Optional[str] = FieldInfo(alias="BillingCode", default=None)
    """Billing code of the company."""

    contact: Optional[str] = FieldInfo(alias="Contact", default=None)
    """Other contact details, such as telephone, email or similar."""

    contact_person: Optional[str] = FieldInfo(alias="ContactPerson", default=None)
    """Contact person of the company."""

    created_utc: Optional[datetime] = FieldInfo(alias="CreatedUtc", default=None)
    """
    Date of
    [Company](https://mews-systems.gitbook.io/connector-api/operations/#company)
    creation date and time.
    """

    department: Optional[str] = FieldInfo(alias="Department", default=None)
    """The internal segmentation of a company, e.g. sales department."""

    duns_number: Optional[str] = FieldInfo(alias="DunsNumber", default=None)
    """The Dun & Bradstreet unique 9-digit DUNS number."""

    electronic_invoice_identifier: Optional[str] = FieldInfo(alias="ElectronicInvoiceIdentifier", default=None)
    """Electronic invoice identifier of the company."""

    external_identifier: Optional[str] = FieldInfo(alias="ExternalIdentifier", default=None)
    """Identifier of company from external system."""

    iata: Optional[str] = FieldInfo(alias="Iata", default=None)
    """Iata of the company."""

    identifier: Optional[str] = FieldInfo(alias="Identifier", default=None)
    """Other identifier of the company, e.g. legal identifier."""

    invoice_due_interval: Optional[str] = FieldInfo(alias="InvoiceDueInterval", default=None)
    """
    The maximum time, when the invoice has to be be paid in ISO 8601 duration
    format.
    """

    invoicing_email: Optional[str] = FieldInfo(alias="InvoicingEmail", default=None)
    """Email for issuing invoices to the company."""

    merge_target_id: Optional[str] = FieldInfo(alias="MergeTargetId", default=None)
    """Unique identifier of the account (Customer) to which this company is linked."""

    mother_company_id: Optional[str] = FieldInfo(alias="MotherCompanyId", default=None)
    """Unique identifier of mother company."""

    notes: Optional[str] = FieldInfo(alias="Notes", default=None)
    """Additional notes."""

    reference_identifier: Optional[str] = FieldInfo(alias="ReferenceIdentifier", default=None)
    """
    External system identifier - custom identifier used by an external system such
    as an external database.
    """

    tax_identification_number: Optional[str] = FieldInfo(alias="TaxIdentificationNumber", default=None)

    tax_identifier: Optional[str] = FieldInfo(alias="TaxIdentifier", default=None)
    """Tax identification number of the company."""

    telephone: Optional[str] = FieldInfo(alias="Telephone", default=None)
    """Contact telephone number."""

    updated_utc: Optional[datetime] = FieldInfo(alias="UpdatedUtc", default=None)
    """
    Date of
    [Company](https://mews-systems.gitbook.io/connector-api/operations/#company)
    last update date and time.
    """

    website_url: Optional[str] = FieldInfo(alias="WebsiteUrl", default=None)
    """The website url of the company."""


class ItemAmountBreakdownItem(BaseModel):
    net_value: float = FieldInfo(alias="NetValue")
    """The net value that the tax is calculated from."""

    tax_value: float = FieldInfo(alias="TaxValue")
    """The value of the tax."""

    tax_rate_code: Optional[str] = FieldInfo(alias="TaxRateCode", default=None)
    """Tax rate code for the item. `null` for untaxed amounts."""


class ItemAmountBreakdown(BaseModel):
    items: List[ItemAmountBreakdownItem] = FieldInfo(alias="Items")
    """Tax breakdown items per each tax rate applied."""


class ItemAmountTaxValue(BaseModel):
    value: float = FieldInfo(alias="Value")
    """Amount of tax applied."""

    code: Optional[str] = FieldInfo(alias="Code", default=None)
    """Code corresponding to tax type."""


class ItemAmount(BaseModel):
    breakdown: ItemAmountBreakdown = FieldInfo(alias="Breakdown")
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

    tax_values: List[ItemAmountTaxValue] = FieldInfo(alias="TaxValues")
    """The tax values applied."""

    net: Optional[float] = FieldInfo(alias="Net", default=None)

    tax: Optional[float] = FieldInfo(alias="Tax", default=None)

    tax_rate: Optional[float] = FieldInfo(alias="TaxRate", default=None)

    value: Optional[float] = FieldInfo(alias="Value", default=None)


class Item(BaseModel):
    account_id: Optional[str] = FieldInfo(alias="AccountId", default=None)

    accounting_category_id: Optional[str] = FieldInfo(alias="AccountingCategoryId", default=None)

    amount: Optional[ItemAmount] = FieldInfo(alias="Amount", default=None)

    bill_id: Optional[str] = FieldInfo(alias="BillId", default=None)

    closed_utc: Optional[str] = FieldInfo(alias="ClosedUtc", default=None)

    consumption_utc: Optional[str] = FieldInfo(alias="ConsumptionUtc", default=None)

    credit_card_id: Optional[str] = FieldInfo(alias="CreditCardId", default=None)

    customer_id: Optional[str] = FieldInfo(alias="CustomerId", default=None)

    id: Optional[str] = FieldInfo(alias="Id", default=None)

    invoice_id: Optional[str] = FieldInfo(alias="InvoiceId", default=None)

    name: Optional[str] = FieldInfo(alias="Name", default=None)

    notes: Optional[str] = FieldInfo(alias="Notes", default=None)

    order_id: Optional[str] = FieldInfo(alias="OrderId", default=None)

    product_id: Optional[str] = FieldInfo(alias="ProductId", default=None)

    service_id: Optional[str] = FieldInfo(alias="ServiceId", default=None)

    state: Optional[str] = FieldInfo(alias="State", default=None)

    sub_state: Optional[str] = FieldInfo(alias="SubState", default=None)

    sub_type: Optional[str] = FieldInfo(alias="SubType", default=None)

    tax_exemption_reason_code: Optional[str] = FieldInfo(alias="TaxExemptionReasonCode", default=None)
    """Code of tax exemption reason.

    **Restricted!** This property is currently intended for Mews' internal usage and
    may be subject to change.
    """

    type: Optional[str] = FieldInfo(alias="Type", default=None)


class Note(BaseModel):
    created_utc: Optional[datetime] = FieldInfo(alias="CreatedUtc", default=None)
    """
    Creation date and time of the service order note in UTC timezone in ISO 8601
    format.
    """

    id: Optional[str] = FieldInfo(alias="Id", default=None)
    """Unique identifier of the service order note."""

    order_id: Optional[str] = FieldInfo(alias="OrderId", default=None)
    """
    Unique identifier of the `Service order` to which the Service Order Note
    belongs.
    """

    text: Optional[str] = FieldInfo(alias="Text", default=None)
    """Content of the service order note."""

    type: Optional[Literal["General", "ChannelManager", "SpecialRequest"]] = FieldInfo(alias="Type", default=None)
    """General

    ChannelManager

    SpecialRequest
    """

    updated_utc: Optional[datetime] = FieldInfo(alias="UpdatedUtc", default=None)
    """
    Last update date and time of the service order note in UTC timezone in ISO 8601
    format.
    """


class OrderItemAmountBreakdownItem(BaseModel):
    net_value: float = FieldInfo(alias="NetValue")
    """The net value that the tax is calculated from."""

    tax_value: float = FieldInfo(alias="TaxValue")
    """The value of the tax."""

    tax_rate_code: Optional[str] = FieldInfo(alias="TaxRateCode", default=None)
    """Tax rate code for the item. `null` for untaxed amounts."""


class OrderItemAmountBreakdown(BaseModel):
    items: List[OrderItemAmountBreakdownItem] = FieldInfo(alias="Items")
    """Tax breakdown items per each tax rate applied."""


class OrderItemAmountTaxValue(BaseModel):
    value: float = FieldInfo(alias="Value")
    """Amount of tax applied."""

    code: Optional[str] = FieldInfo(alias="Code", default=None)
    """Code corresponding to tax type."""


class OrderItemAmount(BaseModel):
    breakdown: OrderItemAmountBreakdown = FieldInfo(alias="Breakdown")
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

    tax_values: List[OrderItemAmountTaxValue] = FieldInfo(alias="TaxValues")
    """The tax values applied."""

    net: Optional[float] = FieldInfo(alias="Net", default=None)

    tax: Optional[float] = FieldInfo(alias="Tax", default=None)

    tax_rate: Optional[float] = FieldInfo(alias="TaxRate", default=None)

    value: Optional[float] = FieldInfo(alias="Value", default=None)


class OrderItemDataValueRebateOrderItemData(BaseModel):
    rebated_item_id: Optional[str] = FieldInfo(alias="RebatedItemId", default=None)


class OrderItemDataValueProductOrderItemData(BaseModel):
    age_category_id: Optional[str] = FieldInfo(alias="AgeCategoryId", default=None)

    product_id: Optional[str] = FieldInfo(alias="ProductId", default=None)


OrderItemDataValue: TypeAlias = Union[OrderItemDataValueRebateOrderItemData, OrderItemDataValueProductOrderItemData]


class OrderItemData(BaseModel):
    discriminator: Optional[
        Literal[
            "CancellationFee",
            "Rebate",
            "Deposit",
            "ExchangeRateDifference",
            "CustomItem",
            "Surcharge",
            "SurchargeDiscount",
            "SpaceOrder",
            "ProductOrder",
            "Other",
            "TaxCorrection",
            "ResourceUpgradeFee",
            "InvoiceFee",
        ]
    ] = None

    value: Optional[OrderItemDataValue] = None


class OrderItemOriginalAmountBreakdownItem(BaseModel):
    net_value: float = FieldInfo(alias="NetValue")
    """The net value that the tax is calculated from."""

    tax_value: float = FieldInfo(alias="TaxValue")
    """The value of the tax."""

    tax_rate_code: Optional[str] = FieldInfo(alias="TaxRateCode", default=None)
    """Tax rate code for the item. `null` for untaxed amounts."""


class OrderItemOriginalAmountBreakdown(BaseModel):
    items: List[OrderItemOriginalAmountBreakdownItem] = FieldInfo(alias="Items")
    """Tax breakdown items per each tax rate applied."""


class OrderItemOriginalAmountTaxValue(BaseModel):
    value: float = FieldInfo(alias="Value")
    """Amount of tax applied."""

    code: Optional[str] = FieldInfo(alias="Code", default=None)
    """Code corresponding to tax type."""


class OrderItemOriginalAmount(BaseModel):
    breakdown: OrderItemOriginalAmountBreakdown = FieldInfo(alias="Breakdown")
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

    tax_values: List[OrderItemOriginalAmountTaxValue] = FieldInfo(alias="TaxValues")
    """The tax values applied."""

    net: Optional[float] = FieldInfo(alias="Net", default=None)

    tax: Optional[float] = FieldInfo(alias="Tax", default=None)

    tax_rate: Optional[float] = FieldInfo(alias="TaxRate", default=None)

    value: Optional[float] = FieldInfo(alias="Value", default=None)


class OrderItemUnitAmountBreakdownItem(BaseModel):
    net_value: float = FieldInfo(alias="NetValue")
    """The net value that the tax is calculated from."""

    tax_value: float = FieldInfo(alias="TaxValue")
    """The value of the tax."""

    tax_rate_code: Optional[str] = FieldInfo(alias="TaxRateCode", default=None)
    """Tax rate code for the item. `null` for untaxed amounts."""


class OrderItemUnitAmountBreakdown(BaseModel):
    items: List[OrderItemUnitAmountBreakdownItem] = FieldInfo(alias="Items")
    """Tax breakdown items per each tax rate applied."""


class OrderItemUnitAmountTaxValue(BaseModel):
    value: float = FieldInfo(alias="Value")
    """Amount of tax applied."""

    code: Optional[str] = FieldInfo(alias="Code", default=None)
    """Code corresponding to tax type."""


class OrderItemUnitAmount(BaseModel):
    breakdown: OrderItemUnitAmountBreakdown = FieldInfo(alias="Breakdown")
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

    tax_values: List[OrderItemUnitAmountTaxValue] = FieldInfo(alias="TaxValues")
    """The tax values applied."""


class OrderItem(BaseModel):
    account_id: Optional[str] = FieldInfo(alias="AccountId", default=None)
    """
    Unique identifier of the account (for example
    [Customer](https://mews-systems.gitbook.io/connector-api/operations/customers/#customer))
    the item belongs to.
    """

    accounting_category_id: Optional[str] = FieldInfo(alias="AccountingCategoryId", default=None)
    """
    Unique identifier of the
    [Accounting category](https://mews-systems.gitbook.io/connector-api/operations/accountingcategories/#accounting-category)
    the item belongs to.
    """

    accounting_state: Optional[str] = FieldInfo(alias="AccountingState", default=None)
    """Accounting state of the item."""

    amount: Optional[OrderItemAmount] = FieldInfo(alias="Amount", default=None)

    bill_id: Optional[str] = FieldInfo(alias="BillId", default=None)
    """
    Unique identifier of the
    [Bill](https://mews-systems.gitbook.io/connector-api/operations/bills/#bill) the
    item is assigned to.
    """

    canceled_utc: Optional[date] = FieldInfo(alias="CanceledUtc", default=None)

    closed_utc: Optional[date] = FieldInfo(alias="ClosedUtc", default=None)
    """Date and time of the item bill closure in UTC timezone in ISO 8601 format."""

    consumed_utc: Optional[date] = FieldInfo(alias="ConsumedUtc", default=None)
    """Date and time of the item consumption in UTC timezone in ISO 8601 format."""

    created_utc: Optional[date] = FieldInfo(alias="CreatedUtc", default=None)

    creator_profile_id: Optional[str] = FieldInfo(alias="CreatorProfileId", default=None)

    data: Optional[OrderItemData] = FieldInfo(alias="Data", default=None)
    """Additional data specific to particular order item."""

    id: Optional[str] = FieldInfo(alias="Id", default=None)
    """Unique identifier of the item."""

    order_id: Optional[str] = FieldInfo(alias="OrderId", default=None)
    """
    Unique identifier of the order (or
    [Reservation](https://mews-systems.gitbook.io/connector-api/operations/reservations/#reservation-ver-2023-06-06)
    which is a special type of order) the item belongs to.
    """

    original_amount: Optional[OrderItemOriginalAmount] = FieldInfo(alias="OriginalAmount", default=None)

    revenue_type: Optional[str] = FieldInfo(alias="RevenueType", default=None)
    """Revenue type of the item."""

    start_utc: Optional[date] = FieldInfo(alias="StartUtc", default=None)

    unit_amount: Optional[OrderItemUnitAmount] = FieldInfo(alias="UnitAmount", default=None)

    unit_count: Optional[int] = FieldInfo(alias="UnitCount", default=None)
    """Unit count of item, i.e. the number of sub-items or units, if applicable."""

    updated_utc: Optional[date] = FieldInfo(alias="UpdatedUtc", default=None)

    updater_profile_id: Optional[str] = FieldInfo(alias="UpdaterProfileId", default=None)


class ProductClassifications(BaseModel):
    beverage: Optional[bool] = FieldInfo(alias="Beverage", default=None)
    """Product is classified as beverage."""

    city_tax: Optional[bool] = FieldInfo(alias="CityTax", default=None)
    """Product is classified as city tax."""

    food: Optional[bool] = FieldInfo(alias="Food", default=None)
    """Product is classified as food."""

    wellness: Optional[bool] = FieldInfo(alias="Wellness", default=None)
    """Product is classified as wellness."""


class ProductOptions(BaseModel):
    bill_as_package: bool = FieldInfo(alias="BillAsPackage")
    """Product should be displayed as part of a package."""


class ProductPriceBreakdownItem(BaseModel):
    net_value: float = FieldInfo(alias="NetValue")
    """The net value that the tax is calculated from."""

    tax_value: float = FieldInfo(alias="TaxValue")
    """The value of the tax."""

    tax_rate_code: Optional[str] = FieldInfo(alias="TaxRateCode", default=None)
    """Tax rate code for the item. `null` for untaxed amounts."""


class ProductPriceBreakdown(BaseModel):
    items: List[ProductPriceBreakdownItem] = FieldInfo(alias="Items")
    """Tax breakdown items per each tax rate applied."""


class ProductPriceTaxValue(BaseModel):
    value: float = FieldInfo(alias="Value")
    """Amount of tax applied."""

    code: Optional[str] = FieldInfo(alias="Code", default=None)
    """Code corresponding to tax type."""


class ProductPrice(BaseModel):
    breakdown: ProductPriceBreakdown = FieldInfo(alias="Breakdown")
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

    tax_values: List[ProductPriceTaxValue] = FieldInfo(alias="TaxValues")
    """The tax values applied."""

    net: Optional[float] = FieldInfo(alias="Net", default=None)

    tax: Optional[float] = FieldInfo(alias="Tax", default=None)

    tax_rate: Optional[float] = FieldInfo(alias="TaxRate", default=None)

    value: Optional[float] = FieldInfo(alias="Value", default=None)


class ProductPromotions(BaseModel):
    after_check_in: bool = FieldInfo(alias="AfterCheckIn")
    """Whether it can be promoted after check-in."""

    after_check_out: bool = FieldInfo(alias="AfterCheckOut")
    """Whether it can be promoted after check-out."""

    before_check_in: bool = FieldInfo(alias="BeforeCheckIn")
    """Whether it can be promoted before check-in."""

    before_check_out: bool = FieldInfo(alias="BeforeCheckOut")
    """Whether it can be promoted before check-out."""

    during_check_out: bool = FieldInfo(alias="DuringCheckOut")
    """Whether it can be promoted during check-out."""

    during_stay: bool = FieldInfo(alias="DuringStay")
    """Whether it can be promoted during stay."""


class ProductPricingValueExtendedAmountBreakdownItem(BaseModel):
    net_value: float = FieldInfo(alias="NetValue")
    """The net value that the tax is calculated from."""

    tax_value: float = FieldInfo(alias="TaxValue")
    """The value of the tax."""

    tax_rate_code: Optional[str] = FieldInfo(alias="TaxRateCode", default=None)
    """Tax rate code for the item. `null` for untaxed amounts."""


class ProductPricingValueExtendedAmountBreakdown(BaseModel):
    items: List[ProductPricingValueExtendedAmountBreakdownItem] = FieldInfo(alias="Items")
    """Tax breakdown items per each tax rate applied."""


class ProductPricingValueExtendedAmountTaxValue(BaseModel):
    value: float = FieldInfo(alias="Value")
    """Amount of tax applied."""

    code: Optional[str] = FieldInfo(alias="Code", default=None)
    """Code corresponding to tax type."""


class ProductPricingValueExtendedAmount(BaseModel):
    breakdown: ProductPricingValueExtendedAmountBreakdown = FieldInfo(alias="Breakdown")
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

    tax_values: List[ProductPricingValueExtendedAmountTaxValue] = FieldInfo(alias="TaxValues")
    """The tax values applied."""

    net: Optional[float] = FieldInfo(alias="Net", default=None)

    tax: Optional[float] = FieldInfo(alias="Tax", default=None)

    tax_rate: Optional[float] = FieldInfo(alias="TaxRate", default=None)

    value: Optional[float] = FieldInfo(alias="Value", default=None)


class ProductPricingValueRelativeProductPrice(BaseModel):
    multiplier: Optional[float] = FieldInfo(alias="Multiplier", default=None)

    product_ids: Optional[List[str]] = FieldInfo(alias="ProductIds", default=None)

    target: Optional[str] = FieldInfo(alias="Target", default=None)

    tax_rate_codes: Optional[List[str]] = FieldInfo(alias="TaxRateCodes", default=None)


ProductPricingValue: TypeAlias = Union[ProductPricingValueExtendedAmount, ProductPricingValueRelativeProductPrice]


class ProductPricing(BaseModel):
    discriminator: Optional[Literal["Absolute", "Relative"]] = None

    value: Optional[ProductPricingValue] = None


class Product(BaseModel):
    charging_mode: Literal["Once", "PerTimeUnit", "PerPersonPerTimeUnit", "PerPerson"] = FieldInfo(alias="ChargingMode")
    """Once

    PerTimeUnit

    PerPersonPerTimeUnit

    PerPerson
    """

    classifications: ProductClassifications = FieldInfo(alias="Classifications")

    consumption_moment: Literal["ServiceOrderEnd", "ServiceOrderStart", "PostingTimeUnit", "NextTimeUnit"] = FieldInfo(
        alias="ConsumptionMoment"
    )
    """ServiceOrderEnd

    ServiceOrderStart

    PostingTimeUnit

    NextTimeUnit
    """

    created_utc: datetime = FieldInfo(alias="CreatedUtc")
    """Creation date and time of the product in UTC timezone in ISO 8601 format."""

    external_names: Dict[str, str] = FieldInfo(alias="ExternalNames")
    """All translations of external name."""

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the product."""

    is_active: bool = FieldInfo(alias="IsActive")
    """Whether the product is still active."""

    names: Dict[str, str] = FieldInfo(alias="Names")
    """All translations of the name."""

    options: ProductOptions = FieldInfo(alias="Options")

    ordering: int = FieldInfo(alias="Ordering")
    """Order value for presentation purposes."""

    posting_mode: Literal["Once", "PerTimeUnit"] = FieldInfo(alias="PostingMode")
    """Once

    PerTimeUnit
    """

    price: ProductPrice = FieldInfo(alias="Price")

    promotions: ProductPromotions = FieldInfo(alias="Promotions")

    service_id: str = FieldInfo(alias="ServiceId")
    """
    Unique identifier of the
    [Service](https://mews-systems.gitbook.io/connector-api/operations/services/#service).
    """

    short_names: Dict[str, str] = FieldInfo(alias="ShortNames")
    """All translations of short name."""

    updated_utc: datetime = FieldInfo(alias="UpdatedUtc")
    """Last update date and time of the product in UTC timezone in ISO 8601 format."""

    accounting_category_id: Optional[str] = FieldInfo(alias="AccountingCategoryId", default=None)
    """
    Unique identifier of
    [Accounting Category](https://mews-systems.gitbook.io/connector-api/operations/accountingcategories/#accounting-category).
    """

    category_id: Optional[str] = FieldInfo(alias="CategoryId", default=None)
    """Unique identifier of the Product category."""

    charging: Optional[Literal["Once", "PerTimeUnit", "PerPersonPerTimeUnit", "PerPerson"]] = FieldInfo(
        alias="Charging", default=None
    )
    """Once

    PerTimeUnit

    PerPersonPerTimeUnit

    PerPerson
    """

    description: Optional[str] = FieldInfo(alias="Description", default=None)
    """Description of the product. **Deprecated!** Please use Descriptions"""

    descriptions: Optional[Dict[str, str]] = FieldInfo(alias="Descriptions", default=None)
    """All translations of descriptions."""

    external_identifier: Optional[str] = FieldInfo(alias="ExternalIdentifier", default=None)
    """Identifier of the product from external system."""

    external_name: Optional[str] = FieldInfo(alias="ExternalName", default=None)
    """Name of the product meant to be displayed to customer.

    **Deprecated!** Please use ExternalNames
    """

    image_ids: Optional[List[str]] = FieldInfo(alias="ImageIds", default=None)
    """Unique identifier of the product image."""

    is_default: Optional[bool] = FieldInfo(alias="IsDefault", default=None)

    name: Optional[str] = FieldInfo(alias="Name", default=None)
    """Name of the product. **Deprecated!** Please use Names"""

    posting: Optional[Literal["Once", "Daily"]] = FieldInfo(alias="Posting", default=None)
    """Once

    Daily
    """

    pricing: Optional[ProductPricing] = FieldInfo(alias="Pricing", default=None)

    short_name: Optional[str] = FieldInfo(alias="ShortName", default=None)
    """Short name of the product. **Deprecated!** Please use ShortNames"""

    tax_exemption_legal_reference: Optional[str] = FieldInfo(alias="TaxExemptionLegalReference", default=None)
    """Legal reference that states why this product is exempt from tax."""

    tax_exemption_reason: Optional[Literal["IT_N1", "IT_N2_2", "IT_N3_5", "IT_N4", "IT_N5"]] = FieldInfo(
        alias="TaxExemptionReason", default=None
    )
    """IT_N1 (N1 - Escluse ex art.15)

    IT_N2_2 (N2.2 - Non soggette – altri casi)

    IT_N3_5 (N3.5 - Non imponibili – a seguito di dichiarazioni d’intento)

    IT_N4 (N4 - Esenti)

    IT_N5 (N5 - Regime del margine / IVA non esposta in fattura)

    - `IT_N1` - N1 - Escluse ex art.15
    - `IT_N2_2` - N2.2 - Non soggette – altri casi
    - `IT_N3_5` - N3.5 - Non imponibili – a seguito di dichiarazioni d’intento
    - `IT_N4` - N4 - Esenti
    - `IT_N5` - N5 - Regime del margine / IVA non esposta in fattura
    """


class QrCodeData(BaseModel):
    data: Optional[str] = FieldInfo(alias="Data", default=None)
    """Reservation data for QR code generation."""

    reservation_id: Optional[str] = FieldInfo(alias="ReservationId", default=None)
    """Unique identifier of the reservation."""


class RateGroup(BaseModel):
    external_identifier: Optional[str] = FieldInfo(alias="ExternalIdentifier", default=None)
    """External identifier of the rate group."""

    id: Optional[str] = FieldInfo(alias="Id", default=None)
    """Unique identifier of the rate group."""

    is_active: Optional[bool] = FieldInfo(alias="IsActive", default=None)
    """Whether the rate group is still active."""

    name: Optional[str] = FieldInfo(alias="Name", default=None)
    """Name of the rate group."""

    service_id: Optional[str] = FieldInfo(alias="ServiceId", default=None)
    """Unique identifier of the Service that the rate group belongs to."""


class Rate(BaseModel):
    group_id: str = FieldInfo(alias="GroupId")
    """Unique identifier of `Rate Group` where the rate belongs."""

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the rate."""

    is_active: bool = FieldInfo(alias="IsActive")
    """Whether the rate is still active."""

    is_base_rate: bool = FieldInfo(alias="IsBaseRate")
    """Whether the rate is a base rate."""

    is_enabled: bool = FieldInfo(alias="IsEnabled")
    """Whether the rate is currently available to customers."""

    is_public: bool = FieldInfo(alias="IsPublic")
    """Whether the rate is publicly available."""

    names: Dict[str, str] = FieldInfo(alias="Names")
    """All translations of the name."""

    service_id: str = FieldInfo(alias="ServiceId")
    """Unique identifier of the `Service`."""

    type: Literal["Public", "Private", "AvailabilityBlock"] = FieldInfo(alias="Type")
    """Public

    Private

    AvailabilityBlock
    """

    updated_utc: datetime = FieldInfo(alias="UpdatedUtc")
    """Interval in which the rates were updated."""

    base_rate_id: Optional[str] = FieldInfo(alias="BaseRateId", default=None)
    """Unique identifier of the base `Rate`."""

    business_segment_id: Optional[str] = FieldInfo(alias="BusinessSegmentId", default=None)
    """Unique identifier of the `Business Segment`."""

    description: Optional[Dict[str, str]] = FieldInfo(alias="Description", default=None)
    """All translations of the description of the rate."""

    external_identifier: Optional[str] = FieldInfo(alias="ExternalIdentifier", default=None)
    """Identifier of the rate from external system."""

    external_names: Optional[Dict[str, str]] = FieldInfo(alias="ExternalNames", default=None)
    """All translations of the external name of the rate."""

    name: Optional[str] = FieldInfo(alias="Name", default=None)
    """Name of the rate (in the default language)."""

    short_name: Optional[str] = FieldInfo(alias="ShortName", default=None)
    """Short name of the rate (in the default language)."""


class ReservationGroup(BaseModel):
    id: Optional[str] = FieldInfo(alias="Id", default=None)
    """Unique identifier of the reservation group."""

    name: Optional[str] = FieldInfo(alias="Name", default=None)
    """Name of the reservation group."""


class ReservationOptions(BaseModel):
    all_companions_checked_in: bool = FieldInfo(alias="AllCompanionsCheckedIn")
    """All companions of the reservation checked in."""

    any_companion_checked_in: bool = FieldInfo(alias="AnyCompanionCheckedIn")
    """Any companion of the reservation checked in."""

    owner_checked_in: bool = FieldInfo(alias="OwnerCheckedIn")
    """Owner of the reservation checked in."""


class ReservationPersonCount(BaseModel):
    age_category_id: str = FieldInfo(alias="AgeCategoryId")
    """
    Unique identifier of the
    [Age category](https://mews-systems.gitbook.io/connector-api/operations/agecategories#age-category).
    """

    count: int = FieldInfo(alias="Count")
    """Number of people of a given age category. Only positive value is accepted."""


class Reservation(BaseModel):
    assigned_resource_locked: bool = FieldInfo(alias="AssignedResourceLocked")
    """Whether the reservation is locked to the assigned Resource and cannot be moved."""

    companion_ids: List[str] = FieldInfo(alias="CompanionIds")
    """Unique identifiers of the `Customer`s that will use the resource."""

    created_utc: str = FieldInfo(alias="CreatedUtc")
    """Creation date and time of the reservation in UTC timezone in ISO 8601 format."""

    customer_id: str = FieldInfo(alias="CustomerId")
    """Unique identifier of the Customer who owns the reservation."""

    end_utc: str = FieldInfo(alias="EndUtc")
    """End of the reservation (departure) in UTC timezone in ISO 8601 format."""

    group_id: str = FieldInfo(alias="GroupId")
    """Unique identifier of the Reservation group."""

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the reservation."""

    number: str = FieldInfo(alias="Number")
    """Confirmation number of the reservation in Mews."""

    options: ReservationOptions = FieldInfo(alias="Options")
    """Options of the reservation."""

    origin: Literal[
        "Distributor",
        "ChannelManager",
        "Import",
        "Connector",
        "Navigator",
        "CommanderInPerson",
        "CommanderChannel",
        "CommanderPhone",
        "CommanderEmail",
        "CommanderWebsite",
        "CommanderMessage",
        "CommanderCallCenter",
    ] = FieldInfo(alias="Origin")
    """
    - `Distributor` - From the Mews Booking Engine or Booking Engine API.
    - `ChannelManager` - From a channel manager.
    - `Import` - From an import process.
    - `Connector` - From the Mews Connector API.
    - `Navigator` - From Mews Guest Services.
    - `CommanderInPerson` - From Mews Operations, in person.
    - `CommanderChannel` - From Mews Operations, via channel.
    - `CommanderPhone` - From Mews Operations, via telephone.
    - `CommanderEmail` - From Mews Operations, via email.
    - `CommanderWebsite` - From Mews Operations, via website.
    - `CommanderMessage` - From Mews Operations, via message person.
    - `CommanderCallCenter` - From Mews Operations, via call center.
    """

    owner_id: str = FieldInfo(alias="OwnerId")
    """Unique identifier of the Customer or Company who owns the reservation."""

    person_counts: List[ReservationPersonCount] = FieldInfo(alias="PersonCounts")
    """Number of people per age category the reservation was booked for."""

    rate_id: str = FieldInfo(alias="RateId")
    """Identifier of the reservation Rate."""

    requested_category_id: str = FieldInfo(alias="RequestedCategoryId")
    """Identifier of the requested Resource category."""

    service_id: str = FieldInfo(alias="ServiceId")
    """Unique identifier of the Service that is reserved."""

    start_utc: str = FieldInfo(alias="StartUtc")
    """Start of the reservation in UTC timezone in ISO 8601 format.

    This is either the scheduled reservation start time, or the actual customer
    check-in time if this is earlier than the scheduled start time.
    """

    state: Literal["Enquired", "Confirmed", "Started", "Processed", "Canceled", "Optional", "Requested"] = FieldInfo(
        alias="State"
    )

    updated_utc: str = FieldInfo(alias="UpdatedUtc")
    """
    Last update date and time of the reservation in UTC timezone in ISO 8601 format.
    """

    adult_count: Optional[int] = FieldInfo(alias="AdultCount", default=None)
    """Count of adults the reservation was booked for."""

    assigned_resource_id: Optional[str] = FieldInfo(alias="AssignedResourceId", default=None)
    """Identifier of the assigned Resource."""

    assigned_space_id: Optional[str] = FieldInfo(alias="AssignedSpaceId", default=None)
    """Identifier of the assigned Space."""

    assigned_space_locked: Optional[bool] = FieldInfo(alias="AssignedSpaceLocked", default=None)
    """Whether the reservation is locked to the assigned Space and cannot be moved."""

    availability_block_id: Optional[str] = FieldInfo(alias="AvailabilityBlockId", default=None)
    """Unique identifier of the Availability block the reservation is assigned to."""

    booker_id: Optional[str] = FieldInfo(alias="BookerId", default=None)
    """Unique identifier of the Customer on whose behalf the reservation was made."""

    business_segment_id: Optional[str] = FieldInfo(alias="BusinessSegmentId", default=None)
    """Identifier of the reservation Business segment."""

    cancellation_reason: Optional[
        Literal[
            "Other",
            "ConfirmationMissed",
            "BookedElsewhere",
            "ForceMajeure",
            "GuestComplaint",
            "NoShow",
            "PriceTooHigh",
            "ServiceNotAvailable",
            "InputError",
            "InvalidPayment",
            "TravelAgency",
            "RequestedByGuest",
            "Update",
            "BookingAbandoned",
            "RequestedByBooker",
        ]
    ] = FieldInfo(alias="CancellationReason", default=None)
    """Cancellation reason of the reservation."""

    cancelled_utc: Optional[str] = FieldInfo(alias="CancelledUtc", default=None)
    """Cancellation date and time in UTC timezone in ISO 8601 format."""

    channel_manager: Optional[str] = FieldInfo(alias="ChannelManager", default=None)
    """Name of the Channel manager (e.g. AvailPro, SiteMinder, TravelClick, etc)."""

    channel_manager_group_number: Optional[str] = FieldInfo(alias="ChannelManagerGroupNumber", default=None)
    """
    Number of the reservation group within a Channel manager that transferred the
    reservation from Channel to Mews.
    """

    channel_manager_id: Optional[str] = FieldInfo(alias="ChannelManagerId", default=None)
    """Channel Manager number."""

    channel_manager_number: Optional[str] = FieldInfo(alias="ChannelManagerNumber", default=None)
    """Unique number of the reservation within the reservation group."""

    channel_number: Optional[str] = FieldInfo(alias="ChannelNumber", default=None)
    """Number of the reservation within the Channel (i.e.

    OTA, GDS, CRS, etc) in case the reservation group originates there (e.g.
    Booking.com confirmation number).
    """

    child_count: Optional[int] = FieldInfo(alias="ChildCount", default=None)
    """Count of children the reservation was booked for."""

    company_id: Optional[str] = FieldInfo(alias="CompanyId", default=None)
    """Identifier of the Company on behalf of which the reservation was made."""

    credit_card_id: Optional[str] = FieldInfo(alias="CreditCardId", default=None)
    """Unique identifier of the Credit card."""

    origin_details: Optional[str] = FieldInfo(alias="OriginDetails", default=None)
    """Details about the reservation origin."""

    purpose: Optional[Literal["Leisure", "Business", "Student"]] = FieldInfo(alias="Purpose", default=None)
    """Purpose of the reservation."""

    released_utc: Optional[str] = FieldInfo(alias="ReleasedUtc", default=None)
    """
    Date when the optional reservation is released in UTC timezone in ISO 8601
    format.
    """

    travel_agency_id: Optional[str] = FieldInfo(alias="TravelAgencyId", default=None)
    """Identifier of the Company that mediated the reservation."""

    voucher_id: Optional[str] = FieldInfo(alias="VoucherId", default=None)
    """Unique identifier of the Voucher that has been used to create reservation."""


class ResourceAccessTokenPermissions(BaseModel):
    bed: Optional[bool] = FieldInfo(alias="Bed", default=None)

    building: Optional[bool] = FieldInfo(alias="Building", default=None)

    floor: Optional[bool] = FieldInfo(alias="Floor", default=None)

    room: Optional[bool] = FieldInfo(alias="Room", default=None)


class ResourceAccessToken(BaseModel):
    created_utc: datetime = FieldInfo(alias="CreatedUtc")
    """
    Creation date and time of the resource access token in UTC timezone in ISO 8601
    format.
    """

    enterprise_id: str = FieldInfo(alias="EnterpriseId")
    """
    Unique identifier of the
    [Enterprise](https://mews-systems.gitbook.io/connector-api/operations/enterprises/#enterprise).
    """

    id: str = FieldInfo(alias="Id")
    """
    Unique identifier of
    [Resource access token](https://mews-systems.gitbook.io/connector-api/operations/#resource-access-token).
    """

    is_active: bool = FieldInfo(alias="IsActive")
    """Whether the resource access token is still active."""

    service_order_id: str = FieldInfo(alias="ServiceOrderId")
    """Unique identifier of a reservation."""

    type: Literal["PinCode", "RfidTag"] = FieldInfo(alias="Type")

    updated_utc: datetime = FieldInfo(alias="UpdatedUtc")
    """
    Last update date and time of the resource access token in UTC timezone in ISO
    8601 format.
    """

    validity_end_utc: datetime = FieldInfo(alias="ValidityEndUtc")
    """Marks the end of interval in which the resource access token can be used."""

    validity_start_utc: datetime = FieldInfo(alias="ValidityStartUtc")
    """Marks the start of interval in which the resource access token can be used."""

    companionship_id: Optional[str] = FieldInfo(alias="CompanionshipId", default=None)
    """
    Unique identifier of
    [Companionship](https://mews-systems.gitbook.io/connector-api/operations/companionships/#companionship).
    """

    permissions: Optional[ResourceAccessTokenPermissions] = FieldInfo(alias="Permissions", default=None)
    """
    Specify permissions of
    [Resource access token](https://mews-systems.gitbook.io/connector-api/operations/#resource-access-token).
    """

    resource_id: Optional[str] = FieldInfo(alias="ResourceId", default=None)
    """
    Unique identifier of
    [Resource](https://mews-systems.gitbook.io/connector-api/operations/resources/#resource).
    """

    serial_number: Optional[str] = FieldInfo(alias="SerialNumber", default=None)
    """
    Serial number of
    [Resource access token type](https://mews-systems.gitbook.io/connector-api/operations/#resource-access-token-type).
    """

    value: Optional[str] = FieldInfo(alias="Value", default=None)
    """Value of resource access token"""


class ResourceCategory(BaseModel):
    capacity: int = FieldInfo(alias="Capacity")

    classification: Literal[
        "StandardSingle",
        "StandardDouble",
        "SuperiorTwin",
        "SuperiorDouble",
        "JuniorSuite",
        "SharedOrDorm",
        "Other",
        "SuperiorSingle",
        "Triple",
        "Family",
        "StandardTwin",
        "Studio",
        "SuperiorTripleRoom",
        "OneBedroomApartment",
        "ThreeBedroomsApartment",
        "TwoBedroomsApartment",
    ] = FieldInfo(alias="Classification")

    descriptions: Dict[str, str] = FieldInfo(alias="Descriptions")
    """All translations of the description."""

    enterprise_id: str = FieldInfo(alias="EnterpriseId")
    """
    Unique identifier of the
    [Enterprise](https://mews-systems.gitbook.io/connector-api/operations/enterprises/#enterprise).
    """

    extra_capacity: int = FieldInfo(alias="ExtraCapacity")
    """Extra capacity that can be served (e.g. extra bed count)."""

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the category."""

    is_active: bool = FieldInfo(alias="IsActive")
    """Whether the category is still active."""

    names: Dict[str, str] = FieldInfo(alias="Names")
    """All translations of the name."""

    ordering: int = FieldInfo(alias="Ordering")

    service_id: str = FieldInfo(alias="ServiceId")
    """
    Unique identifier of the
    [Service](https://mews-systems.gitbook.io/connector-api/operations/services/#service)
    of the resource category.
    """

    short_names: Dict[str, str] = FieldInfo(alias="ShortNames")
    """All translations of the short name."""

    type: Literal[
        "Room",
        "Bed",
        "Dorm",
        "Apartment",
        "Suite",
        "Villa",
        "Site",
        "Office",
        "MeetingRoom",
        "ParkingSpot",
        "Desk",
        "TeamArea",
        "Membership",
        "Tent",
        "CaravanOrRV",
        "UnequippedCampsite",
        "Bike",
        "ExtraBed",
        "Cot",
        "Crib",
        "ConferenceRoom",
        "Rooftop",
        "Garden",
        "Restaurant",
        "Amphitheater",
        "PrivateSpaces",
    ] = FieldInfo(alias="Type")

    accounting_category_id: Optional[str] = FieldInfo(alias="AccountingCategoryId", default=None)

    external_identifier: Optional[str] = FieldInfo(alias="ExternalIdentifier", default=None)
    """Identifier of the resource category from external system."""


class ResourceCategoryAssignment(BaseModel):
    category_id: str = FieldInfo(alias="CategoryId")
    """
    Unique identifier of the
    [Resource category](https://mews-systems.gitbook.io/connector-api/operations/#resource-category).
    """

    created_utc: datetime = FieldInfo(alias="CreatedUtc")
    """Creation date and time of the assignment in UTC timezone in ISO 8601 format."""

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the assignment."""

    is_active: bool = FieldInfo(alias="IsActive")
    """Whether the assignment is still active."""

    resource_id: str = FieldInfo(alias="ResourceId")
    """
    Unique identifier of the
    [Resource](https://mews-systems.gitbook.io/connector-api/operations/#resource)
    assigned to the Resource category.
    """

    updated_utc: datetime = FieldInfo(alias="UpdatedUtc")
    """Last update date and time of the assignment in UTC timezone in ISO 8601 format."""


class ResourceDataValueSpaceData(BaseModel):
    floor_number: str = FieldInfo(alias="FloorNumber")

    location_notes: Optional[str] = FieldInfo(alias="LocationNotes", default=None)


ResourceDataValue: TypeAlias = Union[ResourceDataValueSpaceData, object, object]


class ResourceData(BaseModel):
    discriminator: Optional[str] = None

    value: Optional[ResourceDataValue] = None


class Resource(BaseModel):
    created_utc: str = FieldInfo(alias="CreatedUtc")
    """Creation date and time of the resource in UTC timezone in ISO 8601 format."""

    data: ResourceData = FieldInfo(alias="Data")
    """Additional data of the resource."""

    descriptions: Dict[str, str] = FieldInfo(alias="Descriptions")
    """All translations of the description."""

    directions: Dict[str, str] = FieldInfo(alias="Directions")
    """All translations of direction."""

    enterprise_id: str = FieldInfo(alias="EnterpriseId")
    """
    Unique identifier of the
    [Enterprise](https://mews-systems.gitbook.io/connector-api/operations/enterprises/#enterprise).
    """

    external_names: Dict[str, str] = FieldInfo(alias="ExternalNames")
    """All translations of external name."""

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the resource."""

    is_active: bool = FieldInfo(alias="IsActive")
    """Whether the resource is still active."""

    name: str = FieldInfo(alias="Name")
    """Name of the resource (e.g. room number)."""

    state: str = FieldInfo(alias="State")
    """State of the resource."""

    updated_utc: str = FieldInfo(alias="UpdatedUtc")
    """Last update date and time of the resource in UTC timezone in ISO 8601 format."""

    parent_resource_id: Optional[str] = FieldInfo(alias="ParentResourceId", default=None)
    """
    Identifier of the parent
    [Resource](https://mews-systems.gitbook.io/connector-api/operations/#resource)
    (e.g. room of a bed).
    """


class ServiceDataValueBookableServiceData(BaseModel):
    end_offset: str = FieldInfo(alias="EndOffset")
    """
    Offset from the end of the
    [time unit](https://mews-systems.gitbook.io/connector-api/concepts/time-units/)
    which defines the default end of the service; expressed in ISO 8601 duration
    format.
    """

    occupancy_end_offset: str = FieldInfo(alias="OccupancyEndOffset")
    """
    Offset from the end of the
    [time unit](https://mews-systems.gitbook.io/connector-api/concepts/time-units/)
    which defines the occupancy end of the service; expressed in ISO 8601 duration
    format. 'Occupancy end' is used for availability and reporting purposes, it
    implies the time at which the booked resource is no longer considered occupied.
    """

    occupancy_start_offset: str = FieldInfo(alias="OccupancyStartOffset")
    """
    Offset from the start of the
    [time unit](https://mews-systems.gitbook.io/connector-api/concepts/time-units/)
    which defines the occupancy start of the service; expressed in ISO 8601 duration
    format. 'Occupancy start' is used for availability and reporting purposes, it
    implies the time at which the booked resource is considered occupied.
    """

    start_offset: str = FieldInfo(alias="StartOffset")
    """
    Offset from the start of the
    [time unit](https://mews-systems.gitbook.io/connector-api/concepts/time-units/)
    which defines the default start of the service; expressed in ISO 8601 duration
    format.
    """

    time_unit: Literal["Day", "Month", "Hour"] = FieldInfo(alias="TimeUnit")
    """Day

    Month

    Hour
    """

    time_unit_period: Literal["Day", "Month", "Hour"] = FieldInfo(alias="TimeUnitPeriod")
    """Day

    Month

    Hour
    """


class ServiceDataValueAdditionalServiceDataPromotions(BaseModel):
    after_check_in: bool = FieldInfo(alias="AfterCheckIn")
    """Whether it can be promoted after check-in."""

    after_check_out: bool = FieldInfo(alias="AfterCheckOut")
    """Whether it can be promoted after check-out."""

    before_check_in: bool = FieldInfo(alias="BeforeCheckIn")
    """Whether it can be promoted before check-in."""

    before_check_out: bool = FieldInfo(alias="BeforeCheckOut")
    """Whether it can be promoted before check-out."""

    during_check_out: bool = FieldInfo(alias="DuringCheckOut")
    """Whether it can be promoted during check-out."""

    during_stay: bool = FieldInfo(alias="DuringStay")
    """Whether it can be promoted during stay."""


class ServiceDataValueAdditionalServiceData(BaseModel):
    promotions: ServiceDataValueAdditionalServiceDataPromotions = FieldInfo(alias="Promotions")


ServiceDataValue: TypeAlias = Union[ServiceDataValueBookableServiceData, ServiceDataValueAdditionalServiceData]


class ServiceData(BaseModel):
    discriminator: Optional[Literal["Bookable", "Additional"]] = None

    value: Optional[ServiceDataValue] = None


class ServiceOptions(BaseModel):
    bill_as_package: bool = FieldInfo(alias="BillAsPackage")
    """Products should be displayed as a single package instead of individual items."""


class ServicePromotions(BaseModel):
    after_check_in: bool = FieldInfo(alias="AfterCheckIn")
    """Whether it can be promoted after check-in."""

    after_check_out: bool = FieldInfo(alias="AfterCheckOut")
    """Whether it can be promoted after check-out."""

    before_check_in: bool = FieldInfo(alias="BeforeCheckIn")
    """Whether it can be promoted before check-in."""

    before_check_out: bool = FieldInfo(alias="BeforeCheckOut")
    """Whether it can be promoted before check-out."""

    during_check_out: bool = FieldInfo(alias="DuringCheckOut")
    """Whether it can be promoted during check-out."""

    during_stay: bool = FieldInfo(alias="DuringStay")
    """Whether it can be promoted during stay."""


class Service(BaseModel):
    created_utc: datetime = FieldInfo(alias="CreatedUtc")
    """Creation date and time of the service in UTC timezone in ISO 8601 format."""

    data: ServiceData = FieldInfo(alias="Data")
    """Additional information about the specific service."""

    enterprise_id: str = FieldInfo(alias="EnterpriseId")
    """
    Unique identifier of the
    [Enterprise](https://mews-systems.gitbook.io/connector-api/operations/enterprises/#enterprise).
    """

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the service."""

    is_active: bool = FieldInfo(alias="IsActive")
    """Whether the service is still active."""

    name: str = FieldInfo(alias="Name")
    """Name of the service."""

    names: Dict[str, str] = FieldInfo(alias="Names")
    """All translations of the name."""

    options: ServiceOptions = FieldInfo(alias="Options")
    """Options of the service."""

    ordering: int = FieldInfo(alias="Ordering")
    """Order value for presentation purposes."""

    updated_utc: datetime = FieldInfo(alias="UpdatedUtc")
    """Last update date and time of the service in UTC timezone in ISO 8601 format."""

    end_time: Optional[str] = FieldInfo(alias="EndTime", default=None)

    external_identifier: Optional[str] = FieldInfo(alias="ExternalIdentifier", default=None)
    """Identifier of the service from external system."""

    promotions: Optional[ServicePromotions] = FieldInfo(alias="Promotions", default=None)

    start_time: Optional[str] = FieldInfo(alias="StartTime", default=None)

    type: Optional[str] = FieldInfo(alias="Type", default=None)


class ReservationResult(BaseModel):
    business_segments: Optional[List[BusinessSegment]] = FieldInfo(alias="BusinessSegments", default=None)
    """Business segments of the reservations."""

    companies: Optional[List[Company]] = FieldInfo(alias="Companies", default=None)
    """Companies related to the reservations."""

    cursor: Optional[str] = FieldInfo(alias="Cursor", default=None)
    """Unique identifier of the last and hence oldest reservation returned.

    This can be used in
    [Limitation](https://mews-systems.gitbook.io/connector-api/guidelines/pagination/#limitation)
    in a subsequent request to fetch the next batch of older reservations.
    """

    customers: Optional[List[Customer]] = FieldInfo(alias="Customers", default=None)
    """Customers that are members of the reservations."""

    items: Optional[List[Item]] = FieldInfo(alias="Items", default=None)
    """Accounting items that are part of the reservations."""

    notes: Optional[List[Note]] = FieldInfo(alias="Notes", default=None)
    """Notes of the reservations."""

    order_items: Optional[List[OrderItem]] = FieldInfo(alias="OrderItems", default=None)
    """Revenue items of the reservations."""

    products: Optional[List[Product]] = FieldInfo(alias="Products", default=None)
    """Products orderable with reservations."""

    qr_code_data: Optional[List[QrCodeData]] = FieldInfo(alias="QrCodeData", default=None)
    """QR code data of the reservations."""

    rate_groups: Optional[List[RateGroup]] = FieldInfo(alias="RateGroups", default=None)
    """Rate groups of the reservation rates."""

    rates: Optional[List[Rate]] = FieldInfo(alias="Rates", default=None)
    """Rates of the reservations."""

    reservation_groups: Optional[List[ReservationGroup]] = FieldInfo(alias="ReservationGroups", default=None)
    """Reservation groups that the reservations are members of."""

    reservations: Optional[List[Reservation]] = FieldInfo(alias="Reservations", default=None)
    """The reservations that collide with the specified interval."""

    resource_access_tokens: Optional[List[ResourceAccessToken]] = FieldInfo(alias="ResourceAccessTokens", default=None)
    """Resource access tokens for the reservations."""

    resource_categories: Optional[List[ResourceCategory]] = FieldInfo(alias="ResourceCategories", default=None)
    """Resource categories of the resources."""

    resource_category_assignments: Optional[List[ResourceCategoryAssignment]] = FieldInfo(
        alias="ResourceCategoryAssignments", default=None
    )
    """Assignments of the resources to categories."""

    resources: Optional[List[Resource]] = FieldInfo(alias="Resources", default=None)
    """Assigned resources of the reservations."""

    services: Optional[List[Service]] = FieldInfo(alias="Services", default=None)
    """Services that have been reserved."""
