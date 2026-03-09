from concurrent import futures
import random

import grpc

import recommendations_pb2
# from recommendations_pb2 import (
#     BookCategory,
#     BookRecommendation,
#     RecommendationResponse,
# )

import recommendations_pb2_grpc

books_by_category = {
    recommendations_pb2.BookCategory.MYSTERY: [
        recommendations_pb2.BookRecommendation(id=1, title="The Maltese Falcon"),
        recommendations_pb2.BookRecommendation(id=2, title="Murder on the Orient Express"),
        recommendations_pb2.BookRecommendation(id=3, title="The Hound of the Baskervilles"),
    ],
    recommendations_pb2.BookCategory.SCIENCE_FICTION: [
        recommendations_pb2.BookRecommendation(id=4, title="The Hitchhiker's Guide to the Galaxy"),
        recommendations_pb2.BookRecommendation(id=5, title="Ender's Game"),
        recommendations_pb2.BookRecommendation(id=6, title="The Dune Chronicles")
    ],
    recommendations_pb2.BookCategory.SELF_HELP: [
        recommendations_pb2.BookRecommendation(id=7, title="The 7 Habits of Highly Effective People"),
        recommendations_pb2.BookRecommendation(id=8, title="How to Win Friends and Influence People"),
        recommendations_pb2.BookRecommendation(id=9, title="Man's Search for Meaning")
    ]
}


class RecommendationsService(recommendations_pb2_grpc.RecommendationsServicer):
    def Recommend(self, request, context):
        if request.category not in books_by_category:
            context.abort(grpc.StatusCode.NOT_FOUND, "Category not found.")

        print(f'Category {request.category}')
        print(f'BookCategory {books_by_category[request.category]}')
        books_for_category = books_by_category[request.category]
        num_results = min(request.max_results, len(books_for_category))
        books_to_recommend = random.sample(books_for_category, num_results)

        return recommendations_pb2.RecommendationResponse(recommendations=books_to_recommend)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    recommendations_pb2_grpc.add_RecommendationsServicer_to_server(
        RecommendationsService(), server
    )
    print("Starting recommendations server on port 50051...")
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
