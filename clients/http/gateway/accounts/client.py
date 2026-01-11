from httpx import Response

from clients.http.client import HTTPClient, QueryParams
from clients.http.gateway.accounts.schema import (
    GetAccountsQuerySchema,
    GetAccountsResponseSchema,
    OpenCreditCardAccountRequestSchema,
    OpenCreditCardAccountResponseSchema,
    OpenDebitCardAccountRequestSchema,
    OpenDebitCardAccountResponseSchema,
    OpenDepositAccountRequestSchema,
    OpenDepositAccountResponseSchema,
    OpenSavingsAccountRequestSchema,
    OpenSavingsAccountResponseSchema,
)
from clients.http.gateway.client import build_gateway_http_client


class AccountsGatewayHTTPClient(HTTPClient):
    """
    Class for interacting with the Accounts API

    Provides methods for creating different types of accounts and retrieving accounts.
    """

    def get_accounts_api(self, query: GetAccountsQuerySchema) -> Response:
        """
        Retrieves a list of user accounts via GET request
        :param query: A dictionary containing query parameters for filtering accounts.
                      See :class: ``GetAccountsQueryDict`` for details
        :return: The HTTP response object. Accounts data is available in the ``response.json()`` method.
        """
        return self.get(
            url='/api/v1/accounts',
            params=QueryParams(**query.model_dump(by_alias=True))
        )

    def open_deposit_account_api(self, payload: OpenDepositAccountRequestSchema) -> Response:
        """
        Opens a deposit account via raw API endpoint.

        :param payload: Request data for opening a deposit account
        :return: The server response(httpx.Response object with the account data)
        """
        return self.post(
            url='/api/v1/accounts/open-deposit-account', payload=
            payload.model_dump(by_alias=True)
        )

    def open_savings_account_api(self, payload: OpenSavingsAccountRequestSchema) -> Response:
        """
        Opens a savings account via raw API endpoint.
        :param payload: Request data for opening a savings account
        :return: The server response(httpx.Response object with the account data)
        """
        return self.post(
            url='/api/v1/accounts/open-savings-account', payload=
            payload.model_dump(by_alias=True)
        )

    def open_debit_card_account_api(self, payload: OpenDebitCardAccountRequestSchema) -> Response:
        """
        Opens a debit card account via raw API endpoint.
        :param payload: Request data for opening a debit card account.
        :return: The server response(httpx.Response object).
        """
        return self.post(
            url='/api/v1/accounts/open-debit-card-account',
            payload=payload.model_dump(by_alias=True)
        )

    def open_credit_card_account_api(self, payload: OpenCreditCardAccountRequestSchema) -> Response:
        """
        Opens a credit card account via raw API endpoint.
        :param payload: Request data for opening a credit card account.
        :return: The server response(httpx.Response object).
        """
        return self.post(
            url='/api/v1/accounts/open-credit-card-account',
            payload=payload.model_dump(by_alias=True)
        )

    def get_accounts(self, user_id: str) -> GetAccountsResponseSchema:
        """
        Retrieves a list of user accounts by user id.

        :param user_id: The ID of the user to retrieve accounts for.
        :return: A response schema containing the user accounts data.
        """
        query = GetAccountsQuerySchema(user_id=user_id)
        response = self.get_accounts_api(query=query)
        return GetAccountsResponseSchema.model_validate_json(response.text)

    def open_deposit_account(self, user_id: str) -> OpenDepositAccountResponseSchema:
        """
        Creates a new deposit account and returns the account details.

        :param user_id: The ID of the user to create the deposit account for.
        :return: A response schema containing the deposit account details.
        """
        payload = OpenDepositAccountRequestSchema(user_id=user_id)
        response = self.open_deposit_account_api(payload=payload)
        return OpenDepositAccountResponseSchema.model_validate_json(response.text)

    def open_savings_account(self, user_id: str) -> OpenSavingsAccountResponseSchema:
        """
        Creates a new savings account and returns the account details.

        :param user_id: The ID of the user to create the savings account for.
        :return: A response schema containing the savings account details.
        """
        payload = OpenSavingsAccountRequestSchema(user_id=user_id)
        response = self.open_savings_account_api(payload=payload)
        return OpenSavingsAccountResponseSchema.model_validate_json(response.text)

    def open_debit_card_account(self, user_id: str) -> OpenDebitCardAccountResponseSchema:
        """
        Creates a new debit card account and returns the account details.

        :param user_id: The ID of the user to create the debit card account for.
        :return: A response schema containing the debit card account details.
        """
        payload = OpenDebitCardAccountRequestSchema(user_id=user_id)
        response = self.open_debit_card_account_api(payload=payload)
        return OpenDebitCardAccountResponseSchema.model_validate_json(response.text)

    def open_credit_card_account(self, user_id: str) -> OpenCreditCardAccountResponseSchema:
        """
        Creates a new credit card account and returns the account details.

        :param user_id: The ID of the user to create the credit card account for.
        :return: A response schema containing the credit card account details.
        """
        payload = OpenCreditCardAccountRequestSchema(user_id=user_id)
        response = self.open_credit_card_account_api(payload=payload)
        return OpenCreditCardAccountResponseSchema.model_validate_json(response.text)


def build_accounts_gateway_http_client() -> AccountsGatewayHTTPClient:
    """
    Builds and returns an AccountsGatewayHTTPClient instance.

    Uses the build_gateway_http_client function to create an underlying http client.
    :return: An instance of the AccountsGatewayHTTPClient.
    """
    return AccountsGatewayHTTPClient(client=build_gateway_http_client())
