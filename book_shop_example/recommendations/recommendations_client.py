import grpc
import recommendations_pb2
# from recommendations_pb2 import BookCategory, RecommendationRequest
from recommendations_pb2_grpc import RecommendationsStub


def run():
    channel = grpc.insecure_channel('localhost:50051')

    stub = RecommendationsStub(channel)

    request = recommendations_pb2.RecommendationRequest(
        user_id=2, category=recommendations_pb2.BookCategory.SCIENCE_FICTION, max_results=2
    )
    response = stub.Recommend(request)
    print(f'Server response: {response}')


if __name__ == '__main__':
    run()
