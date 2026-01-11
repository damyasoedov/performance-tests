from pydantic import BaseModel, Field


class Address(BaseModel):
    city: str = Field()
    zip_code: str


class User(BaseModel):
    id: int
    name: str
    email: str
    address: Address
    is_active: bool = False


user = User(
    id=1,
    name='Alice',
    email='alice@example.com',
    address={"city": "New York", "zip_code": "1000"}
)

print(user)
