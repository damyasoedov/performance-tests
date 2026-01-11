from pydantic import BaseModel, Field, ConfigDict
from enum import StrEnum
from datetime import date


class CardType(StrEnum):
    UNSPECIFIED = "UNSPECIFIED"
    VIRTUAL = "VIRTUAL"
    PHYSICAL = "PHYSICAL"


class CardStatus(StrEnum):
    UNSPECIFIED = "UNSPECIFIED"
    ACTIVE = "ACTIVE"
    FROZEN = "FROZEN"
    CLOSED = "CLOSED"
    BLOCKED = "BLOCKED"


class CardPaymentSystem(StrEnum):
    UNSPECIFIED = "UNSPECIFIED"
    MASTERCARD = "MASTERCARD"
    VISA = "VISA"


class CardSchema(BaseModel):
    """
    Data structure representing a card.

    Contains the details of the card.
    """
    id: str
    pin: str
    cvv: str
    type: CardType
    status: CardStatus
    account_id: str = Field(alias = 'accountId')
    card_number: str = Field(alias = 'cardNumber')
    card_holder: str = Field(alias = 'cardHolder')
    expiry_date: date = Field(alias = 'expiryDate')
    payment_system: CardPaymentSystem = Field(alias = 'paymentSystem')


class IssueVirtualCardRequestSchema(BaseModel):
    """
    Request payload for issuing a virtual card.

    Contains the user ID and account ID for which to issue the card.
    """
    model_config = ConfigDict(populate_by_name=True)

    user_id: str = Field(alias = 'userId')
    account_id: str = Field(alias = 'accountId')


class IssueVirtualCardResponseSchema(BaseModel):
    """
    Response data structure for issuing virtual card.

    Contains the details of the issued virtual card.
    """
    card: CardSchema


class IssuePhysicalCardRequestSchema(BaseModel):
    """
    Request payload for issuing a physical card.

    Contains the user ID and account ID for which to issue the card.
    """
    model_config = ConfigDict(populate_by_name=True)

    user_id: str = Field(alias='userId')
    account_id: str = Field(alias='accountId')


class IssuePhysicalCardResponseSchema(BaseModel):
    """
    Response data structure for issuing physical card.

    Contains the details of the issued physical card.
    """
    card: CardSchema
