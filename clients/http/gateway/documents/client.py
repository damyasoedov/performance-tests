from httpx import Response

from clients.http.client import HTTPClient


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
