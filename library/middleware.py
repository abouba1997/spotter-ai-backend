import time
import logging


logger = logging.getLogger(__name__)


class RequestTimeLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        duration = time.time() - start_time

        # Logging the request time for each request
        logger.info(f"Request to {request.path} took {duration:.2f} seconds.")

        return response
