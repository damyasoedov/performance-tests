from grpc import Channel

from clients.grpc.client import GRPCClient
from clients.grpc.gateway.client import build_gateway_grpc_client
from contracts.services.gateway.accounts.accounts_gateway_service_pb2_grpc import \
    AccountsGatewayServiceStub
from contracts.services.gateway.accounts.rpc_get_accounts_pb2 import \
    GetAccountsRequest, GetAccountsResponse
from contracts.services.gateway.accounts.rpc_open_credit_card_account_pb2 import \
    OpenCreditCardAccountRequest, OpenCreditCardAccountResponse
from contracts.services.gateway.accounts.rpc_open_debit_card_account_pb2 import \
    OpenDebitCardAccountRequest, OpenDebitCardAccountResponse
from contracts.services.gateway.accounts.rpc_open_deposit_account_pb2 import \
    OpenDepositAccountRequest, OpenDepositAccountResponse
from contracts.services.gateway.accounts.rpc_open_savings_account_pb2 import \
    OpenSavingsAccountRequest, OpenSavingsAccountResponse


class AccountsGatewayGRPCClient(GRPCClient):
    """A client for interacting with the Accounts Gateway gRPC service.

    Provides methods for creating different types of accounts
    and retrieving accounts information.
    """
    def __init__(self, channel: Channel):
        """Initializes a AccountsGatewayGRPCClient with the given channel.

        :param channel: A grpc.Channel to connect to the Operations Gateway service.
        """
        super().__init__(channel=channel)

        self.stub = AccountsGatewayServiceStub(channel=channel)

    def get_accounts_api(self, request: GetAccountsRequest) -> GetAccountsResponse:
        """Retrieves accounts via gRPC call."""
        return self.stub.GetAccounts(request)

    def open_deposit_account_api(self, request: OpenDepositAccountRequest) -> OpenDepositAccountResponse:
        """Creates deposit account via gRPC call."""
        return self.stub.OpenDepositAccount(request)

    def open_savings_account_api(self, request: OpenSavingsAccountRequest) -> OpenSavingsAccountResponse:
        """Creates savings account via gRPC call."""
        return self.stub.OpenSavingsAccount(request)

    def open_debit_card_account_api(self, request: OpenDebitCardAccountRequest) -> OpenDebitCardAccountResponse:
        """Creates debit card account via gRPC call."""
        return self.stub.OpenDebitCardAccount(request)

    def open_credit_card_account_api(self, request: OpenCreditCardAccountRequest) -> OpenCreditCardAccountResponse:
        """Creates credit card account via gRPC call."""
        return self.stub.OpenCreditCardAccount(request)

    def get_accounts(self, user_id: str) -> GetAccountsResponse:
        """Retrieves accounts for the given user by user_id"""
        request = GetAccountsRequest(user_id=user_id)
        return self.get_accounts_api(request=request)

    def open_deposit_account(self, user_id: str) -> OpenDepositAccountResponse:
        """Creates deposit account fot the given user by user_id"""
        request = OpenDepositAccountRequest(user_id=user_id)
        return self.open_deposit_account_api(request=request)

    def open_savings_account(self, user_id: str) -> OpenSavingsAccountResponse:
        """Creates savings account for the given user by user_id"""
        request = OpenSavingsAccountRequest(user_id=user_id)
        return self.open_savings_account_api(request=request)

    def open_debit_card_account(self, user_id: str) -> OpenDebitCardAccountResponse:
        """Creates debit card account for the given user by user_id"""
        request = OpenDebitCardAccountRequest(user_id=user_id)
        return self.open_debit_card_account_api(request=request)

    def open_credit_card_account(self, user_id: str) -> OpenCreditCardAccountResponse:
        """Creates credit card account for the given user by user_id"""
        request = OpenCreditCardAccountRequest(user_id=user_id)
        return self.open_credit_card_account_api(request=request)


def build_accounts_gateway_grpc_client() -> AccountsGatewayGRPCClient:
    """Creates and returns a AccountsGatewayGRPCClient instance.

    This function acts as a factory for creating a client connected
    to the Accounts Gateway service.
    """
    return AccountsGatewayGRPCClient(channel=build_gateway_grpc_client())
