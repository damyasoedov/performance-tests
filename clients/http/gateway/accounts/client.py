from typing import TypedDict

from httpx import Response

from clients.http.client import HTTPClient, QueryParams
from clients.http.gateway.cards.client import CardDict
from clients.http.gateway.client import build_gateway_http_client


class AccountDict(TypedDict):
    """
    Data structure representing an account.

    Containing the account details.
    """
    id: str
    type: str
    cards: list[CardDict]
    status: str
    balance: float


class GetAccountsQueryDict(TypedDict):
    """
    Data structure for query parameters to retrieve accounts.

    :param str userId: User identifier (UUID string)
    """
    userId: str


class GetAccountsResponseDict(TypedDict):
    """
    Response data structure for retrieving user accounts.

    Contains the list of user accounts.
    """
    accounts: list[AccountDict]


class OpenDepositAccountRequestDict(TypedDict):
    """
    Data structure for opening deposit account.
    """
    userId: str


class OpenDepositAccountResponseDict(TypedDict):
    """
    Response data structure for opening deposit account.
    """
    account: AccountDict


class OpenSavingsAccountRequestDict(TypedDict):
    """
    Data structure for opening savings account.
    """
    userId: str


class OpenSavingsAccountResponseDict(TypedDict):
    """
    Response data structure for opening savings account.
    """
    account: AccountDict


class OpenDebitCardAccountRequestDict(TypedDict):
    """
    Data structure for opening debit card account
    """
    userId: str


class OpenDebitCardAccountResponseDict(TypedDict):
    """
    Response data structure for opening debit card account.
    """
    account: AccountDict


class OpenCreditCardAccountRequestDict(TypedDict):
    """
    Data structure for opening credit card account
    """
    userId: str


class OpenCreditCardAccountResponseDict(TypedDict):
    """
    Response data structure for opening credit card account.
    """
    account: AccountDict


class AccountsGatewayHTTPClient(HTTPClient):
    """
    Class for interacting with the Accounts API

    Provides methods for creating different types of accounts and retrieving accounts.
    """

    def get_accounts_api(self, query: GetAccountsQueryDict) -> Response:
        """
        Retrieves a list of user accounts via GET request
        :param query: A dictionary containing query parameters for filtering accounts.
                      See :class: ``GetAccountsQueryDict`` for details
        :return: The HTTP response object. Accounts data is available in the ``response.json()`` method.
        """
        return self.get(url='/api/v1/accounts', params=QueryParams(**query))

    def open_deposit_account_api(self, payload: OpenDepositAccountRequestDict) -> Response:
        """
        Opens a deposit account via raw API endpoint.

        :param payload: Request data for opening a deposit account
        :return: The server response(httpx.Response object with the account data)
        """
        return self.post(url='/api/v1/accounts/open-deposit-account', payload=payload)

    def open_savings_account_api(self, payload: OpenSavingsAccountRequestDict) -> Response:
        """
        Opens a savings account via raw API endpoint.
        :param payload: Request data for opening a savings account
        :return: The server response(httpx.Response object with the account data)
        """
        return self.post(url='/api/v1/accounts/open-savings-account', payload=payload)

    def open_debit_card_account_api(self, payload: OpenDebitCardAccountRequestDict) -> Response:
        """
        Opens a debit card account via raw API endpoint.
        :param payload: Request data for opening a debit card account.
        :return: The server response(httpx.Response object).
        """
        return self.post(url='/api/v1/accounts/open-debit-card-account', payload=payload)

    def open_credit_card_account_api(self, payload: OpenCreditCardAccountRequestDict) -> Response:
        """
        Opens a credit card account via raw API endpoint.
        :param payload: Request data for opening a credit card account.
        :return: The server response(httpx.Response object).
        """
        return self.post(url='/api/v1/accounts/open-credit-card-account', payload=payload)

    def get_accounts(self, user_id: str) -> GetAccountsResponseDict:
        """
        Retrieves a list of user accounts by user id.

        :param user_id: The ID of the user to retrieve accounts for.
        :return: A TypedDict object containing the user accounts data.
        """
        query = GetAccountsQueryDict(userId=user_id)
        response = self.get_accounts_api(query=query)
        return response.json()

    def open_deposit_account(self, user_id: str) -> OpenDepositAccountResponseDict:
        """
        Creates a new deposit account and returns the account details.

        :param user_id: The ID of the user to create the deposit account for.
        :return: A TypedDict object containing the deposit account details.
        """
        payload = OpenDepositAccountRequestDict(userId=user_id)
        response = self.open_deposit_account_api(payload=payload)
        return response.json()

    def open_savings_account(self, user_id: str) -> OpenSavingsAccountResponseDict:
        """
        Creates a new savings account and returns the account details.

        :param user_id: The ID of the user to create the savings account for.
        :return: A TypedDict object containing the savings account details.
        """
        payload = OpenSavingsAccountRequestDict(userId=user_id)
        response = self.open_savings_account_api(payload=payload)
        return response.json()

    def open_debit_card_account(self, user_id: str) -> OpenDebitCardAccountResponseDict:
        """
        Creates a new debit card account and returns the account details.

        :param user_id: The ID of the user to create the debit card account for.
        :return: A TypedDict object containing the debit card account details.
        """
        payload = OpenDebitCardAccountRequestDict(userId=user_id)
        response = self.open_debit_card_account_api(payload=payload)
        return response.json()

    def open_credit_card_account(self, user_id: str) -> OpenCreditCardAccountResponseDict:
        """
        Creates a new credit card account and returns the account details.

        :param user_id: The ID of the user to create the credit card account for.
        :return: A TypedDict object containing the credit card account details.
        """
        payload = OpenCreditCardAccountRequestDict(userId=user_id)
        response = self.open_credit_card_account_api(payload=payload)
        return response.json()


def build_accounts_gateway_http_client() -> AccountsGatewayHTTPClient:
    """
    Builds and returns an AccountsGatewayHTTPClient instance.

    Uses the build_gateway_http_client function to create an underlying http client.
    :return: An instance of the AccountsGatewayHTTPClient.
    """
    return AccountsGatewayHTTPClient(client=build_gateway_http_client())
