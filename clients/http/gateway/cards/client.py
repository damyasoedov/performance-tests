from typing import TypedDict

from httpx import Response

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client


class CardDict(TypedDict):
    """
    Data structure representing a card.

    Contains the details of the card.
    """
    id: str
    pin: str
    cvv: str
    type: str
    status: str
    accountId: str
    cardNumber: str
    cardHolder: str
    expiryDate: str
    paymentSystem: str


class IssueVirtualCardRequestDict(TypedDict):
    """
    Request payload for issuing a virtual card.

    Contains the user ID and account ID for which to issue the card.
    """
    userId: str
    accountId: str


class IssueVirtualCardResponseDict(TypedDict):
    """
    Response data structure for issuing virtual card.

    Contains the details of the issued virtual card.
    """
    card: CardDict


class IssuePhysicalCardRequestDict(TypedDict):
    """
    Request payload for issuing a physical card.

    Contains the user ID and account ID for which to issue the card.
    """
    userId: str
    accountId: str


class IssuePhysicalCardResponseDict(TypedDict):
    """
    Response data structure for issuing physical card.

    Contains the details of the issued physical card.
    """
    card: CardDict


class CardsGatewayHTTPClient(HTTPClient):
    """
    Client for interacting with the /api/v1/cards endpoint of the http-gateway service.

    Provides methods for issuing virtual and physical cards.
    """

    def issue_virtual_card_api(self, payload: IssueVirtualCardRequestDict) -> Response:
        """
        Issues a virtual card using the raw API endpoint.

        :param payload: A TypedDict object with card creation parameters.
        :return: The server response(httpx.Response with card details).
        """
        return self.post(url='/api/v1/cards/issue-virtual-card', payload=payload)

    def issue_physical_card_api(self, payload: IssuePhysicalCardRequestDict) -> Response:
        """
        Issues a physical card using the raw API endpoint.

        :param payload: A TypedDict object with card creation parameters.
        :return: The server response(httpx.Response with card details).
        """
        return self.post(url='/api/v1/cards/issue-physical-card', payload=payload)

    def issue_virtual_card(self, user_id: str, account_id: str) -> IssueVirtualCardResponseDict:
        """
        Issues a virtual card for user's account and returns the card details.

        :param user_id: The user ID
        :param account_id: The ID of the account to issue the virtual card.
        :return: A TypedDict object with the issued virtual card details.
        """
        request_payload = IssueVirtualCardRequestDict(userId=user_id, accountId=account_id)
        response = self.post(url='/api/v1/cards/issue-virtual-card', payload=request_payload)
        return response.json()

    def issue_physical_card(self, user_id: str, account_id: str) -> IssuePhysicalCardResponseDict:
        """
        Issues a physical card for user's account and returns the card details.

        :param user_id: The user ID
        :param account_id: The ID of the account to issue the physical card.
        :return: A TypedDict object containing the issued physical card details.
        """
        request_payload = IssuePhysicalCardRequestDict(userId=user_id, accountId=account_id)
        response = self.post(url='/api/v1/cards/issue-physical-card', payload=request_payload)
        return response.json()


def build_cards_gateway_http_client() -> CardsGatewayHTTPClient:
    """
    Builds and returns an instance of CardsGatewayHTTPClient.

    Uses the build_gateway_http_client function to create an underlying http client.
    :return: An instance of CardsGatewayHTTPClient.
    """
    return CardsGatewayHTTPClient(client=build_gateway_http_client())
