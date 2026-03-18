from locust import HttpUser, between, task

from tools.fakers import fake


class OpenDebitCardAccountUser(HttpUser):
    wait_time = between(1, 2)
    user_data: dict

    def on_start(self):
        request = {
            'email': fake.email(),
            'lastName': fake.last_name(),
            'firstName': fake.first_name(),
            'middleName': fake.middle_name(),
            'phoneNumber': fake.phone_number(),
        }

        response = self.client.post('/api/v1/users', json=request)
        self.user_data = response.json()

    @task
    def open_debit_card_account(self):
        request = {
            'userId': self.user_data['user']['id'],
        }
        self.client.post('/api/v1/accounts/open-debit-card-account', json=request)
