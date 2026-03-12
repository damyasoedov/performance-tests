import grpc

from contracts.services.gateway.accounts.accounts_gateway_service_pb2_grpc import \
    AccountsGatewayServiceStub
from contracts.services.gateway.accounts.rpc_open_savings_account_pb2 import \
    OpenSavingsAccountRequest, OpenSavingsAccountResponse
from contracts.services.gateway.documents.documents_gateway_service_pb2_grpc import \
    DocumentsGatewayServiceStub
from contracts.services.gateway.documents.rpc_get_contract_document_pb2 import \
    GetContractDocumentRequest, GetContractDocumentResponse
from contracts.services.gateway.documents.rpc_get_tariff_document_pb2 import \
    GetTariffDocumentRequest, GetTariffDocumentResponse
from contracts.services.gateway.users.rpc_create_user_pb2 import \
    CreateUserRequest, CreateUserResponse
from contracts.services.gateway.users.users_gateway_service_pb2_grpc import \
    UsersGatewayServiceStub
from tools.fakers import fake

channel = grpc.insecure_channel('localhost:9003')

accounts_gateway_service = AccountsGatewayServiceStub(channel)
documents_gateway_service = DocumentsGatewayServiceStub(channel)
users_gateway_service = UsersGatewayServiceStub(channel)

create_user_request = CreateUserRequest(
    email=fake.email(),
    first_name=fake.first_name(),
    last_name=fake.last_name(),
    middle_name=fake.middle_name(),
    phone_number=fake.phone_number(),
)
create_user_response: CreateUserResponse = \
    users_gateway_service.CreateUser(create_user_request)
print('Create user response: {}'.format(create_user_response))

create_open_savings_account_request = OpenSavingsAccountRequest(
    user_id=create_user_response.user.id
)
create_open_savings_account_response: OpenSavingsAccountResponse = \
    accounts_gateway_service.OpenSavingsAccount(create_open_savings_account_request)

print(
    'Create open savings account response: {}'.format(create_open_savings_account_response)
)

get_contract_document_request = GetContractDocumentRequest(
    account_id=create_open_savings_account_response.account.id
)
print(get_contract_document_request)

get_contract_document_response: GetContractDocumentResponse = \
    documents_gateway_service.GetContractDocument(get_contract_document_request)
print(
    'Get contract document response: {}'.format(get_contract_document_response)
)
get_tariff_document_request = GetTariffDocumentRequest(
    account_id=create_open_savings_account_response.account.id
)
get_tariff_document_response: GetTariffDocumentResponse = \
    documents_gateway_service.GetTariffDocument(get_tariff_document_request)
print(
    'Get tariff document response: {}'.format(get_tariff_document_response)
)
