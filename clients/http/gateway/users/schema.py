from pydantic import BaseModel, Field, EmailStr, ConfigDict

from tools.fakers import fake


class UserSchema(BaseModel):
    """
    Data structure representing a user.
    """
    id: str
    email: EmailStr
    last_name: str = Field(alias='lastName')
    first_name: str = Field(alias='firstName')
    middle_name: str = Field(alias='middleName')
    phone_number: str = Field(alias='phoneNumber')


class GetUserResponseSchema(BaseModel):
    """
    Response data structure for retrieving user data.
    """
    user: UserSchema


class CreateUserRequestSchema(BaseModel):
    """
    Data structure for creating a new user.
    """
    model_config = ConfigDict(populate_by_name=True)

    email: EmailStr = Field(default_factory=fake.email)
    last_name: str = Field(alias='lastName', default_factory=fake.last_name)
    first_name: str = Field(alias='firstName', default_factory=fake.first_name)
    middle_name: str = Field(alias='middleName', default_factory=fake.middle_name)
    phone_number: str = Field(alias='phoneNumber', default_factory=fake.phone_number)


class CreateUserResponseSchema(BaseModel):
    """
    Response data structure for creating a new user.
    """
    user: UserSchema
