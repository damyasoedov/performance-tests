from typing import TypedDict

from httpx import Response
from shortuuid import uuid

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client


class CreateUserRequestDict(TypedDict):
    """
    Data structure for creating a new user.
    """
    email: str
    lastName: str
    firstName: str
    middleName: str
    phoneNumber: str


class UserDict(TypedDict):
    """
    Data structure representing a user.
    """
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str
    phoneNumber: str


class GetUserResponseDict(TypedDict):
    """
    Response data structure for retrieving user data.
    """
    user: UserDict


class CreateUserResponseDict(TypedDict):
    """
    Response data structure for creating a new user.
    """
    user: UserDict


class UsersGatewayHTTPClient(HTTPClient):
    """
    Client for interacting with the /api/v1/users endpoint of the http-gateway service

    Provides methods for creating new users and retrieving user data by ID.
    """

    def create_user_api(self, payload: CreateUserRequestDict) -> Response:
        """
        Creates new user using raw API endpoint.

        :param payload: A TypedDict object containing the user creation data.
        :return: The server response(httpx.Response object).
        """
        return self.post('/api/v1/users', payload=payload)

    def get_user_api(self, user_id: str) -> Response:
        """
        Retrieves user data using raw API endpoint.

        :param user_id: The ID of the user to retrieve.
        :return: The server response(httpx.Response object).
        """
        return self.get(f'/api/v1/users/{user_id}')

    def get_user(self, user_id: str) -> GetUserResponseDict:
        """
        Retrieves user data by user ID.

        :param user_id: The ID of the user to retrieve.
        :return: A TypedDict object containing the user data.
        """
        response = self.get_user_api(user_id)
        return response.json()

    def create_user(self) -> CreateUserResponseDict:
        """
        Creates a new user with randomly generated data.

        :return: A TypedDict object containing the data of the created new user.
        """
        create_user_payload = CreateUserRequestDict(
            email=f"{uuid()}@example.com",
            lastName="string",
            firstName="string",
            middleName="string",
            phoneNumber="string",
        )
        response = self.create_user_api(create_user_payload)
        return response.json()


def build_users_gateway_http_client() -> UsersGatewayHTTPClient:
    """
    Builds and returns an UsersGatewayHTTPClient instance.

    Uses the build_gateway_http_client function to create an underlying http client.
    :return: An instance of UsersGatewayHTTPClient.
    """
    return UsersGatewayHTTPClient(client=build_gateway_http_client())
