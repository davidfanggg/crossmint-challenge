import requests
import pybreaker
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type,
    retry_if_result,
)


class HttpReliableClient:
    def __init__(self, recovery_timeout: int = 10):
        self.circuit_breaker = pybreaker.CircuitBreaker(
            fail_max=3, reset_timeout=recovery_timeout
        )

    @staticmethod
    def _is_client_error(response):
        return 400 <= response.status_code < 500

    @classmethod
    def retry_decorator(cls, func):
        return retry(
            stop=stop_after_attempt(3),
            wait=wait_exponential(multiplier=1, min=2, max=10),
            retry=(
                retry_if_exception_type(requests.RequestException)
                | retry_if_result(cls._is_client_error)
            ),
        )(func)

    def circuit_breaker_protected_decorator(self, func):
        def wrapper(*args, **kwargs):
            return self.circuit_breaker.call(func, *args, **kwargs)

        return wrapper

    def get(self, url: str, **kwargs):
        @self.retry_decorator
        @self.circuit_breaker_protected_decorator
        def _get_request():
            response = requests.get(url, **kwargs)
            response.raise_for_status()
            return response

        return _get_request()

    def post(self, url: str, data=None, json=None, **kwargs):
        @self.retry_decorator
        @self.circuit_breaker_protected_decorator
        def _post_request():
            response = requests.post(url, data=data, json=json, **kwargs)
            response.raise_for_status()
            return response

        return _post_request()

    def delete(self, url: str, **kwargs):
        @self.retry_decorator
        @self.circuit_breaker_protected_decorator
        def _delete_request():
            response = requests.delete(url, **kwargs)
            response.raise_for_status()
            return response

        return _delete_request()
