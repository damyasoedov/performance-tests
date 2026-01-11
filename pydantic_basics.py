"""
{
    "id": "string",
    "type": "UNSPECIFIED",
    "status": "UNSPECIFIED",
    "balance": 0
}
"""
import uuid

"""
{
  "account": {
    "id": "string",
    "type": "UNSPECIFIED",
    "cards": [
      {
        "id": "string",
        "pin": "string",
        "cvv": "string",
        "type": "UNSPECIFIED",
        "status": "UNSPECIFIED",
        "accountId": "string",
        "cardNumber": "string",
        "cardHolder": "string",
        "expiryDate": "2026-01-10",
        "paymentSystem": "UNSPECIFIED"
      }
    ],
    "status": "UNSPECIFIED",
    "balance": 0
  }
}
"""

from pydantic import BaseModel, Field, ConfigDict, HttpUrl, EmailStr, ValidationError, FilePath
from pydantic.alias_generators import to_camel
from datetime import date


class DocumentSchema(BaseModel):
    url: HttpUrl
    document: str


class UserSchema(BaseModel):
    id: str
    email: EmailStr
    first_name: str = Field(alias='firstName')
    last_name: str = Field(alias='lastName')
    middle_name: str = Field(alias='middleName')
    phone_number: str = Field(alias='phoneNumber')


print(UserSchema(id='user_id', email='fhds@frh.yt', firstName='fn', lastName='ln', middleName='mn', phoneNumber='84751-94867'))

try:
    document_model = DocumentSchema(
        url = "lkgwietwgn",
        document="feitewgndv"
    )
    print(document_model)
except ValidationError as e:
    print(e)
    print(e.errors())
    print(e.json())


class CardSchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    id: str
    pin: str
    cvv: str
    type: str
    status: str
    account_id: str = Field(alias='accountId')
    card_number: str = Field(alias='cardNumber')
    card_holder: str = Field(alias='cardHolder')
    expiry_date: date = Field(alias='expiryDate')
    payment_system: str = Field(alias='paymentSystem')


class AccountSchema(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    type: str = "CREDIT_CARD"
    cards: list[CardSchema] = Field(default_factory=list)
    status: str = 'ACTIVE'
    balance: float = 25000

account_default_model_1 = AccountSchema()

account_default_model_2 = AccountSchema()

print(account_default_model_1, account_default_model_2, sep='\n')

account_default_model = AccountSchema(
    id='account_id',
    type='CREDIT_CARD',
    cards=[
        CardSchema(
            id='card_id',
            pin='1234',
            cvv='123',
            type='PHYSICAL',
            status='ACTIVE',
            accountId='card_account_id',
            cardNumber='card_card_number',
            cardHolder='Alise Smith',
            expiryDate=date(2027, 3, 10),
            paymentSystem='VISA'
        )
    ],
    status='ACTIVE',
    balance=100.55
)

print('Account default model:', account_default_model)
print(account_default_model.model_dump_json(indent=4))

account_dict = {
    'id': 'account_id',
    'type': 'CREDIT_CARD',
    'cards': [
        {
            'id': 'card_id',
            'pin': '1234',
            'cvv': '123',
            'type': 'PHYSICAL',
            'status': 'ACTIVE',
            'accountId': 'card_account_id',
            'cardNumber': 'card_card_number',
            'cardHolder': 'Alise Smith',
            'expiryDate': '2027-03-10',
            'paymentSystem': 'VISA'
        }
    ],
    'status': 'ACTIVE',
    'balance': 333.77
}

account_dict_model = AccountSchema(**account_dict)
print('Account dict model:', account_dict_model)

account_json = """
{
    "id": "account_id",
    "type": "CREDIT_CARD",
    "cards": [
        {
            "id": "card_id",
            "pin": "1234",
            "cvv": "123",
            "type": "PHYSICAL",
            "status": "ACTIVE",
            "accountId": "card_account_id",
            "cardNumber": "card_card_number",
            "cardHolder": "Alise Smith",
            "expiryDate": "2027-03-10",
            "paymentSystem": "VISA"
        }
    ],
    "status": "ACTIVE",
    "balance": 555.22
}
"""
account_json_model = AccountSchema.model_validate_json(account_json)
print('Account JSON model:', account_json_model)
