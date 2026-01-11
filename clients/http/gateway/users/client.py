from httpx import Response
from shortuuid import uuid

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client
from clients.http.gateway.users.schema import (
    GetUserResponseSchema,
    CreateUserRequestSchema,
    CreateUserResponseSchema
)


class UsersGatewayHTTPClient(HTTPClient):
    """
    Client for interacting with the /api/v1/users endpoint of the http-gateway service

    Provides methods for creating new users and retrieving user data by ID.
    """

    def create_user_api(self, payload: CreateUserRequestSchema) -> Response:
        """
        Creates new user using raw API endpoint.

        :param payload: A pydantic-model containing the user creation data.
        :return: The server response(httpx.Response object).
        """
        return self.post('/api/v1/users', payload=payload.model_dump(by_alias=True))

    def get_user_api(self, user_id: str) -> Response:
        """
        Retrieves user data using raw API endpoint.

        :param user_id: The ID of the user to retrieve.
        :return: The server response(httpx.Response object).
        """
        return self.get(f'/api/v1/users/{user_id}')

    def get_user(self, user_id: str) -> GetUserResponseSchema:
        """
        Retrieves user data by user ID.

        :param user_id: The ID of the user to retrieve.
        :return: A response schema containing the user data.
        """
        response = self.get_user_api(user_id)
        return GetUserResponseSchema.model_validate_json(response.text)

    def create_user(self) -> CreateUserResponseSchema:
        """
        Creates a new user with randomly generated data.

        :return: A response schema containing the data of the created new user.
        """
        create_user_payload = CreateUserRequestSchema(
            email=f"{uuid()}@example.com",
            last_name="string",
            first_name="string",
            middle_name="string",
            phone_number="string",
        )
        response = self.create_user_api(create_user_payload)
        return CreateUserResponseSchema.model_validate_json(response.text)


def build_users_gateway_http_client() -> UsersGatewayHTTPClient:
    """
    Builds and returns an UsersGatewayHTTPClient instance.

    Uses the build_gateway_http_client function to create an underlying http client.
    :return: An instance of UsersGatewayHTTPClient.
    """
    return UsersGatewayHTTPClient(client=build_gateway_http_client())
