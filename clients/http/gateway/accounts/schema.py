from pydantic import BaseModel, Field, ConfigDict
from enum import StrEnum, Enum

from clients.http.gateway.cards.schema import CardSchema


class AccountType(StrEnum):
    UNSPECIFIED = "UNSPECIFIED"
    DEBIT_CARD = "DEBIT_CARD"
    CREDIT_CARD = "CREDIT_CARD"
    DEPOSIT = "DEPOSIT"
    SAVINGS = "SAVINGS"

class AccountStatus(StrEnum):
    UNSPECIFIED = "UNSPECIFIED"
    ACTIVE = "ACTIVE"
    PENDING_CLOSURE = "PENDING_CLOSURE"
    CLOSED = "CLOSED"


class AccountSchema(BaseModel):
    """
    Data structure representing an account.

    Containing the account details.
    """
    id: str
    type: AccountType
    cards: list[CardSchema]
    status: AccountStatus
    balance: float


class GetAccountsQuerySchema(BaseModel):
    """
    Data structure for query parameters to retrieve accounts.

    :param str user_id: User identifier (UUID string)
    """
    model_config = ConfigDict(populate_by_name=True)
    user_id: str = Field(alias='userId')


class GetAccountsResponseSchema(BaseModel):
    """
    Response data structure for retrieving user accounts.

    Contains the list of user accounts.
    """
    accounts: list[AccountSchema]


class OpenDepositAccountRequestSchema(BaseModel):
    """
    Data structure for opening deposit account.
    """
    model_config = ConfigDict(populate_by_name=True)
    user_id: str = Field(alias='userId')


class OpenDepositAccountResponseSchema(BaseModel):
    """
    Response data structure for opening deposit account.
    """
    account: AccountSchema


class OpenSavingsAccountRequestSchema(BaseModel):
    """
    Data structure for opening savings account.
    """
    model_config = ConfigDict(populate_by_name=True)
    user_id: str = Field(alias='userId')


class OpenSavingsAccountResponseSchema(BaseModel):
    """
    Response data structure for opening savings account.
    """
    account: AccountSchema


class OpenDebitCardAccountRequestSchema(BaseModel):
    """
    Data structure for opening debit card account
    """
    model_config = ConfigDict(populate_by_name=True)
    user_id: str = Field(alias='userId')


class OpenDebitCardAccountResponseSchema(BaseModel):
    """
    Response data structure for opening debit card account.
    """
    account: AccountSchema


class OpenCreditCardAccountRequestSchema(BaseModel):
    """
    Data structure for opening credit card account
    """
    model_config = ConfigDict(populate_by_name=True)
    user_id: str = Field(alias='userId')


class OpenCreditCardAccountResponseSchema(BaseModel):
    """
    Response data structure for opening credit card account.
    """
    account: AccountSchema
