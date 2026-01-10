from clients.http.gateway.accounts.client import build_accounts_gateway_http_client
from clients.http.gateway.operations.client import build_operations_gateway_http_client
from clients.http.gateway.users.client import build_users_gateway_http_client

users_gateway_client = build_users_gateway_http_client()
accounts_gateway_client = build_accounts_gateway_http_client()
operations_gateway_client = build_operations_gateway_http_client()

create_user_data = users_gateway_client.create_user()
print('User data', create_user_data)
user_id = create_user_data['user']['id']

open_debit_card_account_response = accounts_gateway_client.open_debit_card_account(user_id)
print('Debit card account:', open_debit_card_account_response)
account_id = open_debit_card_account_response['account']['id']
card_id = open_debit_card_account_response['account']['cards'][0]['id']
print('Card id:', card_id)

make_top_up_operation_response = operations_gateway_client.make_top_up_operation(card_id=card_id, account_id=account_id)
print('Top up operation:', make_top_up_operation_response)
make_purchase_operation_response = operations_gateway_client.make_purchase_operation(card_id=card_id, account_id=account_id)
print('Purchase operation:', make_purchase_operation_response)
get_operations_response = operations_gateway_client.get_operations(account_id=account_id)
print('Operations:', get_operations_response)
get_operations_summary_response = operations_gateway_client.get_operations_summary(account_id=account_id)
print('Summary:', get_operations_summary_response)

get_accounts_response = accounts_gateway_client.get_accounts(user_id=user_id)
print('Accounts:', get_accounts_response)
