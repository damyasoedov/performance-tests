from httpx import Response

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client
from clients.http.gateway.documents.schema import (
    GetContractDocumentResponseSchema,
    GetTariffDocumentResponseSchema,
)


class DocumentsGatewayHTTPClient(HTTPClient):
    """
    Client for interacting with the documents API.
    """

    def get_tariff_document_api(self, account_id: str) -> Response:
        """
        Retrieves the tariff document for the given account id.

        :param account_id: The account ID
        :return: HTTP response containing the tariff document
        """
        return self.get(url=f'/api/v1/documents/tariff-document/{account_id}')

    def get_contract_document_api(self, account_id: str) -> Response:
        """
        Retrieves the contract document for a given account id.

        :param account_id: The account ID
        :return: HTTP response containing the contract document
        """
        return self.get(url=f'/api/v1/documents/contract-document/{account_id}')

    def get_tariff_document(self, account_id: str) -> GetTariffDocumentResponseSchema:
        """
        Retrieves the tariff document for the given account id.

        :param account_id: The account ID to retrieve the tariff document for.
        :return: A response schema containing the tariff document.
        """
        response = self.get_tariff_document_api(account_id=account_id)

        return GetTariffDocumentResponseSchema.model_validate_json(response.text)

    def get_contract_document(self, account_id: str) -> GetContractDocumentResponseSchema:
        """
        Retrieves the contract document for the given account id.

        :param account_id: The account ID to retrieve the contract document for.
        :return: A response schema containing the contract document.
        """
        response = self.get_contract_document_api(account_id=account_id)

        return GetContractDocumentResponseSchema.model_validate_json(response.text)


def build_documents_gateway_http_client() -> DocumentsGatewayHTTPClient:
    """
    Builds and returns an instance of the DocumentsGatewayHTTPClient class.

    Uses the build_gateway_http_client function to create an underlying http client.
    :return: A DocumentsGatewayHTTPClient instance.
    """
    return DocumentsGatewayHTTPClient(client=build_gateway_http_client())
