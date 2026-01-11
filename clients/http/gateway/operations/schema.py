from pydantic import BaseModel, Field, HttpUrl, ConfigDict
from enum import StrEnum
from datetime import datetime


class OperationType(StrEnum):
    FEE = "FEE"
    TOP_UP = "TOP_UP"
    PURCHASE = "PURCHASE"
    CASHBACK = "CASHBACK"
    TRANSFER = "TRANSFER"
    BILL_PAYMENT = "BILL_PAYMENT"
    CASH_WITHDRAWAL = "CASH_WITHDRAWAL"


class OperationStatus(StrEnum):
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
    IN_PROGRESS = "IN_PROGRESS"
    UNSPECIFIED = "UNSPECIFIED"

class OperationSchema(BaseModel):
    """
    Data structure representing an operation.

    Contains operation details.
    """
    id: str
    type: OperationType
    status: OperationStatus
    amount: float
    card_id: str = Field(alias='cardId')
    category: str
    created_at: datetime = Field(alias='createdAt')
    account_id: str = Field(alias='accountId')


class OperationsSummarySchema(BaseModel):
    """
    Data structure representing a summary of operations.

    Contains summary information.
    """
    spent_amount: float = Field(alias='spentAmount')
    received_amount: float = Field(alias='receivedAmount')
    cashback_amount: float = Field(alias='cashbackAmount')


class OperationReceiptSchema(BaseModel):
    """
    Data structure representing a receipt of an operation.
    """
    url: HttpUrl
    document: str


class GetOperationsQuerySchema(BaseModel):
    """
    Data structure for a query parameters to retrieve operations.

    Contains the account ID for which operations should be retrieved.
    """
    account_id: str = Field(alias='accountId')


class GetOperationsResponseSchema(BaseModel):
    """
    Response data structure for retrieving operations.
    """
    operations: list[OperationSchema]


class GetOperationsSummaryQuerySchema(BaseModel):
    """
    Data structure for a query parameters to retrieve a summary of operations.

    Contains the account ID for which the summary should be retrieved.
    """
    account_id: str = Field(alias='accountId')


class GetOperationsSummaryResponseSchema(BaseModel):
    """
    Data structure for retrieving operations summary information.
    """
    summary: OperationsSummarySchema


class GetOperationReceiptResponseSchema(BaseModel):
    """
    Data structure for retrieving a receipt for an operation.
    """
    receipt: OperationReceiptSchema


class GetOperationResponseSchema(BaseModel):
    """
    Response data structure for retrieving operation.
    """
    operation: OperationSchema


class MakeOperationRequestSchema(BaseModel):
    """
    Base data structure for a request to perform an operation.

    Contains common fields required for all operation types.
    """
    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus
    amount: float
    card_id: str = Field(alias='cardId')
    account_id: str = Field(alias='accountId')


class MakeFeeOperationRequestSchema(MakeOperationRequestSchema):
    """
    Data structure for a request to perform a fee operation.

    Inherits from MakeOperationRequestSchema and does not contain additional fields.
    """
    ...


class MakeFeeOperationResponseSchema(BaseModel):
    """
    Response data structure for making a fee operation.
    """
    operation: OperationSchema


class MakeTopUpOperationRequestSchema(MakeOperationRequestSchema):
    """
    Data structure for a request to perform a top-up operation.

    Inherits from MakeOperationRequestSchema and does not contain additional fields.
    """
    ...


class MakeTopUpOperationResponseSchema(BaseModel):
    """
    Response data structure for making a top-up operation.
    """
    operation: OperationSchema


class MakeCashbackOperationRequestSchema(MakeOperationRequestSchema):
    """
    Data structure for a request to perform a cashback operation.

    Inherits from MakeOperationRequestSchema and does not contain additional fields.
    """
    ...


class MakeCashbackOperationResponseSchema(BaseModel):
    """
    Response data structure for making a cashback operation.
    """
    operation: OperationSchema


class MakeTransferOperationRequestSchema(MakeOperationRequestSchema):
    """
    Data structure for a request to perform a transfer operation.

    Inherits from MakeOperationRequestSchema and does not contain additional fields.
    """
    ...


class MakeTransferOperationResponseSchema(BaseModel):
    """
    Response data structure for making a transfer operation.
    """
    operation: OperationSchema


class MakePurchaseOperationRequestSchema(MakeOperationRequestSchema):
    """
    Data structure for a request to perform a purchase operation.

    Inherits from MakeOperationRequestSchema and contains additional field for purchase category.
    """
    category: str


class MakePurchaseOperationResponseSchema(BaseModel):
    """
    Response data structure for making a purchase operation.
    """
    operation: OperationSchema


class MakeBillPaymentOperationRequestSchema(MakeOperationRequestSchema):
    """
    Data structure for a request to perform a bill payment operation.

    Inherits from MakeOperationRequestSchema and does not contain additional fields.
    """
    ...


class MakeBillPaymentOperationResponseSchema(BaseModel):
    """
    Response data structure for making a bill payment operation.
    """
    operation: OperationSchema


class MakeCashWithdrawalOperationRequestSchema(MakeOperationRequestSchema):
    """
    Data structure for a request to perform a cash withdrawal operation.

    Inherits from MakeOperationRequestSchema and does not contain additional fields.
    """
    ...


class MakeCashWithdrawalOperationResponseSchema(BaseModel):
    """
    Response data structure for making a cash withdrawal operation.
    """
    operation: OperationSchema
