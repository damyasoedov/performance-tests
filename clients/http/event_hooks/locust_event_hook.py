import time
from typing import Callable

from httpx import Request, Response, HTTPStatusError, HTTPError
from locust.env import Environment


def locust_request_event_hook(request: Request) -> None:
    """HTTPX event hook invoked before sending a request.

    Saves the current time to request.extensions["start_time"]
    for later use in calculating the response time.
    """
    request.extensions["start_time"] = time.time()


def locust_response_event_hook(environment: Environment) -> Callable[..., None]:
    """Returns an HTTPX event hook that is called after receiving a response.

    Uses request.extensions["start_time"] to calculate the response time.
    Extracts the route from request.extensions["route"] if it is set.
    Sends the collected metrics to environment.events.request so that
    Locust can aggregate statistics.
    :param environment: The Locust environment object through which metrics
                        are sent.
    :return: A hook function for the HTTPX response event.
    """
    def inner(response: Response) -> None:
        exception: HTTPError | HTTPStatusError | None = None
        try:
            response = response.raise_for_status()
        except (HTTPError, HTTPStatusError) as error:
            exception = error

        request = response.request

        route = request.extensions.get("route", request.url.path)
        start_time = request.extensions.get("start_time", time.time())
        response_time = (time.time() - start_time) * 1000
        response_length = len(response.read())
        environment.events.request.fire(
            name=f'{request.method} {route}',
            context=None,
            response=response,
            exception=exception,
            request_type='HTTP',
            response_time=response_time,
            response_length=response_length,
        )

    return inner
