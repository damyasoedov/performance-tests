from grpc import Channel

from clients.grpc.client import GRPCClient
from clients.grpc.gateway.client import build_gateway_grpc_client
from contracts.services.gateway.accounts.accounts_gateway_service_pb2_grpc import AccountsGatewayServiceStub
from contracts.services.operations.operation_pb2 import OperationStatus
from contracts.services.gateway.operations.operations_gateway_service_pb2_grpc import \
    OperationsGatewayServiceStub
from contracts.services.gateway.operations.rpc_get_operation_pb2 import \
    GetOperationRequest, GetOperationResponse
from contracts.services.gateway.operations.rpc_get_operations_pb2 import \
    GetOperationsRequest, GetOperationsResponse
from contracts.services.gateway.operations.rpc_get_operation_receipt_pb2 import \
    GetOperationReceiptRequest, GetOperationReceiptResponse
from contracts.services.gateway.operations.rpc_get_operations_summary_pb2 import \
    GetOperationsSummaryRequest, GetOperationsSummaryResponse
from contracts.services.gateway.operations.rpc_make_fee_operation_pb2 import \
    MakeFeeOperationRequest, MakeFeeOperationResponse
from contracts.services.gateway.operations.rpc_make_top_up_operation_pb2 import \
    MakeTopUpOperationRequest, MakeTopUpOperationResponse
from contracts.services.gateway.operations.rpc_make_cashback_operation_pb2 import \
    MakeCashbackOperationRequest, MakeCashbackOperationResponse
from contracts.services.gateway.operations.rpc_make_purchase_operation_pb2 import \
    MakePurchaseOperationRequest, MakePurchaseOperationResponse
from contracts.services.gateway.operations.rpc_make_transfer_operation_pb2 import \
    MakeTransferOperationRequest, MakeTransferOperationResponse
from contracts.services.gateway.operations.rpc_make_bill_payment_operation_pb2 import \
    MakeBillPaymentOperationRequest, MakeBillPaymentOperationResponse
from contracts.services.gateway.operations.rpc_make_cash_withdrawal_operation_pb2 import \
    MakeCashWithdrawalOperationRequest, MakeCashWithdrawalOperationResponse
from tools.fakers import fake


