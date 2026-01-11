from httpx import Response

from clients.http.client import HTTPClient
from clients.http.gateway.cards.schema import (
    IssuePhysicalCardRequestSchema,
    IssuePhysicalCardResponseSchema,
    IssueVirtualCardRequestSchema,
    IssueVirtualCardResponseSchema,
)
from clients.http.gateway.client import build_gateway_http_client


class CardsGatewayHTTPClient(HTTPClient):
    """
    Client for interacting with the /api/v1/cards endpoint of the http-gateway service.

    Provides methods for issuing virtual and physical cards.
    """

    def issue_virtual_card_api(self, payload: IssueVirtualCardRequestSchema) -> Response:
        """
        Issues a virtual card using the raw API endpoint.

        :param payload: A response schema with card creation parameters.
        :return: The server response(httpx.Response with card details).
        """
        return self.post(
            url='/api/v1/cards/issue-virtual-card',
            payload=payload.model_dump(by_alias=True)
        )

    def issue_physical_card_api(self, payload: IssuePhysicalCardRequestSchema) -> Response:
        """
        Issues a physical card using the raw API endpoint.

        :param payload: A response schema with card creation parameters.
        :return: The server response(httpx.Response with card details).
        """
        return self.post(
            url='/api/v1/cards/issue-physical-card',
            payload=payload.model_dump(by_alias=True)
        )

    def issue_virtual_card(self, user_id: str, account_id: str) -> IssueVirtualCardResponseSchema:
        """
        Issues a virtual card for user's account and returns the card details.

        :param user_id: The user ID
        :param account_id: The ID of the account to issue the virtual card.
        :return: A Pydantic-model with the issued virtual card details.
        """
        request_payload = IssueVirtualCardRequestSchema(user_id=user_id, account_id=account_id)
        response = self.issue_virtual_card_api(payload=request_payload)

        return IssueVirtualCardResponseSchema.model_validate_json(response.text)

    def issue_physical_card(self, user_id: str, account_id: str) -> IssuePhysicalCardResponseSchema:
        """
        Issues a physical card for user's account and returns the card details.

        :param user_id: The user ID
        :param account_id: The ID of the account to issue the physical card.
        :return: A response schema containing the issued physical card details.
        """
        request_payload = IssuePhysicalCardRequestSchema(user_id=user_id, account_id=account_id)
        response = self.issue_physical_card_api(payload=request_payload)

        return IssuePhysicalCardResponseSchema.model_validate_json(response.text)


def build_cards_gateway_http_client() -> CardsGatewayHTTPClient:
    """
    Builds and returns an instance of CardsGatewayHTTPClient.

    Uses the build_gateway_http_client function to create an underlying http client.
    :return: An instance of CardsGatewayHTTPClient.
    """
    return CardsGatewayHTTPClient(client=build_gateway_http_client())
