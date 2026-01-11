from httpx import Response, QueryParams

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client
from clients.http.gateway.operations.schema import (
    OperationStatus,
    GetOperationResponseSchema,
    GetOperationsQuerySchema,
    GetOperationsResponseSchema,
    GetOperationsSummaryQuerySchema,
    GetOperationsSummaryResponseSchema,
    GetOperationReceiptResponseSchema,
    MakeBillPaymentOperationRequestSchema,
    MakeBillPaymentOperationResponseSchema,
    MakeCashbackOperationRequestSchema,
    MakeCashbackOperationResponseSchema,
    MakeCashWithdrawalOperationRequestSchema,
    MakeCashWithdrawalOperationResponseSchema,
    MakeFeeOperationRequestSchema,
    MakeFeeOperationResponseSchema,
    MakePurchaseOperationRequestSchema,
    MakePurchaseOperationResponseSchema,
    MakeTopUpOperationRequestSchema,
    MakeTopUpOperationResponseSchema,
    MakeTransferOperationRequestSchema,
    MakeTransferOperationResponseSchema,
)


class OperationsGatewayHTTPClient(HTTPClient):

    def get_operations_api(self, query: GetOperationsQuerySchema) -> Response:
        """
        Retrieves a list of operations

        :param query: Query parameters for filtering operations.
        :return: Server response with operations list information.
        """
        return self.get(
            url='/api/v1/operations',
            params=QueryParams(**query.model_dump(by_alias=True, exclude_unset=True))
        )

    def get_operations_summary_api(
            self, query: GetOperationsSummaryQuerySchema
    ) -> Response:
        """
        Retrieves a summary of operations for the specified account ID.

        :param query: Query parameters for filtering operations summary.
        :return: HTTP response containing the operations summary information.
        """
        return self.get(
            url='/api/v1/operations/operations-summary',
            params=QueryParams(**query.model_dump(by_alias=True))
        )

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

    def make_fee_operation_api(
            self, payload: MakeFeeOperationRequestSchema
    ) -> Response:
        """
        Creates a fee operation.

        :param payload: Request payload containing fee operation details.
        :return: HTTP response confirming the fee operation creation.
        """
        return self.post(
            url='/api/v1/operations/make-fee-operation',
            payload=payload.model_dump(by_alias=True)
        )

    def make_top_up_operation_api(
            self, payload: MakeTopUpOperationRequestSchema
    ) -> Response:
        """
        Creates a top-up operation.

        :param payload: Request payload containing top-up operation details.
        :return: HTTP response confirming the top-up operation creation.
        """
        return self.post(
            url='/api/v1/operations/make-top-up-operation',
            payload=payload.model_dump(by_alias=True)
        )

    def make_cashback_operation_api(
            self, payload: MakeCashbackOperationRequestSchema
    ) -> Response:
        """
        Creates a cashback operation.

        :param payload: Request payload containing cashback operation details.
        :return: HTTP response confirming the cashback operation creation.
        """
        return self.post(
            url='/api/v1/operations/make-cashback-operation',
            payload=payload.model_dump(by_alias=True)
        )

    def make_transfer_operation_api(
            self, payload: MakeTransferOperationRequestSchema
    ) -> Response:
        """
        Creates a transfer operation.

        :param payload: Request payload containing transfer operation details.
        :return: HTTP response confirming the transfer operation creation.
        """
        return self.post(
            url='/api/v1/operations/make-transfer-operation',
            payload=payload.model_dump(by_alias=True)
        )

    def make_purchase_operation_api(
            self, payload: MakePurchaseOperationRequestSchema
    ) -> Response:
        """
        Creates a purchase operation.

        :param payload: Request payload containing purchase operation details.
        :return: HTTP response confirming the purchase operation creation.
        """
        return self.post(
            url='/api/v1/operations/make-purchase-operation',
            payload=payload.model_dump(by_alias=True)
        )

    def make_bill_payment_operation_api(
            self, payload: MakeBillPaymentOperationRequestSchema
    ) -> Response:
        """
        Creates a bill payment operation.

        :param payload: Request payload containing bill payment operation details.
        :return: HTTP response confirming the bill payment operation creation.
        """
        return self.post(
            url='/api/v1/operations/make-bill-payment-operation',
            payload=payload.model_dump(by_alias=True)
        )

    def make_cash_withdrawal_operation_api(
            self, payload: MakeCashWithdrawalOperationRequestSchema
    ) -> Response:
        """
        Creates a cash withdrawal operation.

        :param payload: Request payload containing cash withdrawal operation details.
        :return: HTTP response confirming the cash withdrawal operation creation.
        """
        return self.post(
            url='/api/v1/operations/make-cash-withdrawal-operation',
            payload=payload.model_dump(by_alias=True)
        )

    def get_operations(self, account_id: str) -> GetOperationsResponseSchema:
        """
        Retrieves a list of all operations associated with a given account ID.
        :param account_id:
        :return: A response schema with list of operations.
        """
        query = GetOperationsQuerySchema(accountId=account_id)
        response = self.get_operations_api(query=query)
        return GetOperationsResponseSchema.model_validate_json(response.text)

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponseSchema:
        """
        Retrieves a summary of operations associated with a given account ID.
        :param account_id: The account ID to retrieve summary for.
        :return: A response schema containing the summary information.
        """
        query = GetOperationsSummaryQuerySchema(accountId=account_id)
        response = self.get_operations_summary_api(query=query)
        return GetOperationsSummaryResponseSchema.model_validate_json(response.text)

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponseSchema:
        """
        Retrieves the receipt for an operation by the given operation ID.

        :param operation_id: The operation ID to retrieve receipt for.
        :return: A response schema containing the receipt information.
        """
        response = self.get_operation_receipt_api(operation_id=operation_id)
        return GetOperationReceiptResponseSchema.model_validate_json(response.text)

    def get_operation(self, operation_id) -> GetOperationResponseSchema:
        """
        Retrieves the details of an operation by the given operation ID.

        :param operation_id: The operation ID to retrieve details for.
        :return: A response schema containing the operation details.
        """
        response = self.get_operation_api(operation_id=operation_id)
        return GetOperationResponseSchema.model_validate_json(response.text)

    @staticmethod
    def create_base_payload(card_id: str, account_id: str):
        return {
            'status': OperationStatus.COMPLETED,
            'amount': 100.55,
            'cardId': card_id,
            'accountId': account_id
        }

    def make_fee_operation(
            self, card_id: str, account_id: str
    ) -> MakeFeeOperationResponseSchema:
        """
        Creates a fee operation.
        :param card_id: The card ID to create fee operation for.
        :param account_id: The account ID to create fee operation for.
        :return: A response schema containing the fee operation details.
        """
        base_payload = self.create_base_payload(card_id=card_id, account_id=account_id)
        request_payload = MakeFeeOperationRequestSchema(**base_payload)
        response = self.make_fee_operation_api(payload=request_payload)
        return MakeFeeOperationResponseSchema.model_validate_json(response.text)

    def make_top_up_operation(
            self, card_id: str, account_id: str
    ) -> MakeTopUpOperationResponseSchema:
        """
        Creates a top-up operation.

        :param card_id: The card ID to create top up operation for.
        :param account_id: The account ID to create top up operation for.
        :return: A response schema containing the top-up operation details.
        """
        base_payload = self.create_base_payload(card_id=card_id, account_id=account_id)
        request_payload = MakeTopUpOperationRequestSchema(**base_payload)
        response = self.make_top_up_operation_api(payload=request_payload)
        return MakeTopUpOperationResponseSchema.model_validate_json(response.text)

    def make_cashback_operation(
            self, card_id: str, account_id: str
    ) -> MakeCashbackOperationResponseSchema:
        """
        Creates a cashback operation.

        :param card_id: The card ID to create cashback operation for.
        :param account_id: The account ID to create cashback operation for.
        :return: A response schema containing the cashback operation details.
        """
        base_payload = self.create_base_payload(card_id=card_id, account_id=account_id)
        request_payload = MakeCashbackOperationRequestSchema(**base_payload)
        response = self.make_cashback_operation_api(payload=request_payload)
        return MakeCashbackOperationResponseSchema.model_validate_json(response.text)

    def make_transfer_operation(
            self, card_id: str, account_id: str
    ) -> MakeTransferOperationResponseSchema:
        """
        Creates a transfer operation.

        :param card_id: The card ID to create transfer operation for.
        :param account_id: The account ID to create transfer operation for.
        :return: A response schema containing the transfer operation details.
        """
        base_payload = self.create_base_payload(card_id=card_id, account_id=account_id)
        request_payload = MakeTransferOperationRequestSchema(**base_payload)
        response = self.make_transfer_operation_api(payload=request_payload)
        return MakeTransferOperationResponseSchema.model_validate_json(response.text)

    def make_purchase_operation(
            self, card_id: str, account_id: str
    ) -> MakePurchaseOperationResponseSchema:
        """
        Creates a purchase operation.

        :param card_id: The card ID to create purchase operation for.
        :param account_id: The account ID to create purchase operation for.
        :return: A response schema containing the purchase operation details.
        """
        base_payload = self.create_base_payload(card_id=card_id, account_id=account_id)
        purchase_payload = base_payload | {'amount': 10.55, 'category': 'CINEMA'}
        request_payload = MakePurchaseOperationRequestSchema(**purchase_payload)
        response = self.make_purchase_operation_api(payload=request_payload)
        return MakePurchaseOperationResponseSchema.model_validate_json(response.text)

    def make_bill_payment_operation(
            self, card_id: str, account_id: str
    ) -> MakeBillPaymentOperationResponseSchema:
        """
        Creates a bill payment operation.

        :param card_id: The card ID to create bill payment operation for.
        :param account_id: The account ID to create bill payment operation for.
        :return: A response schema containing the bill payment operation details.
        """
        base_payload = self.create_base_payload(card_id=card_id, account_id=account_id)
        request_payload = MakeBillPaymentOperationRequestSchema(**base_payload)
        response = self.make_bill_payment_operation_api(payload=request_payload)
        return MakeBillPaymentOperationResponseSchema.model_validate_json(response.text)

    def make_cash_withdrawal_operation(
            self, card_id: str, account_id: str
    ) -> MakeCashWithdrawalOperationResponseSchema:
        """
        Creates a cash withdrawal operation.

        :param card_id: The card ID to create cash withdrawal operation for.
        :param account_id: The account ID to create cash withdrawal operation for.
        :return: A response schema containing the cash withdrawal operation details.
        """
        base_payload = self.create_base_payload(card_id=card_id, account_id=account_id)
        request_payload = MakeCashWithdrawalOperationRequestSchema(**base_payload)
        response = self.make_cash_withdrawal_operation_api(payload=request_payload)
        return MakeCashWithdrawalOperationResponseSchema.model_validate_json(response.text)


def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Builds and returns an OperationsGatewayHTTPClient instance.

    Uses the build_gateway_http_client function to create an underlying http client.
    :return: An instance of OperationsGatewayHTTPClient.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())
