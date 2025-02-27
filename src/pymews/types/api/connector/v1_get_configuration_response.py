# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "V1GetConfigurationResponse",
    "Enterprise",
    "EnterpriseAddress",
    "EnterpriseCurrency",
    "EnterpriseSubscription",
    "EnterpriseAccountingConfiguration",
    "EnterpriseAccountingConfigurationSurchargeConfiguration",
    "EnterpriseAccountingConfigurationSurchargeConfigurationSurchargeFees",
    "PaymentCardStorage",
    "Service",
    "ServiceData",
    "ServiceDataValue",
    "ServiceDataValueBookableServiceData",
    "ServiceDataValueAdditionalServiceData",
    "ServiceDataValueAdditionalServiceDataPromotions",
    "ServiceOptions",
    "ServicePromotions",
]


class EnterpriseAddress(BaseModel):
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


class EnterpriseCurrency(BaseModel):
    currency: str = FieldInfo(alias="Currency")
    """ISO-4217 code of the `Currency`."""

    is_default: bool = FieldInfo(alias="IsDefault")
    """Whether the currency is a default accounting currency."""

    is_enabled: bool = FieldInfo(alias="IsEnabled")
    """Whether the currency is enabled for usage."""


class EnterpriseSubscription(BaseModel):
    tax_identifier: Optional[str] = FieldInfo(alias="TaxIdentifier", default=None)
    """Tax identifier of the `Enterprise`."""


class EnterpriseAccountingConfigurationSurchargeConfigurationSurchargeFees(BaseModel):
    amex: Optional[float] = FieldInfo(alias="Amex", default=None)

    bancomat: Optional[float] = FieldInfo(alias="Bancomat", default=None)

    bancontact: Optional[float] = FieldInfo(alias="Bancontact", default=None)

    bc: Optional[float] = FieldInfo(alias="Bc", default=None)

    carte_bleue: Optional[float] = FieldInfo(alias="CarteBleue", default=None)

    dankort: Optional[float] = FieldInfo(alias="Dankort", default=None)

    diners_club: Optional[float] = FieldInfo(alias="DinersClub", default=None)

    discover: Optional[float] = FieldInfo(alias="Discover", default=None)

    eftpos: Optional[float] = FieldInfo(alias="Eftpos", default=None)

    eps: Optional[float] = FieldInfo(alias="Eps", default=None)

    giro: Optional[float] = FieldInfo(alias="Giro", default=None)

    interac: Optional[float] = FieldInfo(alias="Interac", default=None)

    isracard: Optional[float] = FieldInfo(alias="Isracard", default=None)

    jcb: Optional[float] = FieldInfo(alias="Jcb", default=None)

    maestro: Optional[float] = FieldInfo(alias="Maestro", default=None)

    master_card: Optional[float] = FieldInfo(alias="MasterCard", default=None)

    meps: Optional[float] = FieldInfo(alias="Meps", default=None)

    mir: Optional[float] = FieldInfo(alias="Mir", default=None)

    nets: Optional[float] = FieldInfo(alias="Nets", default=None)

    post_finance: Optional[float] = FieldInfo(alias="PostFinance", default=None)

    ru_pay: Optional[float] = FieldInfo(alias="RuPay", default=None)

    troy: Optional[float] = FieldInfo(alias="Troy", default=None)

    union_pay: Optional[float] = FieldInfo(alias="UnionPay", default=None)

    verve: Optional[float] = FieldInfo(alias="Verve", default=None)

    visa: Optional[float] = FieldInfo(alias="Visa", default=None)

    v_pay: Optional[float] = FieldInfo(alias="VPay", default=None)


class EnterpriseAccountingConfigurationSurchargeConfiguration(BaseModel):
    surcharge_fees: EnterpriseAccountingConfigurationSurchargeConfigurationSurchargeFees = FieldInfo(
        alias="SurchargeFees"
    )
    """
    Dictionary keys are `CreditCardType` and values are surcharging fees as a
    percentage.
    """

    surcharge_service_id: Optional[str] = FieldInfo(alias="SurchargeServiceId", default=None)
    """Unique identifier of the surcharging `Service`."""

    surcharge_tax_code: Optional[str] = FieldInfo(alias="SurchargeTaxCode", default=None)
    """Surcharging fee `TaxCode`."""


class EnterpriseAccountingConfiguration(BaseModel):
    enabled_external_payment_types: List[
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
    ] = FieldInfo(alias="EnabledExternalPaymentTypes")
    """
    External payment types that are enabled for the enterprise and can be used in
    `payments/addExternal`.
    """

    surcharge_configuration: EnterpriseAccountingConfigurationSurchargeConfiguration = FieldInfo(
        alias="SurchargeConfiguration"
    )
    """Configuration for surcharging fees."""

    additional_tax_identifier: Optional[str] = FieldInfo(alias="AdditionalTaxIdentifier", default=None)
    """Organization number."""

    bank_account_number: Optional[str] = FieldInfo(alias="BankAccountNumber", default=None)
    """Bank account number."""

    bank_name: Optional[str] = FieldInfo(alias="BankName", default=None)
    """Name of the bank."""

    bic: Optional[str] = FieldInfo(alias="Bic", default=None)
    """Business Identification Code."""

    company_name: Optional[str] = FieldInfo(alias="CompanyName", default=None)
    """Legal name of the company."""

    iban: Optional[str] = FieldInfo(alias="Iban", default=None)
    """International Bank Account Number."""


