import logging

from httpx import Client
from locust.env import Environment

from clients.http.event_hooks.locust_event_hook import \
    locust_request_event_hook, locust_response_event_hook

def build_gateway_http_client() -> Client:
    """The function creates an instance of httpx.Client with basic settings
       for the http-gateway service.

    :return: A ready-to-use httpx.Client object.
    """
    return Client(base_url='http://localhost:8003', timeout=90)

def build_gateway_locust_http_client(environment: Environment) -> Client:
    """An HTTP client designed specifically for load testing with Locust.

    Differs from a regular client in that:

    adds the locust_request_event_hook to record the start time of the request,
    adds the locust_response_event_hook, which calculates metrics(response time,
    response length, etc.) and sends them to Locust via environment.events.request.
    Thus, this client automatically reports statistics to Locust after each executed HTTP request.
    :param environment: The Locust environment object, required for generating metric events.
    :return: An httpx.Client with hooks attached for load testing.
    """
    logging.getLogger('httpx').setLevel(logging.WARNING)
    return Client(base_url='http://localhost:8003', timeout=90,
                  event_hooks={'request': [locust_request_event_hook],
                               'response': [locust_response_event_hook(environment)]}
                  )
