from typing import TypedDict

from httpx import Response, QueryParams

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client


class OperationDict(TypedDict):
    """
    Data structure representing an operation.

    Contains operation details.
    """
    id: str
    type: str
    status: str
    amount: float
    cardId: str
    category: str
    createdAt: str
    accountId: str


class OperationsSummaryDict(TypedDict):
    """
    Data structure representing a summary of operations.

    Contains summary information.
    """
    spentAmount: float
    receivedAmount: float
    cashbackAmount: float


class OperationReceiptDict(TypedDict):
    """
    Data structure representing a receipt of an operation.
    """
    url: str
    document: str


class GetOperationsQueryDict(TypedDict):
    """
    Data structure for a query parameters to retrieve operations.

    Contains the account ID for which operations should be retrieved.
    """
    accountId: str


class GetOperationsResponseDict(TypedDict):
    """
    Response data structure for retrieving operations.
    """
    operations: list[OperationDict]


class GetOperationsSummaryQueryDict(TypedDict):
    """
    Data structure for a query parameters to retrieve a summary of operations.

    Contains the account ID for which the summary should be retrieved.
    """
    accountId: str


class GetOperationsSummaryResponseDict(TypedDict):
    """
    Data structure for retrieving operations summary information.
    """
    summary: OperationsSummaryDict


class GetOperationReceiptResponseDict(TypedDict):
    """
    Data structure for retrieving a receipt for an operation.
    """
    receipt: OperationReceiptDict


class GetOperationResponseDict(TypedDict):
    """
    Response data structure for retrieving operation.
    """
    operation: OperationDict


class MakeOperationRequestDict(TypedDict):
    """
    Base data structure for a request to perform an operation.

    Contains common fields required for all operation types.
    """
    status: str
    amount: float
    cardId: str
    accountId: str


class MakeFeeOperationRequestDict(MakeOperationRequestDict):
    """
    Data structure for a request to perform a fee operation.

    Inherits from MakeOperationRequestDict and does not contain additional fields.
    """
    ...


class MakeFeeOperationResponseDict(TypedDict):
    """
    Response data structure for making a fee operation.
    """
    operation: OperationDict


class MakeTopUpOperationRequestDict(MakeOperationRequestDict):
    """
    Data structure for a request to perform a top-up operation.

    Inherits from MakeOperationRequestDict and does not contain additional fields.
    """
    ...


class MakeTopUpOperationResponseDict(TypedDict):
    """
    Response data structure for making a top-up operation.
    """
    operation: OperationDict


class MakeCashbackOperationRequestDict(MakeOperationRequestDict):
    """
    Data structure for a request to perform a cashback operation.

    Inherits from MakeOperationRequestDict and does not contain additional fields.
    """
    ...


class MakeCashbackOperationResponseDict(TypedDict):
    """
    Response data structure for making a cashback operation.
    """
    operation: OperationDict


class MakeTransferOperationRequestDict(MakeOperationRequestDict):
    """
    Data structure for a request to perform a transfer operation.

    Inherits from MakeOperationRequestDict and does not contain additional fields.
    """
    ...


class MakeTransferOperationResponseDict(TypedDict):
    """
    Response data structure for making a transfer operation.
    """
    operation: OperationDict


class MakePurchaseOperationRequestDict(MakeOperationRequestDict):
    """
    Data structure for a request to perform a purchase operation.

    Inherits from MakeOperationRequestDict and contains additional field for purchase category.
    """
    category: str


class MakePurchaseOperationResponseDict(TypedDict):
    """
    Response data structure for making a purchase operation.
    """
    operation: OperationDict


class MakeBillPaymentOperationRequestDict(MakeOperationRequestDict):
    """
    Data structure for a request to perform a bill payment operation.

    Inherits from MakeOperationRequestDict and does not contain additional fields.
    """
    ...


class MakeBillPaymentOperationResponseDict(TypedDict):
    """
    Response data structure for making a bill payment operation.
    """
    operation: OperationDict


class MakeCashWithdrawalOperationRequestDict(MakeOperationRequestDict):
    """
    Data structure for a request to perform a cash withdrawal operation.

    Inherits from MakeOperationRequestDict and does not contain additional fields.
    """
    ...


class MakeCashWithdrawalOperationResponseDict(TypedDict):
    """
    Response data structure for making a cash withdrawal operation.
    """
    operation: OperationDict


