from pydantic import BaseModel, EmailStr, Field, ConfigDict
from pydantic.alias_generators import to_camel
from shortuuid import uuid


class UserSchema(BaseModel):
    """
    User schema for create and retrieve user.
    """
    id: str
    email: EmailStr
    last_name: str = Field(alias='lastName')
    first_name: str = Field(alias='firstName')
    middle_name: str = Field(alias='middleName')
    phone_number: str = Field(alias='phoneNumber')


class CreateUserRequestSchema(BaseModel):
    """
    Request schema for create user.
    """
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    email: EmailStr = Field(default_factory=lambda: f"{uuid.uuid4}@example.com")
    last_name: str = Field(alias='lastName')
    first_name: str = Field(alias='firstName')
    middle_name: str = Field(alias='middleName')
    phone_number: str = Field(alias='phoneNumber')


class CreateUserResponseSchema(BaseModel):
    """
    Response schema for create user.
    """
    user: UserSchema
