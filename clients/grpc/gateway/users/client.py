from grpc import Channel

from clients.grpc.client import GRPCClient
from clients.grpc.gateway.client import build_gateway_grpc_client
from contracts.services.gateway.users.rpc_create_user_pb2 import \
    CreateUserRequest, CreateUserResponse
from contracts.services.gateway.users.rpc_get_user_pb2 import \
    GetUserRequest, GetUserResponse
from contracts.services.gateway.users.users_gateway_service_pb2_grpc import \
    UsersGatewayServiceStub
from tools.fakers import fake


class UsersGatewayGRPCClient(GRPCClient):
    """A client for interacting with the Users Gateway gRPC service.

    This class provides methods for creating users and getting users.
    It wraps the gRPC stub for easier use.
    """
    def __init__(self, channel: Channel):
        """Initializes the client with the given channel.

        :param channel: The gRPC channel to connect to the Users Gateway service.
        """
        super().__init__(channel=channel)

        self.stub = UsersGatewayServiceStub(channel=channel)

    def create_user_api(self, request: CreateUserRequest) -> CreateUserResponse:
        """Creates a user via the gRPC API.

        Low level API for creating users and getting users.
        :param request: The CreateUserRequest object containing the user details.
        :return: The CreateUserResponse object containing the result of the user creation.
        """
        return self.stub.CreateUser(request)

    def get_user_api(self, request: GetUserRequest) -> GetUserResponse:
        """Retrieves a user via the gRPC API.

        Low level API for getting users.
        :param request: The GetUserRequest object containing the user id.
        :return: The GetUserResponse object containing the user details.
        """
        return self.stub.GetUser(request)

    def create_user(self) -> CreateUserResponse:
        """Creates a new user with randomly generated data.

        This method generates fake user data (email, name, phone number) and
        uses the gRPC API to create the user.
        :return: The CreateUserResponse object containing the result of the user creation.
        """
        request = CreateUserRequest(
            email=fake.email(),
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            middle_name=fake.middle_name(),
            phone_number=fake.phone_number(),
        )
        return self.create_user_api(request)

    def get_user(self, user_id: str) -> GetUserResponse:
        """Retrieves a user by their ID.

        :param user_id: The ID of the user to retrieve.
        :return: The GetUserResponse object containing the result of the user retrieval.
        """
        request = GetUserRequest(id=user_id)
        return self.get_user_api(request)


def build_users_gateway_grpc_client() -> UsersGatewayGRPCClient:
    """Creates and returns a UsersGatewayGRPCClient instance.

    This function acts as a factory for creating a client connected
    to the Users Gateway gRPC service.
    """
    return UsersGatewayGRPCClient(channel=build_gateway_grpc_client())