class OperationsGatewayHTTPClient(HTTPClient):

    def get_operations_api(self, query: GetOperationsQueryDict) -> Response:
        """
        Retrieves a list of operations

        :param query: Query parameters for filtering operations.
        :return: Server response with operations list information.
        """
        return self.get(url='/api/v1/operations', params=QueryParams(**query))

    def get_operations_summary_api(self, query: GetOperationsSummaryQueryDict):
        """
        Retrieves a summary of operations for the specified account ID.

        :param query: Query parameters for filtering operations summary.
        :return: HTTP response containing the operations summary information.
        """
        return self.get(url='/api/v1/operations/operations-summary', params=QueryParams(**query))

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Retrieves the receipt of a specific operation by its ID.

        :param operation_id: The ID of the operation to retrieve.
        :return: HTTP response containing the receipt information.
        """
        return self.get(url=f'/api/v1/operations/operation-receipt/{operation_id}')

    def get_operation_api(self, operation_id: int) -> Response:
        """
        Retrieves a specific operation by its ID.

        :param operation_id: Unique ID of the operation to retrieve.
        :return: HTTP response containing the operation details.
        """
        return self.get(url=f'/api/v1/operations/{operation_id}')

    def make_fee_operation_api(self, payload: MakeFeeOperationRequestDict) -> Response:
        """
        Creates a fee operation.

        :param payload: Request payload containing fee operation details.
        :return: HTTP response confirming the fee operation creation.
        """
        return self.post(url='/api/v1/operations/make-fee-operation', payload=payload)

    def make_top_up_operation_api(self, payload: MakeTopUpOperationRequestDict) -> Response:
        """
        Creates a top-up operation.

        :param payload: Request payload containing top-up operation details.
        :return: HTTP response confirming the top-up operation creation.
        """
        return self.post(url='/api/v1/operations/make-top-up-operation', payload=payload)

    def make_cashback_operation_api(self, payload: MakeCashbackOperationRequestDict) -> Response:
        """
        Creates a cashback operation.

        :param payload: Request payload containing cashback operation details.
        :return: HTTP response confirming the cashback operation creation.
        """
        return self.post(url='/api/v1/operations/make-cashback-operation', payload=payload)

    def make_transfer_operation_api(self, payload: MakeTransferOperationRequestDict) -> Response:
        """
        Creates a transfer operation.

        :param payload: Request payload containing transfer operation details.
        :return: HTTP response confirming the transfer operation creation.
        """
        return self.post(url='/api/v1/operations/make-transfer-operation', payload=payload)

    def make_purchase_operation_api(self, payload: MakePurchaseOperationRequestDict):
        """
        Creates a purchase operation.

        :param payload: Request payload containing purchase operation details.
        :return: HTTP response confirming the purchase operation creation.
        """
        return self.post(url='/api/v1/operations/make-purchase-operation', payload=payload)

    def make_bill_payment_operation_api(self, payload: MakeBillPaymentOperationRequestDict):
        """
        Creates a bill payment operation.

        :param payload: Request payload containing bill payment operation details.
        :return: HTTP response confirming the bill payment operation creation.
        """
        return self.post(url='/api/v1/operations/make-bill-payment-operation', payload=payload)

    def make_cash_withdrawal_operation_api(self, payload: MakeCashWithdrawalOperationRequestDict):
        """
        Creates a cash withdrawal operation.

        :param payload: Request payload containing cash withdrawal operation details.
        :return: HTTP response confirming the cash withdrawal operation creation.
        """
        return self.post(url='/api/v1/operations/make-cash-withdrawal-operation', payload=payload)

    def get_operations(self, account_id: str) -> GetOperationsResponseDict:
        """
        Retrieves a list of all operations associated with a given account ID.
        :param account_id:
        :return:
        """
        query = GetOperationsQueryDict(accountId=account_id)
        response = self.get_operations_api(query=query)
        return response.json()

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponseDict:
        """
        Retrieves a summary of operations associated with a given account ID.
        :param account_id: The account ID to retrieve summary for.
        :return: A TypedDict containing the summary information.
        """
        query = GetOperationsSummaryQueryDict(accountId=account_id)
        response = self.get_operations_summary_api(query=query)
        return response.json()

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponseDict:
        """
        Retrieves the receipt for an operation by the given operation ID.

        :param operation_id: The operation ID to retrieve receipt for.
        :return: A TypedDict containing the receipt information.
        """
        response = self.get_operation_receipt_api(operation_id=operation_id)
        return response.json()

    def get_operation(self, operation_id) -> GetOperationResponseDict:
        """
        Retrieves the details of an operation by the given operation ID.

        :param operation_id: The operation ID to retrieve details for.
        :return: A TypedDict containing the operation details.
        """
        response = self.get_operation_api(operation_id=operation_id)
        return response.json()

    @staticmethod
    def create_base_payload(card_id: str, account_id: str):
        return {
            'status': 'COMPLETED',
            'amount': 100.55,
            'cardId': card_id,
            'accountId': account_id
        }

    def make_fee_operation(
            self, card_id: str, account_id: str
    ) -> MakeFeeOperationResponseDict:
        """
        Creates a fee operation.
        :param card_id: The card ID to create fee operation for.
        :param account_id: The account ID to create fee operation for.
        :return: A TypedDict containing the fee operation details.
        """
        base_payload = self.create_base_payload(card_id=card_id, account_id=account_id)
        request_payload = MakeFeeOperationRequestDict(**base_payload)
        response = self.make_fee_operation_api(payload=request_payload)
        return response.json()

    def make_top_up_operation(
            self, card_id: str, account_id: str
    ) -> MakeTopUpOperationResponseDict:
        """
        Creates a top-up operation.

        :param card_id: The card ID to create top up operation for.
        :param account_id: The account ID to create top up operation for.
        :return: A TypedDict containing the top-up operation details.
        """
        base_payload = self.create_base_payload(card_id=card_id, account_id=account_id)
        request_payload = MakeTopUpOperationRequestDict(**base_payload)
        response = self.make_top_up_operation_api(payload=request_payload)
        return response.json()

    def make_cashback_operation(
            self, card_id: str, account_id: str
    ) -> MakeCashbackOperationResponseDict:
        """
        Creates a cashback operation.

        :param card_id: The card ID to create cashback operation for.
        :param account_id: The account ID to create cashback operation for.
        :return: A TypedDict containing the cashback operation details.
        """
        base_payload = self.create_base_payload(card_id=card_id, account_id=account_id)
        request_payload = MakeCashbackOperationRequestDict(**base_payload)
        response = self.make_cashback_operation_api(payload=request_payload)
        return response.json()

    def make_transfer_operation(
            self, card_id: str, account_id: str
    ) -> MakeTransferOperationResponseDict:
        """
        Creates a transfer operation.

        :param card_id: The card ID to create transfer operation for.
        :param account_id: The account ID to create transfer operation for.
        :return: A TypedDict containing the transfer operation details.
        """
        base_payload = self.create_base_payload(card_id=card_id, account_id=account_id)
        request_payload = MakeTransferOperationRequestDict(**base_payload)
        response = self.make_transfer_operation_api(payload=request_payload)
        return response.json()

    def make_purchase_operation(
            self, card_id: str, account_id: str
    ) -> MakePurchaseOperationResponseDict:
        """
        Creates a purchase operation.

        :param card_id: The card ID to create purchase operation for.
        :param account_id: The account ID to create purchase operation for.
        :return: A TypedDict containing the purchase operation details.
        """
        base_payload = self.create_base_payload(card_id=card_id, account_id=account_id)
        purchase_payload = base_payload | {'amount': 10.55, 'category': 'CINEMA'}
        request_payload = MakePurchaseOperationRequestDict(**purchase_payload)
        response = self.make_purchase_operation_api(payload=request_payload)
        return response.json()

    def make_bill_payment_operation(
            self, card_id: str, account_id: str
    ) -> MakeBillPaymentOperationResponseDict:
        """
        Creates a bill payment operation.

        :param card_id: The card ID to create bill payment operation for.
        :param account_id: The account ID to create bill payment operation for.
        :return: A TypedDict containing the bill payment operation details.
        """
        base_payload = self.create_base_payload(card_id=card_id, account_id=account_id)
        request_payload = MakeBillPaymentOperationRequestDict(**base_payload)
        response = self.make_bill_payment_operation_api(payload=request_payload)
        return response.json()

    def make_cash_withdrawal_operation(
            self, card_id: str, account_id: str
    ) -> MakeCashWithdrawalOperationResponseDict:
        """
        Creates a cash withdrawal operation.

        :param card_id: The card ID to create cash withdrawal operation for.
        :param account_id: The account ID to create cash withdrawal operation for.
        :return: A TypedDict containing the cash withdrawal operation details.
        """
        base_payload = self.create_base_payload(card_id=card_id, account_id=account_id)
        request_payload = MakeCashWithdrawalOperationRequestDict(**base_payload)
        response = self.make_cash_withdrawal_operation_api(payload=request_payload)
        return response.json()


def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Builds and returns an OperationsGatewayHTTPClient instance.

    Uses the build_gateway_http_client function to create an underlying http client.
    :return: An instance of OperationsGatewayHTTPClient.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())
