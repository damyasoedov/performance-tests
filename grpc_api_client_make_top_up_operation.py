from clients.grpc.gateway.users.client import build_users_gateway_grpc_client
from clients.grpc.gateway.accounts.client import build_accounts_gateway_grpc_client
from clients.grpc.gateway.operations.client import build_operations_gateway_grpc_client

users_gateway_client = build_users_gateway_grpc_client()
create_user_response= users_gateway_client.create_user()
print(f'Create user response: {create_user_response}')

accounts_gateway_client = build_accounts_gateway_grpc_client()
open_credit_card_account_response= accounts_gateway_client.open_credit_card_account(
    user_id=create_user_response.user.id
)
print(f'Open credit card account response: {open_credit_card_account_response}')

operations_gateway_client = build_operations_gateway_grpc_client()
make_top_up_operation_response= operations_gateway_client.make_top_up_operation(
    card_id=open_credit_card_account_response.account.cards[0].id,
    account_id=open_credit_card_account_response.account.id
)
print(f'Make top up operation response: {make_top_up_operation_response}')
