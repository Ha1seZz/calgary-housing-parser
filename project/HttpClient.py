import requests

class HttpClient:
    def __init__(self, base_url):
        """
        Initializes the HTTP client with a base URL and a session.
        Инициализирует HTTP-клиент с помощью базового URL-адреса и сеанса.

        :param base_url: The base URL for the HTTP requests.
        """
        self.base_url = base_url
        self.session = requests.Session()

    def get(self, url: str, params: dict=None) -> str:
        """
        Performs a GET request using the session.
        Выполняет запрос GET с использованием сеанса.

        :param url: The endpoint URL for the request.
        :param params: Optional query parameters for the request.
        :return: The response text from the server.
        :raises RuntimeError: If the request fails.
        """
        try:
            response = self.session.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            raise RuntimeError(f"HTTP request failed: {e}")

    def close(self):
        """Closes the session."""
        self.session.close()
