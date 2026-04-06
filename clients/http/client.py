from typing import Any, TypedDict

from httpx import Client, URL, Response, QueryParams


class HTTPClientExtensions(TypedDict, total=False):
    route: str


class HTTPClient:
    """
    Base HTTP API Client accepting httpx.Client object

    :param client: An instance of httpx.Client to make HTTP requests
    """

    def __init__(self, client: Client):
        self.client = client

    def get(self, url: URL | str, params: QueryParams | None = None,
            extensions: HTTPClientExtensions | None = None ) -> Response:
        """
        Performs a GET request

        :param url: The endpoint URL
        :param params: request query params
        :param extensions: additional params passed through request extensions
        :return: An httpx.Response object with the response data
        """
        try:
            response = self.client.get(url, params=params, extensions=extensions)
            response.raise_for_status()
            return response
        except Exception as ex:
            raise RuntimeError(f'Error occurred while performing GET-request: {ex}')

    def post(self, url: URL | str, payload: Any | None = None,
             extensions: HTTPClientExtensions | None = None) -> Response:
        """
        Performs a POST request

        :param url: The endpoint URL
        :param payload: The data to send in the request body. Only JSON-serializable Python objects
        :param extensions: additional params passed through request extensions
        :return: An httpx.Response object with the response data
        """
        try:
            response = self.client.post(url, json=payload, extensions=extensions)
            response.raise_for_status()
            return response
        except Exception as ex:
            raise RuntimeError(f'Error occurred while performing the POST-request: {ex}')
