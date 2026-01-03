from typing import TypedDict

from httpx import Response

from clients.http.client import HTTPClient


class CreateUserRequestDict(TypedDict):
    """
    Data template for creating new user
    """
    email: str
    lastName: str
    firstName: str
    middleName: str
    phoneNumber: str


class UsersGatewayHTTPClient(HTTPClient):
    """ Client for interacting with the /api/v1/users endpoint
    of the http-gateway service
    """

    def create_user_api(self, payload: CreateUserRequestDict) -> Response:
        """Creates new user

        :param payload: A TypedDict object with new user create info
        :return: The server response(httpx.Response object with the user data)
        """
        return self.post('/api/v1/users', payload=payload)

    def get_user_api(self, user_id: str) -> Response:
        """Get user data by user ID.

        :param user_id: User ID
        :return: The server response(httpx.Response object with the user data)
        """
        return self.get(f'/api/v1/users/{user_id}')