class OperationsGatewayGRPCClient(GRPCClient):
    """A client for interacting with the Operations Gateway gRPC service.

    Provides methods for making operations and retrieving operations information.
    """

    def __init__(self, channel: Channel):
        """Initialize an OperationsGatewayGRPCClient with the given channel.

        :param channel: A grpc.Channel to connect to this client in.
        """
        super().__init__(channel=channel)

        self.stub = OperationsGatewayServiceStub(channel=channel)

    def get_operation_api(self, request: GetOperationRequest) -> GetOperationResponse:
        """Retrieves an operation information via gRPC call."""
        return self.stub.GetOperation(request=request)

    def get_operations_api(self, request: GetOperationsRequest) -> GetOperationsResponse:
        """Retrieves information about operations via gRPC call."""
        return self.stub.GetOperations(request=request)

    def get_operation_receipt_api(self, request: GetOperationReceiptRequest) -> GetOperationReceiptResponse:
        """Retrieves an operation receipt via gRPC call."""
        return self.stub.GetOperationReceipt(request=request)

    def get_operations_summary_api(self, request: GetOperationsSummaryRequest) -> GetOperationsSummaryResponse:
        """Retrieves summary information about operations via gRPC call."""
        return self.stub.GetOperationsSummary(request=request)

    def make_fee_operation_api(self, request: MakeFeeOperationRequest) -> MakeFeeOperationResponse:
        """Makes a fee operation via gRPC call."""
        return self.stub.MakeFeeOperation(request=request)

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequest) -> MakeTopUpOperationResponse:
        """Makes a top-up operation via gRPC call."""
        return self.stub.MakeTopUpOperation(request=request)

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequest) -> MakeCashbackOperationResponse:
        """Makes a cashback operation via gRPC call."""
        return self.stub.MakeCashbackOperation(request=request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequest) -> MakePurchaseOperationResponse:
        """Makes a purchase operation via gRPC call."""
        return self.stub.MakePurchaseOperation(request=request)

    def make_transfer_operation_api(self, request: MakeTransferOperationRequest) -> MakeTransferOperationResponse:
        """Makes a transfer operation via gRPC call."""
        return self.stub.MakeTransferOperation(request=request)

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequest) -> \
            MakeBillPaymentOperationResponse:
        """Makes a bill payment operation via gRPC call."""
        return self.stub.MakeBillPaymentOperation(request=request)

    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalOperationRequest) -> \
            MakeCashWithdrawalOperationResponse:
        """Makes a cash withdrawal operation via gRPC call."""
        return self.stub.MakeCashWithdrawalOperation(request=request)

    def get_operation(self, operation_id: str) -> GetOperationResponse:
        """Retrieves an operation information using operation ID."""
        request = GetOperationRequest(id=operation_id)
        return self.get_operation_api(request=request)

    def get_operations(self, account_id) -> GetOperationsResponse:
        """Retrieves information about operations using account ID."""
        request = GetOperationsRequest(account_id=account_id)
        return self.get_operations_api(request=request)

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponse:
        """Retrieves an operation receipt using operation ID."""
        request = GetOperationReceiptRequest(operation_id=operation_id)
        return self.get_operation_receipt_api(request=request)

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponse:
        """Retrieves summary information about operations using account ID."""
        request = GetOperationsSummaryRequest(account_id=account_id)
        return self.get_operations_summary_api(request=request)

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeFeeOperationResponse:
        """Performs a fee transaction based on provided card and account IDs."""
        status, amount = generate_operation_details()
        request = MakeFeeOperationRequest(
            status=status,
            amount=amount,
            card_id=card_id,
            account_id=account_id
        )
        return self.make_fee_operation_api(request=request)

    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeTopUpOperationResponse:
        """Performs a top-up transaction based on provided card and account IDs."""
        status, amount = generate_operation_details()
        request = MakeTopUpOperationRequest(
            status=status,
            amount=amount,
            card_id=card_id,
            account_id=account_id
        )
        return self.make_top_up_operation_api(request=request)

    def make_cashback_operation(self, card_id: str, account_id: str) -> MakeCashbackOperationResponse:
        """Performs a cashback transaction based on provided card and account IDs."""
        status, amount = generate_operation_details()
        request = MakeCashbackOperationRequest(
            status=status,
            amount=amount,
            card_id=card_id,
            account_id=account_id
        )
        return self.make_cashback_operation_api(request=request)

    def make_purchase_operation(self, card_id: str, account_id: str) -> MakePurchaseOperationResponse:
        """Performs a purchase transaction based on provided card and account IDs."""
        status, amount = generate_operation_details()
        request = MakePurchaseOperationRequest(
            status=status,
            amount=amount,
            card_id=card_id,
            category=fake.category(),
            account_id=account_id
        )
        return self.make_purchase_operation_api(request=request)

    def make_transfer_operation(self, card_id: str, account_id: str) -> MakeTransferOperationResponse:
        """Performs a transfer transaction based on provided card and account IDs."""
        status, amount = generate_operation_details()
        request = MakeTransferOperationRequest(
            status=status,
            amount=amount,
            card_id=card_id,
            account_id=account_id
        )
        return self.make_transfer_operation_api(request=request)

    def make_bill_payment_operation(self, card_id: str, account_id: str) -> MakeBillPaymentOperationResponse:
        """Performs a bill payment transaction based on provided card and account IDs."""
        status, amount = generate_operation_details()
        request = MakeBillPaymentOperationRequest(
            status=status,
            amount=amount,
            card_id=card_id,
            account_id=account_id
        )
        return self.make_bill_payment_operation_api(request=request)

    def make_cash_withdrawal_operation(self, card_id: str, account_id: str) -> MakeCashWithdrawalOperationResponse:
        """Performs a cash withdrawal transaction based on provided card and account IDs."""
        status, amount = generate_operation_details()
        request = MakeCashWithdrawalOperationRequest(
            status=status,
            amount=amount,
            card_id=card_id,
            account_id=account_id
        )
        return self.make_cash_withdrawal_operation_api(request=request)


def generate_operation_details() -> tuple[OperationStatus, float]:
    """Generates random operation status and amount."""
    status = fake.proto_enum_choice(OperationStatus)
    amount = fake.amount()
    return status, amount


def build_operations_gateway_grpc_client():
    """Creates and returns an OperationsGatewayGRPCClient instance.

    This function acts as a factory for creating a client connected
    to the Operations Gateway service.
    """
    return OperationsGatewayGRPCClient(channel=build_gateway_grpc_client())
