from clients.http.gateway.accounts.client import build_accounts_gateway_http_client
from clients.http.gateway.cards.client import build_cards_gateway_http_client
from clients.http.gateway.users.client import build_users_gateway_http_client

users_gateway_client = build_users_gateway_http_client()
cards_gateway_client = build_cards_gateway_http_client()
accounts_gateway_client = build_accounts_gateway_http_client()

create_user_data = users_gateway_client.create_user()
print('Create user data:', create_user_data)

user_id = create_user_data.user.id
open_debit_card_account_response = accounts_gateway_client.open_debit_card_account(user_id)
print('Open debit card account response:', open_debit_card_account_response)

account_id = open_debit_card_account_response.account.id
issue_physical_card_response = cards_gateway_client.issue_physical_card(user_id, account_id)
print('Issue physical card response:', issue_physical_card_response)
