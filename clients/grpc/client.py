import grpc.experimental.gevent as grpc_gevent

from grpc import Channel

grpc_gevent.init_gevent()

class GRPCClient:
    """Base class for a gRPC client.

    This class stores a common channel for communication with the gRPC server.
    All other specific clients will inherit from it.
    """
    def __init__(self, channel: Channel):
        """Constructor for the base client.

        :param channel: The gRPC channel used to connect to the server.
                        Typically, created once and reused.
        """
        self.channel = channel
