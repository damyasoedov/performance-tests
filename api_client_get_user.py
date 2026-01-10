from clients.http.gateway.users.client import build_users_gateway_http_client

users_gateway_http_client = build_users_gateway_http_client()

create_user_data = users_gateway_http_client.create_user()
print('Create user data:', create_user_data)

user_id = create_user_data['user']['id']
get_user_data = users_gateway_http_client.get_user(user_id=user_id)
print('Get user data:', get_user_data)