class Enterprise(BaseModel):
    accommodation_environment_code: str = FieldInfo(alias="AccommodationEnvironmentCode")
    """Unique code of the accommodation environment where the enterprise resides."""

    accounting_editable_history_interval: str = FieldInfo(alias="AccountingEditableHistoryInterval")
    """Editable history interval for accounting data in ISO 8601 duration format."""

    accounting_environment_code: str = FieldInfo(alias="AccountingEnvironmentCode")
    """Unique code of the accounting environment where the enterprise resides."""

    address: EnterpriseAddress = FieldInfo(alias="Address")

    address_id: str = FieldInfo(alias="AddressId")
    """Unique identifier of the `Address` of the enterprise."""

    chain_id: str = FieldInfo(alias="ChainId")
    """Unique identifier of the chain to which the enterprise belongs."""

    created_utc: datetime = FieldInfo(alias="CreatedUtc")
    """Creation date and time of the enterprise in UTC timezone in ISO 8601 format."""

    currencies: List[EnterpriseCurrency] = FieldInfo(alias="Currencies")
    """Currencies accepted by the enterprise."""

    default_language_code: str = FieldInfo(alias="DefaultLanguageCode")
    """Language-culture codes of the enterprise default `Language`."""

    editable_history_interval: str = FieldInfo(alias="EditableHistoryInterval")

    group_names: List[str] = FieldInfo(alias="GroupNames")
    """A list of the group names of the enterprise."""

    id: str = FieldInfo(alias="Id")
    """Unique identifier of the enterprise."""

    legal_environment_code: str = FieldInfo(alias="LegalEnvironmentCode")
    """Unique identifier of the legal environment where the enterprise resides."""

    name: str = FieldInfo(alias="Name")
    """Name of the enterprise."""

    operational_editable_history_interval: str = FieldInfo(alias="OperationalEditableHistoryInterval")
    """Editable history interval for operational data in ISO 8601 duration format."""

    pricing: Literal["Gross", "Net"] = FieldInfo(alias="Pricing")
    """Gross (The enterprise shows amount with gross prices.)

    Net (The enterprise shows amount with net prices.)

    - `Gross` - The enterprise shows amount with gross prices.
    - `Net` - The enterprise shows amount with net prices.
    """

    subscription: EnterpriseSubscription = FieldInfo(alias="Subscription")

    tax_environment_code: str = FieldInfo(alias="TaxEnvironmentCode")
    """Unique code of the tax environment where the enterprise resides."""

    time_zone_identifier: str = FieldInfo(alias="TimeZoneIdentifier")
    """IANA timezone identifier of the enterprise."""

    updated_utc: datetime = FieldInfo(alias="UpdatedUtc")
    """Creation date and time of the enterprise in UTC timezone in ISO 8601 format."""

    accounting_configuration: Optional[EnterpriseAccountingConfiguration] = FieldInfo(
        alias="AccountingConfiguration", default=None
    )
    """Configuration information containing financial information about the property."""

    cover_image_id: Optional[str] = FieldInfo(alias="CoverImageId", default=None)
    """Unique identifier of the `Image` of the enterprise cover."""

    email: Optional[str] = FieldInfo(alias="Email", default=None)
    """Email address of the enterprise."""

    external_identifier: Optional[str] = FieldInfo(alias="ExternalIdentifier", default=None)
    """Identifier of the enterprise from external system."""

    is_portfolio: Optional[bool] = FieldInfo(alias="IsPortfolio", default=None)
    """
    Whether the enterprise is a Portfolio enterprise (see
    [Multi-property guidelines](https://mews-systems.gitbook.io/connector-api/guidelines/multi-property)).
    """

    logo_image_id: Optional[str] = FieldInfo(alias="LogoImageId", default=None)
    """Unique identifier of the `Image` of the enterprise logo."""

    phone: Optional[str] = FieldInfo(alias="Phone", default=None)
    """Phone number of the enterprise."""

    tax_precision: Optional[int] = FieldInfo(alias="TaxPrecision", default=None)
    """Tax precision used for financial calculations in the enterprise.

    If `null`, `Currency` precision is used.
    """

    website_url: Optional[str] = FieldInfo(alias="WebsiteUrl", default=None)
    """URL of the enterprise website."""


class PaymentCardStorage(BaseModel):
    public_key: str = FieldInfo(alias="PublicKey")
    """Key for accessing PCI proxy storage."""


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


class V1GetConfigurationResponse(BaseModel):
    enterprise: Enterprise = FieldInfo(alias="Enterprise")

    now_utc: datetime = FieldInfo(alias="NowUtc")
    """Current server date and time in UTC timezone in ISO 8601 format."""

    payment_card_storage: Optional[PaymentCardStorage] = FieldInfo(alias="PaymentCardStorage", default=None)

    service: Optional[Service] = FieldInfo(alias="Service", default=None)
