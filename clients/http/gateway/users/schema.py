from pydantic import BaseModel, Field, EmailStr, ConfigDict


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

    email: EmailStr
    last_name: str = Field(alias='lastName')
    first_name: str = Field(alias='firstName')
    middle_name: str = Field(alias='middleName')
    phone_number: str = Field(alias='phoneNumber')


class CreateUserResponseSchema(BaseModel):
    """
    Response data structure for creating a new user.
    """
    user: UserSchema
