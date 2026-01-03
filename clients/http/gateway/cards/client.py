from typing import TypedDict

from httpx import Response

from clients.http.client import HTTPClient


class IssueVirtualCardRequestDict(TypedDict):
    """
    Request payload for issue virtual card
    """
    userId: str
    accountId: str


class IssuePhysicalCardRequestDict(TypedDict):
    """
    Request payload for issue physical card
    """
    userId: str
    accountId: str


class CardsGatewayHTTPClient(HTTPClient):
    """ Client for interacting with the /api/v1/cards endpoint
        of the http-gateway service
    """

    def issue_virtual_card_api(self, payload: IssueVirtualCardRequestDict) -> Response:
        """
        Issues a virtual card for user's account.

        :param payload: A TypedDict object with card creation parameters
        :return: The server response(httpx.Response with card details)
        """
        return self.post(url='/api/v1/cards/issue-virtual-card', payload=payload)

    def issue_physical_card_api(self, payload: IssuePhysicalCardRequestDict) -> Response:
        """ Issues a physical card for user's account.

        :param payload: A TypedDict object with card creation parameters
        :return: The server response(httpx.Response with card details)
        """
        return self.post(url='/api/v1/cards/issue-physical-card', payload=payload)
