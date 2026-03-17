from grpc import Channel

from clients.grpc.client import GRPCClient
from clients.grpc.gateway.client import build_gateway_grpc_client
from contracts.services.gateway.documents.documents_gateway_service_pb2_grpc import \
    DocumentsGatewayServiceStub
from contracts.services.gateway.documents.rpc_get_contract_document_pb2 import \
    GetContractDocumentRequest, GetContractDocumentResponse
from contracts.services.gateway.documents.rpc_get_tariff_document_pb2 import \
    GetTariffDocumentRequest, GetTariffDocumentResponse


class DocumentsGatewayGRPCClient(GRPCClient):
    """A client for interacting with the Documents Gateway gRPC service.

    This class provides methods for retrieving documents by account_id.
    """
    def __init__(self, channel: Channel):
        """Initializes a DocumentsGatewayGRPCClient with the given channel.

        :param channel: A gRPC channel to connect to the Documents Gateway service.
        """
        super().__init__(channel=channel)

        self.stub = DocumentsGatewayServiceStub(channel=channel)

    def get_contract_document_api(self, request: GetContractDocumentRequest) -> \
            GetContractDocumentResponse:
        """Retrieves contract document via gRPC call."""
        return self.stub.GetContractDocument(request)

    def get_tariff_document_api(self, request: GetTariffDocumentRequest) -> \
            GetTariffDocumentResponse:
        """Retrieves tariff document via gRPC call."""
        return self.stub.GetTariffDocument(request)

    def get_contract_document(self, account_id: str) -> GetContractDocumentResponse:
        """Retrieves a contract document for a given account ID."""
        request = GetContractDocumentRequest(account_id=account_id)
        return self.get_contract_document_api(request=request)

    def get_tariff_document(self, account_id: str) -> GetTariffDocumentResponse:
        """Retrieves a tariff document for a given account ID."""
        request = GetTariffDocumentRequest(account_id=account_id)
        return self.get_tariff_document_api(request=request)


def build_documents_gateway_grpc_client() -> DocumentsGatewayGRPCClient:
    """Creates and returns a DocumentsGatewayGRPCClient instance.

    This function acts as a factory for creating a client connected
    to the Documents Gateway service.
    """
    return DocumentsGatewayGRPCClient(channel=build_gateway_grpc_client())
