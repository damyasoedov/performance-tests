from grpc import Channel, insecure_channel


def build_gateway_grpc_client() -> Channel:
    """Factory function (builder) for creating a gRPC channel to the grpc-gateway service.

        :return: A gRPC channel (Channel) configured to connect to localhost:9003.
    """
    # Create an insecure (non-TLS) connection to the gRPC server at localhost:9003
    return insecure_channel('localhost:9003')
