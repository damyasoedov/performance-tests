from typing import TypedDict

from httpx import Response

from clients.http.client import HTTPClient, QueryParams


class GetAccountsQueryDict(TypedDict):
    """Query parameters for retrieving user accounts.

    :param str userId: User identifier (UUID string)
    """
    userId: str


class OpenDepositAccountRequestDict(TypedDict):
    """
    Request payload for opening deposit account
    """
    userId: str


class OpenSavingsAccountRequestDict(TypedDict):
    """
    Request payload for opening savings account
    """

    userId: str


class OpenDebitCardAccountRequestDict(TypedDict):
    """
    Request payload for opening debit card account
    """
    userId: str


class OpenCreditCardAccountRequestDict(TypedDict):
    """Request payload for opening credit card account
    """
    userId: str


class AccountsGatewayHTTPClient(HTTPClient):
    """
    Class for interacting with the Accounts API
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
        Opens a deposit account via API

        :param payload: Request data for opening a deposit account
        :return: The server response(httpx.Response object with the account data)
        """
        return self.post(url='/api/v1/accounts/open-deposit-account', payload=payload)

    def open_savings_account_api(self, payload: OpenSavingsAccountRequestDict) -> Response:
        """
        Opens a savings account via API
        :param payload: Request data for opening a savings account
        :return: The server response(httpx.Response object with the account data)
        """
        return self.post(url='/api/v1/accounts/open-savings-account', payload=payload)

    def open_debit_card_account_api(self, payload: OpenDebitCardAccountRequestDict) -> Response:
        """
        Opens a debit card account via API
        :param payload: Request data for opening a debit card account
        :return: The server response(httpx.Response object with the account data)
        """
        return self.post(url='/api/v1/accounts/open-debit-card-account', payload=payload)

    def open_credit_card_account_api(self, payload: OpenCreditCardAccountRequestDict) -> Response:
        """
        Opens a credit card account via API
        :param payload: Request data for opening a credit card account
        :return: The server response(httpx.Response object with the account data)
        """
        return self.post(url='/api/v1/accounts/open-credit-card-account', payload=payload)
